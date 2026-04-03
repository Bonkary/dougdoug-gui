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
        self.configure(fg_color=colors.TWITCH_PURPLE, text_color=colors.DEFAULT_TEXT)
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

class CustomComboBox(ctk.CTkComboBox):
    def __init__(self, master, values: list[str] = [], **kwargs):
        super().__init__(master=master, **kwargs)
        self.isHidden = False
        self._values = values
        self.configure(values=self._values)

    def hide(self) -> None:
        self.isHidden = True
        self.grid_remove()

    def show(self) -> None:
        self.isHidden = False
        self.grid()

    def fill(self, values: list[str]) -> None:
        self.configure(values=values)

    def add(self, value: str) -> None:
        print(self._values)
        self._values.append(value)
        self.configure(values=self._values)

    def show_invald(self) -> None:
        self.configure(bg_color=colors.RED)


class ToggleableButton(CustomButton):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
    def enable(self) -> None:
        self.configure(state='normal')
    
    def disable(self) -> None:
        self.configure(state='disabled')
        
class ClearableEntry(CustomFrame):
    def __init__(self, master, width: int = 200, height: int = 50, font: tuple = (gui.FONT_NAME,20), justify: str = 'left'):
        super().__init__(master=master)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._entry = ctk.CTkEntry(master=self, width=width, height=height, font=font, justify=justify)
        self._entry.grid(row=0, column=0)
        
        self._clearButton = CustomButton(master=self, text="X", height=10, width=10, 
                                           command=self.clear, font=(gui.FONT_NAME,font[1]-5))
        self._clearButton.grid(row=0, column=0, sticky='e', padx=(0,3))
        
    def get(self) -> str:
        return self._entry.get()
    
    def clear(self) -> None:
        self._entry.delete(0, ctk.END)

    def set(self, value) -> None:
        self._entry.insert(0, value)

class NamedEntry(CustomFrame):
    def __init__(self, master, name: str, name_placement: str, **kwargs):
        super().__init__(master=master, **kwargs)
        self._name = name
        match name_placement:
            case 'side':
                configureColumns = (0,1)
                entryRow = 0
                entryColumn = 1
                nameSticky = 'e'
                entrySticky = 'e'
            case 'top':
                configureColumns = (0)
                entryRow = 1
                entryColumn = 0
                nameSticky = 'ew'
                entrySticky = 'ew'
            case _:
                raise ValueError(f'{name_placement} is not a valid option.')
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=configureColumns, weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        
        self._nameLabel = CustomLabel(master=self, text=name, font=(gui.FONT_NAME,20), width=5)
        self._nameLabel.grid(row=0, column=0, sticky=nameSticky, padx=(0,10))
        
        self._entry = ClearableEntry(master=self, height=10)
        self._entry.grid(row=entryRow, column=entryColumn, sticky=entrySticky)
        
    def get(self) -> str:
        return self._entry.get().strip()
    
    def set(self, value) -> None:
        self._entry.set(value)

    def clear(self) -> None:
        self._entry.clear()


        


        
    

