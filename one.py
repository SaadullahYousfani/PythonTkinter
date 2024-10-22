try:
    import tkinter
except ImportError:
    import tkinter as tk


mainWindow = tkinter.Tk()
mainWindow.title("Passion")

mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="Hello Passion")
label.pack(side='top')

left_frame = tkinter.Frame(mainWindow)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)


canvas_left = tkinter.Canvas(left_frame,  relief='raised', borderwidth=1)
canvas_left.pack( side='left', anchor='n')


right_frame = tkinter.Frame(mainWindow)
right_frame.pack(side='left', anchor='n', expand=True)


button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")


button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()