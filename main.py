import sys
import threading
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import *
from constants import *
import widgets as wdgts
import popups as popups
from consoles import ConsoleContainer
from configurations import *
from platform_connection import *
from keyboard_control import keyboard_execute_thread, PRESET_FOR_THREAD

class TwitchPlays(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(gui.MAIN_WINDOW_WIDTH, gui.MAIN_WINDOW_HEIGHT)
        self.setWindowTitle("Ez Twitch Plays")
        
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.TWITCH_PURPLE)
        self.setPalette(bg)

        mainLayout = wdgts.NoPadVBoxLayout()

        # Header
        header = Header()
        
        consoleDropdown = QComboBox()
        for console in AVAILABLE_CONSOLES:
            consoleDropdown.addItem(console)
        consoleDropdown.setPlaceholderText("Select Console")
        consoleDropdown.setCurrentIndex(-1)
        
        # Console Container
        self.consoleContainer = ConsoleContainer()
        
        # Footer
        self._footer = Footer(app=self)

        # Main Layout
        mainLayout.addSpacing(15)
        mainLayout.addWidget(header)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(consoleDropdown, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(self.consoleContainer, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(self._footer)
        
        self.setLayout(mainLayout)
        
        consoleDropdown.currentTextChanged.connect(self.consoleContainer.change_console)
    
    @Slot()
    def start_playing(self) -> None:
        KILL_THREADS_FLAG.clear()
        self._footer.playButtonContainer.setCurrentIndex(STOP_PLAYING_BUTTON_INDEX)
        preset = self.consoleContainer.get_preset()
        
        TWITCH_MANAGER.connect(channel_name=SETTINGS[TWITCH_CHANNEL])
        
        threading.Thread(target=TWITCH_MANAGER.listen_forever_thread, daemon=True).start()
        threading.Thread(target=keyboard_execute_thread, args=(preset,), daemon=True).start()
        
        LISTENER_THREAD_FLAG.set()
        EXECUTOR_THREAD_FLAG.set()
        
    @Slot()
    def stop_playing(self) -> None:
        self._footer.playButtonContainer.setCurrentIndex(START_PLAYING_BUTTON_INDEX)
        KILL_THREADS_FLAG.set()
        LISTENER_THREAD_FLAG.clear()
        EXECUTOR_THREAD_FLAG.clear()
        print("AHHHH")

class Header(QFrame):
    def __init__(self):
        super().__init__()
        self.keyMappingsPopup = popups.Keymappings(self)
        
        mainLayout = QHBoxLayout()
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
    
        # Input
        twitchInputContainer = wdgts.NoPadHBoxLayout()
        
        # Channel Label
        twitchLabel = QLabel("Twitch Channel:")
        twitchLabel.setFont(gui.DEFAULT_FONT)
        
        # Channel Input
        self._twitchInput = QLineEdit()
        
        # Save Button
        self._saveButton = QPushButton(text="Save")
        
        twitchInputContainer.addWidget(twitchLabel)
        twitchInputContainer.addSpacing(10)
        twitchInputContainer.addWidget(self._twitchInput)
        twitchInputContainer.addSpacing(10)
        twitchInputContainer.addWidget(self._saveButton)
        
        # Title
        titleFont = QFont()
        titleFont.setWeight(QFont.Weight.Bold)
        titleFont.setPixelSize(30)
        titleLabel = QLabel("Ez Twitch Plays")
        titleLabel.setFont(titleFont)
        
        # Buttons
        buttonContainer = QHBoxLayout()
        buttonContainer.setAlignment(gui.ALIGN_CENTER)
        buttonContainer.setContentsMargins(0,0,0,0)
        buttonContainer.setSpacing(0)
        
        tutorialButton = QPushButton(text="Tutorial")
        tutorialButton.setFont(gui.DEFAULT_FONT)
        
        keymappingsButton = QPushButton(text="See Keymappings")
        keymappingsButton.setFont(gui.DEFAULT_FONT)
        keymappingsButton.clicked.connect(self.open_keymappings)
        
        buttonContainer.addWidget(tutorialButton)
        buttonContainer.addSpacing(20)
        buttonContainer.addWidget(keymappingsButton)
        
        
        mainLayout.addSpacing(50)
        mainLayout.addLayout(twitchInputContainer)
        mainLayout.addSpacing(320)
        mainLayout.addWidget(titleLabel, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(300)
        mainLayout.addLayout(buttonContainer)
        mainLayout.addSpacing(50)
        mainLayout.addStretch(True)
        
        self.setLayout(mainLayout)
        
        if SETTINGS[TWITCH_CHANNEL]:
            self._twitchInput.setText(SETTINGS[TWITCH_CHANNEL])
            self._saveButton.setDisabled(True)
        
        self._saveButton.clicked.connect(self.save_twitch_channel)
        self._twitchInput.textChanged.connect(lambda: self._saveButton.setEnabled(True))
        
    @Slot()
    def save_twitch_channel(self) -> None:
        channel = self._twitchInput.text().strip()
        if channel:
            SETTINGS[TWITCH_CHANNEL] = channel
            update_settings_file()
            self._saveButton.setDisabled(True)

    @Slot()
    def open_keymappings(self):
        if not self.keyMappingsPopup.isVisible():
            self.keyMappingsPopup.show()
        else:
            return

class Footer(QFrame):
    def __init__(self, app: TwitchPlays):
        super().__init__()
        
        mainLayout = wdgts.NoPadHBoxLayout()
        self.setLayout(mainLayout)
        
        self.playButtonContainer = QStackedLayout()
        self.playButtonContainer.setAlignment(gui.ALIGN_CENTER)
        self.playButtonContainer.setContentsMargins(0,0,0,0)
        self.playButtonContainer.setSpacing(0)
        
        startButton = QPushButton("Start Playing")
        startButton.setFixedSize(500,50)
        
        stopButton = QPushButton("Stop Playing")
        stopButton.setFixedSize(500,50)
        
        self.playButtonContainer.insertWidget(START_PLAYING_BUTTON_INDEX, startButton)
        self.playButtonContainer.insertWidget(STOP_PLAYING_BUTTON_INDEX, stopButton)
        
        mainLayout.addStretch()
        mainLayout.addLayout(self.playButtonContainer)
        mainLayout.addStretch()
        
        startButton.clicked.connect(app.start_playing)
        stopButton.clicked.connect(app.stop_playing)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TwitchPlays()
    window.show()
    sys.exit(app.exec())