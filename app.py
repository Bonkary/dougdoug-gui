import customtkinter as ctk
from constants import *
import widgets as wdgts
from twitch_plays import TwitchPlays
import configurations as cfg
import time
import threading

class AppRoot(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._keymappingsPopup: ShowKeyMappings = None
        self._tutorialPopup: Tutorial = None
        
        self.geometry(MAIN_WINDOW_SIZE)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
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
        self._keymappingsPopup = ShowKeyMappings(app_root=self)

    def show_tutorial(self) -> None:
        if self._tutorialPopup:
            if self._tutorialPopup.winfo_exists():
                return
        self._tutorialPopup = Tutorial(app_root=self)

class Header(ctk.CTkFrame):
    def __init__(self, app_root: AppRoot):
        super().__init__(master=app_root)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=(0,1,2), weight=FIXED_SIZE, uniform=EQUAL_SIZED_COLUMNS)
        
        self._channelNameEntry = wdgts.NamedEntry(master=self, name="Twitch Channel", name_placement='side')
        self._channelNameEntry.grid(row=0, column=0, sticky='w', padx=(20,0))
        
        self._titleLabel = wdgts.CustomLabel(master=self, text="Ez Twitch Plays", font=(FONT_NAME,30))
        self._titleLabel.grid(row=0, column=1, sticky='ew')
        
        
        self._buttonsFrame = wdgts.CustomFrame(master=self)
        self._buttonsFrame.grid_columnconfigure(index=(0,1), weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        self._buttonsFrame.grid(row=0, column=2, columnspan=2)
        
        self._tutorialButton = wdgts.CustomButton(master=self._buttonsFrame, text='Tutorial', font=(FONT_NAME,20),
                                                  command=app_root.show_tutorial, width=200)
        self._tutorialButton.grid(row=0, column=0, padx=(0,10))
        
        self._showKeyMappings = wdgts.CustomButton(master=self._buttonsFrame, text="Keyboard Keys", font=(FONT_NAME,20),
                                                   command=app_root.show_key_mappings, width=200)
        self._showKeyMappings.grid(row=0, column=1, padx=(10,0))
        
class ShowKeyMappings(wdgts.CustomToplevel):
    def __init__(self, app_root: AppRoot, **kwargs):
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
    
class Tutorial(wdgts.CustomToplevel):
    def __init__(self, app_root, **kwargs):
        super().__init__(app_root, **kwargs)
        self._appRoot = app_root
        self.geometry(TUTORIAL_WINDOW_SIZE)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
        self._titleLabel = wdgts.CustomLabel(master=self, text="Hi, I'm Tute Toriel. Nice to meet you.", font=(FONT_NAME,20))
        self._titleLabel.pack(pady=50)
        
        self._rewatchAnimationButton = wdgts.CustomButton(master=self, text='Watch "animation" again for some reason',
                                                          command=threading.Thread(target=self.rewatch, daemon=True).start)
        
        
        self._labels: list[wdgts.CustomLabel] = []
        self._rewatchLabels = []
        for line in text.TUTORIAL_TEXT:
             self._labels.append(
                wdgts.CustomLabel(master=self, text=line, font=(FONT_NAME,20))
            )
             
        for line in text.REWATCH_TUTORIAL_TEXT:
            self._rewatchLabels.append(
                wdgts.CustomLabel(master=self, text=line, font=(FONT_NAME,20))
            )
        
        if cfg.SETTINGS['seen_tutorial']:
            for label in self._labels:
                if label == self._labels[-1]: # Don't show the "you can close me now" text
                    break 
                label.pack(pady=20)
            self._rewatchAnimationButton.pack(pady=5)
        else:
            threading.Thread(target=self.animation, daemon=True).start()
            
    
    def animation(self) -> None:
        '''
        This is the thread for the animation. I threw this together and it works but may be ugly.
        '''
        time.sleep(2) # This is so the first message shows up faster than the longer ones.
        for label in self._labels:
            self._appRoot.update()
            if label == self._labels[-1]:
                self._appRoot.update()
                time.sleep(10)
                label.pack(pady=15)
                break
            label.pack(pady=20)
            time.sleep(5)
        self._rewatchAnimationButton.pack(pady=5)
        cfg.SETTINGS['seen_tutorial'] = True
        cfg.update_settings_file()
        
    def rewatch(self) -> None:
        '''Plays the animation again. But different.'''
        self._rewatchAnimationButton.pack_forget()
        self._titleLabel.configure(text="Hey, it's Tute Toriel... again.")
        for label in self._labels:
            label.pack_forget()
        
        for label in self._rewatchLabels:
            time.sleep(3)
            label.pack(pady=15)
        time.sleep(1)
        self._rewatchAnimationButton.configure(command=threading.Thread(target=self.rewatch2, daemon=True).start)
        self._rewatchAnimationButton.pack(pady=5)
        self.update()
        
    def rewatch2(self) -> None:
        '''Another replay, but a he's bit frustrated.'''
        for label in self._rewatchLabels:
            label.pack_forget()
        self._titleLabel.configure(text="I said I'm not doing this again.")
        self._rewatchAnimationButton.configure(command=threading.Thread(target=self.rewatch3, daemon=True).start)
        
    def rewatch3(self) -> None:
        '''He's angry.'''
        self._titleLabel.configure(text="I SAID I'M NOT DOING THIS AGAIN.", font=(FONT_NAME,60), fg_color=colors.RED)
        self._rewatchAnimationButton.pack_forget()
        time.sleep(3)
        self.destroy()