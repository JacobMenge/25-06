# Linux Praxis Challenge: sed & awk
*Für Windows 11 mit WSL (Windows Subsystem for Linux)*

---

## Überblick der Challenge

In dieser Challenge lernst du zwei der mächtigsten Werkzeuge für die automatisierte Textverarbeitung in Linux kennen: **sed** (Stream Editor) und **awk** (Programmiersprache für strukturierte Daten). Diese Tools sind unverzichtbar für jeden, der regelmäßig mit Textdateien, Logs oder Daten arbeitet.

**Was sind sed und awk genau?**
- **sed** ist ein "Stream Editor" - er verarbeitet Text zeilenweise, ohne eine Datei zu öffnen
- **awk** ist eine vollständige Programmiersprache, spezialisiert auf spaltenbasierte Daten
- Beide arbeiten nach dem Unix-Prinzip: Lesen von Standard-Input, Verarbeiten, Ausgabe an Standard-Output

**Warum sind diese Tools so wichtig?**
- **Automatisierung:** Textverarbeitung ohne manuelle Eingriffe
- **Effizienz:** Verarbeitung großer Dateien ohne viel Speicherverbrauch
- **Flexibilität:** Von einfachen Ersetzungen bis zu komplexen Datenanalysen
- **Universalität:** Auf jedem Linux/Unix-System verfügbar

**Aufbau der Challenge:**
1. **Teil 1:** sed - Stream Editor verstehen und anwenden (Grundlagenaufgabe/Verpflichtend)
2. **Teil 2:** awk - Strukturierte Datenverarbeitung meistern 

**Lernpfad:**
Einfache Textmanipulation → Strukturierte Datenverarbeitung → Automatisierte Workflows

---

## Teil 1: sed - Der Stream Editor verstehen

### Was ist ein Stream Editor?

Ein **Stream Editor** wie sed verarbeitet Text **sequenziell** - Zeile für Zeile, von Anfang bis Ende. Anders als bei einem normalen Editor wie vim öffnest du nicht die Datei zur Bearbeitung, sondern sed liest jede Zeile, wendet deine Regeln an und gibt das Ergebnis aus.

**Das Stream-Konzept verstehen:**
```
Input → sed Verarbeitung → Output
Datei → Regel anwenden → Bildschirm/neue Datei
```

**Warum ist das so mächtig?**
- Funktioniert mit riesigen Dateien (Gigabytes)
- Kann in Pipelines integriert werden
- Verändert Original nicht (außer mit -i Option)
- Sehr schnell und speicherschonend

### sed Grundlagen: Der Pattern Space

sed arbeitet mit einem Konzept namens **Pattern Space** - einem internen Speicherbereich, in dem jede Zeile verarbeitet wird:

1. **Zeile lesen** → Pattern Space
2. **Befehle ausführen** → Zeile im Pattern Space bearbeiten  
3. **Ausgabe** → Zeile aus Pattern Space ausgeben
4. **Nächste Zeile** → Prozess wiederholen

**Grundsyntax verstehen:**
```bash
sed 'adresse befehl' datei.txt
```

- **adresse:** Welche Zeile(n) bearbeiten (optional)
- **befehl:** Was mit der Zeile machen
- **datei.txt:** Input-Datei

### Die wichtigsten sed-Befehle erklärt

**1. Substitute (s) - Ersetzen:**
```bash
sed 's/alt/neu/' datei.txt        # Ersetzt erstes Vorkommen pro Zeile
sed 's/alt/neu/g' datei.txt       # Ersetzt ALLE Vorkommen (global)
sed 's/alt/neu/2' datei.txt       # Ersetzt nur das 2. Vorkommen pro Zeile
sed 's/alt/neu/gi' datei.txt      # Global + case insensitive
```

**Was bedeutet das 'g' Flag?**
Ohne 'g' ersetzt sed nur das erste Vorkommen pro Zeile. Mit 'g' (global) werden alle Vorkommen in jeder Zeile ersetzt.

**2. Delete (d) - Löschen:**
```bash
sed '5d' datei.txt               # Löscht Zeile 5
sed '2,4d' datei.txt             # Löscht Zeilen 2 bis 4  
sed '/muster/d' datei.txt        # Löscht alle Zeilen die "muster" enthalten
sed '/^$/d' datei.txt            # Löscht leere Zeilen
```

**3. Insert (i) und Append (a) - Einfügen:**
```bash
sed '3i\Neue Zeile' datei.txt    # Fügt VOR Zeile 3 ein
sed '3a\Neue Zeile' datei.txt    # Fügt NACH Zeile 3 ein
sed '$a\Letzte Zeile' datei.txt  # Fügt am Dateiende ein
```

**4. Print (p) - Ausgabe steuern:**
```bash
sed -n '5p' datei.txt            # Zeigt NUR Zeile 5 (-n unterdrückt normale Ausgabe)
sed -n '2,4p' datei.txt          # Zeigt nur Zeilen 2-4
sed -n '/muster/p' datei.txt     # Zeigt nur Zeilen mit "muster"
```

**Adressen in sed verstehen:**
- **Zahl:** Bestimmte Zeile (z.B. `5`)
- **Bereich:** Mehrere Zeilen (z.B. `2,4`)
- **Muster:** Zeilen die Muster enthalten (z.B. `/ERROR/`)
- **$:** Letzte Zeile
- **Keine Adresse:** Alle Zeilen

---

### Aufgabe 1: sed Grundlagen - Ersetzen verstehen und anwenden

Erstelle eine Arbeitsumgebung für praktische Übungen:

```bash
cd ~
mkdir sed_awk_challenge
cd sed_awk_challenge
```

**Erstelle eine realistische Konfigurationsdatei:**

```bash
cat > webapp_config.txt << 'EOF'
# Web Application Configuration
server_port=8080
database_host=localhost
database_port=5432
debug_mode=true
log_level=INFO
max_connections=100
timeout=30
ssl_enabled=false
ssl_port=443
backup_enabled=false
backup_time=02:00
admin_email=admin@oldcompany.com
api_endpoint=http://api.oldcompany.com/v1
cache_size=512MB
session_timeout=3600
EOF
```

**Erstelle eine typische Logdatei:**

```bash
cat > system.log << 'EOF'
2024-01-15 09:30:22 INFO: System startup completed
2024-01-15 09:30:25 DEBUG: Configuration loaded from /etc/webapp.conf
2024-01-15 09:32:10 WARN: SSL certificate expires in 30 days
2024-01-15 09:35:45 ERROR: Database connection failed: timeout
2024-01-15 09:36:00 INFO: Retrying database connection
2024-01-15 09:36:05 INFO: Database connection established
2024-01-15 09:38:22 ERROR: Authentication failed for user: john.doe@company.com
2024-01-15 09:40:15 INFO: Scheduled backup started
2024-01-15 09:42:30 WARN: Memory usage high: 85% of available RAM
2024-01-15 09:45:10 ERROR: Backup process failed: insufficient disk space
2024-01-15 09:46:00 INFO: Cleanup process completed
EOF
```

**Jetzt teste sed Schritt für Schritt:**

1. **Einfache Ersetzung verstehen:**
```bash
# Zeige zuerst die Originaldatei
echo "=== ORIGINAL KONFIGURATION ==="
cat webapp_config.txt

# Ändere den Port (nur Ausgabe, Datei bleibt unverändert)
echo -e "\n=== PORT 8080 → 9090 ==="
sed 's/8080/9090/' webapp_config.txt

# Überprüfe: Originaldatei ist unverändert
echo -e "\n=== ORIGINAL PRÜFUNG ==="
grep "server_port" webapp_config.txt
```

2. **Globale Ersetzung (g-Flag) verstehen:**
```bash
# Ändere alle Vorkommen der Domain
echo "=== DOMAIN ÄNDERN (GLOBAL) ==="
sed 's/oldcompany\.com/newcompany.com/g' webapp_config.txt

# Erkläre warum der Punkt escaped wird:
echo -e "\n=== WARUM DER BACKSLASH? ==="
echo "Ohne Backslash (FALSCH):"
sed 's/oldcompany.com/MATCH/g' webapp_config.txt | grep MATCH
echo "Mit Backslash (RICHTIG):"
sed 's/oldcompany\.com/MATCH/g' webapp_config.txt | grep MATCH
```

3. **Case-insensitive Ersetzung:**
```bash
# Ändere INFO zu INFORMATION (unabhängig von Groß-/Kleinschreibung)
echo "=== CASE-INSENSITIVE ERSETZUNG ==="
sed 's/info/INFORMATION/gi' system.log
```

4. **Permanent speichern mit -i Option:**
```bash
# Erstelle eine Backup-Datei und ändere sie permanent
cp webapp_config.txt webapp_config_new.txt

echo "=== VOR DER ÄNDERUNG ==="
grep "server_port\|admin_email" webapp_config_new.txt

# Permanente Änderung mit -i
sed -i 's/8080/9090/' webapp_config_new.txt
sed -i 's/oldcompany\.com/newcompany.com/g' webapp_config_new.txt

echo "=== NACH DER ÄNDERUNG ==="
grep "server_port\|admin_email" webapp_config_new.txt
```

**Verstehe, was passiert ist:**
- **Ohne -i:** sed gibt nur das Ergebnis aus, Originaldatei bleibt unverändert
- **Mit -i:** sed ändert die Datei direkt
- **Backslash vor Punkt:** In regulären Ausdrücken ist '.' ein Platzhalter für "jedes Zeichen", '\.' bedeutet "der Punkt selbst"

**Fragen zur Aufgabe 1:**
1. **Erkläre den Unterschied:** Was passiert bei `sed 's/test/TEST/'` vs `sed 's/test/TEST/g'` wenn eine Zeile "test test test" enthält?
2. **Warum Backslash:** Warum schreibt man `oldcompany\.com` statt `oldcompany.com` in sed?
3. **Sicherheit:** Was ist der Vorteil, dass sed standardmäßig die Originaldatei nicht verändert?

**Screenshot-Aufgabe 1:**
Screenshot der Ausgabe von: `sed 's/oldcompany\.com/newcompany.com/g' webapp_config.txt`

---

### Aufgabe 2: sed Erweiterte Funktionen - Zeilen löschen und hinzufügen

**Erstelle eine gemischte Datei mit verschiedenen Inhaltstypen:**

```bash
cat > mixed_config.txt << 'EOF'
# Configuration file for production environment
# Generated on 2024-01-15

server_name=webapp-prod
server_port=8080

# Database settings
db_host=localhost
db_port=5432
db_name=production

# Debug settings (remove in production)
debug_mode=true
verbose_logging=true

# Cache configuration
cache_enabled=true
cache_size=1024MB

# Backup configuration
backup_enabled=false
backup_schedule=daily

# End of configuration
EOF
```

**Lerne erweiterte sed-Funktionen:**

1. **Zeilen löschen nach Mustern:**
```bash
echo "=== ORIGINAL DATEI ==="
cat -n mixed_config.txt  # -n zeigt Zeilennummern

echo -e "\n=== ENTFERNE ALLE KOMMENTARE ==="
sed '/^#/d' mixed_config.txt

echo -e "\n=== ENTFERNE LEERE ZEILEN ==="
sed '/^$/d' mixed_config.txt

echo -e "\n=== ENTFERNE KOMMENTARE UND LEERE ZEILEN ==="
sed -e '/^#/d' -e '/^$/d' mixed_config.txt
```

**Erkläre die Muster:**
- `/^#/d` - Lösche Zeilen die mit # beginnen (^ = Zeilenanfang)
- `/^$/d` - Lösche leere Zeilen (^$ = Anfang direkt gefolgt von Ende)
- `-e` - Führe mehrere sed-Befehle nacheinander aus

2. **Bestimmte Zeilenbereiche löschen:**
```bash
echo "=== LÖSCHE ZEILEN 5-8 ==="
sed '5,8d' mixed_config.txt

echo -e "\n=== LÖSCHE DEBUG-BEREICH ==="
sed '/# Debug settings/,/verbose_logging=true/d' mixed_config.txt
```

3. **Text einfügen (Insert und Append):**
```bash
echo "=== FÜGE HEADER EIN ==="
sed '1i\# Updated configuration - Version 2.0' mixed_config.txt

echo -e "\n=== FÜGE NACH JEDER SEKTION LEERZEILE EIN ==="
sed '/=true$/a\\' mixed_config.txt

echo -e "\n=== FÜGE AM ENDE EINE ZEILE EIN ==="
sed '$a\# Configuration loaded successfully' mixed_config.txt
```

**Verstehe die Insert/Append-Syntax:**
- `1i\text` - Insert: Füge vor Zeile 1 ein
- `$a\text` - Append: Füge nach letzter Zeile ($) ein
- `a\\` - Füge eine Leerzeile ein

4. **Nur bestimmte Zeilen anzeigen (Print):**
```bash
echo "=== NUR KONFIGURATIONSWERTE (KEINE KOMMENTARE) ==="
sed -n '/=/p' mixed_config.txt

echo -e "\n=== NUR ZEILEN 10-15 ==="
sed -n '10,15p' mixed_config.txt

echo -e "\n=== ERSTE UND LETZTE ZEILE ==="
sed -n -e '1p' -e '$p' mixed_config.txt
```

**Die -n Option verstehen:**
- Normalerweise gibt sed jede Zeile aus
- `-n` unterdrückt die normale Ausgabe
- `p` Befehl gibt dann nur bestimmte Zeilen aus
- Nützlich um sed wie grep zu verwenden

**Fragen zur Aufgabe 2:**
1. **Muster verstehen:** Was bedeutet `/^#/d` genau und warum funktioniert es für Kommentare?
2. **Bereichslöschung:** Wie löschst du alle Zeilen zwischen "START" und "END" einschließlich dieser Zeilen?
3. **Print vs grep:** Was ist der Unterschied zwischen `sed -n '/muster/p'` und `grep "muster"`?

**Screenshot-Aufgabe 2:**
Screenshot von: `sed -e '/^#/d' -e '/^$/d' mixed_config.txt`

---

## Teil 2: awk - Strukturierte Datenverarbeitung verstehen

### Was macht awk besonders?

**awk** ist keine einfache Textmanipulation wie sed, sondern eine vollständige **Programmiersprache** für strukturierte Daten. awk wurde speziell entwickelt, um mit **feldbasierten** Daten zu arbeiten - denke an CSV-Dateien, Logfiles mit Spalten oder tabellarische Berichte.

### Das Feld-Konzept verstehen

**Was sind Felder?**
awk teilt jede Zeile automatisch in **Felder** (Spalten) auf. Standardmäßig sind Felder durch Leerzeichen oder Tabs getrennt:

```
Beispielzeile: "John Doe 25 Engineer"
$1 = "John"    (erstes Feld)
$2 = "Doe"     (zweites Feld)  
$3 = "25"      (drittes Feld)
$4 = "Engineer" (viertes Feld)
$0 = ganze Zeile
```

**Field Separator (FS) ändern:**
```bash
awk -F, '{ print $1 }'  # Verwende Komma als Feldtrennzeichen
awk -F: '{ print $1 }'  # Verwende Doppelpunkt als Feldtrennzeichen
```

### awk-Grundstruktur verstehen

**Pattern-Action-Struktur:**
```bash
awk 'pattern { action }' datei.txt
```

- **pattern:** WANN soll die Aktion ausgeführt werden (optional)
- **action:** WAS soll gemacht werden

**Beispiele:**
```bash
awk '{ print $1 }'           # Für jede Zeile: drucke erstes Feld
awk '/ERROR/ { print $0 }'   # Nur für Zeilen mit "ERROR": drucke ganze Zeile
awk 'NR > 1 { print $1 }'   # Ab Zeile 2: drucke erstes Feld
```

### Wichtige awk-Variablen verstehen

**Eingebaute Variablen:**
- `$0` - Die komplette aktuelle Zeile
- `$1, $2, $3...` - Erstes, zweites, drittes Feld usw.
- `NF` - Number of Fields (Anzahl Felder in aktueller Zeile)
- `NR` - Number of Records (Aktuelle Zeilennummer, beginnt bei 1)
- `FS` - Field Separator (Feldtrennzeichen)
- `OFS` - Output Field Separator (Ausgabe-Feldtrennzeichen)

**Praktische Bedeutung:**
```bash
# NR für Zeilennummern
awk '{ print NR, $0 }'       # Jede Zeile mit Nummer ausgeben

# NF für Feldanzahl  
awk '{ print NF, $0 }'       # Jede Zeile mit Feldanzahl ausgeben

# Header überspringen
awk 'NR > 1 { print $1 }'   # Erste Zeile (Header) ignorieren
```

### BEGIN und END verstehen

**Spezielle Muster:**
- `BEGIN` - Wird VOR der ersten Zeile ausgeführt
- `END` - Wird NACH der letzten Zeile ausgeführt

```bash
awk 'BEGIN { print "Start" } { print $1 } END { print "Ende" }' datei.txt
```

**Praktischer Nutzen:**
- `BEGIN` - Header ausgeben, Variablen initialisieren
- `END` - Zusammenfassungen, Statistiken ausgeben

---

### Aufgabe 3: awk Grundlagen - Felder verstehen und verwenden

**Erstelle strukturierte Testdaten (CSV-Format):**

```bash
cat > mitarbeiter.csv << 'EOF'
Nachname,Name,Position,Abteilung,Gehalt,Startdatum
Mueller,Max,Software Engineer,IT,75000,2023-01-15
Schmidt,Anna,Product Manager,Marketing,82000,2022-08-22
Weber,Peter,DevOps Engineer,IT,78000,2023-03-10
Johnson,Lisa,UX Designer,Design,65000,2023-02-01
Brown,Tom,Data Scientist,IT,85000,2022-11-30
Davis,Sarah,HR Manager,HR,70000,2021-05-15
Wilson,Mike,Backend Developer,IT,72000,2023-04-20
Garcia,Maria,Frontend Developer,IT,68000,2023-01-30
EOF
```

**Erstelle ein Access-Log (weltraumgetrennte Felder):**

```bash
cat > access.log << 'EOF'
192.168.1.100 user1 2024-01-15 10:30:22 GET /api/users 200 1234 0.120
192.168.1.105 user2 2024-01-15 10:31:15 POST /api/login 401 89 0.230
10.0.0.50 admin 2024-01-15 10:32:33 GET /admin/dashboard 200 5678 0.045
192.168.1.100 user1 2024-01-15 10:33:44 GET /api/products 200 2345 0.089
10.0.0.75 guest 2024-01-15 10:34:55 GET /api/data 500 0 2.450
192.168.1.200 user3 2024-01-15 10:35:11 DELETE /api/user/123 403 156 0.034
EOF
```

**Verstehe awk Schritt für Schritt:**

1. **Felder verstehen und ausgeben:**
```bash
echo "=== DIE CSV-DATEI VERSTEHEN ==="
echo "Zeige erste paar Zeilen mit Zeilennummern:"
head -4 mitarbeiter.csv | cat -n

echo -e "\n=== ALLE NAMEN AUSGEBEN (OHNE HEADER) ==="
awk -F, 'NR > 1 { print $1 }' mitarbeiter.csv

echo -e "\n=== VERSTEHE DAS FELD-KONZEPT ==="
echo "Erste Zeile aufgeteilt in Felder:"
head -2 mitarbeiter.csv | tail -1 | awk -F, '{ 
    print "Feld 1 (Name):", $1
    print "Feld 2 (Position):", $2  
    print "Feld 3 (Abteilung):", $3
    print "Feld 4 (Gehalt):", $4
    print "Feld 5 (Datum):", $5
    print "Komplette Zeile ($0):", $0
    print "Anzahl Felder (NF):", NF
}'
```

2. **Formatierte Ausgabe mit printf:**
```bash
echo "=== FORMATIERTE NAMENSLISTE ==="
awk -F, 'NR > 1 { printf "%-15s %-20s\n", $1, $2 }' mitarbeiter.csv

echo -e "\n=== GEHALTSLISTE FORMATIERT ==="
awk -F, 'NR > 1 { printf "%-15s %8s EUR\n", $1, $5 }' mitarbeiter.csv
```

**printf verstehen:**
- `%s` - String
- `%d` - Ganze Zahl  
- `%f` - Fließkommazahl
- `%-15s` - String, links ausgerichtet, 15 Zeichen breit
- `%8s` - String, rechts ausgerichtet, 8 Zeichen breit

3. **Access-Log analysieren (weltraumgetrennte Felder):**
```bash
echo "=== ACCESS-LOG FELDER VERSTEHEN ==="
echo "Feld-Struktur:"
head -1 access.log | awk '{ 
    print "IP ($1):", $1
    print "User ($2):", $2
    print "Datum ($3):", $3  
    print "Zeit ($4):", $4
    print "HTTP-Method ($5):", $5
    print "URL ($6):", $6
    print "Status ($7):", $7
    print "Bytes ($8):", $8
    print "Response-Zeit ($9):", $9
}'

echo -e "\n=== NUR IP-ADRESSEN ==="
awk '{ print $1 }' access.log

echo -e "\n=== NUR HTTP-STATUS-CODES ==="
awk '{ print $7 }' access.log
```

4. **Einfache Berechnungen:**
```bash
echo "=== DURCHSCHNITTSGEHALT BERECHNEN ==="
awk -F, 'NR > 1 { 
    summe += $4; 
    anzahl++ 
} 
END { 
    print "Gesamtsumme:", summe, "EUR"
    print "Anzahl Mitarbeiter:", anzahl
    print "Durchschnittsgehalt:", summe/anzahl, "EUR" 
}' mitarbeiter.csv

echo -e "\n=== RESPONSE-ZEITEN ANALYSIEREN ==="
awk '{ 
    total_time += $9; 
    count++ 
} 
END { 
    print "Requests gesamt:", count
    print "Gesamte Response-Zeit:", total_time, "s"
    print "Durchschnittliche Response-Zeit:", total_time/count, "s"
}' access.log
```

**Verstehe die Berechnungen:**
- `summe += $4` - Addiere Feld 4 zur Variable summe
- `anzahl++` - Erhöhe anzahl um 1
- `END` - Wird nach allen Zeilen ausgeführt
- Variablen werden automatisch mit 0 initialisiert

**Fragen zur Aufgabe 3:**
1. **NR verstehen:** Warum verwenden wir `NR > 1` bei CSV-Dateien und was würde ohne passieren?
2. **Field Separator:** Was passiert, wenn du `-F,` weglässt bei der CSV-Verarbeitung?
3. **printf vs print:** Erkläre den Unterschied zwischen `print $1, $5` und `printf "%-15s %8s\n", $1, $5`

**Screenshot-Aufgabe 3:**
Screenshot von: `awk -F, 'NR > 1 { printf "%-15s %8s EUR\n", $1, $5 }' mitarbeiter.csv`

---

### Aufgabe 4: awk Erweiterte Funktionen - Arrays und Gruppierungen

**Was sind Arrays in awk?**
Arrays in awk sind **assoziative Arrays** (wie Hash-Maps). Du kannst sie verwenden um Daten zu **gruppieren** und **aggregieren**:

```bash
# Syntax: array[schlüssel] = wert
verkäufe["Januar"] = 1000
verkäufe["Februar"] = 1200
```

**Erstelle erweiterte Testdaten:**

```bash
cat > verkaufsdaten.csv << 'EOF'
Datum,Produkt,Kategorie,Preis,Menge,Kunde_Typ,Region
2024-01-15,Laptop Pro,Elektronik,1299.99,2,Business,Nord
2024-01-15,Bürostuhl,Möbel,249.99,5,Business,Süd
2024-01-16,Smartphone,Elektronik,799.99,3,Privat,Ost
2024-01-16,Schreibtisch,Möbel,399.99,1,Business,West
2024-01-17,Tablet,Elektronik,449.99,4,Privat,Nord
2024-01-17,Monitor,Elektronik,299.99,2,Business,Süd
2024-01-18,Maus,Elektronik,45.99,10,Privat,Ost
2024-01-18,Lampe,Möbel,79.99,8,Privat,West
2024-01-19,Tastatur,Elektronik,129.99,6,Business,Nord
2024-01-19,Regal,Möbel,189.99,3,Business,Süd
EOF
```

**Lerne Arrays und erweiterte awk-Features:**

1. **Array-Grundlagen verstehen:**
```bash
echo "=== UMSATZ PRO KATEGORIE (ARRAY-BEISPIEL) ==="
awk -F, '
NR > 1 { 
    umsatz = $4 * $5  # Preis mal Menge
    kategorie_umsatz[$3] += umsatz  # Array: kategorie_umsatz["Elektronik"] += wert
}
END {
    print "Umsatz pro Kategorie:"
    for (kategorie in kategorie_umsatz) {
        printf "  %-12s: %8.2f EUR\n", kategorie, kategorie_umsatz[kategorie]
    }
}' verkaufsdaten.csv
```

**Verstehe was passiert:**
- `kategorie_umsatz[$3]` - Array mit Kategorie-Namen als Schlüssel
- `+= umsatz` - Addiere Umsatz zum bestehenden Wert
- `for (kategorie in kategorie_umsatz)` - Iteriere über alle Array-Keys

