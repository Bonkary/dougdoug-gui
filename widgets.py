import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
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