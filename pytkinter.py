import os 

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("World's Best App")
mainWindow.geometry('640x480-8-200')

#Block 1 and Block 2

label = tkinter.Label(mainWindow, text="Tkinter Grid View Demo")
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

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:\Windows\System32'):
    fileList.insert(tkinter.END, zone)

#Block3:
#Add Scroll Bar

ListScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
ListScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = ListScroll.set

#Block4
optionsFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionsFrame.grid(row=1, column=2, sticky='ne')
rbValue = tkinter.IntVar()
rbValue.set(2)

radio1 = tkinter.Radiobutton(optionsFrame, text="File Name", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionsFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionsFrame, text="Timestamp", value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

print(rbValue.get())

#Block5:
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')

result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#Block6:
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

hourSpinner = tkinter.Spinbox(timeFrame, width=2, values = tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4) 
timeFrame['padx'] = 35
                        
#Block7:
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

dayLabel = tkinter.Label(dateFrame, text="Date")
monthLabel= tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#Block8: Spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
yearSpinner =  tkinter.Spinbox(dateFrame, width=5, from_=2020, to=2099)

daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)
dateFrame['padx']  = 25

#Block9:

okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()