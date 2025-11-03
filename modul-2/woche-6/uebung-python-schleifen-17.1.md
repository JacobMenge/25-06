# Praktische Übungen: Schleifen in Python

## Übung 1: Früchtekorb (for-Schleife Grundlagen)

### Aufgabe
Erstelle ein Programm, das einen Früchtekorb verwaltet.

### Schritte:

**Schritt 1:** Erstelle eine Liste mit 5 Früchten
```python
fruechte = ["Apfel", "Banane", "Orange", "Kiwi", "Mango"]
```

**Schritt 2:** Gib jede Frucht mit einer for-Schleife aus
- Format: "Frucht Nr. X: [Name]"

**Schritt 3:** Zähle die Gesamtanzahl der Früchte

**Schritt 4:** Verwende `enumerate()`, um die Position mit auszugeben

### Hinweise:
- Nutze `enumerate()` für automatische Nummerierung
- Denke an die Einrückung im Schleifenkörper

<details>
<summary>Musterlösung anzeigen</summary>

```python
# Schritt 1: Liste erstellen
fruechte = ["Apfel", "Banane", "Orange", "Kiwi", "Mango"]

# Schritt 2: Früchte ausgeben
print("=== Mein Früchtekorb ===\n")
for frucht in fruechte:
    print(f"Leckere Frucht: {frucht}")

# Schritt 3: Anzahl zählen
anzahl = 0
for frucht in fruechte:
    anzahl += 1
print(f"\nGesamtanzahl: {anzahl} Früchte")

# Schritt 4: Mit enumerate()
print("\n=== Mit Position ===")
for index, frucht in enumerate(fruechte):
    print(f"Frucht Nr. {index + 1}: {frucht}")
```

</details>

---

## Übung 2: Countdown-Timer (while-Schleife)

### Aufgabe
Erstelle einen Countdown-Timer, der von einer eingegebenen Zahl bis 0 herunterzählt.

### Schritte:

**Schritt 1:** Frage den Benutzer nach einer Startzahl (z.B. 10)

**Schritt 2:** Erstelle eine while-Schleife, die solange läuft, bis die Zahl 0 erreicht

**Schritt 3:** Gib in jedem Durchlauf die aktuelle Zahl aus

**Schritt 4:** Verringere die Zahl um 1 in jedem Durchlauf

**Schritt 5:** Gib am Ende "Start!" aus

### Hinweise:
- Vergiss nicht, die Variable zu verringern (sonst Endlosschleife!)
- Nutze `input()` und wandle in `int()` um

<details>
<summary>Musterlösung anzeigen</summary>

```python
print("=== Countdown-Timer ===\n")

# Schritt 1: Startzahl abfragen
startzahl = int(input("Von welcher Zahl soll heruntergezählt werden? "))

# Schritt 2-4: While-Schleife
countdown = startzahl
while countdown > 0:
    print(f"Noch {countdown} Sekunden...")
    countdown -= 1

# Schritt 5: Start-Meldung
print("Start!")
```

</details>

---

## Übung 3: Gerade Zahlen finden (range() und if)

### Aufgabe
Erstelle ein Programm, das alle geraden Zahlen zwischen 1 und 20 findet und ausgibt.

### Schritte:

**Schritt 1:** Nutze `range(1, 21)` für die Zahlen 1-20

**Schritt 2:** Prüfe in der Schleife, ob die Zahl gerade ist (Hinweis: `%` Operator)

**Schritt 3:** Gib nur die geraden Zahlen aus

**Schritt 4:** Zähle, wie viele gerade Zahlen gefunden wurden

### Hinweise:
- Eine Zahl ist gerade, wenn `zahl % 2 == 0`
- Nutze einen Zähler für die Anzahl

<details>
<summary>Musterlösung anzeigen</summary>

```python
print("=== Gerade Zahlen finden ===\n")

# Zähler initialisieren
anzahl_gerade = 0

# Schritt 1-3: Zahlen durchlaufen und prüfen
for zahl in range(1, 21):
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade")
        anzahl_gerade += 1

# Schritt 4: Ergebnis
print(f"\nGefunden: {anzahl_gerade} gerade Zahlen")
```

</details>

---

## Übung 4: Passwortstärke-Checker (break und continue)

### Aufgabe
Erstelle einen Passwort-Checker, der Passwörter auf ihre Stärke prüft.

### Schritte:

**Schritt 1:** Erstelle eine Liste mit Test-Passwörtern:
```python
passwoerter = ["12345", "abc", "Sicher123!", "test", "MeinPasswort2024!"]
```

**Schritt 2:** Iteriere über die Passwörter mit einer for-Schleife

**Schritt 3:** Überspringe (continue) Passwörter, die kürzer als 5 Zeichen sind

**Schritt 4:** Stoppe (break) die Schleife, wenn ein Passwort gefunden wird, das:
- Mindestens 10 Zeichen lang ist
- Eine Zahl enthält
- Ein Sonderzeichen enthält (z.B. !)

**Schritt 5:** Gib das erste sichere Passwort aus

### Hinweise:
- Nutze `len()` für die Länge
- `any(c.isdigit() for c in passwort)` prüft auf Zahlen
- `any(c in "!@#$%^&*()" for c in passwort)` prüft auf Sonderzeichen

<details>
<summary>Musterlösung anzeigen</summary>

```python
print("=== Passwortstärke-Checker ===\n")

passwoerter = ["12345", "abc", "Sicher123!", "test", "MeinPasswort2024!"]

for passwort in passwoerter:
    print(f"Prüfe: {passwort}")
    
    # Schritt 3: Zu kurze Passwörter überspringen
    if len(passwort) < 5:
        print("  Zu kurz (< 5 Zeichen) - übersprungen\n")
        continue
    
    # Schritt 4: Prüfung auf sicheres Passwort
    hat_zahl = any(c.isdigit() for c in passwort)
    hat_sonderzeichen = any(c in "!@#$%^&*()" for c in passwort)
    
    if len(passwort) >= 10 and hat_zahl and hat_sonderzeichen:
        print(f"  Sicheres Passwort gefunden!")
        print(f"  Länge: {len(passwort)} Zeichen")
        print(f"  Enthält Zahl: Ja")
        print(f"  Enthält Sonderzeichen: Ja")
        break
    else:
        print("  Nicht sicher genug\n")
else:
    print("Kein sicheres Passwort gefunden!")
```

</details>

---

## Übung 5: Namens-Parser (String-Iteration)

### Aufgabe
Erstelle ein Programm, das durch einen Namen iteriert und Informationen sammelt.

### Schritte:

**Schritt 1:** Frage nach einem Namen

**Schritt 2:** Iteriere durch jeden Buchstaben

**Schritt 3:** Zähle:
- Vokale (a, e, i, o, u)
- Konsonanten
- Leerzeichen

**Schritt 4:** Gib eine Statistik aus

<details>
<summary>Musterlösung anzeigen</summary>

```python
print("=== Namens-Parser ===\n")

# Schritt 1: Namen abfragen
name = input("Gib deinen vollständigen Namen ein: ")

# Zähler initialisieren
vokale = 0
konsonanten = 0
leerzeichen = 0

# Schritt 2-3: Durch Buchstaben iterieren
for buchstabe in name:
    if buchstabe == " ":
        leerzeichen += 1
    elif buchstabe.lower() in "aeiou":
        vokale += 1
    elif buchstabe.isalpha():
        konsonanten += 1

# Schritt 4: Statistik
print("\n=== Statistik ===")
print(f"Gesamtlänge: {len(name)} Zeichen")
print(f"Vokale: {vokale}")
print(f"Konsonanten: {konsonanten}")
print(f"Leerzeichen: {leerzeichen}")
```

</details>

---

## BONUS-ÜBUNG: Login-System 2.0 (Mit Schleifen verbessern!)

### Aufgabe
Verbessere das Login-System von letzter Woche durch den Einsatz von Schleifen!

### Was war das Problem beim alten System?
Das alte System hatte viel duplizierten Code durch die verschachtelten if-else-Strukturen für die 3 Login-Versuche. Das war:
- Fehleranfällig
- Schwer zu warten
- Nicht skalierbar (was wenn wir 5 Versuche wollen?)

### Deine Aufgabe:

**Schritt 1:** Ersetze die verschachtelten if-else-Strukturen durch eine **while-Schleife**
- Die Schleife soll maximal 3 Durchläufe haben
- Nutze einen Zähler für die Versuche

**Schritt 2:** Verwende **break**, um die Schleife bei erfolgreichem Login zu beenden

**Schritt 3:** Nutze die **else-Klausel** der Schleife, um den Account zu sperren

**Schritt 4:** Behalte die restlichen Funktionen bei:
- Altersüberprüfung (>= 18)
- Rollenbasierter Zugriff mit match-Statement

### Hinweise:
- Nutze eine Variable `max_versuche = 3`
- Zähle mit `versuche_verwendet = 0`
- Die Schleifenbedingung: `while versuche_verwendet < max_versuche`
- Das `else` bei einer Schleife wird nur ausgeführt, wenn **kein break** aufgetreten ist

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Authentifizierungssystem 2.0
Mit Schleifen verbessert!
"""

print("=== Authentifizierungssystem 2.0 ===\n")

# Test-Credentials
KORREKTER_USERNAME = "jacob"
KORREKTES_PASSWORT = "jacob12345"

# Schritt 1: Login mit while-Schleife
MAX_VERSUCHE = 3
versuche_verwendet = 0
login_erfolgreich = False

while versuche_verwendet < MAX_VERSUCHE:
    print(f"Login-Versuch {versuche_verwendet + 1}/{MAX_VERSUCHE}")
    username = input("Benutzername: ")
    passwort = input("Passwort: ")
    
    # Prüfen ob Login erfolgreich
    if username == KORREKTER_USERNAME and passwort == KORREKTES_PASSWORT:
        print("Login erfolgreich!\n")
        login_erfolgreich = True
        break  # Schritt 2: Schleife beenden bei Erfolg
    else:
        versuche_verwendet += 1
        if versuche_verwendet < MAX_VERSUCHE:
            print(f"Falsche Anmeldedaten. Noch {MAX_VERSUCHE - versuche_verwendet} Versuch(e) übrig.\n")
        else:
            print("Falsche Anmeldedaten.\n")

# Schritt 3: else-Klausel für Account-Sperre
else:
    print("Account gesperrt! Zu viele fehlgeschlagene Versuche.\n")
    print("Programm wird beendet.")
    exit()

# Wenn Login fehlgeschlagen (sollte nicht erreicht werden nach else)
if not login_erfolgreich:
    print("Programm wird beendet.")
    exit()

# Schritt 4: Restliche Funktionen bleiben gleich
# Altersüberprüfung
alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("\nZugriff verweigert - zu jung")
    print("Du musst mindestens 18 Jahre alt sein.")
    exit()

print("Altersüberprüfung bestanden\n")

# Rollenbasierter Zugriff
print("Verfügbare Rollen: admin, user, guest")
rolle = input("Deine Rolle: ")

# Match-Statement für Rollen
match rolle:
    case "admin":
        zugriff = "Vollzugriff"
        beschreibung = "Du kannst alles sehen und bearbeiten."
    case "user":
        zugriff = "Eingeschränkter Zugriff"
        beschreibung = "Du kannst Inhalte ansehen und eigene Inhalte bearbeiten."
    case "guest":
        zugriff = "Nur Lesezugriff"
        beschreibung = "Du kannst nur Inhalte ansehen."
    case _:
        zugriff = "Keine Berechtigung"
        beschreibung = "Unbekannte Rolle. Zugriff verweigert."

# Ergebnis anzeigen
print("\n" + "="*50)
print("ZUGRIFF GEWÄHRT")
print("="*50)
print(f"Benutzer: {username}")
print(f"Alter: {alter} Jahre")
print(f"Rolle: {rolle}")
print(f"Zugriffslevel: {zugriff}")
print(f"Beschreibung: {beschreibung}")
print("="*50)
```

</details>

### Vergleich: Vorher vs. Nachher

**Vorher (ohne Schleifen):**
- ca. 45 Zeilen nur für Login-Versuche
- 3x duplizierter Code
- Schwer anzupassen

**Nachher (mit Schleifen):**
- ca. 20 Zeilen für Login-Versuche
- Kein duplizierter Code
- Einfach auf 5 oder 10 Versuche erweiterbar (nur `MAX_VERSUCHE` ändern!)

### Diskussionsfragen:
1. Welche Vorteile bietet die Schleifenlösung?
2. Was passiert, wenn ihr `MAX_VERSUCHE = 5` setzt?
3. Wie könntet ihr eine "Passwort vergessen"-Funktion einbauen?

---

## Extra-Challenge: Multiplikationstabelle

Erstelle ein Programm, das eine Multiplikationstabelle ausgibt.

<details>
<summary>Musterlösung anzeigen</summary>

```python
print("=== Multiplikationstabelle ===\n")

# Bis zu welcher Zahl?
bis = int(input("Bis welche Zahl? (z.B. 10): "))

# Verschachtelte Schleifen
for i in range(1, bis + 1):
    for j in range(1, bis + 1):
        ergebnis = i * j
        print(f"{i} × {j} = {ergebnis:3}", end="  ")
    print()  # Neue Zeile nach jeder Reihe
```

</details>

---

## Zusammenfassung

In diesen Übungen hast du gelernt:
- for-Schleifen mit Listen und Strings
- while-Schleifen für bedingte Wiederholungen
- range() für Zahlenfolgen
- enumerate() für Index + Wert
- break zum vorzeitigen Beenden
- continue zum Überspringen
- else bei Schleifen
- Praktische Anwendung: Refactoring von verschachteltem Code

Nächster Schritt: Morgen schauen wir uns Listen, Tuples, Sets und Dicts genauer an und wie man elegant über diese Datenstrukturen iteriert.