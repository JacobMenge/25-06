# Übungs-Projekt: Persönliche Rezeptsammlung

## Hinweise zum Übungsprojekt

**Art der Aufgabe:** Freiwillige Übung zur Vertiefung  
**Abgabe:** Keine Abgabe erforderlich  
**Zweck:** Die Themen dieser Woche praktisch anwenden und vertiefen  
**Zeitaufwand:** 2-4 Stunden (je nach Vorkenntnissen)  
**Schwierigkeit:** Anfängerfreundlich mit klaren Schritten

---

## Worum geht es?

In dieser Übung erstellst du eine einfache **Rezeptverwaltung**. Du kombinierst dabei die wichtigsten Konzepte dieser Woche:

- **JSON-Dateien** zum Speichern von Rezepten
- **SQLite-Datenbank** zum Speichern von Zutaten
- **Python-Code** um beides zu verbinden

Das Projekt ist in **Minimalziel** und **Erweiterungen** aufgeteilt. So kannst du erst die Basis implementieren und dann nach Belieben ausbauen. Am Ende findest du eine vollständige Musterlösung zum Vergleichen.

---

## Was du bauen wirst

### Minimalziel (Kernfunktionen für diese Übung)

1. **Rezepte verwalten** (in JSON-Datei)
   - Rezepte hinzufügen
   - Alle Rezepte anzeigen

2. **Zutaten-Datenbank** (in SQLite)
   - Zutaten speichern (normalisiert)
   - Alle Zutaten auflisten

3. **Einfaches Menü**
   - Grundfunktionen über Menü aufrufen

### Optionale Erweiterungen

- Rezepte nach Namen suchen
- Zutaten mit Kategorie speichern (erfordert DB-Migration)
- Zutaten nach Kategorie filtern
- Rezept löschen
- Statistiken anzeigen

---

## Aufgabenstellung

### Teil 1: JSON-Struktur für Rezepte

**Aufgabe:**  
Erstelle eine JSON-Datei `rezepte.json` mit folgender Struktur:

Jedes Rezept soll diese Felder haben:
- `id` (Integer) - Eindeutige Nummer
- `name` (String) - Name des Rezepts
- `zutaten` (Liste von Strings) - Liste der benötigten Zutaten
- `kategorie` (String) - z.B. "Hauptgericht", "Dessert", "Snack"
- `zubereitungszeit` (Integer) - Zeit in Minuten
- `anleitung` (String) - Kurze Zubereitungsbeschreibung

**Füge mindestens 2 Beispiel-Rezepte hinzu!**

**Empfehlung:** Schreibe Zutaten ohne führende/abschließende Leerzeichen. Das Programm normalisiert sie später automatisch (z.B. "eier" wird zu "Eier", "rote zwiebel" wird zu "Rote Zwiebel").

---

### Teil 2: SQLite-Datenbank für Zutaten

**Aufgabe:**  
Erstelle eine SQLite-Datenbank `kueche.db` mit einer Tabelle `zutaten`:

**Minimalziel - Tabellenstruktur:**
```sql
CREATE TABLE zutaten (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
)
```

**Hinweis zur ID:** Die ID wird von SQLite automatisch vergeben (durch `INTEGER PRIMARY KEY`). Wir setzen sie beim INSERT nicht selbst. `AUTOINCREMENT` ist hier nicht nötig.

**Optional - Mit Kategorie (erfordert später ALTER TABLE oder neue DB):**
```sql
CREATE TABLE zutaten (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    kategorie TEXT
)
```

**Wichtig zur UNIQUE-Bedingung:** Sie verhindert doppelte Einträge nur bei exakt gleicher Schreibweise. "Eier" und "eier" wären zwei verschiedene Einträge! Deshalb normalisieren wir Zutaten im Code.

---

### Teil 3: Python-Programm erstellen

**Aufgabe:**  
Erstelle ein Python-Programm `rezeptverwaltung.py` mit folgenden Funktionen:

#### 3.1 Hilfsfunktionen für JSON

```python
def lade_rezepte():
    """
    Lädt Rezepte aus rezepte.json
    
    Ohne try/except (kommt später):
    - Wenn Datei nicht existiert: leere Liste
    - Wenn Datei leer ist: leere Liste
    - Wenn JSON ungültig ist: Programm bricht ab (ok für diese Übung)
    - Wenn JSON keine Liste ist: leere Liste
    
    Wir prüfen die Datei-Existenz vorher mit os.path.exists(),
    dann scheitert open() nicht wegen FileNotFoundError.
    """
    # Implementierung

def speichere_rezepte(rezepte):
    """Speichert Rezepte in rezepte.json mit UTF-8 und indent=2"""
    # Implementierung

def naechste_id(rezepte):
    """
    Ermittelt nächste freie ID
    
    Setzt voraus: Alle Rezepte haben eine gültige int-ID.
    """
    # Implementierung
```

#### 3.2 Hilfsfunktionen für SQLite

```python
def erstelle_datenbank():
    """Erstellt die Zutaten-Tabelle wenn nicht vorhanden"""
    # Implementierung mit IF NOT EXISTS

def normalisiere_zutat(name):
    """
    Normalisiert Zutatennamen für konsistente Speicherung
    
    - Entfernt Leerzeichen am Anfang/Ende
    - Jedes Wort: Erster Buchstabe groß, Rest klein
    
    Beispiele:
    - "eier" -> "Eier"
    - " MEHL " -> "Mehl"
    - "rote zwiebel" -> "Rote Zwiebel"
    
    Hinweis: Diese Normalisierung ist bewusst simpel gehalten.
    Sonderfälle wie Bindestriche oder Akzente sind nicht Fokus dieser Übung.
    """
    # Implementierung

def fuege_zutaten_hinzu(zutaten_liste):
    """
    Fügt mehrere Zutaten hinzu (eine DB-Verbindung für alle)
    
    - Normalisiert alle Zutaten
    - Nutzt INSERT OR IGNORE für automatische Duplikat-Behandlung
    - Gibt zurück: (anzahl_neu, anzahl_gesamt)
    """
    # Implementierung

def zeige_alle_zutaten():
    """Zeigt alle Zutaten aus der Datenbank alphabetisch sortiert"""
    # Implementierung
```

#### 3.3 Hauptfunktionen

```python
def rezept_hinzufuegen(rezepte):
    """
    Fügt ein neues Rezept hinzu
    
    Ablauf:
    1. Alle Felder abfragen (name, kategorie, zeit, zutaten, anleitung)
    2. Eingaben validieren:
       - Nichts darf leer sein (nach strip())
       - Zeit muss Zahl >= 1 sein
       - Zutaten als kommagetrennte Liste
    3. Duplikate in Zutatenliste entfernen (case-insensitive)
    4. Rezept zur Liste hinzufügen und speichern
    5. Alle Zutaten zur DB hinzufügen (normalisiert, eine Verbindung!)
    """
    # Implementierung

def alle_rezepte_anzeigen(rezepte):
    """
    Zeigt alle Rezepte formatiert an
    
    Sortiere alphabetisch nach Name.
    Zeige: ID, Name, Kategorie, Zeit, Zutaten, Anleitung
    """
    # Implementierung
```

#### 3.4 Menü

Erstelle ein einfaches Menü mit diesen Optionen:
1. Neues Rezept hinzufügen
2. Alle Rezepte anzeigen
3. Alle Zutaten anzeigen
4. Beenden

---

## Anforderungen

### Minimalziel - Kernfunktionen für diese Übung:

- JSON-Datei mit korrekter Struktur und 2 Beispiel-Rezepten
- SQLite-Datenbank mit Tabelle `zutaten` (mindestens `id` und `name`)
- Alle oben genannten Funktionen implementiert
- Programm startet ohne Fehler (bei gültigem JSON)
- Menü mit mindestens 4 Optionen funktioniert
- Änderungen werden korrekt gespeichert:
  - JSON: `json.dump()` mit `ensure_ascii=False` und `indent=2`
  - SQLite: `commit()` nach Änderungen

### Validation/Fehlerbehandlung:

**Heute ausreichend:**
- Eingaben mit `strip()` bereinigen
- Mit `isdigit()` Zahlen prüfen
- Zeit >= 1 prüfen
- Prüfen ob Eingaben nicht leer sind
- Bei JSON-Laden prüfen ob es eine Liste ist (bei gültigem JSON)
- Datei-Existenz mit `os.path.exists()` prüfen

**NICHT erforderlich (kommt später):**
- `try/except` Blöcke für FileNotFoundError oder JSONDecodeError
- Komplexe Fehlerbehandlung

### Datenqualität:

- **IDs in JSON:** Automatisch mit `naechste_id()` vergeben
- **IDs in SQLite:** Von SQLite automatisch vergeben durch `INTEGER PRIMARY KEY`
- **Zutaten normalisieren:** Vor DB-Speicherung:
  - `strip()` anwenden
  - Jedes Wort: Ersten Buchstaben groß, Rest klein
  - "rote zwiebel" -> "Rote Zwiebel"
  - "eier" -> "Eier"
- **Duplikate:** Im Rezept entfernen (case-insensitive)
- **SQLite UNIQUE:** Verhindert Duplikate mit exakt gleichem Namen
- **INSERT OR IGNORE:** Keine Fehler bei Duplikaten

---

## Tipps zum Vorgehen

### Phase 1: Vorbereitung (30 Min)

1. **JSON-Datei erstellen:** Schreibe `rezepte.json` manuell mit 2 Beispielen
2. **Projekt-Struktur:** Erstelle `rezeptverwaltung.py`
3. **Imports:** `import json`, `import sqlite3`, `import os` am Anfang

### Phase 2: Datenbank (45 Min)

4. **Tabelle erstellen:** Implementiere `erstelle_datenbank()`
5. **Test:** Rufe die Funktion auf, prüfe ob `kueche.db` existiert
6. **Normalisierung:** Implementiere `normalisiere_zutat()` - wichtig für Mehrwort-Zutaten!
7. **Zutaten einfügen:** Implementiere `fuege_zutaten_hinzu()` mit einer Verbindung für alle
8. **Test:** Füge testweise ein paar Zutaten ein
9. **Zutaten anzeigen:** Implementiere `zeige_alle_zutaten()`

### Phase 3: JSON (30 Min)

10. **Laden:** Implementiere `lade_rezepte()` mit `os.path.exists()`
11. **Test:** Lade deine Beispiel-Rezepte und gib sie aus
12. **Speichern:** Implementiere `speichere_rezepte()`
13. **ID-Funktion:** Implementiere `naechste_id()`

### Phase 4: Hauptfunktionen (60-90 Min)

14. **Anzeigen:** Implementiere `alle_rezepte_anzeigen()`
15. **Test:** Zeige deine Beispiel-Rezepte an
16. **Hinzufügen:** Implementiere `rezept_hinzufuegen()` - das ist der aufwändigste Teil!
    - Eingaben validieren
    - Duplikate entfernen
    - Zutaten normalisiert zur DB hinzufügen
17. **Test:** Füge ein neues Rezept hinzu

### Phase 5: Menü (30 Min)

18. **Menü-Schleife:** Erstelle `hauptmenu()` Funktion
19. **Test:** Durchlaufe alle Menüpunkte
20. **Feinschliff:** Verbessere Ausgaben, Fehlermeldungen

### Optional: Erweiterungen (30-60 Min pro Feature)

21. **Suche:** Implementiere `rezept_suchen()`
22. **Kategorie:** Erweitere DB (siehe Hinweis zur Migration unten)
23. **Weitere Ideen:** Siehe Bonusaufgaben

---

## Beispiel-Ausgabe

So könnte dein Programm aussehen:

```
==================================================
REZEPTVERWALTUNG
==================================================
1. Neues Rezept hinzufügen
2. Alle Rezepte anzeigen
3. Alle Zutaten anzeigen
4. Beenden
==================================================
Wähle eine Option (1-4): 2

==================================================
ALLE REZEPTE
==================================================

Gesamt: 2 Rezept(e)

[ID 1] Spaghetti Carbonara (Hauptgericht)
       Zeit: 20 Minuten
       Zutaten: Spaghetti, Eier, Speck, Parmesan
       Anleitung: Pasta kochen, Eier mit Käse mischen...

[ID 2] Schokomuffins (Dessert)
       Zeit: 30 Minuten
       Zutaten: Mehl, Zucker, Kakao, Eier, Butter
       Anleitung: Alle Zutaten mischen und backen...
```

---

## Bonusaufgaben (Optional)

Falls du noch mehr üben möchtest:

1. **Rezept suchen:** Teilstring-Suche im Namen (case-insensitive)

2. **Zutaten mit Kategorie:**
   - **Wichtig:** Wenn du die `kategorie`-Spalte nachträglich hinzufügen willst:
     - Entweder: Neue Datenbank erstellen (`kueche2.db`)
     - Oder: `ALTER TABLE zutaten ADD COLUMN kategorie TEXT` nutzen
   - Frage Kategorie beim Hinzufügen ab (mit Vorschlägen: Gemüse, Gewürze, etc.)
   - Implementiere Filter nach Kategorie

3. **Rezept löschen:** Lösche nach ID (mit Bestätigung!)

4. **Statistik:** Zeige Anzahl Rezepte pro Kategorie

5. **Export:** Exportiere ein Rezept als Textdatei

6. **Erweiterte Validierung:** 
   - Mindestanzahl Zutaten (z.B. >= 2)
   - Maximale Zubereitungszeit

---

## Musterlösung

<details>
<summary>rezepte.json (Beispieldaten)</summary>

```json
[
  {
    "id": 1,
    "name": "Spaghetti Carbonara",
    "zutaten": ["Spaghetti", "Eier", "Speck", "Parmesan", "Salz", "Pfeffer"],
    "kategorie": "Hauptgericht",
    "zubereitungszeit": 20,
    "anleitung": "Pasta kochen. Eier mit Käse mischen. Speck anbraten. Alles vermischen."
  },
  {
    "id": 2,
    "name": "Schokomuffins",
    "zutaten": ["Mehl", "Zucker", "Kakao", "Eier", "Butter", "Backpulver"],
    "kategorie": "Dessert",
    "zubereitungszeit": 30,
    "anleitung": "Alle Zutaten mischen. In Muffinformen füllen. Bei 180°C 20 Minuten backen."
  }
]
```

**Beachte:**
- `zubereitungszeit` als Zahl (nicht String)
- Komma zwischen Rezepten, aber nicht nach dem letzten
- Doppelte Anführungszeichen `"` für Strings

</details>

<details>
<summary>rezeptverwaltung.py (Vollständiger Code)</summary>

```python
import json
import sqlite3
import os

# ===========================
# KONFIGURATION
# ===========================

JSON_DATEI = "rezepte.json"
DB_DATEI = "kueche.db"

# ===========================
# JSON-FUNKTIONEN
# ===========================

def lade_rezepte():
    """
    Lädt Rezepte aus JSON-Datei
    
    Ohne try/except (kommt später):
    - Wenn Datei nicht existiert: leere Liste
    - Wenn Datei leer ist: leere Liste
    - Wenn JSON ungültig ist: Programm bricht ab (ok für diese Übung)
    - Wenn JSON keine Liste ist: leere Liste
    
    Wir prüfen die Datei-Existenz vorher mit os.path.exists(),
    dann scheitert open() nicht wegen FileNotFoundError.
    """
    # Prüfe ob Datei existiert
    if not os.path.exists(JSON_DATEI):
        print(f"INFO: {JSON_DATEI} nicht gefunden -> starte mit leerer Liste")
        return []
    
    # Datei existiert - lade sie
    with open(JSON_DATEI, "r", encoding="utf-8") as f:
        inhalt = f.read().strip()
        
        # Prüfe ob Datei leer ist
        if not inhalt:
            print(f"INFO: {JSON_DATEI} ist leer -> starte mit leerer Liste")
            return []
        
        # Parse JSON (kann hier crashen bei ungültigem JSON - das ist ok)
        rezepte = json.loads(inhalt)
        
        # Prüfe ob es eine Liste ist
        if not isinstance(rezepte, list):
            print("WARNUNG: JSON muss eine Liste sein -> starte mit leerer Liste")
            return []
        
        return rezepte

def speichere_rezepte(rezepte):
    """Speichert Rezepte in JSON-Datei"""
    with open(JSON_DATEI, "w", encoding="utf-8") as f:
        json.dump(rezepte, f, ensure_ascii=False, indent=2)

def naechste_id(rezepte):
    """
    Ermittelt die nächste freie ID
    
    Setzt voraus: Alle Rezepte haben eine gültige int-ID.
    """
    if not rezepte:
        return 1
    return max(r["id"] for r in rezepte) + 1

# ===========================
# SQLITE-FUNKTIONEN
# ===========================

def erstelle_datenbank():
    """
    Erstellt die Zutaten-Tabelle wenn nicht vorhanden
    
    Die ID wird von SQLite automatisch vergeben durch INTEGER PRIMARY KEY.
    Wir setzen die ID nicht selbst beim INSERT.
    """
    conn = sqlite3.connect(DB_DATEI)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS zutaten (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)
    
    conn.commit()
    conn.close()

def normalisiere_zutat(name):
    """
    Normalisiert Zutatennamen für konsistente Speicherung
    
    - Entfernt Leerzeichen am Anfang/Ende
    - Jedes Wort: Erster Buchstabe groß, Rest klein
    
    Beispiele:
    - "eier" -> "Eier"
    - " MEHL " -> "Mehl"
    - "rote zwiebel" -> "Rote Zwiebel"
    
    Hinweis: Diese Normalisierung ist bewusst simpel gehalten.
    Sonderfälle wie Bindestriche oder Akzente sind nicht Fokus dieser Übung.
    """
    name = name.strip()
    if not name:
        return name
    
    # Jedes Wort einzeln normalisieren
    woerter = name.split()
    normalisiert = []
    for wort in woerter:
        if wort:  # Nicht-leere Wörter
            wort_normalisiert = wort[0].upper() + wort[1:].lower()
            normalisiert.append(wort_normalisiert)
    
    return " ".join(normalisiert)

def fuege_zutaten_hinzu(zutaten_liste):
    """
    Fügt mehrere Zutaten auf einmal hinzu (eine DB-Verbindung für alle)
    
    - Normalisiert alle Zutaten
    - Nutzt INSERT OR IGNORE für automatische Duplikat-Behandlung
    - Gibt zurück: (anzahl_neu, anzahl_gesamt)
    
    Pro-Tipp: Für größere Datenmengen könnte man executemany() nutzen,
    aber für diese Übung reicht die einfache Schleife völlig aus.
    """
    if not zutaten_liste:
        return 0, 0
    
    # Normalisiere alle Zutaten
    zutaten_normalisiert = [normalisiere_zutat(z) for z in zutaten_liste]
    # Entferne leere Strings
    zutaten_normalisiert = [z for z in zutaten_normalisiert if z]
    
    if not zutaten_normalisiert:
        return 0, 0
    
    # EINE Verbindung für alle Zutaten (effizienter!)
    conn = sqlite3.connect(DB_DATEI)
    cursor = conn.cursor()
    
    anzahl_neu = 0
    for zutat in zutaten_normalisiert:
        cursor.execute(
            "INSERT OR IGNORE INTO zutaten (name) VALUES (?)",
            (zutat,)
        )
        # rowcount > 0 bedeutet: Zeile wurde eingefügt (war neu)
        if cursor.rowcount > 0:
            anzahl_neu += 1
    
    conn.commit()
    conn.close()
    
    return anzahl_neu, len(zutaten_normalisiert)

def zeige_alle_zutaten():
    """Zeigt alle Zutaten aus der Datenbank alphabetisch sortiert"""
    conn = sqlite3.connect(DB_DATEI)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name FROM zutaten ORDER BY name")
    zutaten = cursor.fetchall()
    
    conn.close()
    
    if not zutaten:
        print("\nKeine Zutaten in der Datenbank")
        print("Tipp: Füge ein Rezept hinzu, dann werden Zutaten automatisch gespeichert")
        return
    
    print("\n" + "=" * 50)
    print("ALLE ZUTATEN")
    print("=" * 50)
    print(f"\nGesamt: {len(zutaten)} Zutat(en)\n")
    
    for zutat_id, name in zutaten:
        print(f"  [{zutat_id:3d}] {name}")

# ===========================
# HAUPTFUNKTIONEN
# ===========================

def rezept_hinzufuegen(rezepte):
    """Fügt ein neues Rezept hinzu"""
    print("\n" + "=" * 50)
    print("NEUES REZEPT HINZUFÜGEN")
    print("=" * 50)
    
    # Name erfragen
    name = input("\nRezeptname: ").strip()
    if not name:
        print("[FEHLER] Name darf nicht leer sein")
        return
    
    # Kategorie erfragen
    print("\nKategorie-Vorschläge: Hauptgericht, Dessert, Snack, Frühstück")
    kategorie = input("Kategorie: ").strip()
    if not kategorie:
        print("[FEHLER] Kategorie darf nicht leer sein")
        return
    
    # Zubereitungszeit erfragen
    zeit_eingabe = input("Zubereitungszeit (Minuten): ").strip()
    if not zeit_eingabe.isdigit():
        print("[FEHLER] Zeit muss eine Zahl sein")
        return
    zubereitungszeit = int(zeit_eingabe)
    if zubereitungszeit < 1:
        print("[FEHLER] Zeit muss mindestens 1 Minute sein")
        return
    
    # Zutaten erfragen
    print("\nZutaten (mit Komma trennen, z.B.: Mehl, Zucker, Eier)")
    zutaten_eingabe = input("Zutaten: ").strip()
    if not zutaten_eingabe:
        print("[FEHLER] Mindestens eine Zutat nötig")
        return
    
    # Zutaten splitten und bereinigen
    zutaten = [z.strip() for z in zutaten_eingabe.split(",") if z.strip()]
    
    if not zutaten:
        print("[FEHLER] Keine gültigen Zutaten gefunden")
        return
    
    # Duplikate entfernen (case-insensitive)
    zutaten_normalisiert = [normalisiere_zutat(z) for z in zutaten]
    zutaten_unique = []
    zutaten_lower_set = set()
    for z in zutaten_normalisiert:
        if z.lower() not in zutaten_lower_set:
            zutaten_unique.append(z)
            zutaten_lower_set.add(z.lower())
    
    if len(zutaten_unique) < len(zutaten):
        duplikate_anzahl = len(zutaten) - len(zutaten_unique)
        print(f"INFO: {duplikate_anzahl} doppelte Zutat(en) entfernt")
    
    zutaten = zutaten_unique
    
    # Anleitung erfragen
    anleitung = input("\nKurze Anleitung: ").strip()
    if not anleitung:
        print("[FEHLER] Anleitung darf nicht leer sein")
        return
    
    # Rezept erstellen
    neues_rezept = {
        "id": naechste_id(rezepte),
        "name": name,
        "zutaten": zutaten,
        "kategorie": kategorie,
        "zubereitungszeit": zubereitungszeit,
        "anleitung": anleitung
    }
    
    # Rezept hinzufügen und speichern
    rezepte.append(neues_rezept)
    speichere_rezepte(rezepte)
    
    # Zutaten zur Datenbank hinzufügen (eine Verbindung für alle!)
    anzahl_neu, anzahl_gesamt = fuege_zutaten_hinzu(zutaten)
    
    print(f"\n[OK] Rezept '{name}' hinzugefügt (ID: {neues_rezept['id']})")
    print(f"[OK] {anzahl_neu} neue Zutat(en) zur Datenbank hinzugefügt ({anzahl_gesamt} gesamt)")

def alle_rezepte_anzeigen(rezepte):
    """Zeigt alle Rezepte alphabetisch sortiert an"""
    print("\n" + "=" * 50)
    print("ALLE REZEPTE")
    print("=" * 50)
    
    if not rezepte:
        print("\nKeine Rezepte vorhanden")
        print("Tipp: Wähle Option 1 um ein Rezept hinzuzufügen")
        return
    
    # Nach Name sortieren
    sortierte_rezepte = sorted(rezepte, key=lambda r: r["name"].lower())
    
    print(f"\nGesamt: {len(sortierte_rezepte)} Rezept(e)")
    
    for rezept in sortierte_rezepte:
        print(f"\n[ID {rezept['id']}] {rezept['name']} ({rezept['kategorie']})")
        print(f"       Zeit: {rezept['zubereitungszeit']} Minuten")
        print(f"       Zutaten: {', '.join(rezept['zutaten'])}")
        print(f"       Anleitung: {rezept['anleitung']}")

# ===========================
# HAUPTPROGRAMM
# ===========================

def hauptmenu():
    """Hauptmenü der Anwendung"""
    # Datenbank vorbereiten
    erstelle_datenbank()
    
    # Rezepte laden
    rezepte = lade_rezepte()
    
    while True:
        print("\n" + "=" * 50)
        print("REZEPTVERWALTUNG")
        print("=" * 50)
        print("1. Neues Rezept hinzufügen")
        print("2. Alle Rezepte anzeigen")
        print("3. Alle Zutaten anzeigen")
        print("4. Beenden")
        print("=" * 50)
        
        auswahl = input("Wähle eine Option (1-4): ").strip()
        
        if auswahl == "1":
            rezept_hinzufuegen(rezepte)
        elif auswahl == "2":
            alle_rezepte_anzeigen(rezepte)
        elif auswahl == "3":
            zeige_alle_zutaten()
        elif auswahl == "4":
            print("\nGuten Appetit!")
            break
        else:
            print("\n[FEHLER] Ungültige Eingabe - bitte 1-4 wählen")

if __name__ == "__main__":
    hauptmenu()
```

**Wichtige Code-Details:**

**Zutaten-Normalisierung (auch für Mehrwort-Zutaten):**
```python
def normalisiere_zutat(name):
    name = name.strip()
    if not name:
        return name
    
    # Jedes Wort einzeln normalisieren
    woerter = name.split()
    normalisiert = []
    for wort in woerter:
        if wort:
            wort_normalisiert = wort[0].upper() + wort[1:].lower()
            normalisiert.append(wort_normalisiert)
    
    return " ".join(normalisiert)
```
So wird "rote zwiebel" zu "Rote Zwiebel" (nicht "Rote zwiebel").

**Effiziente DB-Nutzung (eine Verbindung für alle Zutaten):**
```python
def fuege_zutaten_hinzu(zutaten_liste):
    # Eine Verbindung für alle Zutaten
    conn = sqlite3.connect(DB_DATEI)
    cursor = conn.cursor()
    
    for zutat in zutaten_normalisiert:
        cursor.execute(...)
        if cursor.rowcount > 0:
            anzahl_neu += 1
    
    conn.commit()  # Einmal am Ende
    conn.close()
```

**Duplikat-Entfernung im Rezept (case-insensitive):**
```python
zutaten_normalisiert = [normalisiere_zutat(z) for z in zutaten]
zutaten_unique = []
zutaten_lower_set = set()
for z in zutaten_normalisiert:
    if z.lower() not in zutaten_lower_set:
        zutaten_unique.append(z)
        zutaten_lower_set.add(z.lower())
```
Entfernt "Eier" und "eier" als Duplikat.

**Datei-Existenz prüfen (statt try/except FileNotFoundError):**
```python
if not os.path.exists(JSON_DATEI):
    print(f"INFO: {JSON_DATEI} nicht gefunden -> leere Liste")
    return []

# Datei existiert - jetzt sicher öffnen (kein FileNotFoundError)
with open(JSON_DATEI, "r", encoding="utf-8") as f:
    # ...
```

</details>

<details>
<summary>Hinweise zur Musterlösung</summary>

**Was du aus dem Code lernen kannst:**

**1. Struktur und Organisation:**
- Funktionen nach Zweck gruppiert (JSON, SQLite, Hauptfunktionen)
- Konstanten am Anfang (JSON_DATEI, DB_DATEI)
- Hilfsfunktionen vor Hauptfunktionen
- Hauptprogramm am Ende mit `if __name__ == "__main__"`

**2. Datenqualität:**
- **Normalisierung:** Alle Zutaten werden konsistent gespeichert
- **Mehrwort-Zutaten:** "Rote Zwiebel" bleibt "Rote Zwiebel" (nicht "Rote zwiebel")
- **Duplikat-Vermeidung:** Sowohl im Rezept als auch in der DB
- **UNIQUE in SQLite:** Verhindert doppelte Einträge automatisch
- **INSERT OR IGNORE:** Keine Fehler bei Duplikaten

**3. Effizienz:**
- Eine DB-Verbindung für alle Zutaten statt vieler einzelner
- `rowcount` nutzen um zu prüfen ob INSERT erfolgreich war
- Commit einmal am Ende statt nach jedem INSERT

**4. Benutzerfreundlichkeit:**
- Klare Fehlermeldungen mit [FEHLER], [OK], [INFO]
- Vorschläge bei Eingaben
- Sortierte Ausgaben
- Anzahl-Anzeigen
- Info über entfernte Duplikate

**5. Validierung ohne try/except:**
- `os.path.exists()` prüft Datei-Existenz bevor `open()` aufgerufen wird
- `strip()` und Prüfung auf leeren String
- `isdigit()` für Zahlen
- Explizite Werte-Prüfung (>= 1)
- JSON-Parse-Fehler werden bewusst nicht abgefangen (ok für diese Übung)

**6. SQLite ID-Handling:**
- IDs werden automatisch von SQLite vergeben durch `INTEGER PRIMARY KEY`
- Wir setzen die ID nicht selbst beim INSERT
- `AUTOINCREMENT` ist nicht nötig für diese Übung

**Wenn du die Musterlösung nutzt:**
- Lies den Code Zeile für Zeile
- Versuche jede Funktion zu verstehen
- Experimentiere: Ändere Werte, teste Edge Cases
- Vergleiche mit deiner Lösung: Was ist anders? Warum?

</details>

---

## Weiterführend: try/except Fehlerbehandlung

Diese Übung nutzt bewusst **keine try/except Blöcke**, da das Thema erst später ausführlich behandelt wird. Die Musterlösung zeigt alternative Ansätze:

**Statt try/except nutzen wir:**
- `os.path.exists()` für Datei-Existenz-Prüfung
- Explizite Validierung (if/else) für Eingaben
- Bewusstes "Crash lassen" bei ungültigem JSON

**Warum kein try/except FileNotFoundError:**
Wir prüfen die Datei-Existenz vorher mit `os.path.exists()`, dann scheitert `open()` nicht wegen FileNotFoundError (andere Fehler wie fehlende Rechte sind theoretisch möglich, aber nicht Fokus dieser Übung).

```python
# Ohne try/except:
if not os.path.exists(JSON_DATEI):
    return []
with open(JSON_DATEI, "r") as f:  # Kein FileNotFoundError
    # ...
```

**Warum kein try/except JSONDecodeError:**
Bei ungültigem JSON crasht das Programm mit Traceback - das ist für diese Übung ok, da wir die JSON-Datei manuell erstellen (sollte gültig sein).

**Wenn du try/except bereits kennst oder vorgreifen möchtest:**

<details>
<summary>Optionale Erweiterung mit try/except</summary>

So könnte `lade_rezepte()` mit vollständiger Fehlerbehandlung aussehen:

```python
def lade_rezepte():
    """Lädt Rezepte mit vollständiger Fehlerbehandlung"""
    try:
        with open(JSON_DATEI, "r", encoding="utf-8") as f:
            inhalt = f.read().strip()
            
            if not inhalt:
                print(f"INFO: {JSON_DATEI} ist leer -> leere Liste")
                return []
            
            rezepte = json.loads(inhalt)
            
            if not isinstance(rezepte, list):
                print("WARNUNG: JSON muss Liste sein -> leere Liste")
                return []
            
            return rezepte
    
    except FileNotFoundError:
        print(f"INFO: {JSON_DATEI} nicht gefunden -> leere Liste")
        return []
    
    except json.JSONDecodeError as e:
        print(f"FEHLER: Ungültiges JSON: {e}")
        print("TIPP: Prüfe die Syntax in rezepte.json")
        return []
    
    except Exception as e:
        print(f"FEHLER beim Laden: {e}")
        return []
```

**Vorteile von try/except:**
- Fängt alle Fehler ab (auch unerwartete)
- Programm stürzt nicht ab
- Detaillierte Fehlermeldungen möglich
- Robuster Code für Production

**Warum nicht in dieser Übung:**
- Fokus liegt auf JSON und SQLite Basics
- try/except ist ein eigenes, wichtiges Thema
- Alternative Ansätze zeigen: Es geht auch ohne
- Einfacherer Code für Anfänger

**Wann du try/except nutzen solltest:**
- Bei Datei-Operationen in Production-Code
- Bei Netzwerk-Anfragen
- Bei Benutzer-Eingaben (Typ-Konvertierungen)
- Generell: Wenn Code robust gegen Fehler sein soll

**Das lernen wir später ausführlich!**

</details>

---

## Lernziel-Check

Nach dieser Übung solltest du:

- JSON-Dateien mit Python lesen und schreiben können
- SQLite-Datenbanken erstellen und nutzen können  
- CRUD-Operationen (Create, Read) in beiden Formaten umsetzen können
- Verstehen wie man JSON und SQLite kombiniert
- Ein einfaches Menü-Programm strukturieren können
- Grundlegende Eingabe-Validierung durchführen können
- Datenqualität durch Normalisierung sicherstellen können
- Den Unterschied zwischen Minimalziel und Erweiterungen kennen
- Wissen warum `os.path.exists()` eine Alternative zu try/except ist
- Verstehen wie SQLite IDs automatisch vergibt

---

## Hilfreiche Ressourcen

Falls du nicht weiterkommst:

- **JSON mit Python:** Siehe "JSON mit Python - Übung" (Teil 1-3)
- **SQLite mit Python:** Siehe "SQLite mit Python - Übung" (Teil 1-3)
- **Python Basics:** Siehe vorherige Wochen (Listen, Dictionaries, Schleifen)

**Bei Problemen:**
1. Lies die Fehlermeldung genau
2. Prüfe ob alle Dateien existieren und korrekt formatiert sind
3. Teste Funktionen einzeln
4. Nutze `print()` zum Debuggen
5. Schau in die Musterlösung für konkrete Beispiele

**Häufige Stolpersteine:**

- **JSON-Datei:** 
  - Komma nach letztem Element vergessen? 
  - Doppelte Anführungszeichen `"` statt `'`?
  - `true`/`false` kleingeschrieben?
  
- **SQLite:** 
  - `commit()` vergessen? 
  - Connection geschlossen?
  - Parameter mit `?` statt f-strings?
  
- **Normalisierung:** 
  - Mehrwort-Zutaten richtig behandelt?
  - Vor Vergleich und beim Speichern normalisieren!
  
- **IDs:** 
  - JSON: Werden mit `naechste_id()` vergeben
  - SQLite: Werden automatisch von SQLite vergeben (INTEGER PRIMARY KEY)
  
- **Datei-Existenz:**
  - `os.path.exists()` vor `open()` prüfen!

---

**Viel Erfolg beim Programmieren!**
