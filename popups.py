import widgets as wdgts
import customtkinter as ctk
import threading
import time
from constants import *
import configurations as cfg

# KEYMAP POPUP
class ShowKeyMappings(wdgts.CustomToplevel):
    def __init__(self, app_root: ctk.CTk, **kwargs):
        super().__init__(app_root=app_root, **kwargs)
        self._app_root = app_root
        
        self.geometry(gui.KEYMAPPING_WINDOW_SIZE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        titleFont = ctk.CTkFont(family=gui.FONT_NAME, size=30, weight='bold', underline=True)
        self._title = wdgts.CustomLabel(master=self, text='Keyboard Keys',
                                  font=titleFont) 
        self._title.grid(row=0, column=0, pady=20)
        
        self._mappings = wdgts.CustomFrame(master=self)
        self._mappings.grid_columnconfigure(index=(0,1), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._mappings.grid(row=1, column=0, sticky='news')
        row = 0
        column = 0
        for mapping in keys.USER_FRIENDLY_KEYBOARD_MAPPINGS:
            wdgts.CustomLabel(master=self._mappings, text=mapping, 
                        font=(gui.FONT_NAME, 20)).grid(row=row, column=column, sticky='ew', pady=3)
            row += 1
            if row == gui.MAX_KEY_DISPLAY_ROWS:
                row = 0
                column += 1

# TUTORIAL POPUP
class Tutorial(wdgts.CustomToplevel):
    def __init__(self, app_root, **kwargs):
        super().__init__(app_root, **kwargs)
        self._appRoot = app_root
        self.geometry(gui.TUTORIAL_WINDOW_SIZE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._titleLabel = wdgts.CustomLabel(master=self, text="Hi, I'm Tute Toriel. Nice to meet you.", font=(gui.FONT_NAME,20))
        self._titleLabel.pack(pady=50)
        
        self._rewatchAnimationButton = wdgts.CustomButton(master=self, text='Watch "animation" again for some reason',
                                                          command=threading.Thread(target=self.rewatch, daemon=True).start)
        
        
        self._labels: list[wdgts.CustomLabel] = []
        self._rewatchLabels = []
        for line in text.TUTORIAL_TEXT:
             self._labels.append(
                wdgts.CustomLabel(master=self, text=line, font=(gui.FONT_NAME,20))
            )
             
        for line in text.REWATCH_TUTORIAL_TEXT:
            self._rewatchLabels.append(
                wdgts.CustomLabel(master=self, text=line, font=(gui.FONT_NAME,20))
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
        self._titleLabel.configure(text="I SAID I'M NOT DOING THIS AGAIN.", font=(gui.FONT_NAME,60), fg_color=colors.RED)
        self._rewatchAnimationButton.pack_forget()
        time.sleep(3)
        self.destroy()

# BUTTON COMBO POPUP
class ButtonComboConfigPopup(wdgts.CustomToplevel):
    def __init__(self, *, master, console: GameboyControls, **kwargs):
        super().__init__(master, **kwargs)
        self._appRoot = master
        self._console = console
        self._nextComboRow = 0
        self._nextComboColumn = 0
        self._loadedCombos = []
        
        self.geometry(gui.BUTTON_COMBO_WINDOW_SIZE)
        self.grid_columnconfigure(index=(0,1), weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        # CREATE COMBOS
        self._createCombosFrame = wdgts.CustomFrame(master=self, border_width=2, border_color='black')
        self._createCombosFrame.grid_columnconfigure(index=(0,1), weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._createCombosFrame.grid(row=0, column=0, sticky='news', pady=70, padx=20)
        
        self._title = wdgts.CustomLabel(master=self._createCombosFrame, 
                                        text='Create Button Combos', font=(gui.FONT_NAME,30))
        self._title.grid(row=0, column=0, columnspan=2)
        
        self._key1Entry = wdgts.NamedEntry(master=self._createCombosFrame, 
                                           name="Key 1", name_placement='top')
        self._key1Entry.grid(row=2, column=0, pady=5, sticky='e')
        
        self._key2Entry = wdgts.NamedEntry(master=self._createCombosFrame, 
                                           name='Key 2', name_placement='top')
        self._key2Entry.grid(row=2, column=1, pady=5, sticky='w')
        
        self._pressEntry = wdgts.NamedEntry(master=self._createCombosFrame,
                                            name='Press Command', name_placement='side')
        self._pressEntry.grid(row=3, column=0, pady=10, columnspan=2)
        
        self._holdEntry = wdgts.NamedEntry(master=self._createCombosFrame,
                                           name="Hold Command", name_placement='side')
        self._holdEntry.grid(row=4, column=0, columnspan=2)
        
        self._addButton = wdgts.CustomButton(master=self._createCombosFrame, text='Add', 
                                             command=self.add, font=(gui.FONT_NAME,20))
        self._addButton.grid(row=5, column=0, columnspan=2, pady=20)
        
        # MY BUTTON COMBOS
        self._myCombosFrame = wdgts.CustomFrame(master=self, border_width=2, border_color='black')
        self._myCombosFrame.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._myCombosFrame.grid(row=1, column=0, sticky='ew', padx=(20,0))
        
        self._myCombosLabel = wdgts.CustomLabel(master=self._myCombosFrame, text='My Combos', font=(gui.FONT_NAME,25))
        self._myCombosLabel.grid(row=0, column=0, sticky='n', pady=(0,20))
        
        self._comboNamesFrame = wdgts.CustomFrame(master=self._myCombosFrame)
        self._comboNamesFrame.grid_columnconfigure(index=(0,1), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._comboNamesFrame.grid(row=1, column=0, sticky='news')
        
        presetCombos = cfg.CONTROL_SCHEMES[self._console][PRESETS][self._console.loadedPreset][COMBO_BUTTONS]
        for comboID in presetCombos:
            combo = cfg.CONTROL_SCHEMES[self._console][COMBO_BUTTONS][comboID]
            ButtonComboDisplay(master=self._comboNamesFrame, combo=combo, console=self._console)\
                .grid(row=self._nextComboRow, 
                      column=self._nextComboColumn, 
                      pady=10, padx=60, sticky='w')
                
            self._nextComboRow += 1
            if self._nextComboRow == 3:
                self._nextComboRow = 0
                self._nextComboColumn = 1
        
        # INSTRUCTIONS
        self._instructionsFrame = wdgts.CustomFrame(master=self)
        self._instructionsFrame.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._instructionsFrame.grid(row=0, column=1, sticky='news', pady=60, padx=20, rowspan=2)
        
        self._instructions = wdgts.CustomLabel(master=self._instructionsFrame, 
                                               font=(gui.FONT_NAME, 20),
                                               text=text.COMBO_BUTTON_INSTRUCTIONS)
        self._instructions.grid(row=0, column=0)
        
        self._keyMappingFrame = wdgts.CustomFrame(master=self._instructionsFrame)
        self._keyMappingFrame.grid_columnconfigure(index=(0,1,2), weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._keyMappingFrame.grid(row=1, column=0, pady=50)
        
        buttonNamesRow = 0
        for buttonID in ALL_BUTTON_ALIASES[self._console]:
            wdgts.CustomLabel(master=self._keyMappingFrame, text=ALL_BUTTON_ALIASES[self._console][buttonID], font=(gui.FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=0, sticky='w', padx=10, pady=5)
            wdgts.CustomLabel(master=self._keyMappingFrame, text='-------------------->', font=(gui.FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=1, padx=10)
            wdgts.CustomLabel(master=self._keyMappingFrame, text=buttonID, font=(gui.FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=2, sticky='w', padx=10)
            buttonNamesRow += 1
    
    def add(self) -> None:
        key1 = self._key1Entry.get()
        key2 = self._key2Entry.get()
        press = self._pressEntry.get()
        hold = self._pressEntry.get()
        
        self.master.loadedCombos.append({
            newID: {
                "key1": key1,
                "key2": key2,
                "press": press,
                "hold": hold
            }
        })
        
        newID = len(cfg.CONTROL_SCHEMES[self._console][COMBO_BUTTONS]) + 1
        cfg.CONTROL_SCHEMES[self._console][COMBO_BUTTONS][newID] = {
            "key1": key1,
            "key2": key2,
            "press": press,
            "hold": hold
        }
        with open(files.CONTROL_SCHEMES, 'w') as schemesFile:
            schemesFile.write(json.dumps(cfg.CONTROL_SCHEMES))
        self._key1Entry.clear()
        self._key2Entry.clear()
        self._pressEntry.clear()
        self._holdEntry.clear()
        
        combo = cfg.CONTROL_SCHEMES[self._console][COMBO_BUTTONS][newID]
        newFrame = ButtonComboDisplay(master=self._comboNamesFrame, combo=combo, console=self._console)
        newFrame.grid(row=self._nextComboRow, column=self._nextComboColumn, pady=10, padx=60, sticky='w')
        
        self._nextComboRow += 1
        if self._nextComboRow == 3:
            self._nextComboRow = 0
            self._nextComboColumn = 1

class ButtonComboDisplay(wdgts.CustomFrame):
    def __init__(self, master, combo: dict, console: str):
        super().__init__(master)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        comboFont = ctk.CTkFont(family=gui.FONT_NAME, weight='bold', size=19)
        button1Name = ALL_BUTTON_ALIASES[console][combo['key1']]
        button2Name = ALL_BUTTON_ALIASES[console][combo['key2']] 
        self._comboName = wdgts.CustomLabel(master=self, text=f'{button1Name} + {button2Name}', font=comboFont)
        self._comboName.grid(row=0, column=0)
        
        self._pressCmd = wdgts.CustomLabel(master=self, text=f'Press: {combo["press"]}', font=(gui.FONT_NAME,15))
        self._pressCmd.grid(row=1, column=0, padx=(20,0), sticky='w')
        
        self._holdCmd = wdgts.CustomLabel(master=self, text=f'Hold: {combo["hold"]}', font=(gui.FONT_NAME,15))
        self._holdCmd.grid(row=2, column=0, padx=(20,0), sticky='w')

# OTHER POPUPS
class Countdown(wdgts.CustomToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        



