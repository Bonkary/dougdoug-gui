import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from constants import *
import widgets as wdgts

class Keymappings(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.resize(gui.KEYMAP_WINDOW_WIDTH, gui.KEYMAP_WINDOW_HEIGHT)
        
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), '#353836')
        self.setPalette(bg)

        mainLayout = wdgts.NoPadVBoxLayout()
        self.setLayout(mainLayout)
        
        # Title
        titleFont = QFont()
        titleFont.setWeight(QFont.Weight.Bold)
        titleFont.setPixelSize(40)
        title = QLabel("Keymappings")
        title.setStyleSheet(f"color: white")
        title.setFont(titleFont)
        
        mainLayout.addSpacing(40)
        mainLayout.addWidget(title, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(50)
        
        # Mappings
        mappingsLayout = wdgts.NoPadHBoxLayout()
        mappingsLayout.setAlignment(gui.ALIGN_CENTER)
        col1 = wdgts.NoPadVBoxLayout()
        col2 = wdgts.NoPadVBoxLayout()
        mapFont = QFont()
        mapFont.setPixelSize(20)
        
        # Left Col
        colCount = len(keys.USER_FRIENDLY_KEYBOARD_MAPPINGS) // 2
        for key in keys.USER_FRIENDLY_KEYBOARD_MAPPINGS[:colCount]:
            newMapping = QLabel(key)
            newMapping.setFont(mapFont)
            col1.addWidget(newMapping)
            col1.addSpacing(20)
        
        # Right Col
        for key in keys.USER_FRIENDLY_KEYBOARD_MAPPINGS[colCount:]:
            newMapping = QLabel(key)
            newMapping.setFont(mapFont)
            col2.addWidget(newMapping)
            col2.addSpacing(20)
            
        mappingsLayout.addLayout(col1)
        mappingsLayout.addSpacing(200)
        mappingsLayout.addLayout(col2)
        
        mainLayout.addLayout(mappingsLayout)
        
        
class ButtonCombosConfig(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(gui.COMBO_WINDOW_WIDTH, gui.COMBO_WINDOW_HEIGHT)
        self.setWindowTitle("Button Combos")
        
        self.setAutoFillBackground(True)
        bg = self.palette()
        bg.setColor(self.backgroundRole(), colors.DARK_PURPLE)
        self.setPalette(bg)
        
        mainLayout = wdgts.NoPadHBoxLayout()
        self.setLayout(mainLayout)
        
        col1 = wdgts.NoPadVBoxLayout()
        
        addComboInputs = ButtonComboInputs()
        
        col1.addSpacing(30)
        col1.addWidget(addComboInputs, alignment=gui.ALIGN_CENTER|gui.ALIGN_LEFT)
        
        mainLayout.addSpacing(100)
        mainLayout.addLayout(col1)
        mainLayout.addStretch()
        

class ButtonComboInputs(QFrame):
    def __init__(self):
        super().__init__()
        
        mainLayout = wdgts.NoPadVBoxLayout()
        self.setLayout(mainLayout)
        
        # Title
        titleFont = QFont()
        titleFont.setWeight(QFont.Weight.Bold)
        titleFont.setPixelSize(25)
        title = QLabel("New Button Combo")
        title.setFont(titleFont)
        
        # Key Inputs
        keyInputsContainer = wdgts.NoPadHBoxLayout()
        key1Input = wdgts.NamedLineEdit("Key 1", namePlacement='top')
        key2Input = wdgts.NamedLineEdit("Key 2", namePlacement='top')
        
        keyInputsContainer.addWidget(key1Input)
        keyInputsContainer.addWidget(key2Input)
        
        # Commands Inputs
        cmdInputsContainer = wdgts.NoPadVBoxLayout()
        cmdInputsContainer.setContentsMargins(0,0,7,0)
        cmdInputsContainer.setAlignment(gui.ALIGN_CENTER)
        pressInput = wdgts.NamedLineEdit(name="Press", namePlacement='side')
        holdInput = wdgts.NamedLineEdit(name="Hold", namePlacement='side')
        
        cmdInputsContainer.addWidget(pressInput)
        cmdInputsContainer.addSpacing(15)
        cmdInputsContainer.addWidget(holdInput)
        
        # Save Button
        addButton = QPushButton(text='Add Combo')
        
        mainLayout.addWidget(title, alignment=gui.ALIGN_CENTER)
        mainLayout.addSpacing(20)
        mainLayout.addLayout(keyInputsContainer)
        mainLayout.addSpacing(20)
        mainLayout.addLayout(cmdInputsContainer)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(addButton, alignment=gui.ALIGN_CENTER)
        mainLayout.addStretch()