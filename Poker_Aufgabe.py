from collections import Counter #zählt die Anzahl von Elementen in einer Liste
from random import random
import random

#Die Wahrscheinlichkeiten der Hände:
#paar 42,26%
#zwei paar 4,75%
#drillings 2,11%
#straße 0,392%
#flush 0,197%
#full house 0,144%
#straight flush 0,00139%
#royal flush 0,000154%

karten = 52
spiele_anzahl = 10000

#Liste von 0-51, für jede Karte
zahlen = [i for i in range(0, karten)]
#da werden die gz. Karten gespeichert
gezogene_zahlen = []

#Wörterbuch
#Schlüssel: Pokerkombination, Wert: 0
#zählt wie oft was kam
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

def ziehe_fuenf_karten():
    gezogene_zahlen = []
    for i in range(5):
        #wählt eine Karte aus dem Deck aus
        #-i damit nicht nochmal die gleiche Karte gezogen wird
        random_index = random.randint(0, len(zahlen) - 1 - i)
        #Modulo 13 um nur den Wert der Karte zu bekommen
        #13 weil es 13 verschiedene Werte gibt
        #0 für Ass, 10 für Bube, 11 für Dame, 12 für König
        gezogene_zahl = zahlen[random_index] % 13
        #kommt in die Liste
        gezogene_zahlen.append(gezogene_zahl)
        #tauscht die gz. Karte mit der letzten Karte aus und verkleinert
        #somit gibt es keine Karten doppelt
        zahlen[random_index], zahlen[len(zahlen) - 1 - i] = zahlen[len(zahlen) - 1 - i], zahlen[random_index]

    return gezogene_zahlen

def erkenne_kombinationen(hand):
    #überprüft die Hand die wir übergeben haben was drinnen ist
    werte_counter = Counter(hand)

    #überprüfen die Werte der Hand ob es:
    paar = list(werte_counter.values()).count(2) == 1
    zwei_paar = list(werte_counter.values()).count(2) == 2
    drilling = list(werte_counter.values()).count(3) == 1

    werte_sortiert = sorted(set(hand))
    #überprüft ob es eine Straße ist
    strasse = len(werte_sortiert) == 5 and (werte_sortiert[-1] - werte_sortiert[0] == 4)

    #überprüft ob es:
    flush = False
    straight_flush = strasse and flush
    royal_flush = strasse and min(werte_sortiert) == 8
    full_house = drilling and paar

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

#für des halt so oft aus wie oben angegeben
def spiele_poker_simulation(spiele_anzahl):
    for _ in range(spiele_anzahl):
        hand = ziehe_fuenf_karten()
        kombination = erkenne_kombinationen(hand)
        if kombination is not None:
            wahrscheinlichkeiten_statistik[kombination] += 1


spiele_poker_simulation(spiele_anzahl)

print(f"Ergebnisse nach {spiele_anzahl} Spielen:")
#diese for geht durch jedes Element in dem Wörterbuch
for kombination, anzahl in wahrscheinlichkeiten_statistik.items():
    prozent = (anzahl / spiele_anzahl) * 100
    print(f"{kombination}: {anzahl} Mal ({prozent:.4f}%)") #.4f weil 4 Nachkommastellen, f für Float
