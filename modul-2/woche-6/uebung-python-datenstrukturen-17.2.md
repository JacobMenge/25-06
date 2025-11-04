# Datenstrukturen in Python: Listen, Tuples, Sets und Dictionaries

## Übersicht

In dieser Übung lernst du die vier wichtigsten Datenstrukturen in Python kennen:
- **Listen** - Veränderbare, geordnete Sammlungen
- **Tuples** - Unveränderbare, geordnete Sammlungen
- **Sets** - Ungeordnete Sammlungen ohne Duplikate
- **Dictionaries** - Schlüssel-Wert-Paare

---

## Teil 1: Listen

### Was sind Listen?

Listen sind veränderbare (mutable), geordnete Sammlungen von Elementen. Sie gehören zu den am häufigsten verwendeten Datenstrukturen in Python.

**Eigenschaften:**
- Veränderbar: Elemente können hinzugefügt, entfernt oder geändert werden
- Geordnet: Die Reihenfolge bleibt erhalten
- Erlaubt Duplikate
- Zugriff über Index (beginnt bei 0)

**Syntax:**
```python
# Leere Liste
meine_liste = []

# Liste mit Elementen
zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Ben", "Clara"]
gemischt = [1, "Text", 3.14, True]
```

**Wichtige Operationen:**
```python
liste = [1, 2, 3]

# Element hinzufügen
liste.append(4)              # [1, 2, 3, 4]

# Element an bestimmter Position einfügen
liste.insert(0, 0)           # [0, 1, 2, 3, 4]

# Element entfernen
liste.remove(2)              # [0, 1, 3, 4]

# Element per Index entfernen
del liste[0]                 # [1, 3, 4]

# Letztes Element entfernen und zurückgeben
letztes = liste.pop()        # letztes = 4, liste = [1, 3]

# Länge der Liste
laenge = len(liste)          # 2

# Element suchen (Index)
index = liste.index(3)       # 1

# Sortieren
liste.sort()                 # sortiert die Liste

# Liste umkehren
liste.reverse()              # kehrt Reihenfolge um
```

**Hinweis:** Die obigen Zeilen sind einzelne Beispiele. Führt sie am besten einzeln aus, um die jeweilige Wirkung zu sehen.

### Übung 1: Einkaufsliste verwalten

**Aufgabe:**

Erstelle ein Programm zur Verwaltung einer Einkaufsliste mit folgenden Funktionen:

1. Erstelle eine leere Einkaufsliste
2. Füge 5 Artikel zur Liste hinzu (z.B. "Milch", "Brot", "Eier", "Käse", "Butter")
3. Gib die gesamte Liste aus mit Nummerierung
4. Entferne ein Element aus der Mitte der Liste
5. Füge ein neues Element an den Anfang der Liste ein
6. Gib die aktualisierte Liste aus
7. Sortiere die Liste alphabetisch und gib sie aus
8. Zeige an, wie viele Artikel auf der Liste stehen

**Hinweise:**
- Nutze `append()` zum Hinzufügen
- Nutze `insert(0, element)` zum Einfügen am Anfang
- Nutze `remove()` oder `pop(index)` zum Entfernen
- Nutze `sort()` zum Sortieren
- Nutze `enumerate()` für die Nummerierung

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 1: Einkaufsliste verwalten
Musterlösung mit Erklärungen
"""

print("=== Einkaufslisten-Manager ===\n")

# Schritt 1: Leere Liste erstellen
einkaufsliste = []

# Schritt 2: Artikel hinzufügen
# append() fügt Elemente am Ende der Liste hinzu
einkaufsliste.append("Milch")
einkaufsliste.append("Brot")
einkaufsliste.append("Eier")
einkaufsliste.append("Käse")
einkaufsliste.append("Butter")

# Schritt 3: Liste mit Nummerierung ausgeben
print("Ursprüngliche Einkaufsliste:")
for index, artikel in enumerate(einkaufsliste, start=1):
    print(f"{index}. {artikel}")

# Schritt 4: Element aus der Mitte entfernen
# remove() entfernt das erste Vorkommen des Elements
einkaufsliste.remove("Eier")
print(f"\n'Eier' wurde entfernt")

# Schritt 5: Element am Anfang einfügen
# insert(0, element) fügt am Anfang ein
einkaufsliste.insert(0, "Äpfel")
print("'Äpfel' wurde am Anfang eingefügt")

# Schritt 6: Aktualisierte Liste ausgeben
print("\nAktualisierte Einkaufsliste:")
for index, artikel in enumerate(einkaufsliste, start=1):
    print(f"{index}. {artikel}")

# Schritt 7: Liste alphabetisch sortieren
# sort() sortiert die Liste direkt (in-place)
einkaufsliste.sort()
print("\nSortierte Einkaufsliste:")
for index, artikel in enumerate(einkaufsliste, start=1):
    print(f"{index}. {artikel}")

# Schritt 8: Anzahl der Artikel anzeigen
print(f"\nGesamtanzahl: {len(einkaufsliste)} Artikel")

"""
Erklärungen:

1. Listen sind ideal für Sammlungen, die sich ändern können
2. append() ist die häufigste Methode zum Hinzufügen
3. remove() entfernt nach Wert, pop() nach Index
4. sort() verändert die Original-Liste (in-place Operation)
5. enumerate() ist praktisch für nummerierte Ausgaben
6. len() gibt die Anzahl der Elemente zurück
"""
```

</details>

---

## Teil 2: Tuples

### Was sind Tuples?

Tuples sind unveränderbare (immutable), geordnete Sammlungen von Elementen. Einmal erstellt, können sie nicht mehr verändert werden.

**Eigenschaften:**
- Unveränderbar: Keine Elemente können hinzugefügt, entfernt oder geändert werden
- Geordnet: Die Reihenfolge bleibt erhalten
- Erlaubt Duplikate
- Zugriff über Index
- Schneller als Listen (weniger Speicher)
- Können als Dictionary-Keys verwendet werden

**Syntax:**
```python
# Leeres Tuple
leeres_tuple = ()

# Tuple mit Elementen
koordinaten = (10, 20)
person = ("Anna", 25, "Berlin")

# Tuple mit einem Element (Komma wichtig!)
einzeln = (5,)

# Tuple ohne Klammern (Tuple Packing)
punkt = 10, 20, 30
```

**Wichtige Operationen:**
```python
mein_tuple = (1, 2, 3, 2, 4)

# Länge
laenge = len(mein_tuple)     # 5

# Zugriff per Index
erstes = mein_tuple[0]       # 1

# Slicing
teil = mein_tuple[1:3]       # (2, 3)

# Element zählen
anzahl = mein_tuple.count(2) # 2

# Index finden
index = mein_tuple.index(3)  # 2

# Tuple Unpacking
a, b, c, d, e = mein_tuple
```

### Übung 2: Koordinatensystem

**Aufgabe:**

Erstelle ein Programm für ein 2D-Koordinatensystem:

1. Erstelle mehrere Punkte als Tuples (x, y) Koordinaten
   - Punkt A: (0, 0)
   - Punkt B: (3, 4)
   - Punkt C: (6, 8)
   - Punkt D: (3, 4)

2. Speichere alle Punkte in einer Liste

3. Berechne für jeden Punkt die Distanz zum Ursprung (0, 0)
   - Formel: `sqrt(x² + y²)` bzw. `(x² + y²) ** 0.5`

4. Prüfe, ob es doppelte Punkte gibt
   - Zähle wie oft Punkt B (3, 4) vorkommt

5. Entpacke die Koordinaten von Punkt C und gib x und y einzeln aus

6. Erstelle ein Tuple mit allen Distanzen und gib es aus

**Hinweise:**
- Tuples eignen sich perfekt für Koordinaten (unveränderlich)
- Nutze `tuple.count()` zum Zählen
- Nutze Tuple Unpacking: `x, y = punkt`
- Du kannst Tuples in Listen speichern

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 2: Koordinatensystem
Musterlösung mit Erklärungen
"""

print("=== 2D Koordinatensystem ===\n")

# Schritt 1: Punkte als Tuples erstellen
# Tuples sind ideal für Koordinaten, da sie unveränderlich sind
punkt_a = (0, 0)
punkt_b = (3, 4)
punkt_c = (6, 8)
punkt_d = (3, 4)

# Schritt 2: Alle Punkte in einer Liste speichern
# Listen können Tuples enthalten
punkte = [punkt_a, punkt_b, punkt_c, punkt_d]

print("Alle Punkte:")
for i, punkt in enumerate(punkte, start=1):
    print(f"Punkt {i}: {punkt}")

# Schritt 3: Distanz zum Ursprung berechnen
print("\nDistanzen zum Ursprung (0, 0):")
distanzen = []

for punkt in punkte:
    # Tuple Unpacking: x und y aus dem Tuple extrahieren
    x, y = punkt
    
    # Distanzformel: sqrt(x² + y²) = (x² + y²) ** 0.5
    distanz = (x**2 + y**2) ** 0.5
    distanzen.append(distanz)
    
    print(f"Punkt {punkt}: {distanz:.2f} Einheiten")

# Schritt 4: Doppelte Punkte prüfen
# count() zählt Vorkommen in der Liste
anzahl_b = punkte.count(punkt_b)
print(f"\nPunkt {punkt_b} kommt {anzahl_b} mal vor")

if anzahl_b > 1:
    print("Es gibt doppelte Punkte!")

# Schritt 5: Koordinaten von Punkt C entpacken
# Tuple Unpacking ist sehr praktisch
x_c, y_c = punkt_c
print(f"\nPunkt C entpackt:")
print(f"  x-Koordinate: {x_c}")
print(f"  y-Koordinate: {y_c}")

# Schritt 6: Tuple mit allen Distanzen erstellen
# Konvertierung von Liste zu Tuple
distanzen_tuple = tuple(distanzen)
print(f"\nAlle Distanzen als Tuple: {distanzen_tuple}")

# Zusatz: Formatierte Ausgabe
print("\nFormatierte Distanzen:")
for i, dist in enumerate(distanzen_tuple):
    print(f"Distanz {i+1}: {dist:.2f}")

"""
Erklärungen:

1. Tuples sind unveränderlich - perfekt für Koordinaten
2. Tuples brauchen weniger Speicher als Listen
3. Tuple Unpacking macht Code lesbarer: x, y = punkt
4. count() funktioniert auch mit Tuples als Elemente
5. tuple() konvertiert Listen zu Tuples
6. Tuples können als Dictionary-Keys verwendet werden (Listen nicht!)

Wann Tuples verwenden?
- Daten sollen nicht verändert werden
- Als Dictionary-Keys
- Return-Werte von Funktionen
- Koordinaten, RGB-Farben, etc.
"""
```

</details>

---

## Teil 3: Sets

### Was sind Sets?

Sets sind ungeordnete Sammlungen von einzigartigen Elementen. Sie sind ideal zum Entfernen von Duplikaten und für Mengenoperationen.

**Eigenschaften:**
- Ungeordnet: Keine feste Reihenfolge
- Keine Duplikate: Jedes Element nur einmal
- Veränderbar: Elemente können hinzugefügt/entfernt werden
- Kein Index-Zugriff möglich
- Sehr schnelle Mitgliedschaftstests
- Unterstützt mathematische Mengenoperationen

**Syntax:**
```python
# Leeres Set (nicht {} - das ist ein Dictionary!)
leeres_set = set()

# Set mit Elementen
zahlen = {1, 2, 3, 4, 5}
namen = {"Anna", "Ben", "Clara"}

# Set aus Liste erstellen (entfernt Duplikate)
liste = [1, 2, 2, 3, 3, 3]
zahlen_set = set(liste)      # {1, 2, 3}
```

**Wichtige Operationen:**
```python
mein_set = {1, 2, 3}

# Element hinzufügen
mein_set.add(4)              # {1, 2, 3, 4}

# Mehrere Elemente hinzufügen
mein_set.update([5, 6])      # {1, 2, 3, 4, 5, 6}

# Element entfernen
mein_set.remove(2)           # {1, 3, 4, 5, 6}
# oder
mein_set.discard(7)          # Kein Fehler wenn nicht vorhanden

# Prüfen ob Element vorhanden
if 3 in mein_set:
    print("3 ist im Set")

# Mengenoperationen
set1 = {1, 2, 3}
set2 = {3, 4, 5}

vereinigung = set1 | set2         # {1, 2, 3, 4, 5}
schnittmenge = set1 & set2        # {3}
differenz = set1 - set2           # {1, 2}
sym_differenz = set1 ^ set2       # {1, 2, 4, 5}
```

### Übung 3: E-Mail-Verteiler bereinigen

**Aufgabe:**

Du hast drei verschiedene E-Mail-Listen von verschiedenen Veranstaltungen. Erstelle ein Programm zur Verwaltung:

1. Erstelle drei Listen mit E-Mail-Adressen:
   - Konferenz: ["anna@mail.de", "ben@mail.de", "clara@mail.de", "david@mail.de"]
   - Workshop: ["ben@mail.de", "clara@mail.de", "eva@mail.de", "frank@mail.de"]
   - Webinar: ["anna@mail.de", "clara@mail.de", "david@mail.de", "gina@mail.de"]

2. Konvertiere alle Listen in Sets

3. Finde alle einzigartigen E-Mail-Adressen (Vereinigung aller Sets)

4. Finde Personen, die an allen drei Veranstaltungen teilgenommen haben (Schnittmenge)

5. Finde Personen, die nur an der Konferenz waren (Differenz)

6. Finde Personen, die an mindestens zwei Veranstaltungen waren

7. Erstelle eine finale Mailingliste ohne Duplikate und sortiert

**Hinweise:**
- Nutze `set()` zur Konvertierung
- Vereinigung: `|` oder `.union()`
- Schnittmenge: `&` oder `.intersection()`
- Differenz: `-` oder `.difference()`

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 3: E-Mail-Verteiler bereinigen
Musterlösung mit Erklärungen
"""

print("=== E-Mail-Verteiler Manager ===\n")

# Schritt 1: Listen mit E-Mail-Adressen erstellen
konferenz_liste = ["anna@mail.de", "ben@mail.de", "clara@mail.de", "david@mail.de"]
workshop_liste = ["ben@mail.de", "clara@mail.de", "eva@mail.de", "frank@mail.de"]
webinar_liste = ["anna@mail.de", "clara@mail.de", "david@mail.de", "gina@mail.de"]

print("Ursprüngliche Listen:")
print(f"Konferenz: {len(konferenz_liste)} Teilnehmer")
print(f"Workshop: {len(workshop_liste)} Teilnehmer")
print(f"Webinar: {len(webinar_liste)} Teilnehmer")

# Schritt 2: Listen in Sets konvertieren
# Sets entfernen automatisch Duplikate
konferenz = set(konferenz_liste)
workshop = set(workshop_liste)
webinar = set(webinar_liste)

# Schritt 3: Alle einzigartigen E-Mail-Adressen (Vereinigung)
# Der | Operator oder .union() vereinigt alle Sets
alle_teilnehmer = konferenz | workshop | webinar
print(f"\n--- Alle einzigartigen Teilnehmer ---")
print(f"Gesamtanzahl: {len(alle_teilnehmer)}")
for email in sorted(alle_teilnehmer):
    print(f"  - {email}")

# Schritt 4: Personen bei allen drei Veranstaltungen (Schnittmenge)
# Der & Operator oder .intersection() findet gemeinsame Elemente
alle_drei = konferenz & workshop & webinar
print(f"\n--- An allen drei Veranstaltungen teilgenommen ---")
if alle_drei:
    print(f"Anzahl: {len(alle_drei)}")
    for email in alle_drei:
        print(f"  - {email}")
else:
    print("Niemand war bei allen drei Veranstaltungen")

# Schritt 5: Nur an Konferenz teilgenommen (Differenz)
# Der - Operator oder .difference() findet Elemente nur im ersten Set
nur_konferenz = konferenz - workshop - webinar
print(f"\n--- Nur an Konferenz teilgenommen ---")
print(f"Anzahl: {len(nur_konferenz)}")
for email in nur_konferenz:
    print(f"  - {email}")

# Schritt 6: Mindestens an zwei Veranstaltungen teilgenommen
# Variante 1: Alle Kombinationen prüfen
konferenz_und_workshop = konferenz & workshop
konferenz_und_webinar = konferenz & webinar
workshop_und_webinar = workshop & webinar

# Vereinigung aller Zweier-Schnittmengen
mindestens_zwei = konferenz_und_workshop | konferenz_und_webinar | workshop_und_webinar

# Variante 2: Elegant mit Zählung (Booleans als 0/1)
# mindestens_zwei = {
#     email for email in alle_teilnehmer
#     if (email in konferenz) + (email in workshop) + (email in webinar) >= 2
# }

print(f"\n--- An mindestens zwei Veranstaltungen teilgenommen ---")
print(f"Anzahl: {len(mindestens_zwei)}")
for email in sorted(mindestens_zwei):
    # Zählen bei wie vielen Veranstaltungen die Person war
    anzahl = 0
    if email in konferenz:
        anzahl += 1
    if email in workshop:
        anzahl += 1
    if email in webinar:
        anzahl += 1
    print(f"  - {email} ({anzahl} Veranstaltungen)")

# Schritt 7: Finale sortierte Mailingliste
print(f"\n--- Finale Mailingliste (sortiert, ohne Duplikate) ---")
finale_liste = sorted(alle_teilnehmer)
print(f"Gesamtanzahl: {len(finale_liste)}\n")
for i, email in enumerate(finale_liste, start=1):
    print(f"{i}. {email}")

# Zusatz: Statistik
print(f"\n--- Statistik ---")
print(f"Ursprünglich: {len(konferenz_liste) + len(workshop_liste) + len(webinar_liste)} Einträge")
print(f"Nach Duplikat-Entfernung: {len(alle_teilnehmer)} einzigartige Adressen")
print(f"Duplikate entfernt: {len(konferenz_liste) + len(workshop_liste) + len(webinar_liste) - len(alle_teilnehmer)}")

"""
Erklärungen:

1. Sets sind ideal zum Entfernen von Duplikaten
2. Set-Operationen sind sehr schnell (schneller als Listen-Vergleiche)
3. Mengenoperationen:
   - Vereinigung (|): Alle Elemente aus beiden Sets
   - Schnittmenge (&): Nur gemeinsame Elemente
   - Differenz (-): Elemente nur im ersten Set
   - Symmetrische Differenz (^): Elemente in genau einem Set

4. Sets sind ungeordnet, daher sorted() für sortierte Ausgabe
5. 'in' ist bei Sets sehr schnell (O(1) vs O(n) bei Listen)

Wann Sets verwenden?
- Duplikate entfernen
- Mitgliedschaftstests (x in set)
- Mengenoperationen (Schnittmenge, Vereinigung, etc.)
- Unique Collections
"""
```

</details>

---

## Teil 4: Dictionaries

### Was sind Dictionaries?

Dictionaries (Dicts) speichern Daten als Schlüssel-Wert-Paare. Sie sind ideal für strukturierte Daten und schnelle Lookups.

**Eigenschaften:**
- Schlüssel-Wert-Paare
- Schlüssel müssen einzigartig sein
- Schlüssel müssen unveränderbar sein (Strings, Zahlen, Tuples)
- Werte können beliebig sein
- Geordnet (seit Python 3.7 garantiert, in CPython ab 3.6 implementiert)
- Sehr schneller Zugriff über Schlüssel

**Syntax:**
```python
# Leeres Dictionary
leeres_dict = {}
# oder
leeres_dict = dict()

# Dictionary mit Daten
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Berlin"
}

# Verschachtelte Dictionaries
adressbuch = {
    "Anna": {"telefon": "123", "email": "anna@mail.de"},
    "Ben": {"telefon": "456", "email": "ben@mail.de"}
}
```

**Wichtige Operationen:**
```python
person = {"name": "Anna", "alter": 25}

# Wert abrufen
name = person["name"]              # "Anna"
# oder sicherer mit get()
alter = person.get("alter")        # 25
alter = person.get("groesse", 0)   # 0 (Standardwert)

# Wert hinzufügen/ändern
person["stadt"] = "Berlin"         # hinzufügen
person["alter"] = 26               # ändern

# Wert löschen (eine Variante wählen!)
del person["stadt"]
# oder sicherer (wirft keinen Fehler wenn Key nicht existiert):
person.pop("stadt", None)

# Prüfen ob Schlüssel existiert
if "name" in person:
    print("Name vorhanden")

# Alle Schlüssel
keys = person.keys()

# Alle Werte
values = person.values()

# Alle Paare
items = person.items()

# Über Dictionary iterieren
for key, value in person.items():
    print(f"{key}: {value}")
```

### Übung 4: Studentenverwaltung

**Aufgabe:**

Erstelle ein umfassendes Studentenverwaltungssystem:

1. Erstelle ein Dictionary für jeden Studenten mit:
   - Name
   - Matrikelnummer
   - Studienfach
   - Semester
   - Noten (als Liste)

2. Erstelle mindestens 3 Studenten:
   - Anna: Informatik, 3. Semester, Noten: [1.3, 1.7, 2.0, 1.0]
   - Ben: Mathematik, 5. Semester, Noten: [2.3, 2.0, 1.7, 2.7]
   - Clara: Physik, 2. Semester, Noten: [1.0, 1.3, 1.7]

3. Speichere alle Studenten in einem Haupt-Dictionary (Matrikelnummer als Schlüssel)

4. Berechne für jeden Studenten:
   - Durchschnittsnote
   - Anzahl der bestandenen Prüfungen
   - Beste Note

5. Finde den Studenten mit der besten Durchschnittsnote

6. Erstelle eine Statistik:
   - Wie viele Studenten pro Studienfach
   - Durchschnittliche Note über alle Studenten

7. Füge einem Studenten eine neue Note hinzu

8. Gib alle Informationen formatiert aus

**Hinweise:**
- Nutze verschachtelte Dictionaries
- Nutze `.items()` zum Iterieren
- Nutze `.get()` für sichere Zugriffe
- Nutze `sum()` und `len()` für Durchschnitte

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 4: Studentenverwaltung
Musterlösung mit Erklärungen
"""

print("=== Studentenverwaltungssystem ===\n")

# Schritt 1 & 2: Studenten erstellen
# Jeder Student ist ein Dictionary mit verschiedenen Informationen
# Verschachtelte Struktur: Dict im Dict
student_anna = {
    "name": "Anna",
    "matrikelnummer": "12345",
    "studienfach": "Informatik",
    "semester": 3,
    "noten": [1.3, 1.7, 2.0, 1.0]
}

student_ben = {
    "name": "Ben",
    "matrikelnummer": "23456",
    "studienfach": "Mathematik",
    "semester": 5,
    "noten": [2.3, 2.0, 1.7, 2.7]
}

student_clara = {
    "name": "Clara",
    "matrikelnummer": "34567",
    "studienfach": "Physik",
    "semester": 2,
    "noten": [1.0, 1.3, 1.7]
}

# Schritt 3: Alle Studenten in einem Haupt-Dictionary
# Matrikelnummer als Schlüssel für schnellen Zugriff
studenten = {
    "12345": student_anna,
    "23456": student_ben,
    "34567": student_clara
}

print(f"Anzahl der Studenten: {len(studenten)}\n")

# Schritt 4: Berechnungen für jeden Studenten
print("--- Studentendetails ---\n")

for matrikel, student in studenten.items():
    name = student["name"]
    noten = student["noten"]
    
    # Durchschnittsnote berechnen
    durchschnitt = sum(noten) / len(noten)
    
    # Anzahl bestandener Prüfungen (Note <= 4.0)
    bestanden = len([note for note in noten if note <= 4.0])
    
    # Beste Note (kleinste Zahl ist beste Note)
    beste = min(noten)
    
    # In Dictionary speichern für spätere Verwendung
    student["durchschnitt"] = durchschnitt
    student["bestanden"] = bestanden
    student["beste_note"] = beste
    
    # Ausgabe
    print(f"Student: {name}")
    print(f"  Matrikelnummer: {matrikel}")
    print(f"  Studienfach: {student['studienfach']}")
    print(f"  Semester: {student['semester']}")
    print(f"  Noten: {noten}")
    print(f"  Durchschnittsnote: {durchschnitt:.2f}")
    print(f"  Bestandene Prüfungen: {bestanden}")
    print(f"  Beste Note: {beste}")
    print()

# Schritt 5: Student mit bester Durchschnittsnote finden
bester_student = None
beste_durchschnitt = float('inf')  # Startwert: unendlich

for matrikel, student in studenten.items():
    if student["durchschnitt"] < beste_durchschnitt:
        beste_durchschnitt = student["durchschnitt"]
        bester_student = student

print("--- Bester Student ---")
print(f"Name: {bester_student['name']}")
print(f"Durchschnittsnote: {bester_student['durchschnitt']:.2f}\n")

# Schritt 6: Statistiken erstellen
print("--- Statistiken ---\n")

# Studenten pro Studienfach
faecher = {}
for student in studenten.values():
    fach = student["studienfach"]
    # Wenn Fach noch nicht im Dict, initialisiere mit 0
    if fach not in faecher:
        faecher[fach] = 0
    faecher[fach] += 1

print("Studenten pro Studienfach:")
for fach, anzahl in faecher.items():
    print(f"  {fach}: {anzahl} Student(en)")

# Durchschnittliche Note über alle Studenten
alle_noten = []
for student in studenten.values():
    alle_noten.extend(student["noten"])

gesamt_durchschnitt = sum(alle_noten) / len(alle_noten)
print(f"\nGesamtdurchschnitt aller Noten: {gesamt_durchschnitt:.2f}")
print(f"Gesamtanzahl Prüfungen: {len(alle_noten)}")

# Schritt 7: Neue Note hinzufügen
print("\n--- Note hinzufügen ---")
# Wir fügen Anna eine neue Note hinzu
studenten["12345"]["noten"].append(1.7)
print(f"Neue Note für {studenten['12345']['name']} hinzugefügt")
print(f"Aktualisierte Noten: {studenten['12345']['noten']}")

# Durchschnitt neu berechnen
neue_noten = studenten["12345"]["noten"]
neuer_durchschnitt = sum(neue_noten) / len(neue_noten)
studenten["12345"]["durchschnitt"] = neuer_durchschnitt
print(f"Neuer Durchschnitt: {neuer_durchschnitt:.2f}")

# Schritt 8: Finale formatierte Ausgabe
print("\n" + "="*60)
print("FINALE STUDENTENÜBERSICHT")
print("="*60)

for matrikel, student in studenten.items():
    print(f"\nMatrikelnummer: {matrikel}")
    print(f"Name: {student['name']}")
    print(f"Studienfach: {student['studienfach']} ({student['semester']}. Semester)")
    print(f"Noten: {student['noten']}")
    print(f"Durchschnitt: {student['durchschnitt']:.2f}")
    print(f"Beste Note: {student['beste_note']}")
    print("-" * 60)

"""
Erklärungen:

1. Dictionaries mit verschachtelten Strukturen:
   - Äußeres Dict: Matrikelnummer -> Student
   - Inneres Dict: Studenteninformationen
   - Listen innerhalb: Noten

2. .items() gibt Schlüssel-Wert-Paare zurück
   - Perfekt zum Iterieren über Dictionaries

3. .values() gibt nur die Werte zurück
   - Nützlich wenn Schlüssel nicht benötigt werden

4. Dictionary dynamisch erweitern:
   - student["neue_eigenschaft"] = wert

5. get() vs []:
   - dict.get("key", default) ist sicherer
   - dict["key"] wirft Fehler wenn key nicht existiert

6. Verschachtelte Zugriffe:
   - studenten["12345"]["noten"] greift auf verschachtelte Daten zu

Wann Dictionaries verwenden?
- Strukturierte Daten (JSON-ähnlich)
- Schnelle Lookups über Schlüssel
- Konfigurationen
- Datenbank-ähnliche Strukturen
- APIs und Datenübertragung

Best Practices:
- Aussagekräftige Schlüsselnamen
- .get() für optionale Werte
- Konsistente Struktur bei mehreren gleichartigen Dicts
"""
```

</details>

---

## Kombinierte Übung: Bibliotheksverwaltung (Achtung, diese Übung ist sehr schwer und nur für die von euch gedacht die schon länger mit Python arbeiten)

### Aufgabe

Erstelle ein komplettes Bibliotheksverwaltungssystem, das alle vier Datenstrukturen verwendet:

1. **Dictionary** für Bücher:
   - Jedes Buch hat: Titel, Autor, ISBN, Jahr, Kategorien (als Set), Bewertungen (als Liste)
   - Erstelle mindestens 4 Bücher

2. **Liste** für die Reihenfolge der Neuanschaffungen

3. **Set** für alle verfügbaren Kategorien

4. **Tuple** für Buch-Metadaten (ISBN, Titel) - unveränderliche Identifikation

Funktionen:
- Füge ein neues Buch hinzu
- Finde alle Bücher in einer Kategorie
- Berechne Durchschnittsbewertung pro Buch
- Finde Bücher mit überlappenden Kategorien
- Erstelle einen Jahresbericht

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Kombinierte Übung: Bibliotheksverwaltung
Nutzt alle vier Datenstrukturen
Musterlösung mit Erklärungen
"""

print("=== Bibliotheksverwaltungssystem ===\n")

# Dictionary für Bücher (ISBN als Schlüssel)
bibliothek = {
    "978-3-16-148410-0": {
        "titel": "Python für Anfänger",
        "autor": "Max Mustermann",
        "jahr": 2020,
        "kategorien": {"Programmierung", "Python", "Anfänger"},  # Set
        "bewertungen": [4.5, 5.0, 4.0, 4.8]  # Liste
    },
    "978-3-16-148411-7": {
        "titel": "Datenstrukturen und Algorithmen",
        "autor": "Anna Schmidt",
        "jahr": 2019,
        "kategorien": {"Programmierung", "Algorithmen", "Informatik"},
        "bewertungen": [4.8, 4.9, 5.0]
    },
    "978-3-16-148412-4": {
        "titel": "Webentwicklung Grundlagen",
        "autor": "Ben Weber",
        "jahr": 2021,
        "kategorien": {"Programmierung", "Web", "HTML", "CSS"},
        "bewertungen": [4.2, 4.5, 4.0, 4.3, 4.7]
    },
    "978-3-16-148413-1": {
        "titel": "Machine Learning Praxis",
        "autor": "Clara Data",
        "jahr": 2022,
        "kategorien": {"Python", "KI", "Machine Learning"},
        "bewertungen": [5.0, 4.9, 4.8, 5.0]
    }
}

# Liste für Reihenfolge der Neuanschaffungen (chronologisch)
neuanschaffungen = [
    "978-3-16-148410-0",
    "978-3-16-148411-7",
    "978-3-16-148412-4",
    "978-3-16-148413-1"
]

# Set für alle verfügbaren Kategorien (automatisch unique)
alle_kategorien = set()
for buch in bibliothek.values():
    alle_kategorien.update(buch["kategorien"])

print("--- Bibliotheksübersicht ---")
print(f"Anzahl Bücher: {len(bibliothek)}")
print(f"Verfügbare Kategorien: {sorted(alle_kategorien)}\n")

# Funktion 1: Neues Buch hinzufügen
def buch_hinzufuegen(isbn, titel, autor, jahr, kategorien, bewertungen=None):
    """Fügt ein neues Buch zur Bibliothek hinzu"""
    if bewertungen is None:
        bewertungen = []
    
    bibliothek[isbn] = {
        "titel": titel,
        "autor": autor,
        "jahr": jahr,
        "kategorien": set(kategorien),  # Sicherstellen dass es ein Set ist
        "bewertungen": bewertungen
    }
    
    neuanschaffungen.append(isbn)
    alle_kategorien.update(kategorien)
    
    print(f"Buch '{titel}' wurde hinzugefügt!")

# Neues Buch hinzufügen
print("--- Neues Buch hinzufügen ---")
buch_hinzufuegen(
    "978-3-16-148414-8",
    "Datenbanken verstehen",
    "David DB",
    2023,
    ["Datenbanken", "SQL", "Informatik"],
    [4.5]
)
print()

# Funktion 2: Bücher in Kategorie finden
def buecher_in_kategorie(kategorie):
    """Findet alle Bücher in einer bestimmten Kategorie"""
    gefundene_buecher = []
    
    for isbn, buch in bibliothek.items():
        # Set-Mitgliedschaft ist sehr schnell
        if kategorie in buch["kategorien"]:
            gefundene_buecher.append((isbn, buch["titel"]))
    
    return gefundene_buecher

print("--- Bücher in Kategorie 'Programmierung' ---")
programmier_buecher = buecher_in_kategorie("Programmierung")
for isbn, titel in programmier_buecher:
    print(f"  - {titel} (ISBN: {isbn})")
print()

# Funktion 3: Durchschnittsbewertung berechnen
print("--- Durchschnittsbewertungen ---")
for isbn, buch in bibliothek.items():
    bewertungen = buch["bewertungen"]
    
    if bewertungen:  # Nur wenn Bewertungen vorhanden
        durchschnitt = sum(bewertungen) / len(bewertungen)
        print(f"{buch['titel']}: {durchschnitt:.2f} ⭐ ({len(bewertungen)} Bewertungen)")
    else:
        print(f"{buch['titel']}: Noch keine Bewertungen")
print()

# Funktion 4: Bücher mit überlappenden Kategorien finden
def finde_aehnliche_buecher(isbn):
    """Findet Bücher mit gemeinsamen Kategorien"""
    if isbn not in bibliothek:
        return []
    
    buch_kategorien = bibliothek[isbn]["kategorien"]
    aehnliche = []
    
    for andere_isbn, anderes_buch in bibliothek.items():
        if andere_isbn == isbn:
            continue
        
        # Set-Intersection für gemeinsame Kategorien
        gemeinsame = buch_kategorien & anderes_buch["kategorien"]
        
        if gemeinsame:
            aehnliche.append({
                "isbn": andere_isbn,
                "titel": anderes_buch["titel"],
                "gemeinsame_kategorien": gemeinsame
            })
    
    return aehnliche

print("--- Ähnliche Bücher zu 'Python für Anfänger' ---")
aehnliche = finde_aehnliche_buecher("978-3-16-148410-0")
for buch in aehnliche:
    print(f"  - {buch['titel']}")
    print(f"    Gemeinsame Kategorien: {', '.join(buch['gemeinsame_kategorien'])}")
print()

# Funktion 5: Jahresbericht erstellen
print("--- Jahresbericht ---")

# Bücher pro Jahr
buecher_pro_jahr = {}
for buch in bibliothek.values():
    jahr = buch["jahr"]
    if jahr not in buecher_pro_jahr:
        buecher_pro_jahr[jahr] = 0
    buecher_pro_jahr[jahr] += 1

print("\nBücher pro Erscheinungsjahr:")
for jahr in sorted(buecher_pro_jahr.keys()):
    print(f"  {jahr}: {buecher_pro_jahr[jahr]} Buch/Bücher")

# Kategoriestatistik
kategorie_count = {}
for buch in bibliothek.values():
    for kategorie in buch["kategorien"]:
        if kategorie not in kategorie_count:
            kategorie_count[kategorie] = 0
        kategorie_count[kategorie] += 1

print("\nBücher pro Kategorie:")
# Sortiert nach Anzahl (absteigend)
for kategorie, anzahl in sorted(kategorie_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {kategorie}: {anzahl} Buch/Bücher")

# Gesamtbewertung
alle_bewertungen = []
for buch in bibliothek.values():
    alle_bewertungen.extend(buch["bewertungen"])

if alle_bewertungen:
    gesamt_durchschnitt = sum(alle_bewertungen) / len(alle_bewertungen)
    print(f"\nGesamtdurchschnitt aller Bewertungen: {gesamt_durchschnitt:.2f} ⭐")
    print(f"Anzahl aller Bewertungen: {len(alle_bewertungen)}")

# Neueste Anschaffungen (letzten 3)
print("\n--- Neueste Anschaffungen (letzte 3) ---")
for isbn in neuanschaffungen[-3:]:
    buch = bibliothek[isbn]
    print(f"  - {buch['titel']} ({buch['jahr']})")

# Tuple für Buch-Metadaten (unveränderliche Referenzen)
print("\n--- Buch-Referenzen als Tuples ---")
buch_referenzen = []
for isbn, buch in bibliothek.items():
    # Tuple: (ISBN, Titel) - unveränderlich, kann als Dict-Key verwendet werden
    referenz = (isbn, buch["titel"])
    buch_referenzen.append(referenz)

print("Alle Buch-Referenzen:")
for isbn, titel in sorted(buch_referenzen, key=lambda x: x[1]):
    print(f"  {titel}: {isbn}")

"""
Zusammenfassung - Alle Datenstrukturen im Einsatz:

1. DICTIONARY (bibliothek):
   - Schneller Zugriff über ISBN
   - Strukturierte Daten pro Buch
   - Verschachtelte Struktur

2. LISTE (neuanschaffungen, bewertungen):
   - Reihenfolge wichtig (chronologisch)
   - Duplikate erlaubt (bei Bewertungen)
   - Index-Zugriff möglich

3. SET (kategorien, alle_kategorien):
   - Keine Duplikate
   - Schnelle Mengenoperationen (intersection, union)
   - Ideal für Tags/Kategorien

4. TUPLE (buch_referenzen):
   - Unveränderlich
   - Als Dictionary-Keys verwendbar
   - Für feste Paare (ISBN, Titel)

Best Practices demonstriert:
- Richtige Datenstruktur für richtigen Zweck
- Kombination verschiedener Strukturen
- Effiziente Operationen (Set-Intersection statt Listen-Vergleich)
- Funktionen für Wiederverwendbarkeit
- Klare Namensgebung
"""

print("\n" + "="*60)
print("Bibliotheksverwaltung abgeschlossen!")
print("="*60)
```

</details>

---

## Zusammenfassung

### Wann welche Datenstruktur verwenden?

| Datenstruktur | Verwendung | Eigenschaften |
|---------------|------------|---------------|
| **Liste** | Geordnete Sammlung, die sich ändert | Veränderbar, geordnet, Duplikate erlaubt |
| **Tuple** | Unveränderliche Daten, Koordinaten | Unveränderbar, geordnet, schneller als Liste |
| **Set** | Duplikate entfernen, Mengenoperationen | Keine Duplikate, ungeordnet, schnelle Tests |
| **Dictionary** | Schlüssel-Wert-Zuordnungen | Schneller Zugriff, strukturierte Daten |


### Wichtige Methoden im Überblick

**Listen:**
- `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `extend()`

**Tuples:**
- `count()`, `index()`, Tuple Unpacking

**Sets:**
- `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`

**Dictionaries:**
- `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`
