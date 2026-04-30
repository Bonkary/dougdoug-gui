import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit
from PySide6.QtGui import QPalette
from constants import *


class NamedDropdown(QFrame):
    def __init__(self, *, title: str, titlePlacement: str, titleFont: QFont = gui.DEFAULT_FONT):
        super().__init__()
        self.setMinimumHeight(0)
        match titlePlacement:
            case 'top':
                mainLayout = NoPadVBoxLayout()
                mainLayout.setDirection(gui.TOP_TO_BOTTOM)
            case 'side':
                mainLayout = NoPadHBoxLayout()
                mainLayout.setDirection(gui.LEFT_TO_RIGHT)
            case _: 
                raise ValueError(f"{titlePlacement} is not a valid value (must be 'top' or 'side')")
        self.setLayout(mainLayout)
        
        titleLabel = QLabel(text=title)
        titleLabel.setFont(gui.DEFAULT_FONT)
        titleLabel.setContentsMargins(0,0,0,0)
        
        self._dropdown = QComboBox()
        self._dropdown.setFixedWidth(200)
        self._dropdown.setContentsMargins(0,0,0,0)
        
        mainLayout.addWidget(titleLabel, alignment=gui.ALIGN_CENTER)
        mainLayout.addWidget(self._dropdown)
        
    def addItem(self, item: str) -> None:
        self._dropdown.addItem(item)
        
    def setCurrentText(self, text: str|int) -> None:
        self._dropdown.setCurrentText(text)
        
    def setCurrentIndex(self, index: int) -> None:
        self._dropdown.setCurrentIndex(index)
        
    def setPlaceholderText(self, text: str|int) -> None:
        self._dropdown.setPlaceholderText(text)
            
class NamedLineEdit(QFrame):
    def __init__(self, name: str, namePlacement: str, titleFont: QFont = gui.DEFAULT_FONT, width: int = 100):
        super().__init__()
        match namePlacement:
            case 'top':
                mainLayout = NoPadVBoxLayout()
                mainLayout.setDirection(gui.TOP_TO_BOTTOM)
                alignment = gui.ALIGN_CENTER
            case 'side':
                mainLayout = NoPadHBoxLayout()
                mainLayout.setDirection(gui.LEFT_TO_RIGHT)
                alignment = gui.ALIGN_RIGHT
            case _: 
                raise ValueError(f"{namePlacement} is not a valid value (must be 'top' or 'side')")
        self.setLayout(mainLayout)
        
        titleLabel = QLabel(text=name)
        titleLabel.setFont(gui.DEFAULT_FONT)
        
        self.entry = QLineEdit()
        self.entry.setFixedWidth(width)
        self.entry.setFont(gui.DEFAULT_FONT)
        
        mainLayout.addWidget(titleLabel, alignment=alignment)
        mainLayout.addSpacing(7)
        mainLayout.addWidget(self.entry, alignment)
        
    def getText(self) -> str:
        return self.entry.text().strip()
    
    def setText(self, text: str) -> None:
        self.entry.setText(text)

class NoPadHBoxLayout(QHBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.setAlignment(gui.ALIGN_TOP|gui.ALIGN_CENTER)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        
class NoPadVBoxLayout(QVBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.setAlignment(gui.ALIGN_TOP|gui.ALIGN_CENTER)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        
class KeyboardButtonInputs(QFrame):
    def __init__(self, *, name: str):
        super().__init__()
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.setLineWidth(5)
        
        # BORDER COLOR
        borderColor = self.palette()
        borderColor.setColor(QPalette.WindowText, colors.DARK_PURPLE)
        self.setPalette(borderColor)
        
        rootLayout = NoPadVBoxLayout()
        rootLayout.setContentsMargins(20,20,20,20)
        self.setLayout(rootLayout)
        
        # ACTUAL WIDGET STARTS HERE
        mainFrame = QFrame()
        mainTextColor = mainFrame.palette()
        mainTextColor.setColor(QPalette.WindowText, 'white')
        mainFrame.setPalette(mainTextColor)
        
        mainLayout = NoPadVBoxLayout()
        mainFrame.setLayout(mainLayout)
        
        titleFont = QFont()
        titleFont.setUnderline(True)
        titleFont.setPixelSize(18)
        title = QLabel(text=name)
        title.setAlignment(gui.ALIGN_CENTER)
        title.setFont(titleFont)
        
        
        self._keyboardInput = NamedLineEdit(name="Keyboard", namePlacement='side')
        self._pressCmdInput = NamedLineEdit(name="Press Command", namePlacement='side')
        self._holdCmdInput = NamedLineEdit(name="Hold Command", namePlacement='side')
        self._probInput = NamedLineEdit(name="Probability (0-100)", namePlacement='side')
        
        mainLayout.addWidget(title)
        mainLayout.addSpacing(15)
        mainLayout.addWidget(self._keyboardInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self._pressCmdInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self._holdCmdInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self._probInput)
        
        rootLayout.addWidget(mainFrame, alignment=gui.ALIGN_CENTER)
        rootLayout.addStretch(True)
        
    def get_inputs(self) -> dict:
        try:
            probInput = int(self._probInput.getText())
        except ValueError:
            if not probInput:
                probInput = 100
            else:
                print("prob needs to be a whole number")
                probInput = 100 # DEV STUFF
                
        return {
            KEY: self._keyboardInput.getText().lower(),
            PRESS: self._pressCmdInput.getText().lower(),
            HOLD: self._holdCmdInput.getText().lower(),
            PROBABILITY: probInput
        }

    def load_inputs(self, inputs: dict):
        self._keyboardInput.setText(inputs[KEY])
        self._pressCmdInput.setText(inputs[PRESS])
        self._holdCmdInput.setText(inputs[HOLD])
        self._probInput.setText(str(inputs[PROBABILITY]))
    
    def clear_inputs(self) -> None:
        self._keyboardInput.setText("")
        self._pressCmdInput.setText("")
        self._holdCmdInput.setText("")
         

        
        
        
