import customtkinter as ctk
import widgets as wdgts
from constants import *
from control_schemes import *
# from keyboard_control import *

class TwitchPlays(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(0, weight=EQUAL_WEIGHT)
        
        self._consoleSelector = ConsoleSelector(master=self)
        self._consoleSelector.grid(row=0, column=0, pady=(0,20))
        
        self._instructions = ctk.CTkLabel(master=self, text="In the text box, enter the phrase for chat to use for that key", font=(FONT_NAME,20))
        self._instructions.grid(row=1, column=0)
        
        self._controlAssignmentPanel = ControlAssignmentPanel(master=self)
        self._controlAssignmentPanel.grid(row=2, column=0)
        
        self._startPlayingButton = wdgts.ToggleableButton(master=self, text='Start Playing!', command=self.start_playing,
                                                          width=500, height=50, font=(FONT_NAME,25))
        self._startPlayingButton.grid(row=3, column=0, pady=(50,0))
        
        self._stopPlayingButton = wdgts.ToggleableButton(master=self, text='Stop Playing...', command=self.stop_playing,
                                                         width=500, height=50, font=(FONT_NAME,25), fg_color='red')
        self._stopPlayingButton.grid(row=3, column=0, pady=(50,0))
        self._stopPlayingButton.hide()
        
        self._status = ctk.CTkLabel(master=self, text=f"Status: Not Playing", font=(FONT_NAME, 30), text_color='red')
        # self._status.grid(row=4, column=0)
        
    def assign_controls(self) -> None:
        pass
    
    def start_playing(self) -> None:
        self._status.configure(text='Status: Playing!', text_color='green')
        self._stopPlayingButton.show()
        self._startPlayingButton.hide()
        
    def stop_playing(self) -> None:
        self._status.configure(text='Status: Not Playing...', text_color='red')
        self._stopPlayingButton.hide()
        self._startPlayingButton.show()


class ConsoleSelector(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        self._label = ctk.CTkLabel(master=self, text="Select Console", font=(FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = ctk.CTkComboBox(master=self, values=AVAILABLE_CONSOLES, 
                                         width=230, height=40, font=(FONT_NAME, 20))
        self._dropdown.grid(row=1, column=0)

class ControlAssignmentPanel(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        
        self.gameboyControls = GameboyControls(master=self)
        self.gameboyControls.grid(row=0, column=0)






