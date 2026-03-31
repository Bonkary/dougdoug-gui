import customtkinter as ctk
from constants import *
import widgets as wdgts
from twitch_plays import TwitchPlays

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._prevOption = 'options'
        
        self.geometry(MAIN_WINDOW_SIZE)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        
        self._titleLabel = ctk.CTkLabel(master=self, text="Ez Twitch Plays", font=(FONT_NAME,30))
        self._titleLabel.grid(row=0, column=0, pady=30, sticky='ew')
        
        self._activeApp = TwitchPlays(master=self)
        self._activeApp.grid(row=1, column=0, pady=(10,0))


