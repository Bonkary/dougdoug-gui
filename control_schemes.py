import customtkinter as ctk
import widgets as wdgts
from constants import *

class GameboyControls(wdgts.HideableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2,3), weight=EQUAL_WEIGHT)
        
        self._AButton = wdgts.ControlAssignment(master=self, action="A")
        self._AButton.grid(row=0, column=0, padx=20, pady=20)
        
        self._BButton = wdgts.ControlAssignment(master=self, action="B")
        self._BButton.grid(row=0, column=1, padx=20, pady=20)
        
        self._LButton = wdgts.ControlAssignment(master=self, action="L")
        self._LButton.grid(row=0, column=2, padx=20, pady=20)
        
        self._RButton = wdgts.ControlAssignment(master=self, action="R")
        self._RButton.grid(row=0, column=3, padx=20, pady=20)
        
        self._DPadLeft = wdgts.ControlAssignment(master=self, action="Left")
        self._DPadLeft.grid(row=1, column=0, padx=20, pady=20)
        
        self._DPadUp = wdgts.ControlAssignment(master=self, action="Up")
        self._DPadUp.grid(row=1, column=1, padx=20, pady=20)
        
        self._DPadRight = wdgts.ControlAssignment(master=self, action="Right")
        self._DPadRight.grid(row=1, column=2, padx=20, pady=20)
        
        self._DPadDown = wdgts.ControlAssignment(master=self, action='Down')
        self._DPadDown.grid(row=1, column=3, padx=20, pady=20)
        
        self._selectButton = wdgts.ControlAssignment(master=self, action="Select")
        self._selectButton.grid(row=2, column=1, padx=20, pady=20)
        
        self._startButton = wdgts.ControlAssignment(master=self, action="Start")
        self._startButton.grid(row=2, column=2, padx=20, pady=20)