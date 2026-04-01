import customtkinter as ctk
import widgets as wdgts
from constants import *
from configurations import *

class EmptyScheme(wdgts.CustomFrame):
    def __init__(self, master):
        super().__init__(master=master)

    def save_scheme(self) -> None:
        pass

class GameboyControls(wdgts.CustomFrame):
    def __init__(self, panel, **kwargs):
        super().__init__(master=panel, **kwargs)
        self._panel = panel
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2,3), weight=ONLY_THESE_COLUMNS_EXIST)
        
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
        
        self._combosButton = wdgts.CustomButton(master=self, text='Open Button Combos', command=self.open_combinations,
                                                width=200, height=40, font=(FONT_NAME, 20))
        self._combosButton.grid(row=3, column=1, columnspan=2)
        
    def open_combinations(self) -> None:
        popup = GameboyControlCombinations(master=self)
        popup.wait_window()
        
    def save_control_scheme(self) -> None:
        CONTROL_SCHEMES['Gameboy'] = {
            'A': self._AButton.get_controls(),
            'B': self._BButton.get_controls(),
            'L': self._LButton.get_controls(),
            'R': self._RButton.get_controls(),
            'dpad_left': self._DPadLeft.get_controls(),
            'dpad_right': self._DPadRight.get_controls(),
            'dpad_up': self._DPadUp.get_controls(),
            'dpad_down': self._DPadDown.get_controls(),
            'start': self._DPadDown.get_controls(),
            'select': self._DPadDown.get_controls()
        }
        
class GameboyControlCombinations(wdgts.CustomToplevel):
    def __init__(self, master):
        super().__init__(master=master)
        
        self.geometry(COMBINATIONS_WINDOW_SIZE)