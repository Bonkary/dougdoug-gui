import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts
from qt_console_widgets import ConsoleContainer


class TwitchPlays(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1600, 900)
        self.setWindowTitle("Ez Twitch Plays")
        
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.TWITCH_PURPLE)
        self.setPalette(bg)
        
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setDirection(gui.TOP_TO_BOTTOM)
        mainLayout.setAlignment(gui.ALIGN_CENTER|gui.ALIGN_TOP)
        mainLayout.setSpacing(0)

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
        mainLayout = QHBoxLayout()
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
    
        # Input
        twitchInputContainer = QHBoxLayout()
        twitchInputContainer.setAlignment(gui.ALIGN_CENTER)
        twitchInputContainer.setContentsMargins(0,0,0,0)
        twitchInputContainer.setSpacing(0)
        
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

class Footer(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)
        
        configManager = ConfigManager()
        
        
        mainLayout.addWidget(configManager)
        mainLayout.addStretch(True)

class ConfigManager(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(gui.ALIGN_TOP)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        
        self.setLayout(mainLayout)
        
        # Presets
        dropdown = QComboBox()
        dropdown.setPlaceholderText("Select Preset")
        dropdown.setFixedWidth(170)
        
        buttonsContainer = QHBoxLayout()
        buttonsContainer.setAlignment(gui.ALIGN_TOP|gui.ALIGN_CENTER)
        buttonsContainer.setContentsMargins(0, 0, 0, 0)
        buttonsContainer.setSpacing(0)
        
        newButton = QPushButton(text='New')
        newButton.setFixedWidth(75)
        updateButton = QPushButton(text="Update")
        updateButton.setFixedWidth(75)
        
        # Button Combos Buttons
        comboButton = QPushButton(text='Open Button Combos')
        comboButton.setFixedWidth(200)
        
        buttonsContainer.addWidget(newButton)
        buttonsContainer.addSpacing(10)
        buttonsContainer.addWidget(updateButton)
        
        mainLayout.addWidget(dropdown, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(4)
        mainLayout.addLayout(buttonsContainer)
        mainLayout.addWidget(comboButton, alignment=gui.ALIGN_CENTER)
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TwitchPlays()
    window.show()
    sys.exit(app.exec())