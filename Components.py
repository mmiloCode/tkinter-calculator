import tkinter as tk

FONT = "System"
FONT_SIZE = 18

class Display(tk.Entry):
    def __init__(self, root):
        super().__init__(root,
                         font = (FONT, FONT_SIZE),
                         bg = "gray10",
                         fg = "white",
                        justify = "right")
        self.focus()


class Button(tk.Button):
    def __init__(self, root, text, btn_type, action):
        self.bg = ""
        self.fg = ""
        if btn_type == "op":
            self.bg = "orange"
            self.fg = "black"
        elif btn_type == "clear":
            self.bg = "red"
            self.fg = "black"
        elif btn_type == "equals":
            self.bg = "#007FFF"
            self.fg = "white"
        else:
            self.bg = "gray30"
            self.fg = "white"
        
        self.text = text

        super().__init__(root, text = self.text,
                         width = 3,
                         font = (FONT, FONT_SIZE),
                         bg = self.bg,
                         fg = self.fg,
                         cursor = "hand2",
                         command = lambda : action(self.text))
    

        
