# Objektorientierte Programmierung (OOP) in Python - Grundlagen

## Übersicht

In dieser Übung lernst du:
- **Klassen verstehen** - Was ist eine Klasse und wofür braucht man sie
- **Objekte erstellen** - Instanzen einer Klasse erzeugen
- **Attribute nutzen** - Daten in Objekten speichern
- **Methoden schreiben** - Funktionen, die zu Objekten gehören
- **self verstehen** - Die Brücke zwischen Klasse und Objekt

---

## Übersicht nach Schwierigkeitsgrad

### GRUNDLAGEN

Diese Übungen decken die fundamentalen OOP-Konzepte ab:

- **Übung 1**: Erste Klasse erstellen - Person mit Name
- **Übung 2**: Konstruktor (__init__) verstehen und nutzen
- **Übung 3**: Attribute lesen und ändern
- **Übung 4**: Erste Methode hinzufügen
- **Übung 5**: Mehrere Objekte erstellen und vergleichen

**Empfehlung:** Mache alle Grundlagen-Übungen in Reihenfolge. OOP lernt man am besten durch praktisches Üben!

### FORTGESCHRITTEN

Diese Übungen kombinieren alle Konzepte:

- **Übung 6**: Klassenattribute vs. Instanzattribute
- **Bonus-Übung**: Einfaches Bankkonto-System mit mehreren Klassen

**Empfehlung:** Diese Übungen setzen voraus, dass du die Grundlagen verstanden hast.

---

## Was ist objektorientierte Programmierung?

### Die Grundidee

Stell dir vor, du schreibst ein Programm für eine Schule. Du hast viele Schüler mit Namen, Alter, Noten. **Wie organisierst du diese Daten sinnvoll?**

**Ohne OOP:**
```python
schueler1_name = "Anna"
schueler1_alter = 16
schueler1_note = 2.0

schueler2_name = "Ben"
schueler2_alter = 15
schueler2_note = 1.5

schueler3_name = "Clara"
schueler3_alter = 16
schueler3_note = 2.3
```

**Problem:** Viele einzelne Variablen, unübersichtlich, fehleranfällig!

**Mit OOP:**
```python
class Schueler:
    def __init__(self, name, alter, note):
        self.name = name
        self.alter = alter
        self.note = note

anna = Schueler("Anna", 16, 2.0)
ben = Schueler("Ben", 15, 1.5)
clara = Schueler("Clara", 16, 2.3)
```

**Vorteil:** Alles gehört zusammen, übersichtlich, leicht erweiterbar!

### Warum OOP lernen?

1. **Ordnung**: Daten und Funktionen gehören zusammen
2. **Wiederverwendbar**: Einmal schreiben, oft nutzen
3. **Verständlich**: Code wird wie die echte Welt strukturiert
4. **Professionell**: Standard in der Software-Entwicklung
5. **Wartbar**: Änderungen sind einfacher

### Die wichtigsten Begriffe

- **Klasse**: Der Bauplan (wie ein Keks-Ausstecher)
- **Objekt/Instanz**: Das fertige Produkt (der Keks)
- **Attribut**: Eigenschaften (Name, Alter, Farbe...)
- **Methode**: Aktionen (gehen, sprechen, rechnen...)
- **self**: "Ich selbst" - Referenz auf das aktuelle Objekt

**Analogie:**
```
Klasse "Auto":      Bauplan mit 4 Rädern, Motor, Farbe
Objekt "mein_auto": Ein konkretes rotes Auto
Attribut "farbe":   Rot
Methode "fahren()": Das Auto fährt los
```

---

## Teil 1: Die erste Klasse

### Klasse definieren

Eine Klasse ist wie eine Schablone. Sie beschreibt, was alle Objekte dieser Art haben.

**Syntax:**
```python
class KlassenName:
    # Hier kommt der Code
    pass
```

**Regeln:**
- Name beginnt mit Großbuchstaben (PascalCase)
- Keyword `class`
- Doppelpunkt am Ende
- Code ist eingerückt

**Naming Conventions (wichtig!):**
- **Klassennamen:** PascalCase (z.B. `Person`, `Bankkonto`, `AutoVerwaltung`)
- **Methoden & Attribute:** snake_case (z.B. `hatte_geburtstag`, `konto_stand`)
- **Keine Umlaute in Code:** Schreibe `schueler` statt `schüler`, `konto_stand` statt `kontoständ`
  
  **Warum keine Umlaute?**
  - Kompatibilität mit allen Systemen
  - Internationaler Standard
  - Vermeidet Encoding-Probleme
  - Im Text dürfen Umlaute sein, nur nicht in Bezeichnern!

**Beispiel:**
```python
class Person:
    pass  # pass = "noch nichts hier"
```

### Objekt erstellen

Ein Objekt ist eine konkrete Instanz der Klasse.

**Syntax:**
```python
objekt_name = KlassenName()
```

**Beispiel:**
```python
class Person:
    pass

anna = Person()  # anna ist jetzt ein Person-Objekt
print(type(anna))  # <class '__main__.Person'>
```

---

## Übung 1: Erste Klasse erstellen

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~10-15 Minuten**

**Aufgabe:**

1. **Erstelle eine Python-Datei**
   - Erstelle eine Datei `person.py`
   - Öffne sie in deinem Editor (VS Code, PyCharm, etc.)

2. **Schreibe deine erste Klasse**
   ```python
   class Person:
       pass
   ```

3. **Erstelle ein Objekt**
   ```python
   anna = Person()
   print(anna)
   print(type(anna))
   ```

4. **Führe das Programm aus**
   - Im Terminal: `python person.py`
   - Beobachte die Ausgabe

5. **Erstelle mehrere Objekte**
   ```python
   ben = Person()
   clara = Person()
   
   print(anna)
   print(ben)
   print(clara)
   ```

**Hinweise:**
- Jedes Objekt ist einzigartig (andere Speicheradresse)
- `type()` zeigt, dass es ein Person-Objekt ist
- Die Ausgabe sieht kryptisch aus - das ist normal!

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Klasse definieren =====

class Person:
    pass  # Noch keine Eigenschaften oder Methoden


# ===== SCHRITT 2: Erstes Objekt erstellen =====

anna = Person()
print(anna)
# Ausgabe: <__main__.Person object at 0x7f8b3c4d5e10>
# Das ist die Speicheradresse - jedes Objekt ist einzigartig!

print(type(anna))
# Ausgabe: <class '__main__.Person'>
# Zeigt: anna ist vom Typ Person


# ===== SCHRITT 3: Mehrere Objekte erstellen =====

ben = Person()
clara = Person()

print("Anna:", anna)
print("Ben:", ben)
print("Clara:", clara)

# Jedes hat eine andere Adresse!
# Anna: <__main__.Person object at 0x7f1234...>
# Ben: <__main__.Person object at 0x7f5678...>
# Clara: <__main__.Person object at 0x7f9abc...>


# ===== SCHRITT 4: Objekte vergleichen =====

print(anna == ben)  # False - verschiedene Objekte
print(anna is ben)  # False - verschiedene Objekte

anna2 = anna  # anna2 zeigt auf das GLEICHE Objekt wie anna
print(anna is anna2)  # True - das GLEICHE Objekt


# ===== SCHRITT 5: Teste dein Verständnis =====

# Erstelle eine eigene Klasse "Auto"
class Auto:
    pass

mein_auto = Auto()
dein_auto = Auto()

print(type(mein_auto))  # <class '__main__.Auto'>
print(mein_auto == dein_auto)  # False
```

**Erklärungen:**

```
1. CLASS:
   - Keyword zum Definieren einer Klasse
   - Name sollte mit Großbuchstaben beginnen (PascalCase)
   - Person, Auto, Bankkonto (nicht: person, auto)
   
2. PASS:
   - Platzhalter für "hier kommt noch Code"
   - Python braucht mindestens eine Zeile im Block
   - Können wir später durch echten Code ersetzen

3. OBJEKT ERSTELLEN:
   anna = Person()
   - Person() ruft die Klasse auf
   - Erstellt ein neues Objekt
   - anna ist eine Variable, die auf das Objekt zeigt

4. SPEICHERADRESSE:
   <__main__.Person object at 0x7f1234...>
   - 0x7f1234... ist die Speicheradresse im RAM
   - Jedes Objekt hat eine eindeutige Adresse
   - Wie eine Hausnummer im Computer-Speicher

5. TYPE():
   - Zeigt den Datentyp an
   - Bei int: <class 'int'>
   - Bei str: <class 'str'>
   - Bei Person: <class '__main__.Person'>
   
6. __MAIN__:
   - Zeigt, dass die Klasse in diesem Skript definiert ist
   - Nicht in einem importierten Modul
   - Technisches Detail, erstmal ignorieren

7. MEHRERE OBJEKTE:
   - Jeder Aufruf Person() erstellt ein NEUES Objekt
   - anna, ben, clara sind VERSCHIEDENE Objekte
   - Gleiche Klasse, aber verschiedene Instanzen

8. == VS IS:
   is prüft auf gleiches Objekt (gleiche Speicheradresse)
   == prüft auf gleichen Wert/Inhalt (bei Listen, Strings, etc.)
   
   **WICHTIG bei eigenen Klassen:**
   Ohne __eq__-Methode verhält sich == wie is!
   
   x = 5
   y = 5
   x == y  # True - gleicher Wert
   x is y  # True bei kleinen Zahlen (Python-Optimierung)
   
   anna = Person()
   ben = Person()
   anna == ben  # False - verschiedene Objekte (== verhält sich wie is!)
   anna is ben  # False - verschiedene Objekte
   
   Hinweis: Für inhaltlichen Vergleich müsste man __eq__ implementieren.
   Das lernen wir später!

9. REFERENZ KOPIEREN:
   anna2 = anna
   - Erstellt KEIN neues Objekt!
   - anna2 zeigt auf das GLEICHE Objekt wie anna
   - Änderungen über anna2 betreffen auch anna
```

**Was wir gelernt haben:**

```
(OK) Eine Klasse ist ein Bauplan
(OK) Ein Objekt ist eine Instanz der Klasse
(OK) Jedes Objekt ist einzigartig (eigene Speicheradresse)
(OK) Mit Person() erstellen wir ein neues Objekt
(OK) Mehrere Objekte einer Klasse sind möglich
(OK) class-Keyword und PascalCase für Klassennamen
```

</details>

---

### Selbstcheck: Teil 1

1. Was ist der Unterschied zwischen einer Klasse und einem Objekt?
2. Warum kann ich mehrere Objekte von einer Klasse erstellen?
3. Was bedeutet die Speicheradresse in der Ausgabe?

<details>
<summary>Antworten anzeigen</summary>

1. **Klasse = Bauplan** (Rezept), **Objekt = fertiges Produkt** (der Kuchen). Aus einer Klasse kann man viele Objekte erstellen.
2. Eine Klasse ist nur die Vorlage - wie ein Keks-Ausstecher. Damit kann man beliebig viele Kekse (Objekte) machen.
3. Die Speicheradresse zeigt, wo im Computer-RAM das Objekt gespeichert ist. Jedes Objekt hat eine eindeutige Adresse.

</details>

---

## Einschub (optional): Lesbare Ausgaben mit __str__

Hast du bemerkt, dass `print(anna)` so kryptische Ausgaben produziert?

```python
<__main__.Person object at 0x7f8b3c4d5e10>
```

Das ist nicht sehr hilfreich! Mit der **Special Method** `__str__` können wir das ändern:

```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def __str__(self):
        return f"{self.name} ({self.alter} Jahre)"

# Jetzt wird die Ausgabe lesbar:
anna = Person("Anna", 16)
print(anna)  # Anna (16 Jahre)

ben = Person("Ben", 15)
print(ben)   # Ben (15 Jahre)
```

**Was passiert?**
- `__str__` ist eine spezielle Methode (Special Method)
- Wird automatisch von `print()` aufgerufen
- Muss einen String zurückgeben
- Macht Debugging und Tests viel einfacher!

**Hinweis:** Wir werden `__str__` und andere Special Methods später genauer lernen. Fürs Erste reicht es zu wissen: `__str__` macht `print()` lesbar!

<details>
<summary>Beispiel mit __str__ in allen bisherigen Klassen</summary>

```python
# Alle unsere bisherigen Klassen können __str__ nutzen

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def __str__(self):
        return f"Person: {self.name}, {self.alter} Jahre"

class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
    
    def __str__(self):
        return f"{self.farbe}er {self.marke}"

# Viel besser lesbar!
anna = Person("Anna", 16)
mein_auto = Auto("VW", "Rot")

print(anna)      # Person: Anna, 16 Jahre
print(mein_auto) # Roter VW

# Auch in Listen hilfreich
personen = [Person("Anna", 16), Person("Ben", 15)]
for person in personen:
    print(person)
# Person: Anna, 16 Jahre
# Person: Ben, 15 Jahre
```

</details>

**Ab jetzt:** In den folgenden Übungen kannst du gerne `__str__` in deine Klassen einbauen - es macht alles übersichtlicher!

---

## Teil 2: Der Konstruktor (__init__)

### Was ist __init__?

`__init__` ist eine **spezielle Methode**, die automatisch aufgerufen wird, wenn ein Objekt erstellt wird.

**Zweck:**
- Setzt die Startwerte eines Objekts
- Initialisiert Attribute
- Heißt "Konstruktor" oder "Initialisierer"

**Syntax:**
```python
class Person:
    def __init__(self):
        # Code hier wird beim Erstellen ausgeführt
        pass
```

**Wichtig:**
- Immer zwei Unterstriche vor und nach `init`
- Erster Parameter ist immer `self`
- Wird automatisch aufgerufen bei `Person()`

### self - Was ist das?

`self` ist eine Referenz auf das **aktuelle Objekt**.

**Regeln:**
- Erster Parameter in jeder Instanzmethode
- Python setzt es automatisch
- Wir müssen es beim Aufruf NICHT angeben

**Beispiel:**
```python
class Person:
    def __init__(self):
        print("Ein neues Person-Objekt wurde erstellt!")

anna = Person()  
# Ausgabe: Ein neues Person-Objekt wurde erstellt!
```

### Attribute setzen

Attribute sind Eigenschaften eines Objekts.

**Syntax:**
```python
self.attributname = wert
```

**Beispiel:**
```python
class Person:
    def __init__(self):
        self.name = "Anna"
        self.alter = 16

anna = Person()
print(anna.name)   # Anna
print(anna.alter)  # 16
```

---

## Übung 2: Konstruktor und Attribute

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~15-20 Minuten**

**Aufgabe:**

1. **Erstelle Person-Klasse mit __init__ ohne Parameter**
   ```python
   class Person:
       def __init__(self):
           self.name = "Unbekannt"
           self.alter = 0
   ```

2. **Erstelle Objekt und greife auf Attribute zu**
   ```python
   anna = Person()
   print(anna.name)
   print(anna.alter)
   ```

3. **Erweitere __init__ mit Parametern**
   ```python
   class Person:
       def __init__(self, name, alter):
           self.name = name
           self.alter = alter
   ```

4. **Erstelle Objekte mit verschiedenen Werten**
   ```python
   anna = Person("Anna", 16)
   ben = Person("Ben", 15)
   
   print(anna.name, anna.alter)
   print(ben.name, ben.alter)
   ```

5. **Teste: Was passiert ohne Parameter?**
   ```python
   person = Person()  # Was passiert hier?
   ```

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Einfacher __init__ ohne Parameter =====

class Person:
    def __init__(self):
        self.name = "Unbekannt"
        self.alter = 0
        print("Person erstellt!")

anna = Person()
# Ausgabe: Person erstellt!

print(anna.name)   # Unbekannt
print(anna.alter)  # 0


# ===== SCHRITT 2: __init__ mit Parametern =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        print(f"{name} wurde erstellt!")

anna = Person("Anna", 16)
# Ausgabe: Anna wurde erstellt!

print(anna.name)   # Anna
print(anna.alter)  # 16


# ===== SCHRITT 3: Mehrere Objekte mit verschiedenen Werten =====

ben = Person("Ben", 15)
clara = Person("Clara", 17)

print(f"{anna.name} ist {anna.alter} Jahre alt")
print(f"{ben.name} ist {ben.alter} Jahre alt")
print(f"{clara.name} ist {clara.alter} Jahre alt")

# Ausgabe:
# Anna ist 16 Jahre alt
# Ben ist 15 Jahre alt
# Clara ist 17 Jahre alt


# ===== SCHRITT 4: Was passiert ohne Parameter? =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# person = Person()  # FEHLER!
# TypeError: __init__() missing 2 required positional arguments

# Richtig:
person = Person("Max", 20)


# ===== SCHRITT 5: Default-Parameter =====

class Person:
    def __init__(self, name="Unbekannt", alter=0):
        self.name = name
        self.alter = alter

# Jetzt funktioniert beides:
p1 = Person()                    # Nutzt Defaults
p2 = Person("Lisa", 25)         # Überschreibt Defaults
p3 = Person("Tom")              # Nur Name, alter=0
p4 = Person(alter=30)           # Nur alter, name="Unbekannt"

print(p1.name, p1.alter)  # Unbekannt 0
print(p2.name, p2.alter)  # Lisa 25
print(p3.name, p3.alter)  # Tom 0
print(p4.name, p4.alter)  # Unbekannt 30


# ===== SCHRITT 6: Benannte Argumente (Keyword Arguments) =====

class Person:
    def __init__(self, name, alter, stadt):
        self.name = name
        self.alter = alter
        self.stadt = stadt

# Verschiedene Aufruf-Möglichkeiten:

# 1. Positional (Reihenfolge wichtig!)
p1 = Person("Anna", 16, "Berlin")

# 2. Benannt (Reihenfolge egal!)
p2 = Person(name="Ben", alter=15, stadt="Hamburg")
p3 = Person(alter=17, stadt="München", name="Clara")  # Andere Reihenfolge!

# 3. Gemischt (erst positional, dann benannt)
p4 = Person("David", alter=18, stadt="Köln")

# 4. Vorteil: Lesbarkeit und weniger Fehler
p5 = Person(
    name="Emma",
    alter=16,
    stadt="Frankfurt"
)

print(p1.name, p1.stadt)  # Anna Berlin
print(p2.name, p2.stadt)  # Ben Hamburg
print(p3.name, p3.stadt)  # Clara München

# FEHLER: FEHLER: Benannte vor positionalen
# p_falsch = Person(name="Felix", 19, "Dresden")  # SyntaxError!

# (OK) RICHTIG: Erst positional, dann benannt
p_richtig = Person("Felix", 19, stadt="Dresden")


# ===== SCHRITT 7: self verstehen =====

class Person:
    def __init__(self, name, alter):
        # self ist die Referenz auf das AKTUELLE Objekt
        self.name = name      # name des AKTUELLEN Objekts
        self.alter = alter    # alter des AKTUELLEN Objekts
        print(f"self ist: {self}")

anna = Person("Anna", 16)
# Ausgabe: self ist: <__main__.Person object at 0x...>

ben = Person("Ben", 15)
# Ausgabe: self ist: <__main__.Person object at 0x...>
# Andere Adresse! Anderes Objekt!


# ===== SCHRITT 7: Parameter vs. Attribut =====

class Person:
    def __init__(self, name, alter):
        # name (ohne self.) ist der Parameter
        # self.name ist das Attribut
        self.name = name      # Attribut = Parameter
        self.alter = alter
        
        # Wichtig: Parametername und Attributname 
        # MÜSSEN NICHT gleich sein!

class Person2:
    def __init__(self, vorname, jahre):
        self.name = vorname    # Attribut heißt anders als Parameter
        self.alter = jahre

p = Person2("Anna", 16)
print(p.name)   # Anna
print(p.alter)  # 16
```

**Erklärungen:**

```
1. __INIT__:
   - Zwei Unterstriche vor und nach init
   - "Dunder init" (double underscore)
   - Konstruktor oder Initialisierer
   - Wird AUTOMATISCH aufgerufen bei Person()

2. SELF:
   - Referenz auf das aktuelle Objekt
   - Muss immer erster Parameter sein
   - Python setzt es automatisch
   - Beim Aufruf NICHT angeben!
   
   anna = Person("Anna", 16)
   # Python macht intern:
   # Person.__init__(anna, "Anna", 16)
   # anna wird zu self!

3. SELF.NAME:
   - self.name ist ein Attribut des Objekts
   - Gehört zum Objekt, nicht zur Klasse
   - Jedes Objekt hat eigene Attribute
   - Zugriff von außen: anna.name

4. PARAMETER:
   - name und alter sind Parameter
   - Nur innerhalb von __init__ verfügbar
   - Werden genutzt, um Attribute zu setzen

5. SELF.NAME = NAME:
   - Links: Attribut des Objekts (self.name)
   - Rechts: Parameter der Methode (name)
   - Können unterschiedlich heißen!
   
   self.vorname = name  # Auch möglich!

6. DEFAULT-PARAMETER:
   def __init__(self, name="Unbekannt", alter=0):
   - Falls kein Wert übergeben, wird Default genutzt
   - Macht Parameter optional
   - Person() funktioniert dann auch ohne Argumente

6a. BENANNTE ARGUMENTE (KEYWORD ARGUMENTS):
   Person(name="Anna", alter=16, stadt="Berlin")
   
   - Reihenfolge egal bei benannten Argumenten
   - Erhöht Lesbarkeit
   - Vermeidet Positionsfehler
   - Erst positional, dann benannt
   
   (OK) Person("Anna", alter=16, stadt="Berlin")  # OK
   (FALSCH) Person(name="Anna", 16, "Berlin")          # FEHLER!
   
   Vorteil: Selbstdokumentierend
   Person(name="Max", alter=30)  # Klar, was was ist

7. WARUM FEHLER BEI FEHLENDEN PARAMETERN:
   Person()  # Fehler, wenn __init__ Parameter erwartet
   - Python weiß nicht, welche Werte es nehmen soll
   - Entweder Default-Werte angeben
   - Oder immer Argumente übergeben

8. PRINT IN __INIT__:
   - Hilfreich zum Debuggen
   - Zeigt, wann Objekt erstellt wird
   - In echtem Code meist weglassen

9. F-STRING:
   f"{name} ist {alter} Jahre alt"
   - Formatierter String
   - Variablen in geschweiften Klammern
   - Wird seit Python 3.6 empfohlen
```

**Was wir gelernt haben:**

```
(OK) __init__ wird automatisch beim Erstellen aufgerufen
(OK) self referenziert das aktuelle Objekt
(OK) self.attribut speichert Daten im Objekt
(OK) Parameter von __init__ initialisieren Attribute
(OK) Default-Parameter machen Argumente optional
(OK) Jedes Objekt hat eigene Attribut-Werte
```

**Typische Fehler:**

```
FEHLER: FEHLER: self vergessen
   class Person:
       def __init__(name, alter):  # FALSCH!
           self.name = name        # self nicht definiert!
   
   Richtig:
       def __init__(self, name, alter):

FEHLER: FEHLER: self. vergessen beim Attribut
   class Person:
       def __init__(self, name):
           name = name  # FALSCH! Lokale Variable, kein Attribut
   
   Richtig:
       self.name = name

FEHLER: FEHLER: self beim Aufruf angeben
   anna = Person(self, "Anna", 16)  # FALSCH!
   
   Richtig:
   anna = Person("Anna", 16)

FEHLER: FEHLER: __init ohne Unterstriche
   class Person:
       def init(self, name):  # FALSCH! Wird nicht automatisch aufgerufen
   
   Richtig:
       def __init__(self, name):
```

</details>

---

### Selbstcheck: Teil 2

1. Wann wird `__init__` aufgerufen?
2. Was ist der Unterschied zwischen `name` und `self.name`?
3. Warum muss `self` der erste Parameter sein?

<details>
<summary>Antworten anzeigen</summary>

1. `__init__` wird **automatisch** aufgerufen, wenn ein Objekt erstellt wird: `anna = Person("Anna", 16)`
2. `name` ist ein Parameter (nur in der Methode verfügbar), `self.name` ist ein Attribut (gehört zum Objekt, von außen zugreifbar)
3. Python braucht eine Referenz auf das Objekt. `self` ist diese Referenz und wird von Python automatisch gesetzt.

</details>

---

## Teil 3: Attribute lesen und ändern

### Auf Attribute zugreifen

Attribute können von außen gelesen und geändert werden.

**Syntax:**
```python
objekt.attribut        # Lesen
objekt.attribut = wert # Schreiben
```

**Beispiel:**
```python
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

anna = Person("Anna", 16)

# Lesen
print(anna.name)   # Anna
print(anna.alter)  # 16

# Ändern
anna.alter = 17
print(anna.alter)  # 17
```

### Neue Attribute hinzufügen

Python erlaubt das Hinzufügen neuer Attribute zur Laufzeit.

```python
anna = Person("Anna", 16)
anna.wohnort = "Berlin"  # Neues Attribut!
print(anna.wohnort)      # Berlin
```

**Achtung:** Das ist möglich, aber oft nicht empfohlen! Besser alle Attribute in `__init__` definieren.

---

## Übung 3: Attribute manipulieren

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~10-15 Minuten**

**Aufgabe:**

1. **Erstelle Person-Klasse**
   ```python
   class Person:
       def __init__(self, name, alter, stadt):
           self.name = name
           self.alter = alter
           self.stadt = stadt
   ```

2. **Erstelle Objekt und lese Attribute**
   ```python
   anna = Person("Anna", 16, "Berlin")
   print(f"{anna.name} ist {anna.alter} und wohnt in {anna.stadt}")
   ```

3. **Ändere Attribute**
   ```python
   anna.alter = 17
   anna.stadt = "Hamburg"
   print(f"{anna.name} ist {anna.alter} und wohnt in {anna.stadt}")
   ```

4. **Füge neues Attribut hinzu**
   ```python
   anna.beruf = "Schülerin"
   print(anna.beruf)
   ```

5. **Teste: Was passiert bei nicht existierenden Attributen?**
   ```python
   print(anna.hobby)  # Was passiert hier?
   ```

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Klasse mit mehreren Attributen =====

class Person:
    def __init__(self, name, alter, stadt):
        self.name = name
        self.alter = alter
        self.stadt = stadt

anna = Person("Anna", 16, "Berlin")
print(f"{anna.name} ist {anna.alter} und wohnt in {anna.stadt}")
# Ausgabe: Anna ist 16 und wohnt in Berlin


# ===== SCHRITT 2: Attribute ändern =====

print("\n--- Vor der Änderung ---")
print(f"Alter: {anna.alter}")
print(f"Stadt: {anna.stadt}")

# Ändern
anna.alter = 17
anna.stadt = "Hamburg"

print("\n--- Nach der Änderung ---")
print(f"Alter: {anna.alter}")
print(f"Stadt: {anna.stadt}")


# ===== SCHRITT 3: Mehrere Objekte, unabhängige Attribute =====

anna = Person("Anna", 16, "Berlin")
ben = Person("Ben", 15, "München")

print(f"{anna.name}: {anna.stadt}")  # Anna: Berlin
print(f"{ben.name}: {ben.stadt}")    # Ben: München

# Änderung bei anna betrifft ben NICHT
anna.stadt = "Hamburg"

print(f"{anna.name}: {anna.stadt}")  # Anna: Hamburg
print(f"{ben.name}: {ben.stadt}")    # Ben: München (unverändert!)


# ===== SCHRITT 4: Neues Attribut zur Laufzeit =====

anna.beruf = "Schülerin"
anna.lieblingsfarbe = "Blau"

print(anna.beruf)          # Schülerin
print(anna.lieblingsfarbe) # Blau

# ACHTUNG: ben hat diese Attribute NICHT!
# print(ben.beruf)  # AttributeError!


# ===== SCHRITT 5: Nicht existierendes Attribut =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

anna = Person("Anna", 16)

# print(anna.stadt)  # AttributeError: 'Person' object has no attribute 'stadt'

# Besser: Prüfen ob Attribut existiert
if hasattr(anna, 'stadt'):
    print(anna.stadt)
else:
    print("Attribut 'stadt' existiert nicht")


# ===== SCHRITT 6: Attribut mit None initialisieren =====

class Person:
    def __init__(self, name, alter, stadt=None):
        self.name = name
        self.alter = alter
        self.stadt = stadt  # Kann None sein

anna = Person("Anna", 16)           # stadt=None
ben = Person("Ben", 15, "München")  # stadt="München"

print(anna.stadt)  # None
print(ben.stadt)   # München

# Prüfen ob gesetzt
if anna.stadt:
    print(f"Wohnt in {anna.stadt}")
else:
    print("Stadt nicht angegeben")


# ===== SCHRITT 7: Alle Attribute anzeigen =====

anna = Person("Anna", 16, "Berlin")
anna.beruf = "Schülerin"  # Nachträglich hinzugefügt

print(anna.__dict__)
# Ausgabe: {'name': 'Anna', 'alter': 16, 'stadt': 'Berlin', 'beruf': 'Schülerin'}


# ===== SCHRITT 8: Attribute löschen =====

anna = Person("Anna", 16, "Berlin")
print(anna.stadt)  # Berlin

del anna.stadt  # Attribut löschen

# print(anna.stadt)  # AttributeError!

# Neu setzen möglich
anna.stadt = "Hamburg"
print(anna.stadt)  # Hamburg
```

**Erklärungen:**

```
1. ATTRIBUT LESEN:
   objekt.attribut
   - Gibt den Wert des Attributs zurück
   - Falls Attribut nicht existiert: AttributeError

2. ATTRIBUT ÄNDERN:
   objekt.attribut = neuer_wert
   - Überschreibt den alten Wert
   - Falls Attribut nicht existiert: wird erstellt (!)

3. UNABHÄNGIGE OBJEKTE:
   - Jedes Objekt hat eigene Attribute
   - Änderungen bei einem Objekt betreffen andere NICHT
   - anna.alter = 17 ändert nicht ben.alter

4. NEUES ATTRIBUT HINZUFÜGEN:
   anna.beruf = "Schülerin"
   - Funktioniert in Python
   - Aber: Nur dieses Objekt hat das Attribut!
   - Andere Objekte haben es nicht
   - Nicht empfohlen! Besser in __init__ definieren

5. ATTRIBUTEERROR:
   print(anna.hobby)  # AttributeError
   - Passiert, wenn Attribut nicht existiert
   - Programm stürzt ab (Exception)
   - Besser vorher prüfen mit hasattr()

6. HASATTR():
   hasattr(objekt, 'attributname')
   - Prüft, ob Attribut existiert
   - Gibt True oder False zurück
   - Verhindert AttributeError

7. NONE ALS DEFAULT:
   def __init__(self, name, stadt=None):
   - None bedeutet "kein Wert"
   - Besser als Attribut gar nicht zu definieren
   - Kann später gesetzt werden

8. __DICT__:
   objekt.__dict__
   - Zeigt alle Attribute als Dictionary
   - Hilfreich zum Debuggen
   - Enthält Attributname: Wert Paare

9. DEL:
   del objekt.attribut
   - Löscht das Attribut
   - Danach existiert es nicht mehr
   - AttributeError beim Zugriff

10. WARUM ATTRIBUTE IN __INIT__ DEFINIEREN?
    - Dokumentation: Welche Attribute gibt es?
    - Konsistenz: Alle Objekte haben gleiche Attribute
    - Fehler vermeiden: Keine Tippfehler zur Laufzeit
    - Professionell: Standard in der Praxis
```

**Was wir gelernt haben:**

```
(OK) Attribute mit objekt.attribut lesen
(OK) Attribute mit objekt.attribut = wert ändern
(OK) Jedes Objekt hat eigene Attributwerte
(OK) Neue Attribute können hinzugefügt werden (nicht empfohlen)
(OK) hasattr() prüft Existenz von Attributen
(OK) AttributeError bei nicht existierenden Attributen
(OK) None als Default für optionale Attribute
```

**Typische Fehler:**

```
FEHLER: FEHLER: Tippfehler bei Attributname
   anna.Name = "Anna"      # Großes N
   print(anna.name)        # AttributeError (kleines n)
   
   → Python ist case-sensitive!

FEHLER: FEHLER: Attribut nicht initialisiert
   class Person:
       def __init__(self, name):
           self.name = name
           # self.alter fehlt!
   
   anna = Person("Anna")
   print(anna.alter)  # AttributeError
   
   → Alle Attribute in __init__ setzen!

FEHLER: FEHLER: Attribut nur bei einem Objekt hinzufügen
   anna = Person("Anna", 16)
   anna.beruf = "Schülerin"
   
   ben = Person("Ben", 15)
   print(ben.beruf)  # AttributeError
   
   → Nicht nachträglich hinzufügen, sondern in __init__

FEHLER: FEHLER: Auf gelöschtes Attribut zugreifen
   del anna.stadt
   print(anna.stadt)  # AttributeError
   
   → Nach del existiert Attribut nicht mehr
```

</details>

---

### Selbstcheck: Teil 3

1. Kann ich Attribute von außen ändern?
2. Was passiert, wenn ich auf ein nicht existierendes Attribut zugreife?
3. Warum sollte ich alle Attribute in `__init__` definieren?

<details>
<summary>Antworten anzeigen</summary>

1. Ja, mit `objekt.attribut = neuer_wert`. Das ist in Python standardmäßig möglich.
2. Python wirft einen `AttributeError` und das Programm stürzt ab (außer man fängt die Exception ab).
3. Damit alle Objekte die gleiche Struktur haben, keine Tippfehler passieren und der Code dokumentiert ist.

</details>

---

## Teil 4: Methoden

### Was sind Methoden?

Methoden sind Funktionen, die zu einer Klasse gehören und mit dem Objekt arbeiten.

**Unterschied zu Funktionen:**
- Methoden gehören zu einer Klasse
- Erster Parameter ist immer `self`
- Können auf Attribute zugreifen

**Syntax:**
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def begruessung(self):
        print(f"Hallo, ich bin {self.name}!")
```

**Aufruf:**
```python
anna = Person("Anna")
anna.begruessung()  # Hallo, ich bin Anna!
```

### Methoden mit Parametern

Methoden können zusätzliche Parameter haben.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def gruesse(self, andere_person):
        print(f"Hallo {andere_person}, ich bin {self.name}!")

anna = Person("Anna")
anna.gruesse("Ben")  # Hallo Ben, ich bin Anna!
```

### Methoden mit Rückgabewert

Methoden können Werte zurückgeben.

```python
class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
    
    def flaeche(self):
        return self.breite * self.hoehe

r = Rechteck(5, 3)
print(r.flaeche())  # 15
```

---

## Übung 4: Methoden hinzufügen

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~20-25 Minuten**

**Aufgabe:**

1. **Erstelle Klasse mit einfacher Methode**
   ```python
   class Person:
       def __init__(self, name, alter):
           self.name = name
           self.alter = alter
       
       def vorstellen(self):
           print(f"Hallo, ich bin {self.name} und bin {self.alter} Jahre alt.")
   ```

2. **Rufe die Methode auf**
   ```python
   anna = Person("Anna", 16)
   anna.vorstellen()
   ```

3. **Methode, die den Zustand ändert**
   ```python
   def hatte_geburtstag(self):
       self.alter = self.alter + 1
       print(f"Alles Gute! {self.name} ist jetzt {self.alter}!")
   ```

4. **Methode mit Rückgabewert**
   ```python
   def ist_volljaehrig(self):
       return self.alter >= 18
   ```

5. **Erstelle Rechner-Klasse**
   ```python
   class Rechner:
       def addiere(self, a, b):
           return a + b
       
       def multipliziere(self, a, b):
           return a * b
   ```

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Einfache Methode ohne Parameter =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name} und bin {self.alter} Jahre alt.")

anna = Person("Anna", 16)
anna.vorstellen()
# Ausgabe: Hallo, ich bin Anna und bin 16 Jahre alt.

ben = Person("Ben", 15)
ben.vorstellen()
# Ausgabe: Hallo, ich bin Ben und bin 15 Jahre alt.


# ===== SCHRITT 2: Methode die Attribut ändert =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def hatte_geburtstag(self):
        self.alter = self.alter + 1  # oder: self.alter += 1
        print(f"Alles Gute! {self.name} ist jetzt {self.alter}!")

anna = Person("Anna", 16)
print(f"Alter vorher: {anna.alter}")  # 16

anna.hatte_geburtstag()
# Ausgabe: Alles Gute! Anna ist jetzt 17!

print(f"Alter nachher: {anna.alter}")  # 17


# ===== SCHRITT 3: Methode mit Rückgabewert =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def ist_volljaehrig(self):
        return self.alter >= 18
    
    def ist_teenager(self):
        return 13 <= self.alter <= 19

anna = Person("Anna", 16)
ben = Person("Ben", 20)

print(f"{anna.name} volljährig? {anna.ist_volljaehrig()}")  # False
print(f"{ben.name} volljährig? {ben.ist_volljaehrig()}")    # True

print(f"{anna.name} Teenager? {anna.ist_teenager()}")  # True
print(f"{ben.name} Teenager? {ben.ist_teenager()}")    # False


# ===== SCHRITT 4: Methode mit Parametern =====

class Person:
    def __init__(self, name):
        self.name = name
    
    def gruesse(self, andere_person):
        print(f"Hallo {andere_person}, ich bin {self.name}!")
    
    def schenke(self, geschenk, empfaenger):
        print(f"{self.name} schenkt {empfaenger} ein {geschenk}.")

anna = Person("Anna")
anna.gruesse("Ben")
# Ausgabe: Hallo Ben, ich bin Anna!

anna.schenke("Buch", "Clara")
# Ausgabe: Anna schenkt Clara ein Buch.


# ===== SCHRITT 5: Rechner-Klasse =====

class Rechner:
    def addiere(self, a, b):
        return a + b
    
    def subtrahiere(self, a, b):
        return a - b
    
    def multipliziere(self, a, b):
        return a * b
    
    def dividiere(self, a, b):
        if b == 0:
            return "Division durch 0 nicht möglich!"
        return a / b

r = Rechner()

print(r.addiere(5, 3))        # 8
print(r.subtrahiere(10, 4))   # 6
print(r.multipliziere(7, 6))  # 42
print(r.dividiere(15, 3))     # 5.0
print(r.dividiere(10, 0))     # Division durch 0 nicht möglich!


# ===== SCHRITT 6: Methoden können andere Methoden aufrufen =====

class Person:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
    
    def voller_name(self):
        return f"{self.vorname} {self.nachname}"
    
    def vorstellen(self):
        # Nutzt andere Methode!
        name = self.voller_name()
        print(f"Hallo, ich bin {name}!")

anna = Person("Anna", "Müller")
print(anna.voller_name())  # Anna Müller
anna.vorstellen()          # Hallo, ich bin Anna Müller!


# ===== SCHRITT 7: Bankkonto mit Methoden =====

class Bankkonto:
    def __init__(self, inhaber, kontostand=0):
        self.inhaber = inhaber
        self.kontostand = kontostand
    
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand = self.kontostand + betrag
            print(f"{betrag}€ eingezahlt. Neuer Stand: {self.kontostand}€")
        else:
            print("Betrag muss positiv sein!")
    
    def abheben(self, betrag):
        if betrag > self.kontostand:
            print("Nicht genug Geld auf dem Konto!")
        elif betrag > 0:
            self.kontostand = self.kontostand - betrag
            print(f"{betrag}€ abgehoben. Neuer Stand: {self.kontostand}€")
        else:
            print("Betrag muss positiv sein!")
    
    def kontostand_anzeigen(self):
        print(f"Kontostand von {self.inhaber}: {self.kontostand}€")

konto = Bankkonto("Anna", 100)
konto.kontostand_anzeigen()  # Kontostand von Anna: 100€

konto.einzahlen(50)          # 50€ eingezahlt. Neuer Stand: 150€
konto.abheben(30)            # 30€ abgehoben. Neuer Stand: 120€
konto.abheben(200)           # Nicht genug Geld auf dem Konto!
konto.kontostand_anzeigen()  # Kontostand von Anna: 120€
```

**Erklärungen:**

```
1. METHODE DEFINIEREN:
   def methodenname(self):
       # Code
   
   - Wie eine Funktion, aber in einer Klasse
   - Immer self als erster Parameter
   - Einrückung innerhalb der Klasse

2. METHODE AUFRUFEN:
   objekt.methode()
   
   - Objekt, dann Punkt, dann Methodenname
   - self wird automatisch übergeben
   - NICHT: objekt.methode(self) → FALSCH!

3. SELF IN METHODEN:
   def vorstellen(self):
       print(self.name)
   
   - self ermöglicht Zugriff auf Attribute
   - self.name = Attribut des Objekts
   - Ohne self: name wäre lokale Variable

4. METHODE ÄNDERT ATTRIBUT:
   def hatte_geburtstag(self):
       self.alter += 1
   
   - Methode kann Attribute ändern
   - Änderung bleibt bestehen
   - Zustand des Objekts wird verändert

5. RETURN IN METHODEN:
   def ist_volljaehrig(self):
       return self.alter >= 18
   
   - Wie bei Funktionen
   - Gibt Wert zurück
   - Kann in Bedingungen genutzt werden

6. METHODE MIT PARAMETERN:
   def gruesse(self, andere_person):
       print(f"Hallo {andere_person}")
   
   - self ist immer erster Parameter
   - Danach kommen weitere Parameter
   - Beim Aufruf: objekt.gruesse("Ben")

7. METHODEN AUFRUFEN METHODEN:
   def voller_name(self):
       return f"{self.vorname} {self.nachname}"
   
   def vorstellen(self):
       name = self.voller_name()  # Andere Methode!
       print(f"Ich bin {name}")
   
   - Methoden können andere Methoden aufrufen
   - Auch hier: self.methodenname()

8. VALIDATION IN METHODEN:
   def einzahlen(self, betrag):
       if betrag > 0:
           # ...
       else:
           print("Fehler!")
   
   - Methoden sollten Eingaben prüfen
   - Verhindert ungültige Zustände
   - Gibt Feedback bei Fehlern

9. WARUM METHODEN STATT FUNKTIONEN?
   - Methoden haben Zugriff auf Objektdaten (self)
   - Gehören logisch zum Objekt
   - Kapseln Verhalten mit Daten
   - Objekt "weiß", was es tun kann

10. METHODEN VS FUNKTIONEN:
    Funktion:
    def begruessung(name):
        print(f"Hallo {name}")
    
    Methode:
    class Person:
        def begruessung(self):
            print(f"Hallo {self.name}")
    
    → Methode nutzt Objektdaten!
```

**Was wir gelernt haben:**

```
(OK) Methoden sind Funktionen in Klassen
(OK) Erster Parameter ist immer self
(OK) Methoden greifen auf Attribute zu
(OK) Methoden können Attribute ändern
(OK) Methoden können Werte zurückgeben
(OK) Methoden können Parameter haben
(OK) Methoden können andere Methoden aufrufen
```

**Typische Fehler:**

```
FEHLER: FEHLER: self vergessen
   class Person:
       def vorstellen():  # FALSCH!
           print(self.name)
   
   Richtig:
       def vorstellen(self):

FEHLER: FEHLER: self beim Aufruf angeben
   anna.vorstellen(self)  # FALSCH!
   
   Richtig:
   anna.vorstellen()

FEHLER: FEHLER: self. vergessen bei Attributzugriff
   class Person:
       def vorstellen(self):
           print(name)  # FALSCH! Wo ist name definiert?
   
   Richtig:
       print(self.name)

FEHLER: FEHLER: Methode ohne Klammern aufrufen
   anna.vorstellen  # FALSCH! Gibt Methodenobjekt zurück
   
   Richtig:
   anna.vorstellen()

FEHLER: FEHLER: Return vergessen
   def flaeche(self):
       self.breite * self.hoehe  # FALSCH! Kein return!
   
   Richtig:
       return self.breite * self.hoehe
```

</details>

---

### Selbstcheck: Teil 4

1. Was ist der Unterschied zwischen einer Methode und einer Funktion?
2. Warum brauchen Methoden `self`?
3. Kann eine Methode Attribute ändern?

<details>
<summary>Antworten anzeigen</summary>

1. Eine Methode gehört zu einer Klasse und hat `self` als ersten Parameter. Eine Funktion ist unabhängig und hat keinen automatischen Objektbezug.
2. `self` gibt der Methode Zugriff auf die Attribute und andere Methoden des Objekts.
3. Ja, mit `self.attribut = neuer_wert` kann eine Methode den Zustand des Objekts ändern.

</details>

---

## Teil 5: Mehrere Objekte

### Objekte sind unabhängig

Jedes Objekt hat seinen eigenen Zustand.

```python
class Zaehler:
    def __init__(self):
        self.stand = 0
    
    def erhoehen(self):
        self.stand += 1

z1 = Zaehler()
z2 = Zaehler()

z1.erhoehen()
z1.erhoehen()

print(z1.stand)  # 2
print(z2.stand)  # 0 (unverändert!)
```

### Objekte in Listen

Objekte können in Listen gespeichert werden.

```python
class Person:
    def __init__(self, name):
        self.name = name

personen = []
personen.append(Person("Anna"))
personen.append(Person("Ben"))
personen.append(Person("Clara"))

for person in personen:
    print(person.name)
```

---

## Übung 5: Mit mehreren Objekten arbeiten

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~20-25 Minuten**

**Aufgabe:**

1. **Erstelle Zaehler-Klasse**
   ```python
   class Zaehler:
       def __init__(self, start=0):
           self.stand = start
       
       def erhoehen(self):
           self.stand += 1
       
       def anzeigen(self):
           print(f"Stand: {self.stand}")
   ```

2. **Erstelle mehrere unabhängige Zähler**
   ```python
   z1 = Zaehler()
   z2 = Zaehler(10)
   
   z1.erhoehen()
   z1.erhoehen()
   z2.erhoehen()
   
   z1.anzeigen()
   z2.anzeigen()
   ```

3. **Person-Klasse mit Liste**
   ```python
   class Person:
       def __init__(self, name, alter):
           self.name = name
           self.alter = alter
       
       def info(self):
           return f"{self.name} ({self.alter})"
   
   personen = []
   personen.append(Person("Anna", 16))
   personen.append(Person("Ben", 15))
   personen.append(Person("Clara", 17))
   ```

4. **Durch Liste iterieren**
   ```python
   for person in personen:
       print(person.info())
   ```

5. **Objekte suchen**
   ```python
   def finde_person(personen_liste, name):
       for person in personen_liste:
           if person.name == name:
               return person
       return None
   ```

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Mehrere unabhängige Objekte =====

class Zaehler:
    def __init__(self, start=0):
        self.stand = start
    
    def erhoehen(self, schritt=1):
        self.stand += schritt
    
    def zuruecksetzen(self):
        self.stand = 0
    
    def anzeigen(self):
        print(f"Stand: {self.stand}")

z1 = Zaehler()       # start=0
z2 = Zaehler(10)     # start=10
z3 = Zaehler(100)    # start=100

z1.erhoehen()
z1.erhoehen()
print(f"z1: {z1.stand}")  # 2

z2.erhoehen()
z2.erhoehen()
z2.erhoehen()
print(f"z2: {z2.stand}")  # 13

z3.erhoehen(50)
print(f"z3: {z3.stand}")  # 150

# Objekte sind UNABHÄNGIG!


# ===== SCHRITT 2: Objekte in Liste =====

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def info(self):
        return f"{self.name} ({self.alter} Jahre)"

# Liste erstellen und füllen
personen = []
personen.append(Person("Anna", 16))
personen.append(Person("Ben", 15))
personen.append(Person("Clara", 17))

# Alle ausgeben
print("=== Alle Personen ===")
for person in personen:
    print(person.info())


# ===== SCHRITT 3: Objekte direkt in Liste erstellen =====

personen2 = [
    Person("David", 18),
    Person("Emma", 16),
    Person("Felix", 17)
]

for person in personen2:
    print(person.info())


# ===== SCHRITT 4: Nach bestimmten Objekten suchen =====

def finde_person(personen_liste, gesuchter_name):
    for person in personen_liste:
        if person.name == gesuchter_name:
            return person
    return None

gefunden = finde_person(personen, "Ben")
if gefunden:
    print(f"Gefunden: {gefunden.info()}")
else:
    print("Person nicht gefunden")


# ===== SCHRITT 5: Filtern nach Kriterium =====

def finde_volljaehrige(personen_liste):
    volljaehrige = []
    for person in personen_liste:
        if person.alter >= 18:
            volljaehrige.append(person)
    return volljaehrige

alle = [
    Person("Anna", 16),
    Person("Ben", 20),
    Person("Clara", 17),
    Person("David", 19)
]

erwachsene = finde_volljaehrige(alle)
print("\n=== Volljährige Personen ===")
for person in erwachsene:
    print(person.info())


# ===== SCHRITT 6: Durchschnittsalter berechnen =====

def durchschnittsalter(personen_liste):
    if len(personen_liste) == 0:
        return 0
    
    summe = 0
    for person in personen_liste:
        summe += person.alter
    
    return summe / len(personen_liste)

personen = [
    Person("Anna", 16),
    Person("Ben", 20),
    Person("Clara", 18)
]

durchschnitt = durchschnittsalter(personen)
print(f"\nDurchschnittsalter: {durchschnitt:.1f} Jahre")


# ===== SCHRITT 7: Objekte sortieren =====

personen = [
    Person("Clara", 17),
    Person("Anna", 16),
    Person("Ben", 20)
]

# Nach Namen sortieren
personen_nach_name = sorted(personen, key=lambda p: p.name)
print("\n=== Nach Name sortiert ===")
for person in personen_nach_name:
    print(person.info())

# Nach Alter sortieren
personen_nach_alter = sorted(personen, key=lambda p: p.alter)
print("\n=== Nach Alter sortiert ===")
for person in personen_nach_alter:
    print(person.info())


# ===== SCHRITT 8: Klassenzimmer-Beispiel =====

class Klassenzimmer:
    def __init__(self, name):
        self.name = name
        self.schueler = []
    
    def schueler_hinzufuegen(self, person):
        self.schueler.append(person)
        print(f"{person.name} wurde zu {self.name} hinzugefügt")
    
    def alle_schueler(self):
        print(f"\n=== Schüler in {self.name} ===")
        for schueler in self.schueler:
            print(schueler.info())
    
    def anzahl_schueler(self):
        return len(self.schueler)

klasse_10a = Klassenzimmer("Klasse 10a")
klasse_10a.schueler_hinzufuegen(Person("Anna", 16))
klasse_10a.schueler_hinzufuegen(Person("Ben", 15))
klasse_10a.schueler_hinzufuegen(Person("Clara", 16))

klasse_10a.alle_schueler()
print(f"Anzahl Schüler: {klasse_10a.anzahl_schueler()}")
```

**Erklärungen:**

```
1. OBJEKTE SIND UNABHÄNGIG:
   z1 = Zaehler()
   z2 = Zaehler()
   
   z1.erhoehen()
   
   - Ändert nur z1, nicht z2
   - Jedes Objekt hat eigenen Speicher
   - Eigene Attribute, eigener Zustand

2. LISTE VON OBJEKTEN:
   personen = []
   personen.append(Person("Anna", 16))
   
   - Objekte wie andere Datentypen
   - Können in Listen, Dictionaries, etc.
   - Normale list-Operationen funktionieren

3. OBJEKTE IN FOR-SCHLEIFE:
   for person in personen:
       print(person.name)
   
   - person ist jeweils ein Person-Objekt
   - Zugriff auf Attribute und Methoden
   - Wie mit anderen Datentypen

4. OBJEKTE SUCHEN:
   def finde_person(liste, name):
       for person in liste:
           if person.name == name:
               return person
       return None
   
   - Durch Liste iterieren
   - Attribut vergleichen
   - Objekt zurückgeben oder None

5. OBJEKTE FILTERN:
   volljaehrige = []
   for person in personen:
       if person.alter >= 18:
           volljaehrige.append(person)
   
   - Neue Liste erstellen
   - Nur Objekte mit bestimmtem Kriterium
   - Original-Liste bleibt unverändert

6. BERECHNUNGEN ÜBER OBJEKTE:
   summe = 0
   for person in personen:
       summe += person.alter
   durchschnitt = summe / len(personen)
   
   - Attribute aller Objekte nutzen
   - Berechnungen durchführen
   - Ergebnisse zurückgeben

7. OBJEKTE SORTIEREN:
   sorted(personen, key=lambda p: p.name)
   
   - Lambda-Funktion gibt Attribut zum Sortieren an
   - Alphabetisch nach Name: p.name
   - Numerisch nach Alter: p.alter
   - sorted() gibt neue sortierte Liste zurück

8. OBJEKTE IN OBJEKTEN:
   class Klassenzimmer:
       def __init__(self):
           self.schueler = []  # Liste von Person-Objekten
   
   - Objekte können andere Objekte enthalten
   - Komposition: "hat-eine" Beziehung
   - Verschachtelte Strukturen möglich

9. LAMBDA-FUNKTION:
   lambda p: p.name
   
   - Anonyme Funktion
   - p ist Parameter
   - p.name ist Rückgabewert
   - Für kurze, einfache Funktionen
   
   Äquivalent zu:
   def get_name(p):
       return p.name

10. BEST PRACTICE:
    - Objekte in Listen für Gruppen
    - Funktionen für Operationen auf Listen
    - Methoden für Operationen auf einzelnen Objekten
    - Klassen für zusammenhängende Objekte (Klassenzimmer)
```

**Was wir gelernt haben:**

```
(OK) Objekte sind unabhängig voneinander
(OK) Objekte können in Listen gespeichert werden
(OK) Mit for-Schleife über Objekte iterieren
(OK) Objekte suchen, filtern, sortieren
(OK) Berechnungen über mehrere Objekte
(OK) Objekte können andere Objekte enthalten
```

**Typische Fehler:**

```
FEHLER: FEHLER: Denken, Objekte teilen Zustand
   z1 = Zaehler()
   z2 = Zaehler()
   z1.erhoehen()
   print(z2.stand)  # 0, nicht 1!
   
   → Jedes Objekt ist unabhängig

FEHLER: FEHLER: Attribut vergessen beim Zugriff in Schleife
   for person in personen:
       print(name)  # FALSCH! Wo kommt name her?
   
   Richtig:
       print(person.name)

FEHLER: FEHLER: Liste nicht initialisieren
   personen.append(Person("Anna", 16))  # NameError
   
   Richtig:
   personen = []
   personen.append(Person("Anna", 16))

FEHLER: FEHLER: Objekt mit String vergleichen
   if person == "Anna":  # FALSCH!
   
   Richtig:
   if person.name == "Anna":

FEHLER: FEHLER: Sortieren ohne key
   sorted(personen)  # Fehler! Python weiß nicht wie
   
   Richtig:
   sorted(personen, key=lambda p: p.name)
```

</details>

---

### Selbstcheck: Teil 5

1. Wenn ich ein Attribut bei einem Objekt ändere, ändert sich das bei anderen Objekten?
2. Wie kann ich Objekte in einer Liste speichern?
3. Wie finde ich ein bestimmtes Objekt in einer Liste?

<details>
<summary>Antworten anzeigen</summary>

1. Nein! Jedes Objekt ist unabhängig und hat eigene Attributwerte.
2. Ganz normal mit `liste.append(objekt)` oder `liste = [objekt1, objekt2]`
3. Mit einer Schleife durchgehen und Attribute vergleichen: `if objekt.name == gesuchter_name`

</details>

---

## Teil 6: Klassenattribute vs. Instanzattribute

### Der Unterschied

**WICHTIGE WARNUNG - Häufiger Fehler:**

**NIEMALS Instanz- und Klassenattribut mit dem gleichen Namen verwenden!**

Das führt zu verwirrenden Fehlern (Shadowing). Wenn du `objekt.attribut = wert` schreibst, erstellst du ein neues Instanzattribut, das das Klassenattribut "überschattet". Klassenattribute sollten immer über den Klassennamen geändert werden: `Klassenname.attribut = wert`.

Mehr dazu in den Beispielen unten.

---

**Instanzattribut:**
- Gehört zu einem einzelnen Objekt
- Jedes Objekt hat eigenen Wert
- Definiert mit `self.`

**Klassenattribut:**
- Gehört zur Klasse, wird von allen Objekten geteilt
- Alle Objekte sehen den gleichen Wert
- Definiert direkt in der Klasse (ohne `self`)

```python
class Person:
    # Klassenattribut (geteilt)
    anzahl = 0
    
    def __init__(self, name):
        # Instanzattribut (individuell)
        self.name = name
        Person.anzahl += 1

p1 = Person("Anna")
p2 = Person("Ben")

print(p1.name)      # Anna (individuell)
print(p2.name)      # Ben (individuell)
print(Person.anzahl) # 2 (geteilt)
```

---

## Übung 6: Klassenattribute verstehen

**Schwierigkeitsgrad: FORTGESCHRITTEN**  
**Dauer: ~25-30 Minuten**  
**Hinweis:** Diese Übung behandelt fortgeschrittene Konzepte. Mache sie erst nach den Grundlagen-Übungen 1-5.

**Aufgabe:**

1. **Erstelle Klasse mit Klassenattribut**
   ```python
   class Auto:
       anzahl_autos = 0
       
       def __init__(self, marke):
           self.marke = marke
           Auto.anzahl_autos += 1
   ```

2. **Erstelle mehrere Objekte**
   ```python
   a1 = Auto("VW")
   a2 = Auto("BMW")
   a3 = Auto("Audi")
   
   print(Auto.anzahl_autos)  # 3
   ```

3. **Klassenattribut als Konstante**
   ```python
   class Kreis:
       PI = 3.14159
       
       def __init__(self, radius):
           self.radius = radius
       
       def flaeche(self):
           return Kreis.PI * self.radius * self.radius
   ```

4. **Teste: Was passiert bei Änderung?**
   ```python
   a1 = Auto("VW")
   a2 = Auto("BMW")
   
   print(Auto.anzahl_autos)  # 2
   a1.anzahl_autos = 999
   print(a1.anzahl_autos)    # ?
   print(a2.anzahl_autos)    # ?
   print(Auto.anzahl_autos)  # ?
   ```

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python
# ===== SCHRITT 1: Klassenattribut für Zählung =====

class Auto:
    # Klassenattribut (geteilt von allen)
    anzahl_autos = 0
    
    def __init__(self, marke, farbe):
        # Instanzattribute (individuell)
        self.marke = marke
        self.farbe = farbe
        
        # Klassenattribut erhöhen
        Auto.anzahl_autos += 1
    
    def info(self):
        return f"{self.farbe}er {self.marke}"

print(f"Autos am Start: {Auto.anzahl_autos}")  # 0

a1 = Auto("VW", "Rot")
print(f"Autos jetzt: {Auto.anzahl_autos}")     # 1

a2 = Auto("BMW", "Blau")
a3 = Auto("Audi", "Schwarz")
print(f"Autos jetzt: {Auto.anzahl_autos}")     # 3

print(a1.info())  # Roter VW
print(a2.info())  # Blauer BMW


# ===== SCHRITT 2: Zugriff auf Klassenattribut =====

# Über die Klasse (empfohlen)
print(Auto.anzahl_autos)  # 3

# Über ein Objekt (funktioniert auch)
print(a1.anzahl_autos)    # 3
print(a2.anzahl_autos)    # 3

# ALLE sehen den gleichen Wert!


# ===== SCHRITT 3: Klassenattribut als Konstante =====

class Kreis:
    # Konstante als Klassenattribut
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def flaeche(self):
        # Zugriff über Klassenname
        return Kreis.PI * self.radius * self.radius
    
    def umfang(self):
        return 2 * Kreis.PI * self.radius

k1 = Kreis(5)
k2 = Kreis(10)

print(f"Fläche k1: {k1.flaeche():.2f}")  # 78.54
print(f"Fläche k2: {k2.flaeche():.2f}")  # 314.16

print(f"PI ist: {Kreis.PI}")  # 3.14159


# ===== SCHRITT 4: ACHTUNG! Fallstrick =====

class Auto:
    anzahl_autos = 0
    
    def __init__(self, marke):
        self.marke = marke
        Auto.anzahl_autos += 1

a1 = Auto("VW")
a2 = Auto("BMW")

print("=== VOR der Änderung ===")
print(f"Auto.anzahl_autos: {Auto.anzahl_autos}")  # 2
print(f"a1.anzahl_autos: {a1.anzahl_autos}")      # 2
print(f"a2.anzahl_autos: {a2.anzahl_autos}")      # 2

# ACHTUNG: Instanzattribut erstellen!
a1.anzahl_autos = 999

print("\n=== NACH der Änderung ===")
print(f"Auto.anzahl_autos: {Auto.anzahl_autos}")  # 2 (unverändert!)
print(f"a1.anzahl_autos: {a1.anzahl_autos}")      # 999 (eigenes Attribut!)
print(f"a2.anzahl_autos: {a2.anzahl_autos}")      # 2 (Klassenattribut)

# Erklärung:
# a1.anzahl_autos = 999 erstellt ein NEUES Instanzattribut
# Es überschattet das Klassenattribut nur für a1


# ===== SCHRITT 5: Klassenattribut richtig ändern =====

class Auto:
    anzahl_autos = 0
    
    def __init__(self, marke):
        self.marke = marke
        Auto.anzahl_autos += 1

a1 = Auto("VW")
a2 = Auto("BMW")

print(f"Vorher: {Auto.anzahl_autos}")  # 2

# ÜBER DIE KLASSE ändern
Auto.anzahl_autos = 999

print(f"Nachher: {Auto.anzahl_autos}")  # 999
print(f"a1: {a1.anzahl_autos}")         # 999
print(f"a2: {a2.anzahl_autos}")         # 999

# Jetzt sehen ALLE die Änderung!


# ===== SCHRITT 6: Praktisches Beispiel - ID-Vergabe =====

class Ticket:
    # Klassenattribut für nächste ID
    naechste_id = 1
    
    def __init__(self, titel):
        # Jedes Ticket bekommt eindeutige ID
        self.id = Ticket.naechste_id
        self.titel = titel
        
        # ID für nächstes Ticket erhöhen
        Ticket.naechste_id += 1
    
    def info(self):
        return f"Ticket #{self.id}: {self.titel}"

t1 = Ticket("Bug im Login")
t2 = Ticket("Feature-Request")
t3 = Ticket("Performance-Problem")

print(t1.info())  # Ticket #1: Bug im Login
print(t2.info())  # Ticket #2: Feature-Request
print(t3.info())  # Ticket #3: Performance-Problem


# ===== SCHRITT 7: Unterschied nochmal klar =====

class Demo:
    klassenattribut = "Ich bin geteilt"
    
    def __init__(self, wert):
        self.instanzattribut = wert

d1 = Demo("Ich gehöre zu d1")
d2 = Demo("Ich gehöre zu d2")

print("=== Instanzattribute (individuell) ===")
print(d1.instanzattribut)  # Ich gehöre zu d1
print(d2.instanzattribut)  # Ich gehöre zu d2

print("\n=== Klassenattribut (geteilt) ===")
print(Demo.klassenattribut)  # Ich bin geteilt
print(d1.klassenattribut)    # Ich bin geteilt
print(d2.klassenattribut)    # Ich bin geteilt

# Änderung des Klassenattributs
Demo.klassenattribut = "Neue Nachricht"

print("\n=== Nach Änderung ===")
print(d1.klassenattribut)  # Neue Nachricht
print(d2.klassenattribut)  # Neue Nachricht
```

**Erklärungen:**

```
1. KLASSENATTRIBUT:
   class Auto:
       anzahl_autos = 0  # Außerhalb von __init__
   
   - Direkt in der Klasse definiert
   - NICHT mit self
   - Gehört zur Klasse, nicht zu Instanzen

2. INSTANZATTRIBUT:
   def __init__(self):
       self.marke = "VW"  # Mit self
   
   - In __init__ oder Methoden definiert
   - MIT self
   - Gehört zur einzelnen Instanz

3. ZUGRIFF AUF KLASSENATTRIBUT:
   # Über Klasse (empfohlen)
   Auto.anzahl_autos
   
   # Über Instanz (funktioniert, aber verwirrend)
   a1.anzahl_autos
   
   - Beides funktioniert
   - Über Klasse ist klarer

4. KLASSENATTRIBUT ÄNDERN:
   # Richtig (betrifft alle)
   Auto.anzahl_autos = 10
   
   # Falsch (nur diese Instanz)
   a1.anzahl_autos = 10
   
   - IMMER über Klassenname ändern
   - Sonst Instanzattribut mit gleichem Namen!

5. WARUM KLASSENATTRIBUTE?
   - Zähler für alle Instanzen
   - Konstanten (PI, MAX_SPEED, etc.)
   - Gemeinsame Konfiguration
   - Standard-Werte

6. SHADOWING (ÜBERSCHATTEN):
   a1.anzahl_autos = 999
   
   - Erstellt NEUES Instanzattribut
   - Überschattet Klassenattribut
   - Nur für diese Instanz
   - **WARNUNG: SEHR verwirrend! UNBEDINGT VERMEIDEN! WARNUNG:**
   - **NIEMALS Instanz- und Klassenattribut mit gleichem Namen!**

7. BEST PRACTICE:
   - Klassenattribute: Konstanten in GROSSBUCHSTABEN
   - Klassenattribute: Zähler über Klassenname ändern
   - Instanzattribute: Immer mit self
   - **KRITISCH: Niemals Instanzattribut mit gleichem Namen wie Klassenattribut**

8. WANN WELCHES?
   Klassenattribut:
   - Gilt für ALLE Instanzen
   - Wird geteilt
   - Wenig Speicher (nur einmal)
   
   Instanzattribut:
   - Gilt für EINE Instanz
   - Individuell
   - Mehr Speicher (pro Instanz)

9. ID-VERGABE:
   naechste_id = 1
   self.id = Ticket.naechste_id
   Ticket.naechste_id += 1
   
   - Klassenattribut als Zähler
   - Jede Instanz bekommt eindeutige ID
   - Automatische Vergabe
   - Praktisches Pattern!

10. VISUALISIERUNG:
    Klasse:
    [klassenattribut: "geteilt"]
         |
         ├─ Instanz 1: [instanzattribut: "individuell"]
         |
         └─ Instanz 2: [instanzattribut: "individuell"]
    
    - Klassenattribut existiert einmal
    - Instanzattribute pro Objekt
```

**Was wir gelernt haben:**

```
(OK) Klassenattribute werden von allen geteilt
(OK) Instanzattribute sind individuell pro Objekt
(OK) Klassenattribut über Klassenname ändern
(OK) Nicht: gleichnamiges Instanzattribut erstellen
(OK) Klassenattribute für Konstanten und Zähler
(OK) ID-Vergabe mit Klassenattribut
```

**Typische Fehler:**

```
FEHLER: FEHLER: Klassenattribut über Instanz ändern
   a1.anzahl_autos = 999  # Erstellt Instanzattribut!
   
   Richtig:
   Auto.anzahl_autos = 999

FEHLER: FEHLER: self bei Klassenattribut
   class Auto:
       def __init__(self):
           self.anzahl_autos = 0  # FALSCH! Das ist Instanzattribut
   
   Richtig:
   class Auto:
       anzahl_autos = 0  # Außerhalb von __init__

FEHLER: FEHLER: Klassenattribut nicht über Klassenname erhöhen
   def __init__(self):
       anzahl_autos += 1  # FEHLER! Unbekannte Variable
   
   Richtig:
       Auto.anzahl_autos += 1

FEHLER: FEHLER: Denken, dass a1.klassenattribut nur für a1 gilt
   a1.PI = 3.14  # Verwirrt! Überschattet Klassenattribut
   
   → Niemals Instanz- und Klassenattribut mit gleichem Namen!
```

</details>

---

### Selbstcheck: Teil 6

1. Was ist der Unterschied zwischen Klassenattribut und Instanzattribut?
2. Wie ändere ich ein Klassenattribut richtig?
3. Wofür würde ich ein Klassenattribut verwenden?

<details>
<summary>Antworten anzeigen</summary>

1. Klassenattribut wird von allen Objekten geteilt, Instanzattribut ist individuell pro Objekt.
2. Über den Klassennamen: `Klassenname.attribut = wert`, NICHT über ein Objekt!
3. Für Zähler (Anzahl erstellter Objekte), Konstanten (PI, MAX_SPEED), oder gemeinsame Konfiguration.

</details>

---

## Bonus-Übung: Bankkonto-System

**Schwierigkeitsgrad: FORTGESCHRITTEN**  
**Dauer: ~45-60 Minuten**  
**WICHTIG:** Diese Übung ist optional und fortgeschritten. Mache sie nur, wenn du alle Grundlagen-Übungen (1-5) verstanden hast!

**Aufgabe:**

Erstelle ein einfaches Bankkonto-System mit folgenden Anforderungen:

1. **Klasse Bankkonto**
   - Attribute: inhaber (String), kontostand (Float), kontonummer (Int)
   - Methoden: einzahlen, abheben, kontostand_anzeigen, ueberweisen

2. **Automatische Kontonummer-Vergabe**
   - Nutze ein Klassenattribut für die nächste Kontonummer
   - Jedes neue Konto bekommt automatisch eine eindeutige Nummer

3. **Eingabevalidierung**
   - Einzahlung nur mit positivem Betrag
   - Abhebung nur wenn genug Geld vorhanden
   - Überweisung nur wenn genug Geld vorhanden

4. **Überweisung zwischen Konten**
   - Methode ueberweisen(ziel_konto, betrag)
   - Geld von einem Konto auf ein anderes übertragen

5. **Teste das System**
   - Erstelle mehrere Konten
   - Führe verschiedene Transaktionen durch
   - Zeige Kontostände

<details>
<summary>Vollständige Lösung anzeigen</summary>

```python
# ===== BANKKONTO-SYSTEM =====

class Bankkonto:
    # Klassenattribut für automatische Kontonummer
    naechste_kontonummer = 1000
    
    def __init__(self, inhaber, anfangsstand=0):
        """
        Erstellt ein neues Bankkonto.
        
        inhaber: Name des Kontoinhabers
        anfangsstand: Startguthaben (Standard: 0)
        """
        self.inhaber = inhaber
        self.kontostand = anfangsstand
        self.kontonummer = Bankkonto.naechste_kontonummer
        
        # Kontonummer für nächstes Konto erhöhen
        Bankkonto.naechste_kontonummer += 1
        
        print(f"Konto erstellt: {self.inhaber} (Nr. {self.kontonummer})")
    
    def einzahlen(self, betrag):
        """
        Zahlt Geld auf das Konto ein.
        
        betrag: Einzuzahlender Betrag (muss positiv sein)
        """
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein!")
            return False
        
        self.kontostand += betrag
        print(f"{betrag}€ eingezahlt. Neuer Stand: {self.kontostand}€")
        return True
    
    def abheben(self, betrag):
        """
        Hebt Geld vom Konto ab.
        
        betrag: Abzuhebender Betrag (muss positiv sein)
        """
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein!")
            return False
        
        if betrag > self.kontostand:
            print(f"Fehler: Nicht genug Geld! Verfügbar: {self.kontostand}€")
            return False
        
        self.kontostand -= betrag
        print(f"{betrag}€ abgehoben. Neuer Stand: {self.kontostand}€")
        return True
    
    def kontostand_anzeigen(self):
        """
        Zeigt den aktuellen Kontostand an.
        """
        print(f"Konto {self.kontonummer} ({self.inhaber}): {self.kontostand}€")
    
    def ueberweisen(self, ziel_konto, betrag):
        """
        Überweist Geld auf ein anderes Konto.
        
        ziel_konto: Bankkonto-Objekt des Empfängers
        betrag: Zu überweisender Betrag
        """
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein!")
            return False
        
        if betrag > self.kontostand:
            print(f"Fehler: Nicht genug Geld! Verfügbar: {self.kontostand}€")
            return False
        
        # Geld abziehen
        self.kontostand -= betrag
        
        # Geld hinzufügen
        ziel_konto.kontostand += betrag
        
        print(f"{betrag}€ überwiesen von {self.inhaber} an {ziel_konto.inhaber}")
        return True
    
    def info(self):
        """
        Gibt formatierte Kontoinformationen zurück.
        """
        return f"Konto {self.kontonummer}: {self.inhaber} ({self.kontostand}€)"


# ===== PROGRAMM TESTEN =====

print("=== Bankkonten erstellen ===\n")

konto_anna = Bankkonto("Anna", 1000)
konto_ben = Bankkonto("Ben", 500)
konto_clara = Bankkonto("Clara")  # Ohne Anfangsstand

print("\n=== Anfangszustand ===\n")
konto_anna.kontostand_anzeigen()
konto_ben.kontostand_anzeigen()
konto_clara.kontostand_anzeigen()

print("\n=== Einzahlungen ===\n")
konto_anna.einzahlen(500)
konto_clara.einzahlen(200)

print("\n=== Abhebungen ===\n")
konto_ben.abheben(100)
konto_clara.abheben(50)

print("\n=== Fehlerhafte Operationen ===\n")
konto_ben.abheben(1000)  # Zu viel
konto_anna.einzahlen(-50)  # Negativ

print("\n=== Überweisungen ===\n")
konto_anna.ueberweisen(konto_ben, 300)
konto_ben.ueberweisen(konto_clara, 200)

print("\n=== Endzustand ===\n")
konto_anna.kontostand_anzeigen()
konto_ben.kontostand_anzeigen()
konto_clara.kontostand_anzeigen()

print("\n=== Alle Konten ===\n")
alle_konten = [konto_anna, konto_ben, konto_clara]
for konto in alle_konten:
    print(konto.info())

print(f"\nInsgesamt {Bankkonto.naechste_kontonummer - 1000} Konten erstellt")


# ===== ERWEITERT: KONTEN VERWALTEN =====

class Bank:
    def __init__(self, name):
        self.name = name
        self.konten = []
    
    def konto_eroeffnen(self, inhaber, anfangsstand=0):
        """
        Eröffnet ein neues Konto bei dieser Bank.
        """
        neues_konto = Bankkonto(inhaber, anfangsstand)
        self.konten.append(neues_konto)
        return neues_konto
    
    def alle_konten_anzeigen(self):
        """
        Zeigt alle Konten der Bank.
        """
        print(f"\n=== Konten bei {self.name} ===")
        if len(self.konten) == 0:
            print("Keine Konten vorhanden")
        else:
            for konto in self.konten:
                print(konto.info())
    
    def konto_finden(self, kontonummer):
        """
        Findet ein Konto anhand der Kontonummer.
        """
        for konto in self.konten:
            if konto.kontonummer == kontonummer:
                return konto
        return None
    
    def gesamteinlagen(self):
        """
        Berechnet die Summe aller Kontostände.
        """
        summe = 0
        for konto in self.konten:
            summe += konto.kontostand
        return summe


# ===== BANK-SYSTEM TESTEN =====

print("\n\n=== BANK-SYSTEM ===\n")

meine_bank = Bank("Sparkasse")

# Konten eröffnen
k1 = meine_bank.konto_eroeffnen("David", 2000)
k2 = meine_bank.konto_eroeffnen("Emma", 1500)
k3 = meine_bank.konto_eroeffnen("Felix", 3000)

# Alle Konten anzeigen
meine_bank.alle_konten_anzeigen()

# Transaktionen
print("\n=== Transaktionen ===")
k1.abheben(500)
k2.einzahlen(1000)
k1.ueberweisen(k3, 300)

# Aktueller Stand
meine_bank.alle_konten_anzeigen()

# Gesamteinlagen
print(f"\nGesamteinlagen: {meine_bank.gesamteinlagen()}€")

# Konto suchen
print("\n=== Konto suchen ===")
gesuchtes_konto = meine_bank.konto_finden(1001)
if gesuchtes_konto:
    print(f"Gefunden: {gesuchtes_konto.info()}")
else:
    print("Konto nicht gefunden")
```

**Erklärungen:**

```
1. AUTOMATISCHE KONTONUMMER:
   naechste_kontonummer = 1000
   
   self.kontonummer = Bankkonto.naechste_kontonummer
   Bankkonto.naechste_kontonummer += 1
   
   - Klassenattribut als Zähler
   - Startet bei 1000
   - Jedes Konto bekommt eindeutige Nummer
   - Automatisch hochgezählt

2. EINGABEVALIDIERUNG:
   if betrag <= 0:
       print("Fehler...")
       return False
   
   - Prüft Bedingungen
   - Gibt Fehlermeldung aus
   - return False = Operation fehlgeschlagen
   - Verhindert ungültige Zustände

3. KONTOSTAND PRÜFEN:
   if betrag > self.kontostand:
       print("Nicht genug Geld!")
       return False
   
   - Abhebung nur wenn genug Geld da
   - Verhindert negativen Kontostand
   - return False bei Fehler

4. ÜBERWEISUNG:
   self.kontostand -= betrag
   ziel_konto.kontostand += betrag
   
   - Geld vom eigenen Konto abziehen
   - Geld auf anderes Konto einzahlen
   - Zwei Objekte werden geändert
   - Methode arbeitet mit anderem Objekt

5. DOCSTRINGS:
   """
   Zahlt Geld auf das Konto ein.
   
   betrag: Einzuzahlender Betrag
   """
   
   - Dokumentation der Methode
   - Erklärt Parameter
   - Hilfreich für andere Entwickler

6. RETURN TRUE/FALSE:
   return True   # Erfolg
   return False  # Fehler
   
   - Zeigt, ob Operation erfolgreich
   - Kann vom Aufrufer geprüft werden
   - Besseres Fehler-Handling

7. BANK-KLASSE:
   - Verwaltet mehrere Konten
   - Speichert in Liste
   - Bietet Verwaltungs-Funktionen
   - Komposition: Bank hat Konten

8. KONTO_FINDEN:
   for konto in self.konten:
       if konto.kontonummer == nummer:
           return konto
   return None
   
   - Durchsucht Liste
   - Vergleicht Kontonummer
   - Gibt Konto zurück oder None

9. GESAMTEINLAGEN:
   summe = 0
   for konto in self.konten:
       summe += konto.kontostand
   return summe
   
   - Berechnung über alle Konten
   - Summiert Kontostände
   - Gibt Gesamtsumme zurück

10. REALISTISCHE STRUKTUR:
    - Fehlerbehandlung
    - Validierung
    - Objekte interagieren
    - Klassen organisieren Objekte
    - Wie echte Banking-Software (vereinfacht)
```

**Was wir gelernt haben:**

```
(OK) Automatische ID-Vergabe mit Klassenattribut
(OK) Eingabevalidierung in Methoden
(OK) Objekte können mit anderen Objekten interagieren
(OK) return True/False für Erfolg/Fehler
(OK) Verwaltungs-Klasse für mehrere Objekte
(OK) Realistische Programmstruktur
(OK) Docstrings für Dokumentation
```

</details>

---

## Zusammenfassung

### Die wichtigsten Konzepte

**1. Klasse:**
```python
class Person:
    pass
```
- Bauplan für Objekte
- Mit `class` keyword
- PascalCase für Namen

**2. Objekt/Instanz:**
```python
anna = Person()
```
- Konkretes Exemplar einer Klasse
- Mit `Klassenname()` erstellen
- Jedes Objekt ist einzigartig

**3. Konstruktor (__init__):**
```python
def __init__(self, name, alter):
    self.name = name
    self.alter = alter
```
- Wird automatisch aufgerufen
- Initialisiert Attribute
- Erster Parameter ist `self`

**4. self:**
```python
self.name
self.methode()
```
- Referenz auf aktuelles Objekt
- Pflicht in Instanzmethoden
- Zugriff auf Attribute und Methoden

**5. Attribute:**
```python
self.name = "Anna"  # Instanzattribut
Klasse.zaehler = 0  # Klassenattribut
```
- Instanzattribut: individuell pro Objekt
- Klassenattribut: geteilt von allen
- Zugriff: `objekt.attribut`

**6. Methoden:**
```python
def vorstellen(self):
    print(f"Ich bin {self.name}")
```
- Funktionen in Klassen
- Erster Parameter ist `self`
- Zugriff auf Objektdaten

### Goldene Regeln

1. **Klassennamen groß schreiben**
   ```python
   class Person:  # Richtig
   class person:  # Falsch
   ```

2. **self nie vergessen**
   ```python
   def __init__(self, name):        # Richtig
       self.name = name
   
   def __init__(name):              # Falsch
       self.name = name
   ```

3. **Attribute mit self**
   ```python
   self.name = "Anna"  # Richtig
   name = "Anna"       # Falsch (lokale Variable)
   ```

4. **self nicht beim Aufruf**
   ```python
   anna.vorstellen()      # Richtig
   anna.vorstellen(self)  # Falsch
   ```

5. **Klassenattribute über Klassenname ändern**
   ```python
   Klasse.zaehler = 10  # Richtig
   objekt.zaehler = 10  # Falsch (erstellt Instanzattribut)
   ```

### Typische Fehler

```python
# FEHLER: FEHLER 1: self vergessen
class Person:
    def __init__(name):  # Fehlt: self
        self.name = name

# (OK) RICHTIG:
class Person:
    def __init__(self, name):
        self.name = name


# FEHLER: FEHLER 2: self. vergessen
class Person:
    def __init__(self, name):
        name = name  # Lokale Variable!

# (OK) RICHTIG:
class Person:
    def __init__(self, name):
        self.name = name


# FEHLER: FEHLER 3: Methode ohne Klammern aufrufen
anna = Person("Anna")
anna.vorstellen  # Gibt Methoden-Objekt zurück

# (OK) RICHTIG:
anna.vorstellen()


# FEHLER: FEHLER 4: Klassenattribut falsch ändern
class Auto:
    anzahl = 0

a1 = Auto()
a1.anzahl = 5  # Erstellt Instanzattribut!

# (OK) RICHTIG:
Auto.anzahl = 5
```

### Wann welches Konzept?

| Situation | Lösung |
|-----------|--------|
| Daten zusammenhalten | Klasse mit Attributen |
| Daten + Verhalten | Klasse mit Methoden |
| Individueller Zustand | Instanzattribut |
| Geteilter Zustand | Klassenattribut |
| Initialisierung | `__init__` |
| Aktion ausführen | Methode |
| Eindeutige IDs | Klassenattribut als Zähler |

### Nächste Schritte

Nach diesen Grundlagen kannst du lernen:
- **Vererbung**: Klassen von anderen Klassen ableiten
- **Polymorphie**: Gleiche Methode, unterschiedliches Verhalten
- **Kapselung**: Private Attribute mit `_` oder `__`
- **Properties**: Getter und Setter mit `@property`
- **Special Methods**: `__str__`, `__repr__`, `__eq__` etc.
- **Klassenmethoden**: Mit `@classmethod`
- **Statische Methoden**: Mit `@staticmethod`

**Aber:** Beherrsche erst die Grundlagen! Alles baut darauf auf.

---

## Praktische Tipps

### Entwicklungs-Workflow

1. **Überlege die Struktur**
   - Welche Klassen brauche ich?
   - Welche Attribute hat jede Klasse?
   - Welche Methoden brauche ich?

2. **Fang einfach an**
   ```python
   class Person:
       pass
   ```

3. **Füge __init__ hinzu**
   ```python
   def __init__(self, name):
       self.name = name
   ```

4. **Teste früh und oft**
   ```python
   anna = Person("Anna")
   print(anna.name)
   ```

5. **Erweitere schrittweise**
   - Ein Attribut
   - Eine Methode
   - Testen
   - Nächstes Feature

### Professioneller Code-Aufbau

**if __name__ == "__main__":**

In Python-Dateien solltest du Testcode und Beispiele so strukturieren:

```python
# meine_klassen.py

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}!")

class Auto:
    def __init__(self, marke):
        self.marke = marke

# Dieser Code läuft nur, wenn die Datei direkt ausgeführt wird
# Nicht, wenn sie importiert wird!
if __name__ == "__main__":
    # Testcode hier
    anna = Person("Anna", 16)
    anna.vorstellen()
    
    mein_auto = Auto("VW")
    print(f"Mein Auto: {mein_auto.marke}")
```

**Warum ist das wichtig?**
- Code ist wiederverwendbar (kann importiert werden)
- Testcode läuft nicht bei Import
- Professioneller Standard
- Vermeidet ungewollte Seiteneffekte
- **So bleibt die Datei importierbar, ohne Nebenwirkungen**

**Beispiel Import:**
```python
# andere_datei.py
from meine_klassen import Person  # Testcode läuft NICHT!

ben = Person("Ben", 15)
```

### Debugging-Tipps

**Problem: AttributeError**
```python
# Fehler: 'Person' object has no attribute 'alter'
print(anna.alter)

# Lösung: Prüfen ob Attribut gesetzt wurde
if hasattr(anna, 'alter'):
    print(anna.alter)
else:
    print("Alter nicht gesetzt")
```

**Problem: self nicht verfügbar**
```python
# Fehler: name 'self' is not defined
class Person:
    def __init__(name):  # self vergessen!
        self.name = name

# Lösung: self hinzufügen
def __init__(self, name):
    self.name = name
```

**Problem: Methode gibt None zurück**
```python
def flaeche(self):
    self.breite * self.hoehe  # return vergessen!

# Lösung: return hinzufügen
def flaeche(self):
    return self.breite * self.hoehe
```

### Hilfreiche Funktionen

```python
# Typ prüfen
print(type(anna))  # <class '__main__.Person'>

# Ist Objekt eine Instanz?
print(isinstance(anna, Person))  # True

# Attribute anzeigen
print(anna.__dict__)  # {'name': 'Anna', 'alter': 16}

# Hat Objekt ein Attribut?
print(hasattr(anna, 'name'))  # True

# Attribut holen (mit Default)
alter = getattr(anna, 'alter', 0)  # 0 wenn nicht vorhanden
```

---

## Übungsideen

Übe weiter mit diesen Projekten:

### Leicht

1. **Buch-Klasse**
   - Attribute: titel, autor, seiten
   - Methoden: info(), ist_lang() (>300 Seiten)

2. **Würfel-Klasse**
   - Attribut: seiten (6, 20, etc.)
   - Methode: wuerfeln() (Zufallszahl)

3. **Haustier-Klasse**
   - Attribute: name, art, alter
   - Methoden: begruessung(), geburtstag()

### Mittel

4. **Einkaufswagen-Klasse**
   - Artikel hinzufügen/entfernen
   - Gesamtpreis berechnen
   - Anzahl Artikel

5. **Notenverwaltung-Klasse**
   - Noten hinzufügen
   - Durchschnitt berechnen
   - Beste/schlechteste Note

6. **Timer-Klasse**
   - Start, Stop, Reset
   - Vergangene Zeit anzeigen

### Schwer

7. **Bibliotheks-System**
   - Buch-Klasse
   - Bibliothek-Klasse
   - Bücher ausleihen/zurückgeben

8. **Kalender-System**
   - Termin-Klasse
   - Kalender-Klasse
   - Termine hinzufügen, suchen, löschen

9. **Mini-Spiel**
   - Spieler-Klasse
   - Monster-Klasse
   - Kampf-System

---

## Abschluss

Herzlichen Glückwunsch! Du hast die Grundlagen der objektorientierten Programmierung in Python gelernt.

**Du kannst jetzt:**
- (OK) Klassen erstellen und verstehen
- (OK) Objekte mit `__init__` initialisieren
- (OK) Attribute setzen und nutzen
- (OK) Methoden schreiben
- (OK) Mit `self` arbeiten
- (OK) Mehrere Objekte verwalten
- (OK) Klassen- vs. Instanzattribute unterscheiden

**Weiter geht's mit:**
- Vererbung (Klassen erweitern)
- Polymorphie (Methoden überschreiben)
- Properties (Getter/Setter)
- Special Methods (`__str__`, `__repr__`)

**Wichtigste Erkenntnisse:**
1. OOP organisiert Code in wiederverwendbare Bausteine
2. Klassen = Bauplan, Objekte = Produkte
3. `self` ist der Schlüssel zu allem
4. Übung macht den Meister!

Viel Erfolg beim Programmieren!
