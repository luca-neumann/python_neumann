from auto import Auto

class Sportauto(Auto):
    def __init__(self, marke, modell, baujahr, grundpreis, ps):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.ps = ps

    def beschreibung(self):
        return super().beschreibung() + f", PS: {self.ps}"

    def preis_berechnen(self):
        return self.grundpreis + self.ps * 50  # 50 €/PS noch dazu