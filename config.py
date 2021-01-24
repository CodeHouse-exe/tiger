import json

with open("config.json") as f:
    data = json.load(f)

for key in data["custom"]:
    prefix = key["prefix"]
    onMemberJoin = key["onMemberJoin"]
    onMemberRemove = key["onMemberRemove"]

for key in data["control"]:
    messageOnJoin = key["messageOnJoin"]
    messageOnRemove = key["messageOnRemove"]
    ping = key["ping"]
    _8Ball = key["_8Ball"]
    customStatus = key["customStatus"]

status = ["you like he did...", "Space Invaders", "tag with Donald Trump", "absolutely nothing"]
_8BallResponses = ["Certainly!", "Absolutely.", "Without a doubt.", "Yes. For definite.", "You can rely on it.", "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.", "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now", "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.", "Doesn't look too good to me.", "more like a no..."]

# ERROR MESSAGES
clearMissingArg = "So, uh, how many messages do you want me to delete?"
commandNotFound = "I know no such thing."
missingPerms = "You can't do that, cheeky. Ask an admin."
spamMissingArg = "So, uh, how many messages do you want me to send?"