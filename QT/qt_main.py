import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts
from qt_console_widgets import *

GAMEBOY_INDEX = 0


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
        mainLayout.setDirection(gui.TOP_TO_BOTTOM)
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)
    
        header = Header()
        
        consoleDropdownContainer = QHBoxLayout()
        consoleDropdownContainer.setDirection(gui.RIGHT_TO_LEFT)
        consoleDropdownContainer.setAlignment(gui.ALIGN_CENTER)
        
        consoleDropdown = wdgts.NamedDropdown(title='Select Console', titlePlacement='top')
        consoleDropdownContainer.addWidget(consoleDropdown, alignment=gui.ALIGN_CENTER)
        
        consoleContainer = QHBoxLayout()
        consoleContainer.setSpacing(0)
        consoles = ConsoleContainer()
        consoleContainer.addSpacing(50)
        consoleContainer.addWidget(consoles)
        
        footerContainer = QHBoxLayout()
        footerContainer.setSpacing(0)
        footer = Footer()
        footerContainer.addWidget(footer)

        mainLayout.addWidget(header, alignment=gui.ALIGN_CENTER)
        mainLayout.addLayout(consoleDropdownContainer)
        mainLayout.addLayout(consoleContainer)
        mainLayout.addWidget(footer, alignment=gui.ALIGN_TOP)
        mainLayout.addStretch(True)

class Header(QFrame):
    def __init__(self):
        super().__init__()
        mainLayout = QHBoxLayout()
        mainLayout.setDirection(gui.LEFT_TO_RIGHT)
        self.setLayout(mainLayout)

        # Twitch Channel Input
        twitchInputContainer = QHBoxLayout()
        twitchInputContainer.setDirection(gui.LEFT_TO_RIGHT)
        twitchInputContainer.setAlignment(gui.ALIGN_LEFT)
        
        twitchLabel = QLabel("Twitch Channel:")
        twitchLabel.setFont(gui.DEFAULT_FONT)
        
        twitchInput = QLineEdit()
        saveButton = QPushButton(text="Save")
        
        twitchInputContainer.addWidget(twitchLabel)
        twitchInputContainer.addWidget(twitchInput)
        twitchInputContainer.addWidget(saveButton)
        twitchInputContainer.addStretch(True)
        
        # Title
        titleFont = QFont()
        titleFont.setWeight(QFont.Weight.Bold)
        titleFont.setPixelSize(30)
        titleLabel = QLabel("Ez Twitch Plays")
        titleLabel.setFont(titleFont)
        
        
        # Buttons
        buttonContainer = QHBoxLayout()
        buttonContainer.setDirection(gui.LEFT_TO_RIGHT)
        buttonContainer.setAlignment(gui.ALIGN_RIGHT)
        
        tutorialButton = QPushButton(text="Tutorial")
        tutorialButton.setFont(gui.DEFAULT_FONT)
        
        keymappingsButton = QPushButton(text="See Keymappings")
        keymappingsButton.setFont(gui.DEFAULT_FONT)
        
        buttonContainer.addWidget(tutorialButton)
        buttonContainer.addWidget(keymappingsButton)
        
        mainLayout.addLayout(twitchInputContainer)
        mainLayout.addSpacing(300)
        mainLayout.addWidget(titleLabel)
        mainLayout.addSpacing(300)
        mainLayout.addLayout(buttonContainer)
        mainLayout.addSpacing(50)
        mainLayout.addStretch(True)

class Footer(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        self.setLayout(mainLayout)
        
        presetContainer = QHBoxLayout()
        presetContainer.setSpacing(0)
        presets = PresetManager()
        presetContainer.addWidget(presets, alignment=gui.ALIGN_CENTER|gui.ALIGN_TOP)
        
        mainLayout.addLayout(presetContainer)
        mainLayout.addStretch(True)
        
        
        


class ConsoleContainer(QFrame):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.TWITCH_PURPLE)
        self.setPalette(bg)
        
        mainLayout = QStackedLayout()
        self.setLayout(mainLayout)
        
        gameboy = Gameboy()
        
        
        
        
        mainLayout.insertWidget(GAMEBOY_INDEX, gameboy)

class PresetManager(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setContentsMargins(0,0,0,0)
        mainLayout = QHBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        self.setLayout(mainLayout)
        
        # Save Preset
        saveContainer = QVBoxLayout()
        saveContainer.setAlignment(gui.ALIGN_CENTER)
        saveContainer.setSpacing(0)
        
        inputContainer = QVBoxLayout()
        inputContainer.setSpacing(0)
        inputContainer.setAlignment(gui.ALIGN_CENTER)
        presetInput = wdgts.NamedLineEdit(name="New Preset", namePlacement='top')
        inputContainer.addWidget(presetInput, alignment=gui.ALIGN_TOP)
        
        buttonContainer = QVBoxLayout()
        buttonContainer.setSpacing(0)
        buttonContainer.setAlignment(gui.ALIGN_CENTER)
        saveButton = QPushButton(text="Save")
        saveButton.setMaximumWidth(75)
        buttonContainer.addWidget(saveButton)
        
        saveContainer.addLayout(inputContainer)
        saveContainer.addLayout(buttonContainer)

        mainLayout.addLayout(saveContainer)
        mainLayout.addStretch(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TwitchPlays()
    window.show()
    sys.exit(app.exec())