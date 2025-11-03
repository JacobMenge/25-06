count = 0

while True:
    
    eingabe = input("gib eine zahl ein! (0 für ende)")
    
    if not eingabe.lstrip("-").isdigit():
        print("Bitte nur Zahlen!")
        continue

    zahl = int(eingabe)

    if zahl == 0:
        print("ende!")
        break
    
    count = count + 1
    
    if zahl > 0:
        print("positiv")
    else:
        print("negativ")

    if zahl % 2 == 0:
        print("gerade")
    else:
        print("ungerade")

print(f"du hast {count} Zahlen eingegeben")
