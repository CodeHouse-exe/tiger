import json


def get_config(category, key):
    with open("config.json") as f:
        data = json.load(f)
        return data[category][key]


status = ["you like he did...", "Space Invaders", "tag with Donald Trump", "absolutely nothing"]
_8_ball_responses = {"Certainly!", "Absolutely.", "Without a doubt.", "Yes. For definite.", "You can rely on it.",
                     "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.",
                     "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now",
                     "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.",
                     "Doesn't look too good to me.", "more like a no..."}
