# Selbstlernaufgaben - Linux Dateisystem

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Linux Dateisystem Quiz

Deine Aufgabe:

Beantworte folgende Multiple Choice-Fragen. Gucke für die Lösung in den Folien nach oder recherchiere im Internet.

Aufgabe I: Filesystem Hierarchy Standard   
Was beschreibt der Filesystem Hierarchy Standard (FHS)?  
A) Wie schnell die Festplatte Daten lesen kann  
B) Wie Verzeichnisse und Dateien in Linux organisiert sind  
C) Welche Farbe der Desktop-Hintergrund hat  
D) Wie groß der Arbeitsspeicher ist  
 
Aufgabe II: Wichtige Verzeichnisse   
Welches Verzeichnis enthält Konfigurationsdateien?  
A) /bin  
B) /etc  
C) /home  
D) /usr  

Aufgabe III: Absolute Pfade   
Welcher der folgenden ist ein absoluter Pfad?  
A) ../Dokumente/plan.txt   
B) ./Bilder/foto.jpg  
C) /home/user/Dokumente/plan.txt  
D) plan.txt  

Aufgabe IV: Relative Pfade   
Angenommen, du befindest dich im Verzeichnis /home/user/Dokumente/.  
Wie würdest du mit einem relativen Pfad zur Datei /home/user/Bilder/foto.jpg gelangen?  
A) ../Bilder/foto.jpg  
B) /Bilder/foto.jpg  
C) ./Bilder/foto.jpg  
D) ../../Bilder/foto.jpg  

Aufgabe V: Terminalbefehle   
Welcher Befehl zeigt dir den Inhalt einer Textdatei direkt im Terminal an?  
A) ls  
B) cat  
C) mkdir  
D) rm  

Formatvorschläge
- Textdatei


## 2. Grundlagenaufgabe - Verzeichnisbaum und Pfade

Deine Aufgabe:
Gegeben sei folgender Verzeichnisbaum:

```
/
 ├── etc
 │    └── network
 │         └── config.txt
 ├── home
 │    └── user
 │         ├── Dokumente
 │         │     └── hausaufgabe.txt
 │         ├── Bilder
 │         │     └── urlaub.png
 │         └── Projekte
 │               └── linux
 │                    └── script.sh
 └── var
      └── log
           └── system.log
```

Bestimme jeweils den absoluten und den relativen Pfad für folgende Fälle:

1. Von hausaufgabe.txt zu urlaub.png
2. Von script.sh zu system.log
3. Von config.txt zu hausaufgabe.txt

Formatvorschläge
- Textdatei


## 3. Grundlagenaufgabe - Dateiverwaltung mit Terminal

Deine Aufgabe:
Arbeite mit dem Terminal und probiere Befehle zur Dateiverwaltung aus.
- Erstelle ein eigenes Verzeichnis und lege darin Dateien an.
- Verschiebe, kopiere und benenne Dateien um.
- Lösche am Ende eine Datei oder ein Verzeichnis.
- Dokumentiere die verwendeten Befehle und deine Beobachtungen.

Formatvorschläge
- Textdatei mit Befehlen (optional mit Screenshots über die "Drucken"-Taste)


## 4. Weiterführende Selbstlernaufgabe - Navigation & Pfade

Deine Aufgabe:
Simuliere eine kleine Dateisuche im Terminal.

- Navigiere zu einem Verzeichnis deiner Wahl.
- Erstelle dort Unterordner und Dateien (z. B. mit mkdir, touch).
- Notiere dir anschließend den absoluten Pfad zu einer der Dateien.
- Finde mindestens zwei verschiedene relative Pfade, mit denen du dieselbe Datei erreichen kannst (je nach Startpunkt unterschiedlich).

Hinweis: Nutze pwd und ls, um dich zu orientieren.

Formatvorschläge
- Textdatei


## 5. Bonus: Selbstlernaufgabe - Nano & Textdateien

Deine Aufgabe:

- Erstelle mit nano eine neue Datei tagebuch.txt.
- Schreibe ein paar Zeilen hinein (z. B. wie dir die Linux-Übungen gefallen).
- Speichere die Datei und verlasse den Editor.
- Zeige den Inhalt mit cat im Terminal an.
- Reflektiere in 3–4 Sätzen: Was gefällt dir am Arbeiten mit nano, was weniger?

Formatvorschläge
- Textdatei

JPG, PNG
