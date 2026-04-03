import customtkinter as ctk
from constants import *
import widgets as wdgts
import configurations as cfg
import time
import threading
import popups
from console_manager import Console
from platform_connection import *
from keyboard_control import keyboard_execute_thread


### MAIN WINDOW
class AppRoot(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._keymappingsPopup: popups.ShowKeyMappings = None
        self._tutorialPopup: popups.Tutorial = None
        
        self.geometry(gui.MAIN_WINDOW_SIZE)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._header = Header(app_root=self)
        self._header.grid(row=0, column=0, pady=(20,0), sticky='ew')
        
        self._activeProgram = TwitchPlays(app_root=self)
        self._activeProgram.grid(row=1, column=0, pady=(60,0))
        
    def get_channel_name(self) -> None:
        return self._header._channelNameEntry.get().strip()
    
    def show_key_mappings(self) -> None:
        if self._keymappingsPopup:
            if self._keymappingsPopup.winfo_exists():
                return
        self._keymappingsPopup = popups.ShowKeyMappings(app_root=self)

    def show_tutorial(self) -> None:
        if self._tutorialPopup:
            if self._tutorialPopup.winfo_exists():
                return
        self._tutorialPopup = popups.Tutorial(app_root=self)

class Header(ctk.CTkFrame):
    def __init__(self, app_root: AppRoot):
        super().__init__(master=app_root)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=(0,1,2), weight=gui.FIXED_SIZE, uniform=gui.EQUAL_SIZED_COLUMNS)
        
        self._channelNameEntry = wdgts.NamedEntry(master=self, name="Twitch Channel", name_placement='side')
        self._channelNameEntry.grid(row=0, column=0, sticky='w', padx=(20,0))
        self._channelNameEntry.set(cfg.SETTINGS['twitch_channel'])
        
        self._titleLabel = wdgts.CustomLabel(master=self, text="Ez Twitch Plays", font=(gui.FONT_NAME,30))
        self._titleLabel.grid(row=0, column=1, sticky='ew')
        
        self._buttonsFrame = wdgts.CustomFrame(master=self)
        self._buttonsFrame.grid_columnconfigure(index=(0,1), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._buttonsFrame.grid(row=0, column=2, columnspan=2)
        
        self._tutorialButton = wdgts.CustomButton(master=self._buttonsFrame, text='Tutorial', font=(gui.FONT_NAME,20),
                                                  command=app_root.show_tutorial, width=200)
        self._tutorialButton.grid(row=0, column=0, padx=(0,10))
        
        self._showKeyMappings = wdgts.CustomButton(master=self._buttonsFrame, text="Keyboard Keys", font=(gui.FONT_NAME,20),
                                                   command=app_root.show_key_mappings, width=200)
        self._showKeyMappings.grid(row=0, column=1, padx=(10,0))


class TwitchPlays(wdgts.CustomFrame):
    def __init__(self, app_root: AppRoot):
        super().__init__(master=app_root)
        self._appRoot = app_root
        self._listenerThread: threading.Thread = None
        self._executeThread: threading.Thread = None
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._consoleManager = Console(app=self)
        self._consoleManager.grid(row=2, column=0, sticky='news')
        
        self._alertLabel = wdgts.CustomLabel(master=self, text='', text_color='red', font=(gui.FONT_NAME, 20))
        self._alertLabel.grid(row=3, column=0, pady=(5,0))
        
        self.startButton = wdgts.ToggleableButton(master=self, text='Start Playing!', command=self.start_playing,
                                                          width=500, height=50, font=(gui.FONT_NAME,25))
        self.startButton.grid(row=4, column=0, pady=(10,0))
        self.startButton.hide()
        
        self._pauseButton = wdgts.ToggleableButton(master=self, text='Pause Playing...', command=self.stop_playing,
                                                         width=500, height=50, font=(gui.FONT_NAME,25), 
                                                         fg_color='red')
        self._pauseButton.grid(row=4, column=0, pady=(10,0))
        self._pauseButton.hide()
    
    def set_alert(self, message: str, is_persistant: bool = True) -> None:
        self._alertLabel.configure(text=message)
        if not is_persistant:
            time.sleep(2)
            self.clear_alert()
    
    def clear_alert(self) -> None:
        self._alertLabel.configure(text='')
    
    def assign_controls(self) -> None:
        pass
    
    def start_playing(self) -> None:
        # TODO: check that all controls are inputted
        if not self._appRoot.get_channel_name():
            self.set_alert("You need to enter your channel name!")
        else:
            self.clear_alert()
            self._pauseButton.show()
            self.startButton.hide()
            
            if not TWITCH_MANAGER.is_connected():
                TWITCH_MANAGER.connect(channel_name=self._appRoot.get_channel_name())
            controls = self._consoleManager.get_controls()
            
            popup = popups.Countdown(master=self)
            popup.wait_window()
                
            self._listenerThread = threading.Thread(target=TWITCH_MANAGER.listen_forever_thread, daemon=True).start()
            self._executeThread = threading.Thread(target=keyboard_execute_thread, args=(controls,), daemon=True).start()
            
            LISTENER_THREAD_FLAG.set()
            EXECUTOR_THREAD_FLAG.set()
            

    def stop_playing(self) -> None:
        KILL_FLAG.set()
        self._pauseButton.hide()
        self.startButton.show()
        
    
    def change_console(self, console: str) -> None:
        if self.startButton.isHidden:
            self.startButton.show()
        if self.presetSelector.isHidden:
            self.presetSelector.show()
        self._consoleManager.change_console(console)
        
    def change_preset(self, preset: str) -> None:
        self._consoleManager.load_preset(preset)






