class Event:

    def __init__(self, event_type, name, happiness, health, satiety, energy):
        self.type = event_type
        self.name = name
        self.happiness = happiness
        self.health = health
        self.satiety = satiety
        self.energy = energy


class Telagochi:
    happiness_smiles = ["💀", "😭", "😫", "😕", "😄", "😀"]
    food = {
        u"\U0001F34A": Event("Food", "Orange", None, 20, 20, 20),
        u"\U0001F34B": Event("Food", "Lemon", None, 20, 20, 20),
        u"\U0001F34C": Event("Food", "Banana", None, 20, 20, 20),
        u"\U0001F34D": Event("Food", "Pineapple", None, 20, 20, 20),
        u"\U0001F34E": Event("Food", "Apple", None, 20, 20, 20),
        u"\U0001F351": Event("Food", "Peach", None, 20, 20, 20),
        u"\U0001F352": Event("Food", "Cherry", None, 20, 20, 20),
        u"\U0001F353": Event("Food", "Strawberry", None, 20, 20, 20),
        u"\U0001F354": Event("Food", "Hamburger", None, 20, 20, 20),
        u"\U0001F355": Event("Food", "Pizza", None, 20, 20, 20),
        u"\U0001F36A": Event("Food", "Cookies", None, 20, 20, 20),
        u"\U0001F966": Event("Food", "Broccoli", None, 20, 20, 20),
    }

#
    activities = {
        u"⚽": Event("Play", "Football", None, 20, -20, -20),
        u"🏈": Event("Play", "Rugby", None, 20, -20, -20),
        u"⚾": Event("Play", "Baseball", None, 20, -20, -20),
        u"🎾": Event("Play", "Tennis", None, 20, -20, -20),
        u"🏐": Event("Play", "Volleyball", None, 20, -20, -20),
        u"🏓": Event("Play", "Ping-Pong", None, 20, -20, -20),
        u"🏒": Event("Play", "Hockey", None, 20, -20, -20),
        u"🏃": Event("Play", "Running", None, 20, -20, -20),
        u"\U0001F3AE": Event("Play", "Video-Games", None, 20, -20, -20),
    }