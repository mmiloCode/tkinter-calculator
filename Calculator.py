class Calculator:

    def print_num(calc, btn_text):
        if calc.state == "result":
            calc.state = ""
            calc.memory_display.delete(0, "end")
            calc.display.delete(0, "end")
            calc.display.insert("end", btn_text)
        else:
            if calc.display.get() == "0":
                calc.display.delete(0, "end")
            calc.display.insert("end", btn_text)
                


    def clear_display(calc):
        calc.state = ""
        calc.display.delete(0, "end")
        calc.memory = "0"
        calc.memory_display.delete(0, "end")
        calc.display.insert("end", "0")
    
    def calc(calc):
        if calc.state != "result":
            display_value = calc.display.get()
            if display_value.startswith("0"):
                display_value = display_value [1:]
            memory_value = calc.memory_display.get()
            try:    
                op_string = str(memory_value) + str(display_value)
                result = eval(op_string)
                calc.memory_display.delete(0, "end")
                calc.memory_display.insert("end", op_string + " = ")
                calc.display.delete(0, "end")
                calc.display.insert("end", result)
            except Exception as e:
                calc.display.delete(0, "end")
                calc.memory_display.delete(0, "end")
                calc.memory = "0"
                calc.display.insert("end", "Error.")
                
                print(e)
            finally:
                calc.state = "result"
    
    def operation(calc, btn_text):
        display_value = calc.display.get()
        if calc.state != "result":
            match btn_text:
                case "+":
                    if calc.memory == "0":
                        calc.memory = ""
                    calc.memory = display_value
                    calc.memory_display.insert("end", calc.memory + " + ")
                    calc.display.delete(0, "end")
                    calc.display.insert("end", 0)
                    calc.op = "sum"
                case "-":
                    if calc.memory == "0":
                        calc.memory = ""
                    calc.memory = display_value
                    calc.memory_display.insert("end", calc.memory + " - ")
                    calc.display.delete(0, "end")
                    calc.display.insert("end", 0)
                    calc.op = "res"
                case "/":
                    if calc.memory == "0":
                        calc.memory = ""
                    calc.memory = display_value
                    calc.memory_display.insert("end", calc.memory + " / ")
                    calc.display.delete(0, "end")
                    calc.display.insert("end", 0)
                    calc.op = "res"
                case "x":
                    if calc.memory == "0":
                        calc.memory = ""
                    calc.memory = display_value
                    calc.memory_display.insert("end", calc.memory + " * ")
                    calc.display.delete(0, "end")
                    calc.display.insert("end", 0)
                    calc.op = "res"
        