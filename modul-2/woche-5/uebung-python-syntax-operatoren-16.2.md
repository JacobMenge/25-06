# Geführte Übung: Einstieg in Python-Syntax & Operatoren

Diese Übungen helfen dir, die grundlegende Syntax von Python Schritt für Schritt zu verstehen.  
Du lernst Variablen, Datentypen, Operatoren, Eingabe und Ausgabe sowie f-Strings kennen.  
Der Schwierigkeitsgrad steigt langsam von Übung zu Übung.

---

## Übung 1: Dein erstes Programm

Erstelle eine Datei `hallo.py` und schreibe folgendes Programm:

```python
print("Hallo Welt!")
```

**Erklärung:**  
Die `print()`-Funktion gibt Text auf der Konsole aus.  
In Python müssen Strings immer in Anführungszeichen stehen – entweder `" "` oder `' '`.

**Erweiterung:**  
Ersetze `"Hallo Welt!"` durch eine persönliche Begrüßung, zum Beispiel:

```python
print("Hallo, ich starte jetzt mit Python!")
```

---

## Übung 2: Variablen und Datentypen

In dieser Übung lernst du, wie man Informationen speichert.

Erstelle Variablen für deinen Namen, dein Alter und deine Stadt:

```python
name = "Lisa"
alter = 25
stadt = "Hamburg"

print(name, alter, stadt)
```

**Erklärung:**  
Variablen sind Namen für gespeicherte Werte.  
Python erkennt den Datentyp automatisch:
- `"Lisa"` → String  
- `25` → Integer (Ganzzahl)

Probiere aus, was passiert, wenn du z. B. `alter = "25"` schreibst.  
Was ist jetzt anders?

---

## Übung 3: Mathematische Operatoren

Hier lernst du, mit Zahlen und Operatoren zu rechnen.

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Multiplikation:", a * b)
print("Division:", a / b)
print("Ganzzahl-Division:", a // b)
print("Rest:", a % b)
print("Potenz:", a ** b)
```

**Erklärung:**  
Diese Operatoren kennst du vielleicht schon aus der Mathematik.  
Neu ist zum Beispiel:
- `//` → Ganzzahldivision (Ergebnis ohne Nachkommastellen)
- `%` → Modulo (liefert den Rest einer Division)

---

## Übung 4: f-Strings und Vergleichsoperatoren

Hier kombinierst du Strings, Operatoren und einfache Logik.

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))

print(f"Hallo {name}, du bist {alter} Jahre alt.")
print(f"Nächstes Jahr wirst du {alter + 1} Jahre alt.")

print("Bist du volljährig?", alter >= 18)
```

**Erklärung:**  
- `input()` liest Benutzereingaben als Text ein.  
- Mit `int()` wandelst du sie in ganze Zahlen um.  
- Ein **f-String** erlaubt dir, Variablen direkt im Text zu verwenden.  
- Der **Vergleichsoperator `>=`** prüft, ob eine Bedingung wahr (`True`) oder falsch (`False`) ist.

---

## Übung 5: Mini-Rechner mit Benutzereingabe

Zum Abschluss kombinierst du alles Gelernte in einem kleinen Programm.

```python
print("=== Mini-Rechner ===")

zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

print(f"Summe: {zahl1 + zahl2}")
print(f"Differenz: {zahl1 - zahl2}")
print(f"Produkt: {zahl1 * zahl2}")
print(f"Quotient: {zahl1 / zahl2:.2f}")
```

**Erklärung:**  
- Mit `float()` kannst du auch Dezimalzahlen verarbeiten.  
- Die Formatierung `:.2f` zeigt das Ergebnis mit zwei Nachkommastellen.  
- So festigst du den Umgang mit Datentypen, Operatoren, Eingabe und Ausgabe.

---

## Zusammenfassung

Nach diesen Übungen solltest du sicher können:
- Text und Zahlen in Variablen speichern  
- mathematische und Vergleichsoperatoren anwenden  
- mit `print()` und `input()` arbeiten  
- Strings formatieren und berechnete Werte ausgeben  

Als Nächstes lernst du Bedingungen (`if`, `elif`, `else`) und logische Operatoren kennen.
