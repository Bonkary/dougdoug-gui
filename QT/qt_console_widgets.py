import sys
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts

class Gameboy(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.TWITCH_PURPLE)
        self.setPalette(bg)
        
        mainLayout = QVBoxLayout()
        mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
        self.setLayout(mainLayout)
        
        row1 = QHBoxLayout()
        row1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        buttonA = KeyboardButtonInputs(name='A Button')
        row1.addWidget(buttonA)
        
        buttonB = KeyboardButtonInputs(name="B Button")
        row1.addWidget(buttonB)
        
        bumperR = KeyboardButtonInputs(name="Right Bumper")
        row1.addWidget(bumperR)
        
        bumperL = KeyboardButtonInputs(name="Left Bumper")
        row1.addWidget(bumperL)
        row1.addSpacing(55)
        
        row2 = QHBoxLayout()
        row2.setDirection(QBoxLayout.Direction.LeftToRight)
        
        dpadUp = KeyboardButtonInputs(name="D-Pad Up")
        row2.addWidget(dpadUp)
        
        dpadDown = KeyboardButtonInputs(name="D-Pad Down")
        row2.addWidget(dpadDown)
        
        dpadLeft = KeyboardButtonInputs(name="D-Pad Left")
        row2.addWidget(dpadLeft)
        
        dpadRight = KeyboardButtonInputs(name="D-Pad Right")
        row2.addWidget(dpadRight)
        row2.addSpacing(55)
        
        mainLayout.addLayout(row1)
        mainLayout.addLayout(row2)
        mainLayout.addStretch(True)
        
        
          
        
class KeyboardButtonInputs(QWidget):
    def __init__(self, *, name: str):
        super().__init__()
        mainLayout = QVBoxLayout()
        mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
        self.setLayout(mainLayout)
        
        titleFont = QFont()
        titleFont.setUnderline(True)
        titleFont.setPixelSize(18)
        title = QLabel(text=name)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(titleFont)
        mainLayout.addWidget(title)
        
        keyboardInput = wdgts.TitledLineEdit(title="Keyboard", titlePlacement='side')
        mainLayout.addWidget(keyboardInput)
        
        pressCmdInput = wdgts.TitledLineEdit(title="Press Command", titlePlacement='side')
        mainLayout.addWidget(pressCmdInput)
        
        holdCmdInput = wdgts.TitledLineEdit(title="Hold Command", titlePlacement='side')
        mainLayout.addWidget(holdCmdInput)
        
        
        
      