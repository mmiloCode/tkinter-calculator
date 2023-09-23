import tkinter as tk
from Components import Display, Button
from Calculator import Calculator


class CalculatorGUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Tkinter")
        self.root.resizable(0, 0)
        self.root.eval('tk::PlaceWindow . center')
        self.memory = "0"
        self.state = ""
        self.display = Display(self.root)
        self.display.focus()
        self.display.insert("end", 0)
        self.memory_display = Display(self.root)
        self.memory_display.config(font = ("System", 16), fg = "gray60")
        self.symbols = [
            "7", "8", "9", "/",
            "4", "5", "6", "x",
            "1", "2", "3", "-",
            "C", "0", "=", "+",
        ]

        self.btns = []
        for symbol in self.symbols:
            if symbol.isdigit():
                self.btns.append(Button(self.root, symbol, "num", self.on_click))
            elif symbol == "=":     
                self.btns.append(Button(self.root, symbol, "equals", self.on_click))
            elif symbol == "C":
                self.btns.append(Button(self.root, symbol, "clear", self.on_click))
            else: self.btns.append(Button(self.root, symbol, "op", self.on_click))


    def on_click(self, btn_text):
        if btn_text in "0123456789":
            Calculator.print_num(self, btn_text)
        elif btn_text in "/x+-":
            Calculator.operation(self, btn_text)
        elif btn_text == "C":
            Calculator.clear_display(self)
        elif btn_text == "=":
            Calculator.calc(self)


    def print_components(self):
        col = 0
        row = 2
        for btn in self.btns:
            btn.grid(column = col, row = row, sticky = "ew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        self.memory_display.grid(column = 0, row = 0, columnspan = 4, sticky = "ew", ipady = 10)
        self.display.grid(column = 0, row = 1, columnspan = 4, sticky = "ew", ipady = 10)