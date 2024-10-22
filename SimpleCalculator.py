try:
    import tkinter as tk
except ImportError:
    print("Error Import") 

print("calculator in progress")




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



root = tk.Tk()
root.title("Basic GUI Calculator")

root.geometry("500x500")

entry = tk.Entry(root, width=25, font=("Arial", 24), borderwidth=3, relief="solid")
entry.grid(row=0, column=0, columnspan=4)


button7 = tk.Button(root, text="7", command=lambda: entry.insert(tk.END, "7"), height=2, width=5, font=('Arial', 18))
button8 = tk.Button(root, text="8", command=lambda: entry.insert(tk.END, "8"), height=2, width=5, font=('Arial', 18))
button9 = tk.Button(root, text="9", command=lambda: entry.insert(tk.END, "9"), height=2, width=5, font=('Arial', 18))
button_divide = tk.Button(root, text="/", command=lambda: entry.insert(tk.END, "/"), height=2, width=5, font=('Arial',18))

button4 = tk.Button(root, text="4", command=lambda: entry.insert(tk.END, "4"), height=2, width=5, font=('Arial', 18))
button5 = tk.Button(root, text="5", command=lambda: entry.insert(tk.END, "5"), height=2, width=5, font=('Arial', 18))
button6 = tk.Button(root, text="6", command=lambda: entry.insert(tk.END, "6"), height=2, width=5, font=('Arial', 18))
buttonmultiply = tk.Button(root, text="*", command=lambda: entry.insert(tk.END, "*"), height=2, width=5, font=('Arial', 18))

button1 = tk.Button(root, text="1", command=lambda: entry.insert(tk.END, "1"), height=2, width=5, font=('Arial', 18))
button2 = tk.Button(root, text="2", command=lambda: entry.insert(tk.END, "2"), height=2, width=5, font=('Arial', 18))
button3 = tk.Button(root, text="3", command=lambda: entry.insert(tk.END, "3"), height=2, width=5, font=('Arial', 18))
buttonsubtract = tk.Button(root, text="-", command=lambda: entry.insert(tk.END, "-"), height=2, width=5, font=('Arial', 18))

button0 = tk.Button(root, text="0", command=lambda: entry.insert(tk.END, "0"), height=2, width=5, font=('Arial', 18))
buttondot = tk.Button(root, text=".", command=lambda: entry.insert(tk.END, "."), height=2, width=5, font=('Arial', 18))
buttonequals = tk.Button(root, text="=", command=calculate, height=2, width=5, font=('Arial', 18))
buttonplus = tk.Button(root, text="+", command=lambda: entry.insert(tk.END, "+"), height=2, width=5,  font=('Arial', 18))

buttonCE = tk.Button(root, text="CE", command=lambda:  entry.delete(0, tk.END), height=2, width=5, font=('Arial', 18))
buttondelete = tk.Button(root, text="DEL", command=delete_last_character, height=2, width=5, font=('Arial', 18))
buttonClear = tk.Button(root, text="C", command=lambda: entry.delete(0, tk.END), height=2, width=5, font=('Arial', 18))
buttonPercentage = tk.Button(root, text="%", command=lambda: entry.insert(tk.END, "%"), height=2, width=5, font=('Arial', 18))


button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
button_divide.grid(row=1, column=3, padx=5, pady=5)

button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
buttonmultiply.grid(row=2, column=3, padx=5, pady=5)

button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
buttonsubtract.grid(row=3, column=3, padx=5, pady=5)

button0.grid(row=4, column=0, padx=5, pady=5)
buttondot.grid(row=4, column=1, padx=5, pady=5)
buttonequals.grid(row=4, column=2, padx=5, pady=5)
buttonplus.grid(row=4, column=3, padx=5, pady=5)

buttonCE.grid(row=5, column=0, padx=5, pady=5)
buttondelete.grid(row=5, column=1, padx=5, pady=5)
buttonClear.grid(row=5, column=2, padx=5, pady=5)
buttonPercentage.grid(row=5, column=3, padx=5, pady=5)


root.mainloop()