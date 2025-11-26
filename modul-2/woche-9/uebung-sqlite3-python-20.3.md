# SQLite mit Python - Datenbanken programmieren

## Übersicht

In dieser Übung lernst du:
- **Python mit SQLite verbinden** - sqlite3-Modul nutzen
- **Datenbanken aus Python erstellen** - Verbindung aufbauen mit connect()
- **Tabellen programmieren** - CREATE TABLE aus Python ausführen
- **Daten sicher einfügen** - Parameter mit ? nutzen (SQL-Injection vermeiden)
- **Daten auslesen** - SELECT mit fetchall() und fetchone()
- **Daten ändern** - UPDATE und DELETE mit WHERE
- **Änderungen speichern** - commit() richtig einsetzen
- **Praktisch programmieren** - Eigene Datenbankprogramme schreiben

**Voraussetzung:** Du solltest die SQL-Grundlagen kennen (CREATE TABLE, INSERT, SELECT, UPDATE, DELETE)

---

## Lernziele

**HAUPTZIEL: Datenbanken mit Python steuern**
- sqlite3-Modul importieren und nutzen
- Verbindung zu Datenbanken herstellen
- SQL-Befehle aus Python ausführen
- Ergebnisse verarbeiten
- Fehler vermeiden (SQL-Injection, vergessenes commit)

**CRUD-OPERATIONEN PROGRAMMIEREN:**
- CREATE: Tabellen anlegen
- INSERT: Daten einfügen mit Parametern
- SELECT: Daten lesen und verarbeiten
- UPDATE: Daten ändern
- DELETE: Daten löschen

---

## Aufbau der Übung

### TEIL 1: Python & SQLite Setup
- sqlite3 importieren
- Erste Verbindung
- Cursor verstehen

### TEIL 2: Tabellen aus Python erstellen
- CREATE TABLE ausführen
- commit() nutzen
- Verbindung schließen

### TEIL 3: Daten einfügen (INSERT)
- Parameter mit ? (WICHTIG!)
- Mehrere Datensätze
- SQL-Injection vermeiden

### TEIL 4: Daten lesen (SELECT)
- fetchall() für alle Zeilen
- fetchone() für eine Zeile
- Ergebnisse verarbeiten

### TEIL 5: Daten ändern & löschen
- UPDATE mit WHERE
- DELETE mit WHERE
- Änderungen speichern

### TEIL 6: Praktisches Projekt
- Komplettes Programm schreiben
- Best Practices anwenden

---

## Teil 1: Python & SQLite Setup

### Was ist sqlite3?

**sqlite3** ist ein Python-Modul (Standardbibliothek - meist vorinstalliert!)

**Was es macht:**
- Verbindet Python mit SQLite-Datenbanken
- Führt SQL-Befehle aus Python aus
- Holt Ergebnisse zurück nach Python

**Vergleich:**
- **Reine SQL:** Du tippst SQL-Befehle direkt in `sqlite3.exe`
- **Python + SQLite:** Dein Python-Programm führt SQL-Befehle aus

#### Verfügbarkeit prüfen

**Schnellcheck ob sqlite3 verfügbar ist:**

```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

**Erwartete Ausgabe:**
```
3.45.0
```
(oder eine andere Version)

**Falls Fehler:** sqlite3 ist nicht verfügbar - Python neu installieren oder andere Distribution nutzen.

**Tipp:** Python kann auch als SQLite-CLI dienen:
```bash
python -m sqlite3 kontakte.db
```
(Startet interaktive SQLite-Shell - wie `sqlite3.exe`)

---

### Erste Verbindung - Der Workflow

**Der Standard-Workflow:**

```
1. import sqlite3           → Modul laden
2. connect("datei.db")      → Verbindung öffnen
3. cursor()                 → "Ausführhilfe" erstellen
4. execute("SQL...")        → SQL-Befehl ausführen
5. commit()                 → Änderungen speichern (bei INSERT/UPDATE/DELETE)
6. close()                  → Verbindung schließen
```

#### Übung 1: Erste Verbindung

**Schritt 1: Python-Datei erstellen**

Erstelle eine neue Datei: `erste_verbindung.py`

**Schritt 2: Code schreiben**

```python
# sqlite3 importieren (Standardbibliothek - keine Installation nötig!)
import sqlite3

# Verbindung zur Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect("meine_erste_db.db")

# Bestätigung ausgeben
print("Verbindung erfolgreich!")
print(f"Datenbankdatei: meine_erste_db.db")

# Verbindung schließen
conn.close()
print("Verbindung geschlossen")
```

**Schritt 3: Programm ausführen**

```bash
python erste_verbindung.py
```

**Ausgabe:**
```
Verbindung erfolgreich!
Datenbankdatei: meine_erste_db.db
Verbindung geschlossen
```

**Schritt 4: Prüfen**

Schau in deinen Ordner - die Datei `meine_erste_db.db` wurde erstellt!

<details>
<summary>Was passiert im Detail?</summary>

**import sqlite3**
- Lädt das sqlite3-Modul
- Ist Teil von Python (Standard Library)
- Keine Installation mit pip nötig!

**conn = sqlite3.connect("meine_erste_db.db")**
- `connect()` öffnet/erstellt die Datenbankdatei
- Gibt ein "Connection"-Objekt zurück
- Wir speichern es in der Variable `conn`
- **Wichtig:** Der Pfad ist relativ zum aktuellen Arbeitsverzeichnis
- Die .db-Datei landet dort, wo du das Python-Skript ausführst
- Tipp: Nutze absoluten Pfad für festen Speicherort: `"C:/Pfad/zu/datenbank.db"`

**conn.close()**
- Schließt die Verbindung
- Wichtig: Immer schließen wenn fertig!
- Gibt Ressourcen frei

</details>

---

### Was ist ein Cursor?

Ein **Cursor** ist deine "Ausführhilfe" für SQL-Befehle.

**Vergleich:**
- **conn** = Verbindung zur Datenbank (die Leitung)
- **cursor** = Das Werkzeug zum Arbeiten (die Fernbedienung)

**Du brauchst beides:**
```python
conn = sqlite3.connect("datenbank.db")    # Verbindung
cursor = conn.cursor()                     # Cursor erstellen
cursor.execute("SELECT * FROM tabelle")    # SQL ausführen
```

#### Übung 2: Cursor nutzen

```python
import sqlite3

# Verbindung öffnen
conn = sqlite3.connect("test.db")

# Cursor erstellen
cursor = conn.cursor()

print("Cursor erstellt!")
print(f"Cursor-Objekt: {cursor}")

# Aufräumen
conn.close()
```

**Ausgabe:**
```
Cursor erstellt!
Cursor-Objekt: <sqlite3.Cursor object at 0x...>
```

---

## Teil 2: Tabellen aus Python erstellen

### CREATE TABLE mit execute()

**Syntax:**
```python
cursor.execute("SQL-BEFEHL")
conn.commit()  # Änderungen speichern!
```

#### Übung 3: Erste Tabelle erstellen

**Datei:** `tabelle_erstellen.py`

```python
import sqlite3

# Verbindung öffnen
conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS kontakte (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefon TEXT
    )
""")

# WICHTIG: Änderungen speichern!
conn.commit()

print("Tabelle 'kontakte' erfolgreich erstellt!")

# Verbindung schließen
conn.close()
```

**Programm ausführen:**
```bash
python tabelle_erstellen.py
```

**Ausgabe:**
```
Tabelle 'kontakte' erfolgreich erstellt!
```

**Prüfen mit sqlite3:**
```bash
sqlite3 kontakte.db
```

```sql
sqlite> .schema kontakte
-- Zeigt die Tabellenstruktur
```

<details>
<summary>Wichtige Punkte</summary>

**Dreifache Anführungszeichen """**
- Erlauben mehrzeilige Strings
- SQL-Befehl wird übersichtlicher
- Alternative: Alles in eine Zeile (unübersichtlich)

**IF NOT EXISTS**
- Verhindert Fehler beim erneuten Ausführen
- Tabelle wird nur erstellt, wenn sie noch nicht existiert
- Best Practice: Immer nutzen!

**conn.commit()**
- Speichert Änderungen dauerhaft in der Datenbank
- **Besonders wichtig bei:** INSERT, UPDATE, DELETE, REPLACE
- Bei DDL (CREATE TABLE) ist es Best Practice, aber nicht zwingend
- Als Faustregel: Commit nach allem, was "schreibt"
- Nicht bei SELECT nötig (nur Lesezugriff)

**AUTOINCREMENT**
- IDs werden automatisch vergeben
- Startet bei 1, erhöht sich automatisch
- Du musst id nicht manuell angeben

</details>

---

### commit() bei Datenänderungen nicht vergessen

```python
# FEHLER - Änderungen gehen verloren!
cursor.execute("INSERT INTO kontakte (name) VALUES ('Test')")
conn.close()  # Ohne commit()!

# RICHTIG - Änderungen werden gespeichert
cursor.execute("INSERT INTO kontakte (name) VALUES ('Test')")
conn.commit()  # Jetzt dauerhaft gespeichert!
conn.close()
```

**Merke:** INSERT, UPDATE, DELETE, REPLACE brauchen `commit()` für dauerhafte Speicherung!

**Noch besser: Context Manager nutzen (commit automatisch!):**

```python
# Automatisches commit bei Erfolg, rollback bei Fehler
with sqlite3.connect("kontakte.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kontakte (name) VALUES ('Test')")
    # commit() automatisch am Ende des with-Blocks!
```

---

## Teil 3: Daten einfügen (INSERT)

### KRITISCH: Parameter mit ? nutzen

**NIEMALS so machen (SQL-Injection-Gefahr!):**
```python
# GEFÄHRLICH! NIE SO MACHEN!
name = input("Name: ")
cursor.execute(f"INSERT INTO kontakte (name) VALUES ('{name}')")
```

**IMMER so machen (sicher):**
```python
# SICHER! Immer ? nutzen!
name = input("Name: ")
cursor.execute("INSERT INTO kontakte (name) VALUES (?)", (name,))
```

#### Warum ? wichtig ist (SQL-Injection)

**Beispiel-Angriff ohne ? bei einer Suche:**
```python
# UNSICHER - Angreifer kann WHERE-Klausel manipulieren!
email = input("Email suchen: ")  # Angreifer gibt ein: ' OR TRUE; --
cursor.execute(f"SELECT * FROM kontakte WHERE email = '{email}'")
# Führt aus: SELECT * FROM kontakte WHERE email = '' OR TRUE; --'
# Gibt ALLE Kontakte zurück, nicht nur den gesuchten!
```

**Mit ? ist das unmöglich:**
```python
# SICHER - Eingabe wird als reiner String behandelt
email = input("Email suchen: ")  # Angreifer gibt ein: ' OR TRUE; --
cursor.execute("SELECT * FROM kontakte WHERE email = ?", (email,))
# Die Eingabe wird als Literal-String behandelt - keine SQL-Manipulation möglich!
# Sucht nach einem Kontakt mit Email: ' OR TRUE; -- (findet nichts)
```

**Wichtig:** 
- `cursor.execute()` führt nur **ein** SQL-Statement aus
- Mehrere Statements (mit `;`) würden einen `ProgrammingError` werfen
- Aber: WHERE-Klausel-Manipulation funktioniert trotzdem!
- Deshalb: **IMMER** Parameter mit `?` nutzen!

---

#### Übung 4: Daten sicher einfügen

**Datei:** `daten_einfuegen.py`

```python
import sqlite3

# Verbindung öffnen
conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Einen Kontakt einfügen
cursor.execute(
    "INSERT INTO kontakte (name, email, telefon) VALUES (?, ?, ?)",
    ("Anna Schmidt", "anna@example.com", "040-123456")
)

# Änderungen speichern
conn.commit()

print("Kontakt erfolgreich eingefügt!")

# Verbindung schließen
conn.close()
```

**Ausgabe:**
```
Kontakt erfolgreich eingefügt!
```

**⚠️ Beim erneuten Ausführen:**

Wenn du das Skript nochmal ausführst, bekommst du einen Fehler:
```
sqlite3.IntegrityError: UNIQUE constraint failed: kontakte.email
```

**Grund:** Die Email `anna@example.com` existiert bereits (UNIQUE constraint)!

**Lösungen:**
1. Email im Code ändern vor erneutem Ausführen
2. Datenbank löschen: `kontakte.db` Datei löschen
3. Fehlerbehandlung einbauen (kommt in Übung 6 - Projekt)

<details>
<summary>Parameter verstehen</summary>

**Die ? Platzhalter:**
```python
execute("INSERT INTO tabelle (spalte1, spalte2) VALUES (?, ?)", (wert1, wert2))
```

- `?` = Platzhalter für einen Wert
- Werte kommen als Tuple: `(wert1, wert2)`
- Anzahl `?` muss mit Anzahl Werte übereinstimmen

**Wichtig bei einem Wert:**
```python
# Richtig (Tuple mit einem Element):
execute("INSERT INTO tabelle (spalte) VALUES (?)", (wert,))
#                                                         ^ Komma!

# Falsch:
execute("INSERT INTO tabelle (spalte) VALUES (?)", (wert))
# Ohne Komma ist das kein Tuple!
```

</details>

---

#### Übung 5: Mehrere Datensätze einfügen

**Variante A: Einzeln einfügen**

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Mehrere Kontakte nacheinander
kontakte = [
    ("Ben Mueller", "ben@example.com", "030-234567"),
    ("Clara Wagner", "clara@example.com", "0421-345678"),
    ("David Klein", "david@example.com", None)  # Kein Telefon
]

for kontakt in kontakte:
    cursor.execute(
        "INSERT INTO kontakte (name, email, telefon) VALUES (?, ?, ?)",
        kontakt
    )

conn.commit()  # EINMAL am Ende reicht!
print(f"{len(kontakte)} Kontakte eingefügt!")

conn.close()
```

**Variante B: executemany() nutzen (effizienter!)**

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

kontakte = [
    ("Emma Fischer", "emma@example.com", "040-456789"),
    ("Felix Bauer", "felix@example.com", "030-567890")
]

# executemany für mehrere Datensätze
cursor.executemany(
    "INSERT INTO kontakte (name, email, telefon) VALUES (?, ?, ?)",
    kontakte
)

conn.commit()
print(f"{len(kontakte)} Kontakte eingefügt!")

conn.close()
```

**⚠️ Hinweis:** Beim erneuten Ausführen gibt's UNIQUE-Fehler. Lösung: Andere Email-Adressen nutzen oder `INSERT OR IGNORE` verwenden (fügt nur ein, wenn Email noch nicht existiert):

```python
cursor.executemany(
    "INSERT OR IGNORE INTO kontakte (name, email, telefon) VALUES (?, ?, ?)",
    kontakte
)
```

---

## Teil 4: Daten lesen (SELECT)

### fetchall() - Alle Zeilen holen

#### Übung 6: Alle Kontakte auslesen

**Datei:** `daten_lesen.py`

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# SELECT ausführen
cursor.execute("SELECT id, name, email, telefon FROM kontakte")

# Alle Zeilen holen
rows = cursor.fetchall()

# Ausgeben
print(f"Anzahl Kontakte: {len(rows)}\n")

for row in rows:
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Email: {row[2]}")
    print(f"Telefon: {row[3]}")
    print("-" * 40)

conn.close()
```

**Ausgabe:**
```
Anzahl Kontakte: 5

ID: 1
Name: Anna Schmidt
Email: anna@example.com
Telefon: 040-123456
----------------------------------------
ID: 2
Name: Ben Mueller
Email: ben@example.com
Telefon: 030-234567
----------------------------------------
...
```

<details>
<summary>Ergebnisse verstehen</summary>

**fetchall() gibt eine Liste von Tuples zurück:**
```python
rows = cursor.fetchall()
# Ergebnis: [
#     (1, 'Anna Schmidt', 'anna@example.com', '040-123456'),
#     (2, 'Ben Mueller', 'ben@example.com', '030-234567'),
#     ...
# ]
```

**Zugriff auf Werte:**
```python
row = (1, 'Anna Schmidt', 'anna@example.com', '040-123456')
row[0]  # 1 (id)
row[1]  # 'Anna Schmidt' (name)
row[2]  # 'anna@example.com' (email)
row[3]  # '040-123456' (telefon)
```

**SELECT braucht KEIN commit():**
- Nur Leseoperation
- Ändert nichts in der Datenbank
- commit() nur bei INSERT/UPDATE/DELETE

</details>

---

### fetchone() - Eine Zeile holen

#### Übung 7: Bestimmten Kontakt suchen

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Einen bestimmten Kontakt suchen (mit Parameter!)
email_suche = "anna@example.com"

cursor.execute(
    "SELECT id, name, email, telefon FROM kontakte WHERE email = ?",
    (email_suche,)
)

# Eine Zeile holen
row = cursor.fetchone()

if row:
    print(f"Kontakt gefunden:")
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Email: {row[2]}")
    print(f"Telefon: {row[3]}")
else:
    print(f"Kein Kontakt mit Email '{email_suche}' gefunden")

conn.close()
```

**Unterschied fetchone() vs. fetchall():**

```python
# fetchall() - Gibt LISTE von Tuples zurück
rows = cursor.fetchall()  # [(1, 'Anna', ...), (2, 'Ben', ...)]
for row in rows:
    print(row)

# fetchone() - Gibt EIN Tuple zurück (oder None)
row = cursor.fetchone()   # (1, 'Anna', ...)
if row:
    print(row)
```

---

## Teil 5: Daten ändern & löschen

### UPDATE - Daten ändern

**WICHTIG: Immer mit WHERE, sonst werden ALLE Zeilen geändert!**

#### Übung 8: Kontakt aktualisieren

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Telefonnummer ändern
cursor.execute(
    "UPDATE kontakte SET telefon = ? WHERE email = ?",
    ("040-999999", "anna@example.com")
)

# Änderungen speichern!
conn.commit()

print(f"Geänderte Zeilen: {cursor.rowcount}")

conn.close()
```

**Ausgabe:**
```
Geänderte Zeilen: 1
```

<details>
<summary>rowcount verstehen</summary>

**cursor.rowcount**
- Zeigt Anzahl betroffener Zeilen
- Nützlich zur Kontrolle
- Bei UPDATE: Wie viele Zeilen wurden geändert?
- Bei DELETE: Wie viele Zeilen wurden gelöscht?
- **Hinweis:** Bei manchen Datenbanktreibern kann `rowcount` auch `-1` sein (nicht bestimmbar) - bei SQLite funktioniert es aber zuverlässig für UPDATE/DELETE

```python
cursor.execute("UPDATE kontakte SET telefon = ? WHERE id = ?", ("123", 999))
conn.commit()
print(cursor.rowcount)  # 0 (keine Zeile mit id=999 gefunden)

cursor.execute("UPDATE kontakte SET telefon = ? WHERE id = ?", ("123", 1))
conn.commit()
print(cursor.rowcount)  # 1 (eine Zeile geändert)
```

</details>

---

### DELETE - Daten löschen

**NOCH WICHTIGER: Immer mit WHERE, sonst wird ALLES gelöscht!**

#### Übung 9: Kontakt löschen

```python
import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

# Einen bestimmten Kontakt löschen
email_loeschen = "david@example.com"

# Sicherheitsabfrage (optional aber empfohlen)
cursor.execute("SELECT name FROM kontakte WHERE email = ?", (email_loeschen,))
row = cursor.fetchone()

if row:
    print(f"Kontakt '{row[0]}' wird gelöscht...")
    
    cursor.execute("DELETE FROM kontakte WHERE email = ?", (email_loeschen,))
    conn.commit()
    
    print(f"Gelöscht: {cursor.rowcount} Zeile(n)")
else:
    print(f"Kein Kontakt mit Email '{email_loeschen}' gefunden")

conn.close()
```

---

## Teil 6: Praktisches Projekt

### Kontaktverwaltung - Komplettes Programm

Erstelle ein vollständiges Programm mit Menü!

**Datei:** `kontaktverwaltung.py`

```python
import sqlite3

def datenbank_erstellen():
    """Erstellt die Datenbank und Tabelle"""
    conn = sqlite3.connect("kontakte.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kontakte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefon TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("Datenbank bereit!")

def kontakt_hinzufuegen():
    """Fügt einen neuen Kontakt hinzu"""
    name = input("Name: ")
    email = input("Email: ")
    telefon = input("Telefon (Enter für leer): ")
    
    if not telefon:
        telefon = None
    
    conn = sqlite3.connect("kontakte.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO kontakte (name, email, telefon) VALUES (?, ?, ?)",
            (name, email, telefon)
        )
        conn.commit()
        print("Kontakt erfolgreich hinzugefügt!")
    except sqlite3.IntegrityError:
        print("FEHLER: Email existiert bereits!")
    finally:
        conn.close()

def kontakte_anzeigen():
    """Zeigt alle Kontakte an"""
    conn = sqlite3.connect("kontakte.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, email, telefon FROM kontakte ORDER BY name")
    rows = cursor.fetchall()
    
    if not rows:
        print("Keine Kontakte vorhanden")
    else:
        print(f"\n{'ID':<5} {'Name':<20} {'Email':<30} {'Telefon':<15}")
        print("-" * 70)
        for row in rows:
            telefon = row[3] if row[3] else "-"
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<30} {telefon:<15}")
    
    conn.close()

def kontakt_suchen():
    """Sucht einen Kontakt nach Email"""
    email = input("Email suchen: ")
    
    conn = sqlite3.connect("kontakte.db")
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, name, email, telefon FROM kontakte WHERE email = ?",
        (email,)
    )
    row = cursor.fetchone()
    
    if row:
        print(f"\nKontakt gefunden:")
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Email: {row[2]}")
        print(f"Telefon: {row[3] if row[3] else '-'}")
    else:
        print("Kontakt nicht gefunden")
    
    conn.close()

def kontakt_loeschen():
    """Löscht einen Kontakt"""
    email = input("Email des zu löschenden Kontakts: ")
    
    conn = sqlite3.connect("kontakte.db")
    cursor = conn.cursor()
    
    # Erst anzeigen
    cursor.execute("SELECT name FROM kontakte WHERE email = ?", (email,))
    row = cursor.fetchone()
    
    if row:
        bestaetigung = input(f"'{row[0]}' wirklich löschen? (j/n): ")
        if bestaetigung.lower() == 'j':
            cursor.execute("DELETE FROM kontakte WHERE email = ?", (email,))
            conn.commit()
            print("Kontakt gelöscht!")
        else:
            print("Abgebrochen")
    else:
        print("Kontakt nicht gefunden")
    
    conn.close()

def hauptmenu():
    """Zeigt das Hauptmenü"""
    while True:
        print("\n" + "=" * 40)
        print("KONTAKTVERWALTUNG")
        print("=" * 40)
        print("1. Kontakt hinzufügen")
        print("2. Alle Kontakte anzeigen")
        print("3. Kontakt suchen")
        print("4. Kontakt löschen")
        print("5. Beenden")
        print("=" * 40)
        
        auswahl = input("Wähle eine Option (1-5): ")
        
        if auswahl == "1":
            kontakt_hinzufuegen()
        elif auswahl == "2":
            kontakte_anzeigen()
        elif auswahl == "3":
            kontakt_suchen()
        elif auswahl == "4":
            kontakt_loeschen()
        elif auswahl == "5":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe!")

if __name__ == "__main__":
    datenbank_erstellen()
    hauptmenu()
```

**Programm starten:**
```bash
python kontaktverwaltung.py
```

**Beispiel-Session:**
```
Datenbank bereit!

========================================
KONTAKTVERWALTUNG
========================================
1. Kontakt hinzufügen
2. Alle Kontakte anzeigen
3. Kontakt suchen
4. Kontakt löschen
5. Beenden
========================================
Wähle eine Option (1-5): 1
Name: Max Mustermann
Email: max@example.com
Telefon (Enter für leer): 040-123456
Kontakt erfolgreich hinzugefügt!
...
```

---

## Best Practices - Die wichtigsten Regeln

### 0. Context Manager nutzen (Empfohlen!)

**Der beste Weg: with-Statement**

```python
# BESTE PRAXIS - Automatisches commit/rollback
with sqlite3.connect("kontakte.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kontakte (name, email) VALUES (?, ?)", 
                   ("Anna", "anna@example.com"))
    # commit() wird automatisch aufgerufen bei Erfolg
    # rollback() bei Exception
# Connection wird automatisch geschlossen

# Vergleich zur manuellen Variante:
conn = sqlite3.connect("kontakte.db")
try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kontakte (name, email) VALUES (?, ?)", 
                   ("Anna", "anna@example.com"))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Fehler: {e}")
finally:
    conn.close()
```

**Vorteile:**
- Kein `commit()` vergessen
- Automatisches `rollback()` bei Fehlern
- Connection wird immer geschlossen
- Weniger Code, weniger Fehler

---

### 1. Immer ? für Parameter nutzen

```python
# FALSCH - SQL-Injection möglich!
name = "Anna"
cursor.execute(f"SELECT * FROM kontakte WHERE name = '{name}'")

# RICHTIG - Sicher!
name = "Anna"
cursor.execute("SELECT * FROM kontakte WHERE name = ?", (name,))
```

### 2. commit() nicht vergessen

```python
# Bei Änderungen IMMER commit()
cursor.execute("INSERT INTO kontakte ...")
conn.commit()  # WICHTIG!

# Bei SELECT NICHT nötig
cursor.execute("SELECT * FROM kontakte")
rows = cursor.fetchall()  # Kein commit() nötig
```

### 3. Verbindung schließen

```python
# Manuell schließen
conn = sqlite3.connect("db.db")
# ... Code ...
conn.close()  # Wichtig!

# ODER: with-Statement (automatisch)
with sqlite3.connect("db.db") as conn:
    # ... Code ...
# wird automatisch geschlossen
```

### 4. Fehlerbehandlung

```python
try:
    cursor.execute("INSERT INTO kontakte (name, email) VALUES (?, ?)", 
                   ("Anna", "anna@example.com"))
    conn.commit()
    print("Erfolgreich!")
except sqlite3.IntegrityError:
    print("Fehler: Email existiert bereits (UNIQUE)")
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
```

### 5. IF NOT EXISTS nutzen

```python
# Verhindert Fehler beim erneuten Ausführen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS kontakte (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")
```

---

## Zusammenfassung

### Die wichtigsten Befehle

| Befehl | Wofür? | Beispiel |
|--------|--------|----------|
| `import sqlite3` | Modul laden | `import sqlite3` |
| `connect()` | Verbindung öffnen | `conn = sqlite3.connect("db.db")` |
| `cursor()` | Cursor erstellen | `cur = conn.cursor()` |
| `execute()` | SQL ausführen | `cur.execute("SELECT * FROM t")` |
| `fetchall()` | Alle Zeilen holen | `rows = cur.fetchall()` |
| `fetchone()` | Eine Zeile holen | `row = cur.fetchone()` |
| `commit()` | Änderungen speichern | `conn.commit()` |
| `close()` | Verbindung schließen | `conn.close()` |

### Der Standard-Workflow

**Variante 1: Manuelle Verwaltung**

```python
import sqlite3

# 1. Verbindung öffnen
conn = sqlite3.connect("datenbank.db")

# 2. Cursor erstellen
cursor = conn.cursor()

# 3. SQL ausführen
cursor.execute("SQL-BEFEHL", (parameter,))

# 4. Bei Änderungen: commit()
conn.commit()

# 5. Bei SELECT: Ergebnisse holen
rows = cursor.fetchall()

# 6. Verbindung schließen
conn.close()
```

**Variante 2: Mit Context Manager (empfohlen!)**

```python
import sqlite3

# with-Statement: commit/close automatisch
with sqlite3.connect("datenbank.db") as conn:
    cursor = conn.cursor()
    
    # SQL ausführen
    cursor.execute("SQL-BEFEHL", (parameter,))
    
    # Bei SELECT: Ergebnisse holen
    rows = cursor.fetchall()
    
# commit() automatisch bei Erfolg
# close() automatisch am Ende
```

### Die goldenen Regeln

1. **Immer ? für Parameter** (SQL-Injection vermeiden - auch bei WHERE!)
2. **commit() bei INSERT/UPDATE/DELETE/REPLACE** (sonst gehen Änderungen verloren!)
3. **Kein commit() bei SELECT** (nur Lesevorgang)
4. **Verbindung immer schließen** (oder with-Statement nutzen - empfohlen!)
5. **IF NOT EXISTS bei CREATE TABLE** (Fehler bei erneutem Ausführen vermeiden)
6. **WHERE bei UPDATE/DELETE** (sonst werden ALLE Zeilen betroffen!)
7. **Fehlerbehandlung mit try/except** (besonders bei UNIQUE constraints)
8. **Bei wiederholtem Ausführen:** UNIQUE-Fehler beachten oder `INSERT OR IGNORE` nutzen

### Typische Anfängerfehler

```
FEHLER: Parameter nicht als Tuple
   execute("INSERT ... VALUES (?)", wert)
RICHTIG:
   execute("INSERT ... VALUES (?)", (wert,))  # Komma!

FEHLER: commit() vergessen bei Datenänderungen
   cursor.execute("INSERT ...")
   conn.close()  # Änderungen gehen verloren!
RICHTIG:
   cursor.execute("INSERT ...")
   conn.commit()  # Jetzt gespeichert!

FEHLER: SQL-Injection (f-strings in SQL)
   email = input()
   execute(f"SELECT * FROM t WHERE email = '{email}'")
   # Angreifer kann ' OR TRUE; -- eingeben!
RICHTIG:
   email = input()
   execute("SELECT * FROM t WHERE email = ?", (email,))

FEHLER: WHERE bei UPDATE vergessen
   execute("UPDATE kontakte SET name = 'Test'")  # ALLE geändert!
RICHTIG:
   execute("UPDATE kontakte SET name = ? WHERE id = ?", ("Test", 1))

FEHLER: Skript mehrfach ausführen ohne UNIQUE zu beachten
   # Zweiter Durchlauf: IntegrityError bei gleichen Emails
LÖSUNG:
   INSERT OR IGNORE oder try/except nutzen

FEHLER: Arbeitsverzeichnis nicht beachten
   # Wo ist meine .db-Datei? Im aktuellen Verzeichnis!
LÖSUNG:
   Absoluten Pfad nutzen oder Verzeichnis kennen
```
