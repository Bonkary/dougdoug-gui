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
        self._buttonA = KeyboardButtonInputs(name='A Button')
        self._buttonB = KeyboardButtonInputs(name="B Button")
        self._bumperR = KeyboardButtonInputs(name="Right Bumper")
        self._bumperL = KeyboardButtonInputs(name="Left Bumper")
        
        row1.addWidget(self._buttonA)
        row1.addSpacing(columnSpacing)
        row1.addWidget(self._buttonB)
        row1.addSpacing(columnSpacing)
        row1.addWidget(self._bumperR)
        row1.addSpacing(columnSpacing)
        row1.addWidget(self._bumperL)
        
        # Row 2
        row2 = wdgts.NoPadHBoxLayout()
        self._dpadUp = KeyboardButtonInputs(name="D-Pad Up")
        self._dpadDown = KeyboardButtonInputs(name="D-Pad Down")
        self._dpadLeft = KeyboardButtonInputs(name="D-Pad Left")
        self._dpadRight = KeyboardButtonInputs(name="D-Pad Right")
        
        row2.addWidget(self._dpadUp)
        row2.addSpacing(columnSpacing)
        row2.addWidget(self._dpadDown)
        row2.addSpacing(columnSpacing)
        row2.addWidget(self._dpadLeft)
        row2.addSpacing(columnSpacing)
        row2.addWidget(self._dpadRight)
        
        # Row 3
        row3 = wdgts.NoPadHBoxLayout()
        self._select = KeyboardButtonInputs(name="Select")
        self._start = KeyboardButtonInputs(name='Start')
        
        row3.addWidget(self._select)
        row3.addSpacing(columnSpacing)
        row3.addWidget(self._start)
        
        
        # Config Manager
        configManager = ConfigManager(console=self)
        
        mainLayout.addLayout(row1)
        mainLayout.addSpacing(columnSpacing)
        mainLayout.addLayout(row2)
        mainLayout.addSpacing(columnSpacing)
        mainLayout.addLayout(row3)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(configManager)
        mainLayout.addStretch(True)

    def get_current_inputs(self) -> dict:
        return {
            'a': self._buttonA.get_inputs(),
            'b': self._buttonB.get_inputs(),
            'r': self._bumperR.get_inputs(),
            'l': self._bumperR.get_inputs(),
            'dpad_up': self._dpadUp.get_inputs(),
            'dpad_down': self._dpadDown.get_inputs(),
            'dpad_left': self._dpadLeft.get_inputs(),
            'dpad_right': self._dpadRight.get_inputs(),
        }



class ConfigManager(QFrame):
    def __init__(self, console: Gameboy):
        super().__init__()
        self.console = console
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
        
        buttonsContainer.addWidget(newButton)
        buttonsContainer.addSpacing(10)
        buttonsContainer.addWidget(updateButton)
        
        mainLayout.addWidget(dropdown, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(4)
        mainLayout.addLayout(buttonsContainer)
        mainLayout.addWidget(comboButton, alignment=gui.ALIGN_CENTER)
        
        newButton.clicked.connect(self.save_new_preset)
        updateButton.clicked.connect(self.update_preset)
        comboButton.clicked.connect(self.open_button_combos)

    @Slot()
    def open_button_combos(self) -> None:
        if not self.comboButtonPopup.isVisible():
            self.comboButtonPopup.exec()
        else:
            return

    @Slot()
    def save_new_preset(self) -> None:
        name, ok = QInputDialog.getText(self, "New Preset", "Preset Name")
        if ok:
            controls = self.console.get_current_inputs()
            preset = {
                name: controls
            }
            
            
    
    @Slot()
    def update_preset(self, preset: str) -> None:
        pass

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
        
        
        self._keyboardInput = wdgts.NamedLineEdit(name="Keyboard", namePlacement='side')
        self._pressCmdInput = wdgts.NamedLineEdit(name="Press Command", namePlacement='side')
        self._holdCmdInput = wdgts.NamedLineEdit(name="Hold Command", namePlacement='side')
        
        mainLayout.addWidget(title)
        mainLayout.addSpacing(15)
        mainLayout.addWidget(self._keyboardInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self._pressCmdInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self._holdCmdInput)
        
        rootLayout.addWidget(mainFrame, alignment=gui.ALIGN_CENTER)
        rootLayout.addStretch(True)
        
    def get_inputs(self) -> dict:
        return {
            'key': self._keyboardInput.get().lower(),
            'press': self._pressCmdInput.get().lower(),
            'hold': self._holdCmdInput.get().lower()
        }