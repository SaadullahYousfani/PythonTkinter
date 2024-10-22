import os 
import tkinter as tk

try:
    import tkinter 
except ImportError:
    import Tkinter as tk


mainWindow = tk.Tk()
mainWindow.title("File List GUI")
mainWindow.geometry("640x480-8-200")

#Block 1 Enter Text Tkinter Grid View Demo:
label = tk.Label(mainWindow, text="Tkinter Grid View Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

#Block2: Adding List Box
listBox = tk.Listbox(mainWindow)
listBox.grid(row=1, column=0, sticky='nsew', rowspan=2)

listBox.config(border=2, relief='sunken')
for zone in os.listdir('C:/Windows/System32/'):
    listBox.insert(tkinter.END, zone)


#Block3: List Box Scroll Grid
listScroll = tk.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=listBox.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)

listBox['yscrollcommand'] = listScroll.set

#Block4: Create File Details Case Label Frame:
optionsFrame = tk.LabelFrame(mainWindow, text="FileDetails")
optionsFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)

radio1 = tk.Radiobutton(optionsFrame, text="Filename", value=1, variable=rbValue)
radio2 = tk.Radiobutton(optionsFrame, text="Path", value=2, variable=rbValue)
radio3 = tk.Radiobutton(optionsFrame, text="TimeStamp", value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

print(rbValue.get())

#Block5: Result Label and Entry Field
resultLabel = tk.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result=tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#Block6: Create TimeSpinner and Frame
timeFrame = tk.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

hourSpinner = tk.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
tk.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tk.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

timeFrame['padx'] = 30

#Block:7
dateFrame = tk.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

dayLabel = tk.Label(dateFrame, text="Day")
monthLabel = tk.Label(dateFrame, text="Month")
yearLabel = tk.Label(dateFrame, text="Year")

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#date Spinner
daySpinner = tk.Spinbox(dateFrame, width=5, from_=1 ,to=31)
monthSpinner = tk.Spinbox(dateFrame, width=5, values=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
yearSpinner = tk.Spinbox(dateFrame, width=5, from_= 2020, to= 2099)

daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)

dateFrame['padx'] = 35

#Block8: Buttons

okButton1 = tk.Button(mainWindow, text="OK")
cancelButton1 = tk.Button(mainWindow, text="Cancel", command=mainWindow.destroy) 

okButton1.grid(row=4, column=3, sticky='e')
cancelButton1.grid(row=4, column=4, sticky='w')
mainWindow.mainloop()