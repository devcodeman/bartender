'''
Spotify widget — handles all DJ booth UI logic.
If the Spotify device is not found at startup a background timer retries
every 15 seconds until the device comes online, then initialises fully
without requiring an app restart.
'''
import os
from PySide6 import QtCore, QtWidgets
from ui.output_files.spotifyUi import Ui_SpotifyWidget
from bartender.spotify import Spotify
from bartender.thread_manager import SpotifyPlayerThread
from utils import constants

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

_RETRY_INTERVAL_MS = 15_000   # poll every 15 s until device appears


class SpotifyWidget(QtWidgets.QWidget):

    def __init__(self, nospotify: bool) -> None:
        super().__init__()
        self.view = Ui_SpotifyWidget()
        self.view.setupUi(self)
        self._nospotify = nospotify
        self.spotifyQueueThread = None
        self.localPlaybackState = False

        self.spotifyPlayer = Spotify("CODEMAN-DEV", nospotify)

        self._retry_timer = QtCore.QTimer(self)
        self._retry_timer.setInterval(_RETRY_INTERVAL_MS)
        self._retry_timer.timeout.connect(self._retry_connection)

        self._setup_dj_booth()

    # ── Connection setup / retry ──────────────────────────────────────────

    def _setup_dj_booth(self) -> None:
        if self._nospotify:
            self._show_disconnected("Spotify disabled (--nospotify)")
            return

        if self.spotifyPlayer.getDeviceId() != -1:
            self._initialise_booth()
        else:
            self._show_disconnected("Searching for device…")
            self._retry_timer.start()

    def _retry_connection(self) -> None:
        print("Retrying Spotify device connection...")
        found = self.spotifyPlayer.establishConnection(maxAttempts=1)
        if found != -1:
            self._retry_timer.stop()
            self._initialise_booth()

    def _initialise_booth(self) -> None:
        '''Wire up all controls — called once a device is confirmed found.'''
        self.view.currentlyPlayingLabel.setText("—")
        self.view.spotifySearchButton.clicked.connect(self.searchSpotify)
        self.view.spotifySearchResultsField.itemDoubleClicked.connect(
            self.selectedSearch)
        self.view.spotifyPlayPauseButton.clicked.connect(
            self.playPauseButtonClicked)
        self.view.spotifyNextButton.clicked.connect(self.nextTrack)
        self.view.spotifyPreviousButton.clicked.connect(self.previousTrack)
        self.view.spotifyTabWidget.setStyleSheet(constants.SPOTIFY_TAB_STYLE)

        if self._get_initial_playback():
            self.view.spotifyPlayPauseButton.setStyleSheet(
                constants.SPOTIFY_PLAY_STATE_STYLE)
        else:
            self.view.spotifyPlayPauseButton.setStyleSheet(
                constants.SPOTIFY_PAUSED_STATE_STYLE)

        self.spotifyQueueThread = SpotifyPlayerThread(self.spotifyPlayer.spotify)
        self.spotifyQueueThread.songChanged.connect(self.updateCurrentPlayback)
        self.spotifyQueueThread.start()
        self.updateQueueField()
        print(f"DJ booth initialised — device: {self.spotifyPlayer.getDeviceId()}")

    def _show_disconnected(self, msg: str) -> None:
        self.view.currentlyPlayingLabel.setText(msg)
        print(f"Spotify: {msg}")

    # ── Playback state ────────────────────────────────────────────────────

    def _get_initial_playback(self) -> bool:
        try:
            temp = self.spotifyPlayer.getCurrentPlayback()
            self.localPlaybackState = temp is not None
        except Exception:
            self.localPlaybackState = False
        return self.localPlaybackState

    def updateCurrentPlayback(self, track: str, artist: str, uri: str) -> None:
        self.view.currentlyPlayingLabel.setText(f"{track} by {artist}")
        self.spotifyPlayer.checkAndRemoveFromQueue(uri)
        self.updateQueueField()

    def playPauseButtonClicked(self) -> None:
        if not self.localPlaybackState:
            self.view.spotifyPlayPauseButton.setStyleSheet(
                constants.SPOTIFY_PLAY_STATE_STYLE)
            self.spotifyPlayer.play()
            self.localPlaybackState = True
        else:
            self.view.spotifyPlayPauseButton.setStyleSheet(
                constants.SPOTIFY_PAUSED_STATE_STYLE)
            self.spotifyPlayer.pause()
            self.localPlaybackState = False

    def nextTrack(self) -> None:
        self.spotifyPlayer.next()

    def previousTrack(self) -> None:
        self.spotifyPlayer.previous()

    # ── Queue / search ────────────────────────────────────────────────────

    def updateQueueField(self) -> None:
        self.view.spotifyQueueField.clear()
        currentQueue = self.spotifyPlayer.getQueue()
        if currentQueue:
            for item in currentQueue:
                self.view.spotifyQueueField.addItem(
                    QtWidgets.QListWidgetItem(
                        f"TRACK: {item[0]}\nARTIST: {item[1]}\n"))
        else:
            self.view.spotifyQueueField.addItem(
                QtWidgets.QListWidgetItem("No songs currently in Bartender queue."))

    def searchSpotify(self) -> None:
        self.view.spotifySearchResultsField.clear()
        self.spotifyPlayer.search(self.view.spotifySearchInputField.text())
        for key, value in self.spotifyPlayer.getRecentQuery().items():
            self.view.spotifySearchResultsField.addItem(
                QtWidgets.QListWidgetItem(
                    f"ID: {key}\nTRACK: {value[0]}\nARTIST: {value[1]}\n"))

    def selectedSearch(self, item: QtWidgets.QListWidgetItem) -> None:
        itemDetails = item.text()
        userInput = QtWidgets.QMessageBox.question(
            self, "Request Track",
            f"Would you like to add the following track to the queue?\n\n{itemDetails}",
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No,
        )
        if userInput == QtWidgets.QMessageBox.StandardButton.Yes:
            data = itemDetails.split("\n")
            track_id = int(data[0].split("ID:")[1].strip())
            self.spotifyPlayer.requestTrack(track_id)
            self.updateQueueField()
