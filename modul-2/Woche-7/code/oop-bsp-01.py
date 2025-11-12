class Zaehler:
    def __init__(self, start=0):
        self.zaehlerstand = start

    def erhoehen(self, schritt=1):
        self.zaehlerstand += schritt

    def reset(self):
        self.zaehlerstand = 0

# Nutzung
z1 = Zaehler()
z2 = Zaehler(2)
z3 = Zaehler(10)
print(z1.zaehlerstand)
z1.erhoehen(20)

print(z1.zaehlerstand)
print(z2.zaehlerstand)
z2.reset()
print(f"der Zählerstand von z2 ist: {z2.zaehlerstand}")