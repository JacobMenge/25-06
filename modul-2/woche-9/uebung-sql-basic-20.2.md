# SQL Grundlagen - Von Null zur eigenen Datenbank

## Übersicht

In dieser Übung lernst du:
- **SQLite installieren** - Datenbank-Software unter Windows 11 einrichten
- **Datenbanken erstellen** - Deine erste eigene Datenbank anlegen
- **Tabellen bauen** - Schritt für Schritt Tabellen mit CREATE TABLE erstellen
- **Datentypen verstehen** - INTEGER, TEXT, REAL richtig einsetzen
- **Constraints nutzen** - PRIMARY KEY, NOT NULL, DEFAULT, CHECK
- **Daten einfügen** - Mit INSERT Zeilen hinzufügen
- **Daten lesen** - Mit SELECT abfragen
- **Daten ändern** - Mit UPDATE und DELETE arbeiten
- **Praktisch üben** - Eigene Datenbanken von Grund auf bauen

---

## Lernziele

**HAUPTZIEL: Eigene Datenbanken erstellen**
- Neue Datenbanken anlegen
- Tabellen mit sinnvoller Struktur erstellen
- Datentypen passend auswählen
- Primärschlüssel definieren
- Constraints richtig einsetzen
- Mehrere zusammenhängende Tabellen bauen

**GRUNDLEGENDE DATENBANKOPERATIONEN:**
- Daten mit INSERT einfügen
- Daten mit SELECT lesen
- Daten mit WHERE filtern
- Daten mit UPDATE ändern
- Daten mit DELETE löschen

---

## Aufbau der Übung

### TEIL 1: Installation & Erste Schritte
- SQLite installieren
- Erste Datenbank erstellen
- SQLite-Befehle kennenlernen

### TEIL 2: Tabellen erstellen (SCHWERPUNKT!)
- Was ist eine Tabelle?
- Datentypen verstehen
- CREATE TABLE Schritt für Schritt
- PRIMARY KEY
- NOT NULL
- DEFAULT
- CHECK
- Mehrere Tabellen erstellen
- Beziehungen zwischen Tabellen

### TEIL 3: Mit Daten arbeiten
- INSERT: Daten einfügen
- SELECT: Daten lesen
- WHERE: Daten filtern
- UPDATE: Daten ändern
- DELETE: Daten löschen

### TEIL 4: Praktische Projekte
- Eigene Datenbank von Grund auf bauen
- Verschiedene Szenarien durchspielen

---

## Teil 1: Installation & Erste Schritte

### SQLite unter Windows 11 installieren

#### Schritt 1: SQLite herunterladen

1. **Browser öffnen:** https://www.sqlite.org/download.html

2. **Zur Windows-Sektion scrollen:** "Precompiled Binaries for Windows"

3. **Diese Datei herunterladen:**
   ```
   sqlite-tools-win-x64-3510000.zip
   ```
   (oder neuere Version - die Zahl im Dateinamen entspricht der Version)
   - WICHTIG: Die "tools" Version, nicht "dll"!
   - Größe: etwa 6 MB

4. **ZIP entpacken:**
   - Rechtsklick → "Alle extrahieren"
   - Zielordner: `C:\sqlite`
   - Klicke auf "Extrahieren"

5. **Dateien prüfen in C:\sqlite:**
   - `sqlite3.exe` (das Hauptprogramm)
   - `sqldiff.exe`
   - `sqlite3_analyzer.exe`

#### Schritt 2: PATH-Variable setzen

Damit du SQLite von überall aufrufen kannst:

1. **Windows-Taste** drücken, tippe: `Umgebungsvariablen`
2. Klicke auf: "Systemumgebungsvariablen bearbeiten"
3. Klick auf "Umgebungsvariablen..."

**Option A: Benutzervariablen (empfohlen, keine Admin-Rechte nötig):**
4. Im **oberen** Bereich "Benutzervariablen" suche "Path"
5. Wähle "Path" → Klick "Bearbeiten..."
6. Klick "Neu"
7. Füge hinzu: `C:\sqlite`
8. Dreimal auf "OK"

**Option B: Systemvariablen (erfordert Admin-Rechte):**
4. Im **unteren** Bereich "Systemvariablen" suche "Path"
5. Wähle "Path" → Klick "Bearbeiten..."
6. Klick "Neu"
7. Füge hinzu: `C:\sqlite`
8. Dreimal auf "OK"

**Hinweis:** Option A (Benutzervariablen) reicht für persönliche Nutzung und funktioniert ohne Admin-Rechte.

#### Schritt 3: Installation testen

1. **Neue Eingabeaufforderung öffnen** (WICHTIG: NEU öffnen!)
   - Windows-Taste + R
   - Tippe: `cmd`
   - Enter

2. **SQLite testen:**
   ```cmd
   C:\> sqlite3 --version
   ```
   
   **Beispiel-Ausgabe (kann bei neueren Versionen abweichen):**
   ```
   3.51.0 2025-11-04 12:34:56 abc123def...
   ```

3. **Problem?** Siehe Troubleshooting unten.

<details>
<summary>Troubleshooting: "sqlite3 wird nicht erkannt"</summary>

**Lösung 1:** Neue Eingabeaufforderung öffnen
- Die PATH-Änderung wirkt nur in neu geöffneten Fenstern!
- Schließe alle cmd-Fenster und öffne ein neues

**Lösung 2:** Pfad prüfen
- Ist die Datei wirklich in `C:\sqlite\sqlite3.exe`?
- Stimmt der PATH-Eintrag?
- Öffne Umgebungsvariablen erneut und prüfe

**Lösung 3:** Direkter Pfad
- Nutze den vollen Pfad: `C:\sqlite\sqlite3.exe --version`
- Funktioniert das? Dann ist PATH falsch gesetzt

**Lösung 4:** Benutzerordner
- Wenn C:\ nicht geht, erstelle: `C:\Users\DeinName\sqlite`
- Entpacke SQLite dorthin
- Nutze diesen Pfad für PATH

</details>

#### Schritt 4: Arbeitsordner erstellen

1. **Ordner für deine SQL-Übungen:**
   ```
   C:\SQL-Uebungen
   ```
   Erstelle diesen Ordner im Windows Explorer

2. **Eingabeaufforderung in diesem Ordner öffnen:**
   - Ordner im Explorer öffnen
   - Klick in die Adressleiste
   - Tippe: `cmd`
   - Enter

   Jetzt bist du direkt im richtigen Ordner!

---

### Deine erste Datenbank erstellen

#### Was ist eine Datenbank?

Eine **Datenbank** ist eine Datei, die Daten organisiert speichert.

**Vergleich:**
- **Excel-Datei:** Eine Datei mit mehreren Tabellenblättern
- **Datenbank:** Eine Datei mit mehreren Tabellen

**Unterschied zu Excel:**
- Mächtiger für große Datenmengen
- Schneller bei Abfragen
- Bessere Datenintegrität
- Standard in der Programmierung

#### Datenbank-Datei erstellen

1. **In deinem Übungsordner (C:\SQL-Uebungen):**
   ```cmd
   C:\SQL-Uebungen> sqlite3 meine_erste_db.db
   ```

2. **SQLite öffnet sich - achte auf den geänderten Prompt:**
   ```
   SQLite version 3.51.0 2025-11-04 12:34:56
   Enter ".help" for usage hints.
   sqlite>
   ```

3. **Das `sqlite>` ist dein Prompt** - hier gibst du SQL-Befehle ein!

4. **Datenbank-Datei wurde erstellt:**
   - Schau in deinen Ordner
   - Du siehst: `meine_erste_db.db`
   - Das ist deine Datenbank!

**WICHTIGER HINWEIS zu Prompts:**
- `C:\>` oder `C:\SQL-Uebungen>` = Windows Eingabeaufforderung
- `sqlite>` = SQLite-Programm
- Befehle mit Punkt (`.help`, `.tables`) funktionieren **nur** im `sqlite>` Prompt!
- SQL-Befehle (SELECT, CREATE TABLE) funktionieren **nur** im `sqlite>` Prompt!

#### Wichtige SQLite-Befehle (mit Punkt!)

Diese Befehle beginnen mit einem Punkt und sind SQLite-spezifisch (funktionieren nur im `sqlite>` Prompt):

```sql
sqlite> .help              -- Zeigt alle Befehle
sqlite> .databases         -- Zeigt alle geöffneten Datenbanken
sqlite> .tables            -- Zeigt alle Tabellen
sqlite> .schema tabelle    -- Zeigt Struktur einer Tabelle
sqlite> .quit              -- Beendet SQLite (zurück zu C:\>)
```

**Bessere Darstellung aktivieren:**
```sql
sqlite> .mode column       -- Spalten schön formatiert
sqlite> .headers on        -- Spaltennamen anzeigen
```

**Diese zwei Befehle solltest du IMMER am Anfang eingeben!**

#### Erste Befehle ausprobieren

```sql
-- Welche Datenbanken sind geöffnet?
sqlite> .databases

-- Beispiel-Ausgabe:
-- main: C:\SQL-Uebungen\meine_erste_db.db r/w

-- Gibt es schon Tabellen?
sqlite> .tables

-- Ausgabe: (noch leer)

-- SQLite beenden:
sqlite> .quit

-- Jetzt bist du wieder in der Windows-Eingabeaufforderung:
C:\SQL-Uebungen>
```

---

### Selbstcheck: Installation

Bevor du weitermachst, prüfe:

- [ ] SQLite installiert und im PATH
- [ ] `sqlite3 --version` funktioniert in cmd
- [ ] Arbeitsordner C:\SQL-Uebungen erstellt
- [ ] Erste Datenbank meine_erste_db.db erstellt
- [ ] Unterschied zwischen `C:\>` und `sqlite>` verstanden
- [ ] `.mode column` und `.headers on` kennengelernt
- [ ] SQLite mit `.quit` beendet

**Alles erledigt? Perfekt! Weiter zu den Tabellen!**

---

## Teil 2: Tabellen erstellen - Der Schwerpunkt!

### Was ist eine Tabelle?

Eine **Tabelle** ist wie ein Tabellenblatt in Excel.

**Beispiel Adressbuch:**

```
| id | vorname | nachname | telefon      |
|----|---------|----------|--------------|
| 1  | Anna    | Schmidt  | 040-123456   |
| 2  | Ben     | Mueller  | 030-234567   |
| 3  | Clara   | Wagner   | 0421-345678  |
```

**Begriffe:**
- **Tabelle:** Das Ganze (wie "Adressbuch")
- **Spalte/Feld:** Eine Eigenschaft (z.B. "vorname")
- **Zeile/Datensatz:** Ein Eintrag (z.B. Anna Schmidt)
- **Wert:** Ein einzelnes Datum (z.B. "Anna")

### Warum Tabellen planen?

**Vor dem Erstellen überlegen:**

1. **Welche Daten will ich speichern?**
   - Beispiel: Kontakte → Name, Telefon, Email

2. **Welche Spalten brauche ich?**
   - id (zur Identifikation)
   - vorname
   - nachname
   - telefon
   - email

3. **Welche Datentypen passen?**
   - id → Zahl (INTEGER)
   - vorname → Text (TEXT)
   - telefon → Text (TEXT) - nicht Zahl wegen Vorwahl!

4. **Welche Regeln gelten?**
   - id muss eindeutig sein → PRIMARY KEY
   - Name ist Pflicht → NOT NULL

### Datentypen in SQLite

**Die wichtigsten Typen:**

| Datentyp | Wofür? | Beispiele |
|----------|--------|-----------|
| `INTEGER` | Ganze Zahlen | 1, 42, -100, 2024 |
| `REAL` | Kommazahlen | 3.14, 99.99, -0.5 |
| `TEXT` | Text/String | 'Anna', 'Hallo Welt', '040-123' |
| `BLOB` | Binärdaten | Bilder, Dateien |

**NULL** = Kein Wert / Unbekannt

**Wichtig:**
- SQLite ist flexibel (type affinity)
- Andere Datenbanken sind strenger
- Wir nutzen die richtigen Typen für gute Praxis!

#### Welcher Datentyp wofür?

**INTEGER nutzen für:**
- IDs (Kundennummer, Bestellnummer)
- Mengen (Anzahl, Stückzahl)
- Jahre (2024)
- Alter (25 Jahre)

**TEXT nutzen für:**
- Namen (Anna, Schmidt)
- Adressen (Hauptstraße 1)
- Emails (anna@example.com)
- **Telefonnummern (040-123456)** - Wichtig! Sonst gehen Vorwahlen verloren
- **PLZ (20095)** - Wichtig! Sonst gehen führende Nullen verloren (01234)
- Datumsangaben als String im ISO-Format ('2024-01-15')

**REAL nutzen für:**
- Preise (99.99)
- Prozentsätze (19.5)
- Gewichte (75.3)
- Messungen (3.14159)

**Hinweis zu Datumsangaben:**
SQLite hat keinen nativen DATE-Datentyp. Die übliche Praxis ist, Datumswerte als TEXT im ISO-Format `YYYY-MM-DD` zu speichern (z.B. '2025-01-15'). So können Datumswerte sortiert und verglichen werden.

**Faustregel:**
- Wird damit gerechnet? → INTEGER oder REAL
- Ist es Text? → TEXT
- Unsicher? → Lieber TEXT (funktioniert immer)

---

### Deine erste Tabelle erstellen

#### Übung 1: Einfache Kontakte-Tabelle

**Ziel:** Eine Tabelle für Kontakte mit ID, Vorname, Nachname

**Schritt 1: Datenbank öffnen**
```cmd
C:\SQL-Uebungen> sqlite3 kontakte.db
```

Du bist jetzt im SQLite-Prompt:
```
sqlite>
```

**Schritt 2: Darstellung verbessern**
```sql
sqlite> .mode column
sqlite> .headers on
```

**Schritt 3: Tabelle erstellen**
```sql
sqlite> CREATE TABLE kontakte (
   ...>     id INTEGER,
   ...>     vorname TEXT,
   ...>     nachname TEXT
   ...> );
```

Hinweis: Die `...>` zeigt an, dass SQL auf das abschließende Semikolon wartet.

**Was passiert:**
- `CREATE TABLE` = Erstelle Tabelle
- `kontakte` = Name der Tabelle
- In Klammern: Die Spalten
- `id INTEGER` = Spalte "id" vom Typ INTEGER
- Komma zwischen Spalten
- Semikolon am Ende

**Schritt 4: Prüfen ob's geklappt hat**
```sql
-- Gibt es jetzt Tabellen?
sqlite> .tables

-- Ausgabe: kontakte

-- Wie sieht die Struktur aus?
sqlite> .schema kontakte

-- Ausgabe zeigt:
-- CREATE TABLE kontakte (
--     id INTEGER,
--     vorname TEXT,
--     nachname TEXT
-- );
```

**Schritt 5: Erste Daten einfügen**
```sql
sqlite> INSERT INTO kontakte (id, vorname, nachname)
   ...> VALUES (1, 'Anna', 'Schmidt');

sqlite> INSERT INTO kontakte (id, vorname, nachname)
   ...> VALUES (2, 'Ben', 'Mueller');
```

**Schritt 6: Daten ansehen**
```sql
sqlite> SELECT * FROM kontakte;
```

**Ausgabe:**
```
id  vorname  nachname
--  -------  --------
1   Anna     Schmidt
2   Ben      Mueller
```

**Glückwunsch! Du hast deine erste Tabelle erstellt!**

<details>
<summary>Detaillierte Erklärung anzeigen</summary>

**CREATE TABLE Syntax:**
```sql
CREATE TABLE tabellenname (
    spalte1 datentyp,
    spalte2 datentyp,
    spalte3 datentyp
);
```

**Wichtige Regeln:**
1. `CREATE TABLE` ist das Kommando
2. Tabellenname danach (kleingeschrieben, keine Leerzeichen)
3. Spaltendefinitionen in runden Klammern `( )`
4. Jede Spalte: Name + Datentyp
5. Komma zwischen Spalten
6. KEIN Komma nach letzter Spalte!
7. Semikolon am Ende `;`

**Üblich:**
- Tabellennamen: Plural (kontakte, kunden, produkte)
- Spaltennamen: Singular, kleingeschrieben
- Keine Umlaute, keine Leerzeichen

**INSERT Syntax:**
```sql
INSERT INTO tabelle (spalte1, spalte2, spalte3)
VALUES (wert1, wert2, wert3);
```

- Text in 'einfachen Anführungszeichen'
- Zahlen ohne Anführungszeichen

**SELECT Syntax:**
```sql
SELECT * FROM tabelle;
```

- `*` bedeutet "alle Spalten"
- `FROM tabelle` gibt an wo

</details>

---

### PRIMARY KEY - Der eindeutige Schlüssel

#### Warum brauchen wir einen PRIMARY KEY?

**Problem ohne PRIMARY KEY:**
```sql
-- Zwei Annas mit gleicher ID?
sqlite> INSERT INTO kontakte VALUES (1, 'Anna', 'Schmidt');
sqlite> INSERT INTO kontakte VALUES (1, 'Anna', 'Mueller');  -- Gleiche ID!

-- Welche Anna meinst du?
sqlite> SELECT * FROM kontakte WHERE id = 1;
-- Beide Annas werden gefunden!
```

**Mit PRIMARY KEY:**
- ID ist **eindeutig** - keine Duplikate möglich
- Jede Zeile hat eine **klare Identifikation**
- Datenbank verhindert doppelte IDs automatisch

**Hinweis:** Ein PRIMARY KEY kann auch aus mehreren Spalten bestehen (Composite Primary Key), aber für den Anfang nutzen wir einfache Single-Column Primary Keys.

#### Übung 2: Tabelle mit PRIMARY KEY

Öffne eine neue Datenbank:
```cmd
C:\SQL-Uebungen> sqlite3 personen.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE personen (
   ...>     id INTEGER PRIMARY KEY,
   ...>     vorname TEXT,
   ...>     nachname TEXT
   ...> );
```

**Testen:**
```sql
-- Erste Person einfügen - funktioniert:
sqlite> INSERT INTO personen (id, vorname, nachname)
   ...> VALUES (1, 'Anna', 'Schmidt');

-- Zweite Person - funktioniert:
sqlite> INSERT INTO personen (id, vorname, nachname)
   ...> VALUES (2, 'Ben', 'Mueller');

-- Gleiche ID nochmal - FEHLER!
sqlite> INSERT INTO personen (id, vorname, nachname)
   ...> VALUES (1, 'Clara', 'Wagner');

-- Beispiel-Fehlermeldung (kann leicht variieren):
-- Error: UNIQUE constraint failed: personen.id
```

**Das ist gut! Die Datenbank schützt uns vor Fehlern!**

```sql
-- Daten ansehen:
sqlite> SELECT * FROM personen;
```

<details>
<summary>PRIMARY KEY im Detail</summary>

**Was ist ein PRIMARY KEY?**
- Eindeutige Kennzeichnung einer Zeile
- Wie ein Personalausweis - jeder hat eine einzigartige Nummer
- Darf nicht doppelt vorkommen
- Darf nicht NULL sein (automatisch)

**Eigenschaften:**
- Automatisch UNIQUE (eindeutig)
- Automatisch NOT NULL (muss Wert haben)
- Pro Tabelle kann es nur einen PRIMARY KEY geben (kann aber aus mehreren Spalten bestehen)
- Meist die erste Spalte (id)

**Typische Namen:**
- `id` (allgemein)
- `kundennummer` (spezifisch)
- `bestellnummer` (spezifisch)
- `produktnummer` (spezifisch)

**Best Practice:**
- Jede Tabelle sollte einen PRIMARY KEY haben!
- Meist eine einfache Zahl (INTEGER)

</details>

---

### Automatische IDs mit INTEGER PRIMARY KEY

#### Das Problem mit manuellen IDs

```sql
-- Jedes Mal müssen wir uns die nächste ID merken:
sqlite> INSERT INTO personen VALUES (1, 'Anna', 'Schmidt');
sqlite> INSERT INTO personen VALUES (2, 'Ben', 'Mueller');
sqlite> INSERT INTO personen VALUES (3, 'Clara', 'Wagner');  -- Welche Nummer jetzt?

-- Was wenn wir eine löschen?
sqlite> DELETE FROM personen WHERE id = 2;
-- Ist 2 jetzt frei? Können wir 2 wieder nutzen?
```

**Lösung: SQLite vergibt IDs automatisch!**

#### Übung 3: Automatische IDs

**WICHTIG:** In SQLite reicht `INTEGER PRIMARY KEY` für automatische IDs!

```cmd
C:\SQL-Uebungen> sqlite3 mitarbeiter.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE mitarbeiter (
   ...>     id INTEGER PRIMARY KEY,
   ...>     vorname TEXT,
   ...>     nachname TEXT,
   ...>     abteilung TEXT
   ...> );
```

**Testen - ID einfach weglassen:**
```sql
-- ID wird automatisch vergeben!
sqlite> INSERT INTO mitarbeiter (vorname, nachname, abteilung)
   ...> VALUES ('Anna', 'Schmidt', 'IT');

sqlite> INSERT INTO mitarbeiter (vorname, nachname, abteilung)
   ...> VALUES ('Ben', 'Mueller', 'Vertrieb');

sqlite> INSERT INTO mitarbeiter (vorname, nachname, abteilung)
   ...> VALUES ('Clara', 'Wagner', 'IT');

-- Ansehen:
sqlite> SELECT * FROM mitarbeiter;
```

**Ausgabe:**
```
id  vorname  nachname  abteilung
--  -------  --------  ---------
1   Anna     Schmidt   IT
2   Ben      Mueller   Vertrieb
3   Clara    Wagner    IT
```

**Die IDs wurden automatisch vergeben!**

<details>
<summary>Automatische IDs verstehen</summary>

**Wie funktioniert das in SQLite?**
- `INTEGER PRIMARY KEY` nutzt intern SQLites ROWID
- Wenn du die ID beim INSERT weglässt, wird automatisch die nächste freie Nummer vergeben
- Startet bei 1
- Erhöht sich bei jedem INSERT

**Wann AUTOINCREMENT verwenden?**

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

**AUTOINCREMENT ist in den meisten Fällen NICHT nötig!**

Unterschied:
- **INTEGER PRIMARY KEY:** Wiederverwendet gelöschte IDs (nach VACUUM)
- **INTEGER PRIMARY KEY AUTOINCREMENT:** Wiederverwendet NIE gelöschte IDs

**Wann AUTOINCREMENT nutzen:**
- Wenn du garantieren willst, dass IDs nie wiederverwendet werden
- Bei Audit-Logs oder gesetzlichen Anforderungen
- Wenn gelöschte IDs nicht neu vergeben werden dürfen

**Für den Alltag:**
- `INTEGER PRIMARY KEY` reicht völlig
- Weniger Overhead
- SQLite-Dokumentation empfiehlt: "AUTOINCREMENT is usually not needed"

**Beim INSERT:**
```sql
-- ID weglassen (empfohlen):
INSERT INTO mitarbeiter (vorname, nachname)
VALUES ('David', 'Klein');

-- ID explizit angeben (selten nötig):
INSERT INTO mitarbeiter (id, vorname, nachname)
VALUES (10, 'Emma', 'Fischer');
-- Nächste Auto-ID wird dann 11 sein
```

**Was passiert bei DELETE?**
```sql
DELETE FROM mitarbeiter WHERE id = 2;
-- Ben ist weg

INSERT INTO mitarbeiter (vorname, nachname)
VALUES ('Felix', 'Bauer');
-- Felix bekommt ID 4 (nicht 2!)
-- 2 wird erst nach VACUUM wiederverwendet (bei INTEGER PRIMARY KEY ohne AUTOINCREMENT)
```

**Best Practice:**
- Nutze `INTEGER PRIMARY KEY` für automatische IDs
- Lass die Datenbank die IDs verwalten
- Gib IDs nicht manuell an (außer bei speziellen Anforderungen)
- AUTOINCREMENT nur bei echtem Bedarf (Audit, nie wiederverwenden)

</details>

---

### NOT NULL - Pflichtfelder definieren

#### Warum NOT NULL?

**Ohne NOT NULL:**
```sql
sqlite> CREATE TABLE kunden (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT,
   ...>     email TEXT
   ...> );

-- Das funktioniert - aber ist es sinnvoll?
sqlite> INSERT INTO kunden (id, name) VALUES (1, 'Anna');
-- Kunde ohne Email!

sqlite> INSERT INTO kunden (id, email) VALUES (2, 'ben@example.com');
-- Kunde ohne Name!
```

**Problem:** Wichtige Daten fehlen!

**Mit NOT NULL:**
```sql
sqlite> CREATE TABLE kunden (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT NOT NULL,
   ...>     email TEXT NOT NULL
   ...> );

-- Jetzt MUSS beides angegeben werden!
```

#### Übung 4: Tabelle mit NOT NULL

```cmd
C:\SQL-Uebungen> sqlite3 kunden.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE kunden (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT NOT NULL,
   ...>     email TEXT NOT NULL,
   ...>     telefon TEXT
   ...> );
```

**Testen:**
```sql
-- Funktioniert (alles angegeben):
sqlite> INSERT INTO kunden (name, email, telefon)
   ...> VALUES ('Anna Schmidt', 'anna@example.com', '040-123456');

-- Funktioniert (telefon ist optional):
sqlite> INSERT INTO kunden (name, email)
   ...> VALUES ('Ben Mueller', 'ben@example.com');

-- FEHLER (name fehlt):
sqlite> INSERT INTO kunden (email)
   ...> VALUES ('clara@example.com');
-- Beispiel-Fehlermeldung:
-- Error: NOT NULL constraint failed: kunden.name

-- FEHLER (email fehlt):
sqlite> INSERT INTO kunden (name)
   ...> VALUES ('David Klein');
-- Error: NOT NULL constraint failed: kunden.email

-- Daten ansehen:
sqlite> SELECT * FROM kunden;
```

<details>
<summary>NOT NULL im Detail</summary>

**Was bedeutet NOT NULL?**
- Spalte MUSS einen Wert haben
- NULL ist nicht erlaubt
- Bei INSERT muss Wert angegeben werden

**Wann NOT NULL nutzen?**

**JA für:**
- Namen (kein Kunde ohne Namen)
- Email (wenn für Login benötigt)
- Wichtige Kennzahlen
- Pflichtangaben

**NEIN für:**
- Optionale Daten
- Telefonnummer (nicht jeder hat eine)
- Zweiter Vorname
- Bemerkungen

**Syntax:**
```sql
spalte DATENTYP NOT NULL
```

**Beispiele:**
```sql
CREATE TABLE produkte (
    id INTEGER PRIMARY KEY,
    produktname TEXT NOT NULL,          -- Pflicht
    preis REAL NOT NULL,                -- Pflicht
    beschreibung TEXT,                   -- Optional (NULL erlaubt)
    lieferant TEXT                       -- Optional
);
```

**Was ist NULL?**
- NULL = "kein Wert" / "unbekannt"
- Nicht: 0 (Null ist eine Zahl!)
- Nicht: '' (leerer String)
- NULL ist "nichts"

**Prüfen auf NULL:**
```sql
SELECT * FROM kunden WHERE telefon IS NULL;
-- Findet Kunden ohne Telefon

SELECT * FROM kunden WHERE telefon IS NOT NULL;
-- Findet Kunden mit Telefon
```

</details>

---

### DEFAULT - Standardwerte setzen

#### Warum DEFAULT?

**Oft gibt es sinnvolle Standardwerte:**
- Status: 'aktiv'
- Erstelldatum: Heute
- Anzahl: 0
- Land: 'Deutschland'

#### Übung 5: Tabelle mit DEFAULT

```cmd
C:\SQL-Uebungen> sqlite3 aufgaben.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE aufgaben (
   ...>     id INTEGER PRIMARY KEY,
   ...>     titel TEXT NOT NULL,
   ...>     beschreibung TEXT,
   ...>     status TEXT DEFAULT 'offen',
   ...>     prioritaet INTEGER DEFAULT 3
   ...> );
```

**Testen:**
```sql
-- Ohne status und prioritaet (nutzt Defaults):
sqlite> INSERT INTO aufgaben (titel, beschreibung)
   ...> VALUES ('Datenbank lernen', 'SQL-Grundlagen üben');

-- status und prioritaet werden automatisch gesetzt!
sqlite> SELECT * FROM aufgaben;
```

**Ausgabe:**
```
id  titel               beschreibung         status  prioritaet
--  ------------------  -------------------  ------  ----------
1   Datenbank lernen    SQL-Grundlagen üben  offen   3
```

**Eigene Werte angeben (überschreibt Default):**
```sql
sqlite> INSERT INTO aufgaben (titel, status, prioritaet)
   ...> VALUES ('Wichtige Aufgabe', 'dringend', 1);

sqlite> SELECT * FROM aufgaben;
```

**Ausgabe:**
```
id  titel               beschreibung         status    prioritaet
--  ------------------  -------------------  --------  ----------
1   Datenbank lernen    SQL-Grundlagen üben  offen     3
2   Wichtige Aufgabe                         dringend  1
```

<details>
<summary>DEFAULT verstehen</summary>

**Was macht DEFAULT?**
- Setzt automatisch einen Wert
- Wenn bei INSERT nichts angegeben wird
- Macht Spalte praktisch "optional"

**Syntax:**
```sql
spalte DATENTYP DEFAULT wert
```

**Beispiele:**
```sql
CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY,
    bestelldatum TEXT DEFAULT CURRENT_DATE,     -- Heutiges Datum
    status TEXT DEFAULT 'neu',                  -- Text-Default
    versandkosten REAL DEFAULT 4.99,            -- Zahl-Default
    bezahlt INTEGER DEFAULT 0                   -- 0 = nein, 1 = ja
);
```

**DEFAULT mit NOT NULL kombinieren:**
```sql
status TEXT NOT NULL DEFAULT 'offen'
-- Pflichtfeld, aber hat Standardwert
-- Muss nicht angegeben werden (Default wird genutzt)
```

**Nützliche Defaults:**

| Spaltentyp | Guter Default |
|------------|---------------|
| Status | 'aktiv', 'offen', 'neu' |
| Datum | CURRENT_DATE |
| Zeitstempel | CURRENT_TIMESTAMP |
| Zähler | 0 |
| Boolean (Ja/Nein) | 0 (=nein) |
| Land | 'Deutschland' |

**CURRENT_DATE und CURRENT_TIMESTAMP:**
```sql
erstellt TEXT DEFAULT CURRENT_DATE
-- Setzt automatisch aktuelles Datum: '2025-01-15'

erstellt TEXT DEFAULT CURRENT_TIMESTAMP
-- Setzt Datum + Zeit: '2025-01-15 14:30:25'
```

</details>

---

### CHECK - Bedingungen prüfen

#### Warum CHECK?

**Manche Werte machen keinen Sinn:**
- Preis: -10 Euro (negativ!)
- Alter: 150 Jahre (unrealistisch!)
- Prozent: 120% (über 100!)

**CHECK verhindert unsinnige Werte!**

#### Übung 6: Tabelle mit CHECK

```cmd
C:\SQL-Uebungen> sqlite3 produkte.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE produkte (
   ...>     id INTEGER PRIMARY KEY,
   ...>     produktname TEXT NOT NULL,
   ...>     preis REAL NOT NULL CHECK(preis > 0),
   ...>     lagerbestand INTEGER CHECK(lagerbestand >= 0)
   ...> );
```

**Testen:**
```sql
-- Funktioniert (alles in Ordnung):
sqlite> INSERT INTO produkte (produktname, preis, lagerbestand)
   ...> VALUES ('Laptop', 899.99, 10);

sqlite> INSERT INTO produkte (produktname, preis, lagerbestand)
   ...> VALUES ('Maus', 24.99, 50);

-- FEHLER (negativer Preis):
sqlite> INSERT INTO produkte (produktname, preis, lagerbestand)
   ...> VALUES ('Test', -100, 5);
-- Beispiel-Fehlermeldung:
-- Error: CHECK constraint failed: preis > 0

-- FEHLER (negativer Lagerbestand):
sqlite> INSERT INTO produkte (produktname, preis, lagerbestand)
   ...> VALUES ('Test', 50, -10);
-- Error: CHECK constraint failed: lagerbestand >= 0

-- FEHLER (Preis = 0 geht auch nicht):
sqlite> INSERT INTO produkte (produktname, preis, lagerbestand)
   ...> VALUES ('Gratis', 0, 10);
-- Error: CHECK constraint failed: preis > 0
```

**Die Datenbank schützt uns vor unsinnigen Werten!**

<details>
<summary>CHECK im Detail</summary>

**Was macht CHECK?**
- Prüft eine Bedingung
- INSERT/UPDATE nur wenn Bedingung erfüllt
- Verhindert unsinnige Daten

**Syntax:**
```sql
spalte DATENTYP CHECK(bedingung)
```

**Operatoren in CHECK:**
```sql
CHECK(preis > 0)          -- Größer
CHECK(preis >= 0)         -- Größer oder gleich
CHECK(alter < 150)        -- Kleiner
CHECK(alter <= 120)       -- Kleiner oder gleich
CHECK(menge > 0)          -- Nicht null oder negativ
```

**CHECK mit Bereichen:**
```sql
CHECK(alter BETWEEN 0 AND 120)
-- Zwischen 0 und 120 (inklusive)

CHECK(prozent >= 0 AND prozent <= 100)
-- 0 bis 100 Prozent
```

**CHECK mit Listen:**
```sql
CHECK(status IN ('offen', 'in Arbeit', 'erledigt'))
-- Nur diese drei Werte erlaubt

CHECK(groesse IN ('S', 'M', 'L', 'XL'))
-- Nur bestimmte Größen
```

**Beispiele:**
```sql
CREATE TABLE personal (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    alter INTEGER CHECK(alter >= 18 AND alter <= 67),
    gehalt REAL CHECK(gehalt > 0),
    wochenstunden INTEGER CHECK(wochenstunden BETWEEN 1 AND 40)
);

CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY,
    status TEXT CHECK(status IN ('neu', 'versendet', 'geliefert')),
    prioritaet INTEGER CHECK(prioritaet BETWEEN 1 AND 5)
);
```

**CHECK vs. NOT NULL:**
```sql
-- NOT NULL: Wert MUSS da sein
spalte TEXT NOT NULL

-- CHECK: Wert muss Bedingung erfüllen (NULL ist oft OK!)
spalte INTEGER CHECK(spalte > 0)
-- NULL ist hier erlaubt!

-- Beides kombinieren:
spalte INTEGER NOT NULL CHECK(spalte > 0)
-- Muss da sein UND positiv
```

**Hinweis zu Fehlermeldungen:**
Die genauen Fehlermeldungen können je nach SQLite-Version leicht variieren. Wichtig ist, dass der CHECK-Constraint die ungültigen Werte verhindert.

</details>

---

### Große Übung: Komplette Tabelle erstellen

Jetzt nutzen wir alles zusammen!

**Aufgabe:** Erstelle eine Tabelle für eine Schülerverwaltung

```cmd
C:\SQL-Uebungen> sqlite3 schule.db
```

```sql
sqlite> .mode column
sqlite> .headers on

sqlite> CREATE TABLE schueler (
   ...>     id INTEGER PRIMARY KEY,
   ...>     vorname TEXT NOT NULL,
   ...>     nachname TEXT NOT NULL,
   ...>     geburtsdatum TEXT,
   ...>     klasse TEXT NOT NULL,
   ...>     notendurchschnitt REAL CHECK(notendurchschnitt BETWEEN 1.0 AND 6.0),
   ...>     aktiv INTEGER DEFAULT 1 CHECK(aktiv IN (0, 1))
   ...> );
```

**Testdaten einfügen:**
```sql
sqlite> INSERT INTO schueler (vorname, nachname, geburtsdatum, klasse, notendurchschnitt)
   ...> VALUES ('Anna', 'Schmidt', '2008-05-15', '10a', 2.1);

sqlite> INSERT INTO schueler (vorname, nachname, geburtsdatum, klasse, notendurchschnitt)
   ...> VALUES ('Ben', 'Mueller', '2008-03-22', '10a', 1.8);

sqlite> INSERT INTO schueler (vorname, nachname, klasse, notendurchschnitt)
   ...> VALUES ('Clara', 'Wagner', '10b', 2.5);

-- Ansehen:
sqlite> SELECT * FROM schueler;

-- Verschiedene Abfragen:
sqlite> SELECT vorname, nachname, notendurchschnitt FROM schueler;
sqlite> SELECT * FROM schueler WHERE klasse = '10a';
sqlite> SELECT * FROM schueler WHERE notendurchschnitt < 2.0;
```

---

### Selbstcheck: CREATE TABLE

Bevor du weitermachst, prüfe dein Verständnis:

1. Was macht `CREATE TABLE`?
2. Welche Datentypen gibt es? (INTEGER, TEXT, REAL)
3. Was ist ein PRIMARY KEY?
4. Reicht `INTEGER PRIMARY KEY` für automatische IDs?
5. Wann nutze ich NOT NULL?
6. Wofür ist DEFAULT gut?
7. Was prüft CHECK?

<details>
<summary>Antworten anzeigen</summary>

1. `CREATE TABLE` erstellt eine neue, leere Tabelle mit definierter Struktur
2. INTEGER (ganze Zahlen), TEXT (Text), REAL (Kommazahlen), BLOB (Binärdaten)
3. PRIMARY KEY ist die eindeutige Kennzeichnung einer Zeile - wie ein Personalausweis
4. Ja! `INTEGER PRIMARY KEY` reicht völlig für automatische IDs. AUTOINCREMENT ist meist unnötig
5. NOT NULL bei Pflichtfeldern - wenn der Wert unbedingt benötigt wird
6. DEFAULT setzt automatisch einen Wert, wenn keiner angegeben wird
7. CHECK prüft ob ein Wert sinnvoll ist (z.B. Preis > 0, Alter zwischen 0 und 120)

</details>

---

## Teil 3: Mit Daten arbeiten

### INSERT - Daten einfügen

Du kennst INSERT schon aus den vorherigen Übungen!

**Grundsyntax:**
```sql
INSERT INTO tabelle (spalte1, spalte2, spalte3)
VALUES (wert1, wert2, wert3);
```

#### Verschiedene Arten INSERT zu nutzen

**1. Alle Spalten angeben (empfohlen):**
```sql
sqlite> INSERT INTO personen (id, vorname, nachname)
   ...> VALUES (1, 'Anna', 'Schmidt');
```

**2. Spalten in beliebiger Reihenfolge:**
```sql
sqlite> INSERT INTO personen (nachname, vorname, id)
   ...> VALUES ('Mueller', 'Ben', 2);
```

**3. Nur manche Spalten (Rest wird NULL oder Default):**
```sql
sqlite> INSERT INTO personen (vorname, nachname)
   ...> VALUES ('Clara', 'Wagner');
-- id wird automatisch vergeben (INTEGER PRIMARY KEY)
```

**4. Mehrere Zeilen gleichzeitig:**
```sql
sqlite> INSERT INTO personen (vorname, nachname)
   ...> VALUES 
   ...>     ('David', 'Klein'),
   ...>     ('Emma', 'Fischer'),
   ...>     ('Felix', 'Bauer');
```

---

### SELECT - Daten lesen

**Grundsyntax:**
```sql
SELECT spalten FROM tabelle;
```

#### Alle Spalten:
```sql
sqlite> SELECT * FROM personen;
```

#### Bestimmte Spalten:
```sql
sqlite> SELECT vorname, nachname FROM personen;
```

#### Mit WHERE filtern:
```sql
sqlite> SELECT * FROM personen WHERE vorname = 'Anna';
```

---

### UPDATE - Daten ändern

**WICHTIG: Immer mit WHERE, sonst werden ALLE Zeilen geändert!**

**Syntax:**
```sql
UPDATE tabelle
SET spalte = wert
WHERE bedingung;
```

#### Beispiele:
```sql
-- Email ändern:
sqlite> UPDATE kunden
   ...> SET email = 'neue_email@example.com'
   ...> WHERE id = 1;

-- Mehrere Spalten ändern:
sqlite> UPDATE kunden
   ...> SET email = 'anna.neu@example.com', telefon = '040-999999'
   ...> WHERE id = 1;

-- GEFAHR! Ohne WHERE werden ALLE geändert:
-- UPDATE kunden SET email = 'test@example.com';
-- Jetzt haben ALLE Kunden die gleiche Email!
```

**Best Practice: Erst prüfen, dann ändern:**
```sql
-- 1. Schauen was geändert würde:
sqlite> SELECT * FROM kunden WHERE id = 1;

-- 2. Dann ändern:
sqlite> UPDATE kunden SET email = 'neu@example.com' WHERE id = 1;

-- 3. Prüfen ob's geklappt hat:
sqlite> SELECT * FROM kunden WHERE id = 1;
```

---

### DELETE - Daten löschen

**NOCH WICHTIGER: Immer mit WHERE, sonst wird ALLES gelöscht!**

**Syntax:**
```sql
DELETE FROM tabelle
WHERE bedingung;
```

#### Beispiele:
```sql
-- Eine Zeile löschen:
sqlite> DELETE FROM kunden WHERE id = 5;

-- Mehrere Zeilen löschen:
sqlite> DELETE FROM kunden WHERE stadt = 'Berlin';

-- GEFAHR! Ohne WHERE wird ALLES gelöscht:
-- DELETE FROM kunden;
-- Tabelle ist leer!
```

**Best Practice: Erst prüfen, dann löschen:**
```sql
-- 1. Schauen was gelöscht würde:
sqlite> SELECT * FROM kunden WHERE stadt = 'Berlin';

-- 2. Sicher dass diese gelöscht werden sollen?

-- 3. Dann löschen:
sqlite> DELETE FROM kunden WHERE stadt = 'Berlin';

-- 4. Prüfen:
sqlite> SELECT * FROM kunden;
```

---

### Übung 7: Eigene Datenbank erstellen

**Aufgabe:** Erstelle eine Kontaktverwaltung von Grund auf!

**Schritt 1: Neue Datenbank**
```cmd
C:\SQL-Uebungen> sqlite3 meine_kontakte.db
```

**Schritt 2: Darstellung einstellen**
```sql
sqlite> .mode column
sqlite> .headers on
```

**Schritt 3: Tabelle erstellen**
```sql
sqlite> CREATE TABLE kontakte (
   ...>     id INTEGER PRIMARY KEY,
   ...>     vorname TEXT NOT NULL,
   ...>     nachname TEXT NOT NULL,
   ...>     email TEXT,
   ...>     telefon TEXT,
   ...>     geburtstag TEXT,
   ...>     notizen TEXT
   ...> );
```

**Schritt 4: Deine Kontakte einfügen**
```sql
-- Füge dich selbst ein:
sqlite> INSERT INTO kontakte (vorname, nachname, email)
   ...> VALUES ('Dein Vorname', 'Dein Nachname', 'deine@email.com');

-- Füge Familie/Freunde ein:
sqlite> INSERT INTO kontakte (vorname, nachname, telefon)
   ...> VALUES ('Mama', 'Nachname', '0123-456789');

-- Noch mehr Kontakte:
sqlite> INSERT INTO kontakte (vorname, nachname, email, telefon)
   ...> VALUES 
   ...>     ('Max', 'Mustermann', 'max@example.com', '040-111111'),
   ...>     ('Lisa', 'Test', 'lisa@example.com', '030-222222');
```

**Schritt 5: Abfragen**
```sql
-- Alle Kontakte:
sqlite> SELECT * FROM kontakte;

-- Nur Namen und Emails:
sqlite> SELECT vorname, nachname, email FROM kontakte;

-- Kontakte mit Email:
sqlite> SELECT * FROM kontakte WHERE email IS NOT NULL;

-- Einen bestimmten Kontakt:
sqlite> SELECT * FROM kontakte WHERE vorname = 'Max';
```

**Schritt 6: Ändern**
```sql
-- Email aktualisieren:
sqlite> UPDATE kontakte
   ...> SET email = 'neue_email@example.com'
   ...> WHERE id = 1;

-- Notiz hinzufügen:
sqlite> UPDATE kontakte
   ...> SET notizen = 'Wichtiger Kontakt'
   ...> WHERE vorname = 'Max';
```

**Schritt 7: Löschen**
```sql
-- Einen Kontakt löschen (erst prüfen!):
sqlite> SELECT * FROM kontakte WHERE id = 5;
sqlite> DELETE FROM kontakte WHERE id = 5;
```

---

## Teil 4: Fortgeschrittene Themen (Optional)

Diese Themen sind optional - konzentriere dich erst auf die Basics!

### FOREIGN KEY - Tabellen verbinden

**Szenario:** Eine Schule mit Schülern und Klassen

**Wichtiger Hinweis:** SQLite erzwingt Foreign Keys nicht automatisch! Du musst sie pro Verbindung aktivieren:

```sql
sqlite> PRAGMA foreign_keys = ON;
```

**Zwei Tabellen:**
```sql
-- Erst PRAGMA setzen:
sqlite> PRAGMA foreign_keys = ON;

-- Klassen-Tabelle:
sqlite> CREATE TABLE klassen (
   ...>     klassen_id INTEGER PRIMARY KEY,
   ...>     klassenname TEXT NOT NULL UNIQUE,
   ...>     klassenlehrer TEXT
   ...> );

-- Schüler-Tabelle (mit Verweis auf Klasse):
sqlite> CREATE TABLE schueler (
   ...>     schueler_id INTEGER PRIMARY KEY,
   ...>     vorname TEXT NOT NULL,
   ...>     nachname TEXT NOT NULL,
   ...>     klassen_id INTEGER,
   ...>     FOREIGN KEY (klassen_id) REFERENCES klassen(klassen_id)
   ...> );
```

**Daten einfügen:**
```sql
-- Erst Klassen:
sqlite> INSERT INTO klassen (klassenname, klassenlehrer)
   ...> VALUES ('10a', 'Herr Schmidt');

sqlite> INSERT INTO klassen (klassenname, klassenlehrer)
   ...> VALUES ('10b', 'Frau Mueller');

-- Dann Schüler (müssen auf existierende Klasse verweisen):
sqlite> INSERT INTO schueler (vorname, nachname, klassen_id)
   ...> VALUES ('Anna', 'Test', 1);  -- Klasse 10a

sqlite> INSERT INTO schueler (vorname, nachname, klassen_id)
   ...> VALUES ('Ben', 'Test', 1);   -- Klasse 10a

sqlite> INSERT INTO schueler (vorname, nachname, klassen_id)
   ...> VALUES ('Clara', 'Test', 2); -- Klasse 10b

-- Dies würde FEHLSCHLAGEN (wenn PRAGMA foreign_keys = ON):
-- INSERT INTO schueler (vorname, nachname, klassen_id)
-- VALUES ('David', 'Test', 99);  -- Klasse 99 existiert nicht!
```

**WICHTIG:** Ohne `PRAGMA foreign_keys = ON;` würde SQLite auch ungültige klassen_id-Werte akzeptieren!

---

### ORDER BY - Sortieren

```sql
-- Alphabetisch nach Namen:
sqlite> SELECT * FROM kontakte
   ...> ORDER BY nachname;

-- Absteigend (Z nach A):
sqlite> SELECT * FROM kontakte
   ...> ORDER BY nachname DESC;
```

### LIMIT - Anzahl begrenzen

```sql
-- Nur die ersten 5:
sqlite> SELECT * FROM kontakte
   ...> LIMIT 5;

-- Die 3 neuesten (höchste IDs):
sqlite> SELECT * FROM kontakte
   ...> ORDER BY id DESC
   ...> LIMIT 3;
```

### COUNT - Zählen

```sql
-- Wie viele Kontakte gibt es?
sqlite> SELECT COUNT(*) FROM kontakte;

-- Wie viele haben Email?
sqlite> SELECT COUNT(email) FROM kontakte;
```

---

## Zusammenfassung

### Die wichtigsten Befehle

| Befehl | Wofür? | Beispiel |
|--------|--------|----------|
| `CREATE TABLE` | Tabelle erstellen | `CREATE TABLE name (...)` |
| `INSERT INTO` | Daten einfügen | `INSERT INTO tabelle VALUES (...)` |
| `SELECT` | Daten lesen | `SELECT * FROM tabelle` |
| `UPDATE` | Daten ändern | `UPDATE tabelle SET ... WHERE ...` |
| `DELETE` | Daten löschen | `DELETE FROM tabelle WHERE ...` |

### Die wichtigsten Constraints

| Constraint | Wofür? |
|------------|--------|
| `PRIMARY KEY` | Eindeutige ID |
| `NOT NULL` | Pflichtfeld |
| `DEFAULT` | Standardwert |
| `CHECK` | Bedingung prüfen |
| `UNIQUE` | Eindeutig (aber nicht Primary Key) |
| `FOREIGN KEY` | Beziehung zu anderer Tabelle (mit PRAGMA!) |

### Die goldenen Regeln

1. **Jede Tabelle braucht einen PRIMARY KEY**
2. **INTEGER PRIMARY KEY reicht für automatische IDs** (AUTOINCREMENT meist unnötig!)
3. **NOT NULL bei Pflichtfeldern**
4. **CHECK für sinnvolle Werte**
5. **IMMER WHERE bei UPDATE und DELETE**
6. **Plane deine Tabellen vorher**
7. **Teste mit SELECT bevor du änderst/löschst**
8. **Unterscheide cmd-Prompt (C:\>) und sqlite-Prompt (sqlite>)**
9. **Bei FOREIGN KEY: PRAGMA foreign_keys = ON setzen!**

### Typische Anfängerfehler

```
FEHLER: Komma nach letzter Spalte in CREATE TABLE
   CREATE TABLE test (
       id INTEGER PRIMARY KEY,
       name TEXT,
   );  -- Falsches Komma!

RICHTIG: Kein Komma nach letzter Spalte

FEHLER: WHERE vergessen bei UPDATE/DELETE
   UPDATE kunden SET stadt = 'Hamburg';
   -- ALLE Kunden haben jetzt diese Stadt!

RICHTIG: Immer WHERE angeben

FEHLER: Telefonnummer als INTEGER
   telefon INTEGER

RICHTIG: Telefonnummer als TEXT (wegen Vorwahl!)
   telefon TEXT

FEHLER: PLZ als INTEGER
   plz INTEGER

RICHTIG: PLZ als TEXT (wegen führender Null!)
   plz TEXT

FEHLER: PRIMARY KEY vergessen
   CREATE TABLE kunden (
       name TEXT,
       email TEXT
   );

RICHTIG: Jede Tabelle braucht PRIMARY KEY
   id INTEGER PRIMARY KEY

FEHLER: telefon = NULL prüfen
   WHERE telefon = NULL

RICHTIG: IS NULL verwenden
   WHERE telefon IS NULL

FEHLER: .mode und .headers in cmd eingeben
   C:\> .mode column  -- Funktioniert nicht!

RICHTIG: Nur im sqlite> Prompt
   sqlite> .mode column

FEHLER: AUTOINCREMENT als Standard
   id INTEGER PRIMARY KEY AUTOINCREMENT

BESSER: Meist reicht das
   id INTEGER PRIMARY KEY

FEHLER: FOREIGN KEY ohne PRAGMA
   CREATE TABLE ... FOREIGN KEY ...
   -- Wird nicht durchgesetzt!

RICHTIG: PRAGMA foreign_keys = ON; setzen
```

### Prompt-Übersicht

Unterscheide immer zwischen diesen beiden Prompts:

```
C:\SQL-Uebungen>           -- Windows Eingabeaufforderung
sqlite>                    -- SQLite-Programm
```

**In Windows-Eingabeaufforderung (C:\>):**
- sqlite3 starten
- Zwischen Ordnern wechseln (cd)
- SQLite beenden mit .quit bringt dich hierhin zurück

**Im SQLite-Prompt (sqlite>):**
- SQL-Befehle (CREATE, INSERT, SELECT, etc.)
- SQLite-Befehle mit Punkt (.tables, .schema, .quit)
- .quit beendet SQLite

### Nächste Schritte

1. **Übe, übe, übe!** Erstelle eigene Datenbanken
2. **Eigene Projekte:** Adressbuch, Aufgabenverwaltung, Rezeptsammlung
3. **Erweitere dein Wissen:** JOINs, Aggregationen, Subqueries
4. **Lerne SQL mit Python:** sqlite3-Modul
5. **Andere Datenbanken:** PostgreSQL, MySQL

**Du hast jetzt die Grundlagen! Zeit für eigene Projekte!**
