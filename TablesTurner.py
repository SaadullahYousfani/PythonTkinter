try:
    import tkinter as tk
except ImportError:
    print("Use Correct Import")


def display_table():
    try:
        num = int(entry.get())
        table = ""
        for i in range(1, 12):
            table += f'{num} x {i} = {num * i}\n'

        result_label.config(text=table)

    except:
        result_label.config(text="Please Enter a number valid input")


def main():
    root = tk.Tk()
    root.title("Main Window Tables")
    root.geometry("800x600-2-200")

    global entry, result_label

    label = tk.Label(root, text="Enter a number:")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1)

    button = tk.Button(root, text="Click to Generate", command=display_table)
    button.grid(row=0, column=2)


    result_label = tk.Label(text="")
    result_label.grid(row=1, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()
    
### 4 time Practice 