import sys
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts

class Gameboy(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        mainLayout.setDirection(gui.TOP_TO_BOTTOM)
        self.setLayout(mainLayout)
        
        row1 = QHBoxLayout()
        row1.setAlignment(gui.ALIGN_CENTER)
        
        buttonA = KeyboardButtonInputs(name='A Button')
        buttonB = KeyboardButtonInputs(name="B Button")
        bumperR = KeyboardButtonInputs(name="Right Bumper")
        bumperL = KeyboardButtonInputs(name="Left Bumper")
        
        row2 = QHBoxLayout()
        row2.setAlignment(gui.ALIGN_CENTER)
        row2.setDirection(gui.LEFT_TO_RIGHT)
        
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
        rootLayout.setSpacing(0)
        self.setLayout(rootLayout)
        
        mainFrame = QFrame()
        mainFrame.setMinimumHeight(0)
        mainTextColor = mainFrame.palette()
        mainTextColor.setColor(QPalette.WindowText, 'white')
        mainFrame.setPalette(mainTextColor)
        
        
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setDirection(gui.TOP_TO_BOTTOM)
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
        mainLayout.addWidget(keyboardInput)
        mainLayout.addWidget(pressCmdInput)
        mainLayout.addWidget(holdCmdInput)
        
        rootLayout.addWidget(mainFrame, alignment=gui.ALIGN_CENTER)
        rootLayout.addStretch(True)
        
      