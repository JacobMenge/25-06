# JSON mit Python - Dokumente speichern und verwalten

## Übersicht

In dieser Übung lernst du:
- **JSON-Format verstehen** - Dokumentenstruktur und Datentypen
- **JSON-Dateien lesen** - json.load() nutzen
- **JSON-Dateien schreiben** - json.dump() nutzen
- **Daten bearbeiten** - CRUD-Operationen (Create, Read, Update, Delete)
- **Python ↔ JSON Mapping** - Wie dict/list zu JSON werden
- **Praktisch arbeiten** - Eigene Bücherverwaltung mit JSON-Dateien

**Voraussetzung:** Du solltest Python-Grundlagen kennen (Datentypen, Listen, Dictionaries, Schleifen)

**Wichtig:** Wir arbeiten mit **JSON-Dateien**, nicht mit NoSQL-Datenbanken! Eine JSON-Datei ist einfacher Text auf der Festplatte - keine Datenbank mit Server, Indizes oder Transaktionen.

---

## Lernziele

**HAUPTZIEL: Dokumente mit JSON-Dateien verwalten**
- JSON-Format verstehen und nutzen
- Dokumente laden und speichern
- CRUD-Operationen umsetzen
- Grenzen von JSON-Dateien kennen

**DOKUMENTENPRINZIP VERSTEHEN:**
- Unterschied zu relationalen Tabellen
- Vorteile flexibler Strukturen
- Wann JSON-Dateien sinnvoll sind
- Abgrenzung zu echten Dokumenten-Datenbanken (MongoDB etc.)

---

## Aufbau der Übung

### TEIL 1: JSON-Grundlagen 
- Was ist JSON?
- Python ↔ JSON Mapping
- JSON ist nur Text!

### TEIL 2: JSON laden und speichern 
- json.load() und json.dump()
- Hilfsfunktionen erstellen
- Grundablauf ohne Fehlerbehandlung

### TEIL 3: CRUD-Operationen 
- CREATE: Dokument hinzufügen
- READ: Dokument suchen
- UPDATE: Dokument ändern
- DELETE: Dokument löschen

### TEIL 4: Praktisches Mini-Projekt 
- Einfache Bücherverwaltung
- Menü mit Grundfunktionen

### ZUSATZAUFGABEN 
- Erweiterte Funktionen
- Export, Sortierung, Statistik

---

## Wichtig: Arbeitsweise mit JSON-Dateien

**In dieser Übung nutzen wir eine einzige Datei:**

```
bibliothek.json
```

Alle Beispiele und Übungen arbeiten mit dieser Datei. Das verhindert Verwirrung und ist näher an der Praxis (eine Anwendung = eine Datendatei).

---

## Teil 1: JSON-Grundlagen

### Was ist JSON?

**JSON** = **J**ava**S**cript **O**bject **N**otation

**Was es ist:**
- Ein **Textformat** für strukturierte Daten
- Ähnlich wie ein Python-Dictionary
- Menschen- und maschinenlesbar
- Standardformat für Datenaustausch

**Was es NICHT ist:**
- Keine Datenbank
- Kein Server
- Kein DBMS (Database Management System)

**Vergleich:**
- **SQL-Datenbank:** Tabellen mit festen Spalten, Server, Indizes, Transaktionen
- **JSON-Datei:** Textdatei auf der Festplatte, flexibel, einfach
- **NoSQL-Datenbank (z.B. MongoDB):** Dokumentenbasiert, aber mit Server, Indizes, Queries

#### JSON-Struktur

**Ein einfaches JSON-Dokument:**

```json
{
  "name": "Python Crashkurs",
  "autor": "Eric Matthes",
  "seiten": 688,
  "gelesen": false,
  "tags": ["Python", "Programmierung", "Anfänger"]
}
```

**JSON kennt diese Datentypen:**
- `"text"` - String (Text)
- `123` - Number (Zahl)
- `true` / `false` - Boolean (Wahrheitswert)
- `null` - null (entspricht None in Python)
- `[...]` - Array (Liste)
- `{...}` - Object (Dictionary)

---

### Python ↔ JSON Mapping

**Beim Laden (JSON → Python):**

| JSON | Python |
|------|--------|
| `{"key": "value"}` | `dict` |
| `[1, 2, 3]` | `list` |
| `"text"` | `str` |
| `123` | `int` |
| `12.5` | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

**Beim Speichern (Python → JSON):**

| Python | JSON |
|--------|------|
| `dict` | `{"key": "value"}` |
| `list` / `tuple` | `[1, 2, 3]` |
| `str` | `"text"` |
| `int` / `float` | `123` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

### JSON ist nur Text!

**Wichtig zu verstehen:**

```python
# Eine JSON-Datei ist nur Text:
# bibliothek.json enthält z.B.:
# [{"id": 1, "titel": "Test"}]

# Wenn du die Datei öffnest:
buecher = json.load(f)
# wird der TEXT geparst und zu Python-Objekten (list, dict)

# Wenn du Änderungen machst:
buecher.append({"id": 2, "titel": "Neu"})
# ist das nur im RAM! Die Datei ist NICHT automatisch aktualisiert.

# Erst beim Speichern:
json.dump(buecher, f)
# werden die Python-Objekte wieder zu TEXT und in die Datei geschrieben
```

**Das bedeutet:**
- Keine "Live-Verbindung" zur Datei
- Änderungen müssen explizit gespeichert werden
- Bei jedem Laden wird die ganze Datei neu eingelesen
- Bei jedem Speichern wird die ganze Datei neu geschrieben

#### Übung 1: Erste JSON-Datei erstellen

**Aufgabe:**

Erstelle eine JSON-Datei namens `bibliothek.json` mit zwei Büchern:

1. "Python Crashkurs" von Eric Matthes (2019, nicht gelesen)
2. "Automate the Boring Stuff" von Al Sweigart (2020, gelesen)

Jedes Buch soll folgende Felder haben: id, titel, autor, jahr, gelesen

**Hinweise:**
- JSON nutzt eckige Klammern `[]` für Listen
- JSON nutzt geschweifte Klammern `{}` für Objekte
- Strings in doppelten Anführungszeichen `"..."`
- Boolean-Werte: `true` oder `false` (kleingeschrieben!)

<details>
<summary>Lösung anzeigen</summary>

```json
[
  {
    "id": 1,
    "titel": "Python Crashkurs",
    "autor": "Eric Matthes",
    "jahr": 2019,
    "gelesen": false
  },
  {
    "id": 2,
    "titel": "Automate the Boring Stuff",
    "autor": "Al Sweigart",
    "jahr": 2020,
    "gelesen": true
  }
]
```

**Erklärung:**
- `[...]` = Liste von Dokumenten (Array)
- Jedes `{...}` ist ein Buch-Dokument (Object)
- Komma zwischen den Objekten, aber NICHT nach dem letzten
- `false` und `true` kleingeschrieben (nicht `False`/`True` wie in Python!)
- Jedes Buch hat die gleichen Felder - muss aber nicht sein!

</details>

<details>
<summary>JSON-Format verstehen</summary>

**Wichtige Regeln:**
- Strings immer in `"doppelten Anführungszeichen"`
- Keine einfachen Anführungszeichen `'...'` wie in Python!
- Kein Komma nach dem letzten Element
- Einrückung ist optional, macht aber lesbarer

**Gültig:**
```json
{"name": "Test", "wert": 123}
```

**Ungültig:**
```json
{'name': 'Test', 'wert': 123,}  # Falsche Anführungszeichen, Komma am Ende
```

</details>

---

### Lernziel-Check Teil 1

Bevor du weiter machst, teste dein Verständnis:

1. **Was ist der Unterschied zwischen einer JSON-Datei und einer NoSQL-Datenbank wie MongoDB?**
   <details>
   <summary>Antwort anzeigen</summary>
   Eine JSON-Datei ist nur Text auf der Festplatte. MongoDB ist eine Datenbank mit Server, Indizes, Transaktionen und Query-Sprache. JSON-Dateien sind einfacher, aber langsamer und weniger leistungsfähig.
   </details>

2. **Welche Python-Typen bekommst du nach `json.load()`?**
   <details>
   <summary>Antwort anzeigen</summary>
   Typischerweise `list` (für JSON-Array) oder `dict` (für JSON-Object), mit `str`, `int`, `float`, `bool`, `None` als Werte darin.
   </details>

3. **Warum müssen Änderungen explizit gespeichert werden?**
   <details>
   <summary>Antwort anzeigen</summary>
   Weil JSON-Dateien nur Text sind. Nach `json.load()` arbeitet Python mit Kopien im RAM. Die Datei selbst ändert sich nicht, bis `json.dump()` aufgerufen wird.
   </details>

---

## Teil 2: JSON laden und speichern

### HINWEIS: Fehlerbehandlung kommt später

**Heute konzentrieren wir uns auf den Grundablauf:**

```
laden → ändern → speichern
```

Wir gehen heute davon aus, dass `bibliothek.json` existiert und gültiges JSON enthält.

**Morgen lernen wir dann:**
- `try/except` für Fehlerbehandlung
- `FileNotFoundError` wenn Datei nicht existiert
- `json.JSONDecodeError` bei ungültigem JSON
- `ValueError` bei ungültigen Eingaben

**Heute bleiben wir beim Happy Path (alles läuft glatt)!**

---

### Hilfsfunktionen erstellen (Version 1 - heute)

**Wichtig:** Wir erstellen EINMAL zwei zentrale Funktionen und nutzen diese dann überall. Das verhindert Code-Duplikate und Fehler.

**Datei:** `json_helper.py` (Version 1 - heute ohne Fehlerbehandlung)

```python
import json

DATEI = "bibliothek.json"

def lade_buecher():
    """
    Lädt Bücher aus bibliothek.json
    
    Heute: ohne Fehlerbehandlung (try/except kommt morgen)
    Voraussetzung: bibliothek.json existiert und enthält gültiges JSON
    
    Returns:
        list: Liste von Buch-Dictionaries
    """
    with open(DATEI, "r", encoding="utf-8") as f:
        buecher = json.load(f)
    
    # Mini-Check: JSON muss eine Liste sein
    if not isinstance(buecher, list):
        raise TypeError("bibliothek.json muss ein JSON-Array (Liste) enthalten!")
    
    return buecher

def speichere_buecher(buecher):
    """
    Speichert Bücher in bibliothek.json
    
    Args:
        buecher (list): Liste von Buch-Dictionaries
    """
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(buecher, f, ensure_ascii=False, indent=2)

def naechste_id(buecher):
    """
    Ermittelt die nächste freie ID
    
    Args:
        buecher (list): Liste von Buch-Dictionaries
    
    Returns:
        int: Nächste freie ID
    """
    if not buecher:
        return 1
    return max(buch["id"] for buch in buecher) + 1
```

**Diese Funktionen nutzen wir ab jetzt in ALLEN folgenden Beispielen!**

<details>
<summary>Warum ensure_ascii=False und indent=2?</summary>

**ensure_ascii=False**
- Ohne: `"München"` wird zu `"\u00fcnchen"`
- Mit: `"München"` bleibt `"München"`
- Wichtig für deutsche Texte!

**indent=2**
- Ohne: `[{"id":1,"titel":"Test"},{"id":2,"titel":"Noch ein Test"}]` (eine Zeile, unleserlich)
- Mit: Schön formatiert mit Einrückungen
- Macht JSON für Menschen lesbar

</details>

<details>
<summary>Ausblick: Version 2 - morgen mit Fehlerbehandlung</summary>

**Morgen werden wir `json_helper.py` erweitern:**

```python
import json

DATEI = "bibliothek.json"

def lade_buecher():
    """
    Lädt Bücher aus bibliothek.json
    
    Version 2 - morgen mit Fehlerbehandlung
    """
    try:
        with open(DATEI, "r", encoding="utf-8") as f:
            buecher = json.load(f)
        
        if not isinstance(buecher, list):
            print("WARNUNG: JSON muss eine Liste (Array) sein -> starte leer")
            return []
        
        return buecher
    
    except FileNotFoundError:
        print("INFO: Datei existiert noch nicht -> starte mit leerer Liste")
        return []
    
    except json.JSONDecodeError:
        print("WARNUNG: Ungültiges JSON -> starte mit leerer Liste")
        return []

def speichere_buecher(buecher):
    """Speichert Bücher in bibliothek.json"""
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(buecher, f, ensure_ascii=False, indent=2)
```

**Das lernen wir morgen!**

</details>

---

#### Übung 2: Hilfsfunktionen nutzen

**Aufgabe:**

Erstelle ein Programm `json_lesen.py`, das:
1. Die Hilfsfunktion `lade_buecher()` importiert
2. Alle Bücher lädt
3. Den Typ und die Anzahl ausgibt
4. Alle Bücher in einer Schleife durchgeht und formatiert ausgibt (Status, Titel, Autor)

**Hinweise:**
- Nutze `from json_helper import lade_buecher`
- Für den Status: `[X]` wenn gelesen, `[ ]` wenn nicht gelesen
- Nutze einen f-String für die Formatierung

<details>
<summary>Lösung anzeigen</summary>

```python
from json_helper import lade_buecher

# Bücher laden
buecher = lade_buecher()

# Ausgeben
print(f"Typ: {type(buecher)}")  # <class 'list'>
print(f"Anzahl Bücher: {len(buecher)}")

# Alle Bücher durchgehen
print("\nAlle Bücher:")
for buch in buecher:
    status = "[X] gelesen" if buch["gelesen"] else "[ ] ungelesen"
    print(f"{status} - {buch['titel']} von {buch['autor']}")
```

**Erklärung:**
- `lade_buecher()` gibt eine Liste zurück
- `type(buecher)` zeigt `<class 'list'>`
- Jedes Buch in der Liste ist ein Dictionary
- Zugriff mit `buch["titel"]`, `buch["autor"]` etc.
- Ternärer Operator für Status: `wert_wenn_true if bedingung else wert_wenn_false`

**Ausgabe:**
```
Typ: <class 'list'>
Anzahl Bücher: 2

Alle Bücher:
[ ] ungelesen - Python Crashkurs von Eric Matthes
[X] gelesen - Automate the Boring Stuff von Al Sweigart
```

</details>

---

### json.dumps() und json.loads() - String statt Datei

**Zusätzlich gibt es:**

```python
import json

# Python → JSON-String (kein File)
buch = {"id": 1, "titel": "Test"}
json_string = json.dumps(buch, ensure_ascii=False, indent=2)
print(json_string)
# Ausgabe: 
# {
#   "id": 1,
#   "titel": "Test"
# }

# JSON-String → Python (kein File)
json_string = '{"id": 1, "titel": "Test"}'
buch = json.loads(json_string)
print(buch["titel"])  # Test
```

**Merkregel:**
- `dump` / `load` = **Datei** (File)
- `dumps` / `loads` = **String** (das "s" steht für "string")

**Wann braucht man das?**
- APIs: JSON kommt oft als String (HTTP Response)
- Debugging: Schnell mal Python-Objekt als JSON anzeigen
- Konfiguration: JSON-String in Variable speichern

---

### Lernziel-Check Teil 2

1. **Warum erstellen wir `json_helper.py` mit zentralen Funktionen?**
   <details>
   <summary>Antwort anzeigen</summary>
   Um Code-Duplikate zu vermeiden. Wenn wir die Funktionen überall kopieren, müssen wir bei Änderungen (z.B. anderer Dateiname) jeden Code ändern. Mit Hilfsfunktionen ändern wir nur an einer Stelle.
   </details>

2. **Warum nutzen wir heute KEINE Fehlerbehandlung?**
   <details>
   <summary>Antwort anzeigen</summary>
   Um den Fokus auf den Grundablauf zu legen: laden → ändern → speichern. Fehlerbehandlung mit try/except ist ein eigenes Thema, das morgen kommt.
   </details>

3. **Was ist der Unterschied zwischen `json.dump()` und `json.dumps()`?**
   <details>
   <summary>Antwort anzeigen</summary>
   `dump()` schreibt in eine Datei, `dumps()` gibt einen String zurück. Das "s" steht für "string".
   </details>

---

## Teil 3: CRUD-Operationen

**CRUD** = **C**reate, **R**ead, **U**pdate, **D**elete

**Workflow bei JSON-Dateien:**

```
1. Datei laden        → buecher = lade_buecher()
2. In Python ändern   → buecher.append(...) / buecher[0]["feld"] = ...
3. Datei speichern    → speichere_buecher(buecher)
```

**WICHTIG: Ohne Schritt 3 sind Änderungen beim nächsten Programmstart weg!**

---

### CREATE: Dokument hinzufügen

#### Übung 3: Neues Buch hinzufügen

**Aufgabe:**

Erstelle ein Programm `buch_hinzufuegen.py`, das:
1. Die bestehenden Bücher lädt
2. Ein neues Buch erstellt: "Learning Python" von Mark Lutz (2013, nicht gelesen)
3. Die ID automatisch vergibt (nutze `naechste_id()`)
4. Das Buch zur Liste hinzufügt
5. Die Liste speichert
6. Statusmeldungen ausgibt (vorher/nachher Anzahl, welches Buch mit welcher ID)

**Hinweise:**
- Importiere alle drei Hilfsfunktionen: `lade_buecher`, `speichere_buecher`, `naechste_id`
- Nutze `append()` um das Buch zur Liste hinzuzufügen
- Vergiss nicht zu speichern!

<details>
<summary>Lösung anzeigen</summary>

```python
from json_helper import lade_buecher, speichere_buecher, naechste_id

# 1. Laden
buecher = lade_buecher()
print(f"Aktuell {len(buecher)} Bücher vorhanden")

# 2. Neues Buch erstellen
neues_buch = {
    "id": naechste_id(buecher),  # Automatische ID!
    "titel": "Learning Python",
    "autor": "Mark Lutz",
    "jahr": 2013,
    "gelesen": False
}

# 3. Hinzufügen
buecher.append(neues_buch)
print(f"Buch '{neues_buch['titel']}' hinzugefügt (ID: {neues_buch['id']})")

# 4. Speichern (WICHTIG!)
speichere_buecher(buecher)
print(f"[OK] Änderungen gespeichert - jetzt {len(buecher)} Bücher")
```

**Erklärung:**
- `naechste_id(buecher)` findet automatisch die nächste freie ID (höchste ID + 1)
- `buecher.append(neues_buch)` fügt das Buch zur Liste hinzu (nur im RAM!)
- `speichere_buecher(buecher)` schreibt die komplette Liste zurück in die Datei
- **WICHTIG:** Ohne `speichere_buecher()` ist die Änderung beim nächsten Start weg!

**Ausgabe:**
```
Aktuell 2 Bücher vorhanden
Buch 'Learning Python' hinzugefügt (ID: 3)
[OK] Änderungen gespeichert - jetzt 3 Bücher
```

**Prüfen:**
Öffne `bibliothek.json` - es sollten jetzt 3 Bücher drin sein!

</details>

---

### READ: Dokument suchen

#### Übung 4: Buch nach Titel suchen

**Aufgabe:**

Erstelle ein Programm `buch_suchen.py` mit einer Suchfunktion:

1. Schreibe eine Funktion `suche_buch_nach_titel(buecher, suchbegriff)`, die:
   - Eine Liste von Büchern durchsucht
   - Alle Bücher zurückgibt, die den Suchbegriff im Titel enthalten
   - Groß-/Kleinschreibung ignoriert (case-insensitive)
   - Leere Suchbegriffe abfängt (gibt leere Liste zurück)

2. Lade die Bücher
3. Suche nach "Python"
4. Gib die Ergebnisse formatiert aus (ID, Titel, Autor, Jahr)

**Hinweise:**
- Nutze `.lower()` für case-insensitive Vergleich
- Nutze `in` Operator: `"abc" in "abcdef"` → True
- Nutze `.strip()` um Leerzeichen am Anfang/Ende zu entfernen

<details>
<summary>Lösung anzeigen</summary>

```python
from json_helper import lade_buecher

def suche_buch_nach_titel(buecher, suchbegriff):
    """
    Sucht Bücher nach Titel (Teilstring-Suche, case-insensitive)
    
    Args:
        buecher (list): Liste von Buch-Dictionaries
        suchbegriff (str): Suchbegriff
    
    Returns:
        list: Gefundene Bücher
    """
    # Leeren Suchbegriff abfangen
    if not suchbegriff or not suchbegriff.strip():
        return []
    
    gefunden = []
    suchbegriff = suchbegriff.lower()
    
    for buch in buecher:
        if suchbegriff in buch["titel"].lower():
            gefunden.append(buch)
    
    return gefunden

# Laden
buecher = lade_buecher()

# Suchen
suchbegriff = "Python"
ergebnisse = suche_buch_nach_titel(buecher, suchbegriff)

# Ausgeben
print(f"Suche nach '{suchbegriff}':")
print(f"-> {len(ergebnisse)} Buch/Bücher gefunden\n")

if ergebnisse:
    for buch in ergebnisse:
        print(f"[{buch['id']}] {buch['titel']}")
        print(f"     Autor: {buch['autor']}")
        print(f"     Jahr: {buch['jahr']}")
        print()
else:
    print("Keine Bücher gefunden.")
```

**Erklärung:**
- `suchbegriff.strip()` entfernt Leerzeichen: `"  test  "` → `"test"`
- `if not suchbegriff` prüft auf leeren String oder None
- `.lower()` für beide Strings: "Python" und "python" werden gefunden
- `in` prüft Teilstring: "Python" in "Learning Python" → True
- `append()` fügt gefundenes Buch zur Ergebnisliste hinzu

**Ausgabe:**
```
Suche nach 'Python':
-> 2 Buch/Bücher gefunden

[1] Python Crashkurs
     Autor: Eric Matthes
     Jahr: 2019

[3] Learning Python
     Autor: Mark Lutz
     Jahr: 2013
```

**Alternative (kompakter):**
```python
def suche_buch_nach_titel(buecher, suchbegriff):
    if not suchbegriff or not suchbegriff.strip():
        return []
    suchbegriff = suchbegriff.lower()
    return [b for b in buecher if suchbegriff in b["titel"].lower()]
```

</details>

<details>
<summary>Hilfsfunktion: Nach ID suchen</summary>

**Für exakte ID-Suche:**

```python
def finde_buch_nach_id(buecher, buch_id):
    """Findet ein Buch anhand seiner ID"""
    for buch in buecher:
        if buch["id"] == buch_id:
            return buch
    return None

# Nutzen:
buch = finde_buch_nach_id(buecher, 2)
if buch:
    print(f"Gefunden: {buch['titel']}")
else:
    print("Buch nicht gefunden")
```

Diese Funktion werden wir später oft brauchen!

</details>

---

### UPDATE: Dokument ändern

#### Übung 5: Buch als gelesen markieren

**Aufgabe:**

Erstelle ein Programm `buch_aktualisieren.py`:

1. Schreibe eine Funktion `markiere_als_gelesen(buecher, buch_id)`, die:
   - Ein Buch anhand der ID sucht
   - Das Feld `gelesen` auf `True` setzt
   - `True` zurückgibt wenn erfolgreich, `False` wenn ID nicht gefunden

2. Lade die Bücher
3. Markiere Buch mit ID 1 als gelesen
4. Speichere die Änderungen
5. Gib eine Erfolgsmeldung aus (oder Fehlermeldung wenn ID nicht existiert)

**Hinweise:**
- Durchlaufe die Liste mit einer Schleife
- Vergleiche `buch["id"]` mit der gesuchten ID
- Vergiss nicht zu speichern!

<details>
<summary>Lösung anzeigen</summary>

```python
from json_helper import lade_buecher, speichere_buecher

def markiere_als_gelesen(buecher, buch_id):
    """
    Markiert ein Buch als gelesen
    
    Args:
        buecher (list): Liste von Buch-Dictionaries
        buch_id (int): ID des Buchs
    
    Returns:
        bool: True wenn gefunden, False sonst
    """
    for buch in buecher:
        if buch["id"] == buch_id:
            buch["gelesen"] = True
            return True
    return False

# Laden
buecher = lade_buecher()

# Aktualisieren
buch_id = 1
erfolg = markiere_als_gelesen(buecher, buch_id)

if erfolg:
    # Speichern (WICHTIG!)
    speichere_buecher(buecher)
    print(f"[OK] Buch mit ID {buch_id} als gelesen markiert")
else:
    print(f"[FEHLER] Buch mit ID {buch_id} nicht gefunden")
```

**Erklärung:**
- Wir durchlaufen alle Bücher mit `for buch in buecher`
- Bei Treffer: `buch["gelesen"] = True` ändert das Feld direkt im Dictionary
- Das Dictionary ist Teil der Liste `buecher`, also ist die Liste jetzt geändert
- `return True` beendet die Funktion sofort (keine weitere Suche nötig)
- Wenn Schleife endet ohne Treffer: `return False`
- **WICHTIG:** Die Änderung ist nur im RAM! `speichere_buecher()` schreibt in die Datei

**Ausgabe bei Erfolg:**
```
[OK] Buch mit ID 1 als gelesen markiert
```

**Ausgabe bei nicht existierender ID:**
```
[FEHLER] Buch mit ID 99 nicht gefunden
```

**Was passiert in der Datei:**
Das Buch mit ID 1 hat jetzt `"gelesen": true` statt `"gelesen": false`

</details>

---

### DELETE: Dokument löschen

#### Übung 6: Buch löschen

**Aufgabe:**

Erstelle ein Programm `buch_loeschen.py`:

1. Schreibe eine Funktion `loesche_buch(buecher, buch_id)`, die:
   - Ein Buch anhand der ID sucht
   - Das Buch aus der Liste entfernt
   - Das gelöschte Buch zurückgibt (oder `None` wenn nicht gefunden)

2. Lade die Bücher
3. Lösche Buch mit ID 2
4. Speichere die Änderungen
5. Gib aus: Vorher-Anzahl, gelöschter Titel, Nachher-Anzahl

**Hinweise:**
- Nutze `enumerate()` um sowohl Index als auch Element zu bekommen
- Nutze `pop(index)` um Element zu entfernen UND zurückzugeben
- Vergiss nicht zu speichern!

<details>
<summary>Lösung anzeigen</summary>

```python
from json_helper import lade_buecher, speichere_buecher

def loesche_buch(buecher, buch_id):
    """
    Löscht ein Buch anhand der ID
    
    Args:
        buecher (list): Liste von Buch-Dictionaries
        buch_id (int): ID des Buchs
    
    Returns:
        dict or None: Gelöschtes Buch oder None
    """
    for i, buch in enumerate(buecher):
        if buch["id"] == buch_id:
            geloeschtes_buch = buecher.pop(i)
            return geloeschtes_buch
    return None

# Laden
buecher = lade_buecher()
print(f"Vorher: {len(buecher)} Bücher")

# Löschen
buch_id = 2
geloescht = loesche_buch(buecher, buch_id)

if geloescht:
    # Speichern (WICHTIG!)
    speichere_buecher(buecher)
    print(f"[OK] Buch gelöscht: {geloescht['titel']}")
    print(f"Nachher: {len(buecher)} Bücher")
else:
    print(f"[FEHLER] Buch mit ID {buch_id} nicht gefunden")
```

**Erklärung:**
- `enumerate(buecher)` gibt Tupel zurück: `(index, element)`
- Beispiel: `for i, buch in enumerate([...])` → i=0, buch={...}, dann i=1, buch={...}
- Wir brauchen den Index `i` für `pop(i)`
- `pop(i)` entfernt Element an Position i UND gibt es zurück
- Die Liste `buecher` ist jetzt kürzer (ein Element weniger)
- `return geloeschtes_buch` beendet Funktion sofort nach Erfolg
- Wenn nichts gefunden: `return None`

**Ausgabe:**
```
Vorher: 3 Bücher
[OK] Buch gelöscht: Automate the Boring Stuff
Nachher: 2 Bücher
```

**Alternative mit List Comprehension:**
```python
def loesche_buch(buecher, buch_id):
    """Gibt neue Liste ohne das Buch zurück"""
    neue_liste = [b for b in buecher if b["id"] != buch_id]
    return neue_liste

# Nutzen (andere Verwendung!):
buecher = loesche_buch(buecher, 2)
speichere_buecher(buecher)
```
Nachteil: Man weiß nicht, ob tatsächlich etwas gelöscht wurde.

</details>

---

### Lernziel-Check Teil 3

1. **Was passiert, wenn du nach `buecher.append(neues_buch)` NICHT speicherst?**
   <details>
   <summary>Antwort anzeigen</summary>
   Die Änderung ist nur im RAM (Arbeitsspeicher). Beim nächsten Programmstart ist das neue Buch weg, weil die Datei nicht geändert wurde.
   </details>

2. **Warum prüfen wir in `suche_buch_nach_titel()` auf leeren Suchbegriff?**
   <details>
   <summary>Antwort anzeigen</summary>
   Ohne Prüfung würde ein leerer String in JEDEM Titel gefunden werden (leerer String ist in jedem String enthalten). Das ist vermutlich nicht gewollt.
   </details>

3. **Was macht `enumerate()` in der DELETE-Funktion?**
   <details>
   <summary>Antwort anzeigen</summary>
   `enumerate()` gibt sowohl Index als auch Element zurück: `for i, buch in enumerate(buecher)`. Wir brauchen den Index `i` für `pop(i)`.
   </details>

---

## Teil 4: Praktisches Mini-Projekt

### Einfache Bücherverwaltung mit Menü

Jetzt bauen wir ein einfaches Programm mit Menü! Wir halten es heute bewusst einfach.

**Datei:** `buecherverwaltung_einfach.py`

```python
from json_helper import lade_buecher, speichere_buecher, naechste_id

def buch_hinzufuegen(buecher):
    """Fügt ein neues Buch hinzu"""
    print("\n" + "=" * 50)
    print("NEUES BUCH HINZUFÜGEN")
    print("=" * 50)
    
    titel = input("Titel: ").strip()
    if not titel:
        print("[FEHLER] Titel darf nicht leer sein")
        return
    
    autor = input("Autor: ").strip()
    if not autor:
        print("[FEHLER] Autor darf nicht leer sein")
        return
    
    jahr = input("Erscheinungsjahr: ").strip()
    if not jahr.isdigit():
        print("[FEHLER] Jahr muss eine Zahl sein")
        return
    jahr = int(jahr)
    
    neues_buch = {
        "id": naechste_id(buecher),
        "titel": titel,
        "autor": autor,
        "jahr": jahr,
        "gelesen": False
    }
    
    buecher.append(neues_buch)
    speichere_buecher(buecher)
    print(f"\n[OK] Buch '{titel}' hinzugefügt (ID: {neues_buch['id']})")

def alle_buecher_anzeigen(buecher):
    """Zeigt alle Bücher an"""
    print("\n" + "=" * 50)
    print("ALLE BÜCHER")
    print("=" * 50)
    
    if not buecher:
        print("\nKeine Bücher vorhanden")
        print("Tipp: Wähle Option 1 um ein Buch hinzuzufügen")
        return
    
    # Nach Titel sortieren
    sortierte_buecher = sorted(buecher, key=lambda b: b["titel"].lower())
    
    for buch in sortierte_buecher:
        status = "[X]" if buch["gelesen"] else "[ ]"
        print(f"\n[ID {buch['id']}] {status} {buch['titel']}")
        print(f"        Autor: {buch['autor']}")
        print(f"        Jahr: {buch['jahr']}")

def buch_als_gelesen_markieren(buecher):
    """Markiert ein Buch als gelesen"""
    print("\n" + "=" * 50)
    print("BUCH ALS GELESEN MARKIEREN")
    print("=" * 50)
    
    id_eingabe = input("Buch-ID: ").strip()
    if not id_eingabe.isdigit():
        print("[FEHLER] ID muss eine Zahl sein")
        return
    
    buch_id = int(id_eingabe)
    
    for buch in buecher:
        if buch["id"] == buch_id:
            if buch["gelesen"]:
                print(f"\n[INFO] Buch '{buch['titel']}' ist bereits als gelesen markiert")
            else:
                buch["gelesen"] = True
                speichere_buecher(buecher)
                print(f"\n[OK] Buch '{buch['titel']}' als gelesen markiert")
            return
    
    print(f"[FEHLER] Kein Buch mit ID {buch_id} gefunden")

def hauptmenu():
    """Zeigt das Hauptmenü und verarbeitet Eingaben"""
    buecher = lade_buecher()
    
    while True:
        print("\n" + "=" * 50)
        print("BÜCHERVERWALTUNG")
        print("=" * 50)
        print("1. Neues Buch hinzufügen")
        print("2. Alle Bücher anzeigen")
        print("3. Buch als gelesen markieren")
        print("4. Beenden")
        print("=" * 50)
        
        auswahl = input("Wähle eine Option (1-4): ").strip()
        
        if auswahl == "1":
            buch_hinzufuegen(buecher)
        elif auswahl == "2":
            alle_buecher_anzeigen(buecher)
        elif auswahl == "3":
            buch_als_gelesen_markieren(buecher)
        elif auswahl == "4":
            print("\nAuf Wiedersehen!")
            break
        else:
            print("\n[FEHLER] Ungültige Eingabe - bitte 1-4 wählen")

if __name__ == "__main__":
    hauptmenu()
```

**Programm starten:**
```bash
python buecherverwaltung_einfach.py
```

**Erklärung:**
- Einfache Validierung mit `isdigit()` statt try/except
- `strip()` entfernt Leerzeichen am Anfang/Ende
- `sorted()` sortiert Bücher alphabetisch
- `lambda b: b["titel"].lower()` ist die Sortierfunktion
- Statusmeldungen mit [OK], [FEHLER], [INFO]

---

## Best Practices - Die wichtigsten Regeln

### 1. Immer UTF-8 Encoding nutzen

```python
# RICHTIG - Umlaute funktionieren
with open("datei.json", "r", encoding="utf-8") as f:
    daten = json.load(f)

# FALSCH - Umlaute können Probleme machen
with open("datei.json", "r") as f:
    daten = json.load(f)
```

### 2. Immer indent und ensure_ascii nutzen

```python
# RICHTIG - Lesbar und mit Umlauten
json.dump(daten, f, ensure_ascii=False, indent=2)

# FALSCH - Unleserlich und Umlaute als Escape-Sequenzen
json.dump(daten, f)
```

### 3. Änderungen speichern nicht vergessen

```python
# RICHTIG - Änderungen werden gespeichert
buecher = lade_buecher()
buecher.append(neues_buch)
speichere_buecher(buecher)  # WICHTIG!

# FALSCH - Änderungen gehen verloren
buecher = lade_buecher()
buecher.append(neues_buch)
# Ohne speichern() ist die Änderung beim nächsten Start weg!
```

### 4. Eingaben validieren

```python
# RICHTIG - Eingaben prüfen
jahr_eingabe = input("Jahr: ")
if not jahr_eingabe.isdigit():
    print("Ungültige Eingabe")
    return
jahr = int(jahr_eingabe)

# FALSCH - Keine Validierung (Programm stürzt ab bei "abc")
jahr = int(input("Jahr: "))
```

### 5. Hilfsfunktionen erstellen und wiederverwenden

```python
# RICHTIG - Zentrale Funktionen
from json_helper import lade_buecher, speichere_buecher

# In allen Dateien nutzen:
buecher = lade_buecher()
# ...
speichere_buecher(buecher)

# FALSCH - Überall kopieren
# Wenn sich der Dateiname ändert, muss man überall ändern!
```

---

## Zusammenfassung

### Die wichtigsten Befehle

| Befehl | Wofür? | Beispiel |
|--------|--------|----------|
| `import json` | JSON-Modul laden | `import json` |
| `json.load(f)` | JSON aus Datei lesen | `daten = json.load(f)` |
| `json.dump(d, f)` | JSON in Datei schreiben | `json.dump(daten, f)` |
| `json.loads(s)` | JSON aus String lesen | `daten = json.loads(text)` |
| `json.dumps(d)` | JSON zu String | `text = json.dumps(daten)` |

### Der Standard-Workflow

**Für ALLE Änderungen:**

```python
from json_helper import lade_buecher, speichere_buecher

# 1. LADEN
buecher = lade_buecher()

# 2. ÄNDERN
# CREATE: buecher.append(neues_buch)
# UPDATE: buecher[0]["feld"] = neuer_wert
# DELETE: buecher.pop(index)

# 3. SPEICHERN
speichere_buecher(buecher)
```

### Python ↔ JSON Mapping

```python
# Python → JSON
{...}     → {...}       # dict → Object
[...]     → [...]       # list → Array
"text"    → "text"      # str → String
123       → 123         # int/float → Number
True      → true        # bool → Boolean
None      → null        # None → null

# JSON → Python
{...}     → dict
[...]     → list
"text"    → str
123       → int/float
true      → bool
null      → None
```

### Die goldenen Regeln

1. **JSON-Datei != Datenbank** - Es ist nur Text auf der Festplatte
2. **Immer encoding="utf-8"** - Umlaute korrekt behandeln
3. **Immer ensure_ascii=False, indent=2** - Lesbar und mit Umlauten
4. **Änderungen speichern** - json.dump() nach Änderungen nicht vergessen!
5. **Eingaben validieren** - Nicht davon ausgehen, dass Benutzer korrekt eingibt
6. **Hilfsfunktionen** - Nicht überall Copy-Paste, sondern zentrale Funktionen
7. **IDs automatisch** - naechste_id() nutzen statt manuell vergeben

### Typische Anfängerfehler

```
FEHLER: Encoding vergessen
   open("datei.json", "r")
RICHTIG:
   open("datei.json", "r", encoding="utf-8")

FEHLER: ensure_ascii nicht gesetzt
   json.dump(daten, f)  # "München" wird zu "\u00fcnchen"
RICHTIG:
   json.dump(daten, f, ensure_ascii=False)

FEHLER: Änderungen nicht gespeichert
   daten = lade_daten()
   daten.append(neu)
   # Ohne speichern()!
RICHTIG:
   daten = lade_daten()
   daten.append(neu)
   speichere_daten(daten)  # WICHTIG!

FEHLER: Keine Validierung
   jahr = int(input("Jahr: "))  # Crash bei "abc"!
RICHTIG:
   jahr_str = input("Jahr: ")
   if not jahr_str.isdigit():
       print("Ungültige Eingabe")
       return
   jahr = int(jahr_str)

FEHLER: Falsche Anführungszeichen in JSON-Datei
   {'name': 'Test'}  # Ungültig!
RICHTIG:
   {"name": "Test"}  # Gültig!
```

---

## Grenzen von JSON-Dateien

**JSON-Dateien sind NICHT geeignet für:**

- Größere Datenmengen (wenn hunderte oder tausende Einträge werden die Operationen langsam)
- Komplexe Abfragen (wie SQL WHERE, JOIN, etc.)
- Mehrere gleichzeitige Zugriffe (mehrere Programme/Benutzer)
- Transaktionen (Alles oder Nichts, ACID-Eigenschaften)
- Beziehungen zwischen Dokumenten (Foreign Keys)
- Indizes für schnelle Suche
- Hohe Performance-Anforderungen

**JSON-Dateien sind GEEIGNET für:**

- Konfigurationsdateien
- Kleinere Datensammlungen (einige Dutzend bis wenige hundert Einträge)
- Prototypen und Lernprojekte
- Datenaustausch zwischen Programmen
- Einfache CRUD-Operationen
- Lokale Anwendungen (ein Benutzer)
- Flexibel strukturierte Daten

**Wichtig:**
- Bei größeren Datenmengen: Besser eine echte Datenbank (SQLite für lokal, PostgreSQL/MySQL für Server)
- Bei mehreren Benutzern: Datenbank mit Locking/Transaktionen
- Für komplexe Suchen: SQL-Datenbank
- Für dokumentenbasierte Daten mit vielen Einträgen: MongoDB (echte NoSQL-Datenbank)

---

## Vergleich: JSON-Datei vs. Datenbanken

| Merkmal | JSON-Datei | SQLite | MongoDB |
|---------|------------|--------|---------|
| Was ist es? | Textdatei | Lokale Datenbank | NoSQL-Datenbank |
| Setup | Keine | Tabellen definieren | Collections erstellen |
| Geschwindigkeit | Wird langsam bei vielen Einträgen | Schnell (Indizes) | Sehr schnell |
| Abfragen | Python-Code | SQL | MongoDB Query Language |
| Struktur | Flexibel | Fix (Schema) | Flexibel (Schema-optional) |
| Gleichzeitige Zugriffe | Problematisch | Unterstützt | Sehr gut unterstützt |
| Geeignet für | Dutzende Einträge | Tausende Einträge | Millionen Einträge |
| Lernkurve | Sehr einfach | Mittel (SQL) | Mittel |

**Faustregel:**
- **Prototyp / Lernen / wenige Daten** → JSON-Datei
- **Production / lokale App / strukturierte Daten** → SQLite
- **Server / viele Benutzer / strukturierte Daten** → PostgreSQL/MySQL
- **Server / flexible Dokumente / große Datenmengen** → MongoDB

---

## Zusatzaufgaben zum Üben (OPTIONAL)

Teste dein Wissen mit diesen Aufgaben! Versuche sie erst selbst zu lösen, bevor du die Lösung anschaust.

### Aufgabe 1: Nach Autor filtern

**Aufgabe:**
Schreibe eine Funktion `finde_buecher_nach_autor(buecher, autor)`, die alle Bücher eines bestimmten Autors zurückgibt (exakte Übereinstimmung, case-insensitive).

<details>
<summary>Lösung anzeigen</summary>

```python
def finde_buecher_nach_autor(buecher, autor):
    """Findet alle Bücher eines Autors"""
    autor = autor.lower()
    return [b for b in buecher if b["autor"].lower() == autor]

# Test:
buecher = lade_buecher()
ergebnisse = finde_buecher_nach_autor(buecher, "Eric Matthes")
for buch in ergebnisse:
    print(f"{buch['titel']} ({buch['jahr']})")
```

</details>

---

### Aufgabe 2: Ungelesene Bücher zählen

**Aufgabe:**
Schreibe eine Funktion `zaehle_ungelesen(buecher)`, die die Anzahl ungelesener Bücher zurückgibt.

<details>
<summary>Lösung anzeigen</summary>

```python
def zaehle_ungelesen(buecher):
    """Zählt ungelesene Bücher"""
    return len([b for b in buecher if not b["gelesen"]])

# Alternative:
def zaehle_ungelesen(buecher):
    """Zählt ungelesene Bücher"""
    return sum(1 for b in buecher if not b["gelesen"])

# Test:
buecher = lade_buecher()
anzahl = zaehle_ungelesen(buecher)
print(f"Du hast noch {anzahl} ungelesene Bücher")
```

</details>

---

### Aufgabe 3: Bücher nach Jahr sortieren

**Aufgabe:**
Schreibe eine Funktion `sortiere_nach_jahr(buecher, aufsteigend=True)`, die eine sortierte Kopie der Bücherliste zurückgibt (nach Erscheinungsjahr).

<details>
<summary>Lösung anzeigen</summary>

```python
def sortiere_nach_jahr(buecher, aufsteigend=True):
    """Sortiert Bücher nach Erscheinungsjahr"""
    return sorted(buecher, key=lambda b: b["jahr"], reverse=not aufsteigend)

# Test:
buecher = lade_buecher()

print("Älteste zuerst:")
for buch in sortiere_nach_jahr(buecher):
    print(f"{buch['jahr']}: {buch['titel']}")

print("\nNeueste zuerst:")
for buch in sortiere_nach_jahr(buecher, aufsteigend=False):
    print(f"{buch['jahr']}: {buch['titel']}")
```

**Erklärung:**
- `sorted()` gibt neue Liste zurück (Original bleibt unverändert)
- `key=lambda b: b["jahr"]` sagt: sortiere nach dem Jahr-Feld
- `reverse=not aufsteigend` dreht die Sortierung um wenn aufsteigend=False

</details>

---

### Aufgabe 4: Export als Text

**Aufgabe:**
Schreibe eine Funktion `exportiere_als_text(buecher, dateiname)`, die alle Bücher in eine lesbare Textdatei schreibt.

Format:
```
=======================================
BÜCHERLISTE
=======================================

[X] Python Crashkurs
    Autor: Eric Matthes
    Jahr: 2019
    ID: 1

[ ] Automate the Boring Stuff
    Autor: Al Sweigart
    Jahr: 2020
    ID: 2
```

<details>
<summary>Lösung anzeigen</summary>

```python
def exportiere_als_text(buecher, dateiname):
    """Exportiert Bücher als lesbare Textdatei"""
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("BÜCHERLISTE\n")
        f.write("=" * 40 + "\n\n")
        
        for buch in buecher:
            status = "[X]" if buch["gelesen"] else "[ ]"
            f.write(f"{status} {buch['titel']}\n")
            f.write(f"    Autor: {buch['autor']}\n")
            f.write(f"    Jahr: {buch['jahr']}\n")
            f.write(f"    ID: {buch['id']}\n\n")

# Test:
buecher = lade_buecher()
exportiere_als_text(buecher, "buecherliste.txt")
print("[OK] Exportiert nach buecherliste.txt")
```

**Erklärung:**
- `open(..., "w")` öffnet Datei im Schreibmodus (überschreibt!)
- `f.write()` schreibt String in die Datei
- `\n` = Zeilenumbruch
- Jedes Buch wird formatiert ausgegeben

</details>

---

### Aufgabe 5: Duplikat-Prüfung

**Aufgabe:**
Schreibe eine Funktion `existiert_buch(buecher, titel, autor)`, die `True` zurückgibt wenn ein Buch mit diesem Titel UND Autor bereits existiert (case-insensitive).

<details>
<summary>Lösung anzeigen</summary>

```python
def existiert_buch(buecher, titel, autor):
    """Prüft ob Buch bereits existiert"""
    titel = titel.lower()
    autor = autor.lower()
    
    for buch in buecher:
        if (buch["titel"].lower() == titel and 
            buch["autor"].lower() == autor):
            return True
    return False

# In buch_hinzufuegen nutzen:
def buch_hinzufuegen_sicher(buecher):
    """Fügt Buch hinzu mit Duplikat-Prüfung"""
    titel = input("Titel: ").strip()
    autor = input("Autor: ").strip()
    
    if existiert_buch(buecher, titel, autor):
        print(f"[FEHLER] Buch '{titel}' von {autor} existiert bereits!")
        return
    
    # Rest wie gehabt...
```

</details>




---

## Ausblick: Was kommt morgen?

**Morgen lernen wir:**
- **try/except Blöcke** - Fehlerbehandlung richtig machen
- **FileNotFoundError** - Was tun wenn Datei nicht existiert?
- **json.JSONDecodeError** - Was tun bei ungültigem JSON?
- **ValueError** - Was tun bei ungültigen Eingaben?
- **Bessere Validierung** - Mit Jahresbereichen, Pflichtfeldern etc.

Dann wird aus dem einfachen Programm ein robustes Programm, das auch mit Fehlern umgehen kann!

---

## Hilfreiche Ressourcen

**Python JSON Dokumentation:**
- https://docs.python.org/3/library/json.html

**JSON Format:**
- https://www.json.org/json-de.html

**JSON Validator (zum Prüfen):**
- https://jsonlint.com/

**Nächste Schritte:**
- SQLite lernen (relationale Datenbank, mit SQL)
- MongoDB lernen (echte Dokumenten-Datenbank mit Server)
- FastAPI lernen (REST API mit JSON)
- Fehlerbehandlung mit try/except (kommt morgen!)

---

**Viel Erfolg beim Programmieren!**
