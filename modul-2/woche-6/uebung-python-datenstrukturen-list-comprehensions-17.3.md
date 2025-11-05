# Iteration über Datenstrukturen und List Comprehensions

## Übersicht

In dieser Übung lernst du:
- **Iteration** - Wie man über Listen, Tuples, Sets und Dictionaries iteriert
- **enumerate()** - Nummerierung beim Iterieren
- **List Comprehensions** - Kompakte Schreibweise für Listen
- **Filter** - Elemente nach Bedingungen filtern

---

## Teil 1: Iteration Grundlagen

### Was ist Iteration?

Iteration bedeutet, dass du über die Elemente einer Datenstruktur "gehst" und mit jedem Element etwas machst. In Python nutzt du dafür hauptsächlich `for`-Schleifen.

**Grundprinzip:**
```python
for element in datenstruktur:
    # Mache etwas mit element
    print(element)
```

### Iteration über verschiedene Datenstrukturen

**Listen:**
```python
staedte = ["Berlin", "Hamburg", "München"]
for stadt in staedte:
    print(stadt)
```

**Tuples:**
```python
koordinaten = (10, 20, 30)
for zahl in koordinaten:
    print(zahl)
```

**Sets:**
```python
farben = {"rot", "grün", "blau"}
for farbe in sorted(farben):  # sorted() für Reihenfolge
    print(farbe)
```

**Dictionaries - drei Möglichkeiten:**
```python
person = {"name": "Anna", "alter": 25, "stadt": "Berlin"}

# 1. Über Schlüssel
for key in person:
    print(key)

# 2. Über Werte
for value in person.values():
    print(value)

# 3. Über Schlüssel-Wert-Paare (am häufigsten!)
for key, value in person.items():
    print(f"{key}: {value}")
```

### enumerate() für Nummerierung

Wenn du beim Iterieren auch die Position (Index) brauchst:

```python
fruechte = ["Apfel", "Banane", "Orange"]

for index, frucht in enumerate(fruechte):
    print(f"{index + 1}. {frucht}")

# Ausgabe:
# 1. Apfel
# 2. Banane
# 3. Orange
```

---

## Benötigte Methoden und Werkzeuge

Bevor wir mit den Übungen starten, schauen wir uns die wichtigsten Methoden und Funktionen an, die du benötigen wirst:

### assert - Bedingungen prüfen

`assert` überprüft eine Bedingung und stoppt das Programm mit einer Fehlermeldung, wenn die Bedingung nicht erfüllt ist.

**Syntax:**
```python
assert bedingung, "Fehlermeldung"
```

**Beispiel:**
```python
temperaturen = [18, 22, 19]
wochentage = ["Mo", "Di", "Mi"]

assert len(temperaturen) == len(wochentage), "Listen haben unterschiedliche Längen!"
# Kein Fehler, weil beide Listen 3 Elemente haben

assert len(temperaturen) == 7, "Temperaturen für ganze Woche fehlen!"
# AssertionError: Temperaturen für ganze Woche fehlen!
```

**Wann verwenden?** Bei Voraussetzungen, die erfüllt sein müssen (z.B. gleiche Listenlängen bei `zip()`).

### zip() - Listen parallel verarbeiten

`zip()` kombiniert mehrere Listen zu Paaren (oder Tripeln, etc.).

**Beispiel:**
```python
namen = ["Anna", "Ben", "Clara"]
alter = [25, 30, 28]

for name, jahre in zip(namen, alter):
    print(f"{name} ist {jahre} Jahre alt")

# Ausgabe:
# Anna ist 25 Jahre alt
# Ben ist 30 Jahre alt
# Clara ist 28 Jahre alt
```

**Wichtig:** `zip()` stoppt bei der kürzesten Liste!
```python
zip([1, 2, 3], ["A", "B"])  # Gibt nur 2 Paare: (1,"A"), (2,"B")
```

### sum() - Summe berechnen

`sum()` addiert alle Zahlen in einer Liste (oder anderem iterierbaren Objekt).

**Beispiel:**
```python
zahlen = [10, 20, 30, 40]
summe = sum(zahlen)  # 100

# Mit Startwert
summe = sum(zahlen, 5)  # 105 (5 + 10 + 20 + 30 + 40)
```

### len() - Anzahl Elemente

`len()` gibt die Anzahl der Elemente zurück.

**Beispiel:**
```python
liste = [1, 2, 3, 4, 5]
anzahl = len(liste)  # 5

text = "Hallo"
zeichen = len(text)  # 5

dictionary = {"a": 1, "b": 2}
eintraege = len(dictionary)  # 2
```

### max() und min() - Größtes/Kleinstes Element

Findet das größte bzw. kleinste Element.

**Beispiel:**
```python
zahlen = [15, 8, 23, 4, 16]
groesste = max(zahlen)  # 23
kleinste = min(zahlen)  # 4

# Bei Strings: Alphabetisch
woerter = ["Zebra", "Apfel", "Banane"]
erstes = min(woerter)  # "Apfel"
letztes = max(woerter)  # "Zebra"
```

**Mit key-Parameter:**
```python
# Längste Wort finden
woerter = ["Hi", "Hallo", "Hey"]
laengstes = max(woerter, key=len)  # "Hallo"

# Bei zip(): Nach zweitem Element sortieren
paare = [("Anna", 25), ("Ben", 30), ("Clara", 28)]
aelteste = max(paare, key=lambda x: x[1])  # ("Ben", 30)
```

### .index() - Position finden

Gibt die Position (Index) des ersten Vorkommens eines Elements zurück.

**Beispiel:**
```python
liste = ["Apfel", "Banane", "Orange", "Banane"]
position = liste.index("Banane")  # 1 (erste Position)

# Fehler bei nicht vorhandenem Element
position = liste.index("Kiwi")  # ValueError: 'Kiwi' is not in list
```

**Tipp:** Prüfe vorher mit `in`:
```python
if "Kiwi" in liste:
    position = liste.index("Kiwi")
else:
    print("Nicht gefunden")
```

### enumerate() - Index + Element

`enumerate()` gibt bei Iteration sowohl den Index als auch das Element zurück.

**Beispiel:**
```python
fruechte = ["Apfel", "Banane", "Orange"]

for index, frucht in enumerate(fruechte):
    print(f"Index {index}: {frucht}")

# Ausgabe:
# Index 0: Apfel
# Index 1: Banane
# Index 2: Orange
```

**Mit start-Parameter:**
```python
for nummer, frucht in enumerate(fruechte, start=1):
    print(f"{nummer}. {frucht}")

# Ausgabe:
# 1. Apfel
# 2. Banane
# 3. Orange
```

### sorted() - Sortierte Kopie

`sorted()` gibt eine neue, sortierte Liste zurück (Original bleibt unverändert).

**Beispiel:**
```python
zahlen = [3, 1, 4, 1, 5]
sortiert = sorted(zahlen)  # [1, 1, 3, 4, 5]
print(zahlen)  # [3, 1, 4, 1, 5] - Original unverändert

# Rückwärts sortieren
sortiert_rueck = sorted(zahlen, reverse=True)  # [5, 4, 3, 1, 1]

# Bei Sets: Erzeugt sortierte Liste
menge = {3, 1, 2}
liste = sorted(menge)  # [1, 2, 3]
```

**Unterschied zu .sort():**
```python
# .sort() verändert die Original-Liste
zahlen.sort()  # zahlen ist jetzt [1, 1, 3, 4, 5]

# sorted() gibt neue Liste zurück
sortiert = sorted(zahlen)  # zahlen bleibt unverändert
```

---

## Übung 1: Wetterdaten analysieren

**Aufgabe:**

Du hast Temperaturdaten einer Woche als Liste. Erstelle ein Programm, das:

1. Alle Temperaturen einzeln ausgibt mit dem jeweiligen Tag
2. Die durchschnittliche Temperatur berechnet
3. Den wärmsten Tag findet
4. Zählt, wie viele Tage über 20°C waren

**Gegeben:**
```python
temperaturen = [18, 22, 19, 25, 23, 21, 20]
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
```

**Hinweise:**
- Nutze `zip()` um zwei Listen parallel zu durchlaufen: `for tag, temp in zip(wochentage, temperaturen):`
- Nutze `max()` um die höchste Temperatur zu finden
- Nutze eine Zählvariable für Tage über 20°C

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 1: Wetterdaten analysieren
Musterlösung mit Erklärungen
"""

print("=== Wetteranalyse der Woche ===\n")

# Daten
temperaturen = [18, 22, 19, 25, 23, 21, 20]
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# Sicherheitscheck: Listen müssen gleich lang sein
assert len(temperaturen) == len(wochentage), "Listen haben unterschiedliche Längen!"

# Schritt 1: Alle Temperaturen mit Tag ausgeben
print("Temperaturen der Woche:")
for tag, temp in zip(wochentage, temperaturen):
    print(f"{tag}: {temp}°C")

# Schritt 2: Durchschnittstemperatur berechnen
durchschnitt = sum(temperaturen) / len(temperaturen)
print(f"\nDurchschnittstemperatur: {durchschnitt:.1f}°C")

# Schritt 3: Wärmsten Tag finden
max_temp = max(temperaturen)
# Index der maximalen Temperatur finden
max_index = temperaturen.index(max_temp)
waermster_tag = wochentage[max_index]

# Alternative: Eleganter mit zip und max
# waermster_tag, max_temp = max(zip(wochentage, temperaturen), key=lambda x: x[1])

print(f"Wärmster Tag: {waermster_tag} mit {max_temp}°C")

# Schritt 4: Tage über 20°C zählen
tage_ueber_20 = 0
for temp in temperaturen:
    if temp > 20:
        tage_ueber_20 += 1

print(f"Tage über 20°C: {tage_ueber_20} von {len(temperaturen)}")

# Bonus: Welche Tage waren über 20°C?
print("\nTage über 20°C:")
for tag, temp in zip(wochentage, temperaturen):
    if temp > 20:
        print(f"  - {tag}: {temp}°C")

"""
Erklärungen:

1. assert prüft eine Bedingung und stoppt das Programm wenn sie falsch ist
   - Wichtig bei zip(), damit keine Daten "verloren" gehen

2. zip() kombiniert zwei Listen zu Paaren:
   zip(["A", "B"], [1, 2]) → [("A", 1), ("B", 2)]

3. sum() addiert alle Elemente einer Liste
   len() gibt die Anzahl der Elemente zurück

4. max() findet den größten Wert
   .index() findet die Position eines Elements
   Alternative: max(zip(...), key=lambda x: x[1]) findet direkt das Paar

5. Zählvariable wird bei jedem Fund erhöht
"""
```

</details>

---

## Benötigte Methoden für Übung 2: Set-Operationen

Bevor du mit Übung 2 startest, hier die wichtigsten Set-Operationen:

### Set-Operationen im Überblick

**Vereinigung (Union) - Alle Elemente aus beiden Sets:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Mit Operator |
vereinigung = set1 | set2  # {1, 2, 3, 4, 5}

# Mit Methode .union()
vereinigung = set1.union(set2)  # {1, 2, 3, 4, 5}
```

**Schnittmenge (Intersection) - Nur gemeinsame Elemente:**
```python
# Mit Operator &
schnittmenge = set1 & set2  # {3}

# Mit Methode .intersection()
schnittmenge = set1.intersection(set2)  # {3}
```

**Differenz - Elemente nur im ersten Set:**
```python
# Mit Operator -
differenz = set1 - set2  # {1, 2}

# Mit Methode .difference()
differenz = set1.difference(set2)  # {1, 2}
```

**Symmetrische Differenz - Elemente in genau einem Set:**
```python
# Mit Operator ^
sym_diff = set1 ^ set2  # {1, 2, 4, 5}

# Mit Methode .symmetric_difference()
sym_diff = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
```

**Praxisbeispiel:**
```python
kurs_a = {"Anna", "Ben", "Clara"}
kurs_b = {"Ben", "Clara", "David"}

beide_kurse = kurs_a & kurs_b      # {"Ben", "Clara"}
nur_a = kurs_a - kurs_b            # {"Anna"}
nur_b = kurs_b - kurs_a            # {"David"}
alle = kurs_a | kurs_b             # {"Anna", "Ben", "Clara", "David"}
nur_einer = kurs_a ^ kurs_b        # {"Anna", "David"}
```

---

## Übung 2: Studentengruppen verwalten

**Aufgabe:**

Du hast zwei Sets mit Studenten aus verschiedenen Kursen. Erstelle ein Programm, das:

1. Alle Studenten aus Kurs A sortiert ausgibt
2. Alle Studenten aus Kurs B sortiert ausgibt
3. Findet, welche Studenten in beiden Kursen sind (Schnittmenge)
4. Findet, welche Studenten nur in einem der Kurse sind
5. Erstellt ein Dictionary mit jedem Studenten und in welchen Kursen er/sie ist

**Gegeben:**
```python
kurs_a = {"Anna", "Ben", "Clara", "David", "Eva"}
kurs_b = {"Ben", "Clara", "Frank", "Gina", "Eva"}
```

**Hinweise:**
- Nutze `sorted()` für sortierte Ausgabe von Sets
- Set-Operationen: `&` für Schnittmenge, `-` für Differenz
- Iteriere über die Vereinigung aller Studenten

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 2: Studentengruppen verwalten
Musterlösung mit Erklärungen
"""

print("=== Studentengruppenverwaltung ===\n")

# Daten
kurs_a = {"Anna", "Ben", "Clara", "David", "Eva"}
kurs_b = {"Ben", "Clara", "Frank", "Gina", "Eva"}

# Schritt 1: Studenten aus Kurs A sortiert ausgeben
print("Studenten in Kurs A:")
for student in sorted(kurs_a):
    print(f"  - {student}")

# Schritt 2: Studenten aus Kurs B sortiert ausgeben
print("\nStudenten in Kurs B:")
for student in sorted(kurs_b):
    print(f"  - {student}")

# Schritt 3: Studenten in beiden Kursen (Schnittmenge)
beide_kurse = kurs_a & kurs_b
print(f"\nStudenten in beiden Kursen ({len(beide_kurse)}):")
for student in sorted(beide_kurse):
    print(f"  - {student}")

# Schritt 4: Studenten nur in einem Kurs
nur_a = kurs_a - kurs_b
nur_b = kurs_b - kurs_a

# Alternative: Symmetrische Differenz (eleganter)
# nur_in_einem = kurs_a ^ kurs_b  # Alle die in genau einem der beiden Sets sind

print(f"\nNur in Kurs A ({len(nur_a)}):")
for student in sorted(nur_a):
    print(f"  - {student}")

print(f"\nNur in Kurs B ({len(nur_b)}):")
for student in sorted(nur_b):
    print(f"  - {student}")

# Schritt 5: Dictionary mit Kurszugehörigkeit erstellen
print("\n--- Kurszugehörigkeit ---")

alle_studenten = kurs_a | kurs_b  # Vereinigung
kurs_zuordnung = {}

for student in sorted(alle_studenten):
    kurse = []
    if student in kurs_a:
        kurse.append("Kurs A")
    if student in kurs_b:
        kurse.append("Kurs B")
    
    kurs_zuordnung[student] = kurse

# Dictionary ausgeben
for student, kurse in kurs_zuordnung.items():
    kurse_str = " und ".join(kurse)
    print(f"{student}: {kurse_str}")

# Zusatz: Statistik
print("\n--- Statistik ---")
print(f"Gesamtanzahl Studenten: {len(alle_studenten)}")
print(f"Nur Kurs A: {len(nur_a)}")
print(f"Nur Kurs B: {len(nur_b)}")
print(f"Beide Kurse: {len(beide_kurse)}")

"""
Erklärungen:

1. sorted() sortiert ein Set alphabetisch und gibt eine Liste zurück

2. Set-Operationen:
   - & (Schnittmenge): Elemente in beiden Sets
   - | (Vereinigung): Alle Elemente aus beiden Sets
   - - (Differenz): Elemente nur im ersten Set
   - ^ (Symmetrische Differenz): Elemente in genau einem der beiden Sets

3. 'in' Operator prüft Mitgliedschaft in Set (sehr schnell!)

4. Dictionary wird dynamisch aufgebaut während Iteration

5. .join() verbindet Liste zu String
"""
```

</details>

---

## Teil 2: List Comprehensions

### Was sind List Comprehensions?

List Comprehensions sind eine kompakte Art, neue Listen zu erstellen. Statt einer mehrzeiligen Schleife schreibst du alles in eine Zeile.

**Vergleich:**

```python
# Normal mit Schleife
zahlen = [1, 2, 3, 4, 5]
quadrate = []
for x in zahlen:
    quadrate.append(x * x)

# Mit List Comprehension
quadrate = [x * x for x in zahlen]
```

**Grundstruktur:**
```python
neue_liste = [ausdruck for element in alte_liste]
```

### List Comprehensions mit Filter

Du kannst auch Bedingungen einbauen:

```python
# Nur gerade Zahlen
zahlen = [1, 2, 3, 4, 5, 6]
gerade = [x for x in zahlen if x % 2 == 0]
# Ergebnis: [2, 4, 6]
```

**Struktur mit Filter:**
```python
neue_liste = [ausdruck for element in alte_liste if bedingung]
```

### Beispiele

```python
# Strings in Großbuchstaben umwandeln
woerter = ["hallo", "welt", "python"]
gross = [w.upper() for w in woerter]
# ['HALLO', 'WELT', 'PYTHON']

# Längen berechnen
laengen = [len(w) for w in woerter]
# [5, 4, 6]

# Nur lange Wörter
lange_woerter = [w for w in woerter if len(w) > 4]
# ['hallo', 'python']
```

### Wann List Comprehensions verwenden?

 **Gut geeignet:**
- Einfache Transformationen (quadrieren, umwandeln, etc.)
- Einfache Filter (gerade Zahlen, lange Strings, etc.)
- Wenn es in eine Zeile passt und lesbar bleibt

 **Nicht geeignet:**
- Komplexe Logik mit mehreren Bedingungen
- Mehrere verschachtelte Schleifen
- Wenn Lesbarkeit leidet

**Faustregel:** Lesbarkeit vor Kürze!

---

## Benötigte Methoden für Übung 3: String-Methoden

Wichtige String-Methoden für die Produktverwaltung:

### .upper() und .lower() - Groß-/Kleinschreibung

Wandelt alle Zeichen in Groß- bzw. Kleinbuchstaben um.

**Beispiel:**
```python
text = "Hallo Welt"

gross = text.upper()    # "HALLO WELT"
klein = text.lower()    # "hallo welt"

# Original bleibt unverändert
print(text)  # "Hallo Welt"
```

**Anwendung:**
```python
# Vergleich ohne Groß-/Kleinschreibung
eingabe = "APFEL"
if eingabe.lower() == "apfel":
    print("Gefunden!")
```

### .startswith() - Beginnt String mit...?

Prüft ob ein String mit bestimmten Zeichen beginnt.

**Beispiel:**
```python
wort = "Banane"

wort.startswith("B")     # True
wort.startswith("Ba")    # True
wort.startswith("A")     # False

# Groß-/Kleinschreibung beachten!
wort.startswith("b")     # False
```

**Mit List Comprehension:**
```python
woerter = ["Apfel", "Banane", "Ananas", "Birne"]
mit_a = [w for w in woerter if w.startswith("A")]
# ["Apfel", "Ananas"]
```

### .endswith() - Endet String mit...?

Analog zu `.startswith()`, prüft das Ende.

**Beispiel:**
```python
datei = "dokument.pdf"

datei.endswith(".pdf")   # True
datei.endswith(".txt")   # False
```

### len() für Strings

Anzahl der Zeichen in einem String.

**Beispiel:**
```python
text = "Python"
laenge = len(text)  # 6

# Leerzeichen zählen mit
text = "Hallo Welt"
laenge = len(text)  # 10 (Leerzeichen ist auch ein Zeichen)
```

### f-Strings zur Formatierung

Formatierte Strings mit Variablen und Ausdrücken.

**Beispiel:**
```python
name = "Anna"
alter = 25
print(f"{name} ist {alter} Jahre alt")
# "Anna ist 25 Jahre alt"

# Zahlen formatieren
preis = 3.5
print(f"Preis: {preis:.2f} €")  # "Preis: 3.50 €"

# Ausdrücke in f-Strings
zahl = 10
print(f"{zahl} × 2 = {zahl * 2}")  # "10 × 2 = 20"
```

**Formatierungsoptionen:**
```python
zahl = 3.14159

f"{zahl:.2f}"    # "3.14" (2 Dezimalstellen)
f"{zahl:.0f}"    # "3" (keine Dezimalstellen)
f"{zahl:8.2f}"   # "    3.14" (8 Zeichen breit, rechtsbündig)
```

---

## Übung 3: Produktverwaltung mit List Comprehensions

**Aufgabe:**

Du hast eine Liste mit Produktnamen und ein Dictionary mit Preisen. Nutze List Comprehensions für:

1. Erstelle eine Liste mit allen Produktnamen in Großbuchstaben
2. Erstelle eine Liste mit der Länge jedes Produktnamens
3. Erstelle eine Liste mit nur den Produkten, die mehr als 3 Euro kosten
4. Erstelle eine Liste mit Strings im Format "Name: Preis €" für alle Produkte
5. Erstelle eine Liste mit Produktnamen, die mit "M" beginnen
6. Erstelle eine Liste mit allen Preisen, die unter 5 Euro liegen

**Gegeben:**
```python
produkte = ["Apfel", "Milch", "Brot", "Käse", "Marmelade", "Müsli"]
preise = {
    "Apfel": 1.20,
    "Milch": 0.90,
    "Brot": 2.50,
    "Käse": 4.80,
    "Marmelade": 3.50,
    "Müsli": 3.80
}
```

**Hinweise:**
- Nutze `.upper()` für Großbuchstaben
- Nutze `len()` für Länge
- Nutze `if` in der List Comprehension für Filter
- Nutze f-Strings für formatierte Ausgabe
- Nutze `.startswith()` für Anfangsbuchstaben

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 3: Produktverwaltung mit List Comprehensions
Musterlösung mit Erklärungen
"""

print("=== Produktverwaltung ===\n")

# Daten
produkte = ["Apfel", "Milch", "Brot", "Käse", "Marmelade", "Müsli"]
preise = {
    "Apfel": 1.20,
    "Milch": 0.90,
    "Brot": 2.50,
    "Käse": 4.80,
    "Marmelade": 3.50,
    "Müsli": 3.80
}

# Schritt 1: Produktnamen in Großbuchstaben
grossbuchstaben = [p.upper() for p in produkte]
print("Produkte in Großbuchstaben:")
print(grossbuchstaben)

# Schritt 2: Länge der Produktnamen
laengen = [len(p) for p in produkte]
print(f"\nLängen der Produktnamen: {laengen}")

# Schritt 3: Nur Produkte über 3 Euro
teure_produkte = [p for p in produkte if preise[p] > 3.0]
print(f"\nProdukte über 3,00 €:")
for produkt in teure_produkte:
    print(f"  - {produkt}: {preise[produkt]:.2f} €")

# Schritt 4: Formatierte Strings "Name: Preis €"
formatiert = [f"{p}: {preise[p]:.2f} €" for p in produkte]
print("\nAlle Produkte formatiert:")
for zeile in formatiert:
    print(f"  {zeile}")

# Schritt 5: Produkte die mit "M" beginnen
mit_m = [p for p in produkte if p.startswith("M")]
print(f"\nProdukte die mit 'M' beginnen: {mit_m}")

# Schritt 6: Preise unter 5 Euro
guenstige_preise = [preise[p] for p in produkte if preise[p] < 5.0]
print(f"\nPreise unter 5,00 €: {guenstige_preise}")

# Bonus: Durchschnittspreis berechnen
durchschnitt = sum(preise.values()) / len(preise)
print(f"\nDurchschnittspreis: {durchschnitt:.2f} €")

# Bonus: Günstigste und teuerste Produkte
guenstigstes = min(produkte, key=lambda p: preise[p])
teuerstes = max(produkte, key=lambda p: preise[p])
print(f"Günstigstes Produkt: {guenstigstes} ({preise[guenstigstes]:.2f} €)")
print(f"Teuerstes Produkt: {teuerstes} ({preise[teuerstes]:.2f} €)")

"""
Erklärungen:

1. List Comprehension Grundform:
   [ausdruck for element in liste]

2. List Comprehension mit Filter:
   [ausdruck for element in liste if bedingung]

3. Bei Dictionary-Zugriff in LC:
   [preise[p] for p in produkte if preise[p] > 3]
   - Erst wird über produkte iteriert
   - Dann über p auf preise zugegriffen

4. .startswith() prüft Anfang eines Strings

5. f-String Formatierung:
   f"{variable:.2f}" → 2 Dezimalstellen

6. min() und max() mit key-Parameter finden
   das Element mit kleinstem/größtem Wert nach
   einer Funktion (hier: Preis)
"""
```

</details>

---

## Benötigte Methoden für Übung 4: Dictionary-Methoden

Wichtige Dictionary-Operationen für die Notenverwaltung:

### .get() - Sicherer Zugriff

`.get()` holt einen Wert, gibt aber einen Standardwert zurück wenn der Schlüssel nicht existiert (statt Fehler).

**Beispiel:**
```python
person = {"name": "Anna", "alter": 25}

# Normal mit []
print(person["name"])      # "Anna"
print(person["groesse"])   # KeyError!

# Sicher mit .get()
print(person.get("name"))           # "Anna"
print(person.get("groesse"))        # None
print(person.get("groesse", 0))     # 0 (eigener Standardwert)
```

**Anwendung beim Zählen:**
```python
zaehler = {}
wort = "Apfel"

# Umständlich
if wort in zaehler:
    zaehler[wort] += 1
else:
    zaehler[wort] = 1

# Elegant mit .get()
zaehler[wort] = zaehler.get(wort, 0) + 1
```

### .items() - Schlüssel-Wert-Paare

Gibt alle Schlüssel-Wert-Paare als Tuples zurück. Perfekt für Iteration!

**Beispiel:**
```python
noten = {"Anna": 1.3, "Ben": 2.0, "Clara": 1.7}

for name, note in noten.items():
    print(f"{name}: {note}")

# Ausgabe:
# Anna: 1.3
# Ben: 2.0
# Clara: 1.7
```

### .keys() - Nur Schlüssel

Gibt alle Schlüssel zurück.

**Beispiel:**
```python
noten = {"Anna": 1.3, "Ben": 2.0, "Clara": 1.7}

namen = noten.keys()
# dict_keys(['Anna', 'Ben', 'Clara'])

# Zu Liste konvertieren
namen_liste = list(noten.keys())
# ['Anna', 'Ben', 'Clara']

# Direkt iterieren
for name in noten.keys():
    print(name)
```

**Hinweis:** `for key in dict:` ist dasselbe wie `for key in dict.keys():`

### .values() - Nur Werte

Gibt alle Werte zurück.

**Beispiel:**
```python
noten = {"Anna": 1.3, "Ben": 2.0, "Clara": 1.7}

alle_noten = noten.values()
# dict_values([1.3, 2.0, 1.7])

# Statistiken berechnen
durchschnitt = sum(noten.values()) / len(noten.values())
beste_note = min(noten.values())
```

### Dictionary Comprehension (Fortgeschritten)

Analog zu List Comprehensions - erstellt Dictionaries kompakt.

**Syntax:**
```python
{key: value for item in sequenz}
```

**Beispiel:**
```python
# Quadratzahlen
zahlen = [1, 2, 3, 4, 5]
quadrate = {x: x**2 for x in zahlen}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Aus bestehendem Dictionary
noten = {"Anna": 1.3, "Ben": 2.0, "Clara": 1.7}
verdoppelt = {name: note * 2 for name, note in noten.items()}
# {"Anna": 2.6, "Ben": 4.0, "Clara": 3.4}

# Mit Filter
gute_noten = {name: note for name, note in noten.items() if note < 2.0}
# {"Anna": 1.3, "Clara": 1.7}
```

### Verschachtelte List Comprehension

Für Listen in Dictionaries - alle Elemente extrahieren.

**Beispiel:**
```python
noten = {
    "Anna": [1.3, 1.7, 2.0],
    "Ben": [2.3, 2.0, 2.7]
}

# Alle Noten in eine flache Liste
alle_noten = [note for noten_liste in noten.values() for note in noten_liste]
# [1.3, 1.7, 2.0, 2.3, 2.0, 2.7]

# Schritt für Schritt erklärt:
# 1. for noten_liste in noten.values() → [[1.3, 1.7, 2.0], [2.3, 2.0, 2.7]]
# 2. for note in noten_liste → einzelne Noten aus jeder Liste
```

**Mit Filter:**
```python
# Nur Noten besser als 2.0
gute = [note for noten_liste in noten.values() for note in noten_liste if note < 2.0]
# [1.3, 1.7]
```

---

## Übung 4: Notenverwaltung mit komplexer Iteration (Bonus - Optional)

**Hinweis:** Diese Übung ist anspruchsvoller und kombiniert mehrere Konzepte. Perfekt wenn du schon sicherer bist oder eine Herausforderung suchst!

**Aufgabe:**

Du hast ein Dictionary mit Studenten und deren Noten. Verwende Iteration und List Comprehensions für:

1. Gib alle Studenten mit ihren Noten aus
2. Berechne für jeden Studenten die Durchschnittsnote
3. Erstelle mit List Comprehension eine Liste aller Einzelnoten
4. Finde mit List Comprehension alle Noten besser als 2.0
5. Erstelle ein neues Dictionary mit Studenten und Durchschnittsnoten
6. Finde die Studenten mit der besten Durchschnittsnote

**Gegeben:**
```python
noten = {
    "Anna": [1.3, 1.7, 2.0, 1.0],
    "Ben": [2.3, 2.0, 2.7, 3.0],
    "Clara": [1.0, 1.3, 1.7, 1.3],
    "David": [2.7, 3.0, 2.3, 2.7]
}
```

**Hinweise:**
- Nutze `.items()` für Iteration über Dictionary
- Nutze `sum()` und `len()` für Durchschnitt
- Verschachtelte List Comprehension für alle Noten: `[note for noten_liste in ... for note in noten_liste]`
- Nutze `min()` mit `key` Parameter

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 4: Notenverwaltung mit komplexer Iteration
Musterlösung mit Erklärungen
"""

print("=== Notenverwaltungssystem ===\n")

# Daten
noten = {
    "Anna": [1.3, 1.7, 2.0, 1.0],
    "Ben": [2.3, 2.0, 2.7, 3.0],
    "Clara": [1.0, 1.3, 1.7, 1.3],
    "David": [2.7, 3.0, 2.3, 2.7]
}

# Schritt 1: Alle Studenten mit Noten ausgeben
print("Alle Studenten und ihre Noten:")
for student, noten_liste in noten.items():
    print(f"{student}: {noten_liste}")

# Schritt 2: Durchschnittsnote für jeden Studenten
print("\nDurchschnittsnoten:")
for student, noten_liste in noten.items():
    durchschnitt = sum(noten_liste) / len(noten_liste)
    print(f"{student}: {durchschnitt:.2f}")

# Schritt 3: Liste aller Einzelnoten (verschachtelte List Comprehension)
alle_noten = [note for noten_liste in noten.values() for note in noten_liste]
print(f"\nAlle Einzelnoten: {alle_noten}")
print(f"Gesamtanzahl Noten: {len(alle_noten)}")

# Schritt 4: Alle Noten besser als 2.0
gute_noten = [note for noten_liste in noten.values() for note in noten_liste if note < 2.0]
print(f"\nNoten besser als 2.0: {gute_noten}")
print(f"Anzahl: {len(gute_noten)} von {len(alle_noten)}")

# Schritt 5: Dictionary mit Durchschnittsnoten erstellen
# Variante 1: Mit normaler Schleife
durchschnitte = {}
for student, noten_liste in noten.items():
    durchschnitte[student] = sum(noten_liste) / len(noten_liste)

# Variante 2: Mit Dictionary Comprehension (fortgeschritten)
durchschnitte_lc = {
    student: sum(noten_liste) / len(noten_liste) 
    for student, noten_liste in noten.items()
}

print("\nDurchschnittsnoten-Dictionary:")
for student, durchschnitt in durchschnitte.items():
    print(f"{student}: {durchschnitt:.2f}")

# Schritt 6: Student(en) mit bester Durchschnittsnote
beste_note = min(durchschnitte.values())  # Kleinste Durchschnittsnote
beste_studenten = [
    student for student, durchschnitt in durchschnitte.items() 
    if durchschnitt == beste_note
]

print(f"\nBeste(r) Student(en):")
for student in beste_studenten:
    print(f"  {student}: {durchschnitte[student]:.2f}")

# Zusatz: Statistiken
print("\n--- Gesamtstatistik ---")
gesamt_durchschnitt = sum(alle_noten) / len(alle_noten)
beste_einzelnote = min(alle_noten)
schlechteste_einzelnote = max(alle_noten)

print(f"Gesamtdurchschnitt aller Noten: {gesamt_durchschnitt:.2f}")
print(f"Beste Einzelnote: {beste_einzelnote}")
print(f"Schlechteste Einzelnote: {schlechteste_einzelnote}")

# Zusatz: Notenverteilung
print("\n--- Notenverteilung ---")
sehr_gut = [note for note in alle_noten if note < 1.5]
gut = [note for note in alle_noten if 1.5 <= note < 2.5]
befriedigend = [note for note in alle_noten if 2.5 <= note < 3.5]

print(f"Sehr gut (< 1.5): {len(sehr_gut)} Noten")
print(f"Gut (1.5 - 2.5): {len(gut)} Noten")
print(f"Befriedigend (2.5 - 3.5): {len(befriedigend)} Noten")

"""
Erklärungen:

1. .items() gibt Schlüssel-Wert-Paare zurück:
   for key, value in dict.items()

2. Verschachtelte List Comprehension:
   [note for liste in dict.values() for note in liste]
   - Erst wird über alle Listen iteriert
   - Dann über jede Note in jeder Liste

3. Dictionary Comprehension (fortgeschritten):
   {key: wert for key, wert in ...}

4. min() mit .values() findet kleinsten Wert
   Dann Liste der Studenten mit diesem Wert finden

5. Mehrfache Bedingungen mit 'and':
   if 1.5 <= note < 2.5

6. List Comprehensions sind ideal für Filterung:
   - Schnell zu schreiben
   - Gut lesbar bei einfachen Bedingungen
"""
```

</details>

---

## Kombinierte Übung: Online-Shop Analyse (Bonus - Fortgeschritten)

**Hinweis:** Diese Übung ist deutlich umfangreicher und anspruchsvoller! Sie ist gedacht für alle, die sich bereits sicher fühlen und ein realistisches Projekt durcharbeiten möchten. Keine Sorge, wenn sie zu komplex ist - konzentriere dich auf die ersten 3 Übungen!

### Aufgabe

Erstelle ein Analyse-Tool für einen Online-Shop mit folgenden Funktionen:

**Gegeben sind drei Datenstrukturen:**

```python
# Liste aller Bestellungen (jede Bestellung ist ein Tuple: (Produkt, Menge, Preis_pro_Stück))
bestellungen = [
    ("Laptop", 1, 899.00),
    ("Maus", 2, 19.99),
    ("Tastatur", 1, 79.99),
    ("Monitor", 2, 299.00),
    ("Laptop", 1, 899.00),
    ("Maus", 3, 19.99),
    ("USB-Kabel", 5, 4.99),
    ("Tastatur", 1, 79.99),
    ("Monitor", 1, 299.00),
    ("Headset", 2, 49.99)
]

# Dictionary mit Kategorien
kategorien = {
    "Laptop": "Computer",
    "Monitor": "Computer",
    "Maus": "Zubehör",
    "Tastatur": "Zubehör",
    "USB-Kabel": "Zubehör",
    "Headset": "Audio"
}

# Set mit Produkten im Angebot
im_angebot = {"Maus", "USB-Kabel", "Headset"}
```

**Implementiere:**

1. **Gesamtumsatz berechnen**
   - Iteriere über alle Bestellungen
   - Berechne Gesamtwert jeder Bestellung (Menge × Preis)
   - Summiere alle Werte

2. **Produktstatistik mit List Comprehensions**
   - Liste aller verkauften Produktnamen (mit Duplikaten)
   - Liste aller einzigartigen Produkte (nutze Set)
   - Liste aller Bestellwerte (Menge × Preis pro Bestellung)

3. **Top-Produkte finden**
   - Dictionary: Produkt → Gesamte verkaufte Menge
   - Finde die 3 meistverkauften Produkte

4. **Kategorieanalyse**
   - Umsatz pro Kategorie berechnen
   - Anzahl Bestellungen pro Kategorie

5. **Angebots-Analyse**
   - Liste mit Bestellungen von Angebotsprodukten
   - Umsatz durch Angebotsprodukte

6. **Advanced: Empfehlungen**
   - Finde Produkte, die oft zusammen gekauft werden
   - (Vereinfacht: Produkte in aufeinanderfolgenden Bestellungen)

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Kombinierte Übung: Online-Shop Analyse
Umfassende Musterlösung
"""

print("=== Online-Shop Analyse ===\n")

# Daten
bestellungen = [
    ("Laptop", 1, 899.00),
    ("Maus", 2, 19.99),
    ("Tastatur", 1, 79.99),
    ("Monitor", 2, 299.00),
    ("Laptop", 1, 899.00),
    ("Maus", 3, 19.99),
    ("USB-Kabel", 5, 4.99),
    ("Tastatur", 1, 79.99),
    ("Monitor", 1, 299.00),
    ("Headset", 2, 49.99)
]

kategorien = {
    "Laptop": "Computer",
    "Monitor": "Computer",
    "Maus": "Zubehör",
    "Tastatur": "Zubehör",
    "USB-Kabel": "Zubehör",
    "Headset": "Audio"
}

im_angebot = {"Maus", "USB-Kabel", "Headset"}

# ========================================
# 1. Gesamtumsatz berechnen
# ========================================
print("--- Gesamtumsatz ---")

gesamtumsatz = 0
for produkt, menge, preis in bestellungen:
    bestellwert = menge * preis
    gesamtumsatz += bestellwert

print(f"Gesamtumsatz: {gesamtumsatz:.2f} €")
print(f"Anzahl Bestellungen: {len(bestellungen)}")
print(f"Durchschnittlicher Bestellwert: {gesamtumsatz / len(bestellungen):.2f} €")

# ========================================
# 2. Produktstatistik mit List Comprehensions
# ========================================
print("\n--- Produktstatistik ---")

# Alle Produktnamen (mit Duplikaten)
alle_produkte = [produkt for produkt, menge, preis in bestellungen]
print(f"Alle Bestellungen: {alle_produkte}")

# Einzigartige Produkte
einzigartige_produkte = list(set(alle_produkte))
print(f"\nAnzahl verschiedener Produkte: {len(einzigartige_produkte)}")
print(f"Produkte: {sorted(einzigartige_produkte)}")

# Alle Bestellwerte
bestellwerte = [menge * preis for produkt, menge, preis in bestellungen]
print(f"\nBestellwerte: {[f'{w:.2f} €' for w in bestellwerte]}")

# ========================================
# 3. Top-Produkte finden
# ========================================
print("\n--- Top-Produkte ---")

# Dictionary: Produkt → Verkaufte Menge
verkaufte_mengen = {}
for produkt, menge, preis in bestellungen:
    if produkt in verkaufte_mengen:
        verkaufte_mengen[produkt] += menge
    else:
        verkaufte_mengen[produkt] = menge

# Nach Menge sortieren (absteigend)
top_produkte = sorted(
    verkaufte_mengen.items(), 
    key=lambda item: item[1], 
    reverse=True
)

print("Meistverkaufte Produkte:")
for i, (produkt, menge) in enumerate(top_produkte[:3], 1):
    print(f"  {i}. {produkt}: {menge} Stück verkauft")

# ========================================
# 4. Kategorieanalyse
# ========================================
print("\n--- Kategorieanalyse ---")

# Umsatz pro Kategorie
kategorie_umsatz = {}
kategorie_anzahl = {}

for produkt, menge, preis in bestellungen:
    kategorie = kategorien.get(produkt, "Unbekannt")
    umsatz = menge * preis
    
    # Umsatz addieren
    if kategorie in kategorie_umsatz:
        kategorie_umsatz[kategorie] += umsatz
        kategorie_anzahl[kategorie] += 1
    else:
        kategorie_umsatz[kategorie] = umsatz
        kategorie_anzahl[kategorie] = 1

print("Umsatz nach Kategorie:")
for kategorie, umsatz in sorted(kategorie_umsatz.items(), key=lambda x: x[1], reverse=True):
    anzahl = kategorie_anzahl[kategorie]
    anteil = (umsatz / gesamtumsatz) * 100
    print(f"  {kategorie}:")
    print(f"    Umsatz: {umsatz:.2f} € ({anteil:.1f}%)")
    print(f"    Bestellungen: {anzahl}")

# ========================================
# 5. Angebots-Analyse
# ========================================
print("\n--- Angebots-Analyse ---")

# Bestellungen von Angebotsprodukten
angebots_bestellungen = [
    (produkt, menge, preis) 
    for produkt, menge, preis in bestellungen 
    if produkt in im_angebot
]

print(f"Bestellungen von Angebotsprodukten: {len(angebots_bestellungen)}")

# Umsatz durch Angebote
angebots_umsatz = sum([menge * preis for produkt, menge, preis in angebots_bestellungen])
angebots_anteil = (angebots_umsatz / gesamtumsatz) * 100

print(f"Umsatz durch Angebote: {angebots_umsatz:.2f} € ({angebots_anteil:.1f}%)")

print("\nDetails der Angebotsbestellungen:")
for produkt, menge, preis in angebots_bestellungen:
    print(f"  {produkt}: {menge} × {preis:.2f} € = {menge * preis:.2f} €")

# ========================================
# 6. Advanced: Oft zusammen gekaufte Produkte
# ========================================
print("\n--- Kaufverhalten ---")

# Vereinfachte Analyse: Aufeinanderfolgende Bestellungen
kombinationen = {}
for i in range(len(bestellungen) - 1):
    produkt1 = bestellungen[i][0]
    produkt2 = bestellungen[i + 1][0]
    
    if produkt1 != produkt2:  # Nicht das gleiche Produkt
        # Sortieren um Reihenfolge zu normalisieren
        kombi = tuple(sorted([produkt1, produkt2]))
        
        if kombi in kombinationen:
            kombinationen[kombi] += 1
        else:
            kombinationen[kombi] = 1

if kombinationen:
    print("Häufig aufeinanderfolgende Bestellungen:")
    top_kombinationen = sorted(kombinationen.items(), key=lambda x: x[1], reverse=True)[:3]
    for (prod1, prod2), anzahl in top_kombinationen:
        print(f"  {prod1} + {prod2}: {anzahl}x")

# ========================================
# Zusammenfassung
# ========================================
print("\n" + "="*50)
print("ZUSAMMENFASSUNG")
print("="*50)
print(f"Gesamtumsatz: {gesamtumsatz:.2f} €")
print(f"Bestellungen: {len(bestellungen)}")
print(f"Verschiedene Produkte: {len(einzigartige_produkte)}")
print(f"Kategorien: {len(kategorie_umsatz)}")
print(f"Top-Produkt: {top_produkte[0][0]} ({top_produkte[0][1]} verkauft)")
print(f"Angebots-Anteil: {angebots_anteil:.1f}%")

"""
Erklärungen und Best Practices:

1. TUPLE UNPACKING:
   for produkt, menge, preis in bestellungen:
   - Jede Bestellung ist ein Tuple mit 3 Werten
   - Diese werden direkt in Variablen entpackt

2. LIST COMPREHENSIONS:
   - Einfache Transformationen: [x*2 for x in liste]
   - Mit Filter: [x for x in liste if bedingung]
   - Gut für Datenextraktion aus komplexen Strukturen

3. DICTIONARY AUFBAUEN:
   if key in dict:
       dict[key] += wert
   else:
       dict[key] = wert
   
   Alternative mit .get():
   dict[key] = dict.get(key, 0) + wert

4. SORTIERUNG:
   sorted(dict.items(), key=lambda x: x[1], reverse=True)
   - .items() gibt (key, value) Paare
   - key= definiert Sortierkriterium
   - lambda x: x[1] sortiert nach Wert (nicht Schlüssel)
   - reverse=True für absteigende Reihenfolge

5. SET-OPERATIONEN:
   - 'in' Operator für schnelle Mitgliedschaftstests
   - set() entfernt Duplikate aus Listen

6. PROZENTRECHNUNG:
   anteil = (teilwert / gesamtwert) * 100

7. FORMATIERUNG:
   f"{wert:.2f}" → 2 Dezimalstellen
   f"{wert:.1f}" → 1 Dezimalstelle

WICHTIGE KONZEPTE IN DIESER ÜBUNG:
- Iteration über verschiedene Datenstrukturen
- Kombination von Listen, Tuples, Sets und Dicts
- List Comprehensions für Datenextraktion
- Dictionary zum Aggregieren von Daten
- Sortierung nach verschiedenen Kriterien
- Berechnung von Statistiken

Diese Übung zeigt typische Datenanalyse-Aufgaben
die in der Praxis häufig vorkommen!
"""
```

</details>

---

## Zusammenfassung

### Iteration - Die wichtigsten Patterns

```python
# Liste
for element in liste:
    print(element)

# Tuple (gleich wie Liste)
for element in tuple:
    print(element)

# Set (ungeordnet, nutze sorted() für Reihenfolge)
for element in sorted(mein_set):
    print(element)

# Dictionary - drei Varianten
for key in dict:                      # Nur Schlüssel
for value in dict.values():           # Nur Werte
for key, value in dict.items():       # Beides (häufigst!)

# Mit Index: enumerate()
for index, element in enumerate(liste):
    print(f"{index}: {element}")

# Zwei Listen parallel: zip()
for a, b in zip(liste1, liste2):
    print(f"{a} - {b}")
```

### List Comprehensions - Cheat Sheet

```python
# Grundform
[ausdruck for element in sequenz]

# Mit Filter
[ausdruck for element in sequenz if bedingung]

# Beispiele
[x*2 for x in zahlen]                    # Transformation
[x for x in zahlen if x > 5]             # Filter
[w.upper() for w in woerter]             # String-Methoden
[len(w) for w in woerter]                # Funktionen anwenden

# Verschachtelt (für alle Elemente aller Listen)
[element for liste in listen for element in liste]
```

### Wann was verwenden?

| Situation | Verwende |
|-----------|----------|
| Einfache Transformation | List Comprehension |
| Einfacher Filter | List Comprehension |
| Komplexe Logik | Normale Schleife |
| Mehrere Schritte | Normale Schleife |
| Aggregation (Summe, Count) | Normale Schleife + Variable |
| Dictionary aufbauen | Normale Schleife |

### Tipps und Tricks

1. **Lesbarkeit vor Kürze**
   - List Comprehensions sind toll, aber nicht um jeden Preis
   - Wenn es schwer zu lesen ist → normale Schleife

2. **enumerate() ist dein Freund**
   - Nutze es immer wenn du Index + Element brauchst
   - Besser als manuelles Zählen

3. **Dictionary.items() für Paare**
   - Fast immer die beste Wahl beim Iterieren über Dicts
   - Gibt beide Werte direkt

4. **Set für Eindeutigkeit**
   - `set(liste)` entfernt Duplikate sofort
   - Sehr schnell für Mitgliedschaftstests

5. **List Comprehensions kombinieren**
   - Aber nicht zu tief verschachteln
   - Maximum 2 Ebenen für Lesbarkeit
