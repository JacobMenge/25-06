# Linux Entwicklungsumgebung - Musterlösung

## Phase 1: Benutzer und Gruppen erstellen

### Schritt 1.1: Benutzer erstellen

**Ziel:** Drei Benutzer für das Team erstellen

```bash
# Anna (Frontend-Entwicklerin) erstellen
sudo adduser anna_frontend
```
**Erklärung:** `sudo` gibt uns Administrator-Rechte. `adduser` ist der Ubuntu-Befehl zum Erstellen von Benutzern (interaktiver als `useradd`). Das System fragt nach einem Passwort und weiteren Details.

```bash
# Jacob (Backend-Entwickler) erstellen  
sudo adduser jacob_backend
```

```bash
# Lisa (Projekt-Managerin) erstellen
sudo adduser lisa_manager
```

**Kontrolle der erstellten Benutzer:**
```bash
# Letzte 3 Zeilen der passwd-Datei anzeigen
tail -3 /etc/passwd
```

**Erwartete Ausgabe:**
```
anna_frontend:x:1001:1001:,,,:/home/anna_frontend:/bin/bash
jacob_backend:x:1002:1002:,,,:/home/jacob_backend:/bin/bash
lisa_manager:x:1003:1003:,,,:/home/lisa_manager:/bin/bash
```

**Erklärung der Ausgabe:**
- `anna_frontend`: Benutzername
- `x`: Passwort-Platzhalter (echtes Passwort steht in `/etc/shadow`)
- `1001`: Benutzer-ID (UID) - beginnt bei 1000 für normale Benutzer
- `1001`: Gruppen-ID (GID) - gleiche Nummer wie UID für die Standard-Gruppe
- `,,,`: Kommentarfeld (Name, Büro, etc.)
- `/home/anna_frontend`: Home-Verzeichnis
- `/bin/bash`: Standard-Shell

### Schritt 1.2: Gruppen erstellen

**Ziel:** Logische Gruppen für die Teamorganisation

```bash
# Frontend-Team Gruppe
sudo addgroup frontend_team
```
**Erklärung:** `addgroup` erstellt eine neue Gruppe. Ubuntu gibt automatisch eine freie Gruppen-ID.

```bash
# Backend-Team Gruppe
sudo addgroup backend_team
```

```bash
# Projekt-Team Gruppe (für alle)
sudo addgroup project_team
```

**Benutzer zu Gruppen hinzufügen:**
```bash
# Anna zur Frontend-Gruppe
sudo adduser anna_frontend frontend_team
# Anna zur Projekt-Gruppe (alle Teammitglieder)
sudo adduser anna_frontend project_team
```
**Erklärung:** `adduser benutzer gruppe` fügt einen existierenden Benutzer einer existierenden Gruppe hinzu.

```bash
# Jacob zur Backend-Gruppe
sudo adduser jacob_backend backend_team
sudo adduser jacob_backend project_team
```

```bash
# Lisa nur zur Projekt-Gruppe (Manager braucht keine spezielle Entwicklergruppe)
sudo adduser lisa_manager project_team
```

**Kontrolle der Gruppenmitgliedschaften:**
```bash
groups anna_frontend
groups jacob_backend  
groups lisa_manager
```

**Erwartete Ausgaben:**
```
anna_frontend : anna_frontend frontend_team project_team
jacob_backend : jacob_backend backend_team project_team
lisa_manager : lisa_manager project_team
```

**Erklärung:** Jeder Benutzer gehört automatisch zu seiner eigenen Gruppe (gleicher Name) plus den zusätzlich hinzugefügten Gruppen.

---

## Phase 2: Projekt-Verzeichnisse erstellen

### Schritt 2.1: Verzeichnisstruktur anlegen

**Ziel:** Organisierte Ordnerstruktur für das Projekt

```bash
# Hauptverzeichnis erstellen
sudo mkdir -p /opt/techcorp
```
**Erklärung:** 
- `/opt/` ist der Standard-Ort für zusätzliche Software-Pakete
- `-p` erstellt auch übergeordnete Verzeichnisse falls sie nicht existieren
- `sudo` wird benötigt, da `/opt/` dem root-Benutzer gehört

```bash
# Projekt-Verzeichnisse erstellen
sudo mkdir -p /opt/techcorp/projects/frontend
sudo mkdir -p /opt/techcorp/projects/backend
sudo mkdir -p /opt/techcorp/projects/shared
```

```bash
# Dokumenten-Verzeichnisse erstellen
sudo mkdir -p /opt/techcorp/documents/plans
sudo mkdir -p /opt/techcorp/documents/reports
```

**Struktur kontrollieren:**
```bash
ls -la /opt/techcorp/
```

**Erwartete Ausgabe:**
```
total 16
drwxr-xr-x  4 root root 4096 Jan 15 10:30 .
drwxr-xr-x  3 root root 4096 Jan 15 10:30 ..
drwxr-xr-x  2 root root 4096 Jan 15 10:30 documents
drwxr-xr-x  4 root root 4096 Jan 15 10:30 projects
```

```bash
ls -la /opt/techcorp/projects/
```

**Erwartete Ausgabe:**
```
total 20
drwxr-xr-x  5 root root 4096 Jan 15 10:31 .
drwxr-xr-x  4 root root 4096 Jan 15 10:30 ..
drwxr-xr-x  2 root root 4096 Jan 15 10:31 backend
drwxr-xr-x  2 root root 4096 Jan 15 10:31 frontend
drwxr-xr-x  2 root root 4096 Jan 15 10:31 shared
```

### Schritt 2.2: Besitzer und Gruppen zuweisen

**Ziel:** Jeder Ordner gehört der passenden Gruppe

```bash
# Frontend-Ordner der Frontend-Gruppe zuweisen
sudo chown root:frontend_team /opt/techcorp/projects/frontend/
```
**Erklärung:** `chown benutzer:gruppe pfad` ändert Besitzer und Gruppe. `root` bleibt Besitzer für administrative Kontrolle, aber die Gruppe bekommt Zugriff.

```bash
# Backend-Ordner der Backend-Gruppe zuweisen  
sudo chown root:backend_team /opt/techcorp/projects/backend/
```

```bash
# Shared-Ordner dem gesamten Projekt-Team zuweisen
sudo chown root:project_team /opt/techcorp/projects/shared/
```

```bash
# Documents dem Projekt-Team zuweisen (alle sollen lesen können)
sudo chown root:project_team /opt/techcorp/documents/
sudo chown root:project_team /opt/techcorp/documents/plans/
sudo chown root:project_team /opt/techcorp/documents/reports/
```

**Kontrolle:**
```bash
ls -la /opt/techcorp/projects/
```

**Erwartete Ausgabe:**
```
total 20
drwxr-xr-x  5 root root         4096 Jan 15 10:31 .
drwxr-xr-x  4 root root         4096 Jan 15 10:30 ..
drwxr-xr-x  2 root backend_team 4096 Jan 15 10:31 backend
drwxr-xr-x  2 root frontend_team 4096 Jan 15 10:31 frontend
drwxr-xr-x  2 root project_team 4096 Jan 15 10:31 shared
```

---

## Phase 3: Berechtigungen setzen

### Schritt 3.1: Frontend-Berechtigungen

**Ziel:** Anna kann im Frontend arbeiten, andere nicht

```bash
# Frontend: Gruppe kann alles, andere nichts
sudo chmod u+rwx,g+rwx,o-rwx /opt/techcorp/projects/frontend/
```

**Erklärung der chmod-Syntax:**
- `u+rwx`: User (Besitzer) bekommt read, write, execute
- `g+rwx`: Group bekommt read, write, execute  
- `o-rwx`: Others verlieren alle Rechte
- `r` = read (4), `w` = write (2), `x` = execute (1)

**Test als Anna:**
```bash
# Zu Anna wechseln
sudo su - anna_frontend
# In Frontend-Ordner wechseln
cd /opt/techcorp/projects/frontend/
# Test-Datei erstellen
touch test-frontend.html
# Inhalt hinzufügen
echo "<!DOCTYPE html><html>Hallo Frontend!</html>" > test-frontend.html
# Inhalt kontrollieren
cat test-frontend.html
# Zurück zum Admin-Benutzer
exit
```

**Erwartete Ausgabe:**
```
<!DOCTYPE html><html>Hallo Frontend!</html>
```

**Berechtigung kontrollieren:**
```bash
ls -la /opt/techcorp/projects/frontend/
```

**Erwartete Ausgabe:**
```
total 12
drwxrwx---  2 root frontend_team 4096 Jan 15 10:45 .
drwxr-xr-x  5 root root         4096 Jan 15 10:31 ..
-rw-rw-r--  1 anna_frontend frontend_team   40 Jan 15 10:45 test-frontend.html
```

**Erklärung:** `drwxrwx---` zeigt, dass Besitzer (root) und Gruppe (frontend_team) alle Rechte haben, andere keine.

### Schritt 3.2: Backend-Berechtigungen

**Ziel:** Jacob kann Backend bearbeiten, Anna kann nur lesen

```bash
# Backend: Gruppe kann alles, andere nur lesen
sudo chmod u+rwx,g+rwx,o+r /opt/techcorp/projects/backend/
```

**Test als Jacob (sollte funktionieren):**
```bash
sudo su - jacob_backend
cd /opt/techcorp/projects/backend/
touch server.py
echo "# Backend Server
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Backend!'" > server.py
cat server.py
exit
```

**Test als Anna (nur lesen, nicht schreiben):**
```bash
sudo su - anna_frontend
cd /opt/techcorp/projects/backend/
# Das SOLLTE funktionieren (lesen)
cat server.py
# Das sollte FEHLSCHLAGEN (schreiben)
touch anna-test.py
exit
```

**Erwartete Ausgabe beim Schreibversuch:**
```
touch: cannot touch 'anna-test.py': Permission denied
```

### Schritt 3.3: Shared-Berechtigungen

**Ziel:** Beide Entwickler können zusammenarbeiten

```bash
# Shared: Gruppe kann alles
sudo chmod u+rwx,g+rwx,o-rwx /opt/techcorp/projects/shared/
```

**Test mit beiden Benutzern:**
```bash
# Anna erstellt Datei
sudo su - anna_frontend
cd /opt/techcorp/projects/shared/
touch team-notes.txt
echo "=== Team Notizen ===
- Anna: Frontend Komponenten sind bereit" > team-notes.txt
exit

# Jacob erweitert die Datei
sudo su - jacob_backend
cd /opt/techcorp/projects/shared/
echo "- Jacob: API Endpoints implementiert" >> team-notes.txt
cat team-notes.txt
exit
```

**Erwartete Ausgabe:**
```
=== Team Notizen ===
- Anna: Frontend Komponenten sind bereit
- Jacob: API Endpoints implementiert
```

---

## Phase 4: Manager-Zugriff, Tests und Abschluss

### Schritt 4.1: Manager-Berechtigungen

**Ziel:** Lisa kann alle Projekte lesen, aber nur Documents bearbeiten

```bash
# Alle Projekt-Ordner: Andere können lesen
sudo chmod u+rwx,g+rwx,o+rx /opt/techcorp/projects/frontend/
sudo chmod u+rwx,g+rwx,o+rx /opt/techcorp/projects/backend/
sudo chmod u+rwx,g+rwx,o+rx /opt/techcorp/projects/shared/
```

```bash
# Documents: Projekt-Team kann arbeiten
sudo chmod u+rwx,g+rwx,o-rwx /opt/techcorp/documents/plans/
sudo chmod u+rwx,g+rwx,o-rwx /opt/techcorp/documents/reports/
```

**Test als Manager:**
```bash
sudo su - lisa_manager
# Projekte lesen (sollte funktionieren)
cd /opt/techcorp/projects/frontend/
cat test-frontend.html

cd /opt/techcorp/projects/backend/
cat server.py

# In Projekten schreiben (sollte FEHLSCHLAGEN)
touch manager-test.txt

# In Documents arbeiten (sollte funktionieren)
cd /opt/techcorp/documents/plans/
touch project-plan.md
echo "# TechCorp Projekt Plan
## Ziele
- Frontend bis Ende Januar
- Backend bis Mitte Februar
## Team
- Anna: Frontend
- Jacob: Backend" > project-plan.md
cat project-plan.md
exit
```

### Schritt 4.2: Umfangreiche Tests

**Vollständige Test-Matrix:**

```bash
# Test 1: Anna Frontend (✓ sollte funktionieren)
sudo su - anna_frontend
cd /opt/techcorp/projects/frontend/
echo "Anna arbeitet hier" > anna-work.html
ls -la
exit

# Test 2: Anna Backend (✓ lesen sollte gehen, ✗ schreiben nicht)
sudo su - anna_frontend
cd /opt/techcorp/projects/backend/
cat server.py  # ✓ Sollte funktionieren
touch anna-backend-test.py  # ✗ Sollte fehlschlagen
exit

# Test 3: Jacob Backend (✓ sollte funktionieren)
sudo su - jacob_backend
cd /opt/techcorp/projects/backend/
echo "Jacob's Backend Code" > database.py
ls -la
exit

# Test 4: Jacob Frontend (✓ lesen sollte gehen, ✗ schreiben nicht)
sudo su - jacob_backend
cd /opt/techcorp/projects/frontend/
cat anna-work.html  # ✓ Sollte funktionieren
touch jacob-frontend-test.html  # ✗ Sollte fehlschlagen
exit

# Test 5: Beide im Shared (✓ beide sollten arbeiten können)
sudo su - anna_frontend
cd /opt/techcorp/projects/shared/
echo "Anna's gemeinsame Notiz" > collaboration.txt
exit

sudo su - jacob_backend
cd /opt/techcorp/projects/shared/
echo "Jacob's Ergänzung" >> collaboration.txt
cat collaboration.txt
exit

# Test 6: Manager liest alles (✓ sollte überall lesen können)
sudo su - lisa_manager
cat /opt/techcorp/projects/frontend/anna-work.html
cat /opt/techcorp/projects/backend/server.py
cat /opt/techcorp/projects/shared/collaboration.txt

# Test 7: Manager bearbeitet nur Documents (✓ in docs, ✗ in projects)
touch /opt/techcorp/projects/frontend/manager-test.txt  # ✗ Sollte fehlschlagen
cd /opt/techcorp/documents/reports/
touch weekly-report.md  # ✓ Sollte funktionieren
echo "# Wochenbericht
Das Team arbeitet gut zusammen!" > weekly-report.md
exit
```

### Schritt 4.3: Final-Check

**Systemkontrolle ohne grep (für Anfänger):**
```bash
# Alle Benutzer anzeigen (wird sehr lang!)
cat /etc/passwd
# Nur unsere Benutzer finden - scrolle nach unten oder:
cat /etc/passwd | tail -10
```

**Mit grep (effizienter):**
```bash
# Was ist grep? Ein Suchfilter!
# Zeigt nur Zeilen, die bestimmte Wörter enthalten

# Unsere Benutzer finden:
cat /etc/passwd | grep anna
cat /etc/passwd | grep jacob
cat /etc/passwd | grep lisa

# Oder alle auf einmal:
cat /etc/passwd | grep -E "(anna|jacob|lisa)"
```

**Erwartete Ausgabe:**
```
anna_frontend:x:1001:1001:,,,:/home/anna_frontend:/bin/bash
jacob_backend:x:1002:1002:,,,:/home/jacob_backend:/bin/bash
lisa_manager:x:1003:1003:,,,:/home/lisa_manager:/bin/bash
```

**Gruppen kontrollieren:**
```bash
# Unsere Gruppen finden:
cat /etc/group | grep -E "(frontend|backend|project)"
```

**Erwartete Ausgabe:**
```
frontend_team:x:1001:anna_frontend
backend_team:x:1002:jacob_backend
project_team:x:1003:anna_frontend,jacob_backend,lisa_manager
```

**Verzeichnisstruktur und Berechtigungen:**
```bash
# Hauptstruktur
ls -la /opt/techcorp/
# Projekt-Berechtigungen
ls -la /opt/techcorp/projects/
# Dokument-Berechtigungen
ls -la /opt/techcorp/documents/
```

**Erwartete finale Ausgabe für projects:**
```
total 20
drwxr-xr-x  5 root root         4096 Jan 15 10:31 .
drwxr-xr-x  4 root root         4096 Jan 15 10:30 ..
drwxrwxr--  2 root backend_team 4096 Jan 15 11:15 backend
drwxrwxr--  2 root frontend_team 4096 Jan 15 11:10 frontend
drwxrwx---  2 root project_team 4096 Jan 15 11:20 shared
```

**Erklärung der Berechtigungen:**
- `drwxrwxr--`: Besitzer und Gruppe können alles, andere nur lesen
- `drwxrwx---`: Besitzer und Gruppe können alles, andere nichts

---

## Erfolgskontrolle - Was sollte funktionieren:

### Erfolgreich:
1. **Anna erstellt Frontend-Dateien**
2. **Anna liest Backend-Dateien**  
3. **Jacob erstellt Backend-Dateien**
4. **Jacob liest Frontend-Dateien**
5. **Beide arbeiten gemeinsam in Shared**
6. **Lisa liest alle Projektordner**
7. **Lisa bearbeitet Documents**

### Soll fehlschlagen:
1. **Anna schreibt in Backend** → "Permission denied"
2. **Jacob schreibt in Frontend** → "Permission denied"  
3. **Lisa schreibt in Projektordner** → "Permission denied"

### Finale Berechtigungsmatrix:

| Benutzer | Frontend | Backend | Shared | Documents |
|----------|----------|---------|--------|-----------|
| Anna     | Lesen+Schreiben | Nur Lesen | Lesen+Schreiben | Lesen+Schreiben |
| Jacob    | Nur Lesen | Lesen+Schreiben | Lesen+Schreiben | Lesen+Schreiben |
| Lisa     | Nur Lesen | Nur Lesen | Nur Lesen | Lesen+Schreiben |

**Herzlichen Glückwunsch!** Du hast erfolgreich eine sichere Linux-Entwicklungsumgebung mit Benutzerverwaltung und Dateiberechtigungen eingerichtet.
