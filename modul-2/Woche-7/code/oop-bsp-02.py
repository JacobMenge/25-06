class Fahrzeug:
    anzahl = 0

    def __init__(self, art, farbe, marke):
        self.art = art
        self.farbe = farbe
        self.marke = marke
        self.km = 0
        self.tank = 0
        Fahrzeug.anzahl += 1
        print(f"[Fahrzeug wird Nr.[{Fahrzeug.anzahl}] gebaut..] {self.art}, {self.farbe}, {self.marke}")

    def __str__(self):
        return f" Art: {self.art}, Farbe: {self.farbe}, Marke: {self.marke}, KM: {self.km}, Tank: {self.tank}"

    def tanken(self, liter):
        self.tank += liter
        print(f"[Es wird getankt.. {self.art}, {self.farbe}, {self.marke}] Es werden {liter}L getankt --> Tank:{self.tank} ")

    def fahren(self, strecke):
        self.km += strecke
        self.tank -= strecke * 0.1
        print(f"[Fahrzeug fährt.. {self.art}, {self.farbe}, {self.marke}] Es werden {strecke}Km gefahren, Stand: {self.km} --> Tank:{self.tank} ")

    def hupen(self):
        print(f"[Huup Huup.. {self.art}, {self.farbe}, {self.marke}]")


if __name__ == "__main__":
    auto1 = Fahrzeug("auto", "grün", "bmw")
    panzer1 = Fahrzeug("panzer", "pink", "leopard mk2")

    auto1.tanken(50)
    panzer1.tanken(200)

    auto1.fahren(20)
    panzer1.fahren(20)

    panzer1.hupen()