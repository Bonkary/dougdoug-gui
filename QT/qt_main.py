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
        self.setFixedSize(1400, 900)
        self.setWindowTitle("Ez Twitch Plays")
        
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.TWITCH_PURPLE)
        self.setPalette(bg)
        
        mainLayout = QVBoxLayout()
        mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
        self.setLayout(mainLayout)
        
        # Header
        headerLayout = HeaderWidget()
        

        # Dropdowns
        dropdownContainer = QHBoxLayout()
        dropdownContainer.setDirection(QBoxLayout.Direction.RightToLeft)
        
        presetDropdown = wdgts.NamedDropdown(title='Presets', titlePlacement='top')
        consoleDropdown = wdgts.NamedDropdown(title='Select Console', titlePlacement='top')
        
        dropdownContainer.addSpacing(200)
        dropdownContainer.addWidget(presetDropdown)
        dropdownContainer.addSpacing(140)
        dropdownContainer.addWidget(consoleDropdown)
        dropdownContainer.addStretch(True)
        
        
        # Consoles
        consoles = ConsoleContainer()
        

        savePresetContainer = QHBoxLayout()
        savePresetContainer.setDirection(QBoxLayout.Direction.LeftToRight)
        
        presetInput = wdgts.TitledLineEdit(title="Preset Name", titlePlacement='side')
        saveButton = QPushButton(text="Save")
        
        savePresetContainer.addWidget(presetInput)
        savePresetContainer.addWidget(saveButton)
        savePresetContainer.addStretch(True)
        
        mainLayout.addWidget(headerLayout)
        mainLayout.addLayout(dropdownContainer)
        mainLayout.addWidget(consoles, alignment=Qt.AlignmentFlag.AlignTop)
        mainLayout.addStretch(True)

class HeaderWidget(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = QHBoxLayout()
        mainLayout.setDirection(QBoxLayout.Direction.LeftToRight)
        self.setLayout(mainLayout)

        # Twitch Channel Input
        twitchInputContainer = QHBoxLayout()
        twitchInputContainer.setDirection(QHBoxLayout.Direction.LeftToRight)
        twitchInputContainer.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
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
        buttonContainer.setDirection(QHBoxLayout.Direction.LeftToRight)
        buttonContainer.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        tutorialButton = QPushButton(text="Tutorial")
        tutorialButton.setFont(gui.DEFAULT_FONT)
        
        keymappingsButton = QPushButton(text="See Keymappings")
        keymappingsButton.setFont(gui.DEFAULT_FONT)
        
        buttonContainer.addWidget(tutorialButton)
        buttonContainer.addWidget(keymappingsButton)
        
        mainLayout.addLayout(twitchInputContainer)
        mainLayout.addSpacing(225)
        mainLayout.addWidget(titleLabel)
        mainLayout.addSpacing(180)
        mainLayout.addLayout(buttonContainer)
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

        





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TwitchPlays()
    window.show()
    sys.exit(app.exec())