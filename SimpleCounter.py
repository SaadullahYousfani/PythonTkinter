try:
    import tkinter as tk
except ImportError:
    print("Use Correct Import")

def increase_number():
    global count
    count += 1
    label.config(text=f"Counter: {count}")

def main():
    global count, label
    count = 0

    root = tk.Tk()
    root.title("Simple Counter Increment: ")
    root.geometry("640x480-8-10")

    label = tk.Label(root, text=f"Counter: {count}!")
    label.grid(row=0, column=0)

    button = tk.Button(root, text="Click to Increment!", command=increase_number)
    button.grid(row=0, column=1)
    
    root.mainloop()


if __name__ == "__main__":
    main()