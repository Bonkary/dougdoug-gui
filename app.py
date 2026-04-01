import customtkinter as ctk
from constants import *
import widgets as wdgts
from twitch_plays import TwitchPlays

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._keymappingsPopup: ShowKeyMappings = None
        
        self.geometry(MAIN_WINDOW_SIZE)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
        self._header = Header(app_root=self)
        self._header.grid(row=0, column=0, pady=(20,0), sticky='ew')
        
        self._activeProgram = TwitchPlays(app_root=self)
        self._activeProgram.grid(row=1, column=0, pady=(10,0))
        
    def get_channel_name(self) -> None:
        return self._header._channelNameEntry.get().strip()
    
    def show_key_mappings(self) -> None:
        # NOTE: you thought "damn i might be too high for this" when you wrote this, so maybe double check it
        if not self._keymappingsPopup:
            self._keymappingsPopup = ShowKeyMappings(app_root=self)
        else:
            if self._keymappingsPopup.winfo_exists():
                return
            else:
                self._keymappingsPopup = ShowKeyMappings(app_root=self)


class Header(ctk.CTkFrame):
    def __init__(self, app_root: MainWindow):
        super().__init__(master=app_root)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=(0,1,2), weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        
        self._channelNameEntry = wdgts.NamedEntry(master=self, name="Twitch Channel", name_placement='side')
        self._channelNameEntry.grid(row=0, column=0, sticky='w', padx=(20,0))
        
        self._titleLabel = ctk.CTkLabel(master=self, text="Ez Twitch Plays", font=(FONT_NAME,30))
        self._titleLabel.grid(row=0, column=1)
        
        self._showKeyMappings = wdgts.CustomButton(master=self, text="Show Keyboard Keys", font=(FONT_NAME,20),
                                                   command=app_root.show_key_mappings)
        self._showKeyMappings.grid(row=0, column=2)
        
class ShowKeyMappings(wdgts.CustomToplevel):
    def __init__(self, app_root: MainWindow, **kwargs):
        super().__init__(app_root=app_root, **kwargs)
        self._app_root = app_root
        
        self.geometry(KEYMAPPING_WINDOW_SIZE)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
        titleFont = ctk.CTkFont(family=FONT_NAME, size=30, weight='bold', underline=True)
        self._title = wdgts.CustomLabel(master=self, text='Keyboard Keys',
                                  font=titleFont) 
        self._title.grid(row=0, column=0, pady=20)
        
        self._mappings = wdgts.CustomFrame(master=self)
        self._mappings.grid_columnconfigure(index=(0,1), weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        self._mappings.grid(row=1, column=0, sticky='news')
        row = 0
        column = 0
        for mapping in DISPLAY_KEYBOARD_MAPPING:
            wdgts.CustomLabel(master=self._mappings, text=mapping, 
                        font=(FONT_NAME, 20)).grid(row=row, column=column, sticky='ew', pady=3)
            row += 1
            if row == MAX_MAPPING_DISPLAY_ROWS:
                row = 0
                column += 1
            