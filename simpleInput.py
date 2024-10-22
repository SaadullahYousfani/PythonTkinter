import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f'Hello, {name}!')


def main():
    
    root = tk.Tk()
    root.title("Greeting App")

    global entry, label
    label = tk.Label(root, text="Enter your name: ")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=2)

    button = tk.Button(root, text="Greet", command=greet)
    button.grid(row=0, column=3)

    root.mainloop()

if __name__ == "__main__":
    main()

