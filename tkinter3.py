import tkinter as tk

def change_text():
    label.config(text="Button Clicked!")


def main():
    
    root = tk.Tk()
    root.geometry("640x480-10-200")
    root.title("Tables Turned into Numbers")
    
    global label
    label = tk.Label(root, text="Click the Button")
    label.grid(row=0, column=0)

    button = tk.Button(root, text="Click Me", command=change_text)
    button.grid(row=0, column=1)

    root.mainloop()



if __name__ == "__main__":
    main()