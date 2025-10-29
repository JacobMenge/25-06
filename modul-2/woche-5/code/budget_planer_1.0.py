# Budget-Rechner - Einfache Musterlösung

# schritt 1: begrueßung und personalisierung
print("==== Budget-Rechner ====")
print()

name = input("Dein Name: ")
monat = input("Aktueller Monat: ")

print()
print(f"Hallo {name}! Lass uns dein Budget für {monat} berechnen.")
print()


#schritt 2: einnahmen erfassen
print("EINNAHMEN:")
gehalt = float(input("Monatliches Gehalt (€): ")) 
zusatz = float(input("Zusatzeinkommen (€): "))

gesamteinnahmen = gehalt + zusatz
print(f"Gesamteinnahmen: {gesamteinnahmen}€")
print()



# schritt 3: Ausgaben erfassen
print("AUSGABEN:")
miete = float(input("Miete (€): "))
lebensmittel = float(input("Lebensmittel (€): "))
transport = float(input("Transport (€): "))
freizeit = float(input("Freizeit (€): "))

gesamtausgaben = miete + lebensmittel + transport + freizeit
print(f"Gesamtausgaben: {gesamtausgaben}€")
print()



# schritt 4: Bilanz berechnen
bilanz = gesamteinnahmen - gesamtausgaben
sparquote = bilanz / gesamteinnahmen * 100


# schritt 5: Übersichtliche Zusammenfassung
print("ZUSAMMENFASSUNG:")
print()
print(f"Einnahmen: {gesamteinnahmen:.2f}€")
print(f"Ausgaben:  {gesamtausgaben:.2f}€")
print(f"Bilanz:    {bilanz:.2f}€")
print(f"Sparquote: {sparquote:.2f}%")
print()
print(f"Danke {name}!")