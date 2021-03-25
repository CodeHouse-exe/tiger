import json
import tkinter
import config

w = tkinter.Tk()
w.geometry("720x720")
w.title("tigerPanel (Universal) v0.0.1")
w.iconbitmap("icon/logo_small_icon_only_inverted.ico")

def save_input():
    global input_prefix
    global input_member_join
    global input_member_remove
    global input_token

    data = {
        "custom": [
            {
                "prefix": input_prefix.get(),
                "on_member_join": input_member_join.get(),
                "on_member_remove": input_member_remove.get()
            }
        ],
        "control": [
            {
                "message_on_join": valueOJC.get(),
                "message_on_remove": valueORC.get(),
                "ping": valueP.get(),
                "_8_ball": value8B.get(),
                "custom_status": valueCS.get()
            }
        ],
        "token": [
            {
                "token": input_token.get()
            }
        ]
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)
    w.destroy()


valueP = tkinter.BooleanVar()
valueP.set(config.get_config("control", "ping"))
valueOJC = tkinter.BooleanVar()
valueOJC.set(config.get_config("control", "messageOnJoin"))
valueORC = tkinter.BooleanVar()
valueORC.set(config.get_config("control", "messageOnRemove"))
valueCS = tkinter.BooleanVar()
valueCS.set(config.get_config("control", "customStatus"))
value8B = tkinter.BooleanVar()
value8B.set(config.get_config("control", "_8Ball"))
valueToken = tkinter.StringVar()
valueToken.set(config.get_config("token", "token"))

title_custom = tkinter.Label(w, text="Customise", font=("bold", 18))

text_prefix = tkinter.Label(w, text="Single Character Command prefix:")
input_prefix = tkinter.Entry(w, width=1)
input_prefix.insert("end", config.get_config("custom", "prefix"))

text_member_join = tkinter.Label(w, text="Message on member join:")
input_member_join = tkinter.Entry(w, width=25)
input_member_join.insert("end", config.get_config("custom", "onMemberJoin"))

text_member_remove = tkinter.Label(w, text="Message on member remove/leave:")
input_member_remove = tkinter.Entry(w, width=25)
input_member_remove.insert("end", config.get_config("custom", "onMemberRemove"))

title_control = tkinter.Label(w, text="Control Panel", font=("bold", 18))

checkbox_on_join = tkinter.Checkbutton(w, text="Output message to console when a player joins", variable=valueOJC)

checkbox_on_remove = tkinter.Checkbutton(w,
                                        text="Output message to console when a player is removed or leaves the server",
                                        variable=valueORC)

checkbox_ping = tkinter.Checkbutton(w, text="Enable ping-command", variable=valueP)

checkbox_8ball = tkinter.Checkbutton(w, text="Enable 8Ball-command", variable=value8B)

checkbox_customStatus = tkinter.Checkbutton(w, text="Enable custom status", variable=valueCS)

text_token = tkinter.Label(w, text="Your Discord Application token:")
input_token = tkinter.Entry(w, show="*", width=50)
input_token.insert("end", config.get_config("token", "token"))

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
