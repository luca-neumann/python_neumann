from elektroauto import ElektroAuto
from sportauto import Sportauto
from auto import Auto

if __name__ == "__main__":
    # normales Auto
    auto = Auto("Volkswagen", "Golf", 2022, 25000)
    print(auto.beschreibung())
    print(f"Gesamtpreis: {auto.preis_berechnen()} €\n")

    # Elektroauto
    elektroauto = ElektroAuto("Tesla", "Model 3", 2023, 40000, 75)
    print(elektroauto.beschreibung())
    print(f"Gesamtpreis: {elektroauto.preis_berechnen()} €\n")

    # Sportauto
    sportauto = Sportauto("Porsche", "911", 2023, 100000, 450)
    print(sportauto.beschreibung())
    print(f"Gesamtpreis: {sportauto.preis_berechnen()} €")
