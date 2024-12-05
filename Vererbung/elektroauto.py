from auto import Auto

class ElektroAuto(Auto):
    def __init__(self, marke, modell, baujahr, grundpreis, batterie_kapazitaet):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.batterie_kapazitaet = batterie_kapazitaet

    def beschreibung(self):
        return super().beschreibung() + f", Batterie: {self.batterie_kapazitaet} kWh"

    def preis_berechnen(self):
        return self.grundpreis + self.batterie_kapazitaet * 100  # 100 €/kWh dazu