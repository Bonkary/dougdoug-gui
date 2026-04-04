import sys
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from qt_constants import *
import qt_widgets as wdgts



class ConsoleContainer(QFrame):
    def __init__(self):
        super().__init__()
        
        rootLayout = QHBoxLayout()
        rootLayout.setAlignment(gui.ALIGN_TOP)
        rootLayout.setContentsMargins(0,0,0,0)
        rootLayout.setSpacing(0)
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
        
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(gui.ALIGN_TOP|gui.ALIGN_CENTER)
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)
        
        row1 = QHBoxLayout()
        row1.setAlignment(gui.ALIGN_CENTER)
        row1.setContentsMargins(0,0,0,0)
        row1.setSpacing(0)
        
        buttonA = KeyboardButtonInputs(name='A Button')
        buttonB = KeyboardButtonInputs(name="B Button")
        bumperR = KeyboardButtonInputs(name="Right Bumper")
        bumperL = KeyboardButtonInputs(name="Left Bumper")
        
        row2 = QHBoxLayout()
        row2.setAlignment(gui.ALIGN_CENTER)
        row2.setContentsMargins(0,0,0,0)
        row2.setSpacing(0)
        
        dpadUp = KeyboardButtonInputs(name="D-Pad Up")
        dpadDown = KeyboardButtonInputs(name="D-Pad Down")
        dpadLeft = KeyboardButtonInputs(name="D-Pad Left")
        dpadRight = KeyboardButtonInputs(name="D-Pad Right")
        
        columnSpacing = 30
        row1.addWidget(buttonA)
        row1.addSpacing(columnSpacing)
        row1.addWidget(buttonB)
        row1.addSpacing(columnSpacing)
        row1.addWidget(bumperR)
        row1.addSpacing(columnSpacing)
        row1.addWidget(bumperL)
        
        row2.addWidget(dpadUp)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadDown)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadLeft)
        row2.addSpacing(columnSpacing)
        row2.addWidget(dpadRight)
        
        mainLayout.addLayout(row1)
        mainLayout.addSpacing(columnSpacing)
        mainLayout.addLayout(row2)
        mainLayout.addStretch(True)

        
          

class KeyboardButtonInputs(QFrame):
    def __init__(self, *, name: str):
        super().__init__()
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.setLineWidth(5)
        
        # BORDER COLOR
        borderColor = self.palette()
        borderColor.setColor(QPalette.WindowText, colors.DARK_PURPLE)
        self.setPalette(borderColor)
        
        rootLayout = QVBoxLayout()
        rootLayout.setSpacing(0)
        self.setLayout(rootLayout)
        
        # ACTUAL WIDGET STARTS HERE
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
        mainLayout.addSpacing(15)
        mainLayout.addWidget(keyboardInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(pressCmdInput)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(holdCmdInput)
        
        rootLayout.addWidget(mainFrame, alignment=gui.ALIGN_CENTER)
        rootLayout.addStretch(True)
        
      