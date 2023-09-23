import tkinter as tk
from CalculatorGUI import CalculatorGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    app.print_components()
    root.mainloop()