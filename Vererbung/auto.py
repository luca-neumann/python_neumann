class Auto:
    def __init__(self, marke, modell, baujahr, grundpreis):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.grundpreis = grundpreis

    def beschreibung(self):
        return f"{self.marke} {self.modell} ({self.baujahr}), Preis: {self.grundpreis} €"

    def preis_berechnen(self):
        return self.grundpreis