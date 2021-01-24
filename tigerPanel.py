import json
import tkinter

w = tkinter.Tk()
w.geometry("720x720")
w.title("tigerPanel (Universal) v0.0.1")
w.iconbitmap("icon/logo_small_icon_only_inverted.ico")

def get_var(var):
    with open("config.json") as f:
        data = json.load(f)

    if var == "prefix":
        for key in data["custom"]:
            return key["prefix"]
    elif var == "oMJ":
        for key in data["custom"]:
            return key["onMemberJoin"]
    elif var == "oMR":
        for key in data["custom"]:
            return key["onMemberRemove"]
    elif var == "mOJ":
        for key in data["control"]:
            return key["messageOnRemove"]
    elif var == "mOR":
        for key in data["control"]:
            return key["messageOnRemove"]
    elif var == "ping":
        for key in data["control"]:
            return key["ping"]
    elif var == "_8Ball":
        for key in data["control"]:
            return key["_8Ball"]
    elif var == "cS":
        for key in data["control"]:
            return key["customStatus"]
    elif var == "token":
        for key in data["token"]:
            return key["token"]

def save_input():
    global input_prefix
    global input_member_join
    global input_member_remove
    global input_token
    
    custom_prefix = input_prefix.get()
    custom_member_join = input_member_join.get()
    custom_member_remove = input_member_remove.get()

    messageOnJoin = valueOJC.get()
    messageOnRemove = valueORC.get()
    ping = valueP.get()
    customStatus = valueCS.get()
    _8Ball = value8B.get()
    customToken = valueToken.get()

    data = {
        "custom": [
            {
            "prefix": custom_prefix,
            "onMemberJoin": custom_member_join,
            "onMemberRemove": custom_member_remove 
            }
        ],
        "control": [
            {
                "messageOnJoin": messageOnJoin,
                "messageOnRemove": messageOnRemove,
                "ping": ping,
                "_8Ball": _8Ball,
                "customStatus": customStatus 
            }
        ],
        "token": [
            {
                "token": customToken
            }
        ]
    }
    
    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)
    w.destroy()

valueP = tkinter.BooleanVar()
valueP.set(get_var("ping"))
valueOJC = tkinter.BooleanVar()
valueOJC.set(get_var("mOJ"))
valueORC = tkinter.BooleanVar()
valueORC.set(get_var("mOR"))
valueCS = tkinter.BooleanVar()
valueCS.set(get_var("cS"))
value8B = tkinter.BooleanVar()
value8B.set(get_var("_8Ball"))
valueToken = tkinter.StringVar()

title_custom = tkinter.Label(w, text="Customise", font=("bold", 18))

text_prefix = tkinter.Label(w, text="Single Character Command prefix:")
input_prefix = tkinter.Entry(w, width=1)
input_prefix.insert("end", get_var("prefix"))

text_member_join = tkinter.Label(w, text="Message on member join:")
input_member_join = tkinter.Entry(w, width=25)
input_member_join.insert("end", get_var("oMJ"))

text_member_remove = tkinter.Label(w, text="Message on member remove/leave:")
input_member_remove = tkinter.Entry(w, width=25)
input_member_remove.insert("end", get_var("oMR"))

title_control = tkinter.Label(w, text="Control Panel", font=("bold", 18))

checkbox_on_join = tkinter.Checkbutton(w, text="Output message to console when a player joins", variable = valueOJC)

checkbox_on_remove = tkinter.Checkbutton(w, text="Output message to console when a player is removed or leaves the server", variable=valueORC)

checkbox_ping = tkinter.Checkbutton(w, text="Enable ping-command", variable=valueP)

checkbox_8ball = tkinter.Checkbutton(w, text="Enable 8Ball-command", variable=value8B)

checkbox_customStatus = tkinter.Checkbutton(w, text="Enable custom status", variable=valueCS)

text_token = tkinter.Label(w, text="Your Discord Application token:")
input_token = tkinter.Entry(w, show="*", width=50,)
input_token.insert("end", get_var("token"))

button_save = tkinter.Button(w, text="Save & Close", command=save_input)

canvas = tkinter.Canvas(w, width=600, height=300)
img = tkinter.PhotoImage(file="icon/logo_small.png")
canvas.create_image(20, 20, anchor="nw", image=img)

title_custom.place(x=1, y=1)
text_prefix.place(x=1, y=50)
input_prefix.place(x=230, y=50)

text_member_join.place(x=1, y=80)
input_member_join.place(x=230, y=80)

text_member_remove.place(x=1, y=110)
input_member_remove.place(x=230, y=110)

title_control.place(x=1, y=160)

checkbox_on_join.place(x=1, y=210)
checkbox_on_remove.place(x=1, y=240)
checkbox_ping.place(x=1, y=270)
checkbox_8ball.place(x=1, y=300)
checkbox_customStatus.place(x=1, y=330)

text_token.place(x=1, y=360)
input_token.place(x=230, y=360)

button_save.place(x=1, y=390)
canvas.place(x=80, y=420)
input_prefix.focus_set()

w.mainloop()