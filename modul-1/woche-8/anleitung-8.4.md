# Arbeiten mit SSH Anleitung - Windows 11 Edition

## Was ist SSH?

**SSH (Secure Shell)** ist wie ein sicherer Tunnel zwischen deinem Windows-Computer und einem anderen Computer. Stell dir vor, du kannst von zu Hause aus sicher einen Computer steuern, der weit weg steht.

### Warum SSH lernen?
- **Sicherheit**: Alles wird verschlüsselt übertragen
- **Fernsteuerung**: Steuere andere Computer von überall
- **Dateien übertragen**: Kopiere sicher Dateien zwischen Computern
- **Server verwalten**: Professionelle Server-Administration

### Wichtige Begriffe (einfach erklärt)
- **Client**: Dein Windows-Computer (von dem aus du dich verbindest)
- **Server**: Der andere Computer (zu dem du dich verbindest)
- **Host**: Anderes Wort für Server
- **Port**: Wie eine Zimmernummer - Port 22 ist das "SSH-Zimmer"

## Teil 1: VirtualBox auf Windows 11 installieren

### Schritt 1: VirtualBox herunterladen

1. **Öffne deinen Browser** (Chrome, Edge, Firefox)
2. **Gehe zu**: [https://www.virtualbox.org](https://www.virtualbox.org)
3. **Klicke auf**: "Downloads"
4. **Klicke auf**: "Windows hosts" (das ist für Windows 11)
5. **Warte** bis der Download fertig ist (ca. 100 MB)

### Schritt 2: VirtualBox installieren

1. **Gehe zum Downloads-Ordner** (normalerweise `C:\Users\DeinName\Downloads`)
2. **Doppelklick** auf die heruntergeladene Datei (z.B. `VirtualBox-7.0.x-Win.exe`)
3. **Wenn Windows fragt "Möchten Sie Änderungen zulassen?"** → Klicke **"Ja"**
4. **Installation**:
   - Klicke immer **"Next"** (Weiter)
   - Bei "Custom Setup": Lass alles angehakt
   - Bei "Warning Network Interfaces": Klicke **"Yes"** (Ja)
   - Klicke **"Install"** (Installieren)
   - **Warte** bis die Installation fertig ist (ca. 2-3 Minuten)
5. **Klicke "Finish"** und lass VirtualBox starten

## Teil 2: Ubuntu Server herunterladen

### Schritt 3: Ubuntu Server ISO-Datei holen

1. **Öffne einen neuen Browser-Tab**
2. **Gehe zu**: [https://ubuntu.com/download/server](https://ubuntu.com/download/server)
3. **Klicke auf**: "Download Ubuntu Server 22.04.x LTS"
4. **Warte** bis der Download fertig ist (ca. 1-2 GB, kann 10-30 Minuten dauern)
5. **Merke dir den Pfad**: Normalerweise `C:\Users\DeinName\Downloads\ubuntu-22.04.x-live-server-amd64.iso`

**Tipp**: Lass das downloaden und mach mit dem nächsten Schritt weiter.

## Teil 3: Ubuntu Server VM erstellen

### Schritt 4: Neue Virtual Machine erstellen

1. **Öffne VirtualBox** (falls noch nicht offen)
2. **Klicke auf den blauen "Neu" Button** (oben links)
3. **Fülle aus**:
   - **Name**: `Ubuntu-SSH-Server` (genau so schreiben)
   - **Ordner**: Lass den Standard-Pfad
   - **ISO Image**: Klicke auf das Dropdown → "Andere..." → Wähle deine heruntergeladene Ubuntu ISO
   - **Typ**: Linux (wird automatisch gewählt)
   - **Version**: Ubuntu (64-bit) (wird automatisch gewählt)
4. **Klicke "Weiter"**

### Schritt 5: Hardware einstellen

1. **Grundspeicher (RAM)**:
   - Stelle den Schieberegler auf **2048 MB** (2 GB)
   - Falls dein Computer weniger als 8 GB RAM hat, nimm 1024 MB
2. **Prozessoren**: Lass auf 1 (ist ok)
3. **Klicke "Weiter"**

### Schritt 6: Festplatte erstellen

1. **Festplatte erstellen**: Lass "Festplatte jetzt erstellen" ausgewählt
2. **Festplattengröße**: Stelle auf **20 GB** (ist genug für unsere Tests)
3. **Klicke "Weiter"**
4. **Zusammenfassung prüfen** und **"Fertig stellen" klicken**


### Schritt 7: Netzwerk für SSH konfigurieren (SEHR WICHTIG!)

**Das ist der wichtigste Teil für SSH!**

1. **Rechtsklick auf deine VM** "Ubuntu-SSH-Server"
2. **Klicke "Ändern..."** (oder "Settings")
3. **Klicke links auf "Netzwerk"**
4. **Bei Adapter 1**:
   - "Netzwerkadapter aktivieren" muss angehakt sein
   - **Angeschlossen an**: Lass auf "NAT"
5. **Klicke "Erweitert"** (der kleine Pfeil nach unten)
6. **Klicke "Port-Weiterleitung"**
7. **Klicke das grüne "+" Symbol** (neue Regel hinzufügen)
8. **Trage ein**:
   - **Name**: `SSH` (genau so)
   - **Protokoll**: `TCP`
   - **Host-IP**: Lass leer
   - **Host-Port**: `2222`
   - **Gast-IP**: Lass leer
   - **Gast-Port**: `22`
9. **Klicke "OK"** für das Port-Weiterleitungs-Fenster
10. **Klicke "OK"** für das Einstellungen-Fenster

**Was haben wir gemacht?** Wir haben gesagt: "Wenn jemand an Port 2222 auf meinem Windows-Computer klopft, leite das an Port 22 in der Ubuntu-VM weiter." Port 22 ist der Standard-SSH-Port.

## Teil 4: Ubuntu Server installieren

### Schritt 8: VM starten und Ubuntu installieren

1. **Doppelklick auf deine VM** "Ubuntu-SSH-Server"
2. **Warte** bis das Ubuntu-Menü erscheint (kann 1-2 Minuten dauern)

### Schritt 9: Ubuntu Installation (Schritt für Schritt)

**Folge genau diesen Schritten:**

1. **Try or Install Ubuntu Server** → Drücke **Enter**
2. **Sprache wählen**: Wähle "Deutsch" oder "English" (ich empfehle English, da Fehlermeldungen dann googelbar sind)
3. **Installer update**: Wähle "Continue without updating" (ohne Update weitermachen)
4. **Tastatur-Layout**: 
   - Wähle "German" falls du eine deutsche Tastatur hast
   - Teste mit ein paar Tasten ob alles stimmt
   - Drücke **Enter**
5. **Installation Type**: Wähle "Ubuntu Server" (sollte schon ausgewählt sein)
6. **Netzwerk-Verbindungen**: 
   - Sollte automatisch "enp0s3" mit einer IP wie 10.0.2.15 zeigen
   - **Das ist gut!** Drücke **Enter**
7. **Proxy**: Lass leer und drücke **Enter**
8. **Ubuntu Archive Mirror**: Standard lassen, drücke **Enter**
9. **Guided storage configuration**:
   - Wähle "Use an entire disk" (ganze Festplatte nutzen)
   - Wähle die angebotene Festplatte
   - Drücke **Enter**
10. **Storage configuration**: 
    - Schau dir kurz an was angezeigt wird (sollte eine Partition mit ca. 20 GB zeigen)
    - Drücke **Enter**
    - Bei "Confirm destructive action" → Wähle **"Continue"**

### Schritt 10: Benutzer anlegen (WICHTIG für SSH!)

**Jetzt kommt der wichtige Teil - hier erstellst du deinen SSH-Benutzer:**

1. **Profile setup**:
   - **Your name**: `Test User`
   - **Your server's name**: `ubuntu-ssh`  (genau so!)
   - **Pick a username**: `testuser` (genau so!)
   - **Choose a password**: Wähle ein einfaches Passwort wie `test123` (nur für Tests!)
   - **Confirm your password**: Wiederhole das Passwort
2. **Drücke Enter**

**Schreib dir auf:**
- Benutzername: `testuser`
- Passwort: `test123` (oder was du gewählt hast)

### Schritt 11: SSH aktivieren (ENTSCHEIDEND!)

1. **SSH Setup**: 
   - Du siehst "Install OpenSSH server"
   - **Drücke die Leertaste um das anzuhaken** 
   - Es sollte ein "X" in den eckigen Klammern erscheinen
   - **Das ist super wichtig!** Ohne das funktioniert SSH nicht.
2. **Drücke Enter**

### Schritt 12: Installation abschließen

1. **Featured Server Snaps**: 
   - Hier kannst du alles leer lassen (nichts auswählen)
   - Drücke **Enter**
2. **Warte** bis die Installation fertig ist (10-20 Minuten)
   - Du siehst einen Fortschrittsbalken
   - **Geh Kaffee trinken! ☕**
3. **Reboot Now**:
   - Wenn "Reboot Now" erscheint, drücke **Enter**
   - Warte bis die VM neu gestartet ist

### Schritt 13: Erste Anmeldung testen

Nach dem Neustart solltest du sehen:
```
ubuntu-ssh login:
```

1. **Tippe**: `testuser`
2. **Drücke Enter**
3. **Tippe dein Passwort**: `test123` (wird nicht angezeigt beim Tippen)
4. **Drücke Enter**

**Erfolgreich!** Du solltest jetzt etwas wie das sehen:
```
testuser@ubuntu-ssh:~$
```

### Schritt 14: SSH-Service überprüfen

In der VM tippe:
```bash
sudo systemctl status ssh
```

**Erklärt:**
- `sudo`: "Tu das als Administrator"
- `systemctl`: "System-Control" - verwaltet Services
- `status ssh`: "Zeig mir den Status vom SSH-Service"

Du solltest **"active (running)"** in grün sehen. Das bedeutet SSH läuft!

## Teil 5: Erste SSH-Verbindung von Windows

### Schritt 15: Windows Terminal oder PowerShell öffnen

**Option 1 - Windows Terminal (empfohlen):**
1. **Drücke**: `Windows-Taste + R`
2. **Tippe**: `wt`
3. **Drücke Enter**

**Option 2 - PowerShell:**
1. **Drücke**: `Windows-Taste + X`
2. **Klicke**: "Windows PowerShell" oder "Terminal"

**Option 3 - Eingabeaufforderung:**
1. **Drücke**: `Windows-Taste + R`
2. **Tippe**: `cmd`
3. **Drücke Enter**

### Schritt 16: SSH-Befehl testen

**Tippe genau das ein** (achte auf den Port!):
```bash
ssh -p 2222 testuser@localhost
```

**Befehl erklärt:**
- `ssh`: Das SSH-Programm (ist in Windows 11 dabei)
- `-p 2222`: "Nutze Port 2222" (unser weitergeleiteter Port)
- `testuser`: Der Benutzername in der Ubuntu-VM
- `@localhost`: "Verbinde zu localhost" (localhost = dein eigener Computer)

### Schritt 17: Host-Key akzeptieren

**Beim ersten Mal** siehst du sowas:
```
The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
ECDSA key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxx
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**Tippe**: `yes` **und drücke Enter**

**Was passiert?** SSH fragt: "Hey, ich kenne diesen Server noch nicht. Soll ich ihm vertrauen?" Du sagst "ja" und SSH merkt sich den Server für die Zukunft.

### Schritt 18: Passwort eingeben

Du siehst:
```
testuser@localhost's password:
```

**Tippe dein Passwort** (`test123`) **und drücke Enter**

**Hinweis**: Das Passwort wird beim Tippen NICHT angezeigt (das ist normal und sicher).

### Schritt 19: Erfolgreich verbunden! 🎉

Du solltest jetzt das sehen:
```
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-x-generic x86_64)
...
testuser@ubuntu-ssh:~$
```

**HERZLICHEN GLÜCKWUNSCH!** Du bist jetzt per SSH mit deiner Ubuntu-VM verbunden!

**Um das zu testen**, tippe:
```bash
whoami
```

Antwort sollte sein: `testuser`

## Teil 6: Wichtige SSH-Befehle lernen

### Navigation - Wo bin ich?

**Aktueller Ordner:**
```bash
pwd
```
**Bedeutung**: "Print Working Directory" = "Zeig mir wo ich bin"
**Antwort**: `/home/testuser` (dein Home-Ordner)

**Was ist in diesem Ordner?**
```bash
ls
```
**Bedeutung**: "List" = "Zeig mir alle Dateien und Ordner"

**Mehr Details zu den Dateien:**
```bash
ls -la
```
**Bedeutung**: 
- `-l`: "Long format" (Details wie Größe, Datum)
- `-a`: "All files" (auch versteckte Dateien die mit . anfangen)

### Ordner wechseln

**In einen anderen Ordner gehen:**
```bash
cd /tmp
pwd
```

**Zurück zum Home-Ordner:**
```bash
cd ~
pwd
```

**Eine Ebene nach oben:**
```bash
cd ..
pwd
```

**Erklärt:**
- `cd`: "Change Directory" = "Ordner wechseln"
- `/tmp`: Ein bestimmter Ordner
- `~`: Abkürzung für deinen Home-Ordner
- `..`: Bedeutet "eine Ebene höher"

### Dateien und Ordner erstellen

**Neuen Ordner erstellen:**
```bash
mkdir mein-test-ordner
ls
```

**In den Ordner wechseln:**
```bash
cd mein-test-ordner
pwd
```

**Leere Datei erstellen:**
```bash
touch test-datei.txt
ls -la
```

**Datei mit Inhalt erstellen:**
```bash
echo "Hallo von SSH!" > hallo.txt
ls -la
```

**Datei-Inhalt anzeigen:**
```bash
cat hallo.txt
```

**Erklärt:**
- `mkdir`: "Make Directory" = "Ordner erstellen"
- `touch`: Erstellt eine leere Datei
- `echo "text" >`: Schreibt Text in eine Datei
- `cat`: Zeigt den Inhalt einer Datei

### Datei bearbeiten mit nano

**Datei öffnen:**
```bash
nano hallo.txt
```

**Im nano-Editor:**
1. **Schreibe etwas dazu**, z.B. "Das ist mein SSH-Test!"
2. **Speichern**: Drücke `Ctrl + O`, dann Enter
3. **Beenden**: Drücke `Ctrl + X`

**Ergebnis prüfen:**
```bash
cat hallo.txt
```

### System-Informationen

**Wer bin ich?**
```bash
whoami
```

**Wie heißt der Computer?**
```bash
hostname
```

**Welches Betriebssystem?**
```bash
uname -a
```

**Datum und Uhrzeit:**
```bash
date
```

**Wie lange läuft das System schon?**
```bash
uptime
```

## Teil 7: Dateien zwischen Windows und Ubuntu übertragen

### Von Windows zur VM senden

**Erstelle zuerst eine Datei auf Windows:**

1. **Öffne den Windows-Editor** (Notepad)
2. **Schreibe**: "Das ist eine Datei von Windows!"
3. **Speichere** als `von-windows.txt` in deinem Desktop

**In PowerShell/Terminal (auf Windows):**
```bash
cd Desktop
scp -P 2222 von-windows.txt testuser@localhost:/home/testuser/
```

**Befehl erklärt:**
- `cd Desktop`: Gehe zum Desktop-Ordner
- `scp`: "Secure Copy" = Dateien per SSH kopieren
- `-P 2222`: Port 2222 nutzen (großes P bei scp!)
- `von-windows.txt`: Die Datei die kopiert werden soll
- `testuser@localhost:/home/testuser/`: Ziel (Benutzer@Computer:Pfad)

### Von VM zu Windows holen

**In der SSH-Verbindung zur VM:**
```bash
echo "Das kommt aus der VM!" > aus-vm.txt
```

**In PowerShell/Terminal (auf Windows):**
```bash
scp -P 2222 testuser@localhost:/home/testuser/aus-vm.txt .
```

**Das `.` am Ende bedeutet: "Speichere hier im aktuellen Ordner"**

### Übertragung prüfen

**In der VM prüfen:**
```bash
ls -la
cat von-windows.txt
```

**Auf Windows prüfen:**
- Schau in deinem aktuellen Ordner nach `aus-vm.txt`
- Öffne die Datei mit Notepad

## Teil 8: SSH-Verbindung verwalten

### Verbindung beenden

**Verschiedene Wege:**
```bash
exit
```

**Oder:**
```bash
logout
```

**Oder Tastenkombination:**
- `Ctrl + D`

**Du bist dann wieder in deinem Windows-Terminal.**

### Wieder verbinden

```bash
ssh -p 2222 testuser@localhost
```

**Jetzt fragst SSH nicht mehr nach dem Host-Key (nur beim ersten Mal).**

### Mehrere SSH-Verbindungen

Du kannst **mehrere Terminal-Fenster öffnen** und dich mehrmals gleichzeitig verbinden:

1. **Öffne ein neues Terminal-Fenster**
2. **Verbinde dich wieder**: `ssh -p 2222 testuser@localhost`

**Jetzt hast du zwei SSH-Verbindungen gleichzeitig!**

## Teil 9: SSH einfacher machen

### SSH-Config-Datei erstellen

**Das ist für Fortgeschrittene, aber sehr praktisch:**

1. **Auf Windows** öffne PowerShell
2. **Erstelle SSH-Ordner** (falls nicht vorhanden):
```bash
mkdir ~/.ssh
```

3. **Erstelle Config-Datei:**
```bash
notepad ~/.ssh/config
```

4. **Schreibe in die Datei:**
```
Host ubuntu-vm
    HostName localhost
    Port 2222
    User testuser
```

5. **Speichern und schließen**

**Jetzt kannst du dich einfacher verbinden:**
```bash
ssh ubuntu-vm
```

**Viel einfacher als der lange Befehl!**

## Teil 10: Praktische Übungen

### Übung 1: Ordner-Navigation
1. Verbinde dich per SSH zur VM
2. Erstelle einen Ordner namens "ssh-übung"
3. Gehe in diesen Ordner
4. Erstelle 3 Dateien: datei1.txt, datei2.txt, datei3.txt
5. Schreibe in jede Datei unterschiedlichen Inhalt
6. Liste alle Dateien mit Details auf
7. Zeige den Inhalt aller Dateien an

### Übung 2: Datei-Transfer
1. Erstelle auf deinem Windows-Desktop eine Datei "test-windows.txt"
2. Übertrage sie zur VM
3. Bearbeite die Datei in der VM (mit nano)
4. Übertrage sie zurück nach Windows
5. Öffne sie auf Windows und prüfe die Änderungen

### Übung 3: System erkunden
1. Zeige alle laufenden Prozesse an: `ps aux`
2. Zeige die Festplattenbelegung: `df -h`
3. Zeige die Systemlaufzeit: `uptime`
4. Finde heraus welche Version Ubuntu läuft: `cat /etc/os-release`

## Teil 11: Wenn etwas nicht funktioniert

### Problem: "Connection refused"

**Das bedeutet**: SSH kann sich nicht verbinden.

**Lösungen:**
1. **Ist die VM gestartet?** Schau in VirtualBox
2. **Läuft SSH in der VM?** In der VM tippen: `sudo systemctl status ssh`
3. **Port-Weiterleitung richtig?** In VirtualBox → VM → Einstellungen → Netzwerk → Port-Weiterleitung prüfen

### Problem: "Permission denied"

**Das bedeutet**: Falscher Benutzername oder Passwort.

**Lösungen:**
1. **Benutzername prüfen**: Ist es wirklich `testuser`?
2. **Passwort prüfen**: Tipp vorsichtig, man sieht es nicht
3. **In der VM direkt anmelden** und prüfen ob Benutzername/Passwort stimmen

### Problem: "Port already in use"

**Das bedeutet**: Port 2222 wird schon verwendet.

**Lösungen:**
1. **Andere SSH-Verbindung schließen**
2. **Anderen Port verwenden**: In VirtualBox Port-Weiterleitung auf 2223 ändern
3. **Windows neu starten** (seltener nötig)

### Problem: SSH ist sehr langsam

**Lösungen:**
1. **Mehr RAM für VM**: VirtualBox → Einstellungen → System → 4096 MB
2. **VM-Einstellungen optimieren**: Beschleunigung aktivieren

### Debug-Informationen anzeigen

**Ausführliche SSH-Verbindung:**
```bash
ssh -v -p 2222 testuser@localhost
```

**Noch mehr Details:**
```bash
ssh -vvv -p 2222 testuser@localhost
```

**Das zeigt dir genau was SSH macht und wo es eventuell hakt.**

## Teil 12: Nächste Schritte

### Was du jetzt kannst:
- VirtualBox und Ubuntu Server installieren
- SSH-Verbindungen aufbauen
- Linux-Befehle über SSH ausführen
- Dateien zwischen Windows und Linux übertragen
- Probleme selbst lösen


### Hilfreiche Befehle:

**Navigation:**
- `pwd` - Wo bin ich?
- `ls -la` - Was ist hier?
- `cd ordner` - Gehe in Ordner
- `cd ..` - Eine Ebene hoch
- `cd ~` - Nach Hause

**Dateien:**
- `touch datei.txt` - Leere Datei erstellen
- `echo "text" > datei.txt` - Datei mit Text erstellen
- `cat datei.txt` - Datei anzeigen
- `nano datei.txt` - Datei bearbeiten

**Transfer:**
- `scp -P 2222 datei.txt testuser@localhost:~/` - Von Windows zur VM
- `scp -P 2222 testuser@localhost:~/datei.txt .` - Von VM zu Windows

**SSH:**
- `ssh -p 2222 testuser@localhost` - Verbinden (mit Passwort)
- `ssh ubuntu-vm` - Verbinden (mit Config)
- `exit` - Verbindung beenden

**SSH-Keys:**
- `ssh-keygen -t ed25519` - Neuen SSH-Key erstellen
- `type %USERPROFILE%\.ssh\id_ed25519.pub` - Öffentlichen Key anzeigen
- `ssh-add ~/.ssh/id_ed25519` - Key zum SSH-Agent hinzufügen

## Zusammenfassung

Du hast erfolgreich gelernt:

1. **VirtualBox auf Windows 11 installieren** und konfigurieren
2. **Ubuntu Server in einer VM aufsetzen** mit allen wichtigen Einstellungen
3. **SSH-Verbindungen herstellen** von Windows zur Linux-VM
4. **Linux-Befehle ausführen** über die SSH-Verbindung
5. **Dateien übertragen** zwischen Windows und Linux
6. **Probleme lösen** wenn etwas nicht funktioniert

**Das ist eine solide Grundlage für:**
- Server-Administration
- Webentwicklung
- DevOps
- Cloud-Computing
- Linux-Administration

SSH ist ein Werkzeug, das Profis täglich nutzen. Du hast jetzt die Grundlagen und kannst darauf aufbauen!

**Tipp**: Übe regelmäßig! Je öfter du SSH nutzt, desto natürlicher wird es. Experimentiere, probiere neue Befehle aus - in der VM kannst du nichts kaputt machen! 
