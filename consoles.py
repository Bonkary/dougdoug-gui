import sys
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import *
from constants import *
import widgets as wdgts
import popups as popups



class ConsoleContainer(QFrame):
    def __init__(self):
        super().__init__()
        
        rootLayout = wdgts.NoPadHBoxLayout()
        self.setLayout(rootLayout)
        
        mainLayout = QStackedLayout()
        mainLayout.setAlignment(gui.ALIGN_CENTER)
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
        
        
        
        gameboy = Gameboy()
        
        mainLayout.insertWidget(GAMEBOY_INDEX, gameboy)
        
        rootLayout.addLayout(mainLayout)



class Gameboy(QFrame):
    def __init__(self):
        super().__init__()
        
        
        
        mainLayout = wdgts.NoPadVBoxLayout()
        self.setLayout(mainLayout)
        
        columnSpacing = 30
        # Row 1
        row1 = wdgts.NoPadHBoxLayout()
        buttonA = KeyboardButtonInputs(name='A Button')
        buttonB = KeyboardButtonInputs(name="B Button")
        bumperR = KeyboardButtonInputs(name="Right Bumper")
        bumperL = KeyboardButtonInputs(name="Left Bumper")
        
        row1.addWidget(buttonA)
        row1.addSpacing(columnSpacing)
        row1.addWidget(buttonB)
        row1.addSpacing(columnSpacing)
        row1.addWidget(bumperR)
        row1.addSpacing(columnSpacing)
        row1.addWidget(bumperL)
        
        # Row 2
        row2 = wdgts.NoPadHBoxLayout()
        dpadUp = KeyboardButtonInputs(name="D-Pad Up")
        dpadDown = KeyboardButtonInputs(name="D-Pad Down")
        dpadLeft = KeyboardButtonInputs(name="D-Pad Left")
        dpadRight = KeyboardButtonInputs(name="D-Pad Right")
        
        row2.addWidget(dpadUp)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadDown)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadLeft)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadRight)
        
        # Config Manager
        configManager = ConfigManager()
        
        
        
        mainLayout.addLayout(row1)
        mainLayout.addSpacing(columnSpacing)
        mainLayout.addLayout(row2)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(configManager)
        mainLayout.addStretch(True)


class ConfigManager(QFrame):
    def __init__(self):
        super().__init__()
        self.comboButtonPopup = popups.ButtonCombosConfig(self)
        mainLayout = wdgts.NoPadVBoxLayout()
        
        self.setLayout(mainLayout)
        
        # Presets
        dropdown = QComboBox()
        dropdown.setPlaceholderText("Select Preset")
        dropdown.setFixedWidth(170)
        
        buttonsContainer = wdgts.NoPadHBoxLayout()
        buttonsContainer.setAlignment(gui.ALIGN_CENTER)
        
        newButton = QPushButton(text='New')
        newButton.setFixedWidth(75)
        updateButton = QPushButton(text="Update")
        updateButton.setFixedWidth(75)
        
        # Button Combos Buttons
        comboButton = QPushButton(text='Open Button Combos')
        comboButton.setFixedWidth(200)
        comboButton.clicked.connect(self.open_button_combos)
        
        buttonsContainer.addWidget(newButton)
        buttonsContainer.addSpacing(10)
        buttonsContainer.addWidget(updateButton)
        
        mainLayout.addWidget(dropdown, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(4)
        mainLayout.addLayout(buttonsContainer)
        mainLayout.addWidget(comboButton, alignment=gui.ALIGN_CENTER)

    @Slot()
    def open_button_combos(self):
        if not self.comboButtonPopup.isVisible():
            self.comboButtonPopup.exec()
        else:
            return


          

class KeyboardButtonInputs(QFrame):
    def __init__(self, *, name: str):
        super().__init__()
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.setLineWidth(5)
        
        # BORDER COLOR
        borderColor = self.palette()
        borderColor.setColor(QPalette.WindowText, colors.DARK_PURPLE)
        self.setPalette(borderColor)
        
        rootLayout = wdgts.NoPadVBoxLayout()
        rootLayout.setContentsMargins(20,20,20,20)
        self.setLayout(rootLayout)
        
        # ACTUAL WIDGET STARTS HERE
        mainFrame = QFrame()
        mainTextColor = mainFrame.palette()
        mainTextColor.setColor(QPalette.WindowText, 'white')
        mainFrame.setPalette(mainTextColor)
        
        mainLayout = wdgts.NoPadVBoxLayout()
        mainFrame.setLayout(mainLayout)
        
        titleFont = QFont()
        titleFont.setUnderline(True)
        titleFont.setPixelSize(18)
        title = QLabel(text=name)
        title.setAlignment(gui.ALIGN_CENTER)
        title.setFont(titleFont)
        
        
        keyboardInput = wdgts.NamedLineEdit(name="Keyboard", namePlacement='side')
        pressCmdInput = wdgts.NamedLineEdit(name="Press Command", namePlacement='side')
        holdCmdInput = wdgts.NamedLineEdit(name="Hold Command", namePlacement='side')
        
        mainLayout.addWidget(title)
        mainLayout.addSpacing(15)
        mainLayout.addWidget(keyboardInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(pressCmdInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(holdCmdInput)
        
        rootLayout.addWidget(mainFrame, alignment=gui.ALIGN_CENTER)
        rootLayout.addStretch(True)
        
      