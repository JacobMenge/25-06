# Selbstlernaufgaben - Linux Benutzer & Rechteverwaltung

Bitte lade deine Ergebnisse bis spätestens Sonntag um 23:59 Uhr im Google Classroom zur entsprechenden Aufgabe hoch.

## 1. Grundlagenaufgabe - Linux Rechte Quiz

Deine Aufgabe:

Beantworte folgende Multiple Choice-Fragen. Gucke für die Lösung in den Folien nach oder recherchiere im Internet.

Aufgabe I: Benutzer & Gruppen (Grundlegend)  
Was beschreibt eine Gruppe in Linux?  
A) Eine Sammlung von Dateien  
B) Eine Sammlung von Benutzern, die gemeinsame Rechte teilen  
C) Ein Verzeichnis im Dateisystem  
D) Einen speziellen Admin-Befehl  

Aufgabe II: Root-User (Grundlegend)  
Was ist der root-Benutzer?  
A) Ein normaler User ohne Rechte  
B) Der Superuser mit uneingeschränkten Rechten   
C) Ein Gastkonto  
D) Eine Gruppe von Administratoren  

Aufgabe III: Dateien passwd & group (Grundlegend)  
Welche Aussage ist korrekt?  
A) /etc/passwd enthält alle Benutzerkonten, /etc/group enthält Gruppeninformationen.  
B) /etc/passwd enthält nur Passwörter, /etc/group enthält Dateiberechtigungen.  
C) Beide Dateien enthalten ausschließlich verschlüsselte Passwörter.  
D) Beide Dateien können nur vom root-Benutzer gelesen werden.  

Aufgabe IV: Sudo vs. Su (Anspruchsvoll)  
Worin besteht der Unterschied zwischen sudo und su?  
A) sudo wechselt dauerhaft zu root, su nur kurzzeitig  
B) sudo führt einzelne Befehle mit Superuser-Rechten aus, su wechselt in eine andere Benutzerumgebung  
C) Beide machen exakt dasselbe  
D) su funktioniert nur im GUI, sudo nur im Terminal  

Aufgabe V: Datei-Rechte (Knifflig)  
Gegeben sei eine Datei mit Rechten -rw-r--r--.  
Was bedeutet das?  
A) Besitzer darf lesen & schreiben, Gruppe darf lesen, andere dürfen lesen  
B) Besitzer darf alles, Gruppe darf nichts, andere dürfen lesen  
C) Alle dürfen lesen & schreiben  
D) Besitzer darf lesen, Gruppe darf schreiben, andere nichts  

Formatvorschläge
- Textdatei

## 2. Grundlagenaufgabe - Benutzer & Gruppen anlegen

Deine Aufgabe:
Führe die folgenden Aufgaben im Terminal durch und dokumentiere:

- Lege einen neuen Benutzer testuser an.
- Finde den neuen Eintrag in der Datei /etc/passwd.
- Lege eine Gruppe projekt an.
- Füge testuser der Gruppe projekt hinzu.
- Überprüfe mit id testuser, ob die Gruppenzugehörigkeit korrekt angezeigt wird.

Formatvorschläge
- Textdatei mit Befehlen & (optional) Screenshots

## 3. Grundlagenaufgabe - Rechte verstehen

Deine Aufgabe:

- Erstelle eine Textdatei notizen.txt.
- Zeige mit ls -l notizen.txt die aktuellen Rechte an.
- Ändere die Rechte so, dass nur der Besitzer schreiben darf, Gruppe und andere dürfen nur lesen.
- Überprüfe erneut mit ls -l, ob die Änderungen übernommen wurden.

Formatvorschläge
- Textdatei mit Befehlen & (optional) Screenshots

## 4. Weiterführende Selbstlernaufgabe - chown & chmod

Deine Aufgabe:

Lege zwei Benutzer (anna und ben) an.
- Erstelle eine Datei projekt.txt als Benutzer anna.
- Ändere mit chown den Besitzer der Datei auf ben.
- Verändere mit chmod die Rechte so, dass nur noch ben Zugriff hat.
- Teste, ob anna noch auf die Datei zugreifen kann.

Formatvorschläge
- Textdatei


## 5. Bonus: Selbstlernaufgabe - Szenario & Reflexion

Deine Aufgabe:

Stelle dir vor, du bist Administrator in einer kleinen Firma.
- Lege 3 Benutzer an: chef, mitarbeiter1, mitarbeiter2.
- Erstelle eine Gruppe buchhaltung.
- Weise nur chef und mitarbeiter1 der Gruppe zu.
- Lege einen Ordner finanzen an, auf den nur die Gruppe buchhaltung Zugriff hat.
- Reflektiere: Warum ist es sinnvoll, mit Gruppen statt mit individuellen Benutzerrechten zu arbeiten?

Formatvorschläge
- Textdatei
