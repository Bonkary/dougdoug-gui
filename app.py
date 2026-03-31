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
        
        self._header = Header(master=self)
        self._header.grid(row=0, column=0, pady=30, sticky='ew')
        
        self._optionsMenu = OptionsMenu(master=self)
        self._optionsMenu.grid(row=1, column=0)
        
        self._activeApp = TwitchPlays(master=self)
        self._activeApp.grid(row=1, column=0, pady=(10,0))
        self._activeApp.hide()
        
    def change_option(self, option: str) -> None:
        if not option == 'options':
            self._optionsMenu.hide()
            self._activeApp.show()
            self._header.backButton.show()
        else:
            self._header.set_title("Select Something")
            self._optionsMenu.show()
            self._activeApp.hide()
            self._header.backButton.hide()
            
        match option:
            case 'twitch_plays':
                self._header.set_title("Twitch Plays")
                self._activeApp = TwitchPlays(master=self)
                
        self._prevOption = option
                
    def back(self) -> None:
        self.change_option(self._prevOption)

class Header(wdgts.HideableFrame):
    def __init__(self, master: MainWindow):
        super().__init__(master=master)
        self._appRoot = master
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2), weight=EQUAL_WEIGHT, uniform='column')
        
        #TODO: Get this shit to center
        self.backButton = wdgts.HideableButton(master=self, text="< Back", font=(FONT_NAME,20), command=self._appRoot.back)
        self.backButton.grid(row=0, column=0, sticky='w', padx=(30,0))
        self.backButton.hide()
        
        self._title = ctk.CTkLabel(master=self, text="Select Something", font=(FONT_NAME, 30))
        self._title.grid(row=0, column=1, sticky='ew')

    def set_title(self, title: str) -> None:
        self._title.configure(text=title)

class OptionsMenu(wdgts.HideableFrame):
    def __init__(self, master: MainWindow):
        super().__init__(master=master)
        self._appRoot = master
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self._twitchPlaysButton = ctk.CTkButton(master=self, text="Twitch Plays", font=(FONT_NAME, 30),
                                                width=400, height=60, command=lambda: self._appRoot.change_option(option='twitch_plays'))
        self._twitchPlaysButton.grid(row=0, column=0)
        
