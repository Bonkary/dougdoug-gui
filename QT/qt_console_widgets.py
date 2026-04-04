import sys
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts

class Gameboy(QFrame):
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
        buttonB = KeyboardButtonInputs(name="B Button")
        bumperR = KeyboardButtonInputs(name="Right Bumper")
        bumperL = KeyboardButtonInputs(name="Left Bumper")
        
        row2 = QHBoxLayout()
        row2.setDirection(QBoxLayout.Direction.LeftToRight)
        
        dpadUp = KeyboardButtonInputs(name="D-Pad Up")
        dpadDown = KeyboardButtonInputs(name="D-Pad Down")
        dpadLeft = KeyboardButtonInputs(name="D-Pad Left")
        dpadRight = KeyboardButtonInputs(name="D-Pad Right")
        
        row1.addWidget(buttonA)
        row1.addWidget(buttonB)
        row1.addWidget(bumperR)
        row1.addWidget(bumperL)
        row1.addSpacing(55)
        
        row2.addWidget(dpadUp)
        row2.addWidget(dpadDown)
        row2.addWidget(dpadLeft)
        row2.addWidget(dpadRight)
        row2.addSpacing(55)
        
        mainLayout.addLayout(row1)
        mainLayout.addLayout(row2)
        mainLayout.addStretch(True)
        
        
          
        
class KeyboardButtonInputs(QFrame):
    def __init__(self, *, name: str):
        super().__init__()
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.setLineWidth(5)
        
        borderColor = self.palette()
        borderColor.setColor(QPalette.WindowText, colors.DARK_PURPLE)
        self.setPalette(borderColor)
        
        rootLayout = QVBoxLayout()
        self.setLayout(rootLayout)
        
        mainFrame = QFrame()
        mainTextColor = mainFrame.palette()
        mainTextColor.setColor(QPalette.WindowText, 'white')
        mainFrame.setPalette(mainTextColor)
        rootLayout.addWidget(mainFrame)
        
        mainLayout = QVBoxLayout()
        mainLayout.setDirection(QBoxLayout.Direction.TopToBottom)
        mainFrame.setLayout(mainLayout)
        
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
        
        
        
      