import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *




class NamedDropdown(QFrame):
    def __init__(self, *, title: str, titlePlacement: str, titleFont: QFont = gui.DEFAULT_FONT):
        super().__init__()
        self.setMinimumHeight(0)
        match titlePlacement:
            case 'top':
                mainLayout = QVBoxLayout()
                mainLayout.setDirection(gui.TOP_TO_BOTTOM)
            case 'side':
                mainLayout = QHBoxLayout()
                mainLayout.setDirection(gui.LEFT_TO_RIGHT)
            case _: 
                raise ValueError(f"{titlePlacement} is not a valid value (must be 'top' or 'side')")
        self.setLayout(mainLayout)
        mainLayout.setSpacing(0)
        self.setContentsMargins(0,0,0,0)
        
        titleLabel = QLabel(text=title)
        titleLabel.setFont(gui.DEFAULT_FONT)
        titleLabel.setContentsMargins(0,0,0,0)
        
        dropdown = QComboBox()
        dropdown.setFixedWidth(200)
        dropdown.setContentsMargins(0,0,0,0)
        
        mainLayout.addWidget(titleLabel, alignment=gui.ALIGN_CENTER)
        mainLayout.addWidget(dropdown)

class NamedLineEdit(QFrame):
    def __init__(self, name: str, namePlacement: str, titleFont: QFont = gui.DEFAULT_FONT, width: int = 100):
        super().__init__()
        self.setMinimumHeight(0)
        match namePlacement:
            case 'top':
                mainLayout = QVBoxLayout()
                mainLayout.setDirection(gui.TOP_TO_BOTTOM)
                alignment = gui.ALIGN_CENTER
            case 'side':
                mainLayout = QHBoxLayout()
                mainLayout.setDirection(gui.LEFT_TO_RIGHT)
                alignment = gui.ALIGN_RIGHT
            case _: 
                raise ValueError(f"{namePlacement} is not a valid value (must be 'top' or 'side')")
            
        self.setLayout(mainLayout)
        mainLayout.setSpacing(0)
        
        titleLabel = QLabel(text=name)
        titleLabel.setMinimumHeight(0)
        titleLabel.setFont(gui.DEFAULT_FONT)
        
        entry = QLineEdit()
        entry.setMinimumHeight(0)
        entry.setFixedWidth(width)
        entry.setFont(gui.DEFAULT_FONT)
        
        mainLayout.addWidget(titleLabel, alignment=alignment)
        mainLayout.addSpacing(7)
        mainLayout.addWidget(entry, alignment)

