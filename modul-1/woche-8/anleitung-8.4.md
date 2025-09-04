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
3. **Klicke auf**: "Download Ubuntu 24.04.3 LTS"
4. **Warte** bis der Download fertig ist (ca. 1-2 GB, kann 10-30 Minuten dauern)
5. **Merke dir den Pfad**: Normalerweise `C:\Users\DeinName\Downloads\ubuntu-24.04.x-live-server-amd64.iso`

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

### Schritt 19: Erfolgreich verbunden! 

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

## Teil 9: SSH-Keys verwenden (Professionell & Sicher!)

### Was sind SSH-Keys und warum sind sie besser?

**Bisher** hast du dich mit einem **Passwort** angemeldet. Das ist wie ein Türschlüssel aus Plastik.

**SSH-Keys** sind wie ein **High-Tech Fingerabdruck-Scanner**:

**Vorteile von SSH-Keys:**
- 🔐 **Viel sicherer** als Passwörter (mathematisch quasi unknackbar)
- 🚀 **Schneller** - keine Passwort-Eingabe nötig
- 🤖 **Automatisierung** - Scripts können sich ohne Passwort verbinden
- 💪 **Professionell** - so arbeiten alle Profis

**Wie funktionieren SSH-Keys?**
- Du erstellst ein **Schlüsselpaar**: Einen **privaten** und einen **öffentlichen** Schlüssel
- **Privater Schlüssel**: Bleibt auf deinem Windows-Computer (wie dein Fingerabdruck)
- **Öffentlicher Schlüssel**: Wird auf den Ubuntu-Server kopiert (wie der Scanner im Türschloss)
- **Anmeldung**: SSH prüft automatisch ob dein privater und öffentlicher Schlüssel zusammenpassen

### Schritt 20: SSH-Key-Paar auf Windows erstellen

**Stelle sicher, dass du NICHT in der SSH-Verbindung bist!**
Falls doch, tippe `exit` um zurück zu Windows zu kommen.

**In PowerShell/Terminal (auf Windows):**
```bash
ssh-keygen -t ed25519 -C "mein-ssh-test"
```

**Befehl erklärt:**
- `ssh-keygen`: "SSH-Key generieren"
- `-t ed25519`: Verwende den modernen, sicheren Ed25519-Algorithmus
- `-C "mein-ssh-test"`: Ein Kommentar zur Identifikation

**Du wirst gefragt:**
```
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\DeinName\.ssh\id_ed25519):
```

**Drücke einfach Enter** (um den Standard-Pfad zu verwenden)

**Dann:**
```
Enter passphrase (empty for no passphrase):
```

**Für diese Übung drücke zweimal Enter** (kein Passphrase). 
*Hinweis: In der Praxis würdest du hier ein starkes Passphrase verwenden!*

**Du siehst dann sowas:**
```
Your identification has been saved in C:\Users\DeinName\.ssh\id_ed25519
Your public key has been saved in C:\Users\DeinName\.ssh\id_ed25519.pub
The key fingerprint is:
SHA256:aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890abcdef mein-ssh-test
```

**GESCHAFFT!** Du hast jetzt ein SSH-Key-Paar:
- **Privater Schlüssel**: `C:\Users\DeinName\.ssh\id_ed25519` (GEHEIM!)
- **Öffentlicher Schlüssel**: `C:\Users\DeinName\.ssh\id_ed25519.pub` (kann geteilt werden)

### Schritt 21: Öffentlichen Schlüssel anzeigen

**Zeige deinen öffentlichen Schlüssel:**
```bash
type %USERPROFILE%\.ssh\id_ed25519.pub
```

**Du siehst eine Zeile wie:**
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOqW7r4fQw... mein-ssh-test
```

**Das ist dein öffentlicher Schlüssel!** Kopiere diese ganze Zeile (markieren und Ctrl+C).

### Schritt 22: Öffentlichen Schlüssel zur Ubuntu-VM übertragen

**Jetzt müssen wir den öffentlichen Schlüssel zur Ubuntu-VM bringen.**

**Methode 1 - Automatisch (einfach):**

```bash
type %USERPROFILE%\.ssh\id_ed25519.pub | ssh -p 2222 testuser@localhost "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

**Du musst dein Passwort eingeben** (`test123`) - das ist das letzte Mal!

**Befehl erklärt:**
- `type ...\.ssh\id_ed25519.pub`: Zeige den öffentlichen Schlüssel
- `|`: "Pipe" - schicke die Ausgabe weiter
- `ssh -p 2222 testuser@localhost`: Verbinde zur VM
- `"mkdir -p ~/.ssh"`: Erstelle SSH-Ordner falls nicht vorhanden
- `&& cat >> ~/.ssh/authorized_keys"`: Und hänge den Schlüssel an die authorized_keys-Datei an

**Methode 2 - Manuell (zum Verstehen):**

Falls Methode 1 nicht funktioniert:

1. **Verbinde dich zur VM:**
   ```bash
   ssh -p 2222 testuser@localhost
   ```

2. **In der VM - SSH-Ordner erstellen:**
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```

3. **authorized_keys-Datei bearbeiten:**
   ```bash
   nano ~/.ssh/authorized_keys
   ```

4. **Füge deinen öffentlichen Schlüssel ein:**
   - Kopiere die ganze Zeile die du vorhin mit `type` angezeigt hast
   - Füge sie in nano ein (Rechtsklick oder Ctrl+V)
   - Speichere: `Ctrl + O`, dann Enter
   - Beende nano: `Ctrl + X`

5. **Berechtigungen setzen:**
   ```bash
   chmod 600 ~/.ssh/authorized_keys
   ```

6. **VM verlassen:**
   ```bash
   exit
   ```

### Schritt 23: SSH-Key-Verbindung testen

**Jetzt der spannende Moment! Verbinde dich OHNE Passwort:**

```bash
ssh -p 2222 testuser@localhost
```

**MAGIE!** 🎩✨ Du solltest OHNE Passwort-Eingabe verbunden sein!

**Falls es nicht funktioniert:**
- Prüfe ob der öffentliche Schlüssel richtig kopiert wurde
- Siehe Troubleshooting-Bereich weiter unten

### Schritt 24: SSH-Key-Verbindung mit scp testen

**Auch Datei-Transfer funktioniert jetzt ohne Passwort:**

1. **Erstelle eine Test-Datei auf Windows:**
   ```bash
   echo "SSH-Key Test!" > ssh-key-test.txt
   ```

2. **Übertrage ohne Passwort:**
   ```bash
   scp -P 2222 ssh-key-test.txt testuser@localhost:~/
   ```

3. **Prüfe in der VM:**
   ```bash
   ssh -p 2222 testuser@localhost "cat ssh-key-test.txt"
   ```

**Alles ohne Passwort! Das ist die Kraft von SSH-Keys!**

### Schritt 25: Mehrere SSH-Keys verwalten

**Du kannst mehrere SSH-Keys für verschiedene Server haben:**

**Neuen SSH-Key für einen anderen Zweck erstellen:**
```bash
ssh-keygen -t ed25519 -f %USERPROFILE%\.ssh\id_ed25519_server2 -C "server2-key"
```

**Bestimmten Key verwenden:**
```bash
ssh -i %USERPROFILE%\.ssh\id_ed25519_server2 -p 2222 testuser@localhost
```

**Befehl erklärt:**
- `-i`: "Identity file" - verwende diesen spezifischen Schlüssel

### Schritt 26: SSH-Agent verwenden (Erweitert)

**Der SSH-Agent speichert deine Keys im Speicher, damit du nicht bei jedem Befehl den Key angeben musst.**

**SSH-Agent starten:**
```bash
ssh-agent
```

**Key zum Agent hinzufügen:**
```bash
ssh-add %USERPROFILE%\.ssh\id_ed25519
```

**Alle geladenen Keys anzeigen:**
```bash
ssh-add -l
```

### SSH-Keys Übungen

#### Übung 1: Key-basierte Anmeldung testen
1. Stelle sicher, dass du dich OHNE Passwort anmelden kannst
2. Verbinde dich 5 mal hintereinander - sollte jedes Mal sofort gehen
3. Teste auch scp ohne Passwort-Eingabe

#### Übung 2: Zweiten SSH-Key erstellen
1. Erstelle einen zweiten SSH-Key mit dem Namen `id_ed25519_backup`
2. Kopiere auch diesen öffentlichen Schlüssel zur VM
3. Teste die Anmeldung mit beiden Keys

#### Übung 3: SSH-Keys verstehen
1. Schaue dir deinen privaten und öffentlichen Schlüssel an
2. Versuche zu verstehen: Was passiert wenn jemand deinen privaten Schlüssel stiehlt?
3. Was passiert wenn jemand nur deinen öffentlichen Schlüssel hat?

## Teil 10: SSH-Sicherheit verstärken (Optional)

### Passwort-Authentifizierung deaktivieren

**Nachdem SSH-Keys funktionieren, kannst du Passwort-Login deaktivieren für maximale Sicherheit:**

1. **Verbinde dich zur VM:**
   ```bash
   ssh -p 2222 testuser@localhost
   ```

2. **SSH-Konfiguration bearbeiten:**
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

3. **Suche diese Zeilen und ändere sie:**
   ```
   PasswordAuthentication no
   ChallengeResponseAuthentication no
   UsePAM no
   ```

4. **SSH-Service neu starten:**
   ```bash
   sudo systemctl reload ssh
   ```

5. **Teste in einem NEUEN Terminal:**
   - SSH-Keys sollten funktionieren
   - Passwort-Login sollte nicht mehr möglich sein

**ACHTUNG!** Mach das nur wenn du 100% sicher bist, dass deine SSH-Keys funktionieren!

### Root-Login deaktivieren

**Zusätzliche Sicherheit:**
```bash
sudo nano /etc/ssh/sshd_config
```

**Ändere:**
```
PermitRootLogin no
```

**Und starte SSH neu:**
```bash
sudo systemctl reload ssh
```

## Teil 11: SSH einfacher machen

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
    IdentityFile ~/.ssh/id_ed25519

Host ubuntu-vm-password
    HostName localhost
    Port 2222
    User testuser
    PreferredAuthentications password
```

5. **Speichern und schließen**

**Jetzt kannst du dich einfacher verbinden:**
```bash
ssh ubuntu-vm
```

**Oder mit Passwort erzwingen:**
```bash
ssh ubuntu-vm-password
```

**Viel einfacher als der lange Befehl!**

### SSH-Config erweitern

**Für mehrere Server:**
```
Host ubuntu-vm
    HostName localhost
    Port 2222
    User testuser
    IdentityFile ~/.ssh/id_ed25519

Host production-server
    HostName 192.168.1.100
    Port 22
    User admin
    IdentityFile ~/.ssh/id_ed25519_production

Host development-server
    HostName dev.example.com
    Port 22
    User developer
    IdentityFile ~/.ssh/id_ed25519_dev
    ForwardAgent yes
```



## Teil 12: Wenn etwas nicht funktioniert

### Problem: SSH-Keys funktionieren nicht

**Das bedeutet**: Du wirst immer noch nach dem Passwort gefragt.

**Debug-Schritte:**

1. **Ausführliche SSH-Verbindung:**
   ```bash
   ssh -v -p 2222 testuser@localhost
   ```
   
   Schaue nach Zeilen wie:
   - `Offering public key: ...` (gut!)
   - `Server refused our key` (schlecht!)

2. **Prüfe ob der öffentliche Schlüssel richtig übertragen wurde:**
   ```bash
   ssh -p 2222 testuser@localhost "cat ~/.ssh/authorized_keys"
   ```
   
   Dein öffentlicher Schlüssel sollte dort stehen.

3. **Prüfe Berechtigungen in der VM:**
   ```bash
   ssh -p 2222 testuser@localhost "ls -la ~/.ssh/"
   ```
   
   Sollte zeigen:
   - `drwx------` für `.ssh/` (700)
   - `-rw-------` für `authorized_keys` (600)

4. **Berechtigungen korrigieren falls nötig:**
   ```bash
   ssh -p 2222 testuser@localhost "chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
   ```

### Problem: "Permission denied (publickey)"

**Lösungen:**
1. **Öffentlicher Schlüssel nicht richtig kopiert**: Wiederhole Schritt 22
2. **Falsche Berechtigungen**: Siehe oben
3. **Passwort-Auth deaktiviert aber Keys funktionieren nicht**: Reaktiviere temporär Passwort-Auth

### Problem: "Connection refused"

**Das bedeutet**: SSH kann sich nicht verbinden.

**Lösungen:**
1. **Ist die VM gestartet?** Schau in VirtualBox
2. **Läuft SSH in der VM?** In der VM tippen: `sudo systemctl status ssh`
3. **Port-Weiterleitung richtig?** In VirtualBox → VM → Einstellungen → Netzwerk → Port-Weiterleitung prüfen

### Problem: SSH ist sehr langsam

**Lösungen:**
1. **Mehr RAM für VM**: VirtualBox → Einstellungen → System → 4096 MB
2. **VM-Einstellungen optimieren**: Beschleunigung aktivieren
3. **DNS-Lookup deaktivieren**: In VM `/etc/ssh/sshd_config` → `UseDNS no`

### Problem: Key funktioniert plötzlich nicht mehr

**Mögliche Ursachen:**
1. **authorized_keys-Datei beschädigt**: Neu erstellen
2. **VM wurde zurückgesetzt**: Öffentlichen Key neu kopieren
3. **SSH-Config Problem**: Config-Datei prüfen

### Debug-Informationen anzeigen

**Sehr ausführliche SSH-Verbindung:**
```bash
ssh -vvv -p 2222 testuser@localhost
```

**SSH-Key-Fingerprint prüfen:**
```bash
ssh-keygen -lf %USERPROFILE%\.ssh\id_ed25519.pub
```

**Welche Keys bietet SSH an:**
```bash
ssh-add -l
```

## Teil 13: Nächste Schritte

### Was du jetzt kannst:
- VirtualBox und Ubuntu Server installieren
- SSH-Verbindungen aufbauen (mit Passwort und Keys)
- Linux-Befehle über SSH ausführen
- Dateien zwischen Windows und Linux übertragen
- SSH-Keys erstellen und verwenden
- SSH-Verbindungen absichern
- Probleme selbst lösen

### Weiterführende Themen:
- **SSH-Tunneling**: Sichere Verbindungen durch Firewalls
- **SSH-Agent Forwarding**: SSH-Keys weiterreichen
- **SSH-Konfiguration**: Erweiterte Einstellungen
- **Fail2ban**: Automatischer Schutz vor Brute-Force-Angriffen
- **SSH-Certificates**: Enterprise SSH-Verwaltung

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

**SSH-Keys (Windows):**
- `ssh-keygen -t ed25519` - Neuen SSH-Key erstellen
- PowerShell: `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub` - Öffentlichen Key anzeigen
- CMD: `type %USERPROFILE%\.ssh\id_ed25519.pub` - Öffentlichen Key anzeigen
- `ssh-add $env:USERPROFILE\.ssh\id_ed25519` - Key zum SSH-Agent hinzufügen
- `ssh-add -l` - Geladene Keys anzeigen

## Zusammenfassung

Du hast erfolgreich gelernt:

1. **VirtualBox auf Windows 11 installieren** und konfigurieren
2. **Ubuntu Server in einer VM aufsetzen** mit allen wichtigen Einstellungen
3. **SSH-Verbindungen herstellen** von Windows zur Linux-VM (mit Passwort)
4. **SSH-Keys erstellen und verwenden** für sichere, passwortlose Anmeldung
5. **Linux-Befehle ausführen** über die SSH-Verbindung
6. **Dateien übertragen** zwischen Windows und Linux (mit und ohne Passwort)
7. **SSH-Verbindungen absichern** und optimieren
8. **Probleme lösen** wenn etwas nicht funktioniert

**Das ist eine professionelle Grundlage für:**
- Server-Administration
- Webentwicklung
- DevOps
- Cloud-Computing
- Linux-Administration
- Automatisierung und Scripting

SSH mit Keys ist der Standard in der Industrie. Du nutzt jetzt die gleichen Techniken wie Profis weltweit!

**Tipp**: Übe regelmäßig! Je öfter du SSH nutzt, desto natürlicher wird es. Experimentiere, probiere neue Befehle aus - in der VM kannst du nichts kaputt machen!
