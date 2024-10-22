def eval_expressions(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error NaN"

def calculate():
    expression = entry.get()
    result = eval_expressions(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)


    
def delete_last_character():
    current = entry.get() #current= entry.get()  is used to get the current value of the entry field
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])