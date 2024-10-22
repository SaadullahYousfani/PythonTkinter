import tkinter as tk

try:
    import tkinter 
except ImportError:
    import Tkinter as tk


def main():

    root = tk.Tk()
    root.title('Grid for Labeling is to Beat Demo')
    root.geometry('640x480-8-200')

    

    label = tk.Label(root, text="Name: ")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1)

    button = tk.Button(text="Submit or Greet")
    button.grid(row=0, column=2)

    def greet():
        name = entry.get()
        label.config(text=f'Hello, {name}!')

    button.config(command=greet)
    root.mainloop()


if __name__ == '__main__':
    main()