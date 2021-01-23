import tkinter
import json
import time

w = tkinter.Tk()
w.geometry("600x600")
w.title("tigerPanel (Universal) v0.0.1")

def nameInp():
    print("Hi")

def run():
    w.destroy()
    import main

messageOnJoinCheckbutton = tkinter.Checkbutton(w, text="Print a message to console when a player joins", onvalue=True, offvalue=False)
messageOnJoinCheckbutton.place(x=1, y=1)

messageOnRemoveCheckbutton = tkinter.Checkbutton(w, text="Print a message to console when a player is removed", onvalue=True, offvalue=False)
messageOnRemoveCheckbutton.place(x=1, y=30)

commandPingCheckbutton = tkinter.Checkbutton(w, text="Enable ping-command", onvalue=True, offvalue=False)
commandPingCheckbutton.place(x=1, y=60)

command8BallCheckbutton = tkinter.Checkbutton(w, text="Enable 8Ball-command", onvalue=True, offvalue=False)
command8BallCheckbutton.place(x=1, y=90)

customStatusCheckbutton = tkinter.Checkbutton(w, text="Enable custom status", onvalue=True, offvalue=False)
customStatusCheckbutton.place(x=1, y=120)

customStatusLabel = tkinter.Label(w, text="Status Interval:")
customStatusLabel.place(x=1, y=180)

customStatusInterval = tkinter.Entry(w)
customStatusInterval.place(x=100, y=180)

runButton = tkinter.Button(w, text="Run", command = run)
runButton.place(x=1, y=210)

w.mainloop()