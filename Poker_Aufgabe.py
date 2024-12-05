from collections import Counter
from random import randint

# Die Wahrscheinlichkeiten der Hände:
# Paar 42,26%
# Zwei Paar 4,75%
# Drilling 2,11%
# Straße 0,392%
# Flush 0,197%
# Full House 0,144%
# Straight Flush 0,00139%
# Royal Flush 0,000154%

# Funktion, um 5 Karten aus einem Deck zu ziehen
def ziehe_fuenf_karten(kartenanzahl):
    # Liste von 0 bis kartenanzahl - 1, repräsentiert das Deck
    deck = list(range(kartenanzahl))
    hand = []
    for i in range(5):
        # Wählt eine Karte zufällig aus
        random_index = randint(0, len(deck) - 1)
        # Modulo 13, um nur den Wert der Karte zu erhalten
        # 0 für Ass, 10 für Bube, 11 für Dame, 12 für König
        gezogene_karte = deck.pop(random_index) % 13
        # Fügt die gezogene Karte der Hand hinzu
        hand.append(gezogene_karte)
    return hand

# Funktion, um Kombinationen in einer Hand zu erkennen
def erkenne_kombinationen(hand):
    # Zählt die Anzahl jedes Wertes in der Hand
    werte_counter = Counter(hand)

    # Überprüft, ob die Hand ein Paar, zwei Paare oder einen Drilling enthält
    paar = list(werte_counter.values()).count(2) == 1
    zwei_paar = list(werte_counter.values()).count(2) == 2
    drilling = list(werte_counter.values()).count(3) == 1

    # Sortiert die Werte der Hand und überprüft, ob es eine Straße ist
    werte_sortiert = sorted(set(hand))
    strasse = len(werte_sortiert) == 5 and (werte_sortiert[-1] - werte_sortiert[0] == 4)

    # Überprüft die weiteren Kombinationen
    flush = False  # Kann erweitert werden, wenn Farben berücksichtigt werden
    straight_flush = strasse and flush
    royal_flush = strasse and min(werte_sortiert) == 8
    full_house = drilling and paar

    # Gibt die höchste Kombination zurück, die erkannt wurde
    if royal_flush:
        return "Royal Flush"
    elif straight_flush:
        return "Straight Flush"
    elif full_house:
        return "Full House"
    elif strasse:
        return "Straße"
    elif drilling:
        return "Drilling"
    elif zwei_paar:
        return "Zwei Paar"
    elif paar:
        return "Paar"
    else:
        return None

# Funktion, um eine bestimmte Anzahl von Poker-Spielen zu simulieren
def spiele_poker_simulation(spiele_anzahl, kartenanzahl):
    # Wörterbuch, um die Häufigkeit jeder Kombination zu speichern
    wahrscheinlichkeiten_statistik = {
        "Paar": 0,
        "Zwei Paar": 0,
        "Drilling": 0,
        "Straße": 0,
        "Flush": 0,
        "Full House": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }

    # Führt die Simulation der angegebenen Anzahl von Spielen durch
    for _ in range(spiele_anzahl):
        # Zieht 5 Karten und erkennt die Kombination
        hand = ziehe_fuenf_karten(kartenanzahl)
        kombination = erkenne_kombinationen(hand)
        # Erhöht den Zähler für die erkannte Kombination
        if kombination:
            wahrscheinlichkeiten_statistik[kombination] += 1

    # Gibt die Statistiken zurück
    return wahrscheinlichkeiten_statistik

# Hauptfunktion
def main():
    try:
        # Fragt die Anzahl der Spiele vom Benutzer ab
        spiele_anzahl = int(input("Geben Sie die Anzahl der Spiele ein: "))
        # Definiert die Anzahl der Karten im Deck (Standard: 52 Karten)
        kartenanzahl = 52

        # Führt die Simulation durch
        ergebnisse = spiele_poker_simulation(spiele_anzahl, kartenanzahl)

        # Gibt die Ergebnisse aus
        print(f"\nErgebnisse nach {spiele_anzahl} Spielen:")
        for kombination, anzahl in ergebnisse.items():
            prozent = (anzahl / spiele_anzahl) * 100
            # Formatiert die Ausgabe mit 2 Dezimalstellen
            print(f"{kombination}: {anzahl} Mal ({prozent:.2f}%)")
    except ValueError:
        # Gibt eine Fehlermeldung aus, wenn die Eingabe ungültig ist
        print("Bitte geben Sie eine gültige Ganzzahl ein.")

if __name__ == "__main__":
    main()
