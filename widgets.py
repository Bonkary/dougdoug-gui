import customtkinter as ctk
from constants import *

class CustomFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.configure(kwargs)
        self.isHidden = False
        
    def hide(self) -> None:
        self.isHidden = True
        self.grid_remove()
        
    def show(self) -> None:
        self.isHidden = False
        self.grid()

class CustomButton(ctk.CTkButton):
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

class CustomToplevel(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.wm_transient(master)
        self.focus()
        self.grab_set()

class ToggleableButton(CustomButton):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
    def enable(self) -> None:
        self.configure(state='normal')
    
    def disable(self) -> None:
        self.configure(state='disabled')
        
class ClearableEntry(CustomFrame):
    def __init__(self, master, width: int = 200, height: int = 50, font: tuple = (FONT_NAME,20), justify: str = 'left'):
        super().__init__(master=master)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        
        self._entry = ctk.CTkEntry(master=self, width=width, height=height, font=font, justify=justify)
        self._entry.grid(row=0, column=0)
        
        self._clearButton = CustomButton(master=self, text="X", height=10, width=10, 
                                           command=self.clear, font=(FONT_NAME,font[1]-5))
        self._clearButton.grid(row=0, column=0, sticky='e', padx=(0,3))
        
    def get(self) -> str:
        return self._entry.get()
    
    def clear(self) -> None:
        self._entry.delete(0, ctk.END)

class ControlAssignment(CustomFrame):
    def __init__(self, master, action: str, **kwargs):
        super().__init__(master, **kwargs)
        self._action = action
        self.grid_columnconfigure(index=(0), weight=EQUAL_WEIGHT, uniform='column')
        
        self._keyLabel = ctk.CTkLabel(master=self, text=action, font=(FONT_NAME, 30), width=80)
        self._keyLabel.grid(row=0, column=0, padx=(20,0))
        
        self._pressEntry = NamedEntry(master=self, name="Press")
        self._pressEntry.grid(row=1, column=0, pady=2, sticky='ew', columnspan=3)
        
        self._holdEntry = NamedEntry(master=self, name="Hold")
        self._holdEntry.grid(row=2, column=0, pady=2, sticky='ew', columnspan=3)
   
class NamedEntry(CustomFrame):
    def __init__(self, master, name: str, **kwargs):
        super().__init__(master=master, **kwargs)
        self._name = name
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1), weight=EQUAL_WEIGHT)
        
        self._nameLabel = ctk.CTkLabel(master=self, text=name, font=(FONT_NAME,20), width=5)
        self._nameLabel.grid(row=0, column=0, sticky='w', padx=(0,5))
        
        self._entry = ClearableEntry(master=self, height=10)
        self._entry.grid(row=0, column=1, sticky='e')
        


