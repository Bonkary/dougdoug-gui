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

class CustomLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.isHidden = False
    
    def show(self) -> None:
        self.isHidden = False
        self.grid()
        
    def hide(self) -> None:
        self.isHidden = True
        self.grid_remove()

class CustomToplevel(ctk.CTkToplevel):
    def __init__(self, app_root: ctk.CTk, **kwargs):
        super().__init__(master=app_root, **kwargs)
        self._appRoot = app_root
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.wm_transient(app_root)
        self.focus()

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
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
        self._entry = ctk.CTkEntry(master=self, width=width, height=height, font=font, justify=justify)
        self._entry.grid(row=0, column=0)
        
        self._clearButton = CustomButton(master=self, text="X", height=10, width=10, 
                                           command=self.clear, font=(FONT_NAME,font[1]-5))
        self._clearButton.grid(row=0, column=0, sticky='e', padx=(0,3))
        
    def get(self) -> str:
        return self._entry.get()
    
    def clear(self) -> None:
        self._entry.delete(0, ctk.END)

    def set(self, value) -> None:
        self._entry.insert(0, value)

class NamedEntry(CustomFrame):
    def __init__(self, master, name: str, **kwargs):
        super().__init__(master=master, **kwargs)
        self._name = name
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1), weight=ONLY_THESE_COLUMNS_EXIST)
        
        self._nameLabel = ctk.CTkLabel(master=self, text=name, font=(FONT_NAME,20), width=5)
        self._nameLabel.grid(row=0, column=0, sticky='w', padx=(0,10))
        
        self._entry = ClearableEntry(master=self, height=10)
        self._entry.grid(row=0, column=1, sticky='e')
        
    def get(self) -> str:
        return self._entry.get().strip()
    
    def set(self, value) -> None:
        self._entry.set(value)

        
        


        
    

