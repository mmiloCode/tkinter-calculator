class Calculator:
    def __init__(self):
        self.memory = 0


    def print_num(calc, btn_text):
        calc.display.insert("end", btn_text)


    def clear_display(calc):
        calc.display.delete(0, "end")
    
    def calc(calc):
        display_value = calc.display.get()
        try:
            result = eval(display_value)
            calc.display.delete(0, "end")
            calc.display.insert("end", result)
        except Exception as e:
            print(e)
    
    def set_op():
        print("opereichon")
        