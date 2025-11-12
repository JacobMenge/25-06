# Objektorientierte Programmierung (OOP) in Python - Vertiefung

## Übersicht

In dieser Übung lernst du:
- **Vererbung verstehen** - Was ist Vererbung und wofür braucht man es
- **Objekte erstellen** - Instanzen einer Klasse erzeugen
- **Attribute nutzen** - Daten in Objekten speichern
- **Methoden überschreiben** - Funktionen der Elternklasse überschreiben
- **super() verstehen** - Die Brücke zu Methoden oder Attributen der Elternklasse


## Übung 1: Erste Klasse erstellen

**Schwierigkeitsgrad: GRUNDLAGEN**  
**Dauer: ~10-15 Minuten**

**Aufgabe**
1. **Erstelle die Basisklasse Tier**
- Füge einen Konstruktor `__init__(self, name, alter)` hinzu.
- Füge die Methode `essen(self)` hinzu, die ausgibt: "{self.name} isst...".

2. **Erstelle die abgeleitete Klasse Hund**
- Lass Hund von Tier erben.
- Füge einen Konstruktor `__init__(self, name, alter, rasse)` hinzu.
- Rufe den Konstruktor der Basisklasse (Tier) mithilfe von `super()` auf, um name und alter zu initialisieren. Initialisiere `rasse` separat.
- Füge die Methode `bellen(self)` hinzu, die ausgibt: "{self.name} bellt: Wuff, wuff!".

***Teste die Vererbung***
1. Erstelle eine Instanz von der Klasse Tier.
- Erstelle eine Instanz: `kitty = Tier("Kitty", 3)`. 
- Rufe die Methode `essen()` auf.

2. Erstelle ein Objekt: `bello = Hund("Bello", 5, "Golden Retriever")`.
- Rufe die geerbte Methode `essen()` auf.
- Rufe die spezifische Methode `bellen()` auf.


<details> <summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python

# ===== SCHRITT 1: Basisklasse Tier =====

class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        print(f"Tier {self.name} erstellt (Basis-Init).")
    
    def essen(self):
        return f"{self.name} isst."


# ===== SCHRITT 2: Abgeleitete Klasse Hund (Spezialisierung) =====

class Hund(Tier): # <-- Vererbungssyntax: Hund erbt von Tier
    
    # Der Konstruktor der Child-Klasse überschreibt den der Basisklasse!
    def __init__(self, name, alter, rasse):
        
        # Aufruf des Konstruktors der Basisklasse (Tier)
        # Initialisiert self.name und self.alter
        super().__init__(name, alter) 
        
        # Hinzufügen des spezifischen Instanzattributs
        self.rasse = rasse
        
    def bellen(self):
        # Nutzt geerbtes self.name
        return f"{self.name} bellt: Wuff, wuff!"


# ===== SCHRITT 3: Instanz erstellen =====

kitty = Tier("Kitty", 3)

# Methode der Basisklasse
print(kitty.essen())


# ===== SCHRITT 4: Test der Vererbung =====

bello = Hund("Bello", 5, "Golden Retriever")

print("\n--- Methoden-Test ---")
# Geerbte Methode der Basisklasse Tier
print(bello.essen()) 

# Spezifische Methode der Child-Klasse Hund
print(bello.bellen())

# Geerbtes Attribut
print(f"Bello's Alter: {bello.alter}")

```

Erklärungen:

1. VERERBUNGSSYNTAX:
   - `class Hund(Tier):` definiert `Hund` als Child-Klasse von `Tier`.
   
2. SUPER()-AUFRUF:
   - Wenn eine Child-Klasse einen eigenen `__init__` hat, muss sie explizit `super().__init__(...)` aufrufen.
   - Wenn das `super()` fehlt, werden die Attribute der Basisklasse (`name`, `alter`) nicht initialisiert!
   
3. INSTANZATTRIBUT-INITIALISIERUNG:
   - Die Initialisierung von geerbten Attributen (`name`, `alter`) übernimmt `super()`.
   - Spezifische Attribute (`rasse`) müssen separat mit `self.rasse = rasse` initialisiert werden (Spezialisierung).
   
Was wir gelernt haben:
```
(OK) Klassen können von anderen Klassen erben (`class Child(Parent):`)
(OK) Child-Klassen erben Methoden und Attribute der Basisklasse
(OK) `super().__init__()` wird verwendet, um geerbte Attribute zu initialisieren
(OK) `super()` ruft Methoden der Elternklasse auf
```
</details>



## Übung 2: Methoden überschreiben

**Schwierigkeitsgrad: Mittel**  
**Dauer: ~20-25 Minuten**

**Aufgabe**

1. **Erstelle die Basisklasse Fahrzeug**
   
Die Klasse hat:
- Konstruktor `__init__(self, marke, geschwindigkeit)`
- Methode `info(self):`: Gibt "{self.marke} fährt mit {self.geschwindigkeit} km/h." aus

2. **Erstelle die abgeleitete Klasse Auto**
- Lass Auto von Fahrzeug erben.
- Konstruktor der Klasse Auto: `__init__(self, marke, geschwindigkeit, ps)`
- Im Konstruktor rufe `super().__init__` auf

3. **Überschreibe die Methode info()**
Implementiere in der Klasse Auto die Methode `info(self)` neu.
Die neue Methode soll:
- Die ursprüngliche Ausgabe der Elternklasse (über `super().info()`) ausgeben.
- Zusätzlich ausgeben: "(Hat {self.ps} PS)".

4. **Teste das Überschreiben**
- Erstelle eine Instanz für ein Fahrzeug
- Erstelle eine Instanz für ein Auto
- Rufe jeweils die Methode `fahren()` einmal für das Fahrzeug und einmal für das Auto auf. Vergleiche die Ausgabe.

<details> <summary>Schritt-für-Schritt Lösung anzeigen</summary>

```python

# ===== SCHRITT 1: Basisklasse Fahrzeug =====

class Fahrzeug:
    def __init__(self, marke, geschwindigkeit):
        self.marke = marke
        self.geschwindigkeit = geschwindigkeit
    
    def info(self):
        # Basis-Implementierung
        print("{self.marke} fährt mit {self.geschwindigkeit} km/h.")


# ===== SCHRITT 2 & 3: Abgeleitete Klasse Auto mit Überschreiben =====

class Auto(Fahrzeug):
    def __init__(self, marke, geschwindigkeit, ps):
        # 1. Basis-Initialisierung aufrufen
        super().__init__(marke, geschwindigkeit) 
        
        # 2. Spezifisches Attribut hinzufügen
        self.ps = ps
        
    # !!! ÜBERSCHREIBEN der Methode info() der Basisklasse !!!
    def info(self):
        # 1. Ursprüngliche Implementierung der Basisklasse abrufen
        super().info()
        
        # 2. Spezialisierte Logik hinzufügen (Spezialisierung/Erweiterung)
        print("(Hat {self.ps} PS)")
        


# ===== SCHRITT 4: Testen des Überschreibens =====

f1 = Fahrzeug("Fahrrad", 20)
a1 = Auto("VW Golf", 180, 150)

print("--- Fahrzeug-Test (Basis) ---")
# Ruft Fahrzeug.info() auf
f1.info()

print("\n--- Auto-Test (Spezialisierung/Erweiterung) ---")
# Ruft Auto.info() auf (da überschrieben)
a1.info()
```

Erklärungen:

1. METHODENÜBERSCHREIBEN (OVERRIDING):
   - `def info(self):` in `Auto` ersetzt `def info(self):` in `Fahrzeug` für alle `Auto`-Objekte.
   
2. ERWEITERUNG MIT SUPER():
   - Durch `basis_info = super().info()` wird explizit die Methode der Elternklasse abgerufen.
   - Dies ermöglicht es der Kindklasse, die Funktionalität der Elternklasse zu **erweitern** (hier: PS hinzufügen), anstatt sie komplett zu ersetzen.
   - Ohne `super().info()` würde die `Auto.info()` die Informationen zu Marke und Geschwindigkeit neu implementieren müssen (was fehleranfällig ist).
   

Was wir gelernt haben:
```
(OK) Methodenüberschreiben ersetzt die Funktionalität der Basisklasse für die Child-Klasse
(OK) `super().methode()` ruft die überschriebene Methode der Elternklasse auf
(OK) Man kann Basis-Funktionalität mit spezifischer Logik in der Child-Klasse kombinieren (Erweiterung)
```
</details>


## Übung 2: Mitarbeiter-System (Generalisierung)

**Schwierigkeitsgrad: Fortgeschritten**  
**Dauer: ~30-40 Minuten**

**Aufgabe**
Im Folgenden finden ihr zwei Klassen, Angestellter und Manager, die viele redundante Attribute enthalten. Das Ziel ist es, diese Klassen zu generalisieren.

1. **Analysiere die Redundanz**
- Betrachte die Klassen `Angestellter` und `Manager`.

2. **Erstelle die Basisklasse Mitarbeiter (Generalisierung)**
- Definiere die gemeinsamen Attribute in einem Konstruktor.
- Füge die gemeinsame Methode `info(self)` hinzu, die Name und Gehalt ausgibt.

3. **Passe die Child-Klassen an (Spezialisierung)**
- Lasse Angestellter und Manager von Mitarbeiter erben.
- Passe ihre Konstruktoren an, indem du `super()` für die gemeinsamen Attribute verwendest.
- Füge die spezifischen Attribute hinzu.

4. **Überschreibe die info()-Methode in Manager**
- Die Manager.info()-Methode soll die allgemeine Mitarbeiter.info()-Ausgabe verwenden (`super().info()`) und den spezifischen Bonus ergänzen.

```python
class Angestellter:
     def __init__(self, name, gehalt, arbeitsstunden):
         self.name = name
         self.gehalt = gehalt
         self.arbeitsstunden = arbeitsstunden

class Manager:
     def __init__(self, name, gehalt, abteilung, bonus):
         self.name = name
         self.gehalt = gehalt
         self.abteilung = abteilung
         self.bonus = bonus
```

<details> <summary>Vollständige Lösung anzeigen</summary>

```python

# ===== SCHRITT 1: Redundante Ursprungsklassen (Analyse) =====
# class Angestellter:
#     def __init__(self, name, gehalt, arbeitsstunden):
#         self.name = name
#         self.gehalt = gehalt
#         self.arbeitsstunden = arbeitsstunden
        
# class Manager:
#     def __init__(self, name, gehalt, abteilung, bonus):
#         self.name = name
#         self.gehalt = gehalt
#         self.abteilung = abteilung
#         self.bonus = bonus

# Fazit: 'name' und 'gehalt' sind redundant!


# ===== SCHRITT 2: Basisklasse Mitarbeiter (Generalisierung) =====

class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt
        
    def info(self):
        # Allgemeine Info-Methode
        return f"Mitarbeiter: {self.name}, Gehalt: {self.gehalt:.2f}€"


# ===== SCHRITT 3: Child-Klassen (Spezialisierung) =====

class Angestellter(Mitarbeiter):
    def __init__(self, name, gehalt, arbeitsstunden):
        # 1. Basis-Initialisierung (Generalisierung)
        super().__init__(name, gehalt)
        
        # 2. Spezifische Attribute (Spezialisierung)
        self.arbeitsstunden = arbeitsstunden
        
    def info(self):
        # Einfache Erweiterung der Basis-Info
        basis_info = super().info()
        return f"{basis_info}, Stunden: {self.arbeitsstunden}"


class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, abteilung, bonus):
        # 1. Basis-Initialisierung
        super().__init__(name, gehalt)
        
        # 2. Spezifische Attribute
        self.abteilung = abteilung
        self.bonus = bonus
        
    # SCHRITT 4: info() Methode überschreiben und erweitern 
    def info(self):
        # 1. Basis-Info abrufen
        basis_info = super().info()
        
        # 2. Spezifische Info hinzufügen
        gesamt_gehalt = self.gehalt + self.bonus
        return f"Manager: {basis_info} (+Bonus: {self.bonus:.2f}€ in {self.abteilung}). Gesamt: {gesamt_gehalt:.2f}€"


# ===== PROGRAMM TESTEN =====

if __name__ == "__main__":
    print("--- Generalisierte Mitarbeiter-Klassen ---")

    # Objekte erstellen
    a1 = Angestellter("Ben Schmidt", 40000.00, 40)
    m1 = Manager("Anna Müller", 70000.00, "Vertrieb", 5000.00)

    print("\n--- Info-Ausgabe ---")
    
    # Ruft Angestellter.info() auf, die Mitarbeiter.info() nutzt
    print(a1.info()) 
    
    # Ruft die überschriebene und erweiterte Manager.info() auf
    print(m1.info()) 

    print("\n--- Typ-Check (Polymorphie-Basis) ---")
    alle_mitarbeiter = [a1, m1]
    
    for ma in alle_mitarbeiter:
        # Hier wird jeweils die korrekte, spezialisierte info()-Methode aufgerufen!
        print(f"[{ma.__class__.__name__}]: {ma.info()}")
        
        # Prüfung auf die Basisklasse
        print(f"Ist Mitarbeiter? {isinstance(ma, Mitarbeiter)}")
```

Erklärungen:

1. CODE-WIEDERVERWENDUNG (GENERALISIERUNG):
   - Durch das Herauslösen von `name` und `gehalt` in `Mitarbeiter` musste der Code nur einmal implementiert werden.
   - Alle Child-Klassen (`Angestellter`, `Manager`) erben diese Logik.
   
2. SPEZIALISIERUNG:
   - Jede Child-Klasse (`Angestellter`, `Manager`) fügt ihre **einzigartigen** Attribute hinzu (`arbeitsstunden`, `bonus`, `abteilung`).
   - Die `info()`-Methode des `Manager` wird überschrieben und um die Bonus-Berechnung spezialisiert.
   
3. POLYMORPHIE (Grundlage):
   - Im letzten Test durchläuft die Schleife Objekte unterschiedlichen Typs (`Angestellter` und `Manager`), ruft aber die gleichnamige Methode `info()` auf.
   - Python ruft automatisch die **korrekte, spezialisierte Version** der Methode für das jeweilige Objekt auf. Das ist Polymorphie.
Was wir gelernt haben:
```
(OK) Generalisierung führt zu Code-Wiederverwendung und besserer Struktur
(OK) Spezialisierung fügt einzigartige Attribute und überschriebene Methoden hinzu
(OK) `super()` ist essentiell, um die Vererbungsbeziehung beim Konstruieren und in Methoden zu erhalten
(OK) Polymorphie ermöglicht es, spezialisierte Objekte in einer gemeinsamen Liste zu verwalten und auf die richtige Methode zuzugreifen
```
</details>

### Selbstcheck: OOP Vertiefung
1. Was ist der Unterschied zwischen Generalisierung und Spezialisierung bei der Vererbung?

2. Warum ist es in einer Child-Klasse, die einen eigenen `__init__ hat`, wichtig, `super().__init__(...)` aufzurufen?

3. Wie kann man verhindern, dass beim Überschreiben einer Methode die ursprüngliche Funktionalität der Basisklasse verloren geht?

Geben Sie die Python-Syntax für Vererbung an, bei der LKW von Fahrzeug erbt.

<details> <summary>Antworten anzeigen</summary>

1. Generalisierung ist der Prozess, gemeinsame Eigenschaften in eine neue, allgemeinere Basisklasse zu verschieben (Hierarchie nach oben). Spezialisierung ist das Hinzufügen spezifischer Attribute oder das Überschreiben von Methoden in einer abgeleiteten Child-Klasse (Hierarchie nach unten).

2. Weil der `__init__` der Child-Klasse den der Basisklasse ersetzt. Ohne den Aufruf von `super().__init__(...)` würden die geerbten Attribute (z.B. `name`, `alter`) nicht initialisiert.

3. Indem man innerhalb der überschriebenen Methode die ursprüngliche Methode über `super().methode_name(...)` aufruft und die Rückgabe oder den Effekt zur eigenen Logik hinzufügt.



</details>
