try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


mainWindow = tk.Tk()
mainWindow.title("Settings")
mainWindow.geometry('640x480-8-200')


def main():

    label = tk.Label(mainWindow, text="What is your Name: ")
    label.pack()

    entry = tk.Entry()
    entry.pack()


   

    def greet():
        name = entry.get()

        if name:
            label.config(text=f'Hello:  {name}!')
        else:
            label.config(text="What it is, anyway?")


    button = tk.Button(mainWindow, text='Greet', command=greet)
    button.pack()

    
    mainWindow.mainloop()
if __name__ == '__main__':
    main()