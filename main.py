import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import *
from constants import *
import widgets as wdgts
import popups as popups
from consoles import ConsoleContainer




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
        
        # Console Dropdown
        consoleDropdown = wdgts.NamedDropdown(title='Select Console', titlePlacement='top')
        
        # Console Container
        consoles = ConsoleContainer()
        
        # Footer
        footer = Footer()

        # Main Layout
        mainLayout.addSpacing(15)
        mainLayout.addWidget(header)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(consoleDropdown, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(consoles, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(footer)
        
        self.setLayout(mainLayout)

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
        
        twitchLabel = QLabel("Twitch Channel:")
        twitchLabel.setFont(gui.DEFAULT_FONT)
        
        twitchInput = QLineEdit()
        
        saveButton = QPushButton(text="Save")
        
        twitchInputContainer.addWidget(twitchLabel)
        twitchInputContainer.addSpacing(10)
        twitchInputContainer.addWidget(twitchInput)
        twitchInputContainer.addSpacing(10)
        twitchInputContainer.addWidget(saveButton)
        
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

    @Slot()
    def open_keymappings(self):
        if not self.keyMappingsPopup.isVisible():
            self.keyMappingsPopup.show()
        else:
            return


class Footer(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = wdgts.NoPadVBoxLayout()
        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TwitchPlays()
    window.show()
    sys.exit(app.exec())