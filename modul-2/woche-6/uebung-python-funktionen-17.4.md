# Funktionen in Python

## Übersicht

In dieser Übung lernst du:
- **Funktionen definieren** - Wie man eigene Funktionen erstellt
- **Parameter** - Wie man Werte an Funktionen übergibt
- **Return** - Wie Funktionen Ergebnisse zurückgeben
- **Scope** - Wo Variablen gültig sind
- **Best Practices** - Wie man sauberen, wiederverwendbaren Code schreibt

---

## Übersicht nach Schwierigkeitsgrad

### GRUNDLAGEN

Diese Übungen decken die fundamentalen Konzepte ab:

- **Übung 1**: Funktionen definieren und aufrufen
- **Übung 2**: Parameter verwenden
- **Übung 3**: Return-Werte
- **Übung 4**: Parameter-Varianten (Positional, Keyword, Default)
- **Übung 5**: Scope verstehen

**Empfehlung:** Mache alle Grundlagen-Übungen in Reihenfolge, bevor du zu den fortgeschrittenen Übungen übergehst.

### FORTGESCHRITTEN

Diese Übungen kombinieren mehrere Konzepte:

- **Übung 6**: Text-Verarbeitung mit kombinierten Funktionen
- **Bonus-Übung**: Mini-Taschenrechner (Projekt)

**Empfehlung:** Diese Übungen sind anspruchsvoller und setzen voraus, dass du die Grundlagen verstanden hast. Nimm dir Zeit und baue die Programme Schritt für Schritt auf.


---

## Teil 1: Funktionen Grundlagen

### Was ist eine Funktion?

Eine Funktion ist ein wiederverwendbarer Code-Block, der eine bestimmte Aufgabe erfüllt. Stell dir eine Funktion wie ein Rezept vor: Du gibst Zutaten (Parameter) hinein, es passiert etwas (Code), und am Ende bekommst du ein Ergebnis (Return-Wert).

**Grundprinzip:**
```python
def funktionsname(parameter):
    # Hier steht der Code
    # der ausgeführt werden soll
    return ergebnis
```

### Warum Funktionen?

- **Wiederverwendbarkeit**: Einmal schreiben, mehrmals nutzen
- **Übersichtlichkeit**: Code in logische Blöcke aufteilen
- **Wartbarkeit**: Änderungen nur an einer Stelle nötig
- **Testbarkeit**: Funktionen lassen sich einzeln testen

### Eine einfache Funktion definieren

```python
def begruessung():
    print("Hallo! Willkommen zu Python-Funktionen!")

# Funktion aufrufen
begruessung()
# Ausgabe: Hallo! Willkommen zu Python-Funktionen!
```

**Wichtig:**
- `def` leitet die Funktionsdefinition ein
- Nach dem Funktionsnamen kommen Klammern `()`
- Der Code der Funktion wird eingerückt (nutze 4 Leerzeichen, mische Tabs/Spaces nicht - PEP 8)
- Zum Aufrufen: Funktionsname + Klammern

---

## Übung 1: Deine erste Funktion

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

Erstelle ein Programm mit mehreren einfachen Funktionen:

1. Eine Funktion `guten_morgen()`, die "Guten Morgen!" ausgibt
2. Eine Funktion `guten_abend()`, die "Guten Abend!" ausgibt
3. Rufe beide Funktionen nacheinander auf

**Hinweise:**
- Nutze `def` zum Definieren
- Nutze `print()` für die Ausgabe
- Vergiss nicht die Einrückung (4 Leerzeichen oder Tab)

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 1: Deine erste Funktion
Musterlösung mit Erklärungen
"""

print("=== Begrüßungsprogramm ===\n")

# Schritt 1: Funktion für Morgenbegrüßung definieren
def guten_morgen():
    print("Guten Morgen!")
    print("Ich wünsche dir einen schönen Tag!")

# Schritt 2: Funktion für Abendbegrüßung definieren
def guten_abend():
    print("Guten Abend!")
    print("Ich hoffe, du hattest einen guten Tag!")

# Schritt 3: Funktionen aufrufen
print("Morgens:")
guten_morgen()

print("\nAbends:")
guten_abend()

"""
Erklärungen:

1. DEFINITION mit def:
   - def ist das Schlüsselwort für Funktionen
   - Danach kommt der Funktionsname (sollte beschreibend sein)
   - Klammern () sind Pflicht, auch wenn leer
   - Doppelpunkt : am Ende nicht vergessen

2. EINRÜCKUNG:
   - Alles was zur Funktion gehört, wird eingerückt
   - Ohne Einrückung gehört es nicht mehr zur Funktion

3. AUFRUFEN:
   - Funktionsname + ()
   - Die Funktion wird erst ausgeführt, wenn sie aufgerufen wird
   - Du kannst eine Funktion beliebig oft aufrufen

4. REIHENFOLGE:
   - Funktion muss definiert sein, BEVOR sie aufgerufen wird
   - Python liest den Code von oben nach unten
"""
```

</details>

---

### Selbstcheck: Teil 1

Bevor du weitermachst, prüfe dein Verständnis:

1. Was passiert, wenn du eine Funktion ohne Klammern aufrufst? (z.B. `meine_funktion` statt `meine_funktion()`)
2. Muss eine Funktion etwas zurückgeben?
3. Wo muss die Funktionsdefinition stehen - vor oder nach dem Aufruf?

<details>
<summary>Antworten anzeigen</summary>

1. Die Funktion wird NICHT ausgeführt. Python zeigt nur, dass es eine Funktion ist.
2. Nein. Funktionen ohne `return` geben automatisch `None` zurück.
3. Die Definition muss VOR dem Aufruf stehen. Python liest den Code von oben nach unten.

</details>

---

## Teil 2: Parameter - Werte an Funktionen übergeben

### Was sind Parameter?

Parameter sind Platzhalter für Werte, die du der Funktion beim Aufruf mitgibst. Sie machen Funktionen flexibel.

**Beispiel:**
```python
def begruesse(name):
    print(f"Hallo, {name}!")

begruesse("Anna")   # Hallo, Anna!
begruesse("Ben")    # Hallo, Ben!
```

### Mehrere Parameter

Du kannst mehrere Parameter verwenden, getrennt durch Kommas:

```python
def addiere(a, b):
    ergebnis = a + b
    print(f"{a} + {b} = {ergebnis}")

addiere(5, 3)    # 5 + 3 = 8
addiere(10, 20)  # 10 + 20 = 30
```

---

## Übung 2: Funktionen mit Parametern

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

Erstelle Funktionen, die mit Parametern arbeiten:

1. Eine Funktion `stelle_vor(name, alter)`, die eine Vorstellung ausgibt:
   - Beispiel: "Ich bin Anna und ich bin 25 Jahre alt."
2. Eine Funktion `rechne(zahl1, zahl2)`, die:
   - Die Summe ausgibt
   - Die Differenz ausgibt
   - Das Produkt ausgibt
3. Teste beide Funktionen mit verschiedenen Werten

**Hinweise:**
- Parameter werden in den Klammern definiert
- Beim Aufruf werden konkrete Werte übergeben (Argumente)
- Die Reihenfolge der Argumente muss zur Reihenfolge der Parameter passen

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 2: Funktionen mit Parametern
Musterlösung mit Erklärungen
"""

print("=== Funktionen mit Parametern ===\n")

# Schritt 1: Vorstellungsfunktion
def stelle_vor(name, alter):
    print(f"Ich bin {name} und ich bin {alter} Jahre alt.")

# Schritt 2: Rechenfunktion
def rechne(zahl1, zahl2):
    """Berechnet Summe, Differenz und Produkt zweier Zahlen."""
    return {
        "summe": zahl1 + zahl2,
        "differenz": zahl1 - zahl2,
        "produkt": zahl1 * zahl2
    }

# Schritt 3: Funktionen testen
print("--- Vorstellungen ---")
stelle_vor("Anna", 25)
stelle_vor("Ben", 30)
stelle_vor("Clara", 28)

print("\n--- Berechnungen ---")
ergebnis1 = rechne(10, 5)
print(f"Berechnung mit 10 und 5:")
print(f"  Summe: {ergebnis1['summe']}")
print(f"  Differenz: {ergebnis1['differenz']}")
print(f"  Produkt: {ergebnis1['produkt']}")

print()
ergebnis2 = rechne(20, 3)
print(f"Berechnung mit 20 und 3:")
print(f"  Summe: {ergebnis2['summe']}")
print(f"  Differenz: {ergebnis2['differenz']}")
print(f"  Produkt: {ergebnis2['produkt']}")

print()
ergebnis3 = rechne(100, 25)
print(f"Berechnung mit 100 und 25:")
print(f"  Summe: {ergebnis3['summe']}")
print(f"  Differenz: {ergebnis3['differenz']}")
print(f"  Produkt: {ergebnis3['produkt']}")

"""
Erklärungen:

1. PARAMETER DEFINIEREN:
   def stelle_vor(name, alter):
   - name und alter sind Parameter (Platzhalter)
   - Sie existieren nur innerhalb der Funktion

2. ARGUMENTE ÜBERGEBEN:
   stelle_vor("Anna", 25)
   - "Anna" wird zu name
   - 25 wird zu alter
   - Die Reihenfolge ist wichtig!

3. PARAMETER VERWENDEN:
   - Innerhalb der Funktion kannst du mit den Parametern rechnen
   - Sie verhalten sich wie normale Variablen

4. MEHRERE BERECHNUNGEN:
   - Eine Funktion kann mehrere Operationen durchführen
   - Dictionary als Return-Wert macht Ergebnisse gut zugänglich
   - Zwischenergebnisse in Dictionary speichern macht den Code lesbarer

5. WIEDERVERWENDBARKEIT:
   - Die gleiche Funktion funktioniert mit unterschiedlichen Werten
   - Ergebnisse können weiterverwendet werden
   - Das ist der große Vorteil von Funktionen!

6. RETURN VS. PRINT:
   - rechne() gibt Werte zurück (Dictionary)
   - stelle_vor() gibt direkt aus (für Begrüßungen ok)
   - Bei Berechnungen: Immer return bevorzugen!
"""
```

</details>

---

### Selbstcheck: Teil 2

1. Was passiert, wenn du Argumente in falscher Reihenfolge übergibst?
2. Können Parameter innerhalb der Funktion wie normale Variablen verwendet werden?
3. Ist `stelle_vor(25, "Anna")` dasselbe wie `stelle_vor("Anna", 25)`?

<details>
<summary>Antworten anzeigen</summary>

1. Die Werte werden falsch zugeordnet - das erste Argument geht an den ersten Parameter usw.
2. Ja! Parameter verhalten sich innerhalb der Funktion wie lokale Variablen.
3. Nein! Es erzeugt keinen Laufzeitfehler, aber die Werte sind vertauscht und die Ausgabe ist inhaltlich falsch. Nutze entweder die richtige Reihenfolge oder Keyword-Argumente.

</details>

---

## Teil 3: Return - Werte zurückgeben

### Was macht return?

Mit `return` gibt eine Funktion ein Ergebnis zurück, das du weiter verwenden kannst.

**Ohne return:**
```python
def addiere(a, b):
    print(a + b)

addiere(3, 5)  # Gibt 8 aus, aber du kannst den Wert nicht speichern
```

**Mit return:**
```python
def addiere(a, b):
    return a + b

ergebnis = addiere(3, 5)  # ergebnis = 8
print(ergebnis)           # 8
print(ergebnis * 2)       # 16
```

### Mehrere Werte zurückgeben

Python kann mehrere Werte als Tuple zurückgeben:

```python
def min_max(zahlen):
    return min(zahlen), max(zahlen)

kleinste, groesste = min_max([3, 7, 1, 9, 4])
print(f"Kleinste: {kleinste}, Größte: {groesste}")
# Kleinste: 1, Größte: 9
```

**Wichtig:** `min()` und `max()` funktionieren nur mit nicht-leeren Listen. Bei leeren Listen gibt es einen `ValueError`. Prüfe vorher, ob die Liste Elemente enthält:
```python
if zahlen:  # Prüft ob Liste nicht leer ist
    return min(zahlen), max(zahlen)
```

### Benötigte Methoden für Übung 3

**round() - Runden von Zahlen:**
```python
zahl = 3.7856
gerundet = round(zahl, 2)  # 3.79 (2 Dezimalstellen)
```

**Hinweis für professionelle Geldbeträge:**
Für Einsteiger ist `round()` völlig ausreichend. In professionellen Anwendungen mit Währungen nutzt man häufig das `Decimal`-Modul für präzise Berechnungen. Das kannst du dir später anschauen, wenn du fortgeschrittener bist.

---

## Übung 3: Funktionen mit Return

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

Erstelle ein Programm mit Funktionen, die Werte zurückgeben:

1. Eine Funktion `quadrat(zahl)`, die das Quadrat einer Zahl zurückgibt
2. Eine Funktion `verdopple(zahl)`, die das Doppelte einer Zahl zurückgibt
3. Eine Funktion `berechne_preis(netto, steuersatz)`, die den Bruttopreis berechnet
   - Formel: `brutto = netto * (1 + steuersatz)`
   - Runde auf 2 Dezimalstellen
4. Eine Funktion `teile_mit_rest(dividend, divisor)`, die sowohl das Ergebnis als auch den Rest zurückgibt
   - Nutze `//` für ganzzahlige Division
   - Nutze `%` für den Rest

**Hinweise:**
- Verwende `return`, um Werte zurückzugeben
- Speichere Return-Werte in Variablen
- Bei mehreren Return-Werten nutze Komma-Trennung

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 3: Funktionen mit Return
Musterlösung mit Erklärungen
"""

print("=== Funktionen mit Return ===\n")

# Schritt 1: Quadratfunktion
def quadrat(zahl: int) -> int:
    """Berechnet das Quadrat einer Zahl."""
    return zahl * zahl

# Schritt 2: Verdopplungsfunktion
def verdopple(zahl: int) -> int:
    """Verdoppelt eine Zahl."""
    return zahl * 2

# Schritt 3: Preisberechnung
def berechne_preis(netto: float, steuersatz: float) -> float:
    """Berechnet den Bruttopreis inkl. Steuer."""
    brutto = netto * (1 + steuersatz)
    return round(brutto, 2)

# Schritt 4: Division mit Rest
def teile_mit_rest(dividend: int, divisor: int) -> tuple:
    """Gibt Ergebnis und Rest einer Division zurück."""
    ergebnis = dividend // divisor
    rest = dividend % divisor
    return ergebnis, rest

# Tests
print("--- Quadrat ---")
zahl = 7
ergebnis = quadrat(zahl)
print(f"Quadrat von {zahl}: {ergebnis}")

print("\n--- Verdopplung ---")
wert = 15
doppelt = verdopple(wert)
print(f"{wert} verdoppelt: {doppelt}")

print("\n--- Preisberechnung ---")
netto = 100
steuer = 0.19
brutto = berechne_preis(netto, steuer)
print(f"Nettopreis: {netto} €")
print(f"Steuersatz: {steuer * 100}%")
print(f"Bruttopreis: {brutto} €")

print("\n--- Division mit Rest ---")
dividend = 17
divisor = 5
quotient, rest = teile_mit_rest(dividend, divisor)
print(f"{dividend} : {divisor} = {quotient} Rest {rest}")

# Bonus: Funktionen kombinieren
print("\n--- Funktionen kombinieren ---")
x = 5
x_quadrat = quadrat(x)
x_quadrat_doppelt = verdopple(x_quadrat)
print(f"{x} → Quadrat: {x_quadrat} → Verdoppelt: {x_quadrat_doppelt}")

"""
Erklärungen:

1. RETURN GRUNDLAGEN:
   - return beendet die Funktion
   - Der Wert nach return wird zurückgegeben
   - Ohne return gibt eine Funktion None zurück

2. RETURN-WERT VERWENDEN:
   ergebnis = quadrat(7)
   - Der Return-Wert wird in der Variable gespeichert
   - Jetzt kannst du damit weiterarbeiten

3. MEHRERE RÜCKGABEWERTE:
   return ergebnis, rest
   - Python packt die Werte in ein Tuple
   - Beim Empfang: quotient, rest = teile_mit_rest(17, 5)
   - Das nennt man "Unpacking"

4. ROUND():
   round(brutto, 2)
   - Rundet die Zahl
   - Zweiter Parameter: Anzahl Dezimalstellen
   - round(3.7856, 2) → 3.79

5. OPERATOREN FÜR DIVISION:
   - // : Ganzzahlige Division (ohne Rest)
   - %  : Modulo (nur der Rest)
   - 17 // 5 = 3
   - 17 % 5 = 2

6. FUNKTIONEN KOMBINIEREN:
   - Return-Werte können direkt an andere Funktionen übergeben werden
   - verdopple(quadrat(5)) ist auch möglich
   - Macht Code kompakt, aber nicht zu verschachtelt!
"""
```

</details>

---

## Teil 3.5: Dokumentation - Docstrings und Type Hints

### Docstrings - Was macht die Funktion?

Ein Docstring ist eine Beschreibung, die direkt unter der Funktionsdefinition steht:

```python
def berechne_rabatt(preis, rabatt=10):
    """
    Berechnet den Preis nach Abzug des Rabatts.
    
    Parameter:
        preis: Ursprünglicher Preis
        rabatt: Rabatt in Prozent (Standard: 10)
    
    Rückgabe:
        Preis nach Rabatt, gerundet auf 2 Dezimalstellen
    """
    return round(preis * (1 - rabatt/100), 2)
```

**Warum?**
- Andere (und du selbst später) verstehen sofort, was die Funktion tut
- `help(berechne_rabatt)` zeigt den Docstring an
- Professioneller Code hat immer Docstrings

### Type Hints - Welche Typen erwartet die Funktion?

Type Hints zeigen, welche Datentypen erwartet werden:

```python
def berechne_rabatt(preis: float, rabatt: float = 10.0) -> float:
    """Gibt den Preis nach Rabatt zurück (Standard 10%)."""
    return round(preis * (1 - rabatt/100), 2)
```

- `preis: float` - Parameter soll ein Float sein
- `rabatt: float = 10.0` - Optional mit Default-Wert
- `-> float` - Funktion gibt einen Float zurück

**Wichtig:** Type Hints sind nur Hinweise! Python prüft sie nicht automatisch, aber:
- IDEs können dich warnen bei falschen Typen
- Code wird lesbarer
- Tools wie `mypy` können Fehler finden

**Kombiniert - Best Practice:**
```python
def addiere(a: int, b: int) -> int:
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b
```

### Selbstcheck: Dokumentation

1. Wo steht ein Docstring?
2. Erzwingt Python die Typen in Type Hints?
3. Solltest du Docstrings bei jeder Funktion schreiben?

<details>
<summary>Antworten anzeigen</summary>

1. Direkt unter der `def`-Zeile, in dreifachen Anführungszeichen.
2. Nein! Type Hints sind nur Hinweise für Entwickler und Tools.
3. Bei komplexeren Funktionen: Ja! Bei sehr einfachen (z.B. `def quadrat(x): return x*x`): Optional.

</details>

---

### Selbstcheck: Teil 3

1. Was macht `return` - läuft der Code nach `return` noch weiter?
2. Gibt eine Funktion ohne `return` einen Wert zurück?
3. Wie fängst du mehrere Return-Werte auf?

<details>
<summary>Antworten anzeigen</summary>

1. `return` beendet die Funktion sofort. Code danach wird nicht mehr ausgeführt.
2. Ja - `None`. Das ist Pythons Wert für "nichts".
3. Mit Unpacking: `wert1, wert2 = funktion()` - Python packt die Werte automatisch in ein Tuple.

</details>

---

## Teil 4: Parameter-Varianten

### Positionsparameter

Die Standardform - Argumente werden in der Reihenfolge zugeordnet:

```python
def formatiere_name(vorname, nachname):
    return f"{nachname}, {vorname}"

print(formatiere_name("Anna", "Schmidt"))  # Schmidt, Anna
```

### Keyword-Argumente

Parameter werden beim Aufruf benannt - Reihenfolge egal:

```python
print(formatiere_name(nachname="Müller", vorname="Ben"))  # Müller, Ben
```

### Default-Werte

Parameter mit Standardwerten sind optional:

```python
def begruesse(name, tageszeit="Tag"):
    print(f"Guten {tageszeit}, {name}!")

begruesse("Anna")              # Guten Tag, Anna!
begruesse("Ben", "Morgen")     # Guten Morgen, Ben!
```

**WICHTIG - Häufiger Fehler mit Listen/Dictionaries:**

Verwende NIEMALS veränderbare Datentypen (Listen, Dictionaries) als Default-Werte:

```python
# FALSCH - vermeiden!
def sammle_items(item, liste=[]):
    liste.append(item)
    return liste

print(sammle_items("A"))  # ["A"]
print(sammle_items("B"))  # ["A", "B"] - Überraschung! Die Liste wird geteilt!
```

**Richtig:**
```python
def sammle_items(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste

print(sammle_items("A"))  # ["A"]
print(sammle_items("B"))  # ["B"] - Jetzt korrekt!
```

**Warum?** Default-Werte werden nur einmal beim Definieren erstellt, nicht bei jedem Aufruf.

---

## Übung 4: Parameter-Varianten

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

Erstelle Funktionen mit verschiedenen Parameter-Typen:

1. Eine Funktion `erstelle_profil(name, alter, stadt, beruf)`, die ein Profil formatiert ausgibt:
   - Nutze alle vier Parameter
   - Teste mit Positions- und Keyword-Argumenten
   
2. Eine Funktion `berechne_rabatt(preis, rabatt=10)`, die einen Preis mit Rabatt berechnet:
   - `rabatt` soll einen Default-Wert von 10 (für 10%) haben
   - Formel: `neuer_preis = preis * (1 - rabatt/100)`
   - Gib den neuen Preis gerundet zurück
   
3. Eine Funktion `erstelle_nachricht(text, absender="System", wichtig=False)`, die eine formatierte Nachricht zurückgibt:
   - Wenn `wichtig=True`: "!!! WICHTIG !!!" vor der Nachricht
   - Format: "[Absender]: Nachricht"

**Hinweise:**
- Parameter ohne Default müssen vor Parametern mit Default stehen
- Keyword-Argumente können in beliebiger Reihenfolge übergeben werden
- Default-Werte werden nur verwendet, wenn kein Argument übergeben wird

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 4: Parameter-Varianten
Musterlösung mit Erklärungen
"""

print("=== Parameter-Varianten ===\n")

# Schritt 1: Profil-Funktion
def erstelle_profil(name, alter, stadt, beruf):
    profil = f"""
--- BENUTZERPROFIL ---
Name:   {name}
Alter:  {alter}
Stadt:  {stadt}
Beruf:  {beruf}
----------------------
    """
    print(profil)

# Schritt 2: Rabatt-Funktion
def berechne_rabatt(preis, rabatt=10):
    neuer_preis = preis * (1 - rabatt/100)
    return round(neuer_preis, 2)

# Schritt 3: Nachrichtenfunktion
def erstelle_nachricht(text, absender="System", wichtig=False):
    if wichtig:
        return f"!!! WICHTIG !!! [{absender}]: {text}"
    else:
        return f"[{absender}]: {text}"

# Tests
print("--- Profil mit Positionsargumenten ---")
erstelle_profil("Anna Müller", 28, "Berlin", "Entwicklerin")

print("--- Profil mit Keyword-Argumenten ---")
erstelle_profil(
    beruf="Designer",
    name="Ben Schmidt",
    stadt="Hamburg",
    alter=32
)

print("--- Rabattberechnung ---")
original_preis = 99.99

# Mit Default-Rabatt (10%)
preis_mit_standard = berechne_rabatt(original_preis)
print(f"Originalpreis: {original_preis} €")
print(f"Mit 10% Rabatt: {preis_mit_standard} €")

# Mit eigenem Rabatt
preis_mit_20 = berechne_rabatt(original_preis, 20)
print(f"Mit 20% Rabatt: {preis_mit_20} €")

preis_mit_5 = berechne_rabatt(original_preis, rabatt=5)
print(f"Mit 5% Rabatt: {preis_mit_5} €")

print("\n--- Nachrichten ---")
# Standard
msg1 = erstelle_nachricht("Server läuft normal")
print(msg1)

# Mit eigenem Absender
msg2 = erstelle_nachricht("Backup abgeschlossen", absender="Backup-Service")
print(msg2)

# Wichtige Nachricht
msg3 = erstelle_nachricht("Wartung in 10 Minuten!", absender="Admin", wichtig=True)
print(msg3)

# Nur wichtig setzen (andere Defaults bleiben)
msg4 = erstelle_nachricht("Sicherheitsupdate erforderlich", wichtig=True)
print(msg4)

"""
Erklärungen:

1. POSITIONSARGUMENTE:
   erstelle_profil("Anna", 28, "Berlin", "Entwicklerin")
   - Argumente werden der Reihe nach zugeordnet
   - Schnell, aber weniger lesbar bei vielen Parametern

2. KEYWORD-ARGUMENTE:
   erstelle_profil(beruf="Designer", name="Ben", ...)
   - Parameter werden namentlich angesprochen
   - Reihenfolge ist egal
   - Sehr lesbar und selbsterklärend
   - Ideal bei vielen Parametern

3. DEFAULT-WERTE:
   def berechne_rabatt(preis, rabatt=10):
   - rabatt ist optional, Standard ist 10
   - berechne_rabatt(100) → rabatt wird 10
   - berechne_rabatt(100, 20) → rabatt wird 20

4. REIHENFOLGE BEI DEFAULTS:
   ✓ def funktion(pflicht, optional=10):
   ✗ def funktion(optional=10, pflicht):
   - Parameter ohne Default immer zuerst!

5. KOMBINATION:
   Du kannst alle drei Arten kombinieren:
   - Positionsargumente zuerst
   - Dann Keyword-Argumente
   - Defaults wo sinnvoll

6. BOOLEAN-PARAMETER:
   wichtig=False
   - Ideal für Flags (an/aus)
   - Macht Funktionen flexibler
   - Gut lesbar: wichtig=True
"""
```

</details>

---

### Selbstcheck: Teil 4

1. Können Keyword-Argumente in beliebiger Reihenfolge übergeben werden?
2. Wo müssen Parameter mit Default-Werten stehen - vor oder nach normalen Parametern?
3. Warum sollte man keine Liste als Default-Wert verwenden?

<details>
<summary>Antworten anzeigen</summary>

1. Ja! Bei Keyword-Argumenten ist die Reihenfolge egal: `funktion(b=2, a=1)` funktioniert.
2. Nach den normalen Parametern: `def funktion(normal, default=wert):` ist richtig.
3. Weil der Default-Wert nur einmal erstellt wird und bei jedem Aufruf wiederverwendet wird - Änderungen bleiben erhalten!

</details>

---

## Teil 5: Scope - Gültigkeitsbereich von Variablen

### Was ist Scope?

Scope bestimmt, wo eine Variable "sichtbar" und verwendbar ist.

**Zwei Arten:**
- **Lokal**: Nur innerhalb der Funktion gültig
- **Global**: Überall im Programm gültig

### Lokale Variablen

```python
def berechne():
    x = 10  # Lokale Variable
    print(x)

berechne()  # 10
print(x)    # Fehler! x existiert hier nicht
```

### Globale Variablen lesen

```python
x = 10  # Globale Variable

def zeige():
    print(x)  # Kann globale Variable lesen

zeige()  # 10
```

### Lokale Variable "überdeckt" globale

```python
x = 10  # Global

def teste():
    x = 5  # Lokal - überdeckt die globale
    print(f"Innen: {x}")

teste()        # Innen: 5
print(f"Außen: {x}")  # Außen: 10 (unverändert!)
```

### Häufiger Fehler: UnboundLocalError

Ein typischer Anfängerfehler beim Arbeiten mit Variablen:

```python
zaehler = 0

def erhoehe():
    print(zaehler)      # Fehler! UnboundLocalError
    zaehler = zaehler + 1

erhoehe()
```

**Warum der Fehler?**
Python sieht die Zuweisung `zaehler = ...` und markiert `zaehler` als lokale Variable. Beim Versuch, sie VOR der Zuweisung zu lesen, existiert sie noch nicht.

**Richtige Lösungen:**

```python
# Variante 1: Mit Parameter und Return (EMPFOHLEN!)
zaehler = 0

def erhoehe(z):
    return z + 1

zaehler = erhoehe(zaehler)
```

```python
# Variante 2: Mit global (nur wenn wirklich nötig)
zaehler = 0

def erhoehe():
    global zaehler
    zaehler = zaehler + 1

erhoehe()
```

**Merke:** Variante 1 ist fast immer besser - die Funktion ist unabhängig und testbar!

---

## Übung 5: Scope verstehen

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

Erstelle ein Programm, um Scope zu verstehen:

1. Definiere eine globale Variable `kontostand = 1000`

2. Eine Funktion `zeige_kontostand()`, die den globalen Kontostand ausgibt

3. Eine Funktion `pruefe_betrag(betrag)`, die:
   - Prüft, ob `betrag` kleiner oder gleich dem globalen `kontostand` ist
   - "Betrag verfügbar" oder "Nicht genug Guthaben" zurückgibt
   
4. Eine Funktion `simuliere_abzug(betrag)`, die:
   - Eine LOKALE Variable `neuer_kontostand` berechnet
   - `neuer_kontostand = kontostand - betrag`
   - Den neuen (simulierten) Kontostand ausgibt
   - ABER: Der globale `kontostand` bleibt unverändert!

5. Teste alle Funktionen und beobachte, dass der globale `kontostand` nie verändert wird

**Hinweise:**
- Funktionen können globale Variablen lesen
- Lokale Variablen existieren nur in der Funktion
- Ohne `global`-Keyword wird der globale Wert nicht verändert

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 5: Scope verstehen
Musterlösung mit Erklärungen
"""

print("=== Scope - Gültigkeitsbereich ===\n")

# Globale Variable
kontostand = 1000

# Schritt 1: Kontostand anzeigen
def zeige_kontostand():
    print(f"Aktueller Kontostand: {kontostand} €")

# Schritt 2: Betrag prüfen
def pruefe_betrag(betrag):
    if betrag <= kontostand:
        return "Betrag verfügbar"
    else:
        return "Nicht genug Guthaben"

# Schritt 3: Abzug simulieren (nur lokal!)
def simuliere_abzug(betrag):
    # Lokale Variable - verändert NICHT den globalen Kontostand
    neuer_kontostand = kontostand - betrag
    print(f"Wenn wir {betrag} € abziehen würden:")
    print(f"  Neuer Kontostand wäre: {neuer_kontostand} €")

# Tests
print("--- Anfangszustand ---")
zeige_kontostand()

print("\n--- Verfügbarkeit prüfen ---")
print(f"300 € abheben? {pruefe_betrag(300)}")
print(f"1500 € abheben? {pruefe_betrag(1500)}")

print("\n--- Simulation 1: 300 € abziehen ---")
simuliere_abzug(300)

print("\n--- Kontostand nach Simulation ---")
zeige_kontostand()
print("→ Der globale Kontostand ist UNVERÄNDERT!")

print("\n--- Simulation 2: 700 € abziehen ---")
simuliere_abzug(700)

print("\n--- Kontostand nach Simulation ---")
zeige_kontostand()
print("→ Immer noch unverändert!")

# Zusätzliche Demonstration
print("\n--- Was passiert bei lokaler Variable? ---")

def demonstration():
    # Lokale Variable mit gleichem Namen
    kontostand = 500  # Dies ist NICHT die globale Variable!
    print(f"Lokaler Kontostand in Funktion: {kontostand} €")

demonstration()
print(f"Globaler Kontostand außerhalb: {kontostand} €")
print("→ Die lokale Variable 'überdeckt' nur innerhalb der Funktion!")

"""
Erklärungen:

1. GLOBALE VARIABLEN:
   kontostand = 1000  # Außerhalb aller Funktionen
   - Überall im Programm sichtbar
   - Funktionen können sie lesen

2. LESEN VS. ÄNDERN:
   - Lesen: kein Problem
   - Ändern: benötigt 'global' Keyword (siehe unten)

3. LOKALE VARIABLEN:
   def simuliere_abzug(betrag):
       neuer_kontostand = kontostand - betrag
   - neuer_kontostand existiert nur in der Funktion
   - Nach Funktionsende ist sie "weg"

4. ÜBERDECKUNG (SHADOWING):
   def demonstration():
       kontostand = 500  # Lokale Variable!
   - Gleiches Name wie globale Variable
   - Aber: Unterschiedliche Variablen!
   - Lokal überdeckt global (nur innerhalb der Funktion)

5. WARUM FUNKTIONIERT PRUEFE_BETRAG?
   if betrag <= kontostand:
   - Liest die globale Variable (erlaubt)
   - Verändert sie nicht

6. WARUM BLEIBT GLOBAL UNVERÄNDERT?
   neuer_kontostand = kontostand - betrag
   - Erstellt NEUE lokale Variable
   - Ändert nicht die globale

7. BEST PRACTICE:
   - Globale Variablen möglichst vermeiden
   - Werte lieber als Parameter übergeben
   - Werte mit return zurückgeben
   - Macht Funktionen unabhängig und testbar

8. WENN DU GLOBAL ÄNDERN WILLST (selten nötig):
   def aendere_kontostand(betrag):
       global kontostand  # Explizit global machen
       kontostand -= betrag
   
   ABER: Besser mit return arbeiten!
"""
```

</details>

---

### Selbstcheck: Teil 5

1. Kann eine Funktion eine globale Variable lesen?
2. Was passiert, wenn du in einer Funktion eine Variable mit gleichem Namen wie eine globale Variable erstellst?
3. Warum solltest du `global` vermeiden?

<details>
<summary>Antworten anzeigen</summary>

1. Ja! Funktionen können globale Variablen lesen, ohne etwas Besonderes zu tun.
2. Die lokale Variable "überdeckt" die globale - aber nur innerhalb der Funktion.
3. Es macht Funktionen schwer testbar und code schwer nachvollziehbar. Besser: Parameter + Return verwenden.

</details>

---

## Benötigte Methoden für Übung 6

Bevor wir zur nächsten Übung kommen, hier noch ein paar hilfreiche String-Methoden:

### .strip() - Leerzeichen entfernen

Entfernt Leerzeichen am Anfang und Ende eines Strings:

```python
text = "  Hallo Welt  "
sauber = text.strip()  # "Hallo Welt"
```

### .title() - Jeden Anfangsbuchstaben groß

Macht jeden Wortanfang groß:

```python
text = "anna müller"
titel = text.title()  # "Anna Müller"
```

**Hinweis:** `.title()` macht ALLE Wörter groß, auch Artikel wie "von", "der", "und". Für Überschriften ist das okay. Für natürliche Sätze gibt es `.capitalize()` (nur erster Buchstabe groß):

```python
text = "python ist toll"
text.capitalize()  # "Python ist toll"
text.title()       # "Python Ist Toll"
```

### .replace() - Zeichen ersetzen

Ersetzt Teile eines Strings:

```python
text = "Hallo Welt"
neu = text.replace("Welt", "Python")  # "Hallo Python"
```

### .split() - String in Liste aufteilen

Teilt einen String an Leerzeichen (oder anderem Zeichen) in eine Liste:

```python
text = "Anna Ben Clara"
namen = text.split()  # ["Anna", "Ben", "Clara"]

datum = "01.01.2024"
teile = datum.split(".")  # ["01", "01", "2024"]
```

---

## Übung 6: Text-Verarbeitung mit Funktionen

**Schwierigkeitsgrad: FORTGESCHRITTEN**

**Aufgabe:**

Erstelle ein Text-Verarbeitungsprogramm mit mehreren Funktionen:

1. **bereite_text_vor(text)**
   - Entfernt Leerzeichen am Anfang/Ende (`.strip()`)
   - Macht jeden Wortanfang groß (`.title()`)
   - Gibt den bereinigten Text zurück

2. **zaehle_woerter(text)**
   - Teilt den Text in Wörter auf (`.split()`)
   - Gibt die Anzahl der Wörter zurück

3. **analysiere_text(text)**
   - Nutzt die beiden obigen Funktionen!
   - Gibt einen Dictionary zurück mit:
     - `"original"`: Der Originaltext
     - `"bereinigt"`: Der bereinigte Text
     - `"anzahl_zeichen"`: Anzahl Zeichen im bereinigten Text
     - `"anzahl_woerter"`: Anzahl Wörter
   - Das ist deine "Hauptfunktion", die andere nutzt

4. **erstelle_zusammenfassung(analyse_dict)**
   - Bekommt das Dictionary von `analysiere_text()`
   - Gibt eine schön formatierte Zusammenfassung als String zurück

5. Teste dein Programm mit verschiedenen Texten

**Hinweise:**
- Nutze die vorgestellten String-Methoden
- Funktionen sollten andere Funktionen nutzen (Wiederverwendung!)
- Verwende sprechende Variablennamen
- Denk an die Einrückung

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Übung 6: Text-Verarbeitung mit Funktionen
Musterlösung mit Erklärungen
"""

print("=== Text-Verarbeitungsprogramm ===\n")

# Schritt 1: Text vorbereiten
def bereite_text_vor(text):
    """
    Bereinigt einen Text von Leerzeichen und formatiert ihn.
    """
    bereinigt = text.strip()
    formatiert = bereinigt.title()
    return formatiert

# Schritt 2: Wörter zählen
def zaehle_woerter(text):
    """
    Zählt die Anzahl der Wörter in einem Text.
    """
    woerter = text.split()
    return len(woerter)

# Schritt 3: Text analysieren (nutzt die anderen Funktionen!)
def analysiere_text(text):
    """
    Analysiert einen Text und gibt verschiedene Informationen zurück.
    """
    bereinigt = bereite_text_vor(text)
    
    analyse = {
        "original": text,
        "bereinigt": bereinigt,
        "anzahl_zeichen": len(bereinigt),
        "anzahl_woerter": zaehle_woerter(bereinigt)
    }
    
    return analyse

# Schritt 4: Zusammenfassung erstellen
def erstelle_zusammenfassung(analyse_dict):
    """
    Erstellt eine formatierte Zusammenfassung der Textanalyse.
    """
    zusammenfassung = f"""
--- TEXTANALYSE ---
Original:
  "{analyse_dict['original']}"

Bereinigt:
  "{analyse_dict['bereinigt']}"

Statistik:
  - Zeichen: {analyse_dict['anzahl_zeichen']}
  - Wörter:  {analyse_dict['anzahl_woerter']}
--------------------
    """
    return zusammenfassung

# Tests
print("--- Test 1: Einfacher Text ---")
text1 = "  hallo welt  "
analyse1 = analysiere_text(text1)
zusammenfassung1 = erstelle_zusammenfassung(analyse1)
print(zusammenfassung1)

print("\n--- Test 2: Längerer Text ---")
text2 = "   python ist eine großartige programmiersprache   "
analyse2 = analysiere_text(text2)
zusammenfassung2 = erstelle_zusammenfassung(analyse2)
print(zusammenfassung2)

print("\n--- Test 3: Satz ---")
text3 = " funktionen machen code wiederverwendbar und übersichtlich "
analyse3 = analysiere_text(text3)
zusammenfassung3 = erstelle_zusammenfassung(analyse3)
print(zusammenfassung3)

# Bonus: Mehrere Texte vergleichen
print("\n--- Vergleich ---")
texte = [
    "  kurz  ",
    "  etwas länger als der erste text  ",
    "  dieser text ist der längste von allen drei texten  "
]

for i, text in enumerate(texte, 1):
    analyse = analysiere_text(text)
    print(f"Text {i}: {analyse['anzahl_woerter']} Wörter, {analyse['anzahl_zeichen']} Zeichen")

"""
Erklärungen:

1. FUNKTIONEN KOMBINIEREN:
   def analysiere_text(text):
       bereinigt = bereite_text_vor(text)
       woerter = zaehle_woerter(bereinigt)
   
   - Eine Funktion ruft andere Funktionen auf
   - Das nennt man "Komposition"
   - Jede Funktion hat eine klare Aufgabe
   - Sehr wartbar und testbar!

2. RÜCKGABE VON DICTIONARIES:
   return {
       "original": text,
       "bereinigt": bereinigt,
       ...
   }
   
   - Perfekt um mehrere zusammenhängende Werte zurückzugeben
   - Besser als Tuple, weil benannt
   - Zugriff über Keys: analyse["original"]

3. STRING-METHODEN:
   - .strip(): Entfernt Whitespace (Leerzeichen, Tabs, Zeilenumbrüche)
   - .title(): Macht jeden Wortanfang groß
   - .split(): Teilt String in Liste (Standard: an Leerzeichen)
   - len(): Funktioniert für Strings (Anzahl Zeichen) und Listen (Anzahl Elemente)

4. DOCSTRINGS:
   """
   Bereinigt einen Text von Leerzeichen und formatiert ihn.
   """
   
   - Direkt nach der Funktionsdefinition
   - Erklärt, was die Funktion tut
   - Wird von help() angezeigt
   - Sehr professionell!

5. WIEDERVERWENDBARKEIT:
   - bereite_text_vor() kann überall genutzt werden
   - zaehle_woerter() ist unabhängig
   - analysiere_text() nutzt beide
   - Jede Funktion einzeln testbar

6. ARBEITEN MIT RETURN-VALUES:
   analyse = analysiere_text(text)
   zusammenfassung = erstelle_zusammenfassung(analyse)
   
   - Rückgabewert wird direkt weiterverwendet
   - "Verkettung" von Funktionen
   - Macht Code lesbar wie eine Geschichte

7. ENUMERATE IN SCHLEIFEN:
   for i, text in enumerate(texte, 1):
   
   - Gibt Index (ab 1) und Element zurück
   - Praktisch für nummerierte Ausgaben

8. F-STRINGS IN MEHRZEILIGEN STRINGS:
   f"""
   Text: {variable}
   """
   
   - Kombiniert mehrzeilige Strings mit Variablen
   - Sehr lesbar für formatierte Ausgaben

9. DESIGN-PRINZIP:
   - Kleine Funktionen, die eine Sache gut machen
   - Funktionen, die andere Funktionen nutzen
   - Klare Input → Output Beziehung
   - Das macht Code professionell und wartbar!
"""
```

</details>

---

## Bonus-Übung: Mini-Taschenrechner

**Schwierigkeitsgrad: FORTGESCHRITTEN**

**Hinweis:** Diese Übung ist umfangreicher und kombiniert alles, was du gelernt hast. Perfekt, wenn du dich sicher fühlst und ein kleines Projekt umsetzen möchtest!

### Aufgabe

Erstelle einen **Taschenrechner** mit verschiedenen Funktionen:

1. **addiere(a, b)** - gibt Summe zurück
2. **subtrahiere(a, b)** - gibt Differenz zurück
3. **multipliziere(a, b)** - gibt Produkt zurück
4. **dividiere(a, b)** - gibt Ergebnis zurück, mit Fehlerbehandlung wenn durch 0 geteilt wird
5. **berechne(operation, a, b)** - Hauptfunktion, die je nach Operation die richtige Funktion aufruft
   - Operation kann sein: "plus", "minus", "mal", "geteilt"
   - Ruft die entsprechende Funktion auf
   - Gibt das formatierte Ergebnis zurück
6. **teste_rechner()** - Testet alle Funktionen mit verschiedenen Werten

<details>
<summary>Musterlösung anzeigen</summary>

```python
"""
Bonus-Übung: Mini-Taschenrechner
Musterlösung mit Erklärungen
"""

print("=== TASCHENRECHNER ===\n")

# Grundrechenarten
def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def subtrahiere(a, b):
    """Subtrahiert b von a."""
    return a - b

def multipliziere(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def dividiere(a, b):
    """
    Dividiert a durch b.
    Gibt None zurück, wenn durch 0 geteilt wird.
    """
    if b == 0:
        return None  # Fehlerfall
    return a / b

# Hauptfunktion
def berechne(operation, a, b):
    """
    Führt eine Berechnung durch.
    
    Parameter:
        operation (str): "plus", "minus", "mal", oder "geteilt"
        a (float): Erste Zahl
        b (float): Zweite Zahl
    
    Rückgabe:
        str: Formatiertes Ergebnis oder Fehlermeldung
    """
    # Operation in Kleinbuchstaben für Vergleich
    op = operation.lower()
    
    if op == "plus":
        ergebnis = addiere(a, b)
        operator = "+"
    elif op == "minus":
        ergebnis = subtrahiere(a, b)
        operator = "-"
    elif op == "mal":
        ergebnis = multipliziere(a, b)
        operator = "×"
    elif op == "geteilt":
        ergebnis = dividiere(a, b)
        if ergebnis is None:
            return f"Fehler: Division durch 0 nicht möglich!"
        operator = "÷"
    else:
        return f"Fehler: Unbekannte Operation '{operation}'"
    
    # Formatierte Rückgabe
    return f"{a} {operator} {b} = {ergebnis}"

# Testfunktion
def teste_rechner():
    """Testet alle Funktionen des Rechners."""
    
    print("--- Grundrechenarten Test ---")
    print(berechne("plus", 10, 5))
    print(berechne("minus", 10, 5))
    print(berechne("mal", 10, 5))
    print(berechne("geteilt", 10, 5))
    
    print("\n--- Fehlerbehandlung ---")
    print(berechne("geteilt", 10, 0))
    print(berechne("wurzel", 10, 5))
    
    print("\n--- Mit Dezimalzahlen ---")
    print(berechne("plus", 3.5, 2.7))
    print(berechne("mal", 2.5, 4.0))
    
    print("\n--- Negative Zahlen ---")
    print(berechne("minus", 5, 10))
    print(berechne("mal", -3, 4))

# Programm ausführen
teste_rechner()

# Interaktiver Teil (optional)
print("\n" + "="*50)
print("Eigene Berechnungen:")
print("="*50)

# Hier könnten zusätzliche Berechnungen folgen
print(berechne("plus", 100, 50))
print(berechne("geteilt", 100, 4))

"""
Erklärungen:

1. MODULARITÄT:
   - Jede Rechenart ist eine eigene Funktion
   - Leicht zu testen
   - Leicht zu erweitern (neue Operationen hinzufügen)

2. FEHLERBEHANDLUNG:
   if b == 0:
       return None
   
   - Gibt None zurück bei Fehler
   - berechne() prüft auf None
   - Gibt aussagekräftige Fehlermeldung

3. ZENTRALE STEUERUNG:
   Die berechne() Funktion:
   - Nimmt Operation als String
   - Entscheidet, welche Funktion aufgerufen wird
   - Formatiert das Ergebnis einheitlich

4. STRING-VERGLEICH:
   op = operation.lower()
   
   - Macht Operation klein für Vergleich
   - Nutzer kann "Plus", "PLUS", oder "plus" eingeben

5. BEDINGTE LOGIK:
   if op == "plus":
       ...
   elif op == "minus":
       ...
   else:
       ...
   
   - Verschiedene Pfade je nach Input
   - else-Block fängt ungültige Operationen ab

6. TESTFUNKTION:
   def teste_rechner():
   
   - Sammelt alle Tests an einem Ort
   - Kann einfach ausgeführt werden
   - Dokumentiert gleichzeitig die Funktionalität

7. DOCSTRINGS:
   """
   Führt eine Berechnung durch.
   
   Parameter:
       ...
   Rückgabe:
       ...
   """
   
   - Professionelle Dokumentation
   - Erklärt Parameter und Rückgabewerte
   - help(berechne) zeigt dies an

8. ERWEITERBARKEIT:
   Um neue Operation hinzuzufügen:
   - Neue Funktion definieren (z.B. def potenziere(a, b))
   - In berechne() neuen elif-Zweig hinzufügen
   - Fertig!

9. RETURN VS. PRINT:
   - Funktionen geben Werte zurück (return)
   - Nur teste_rechner() macht print
   - Trennung von Berechnung und Ausgabe
   - Sehr flexibel!

10. PROJEKTSTRUKTUR:
    - Basis-Funktionen (addiere, etc.)
    - Haupt-Funktion (berechne)
    - Test-Funktion (teste_rechner)
    - Klare Hierarchie
    
    Das ist gutes Software-Design!
"""
```

</details>

---

## Zusammenfassung

### Funktionen - Das Wichtigste

**Definition:**
```python
def funktionsname(parameter):
    # Code
    return ergebnis
```

**Parameter:**
- **Positional**: `funktion(wert1, wert2)`
- **Keyword**: `funktion(name=wert1, alter=wert2)`
- **Default**: `def funktion(param=standardwert):`

**Return:**
- Gibt Wert(e) zurück
- Beendet die Funktion
- Mehrere Werte: `return wert1, wert2`

**Scope:**
- **Lokal**: Variable nur in Funktion gültig
- **Global**: Variable überall gültig
- Lokale überdeckt globale (innerhalb Funktion)

### Best Practices

1. **Eine Funktion = Eine Aufgabe**
   - Funktionen sollten fokussiert sein
   - Lieber mehrere kleine als eine große Funktion

2. **Sprechende Namen**
   - `berechne_rabatt()` statt `br()`
   - Beschreibt, was die Funktion tut
   - **WICHTIG:** Verwende keine Built-in-Namen wie `list`, `dict`, `sum`, `min`, `max` als Variablen- oder Funktionsnamen - sie überschreiben wichtige Python-Funktionen!

3. **Parameter statt globale Variablen**
   - Macht Funktionen unabhängig
   - Leichter testbar

4. **Return statt Print**
   - Funktionen sollten Werte zurückgeben
   - Print nur zur Ausgabe am Ende

5. **Dokumentation**
   - Docstrings für komplexere Funktionen
   - Erklärt, was (nicht wie) die Funktion tut

### Wann Funktionen verwenden?

**Ja, wenn:**
- Code mehrmals verwendet wird
- Logischer Block zusammengehört
- Code übersichtlicher wird
- Funktionalität testbar sein soll

**Nicht nötig, wenn:**
- Code nur einmal vorkommt
- Nur 1-2 Zeilen
- Keine klare Aufgabe

### Typische Fehler vermeiden

1. **Funktion nicht aufrufen:**
   ```python
   def gruss():
       print("Hallo")
   
   gruss  # Falsch - Funktion wird nicht ausgeführt
   gruss()  # Richtig
   ```

2. **Return vergessen:**
   ```python
   def addiere(a, b):
       a + b  # Kein return - gibt None zurück
   
   def addiere(a, b):
       return a + b  # Richtig
   ```

3. **Falsche Parameterreihenfolge:**
   ```python
   def teile(dividend, divisor):
       return dividend / divisor
   
   teile(5, 10)  # Ergibt 0.5 (wahrscheinlich nicht gewollt)
   teile(10, 5)  # Ergibt 2
   ```

4. **Globale Variable ändern wollen:**
   ```python
   x = 10
   
   def aendere():
       x = 5  # Erstellt lokale Variable
       
   def aendere():
       global x  # Wenn wirklich nötig
       x = 5
       
   # ABER: Besser mit return arbeiten!
   def berechne_neu(x):
       return x - 5
   x = berechne_neu(x)  # Am besten
   ```


---

## Tipps für die Praxis

1. **Klein anfangen**: Beginne mit einfachen Funktionen
2. **Testen**: Probiere Funktionen mit verschiedenen Werten aus
3. **Refactoring**: Wenn Code wiederholt wird, mache eine Funktion daraus
4. **Lesen**: Schaue dir Code von anderen an
5. **Üben**: Je mehr Funktionen du schreibst, desto besser wirst du

