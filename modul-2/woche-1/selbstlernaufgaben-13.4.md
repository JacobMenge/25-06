# Selbstlernaufgaben – Linux Benutzer & Rechteverwaltung (Erweitert)

Bitte lade deine Ergebnisse bis spätestens Sonntag um 23:59 Uhr im Google Classroom zur entsprechenden Aufgabe hoch.  

---

## 1. Grundlagenaufgabe – Dateirechte analysieren  

**Deine Aufgabe:**  
Analysiere die folgenden Dateirechte. Schreibe jeweils auf, welche Rechte **Besitzer**, **Gruppe** und **Andere** haben.  

### Symbolische Schreibweise  
1. `-rw-r--r--`  
2. `-rwxr-x---`  
3. `-rwxrwxrwx`  
4. `-rw-------`  
5. `-r--r--r--`  

### Oktale Schreibweise  
6. `600`  
7. `664`  
8. `467`  
9. `755`  
10. `640`  

**Zusatz:**  
Erkläre in 1–2 Sätzen, warum eine sehr großzügige Rechtevergabe (z. B. `777`) in der Praxis ein Sicherheitsrisiko darstellt.  

**Formatvorschläge:**  
- Textdatei mit Tabelle oder Stichpunkten  

---

## 2. Grundlagenaufgabe – Rechte in Schreibweisen umwandeln  

**Deine Aufgabe:**  
Hier sind 5 Beispiele von Dateiberechtigungen in natürlicher Sprache beschrieben.  
Schreibe für jedes Beispiel die **symbolische Schreibweise** (z. B. `-rw-r--r--`) und die **oktal Schreibweise** (z. B. `644`) auf.  

1. Besitzer darf nur lesen und ausführen, Gruppe darf nur ausführen, andere dürfen nichts.  
2. Besitzer darf alles, Gruppe darf nur schreiben, andere dürfen nichts.  
3. Besitzer darf lesen und schreiben, Gruppe darf nichts, andere dürfen nur lesen.  
4. Besitzer darf nur schreiben, Gruppe darf nur lesen, andere dürfen nichts.  
5. Besitzer darf alles, Gruppe darf lesen und ausführen, andere dürfen nur lesen.  

**Formatvorschläge:**  
- Textdatei mit Tabelle oder Stichpunkten  

---

## 3. Grundlagenaufgabe – Rechte mit chmod (Symbolisch und Oktal)  

**Deine Aufgabe:**  
- Erstelle zwei Dateien:  
  - `bericht_symbolisch.txt` (für die symbolische Rechtevergabe)  
  - `bericht_oktal.txt` (für die oktale Rechtevergabe)  
- Setze die Rechte für **bericht_symbolisch.txt** symbolisch so, dass:  
  - der Besitzer alles darf,  
  - die Gruppe nur lesen darf,  
  - andere gar nichts dürfen.  
- Setze die Rechte für **bericht_oktal.txt** mit dem Oktalmodus auf dieselbe Konfiguration.  
- Schreibe **alle verwendeten Befehle** in deine Lösung auf (einschließlich Kontrollausgaben mit `ls -l`).  
- Erkläre außerdem, wie du die verwendete Oktalzahl berechnet hast.  

**Formatvorschläge:**  
- Textdatei mit den Befehlen, Screenshots (optional) und kurzer Erklärung  

---

## 4. Weiterführende Aufgabe – chown und Zusammenarbeit simulieren  

**Deine Aufgabe:**  
- Lege die Benutzer `dev1` und `dev2` an.  
- Erstelle ein gemeinsames Projektverzeichnis `/home/projekt`.  
- Setze den Besitzer auf `dev1` und die Gruppe auf `entwicklung`.  
- Füge `dev2` der Gruppe `entwicklung` hinzu.  
- Teste, ob `dev2` Schreibrechte hat. Falls nicht: Welche zusätzlichen Befehle (Stichwort: `chmod`) sind notwendig?  

**Formatvorschläge:**  
- Textdatei mit Befehlen und kurzer Begründung, warum Gruppen hier sinnvoll sind  

---

## 5. Bonus-Aufgabe – Sicherheits-Szenario mit Gruppen, Besitzern & Dateien  

**Deine Aufgabe:**  
Stelle dir vor, du bist Admin eines Uni-Rechners. Folgende Personen sollen arbeiten:  

- `professor`  
- `student1`  
- `student2`  
- `admin`  

### Schritt 1: Benutzer & Gruppen  
- Lege die Benutzer an.  
- Erstelle die Gruppen:  
  - `dozenten` → enthält `professor`  
  - `studierende` → enthält `student1` und `student2`  
  - `admins` → enthält `admin`  

### Schritt 2: Dateien, Besitzer & Rechte  
Erstelle folgende Dateien und setze **Besitzer**, **Gruppe** und **Berechtigungen** so, dass:  

1. `klausuren.txt`  
   - Besitzer: `professor`  
   - Gruppe: `dozenten`  
   - Rechte: Besitzer und Gruppe dürfen lesen & schreiben, andere gar nichts.  

2. `skripte.txt`  
   - Besitzer: `professor`  
   - Gruppe: `studierende`  
   - Rechte: Besitzer darf lesen & schreiben, Gruppe nur lesen, andere gar nichts.  

3. `systemlog.txt`  
   - Besitzer: `admin`  
   - Gruppe: `admins`  
   - Rechte: Besitzer darf alles, Gruppe darf lesen, andere gar nichts.  

> Hinweis: Setze die **Besitzer** explizit neu (z. B. mit `chown`), nicht nur die Gruppen oder Standardwerte.  

### Schritt 3: Reflexion  
- Erkläre in 3–4 Sätzen, warum es sinnvoll ist, **Besitzer** und **Gruppe** gezielt zu setzen, anstatt sich auf Standardwerte zu verlassen.  
- Welche Sicherheitsprobleme könnten entstehen, wenn der Besitzer nicht korrekt gesetzt ist?  

**Formatvorschläge:**  
- Textdatei mit den verwendeten Befehlen (`adduser`, `addgroup`, `usermod`, `chown`, `chmod`, `ls -l`) und deiner Reflexion  
