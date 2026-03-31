import customtkinter as ctk
from constants import *

class HideableFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(kwargs)
        self.isHidden = False
        
    def hide(self) -> None:
        self.isHidden = True
        self.grid_remove()
        
    def show(self) -> None:
        self.isHidden = False
        self.grid()

class HideableButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(kwargs)
        self.isHidden = False
        
    def hide(self) -> None:
        self.isHidden = True
        self.grid_remove()
        
    def show(self) -> None:
        self.isHidden = False
        self.grid()

class ToggleableButton(HideableButton):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
    def enable(self) -> None:
        self.configure(state='normal')
    
    def disable(self) -> None:
        self.configure(state='disabled')
        
class ClearableEntry(HideableFrame):
    def __init__(self, master, width: int = 200, height: int = 50, font: tuple = (FONT_NAME,30)):
        super().__init__(master=master)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self._entry = ctk.CTkEntry(master=self, width=width, height=height, font=font)
        self._entry.grid(row=0, column=0)
        
        self._clearButton = HideableButton(master=self, text="X", width=height-10, height=height-10, 
                                           command=self.clear, font=(FONT_NAME,30))
        self._clearButton.grid(row=0, column=0, sticky='e', padx=(0,3))
        
    def get(self) -> str:
        return self._entry.get()
    
    def clear(self) -> None:
        self._entry.delete(0, ctk.END)

class ControlAssignment(HideableFrame):
    def __init__(self, master, action: str, **kwargs):
        super().__init__(master, **kwargs)
        self._action = action
        self.configure(fg_color=colors.TWITCH_PURPLE)
        
        self.grid_columnconfigure(index=(0,1), weight=EQUAL_WEIGHT)
        
        self._keyLabel = ctk.CTkLabel(master=self, text=action, font=(FONT_NAME, 30), width=80)
        self._keyLabel.grid(row=0, column=0, sticky='w', padx=10)
        
        self._entry = ClearableEntry(master=self)
        self._entry.grid(row=0, column=1, sticky='e', padx=10)
   
        



   
