
# produkte = ["Apfel", "Banane", "Milch", "Brot", "Birne"]

preise = {
    "Apfel": 1.20,
    "Banane": 0.90,
    "Milch": 1.50,
    "Brot": 2.50
}


for produkte, preis in preise.items():
    print(f": {produkte} Preis: {preis} €")




# ich werf mal meine 5 cent dazwischen:
produkte = ["Apfel", "Banane", "Milch", "Brot", "Birne"]
preise = {
    "Apfel": 1.20,
    "Banane": 0.90,
    "Milch": 1.50,
    "Brot": 2.50
}

for item in produkte:
    price = preise.get(item, "not in store")
    if price != "not in store":
        price = f"{price :.2f} €"
    print(f"{item}: {price}")