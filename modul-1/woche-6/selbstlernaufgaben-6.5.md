# Linux Szenario: Einfache Entwicklungsumgebung für ein Team einrichten

Diese Aufgabe ist als Übung für den VOrmittag gedacht, ihr müsst also nichts einreichen!


## Szenario-Beschreibung

Du bist der neue System-Administrator bei der kleinen Firma **404 Institut** und sollst eine einfache Linux-Entwicklungsumgebung für ein kleines Team einrichten. Das Team arbeitet an einem Web-Projekt und benötigt eine grundlegende, sichere Arbeitsumgebung.

**Team-Zusammensetzung:**
- 1 Frontend-Entwickler
- 1 Backend-Entwickler  
- 1 Projekt-Manager (nur Lese-Zugriff)

---

## Phase 1: Benutzer und Gruppen erstellen

### Schritt 1.1: Benutzer erstellen
Erstelle drei Benutzer für das Team:

- `anna_frontend` (Frontend-Entwicklerin)
- `jacob_backend` (Backend-Entwickler)
- `lisa_manager` (Projekt-Managerin)

**Aufgaben:**
1. Erstelle alle drei Benutzer mit dem `adduser` Befehl
2. Setze für jeden ein einfaches Passwort (z.B. "test123")
3. Überprüfe mit `cat /etc/passwd`, dass alle Benutzer angelegt wurden

💡 **Hinweise:**
- Du benötigst `sudo` für administrative Aufgaben
- Der `adduser` Befehl ist interaktiv und fragt nach Details
- Mit `tail -3 /etc/passwd` siehst du die letzten 3 Einträge

### Schritt 1.2: Gruppen erstellen
Erstelle drei einfache Gruppen:

- `frontend_team` - Für Frontend-Entwicklung
- `backend_team` - Für Backend-Entwicklung
- `project_team` - Für alle Teammitglieder

**Aufgaben:**
1. Erstelle die drei Gruppen
2. Füge jeden Benutzer zu seiner Hauptgruppe hinzu
3. Füge alle Benutzer zur `project_team` Gruppe hinzu
4. Überprüfe die Gruppenmitgliedschaften

💡 **Hinweise:**
- `addgroup` erstellt neue Gruppen
- `adduser benutzername gruppenname` fügt Benutzer zu Gruppen hinzu
- Mit `groups benutzername` kannst du Gruppenmitgliedschaften überprüfen
- Jeder Benutzer sollte in mindestens 2 Gruppen sein

---

## Phase 2: Projekt-Verzeichnisse erstellen 

### Schritt 2.1: Einfache Verzeichnisstruktur anlegen
Erstelle eine übersichtliche Struktur unter `/opt/techcorp/`:

```
/opt/techcorp/
├── projects/
│   ├── frontend/
│   ├── backend/
│   └── shared/
└── documents/
    ├── plans/
    └── reports/
```

**Aufgaben:**
1. Erstelle die komplette Verzeichnisstruktur
2. Überprüfe mit `ls -la`, dass alles erstellt wurde

💡 **Hinweise:**
- `mkdir -p` erstellt Verzeichnisse inklusive übergeordneter Ordner
- Du kannst mehrere Ordner in einem Befehl erstellen
- Beginne mit dem Hauptverzeichnis `/opt/techcorp`
- `ls -la` zeigt Details inklusive Berechtigungen an

### Schritt 2.2: Besitzer und Gruppen zuweisen
Weise die Verzeichnisse den richtigen Gruppen zu:

**Aufgaben:**
1. Frontend-Ordner → `frontend_team`
2. Backend-Ordner → `backend_team`  
3. Shared-Ordner → `project_team`
4. Documents-Ordner → `project_team`

💡 **Hinweise:**
- `chown benutzer:gruppe verzeichnis` ändert Besitzer und Gruppe
- Du kannst `root` als Benutzer beibehalten
- `ls -la` zeigt dir die aktuellen Besitzer und Gruppen
- Vergiss nicht die Unterordnerte in documents/

---

## Phase 3: Berechtigungen setzen 

### Schritt 3.1: Frontend-Berechtigungen
Anna soll im Frontend-Ordner arbeiten können, aber nicht im Backend-Ordner.

**Aufgaben:**
1. Frontend-Ordner: Gruppe kann alles, andere nichts
2. Teste als Anna, ob sie Dateien erstellen kann

💡 **Hinweise:**
- `chmod u+rwx,g+rwx,o-rwx` gibt der Gruppe alle Rechte, anderen keine
- `u` = user (Besitzer), `g` = group, `o` = others
- `r` = read, `w` = write, `x` = execute
- Mit `sudo su - benutzername` wechselst du den Benutzer
- `touch` erstellt leere Dateien, `echo "text" > datei` schreibt Inhalt
- Mit `exit` kommst du zum ursprünglichen Benutzer zurück

### Schritt 3.2: Backend-Berechtigungen  
Jacob soll im Backend-Ordner arbeiten können, aber Anna soll dort nur lesen können.

**Aufgaben:**
1. Backend-Ordner: Gruppe kann alles, andere nur lesen
2. Teste als Jacob, ob er arbeiten kann
3. Teste als Anna, ob sie nur lesen kann

💡 **Hinweise:**
- Für "andere nur lesen": `o+r` statt `o-rwx`
- Jacob sollte Dateien erstellen können
- Anna sollte Dateien lesen, aber nicht erstellen können
- Wenn Anna versucht zu schreiben, sollte "Permission denied" erscheinen
- `cat datei` zeigt Dateiinhalt an

### Schritt 3.3: Shared-Berechtigungen
Alle Teammitglieder sollen im Shared-Ordner arbeiten können.

**Aufgaben:**
1. Shared-Ordner: Gruppe kann alles
2. Teste mit verschiedenen Benutzern

💡 **Hinweise:**
- Shared sollte für die Gruppe `project_team` zugänglich sein
- Beide Entwickler (Anna und Jacob) sind in dieser Gruppe
- `echo "text" >> datei` hängt Text an eine bestehende Datei an
- Teste, dass beide Benutzer in denselben Dateien arbeiten können

---

## Phase 4: Manager-Zugriff, Tests und Abschluss 

### Schritt 4.1: Manager-Berechtigungen
Lisa (Manager) soll alle Projekte lesen können, aber nichts ändern.

**Aufgaben:**
1. Gib dem Manager Lese-Rechte für alle Projekt-Ordner
2. Manager soll im Documents-Ordner arbeiten können

💡 **Hinweise:**
- Lisa ist nur in der `project_team` Gruppe
- Für Lese-Rechte: `o+r` (others können lesen)
- Manager soll NICHT schreiben können in Projekt-Ordnern
- Im Documents-Ordner soll sie aber arbeiten können
- Teste beide Szenarien: Lesen funktioniert, Schreiben schlägt fehl

### Schritt 4.2: Umfangreiche Tests
Teste alle wichtigen Szenarien:

**Test-Liste:**
1. Anna kann Frontend bearbeiten ✓
2. Anna kann Backend nur lesen ✓
3. Jacob kann Backend bearbeiten ✓
4. Jacob kann Frontend nur lesen ✓
5. Beide können Shared bearbeiten ✓
6. Manager kann alles lesen ✓
7. Manager kann nur Documents bearbeiten ✓

💡 **Hinweise für Tests:**
- Wechsle systematisch zwischen den Benutzern
- Teste sowohl erfolgreiche als auch fehlschlagende Aktionen
- "Permission denied" Fehler sind erwünscht bei falschen Zugriffen
- Verwende `touch` zum Testen der Schreibrechte
- Verwende `cat` zum Testen der Leserechte
- Notiere dir, welche Tests erfolgreich waren

### Schritt 4.3: Final-Check
Überprüfe das gesamte System:

💡 **Hinweise zur Systemkontrolle:**

**Benutzer kontrollieren:**
- `cat /etc/passwd` zeigt ALLE Benutzer des Systems
- Das kann sehr lang sein! Deshalb filtern wir:
- `grep` ist ein Such-Befehl, der nur Zeilen mit bestimmten Wörtern zeigt
- `cat /etc/passwd | grep anna` zeigt nur Zeilen mit "anna"
- `cat /etc/passwd | grep -E "(anna|jacob|lisa)"` zeigt Zeilen mit einem der drei Namen

**Gruppen kontrollieren:**
- `cat /etc/group` zeigt alle Gruppen (sehr viele!)
- `cat /etc/group | grep frontend` zeigt nur die frontend-Gruppe
- `cat /etc/group | grep -E "(frontend|backend|project)"` zeigt unsere drei Gruppen

**Verzeichnisstruktur kontrollieren:**
- `tree /opt/techcorp/` zeigt die Verzeichnisstruktur (falls installiert)
- Alternativ: `ls -la` für jeden Ordner einzeln
- `ls -la /opt/techcorp/projects/*/` zeigt alle Projekt-Berechtigungen
- Kontrolliere, dass alle Berechtigungen korrekt gesetzt sind

**Was ist grep?**
Der `grep` Befehl sucht nach Text in Dateien oder Ausgaben. Er filtert nur die Zeilen heraus, die den gesuchten Text enthalten. Das `|` (Pipe) Symbol leitet die Ausgabe des ersten Befehls an den zweiten weiter.

---

## Erfolgskriterien - Checkliste

### Am Ende solltest du folgende Punkte abhaken können:

**Benutzer-Management:**
- [ ] 3 Benutzer erfolgreich erstellt (anna_frontend, jacob_backend, lisa_manager)
- [ ] 3 Gruppen erstellt (frontend_team, backend_team, project_team)
- [ ] Alle Benutzer in korrekten Gruppen

**Verzeichnis-Struktur:**
- [ ] `/opt/techcorp/` Hauptverzeichnis erstellt
- [ ] Projekt-Ordner: frontend, backend, shared
- [ ] Document-Ordner: plans, reports
- [ ] Alle Ordner haben korrekte Gruppen-Zugehörigkeit

**Berechtigungen funktionieren:**
- [ ] Anna kann nur in Frontend arbeiten
- [ ] Jacob kann nur in Backend arbeiten  
- [ ] Beide können in Shared arbeiten
- [ ] Manager kann alles lesen, aber nur Documents bearbeiten
- [ ] Unbefugte haben keinen Zugriff

**Tests erfolgreich:**
- [ ] Alle 7 Test-Szenarien durchgeführt
- [ ] System funktioniert wie geplant

## 🎯 Wichtige Befehle und Tipps

### Benutzer- und Gruppenverwaltung:
- `sudo adduser benutzername` - Neuen Benutzer erstellen
- `sudo addgroup gruppenname` - Neue Gruppe erstellen  
- `sudo adduser benutzer gruppe` - Benutzer zu Gruppe hinzufügen
- `groups benutzername` - Gruppenmitgliedschaften anzeigen
- `whoami` - Aktuellen Benutzer anzeigen

### Verzeichnis-Management:
- `mkdir -p pfad/zu/verzeichnis` - Verzeichnisse erstellen (inkl. übergeordnete)
- `ls -la` - Detaillierte Auflistung mit Berechtigungen
- `cd verzeichnis` - Verzeichnis wechseln
- `pwd` - Aktuellen Pfad anzeigen

### Berechtigungen:
- `sudo chown benutzer:gruppe datei` - Besitzer/Gruppe ändern
- `sudo chmod u+rwx,g+rwx,o-rwx datei` - Berechtigungen setzen
  - `u` = user (Besitzer), `g` = group, `o` = others  
  - `r` = read, `w` = write, `x` = execute
  - `+` = hinzufügen, `-` = entfernen

### Benutzer wechseln und testen:
- `sudo su - benutzername` - Zu anderem Benutzer wechseln
- `exit` - Zurück zum ursprünglichen Benutzer
- `touch datei` - Leere Datei erstellen (Test für Schreibrechte)
- `cat datei` - Dateiinhalt anzeigen (Test für Leserechte)

### Fehlerbehebung:
- **"Permission denied"** → Rechte mit `chmod` anpassen
- **"No such file"** → Pfad mit `pwd` und `ls` überprüfen  
- **"User does not exist"** → Mit `cat /etc/passwd` kontrollieren
- **Vergessen welcher Benutzer** → `whoami` verwenden

### Sicherheit:
- Immer `sudo` vor administrativen Befehlen
- Mit `exit` aus anderen Benutzern zurückkehren
- Nie `chmod 777` verwenden (unsicher!)


