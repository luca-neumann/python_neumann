import random

colors = ["Karo", "Herz", "Pik", "Kreuz"]
symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]


def erstellt_karte():
    deck = [(symbol, farbe) for symbol in symbols for farbe in colors]
    return deck


def macht_hand(deck):
    return random.sample(deck, 5)


def hat_gleiche_werte(hand, count=2):
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == count:
            return True
    return False
