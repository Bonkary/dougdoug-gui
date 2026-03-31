import customtkinter as ctk
import widgets as wdgts
from constants import *
from control_schemes import *
from configurations import *

class TwitchPlays(wdgts.CustomFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(0, weight=EQUAL_WEIGHT)
        
        self._consoleSelector = ConsoleSelector(master=self, app=self)
        self._consoleSelector.grid(row=0, column=0, pady=(0,20))
        
        self._instructions = ctk.CTkLabel(master=self, text="In the text box, enter the phrase for chat to use for that key", font=(FONT_NAME,20))
        self._instructions.grid(row=1, column=0)
        
        self._controlAssignmentPanel = ControlAssignmentPanel(master=self)
        self._controlAssignmentPanel.grid(row=2, column=0)
        
        self._startPlayingButton = wdgts.ToggleableButton(master=self, text='Start Playing!', command=self.start_playing,
                                                          width=500, height=50, font=(FONT_NAME,25))
        self._startPlayingButton.grid(row=3, column=0, pady=(50,0))
        self._startPlayingButton.hide()
        
        self._stopPlayingButton = wdgts.ToggleableButton(master=self, text='Stop Playing...', command=self.stop_playing,
                                                         width=500, height=50, font=(FONT_NAME,25), fg_color='red')
        self._stopPlayingButton.grid(row=3, column=0, pady=(50,0))
        self._stopPlayingButton.hide()
        
        
    def assign_controls(self) -> None:
        pass
    
    def start_playing(self) -> None:
        self._stopPlayingButton.show()
        self._startPlayingButton.hide()
        
    def stop_playing(self) -> None:
        self._stopPlayingButton.hide()
        self._startPlayingButton.show()
        
    def change_console(self, console: str) -> None:
        if self._startPlayingButton.isHidden:
            self._startPlayingButton.show()
        self._controlAssignmentPanel.set_console(console)

class ConsoleSelector(wdgts.CustomFrame):
    def __init__(self, master, app: TwitchPlays):
        super().__init__(master=master)
        self._app = app
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        self._label = ctk.CTkLabel(master=self, text="Select Console", font=(FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = ctk.CTkComboBox(master=self, values=AVAILABLE_CONSOLES, 
                                         width=230, height=40, font=(FONT_NAME, 20), 
                                         state='readonly', command=self._app.change_console)
        self._dropdown.grid(row=1, column=0)
        

class ControlAssignmentPanel(wdgts.CustomFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        
        self._activeControlScheme = EmptyScheme(master=self)
        self._activeControlScheme.grid(row=0, column=0)
        self._activeControlScheme.hide()

    def set_console(self, console: str) -> None:
        match console:
            case 'Gameboy':
                self._activeControlScheme = GameboyControls(master=self)
                self._activeControlScheme.show()


