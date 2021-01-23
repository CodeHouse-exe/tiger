import tkinter
import json

w = tkinter.Tk()
w.geometry("600x600")
w.title("tigerPanel (Universal) v0.0.1")

def nameInp():
    global customStatusInterval
    oJC = valueOJC.get()
    oRC = valueORC.get()
    pC = valuePC.get()
    _8BC = value8BC.get()
    sC = valueSC.get()
    interval = customStatusInterval.get()   #Der interval ist die Zahl die du eingegeben hast

def start():
    w.destroy()
    print("Starting...")
    import main

valueOJC = tkinter.IntVar()                 #Das muss da hin, weil das ein integer ist der dann returnt werden muss, und das tkinter.IntVar() gibt diese zahl als int zurück, was weiter benutzt werden kann
valueORC = tkinter.IntVar()
valuePC = tkinter.IntVar()
value8BC = tkinter.IntVar()
valueSC = tkinter.IntVar()

messageOnJoinCheckbutton = tkinter.Checkbutton(w, text="Print a message to console when a player joins", variable = valueOJC)
messageOnRemoveCheckbutton = tkinter.Checkbutton(w, text="Print a message to console when a player is removed", variable = valueORC)
commandPingCheckbutton = tkinter.Checkbutton(w, text="Enable ping-command", variable = valuePC)
command8BallCheckbutton = tkinter.Checkbutton(w, text="Enable 8Ball-command", variable = value8BC)
customStatusCheckbutton = tkinter.Checkbutton(w, text="Enable custom status", variable = valueSC)
customStatusLabel = tkinter.Label(w, text="Status Interval:")
customStatusInterval = tkinter.Entry(w)
customStatusInteger = tkinter.Button(w, text = "Click here once options are chosen", command = nameInp)
runButton = tkinter.Button(w, text = "Run", command = start)

messageOnJoinCheckbutton.place(x=1, y=1)
messageOnRemoveCheckbutton.place(x=1, y=30)
commandPingCheckbutton.place(x=1, y=60)
command8BallCheckbutton.place(x=1, y=90)
customStatusCheckbutton.place(x=1, y=120)
customStatusLabel.place(x=1, y=180)
customStatusInterval.place(x=100, y=180)
customStatusInterval.focus_set()
customStatusInteger.place(x = 1, y = 240)
runButton.place(x = 1, y = 210)
w.mainloop()