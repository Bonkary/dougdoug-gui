import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *




class NamedDropdown(QWidget):
    def __init__(self, *, title: str, titlePlacement: str, titleFont: QFont = gui.DEFAULT_FONT):
        super().__init__()
        match titlePlacement:
            case 'top':
                mainLayout = QVBoxLayout()
                mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
            case 'side':
                mainLayout = QHBoxLayout()
                mainLayout.setDirection(QBoxLayout.Direction.LeftToRight)
            case _: 
                raise ValueError(f"{titlePlacement} is not a valid value (must be 'top' or 'side')")
        self.setLayout(mainLayout)
        
        titleLabel = QLabel(text=title)
        titleLabel.setFont(gui.DEFAULT_FONT)
        mainLayout.addWidget(titleLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        
        dropdown = QComboBox()
        dropdown.setFixedWidth(200)
        mainLayout.addWidget(dropdown)

class TitledLineEdit(QWidget):
    def __init__(self, title: str, titlePlacement: str, titleFont: QFont = gui.DEFAULT_FONT, width: int = 100):
        super().__init__()
        match titlePlacement:
            case 'top':
                mainLayout = QVBoxLayout()
                mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
                alignment = Qt.AlignmentFlag.AlignCenter
            case 'side':
                mainLayout = QHBoxLayout()
                mainLayout.setDirection(QBoxLayout.Direction.LeftToRight)
                alignment = Qt.AlignmentFlag.AlignRight
            case _: 
                raise ValueError(f"{titlePlacement} is not a valid value (must be 'top' or 'side')")
        self.setLayout(mainLayout)
        
        titleLabel = QLabel(text=title)
        titleLabel.setFont(gui.DEFAULT_FONT)
                
        mainLayout.addWidget(titleLabel, alignment=alignment)
        
        entry = QLineEdit()
        entry.setFixedWidth(width)
        entry.setFont(gui.DEFAULT_FONT)
        mainLayout.addWidget(entry, alignment)

