import json

with open("config.json") as f:
    data = json.load(f)

for key in data["custom"]:
    prefix = key["prefix"]
    on_member_join = key["onMemberJoin"]
    on_member_remove = key["onMemberRemove"]

for key in data["control"]:
    message_on_join = key["messageOnJoin"]
    message_on_remove = key["messageOnRemove"]
    ping = key["ping"]
    _8_ball = key["_8Ball"]
    custom_status = key["customStatus"]

for key in data["token"]:
    token = key["token"]

status = ["you like he did...", "Space Invaders", "tag with Donald Trump", "absolutely nothing"]
_8_ball_responses = {"Certainly!", "Absolutely.", "Without a doubt.", "Yes. For definite.", "You can rely on it.",
                    "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.",
                    "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now",
                    "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.",
                    "Doesn't look too good to me.", "more like a no..."}

# ERROR MESSAGES
clear_missing_arg = "So, uh, how many messages do you want me to delete?"
command_not_found = "I know no such thing."
missing_perms = "You can't do that, cheeky. Ask an admin."
spam_missing_arg = "So, uh, how many messages do you want me to send?"
