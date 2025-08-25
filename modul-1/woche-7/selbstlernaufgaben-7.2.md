# Selbstlernaufgaben – Bash Arithmetik, Eingaben & Kontrollstrukturen

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.  

---

## 1. Grundlagenaufgabe – Erste Berechnung 

**Deine Aufgabe:**  
Schreibe ein Skript `addieren.sh`, das:  
1. Zwei Variablen `a=5` und `b=7` anlegt.  
2. Beide Zahlen mit `echo $((a+b))` addiert und das Ergebnis ausgibt.  
3. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 2. Grundlagenaufgabe – Eingabe und Weiterverarbeitung

**Deine Aufgabe:**  
Erstelle ein Skript `eingabe.sh`, das:  
1. Den Benutzer mit `read` nach seiner Lieblingszahl fragt.  
2. Die Eingabe in einer Variablen speichert.  
3. Mit einer Berechnung die Zahl um 1 erhöht und das Ergebnis ausgibt (z. B. aus 7 wird 8).  
4. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 3. Grundlagenaufgabe – Einfache Bedingung 

**Deine Aufgabe:**  
Schreibe ein Skript `ifcheck.sh`, das:  
1. Eine Variable `farbe="blau"` anlegt.  
2. Mit einer `if`-Abfrage prüft, ob die Variable den Wert `"blau"` hat.  
3. Gibt „Lieblingsfarbe erkannt“ aus, wenn die Bedingung erfüllt ist.  
4. Probiere auch andere Werte für die Variable aus, z. B. `5` oder `"Blau"` (mit großem Anfangsbuchstaben), und beobachte, wie sich das Verhalten ändert.  
5. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 4. Weiterführende Aufgabe – Zwei Zahlen vergleichen

**Deine Aufgabe:**  
Erstelle ein Skript `abfrage.sh`, das:  
1. Den Benutzer mit `read` nach zwei Zahlen fragt (zuerst Zahl 1, dann Zahl 2).  
2. Mit `if`-, `elif`- und `else`-Abfragen prüft:  
   - ob die erste Zahl kleiner ist als die zweite  
   - ob beide Zahlen gleich sind  
   - oder ob die erste Zahl größer ist  
3. Gibt die entsprechende Ausgabe mit `echo` aus.  
4. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 5. Bonusaufgabe – Case-Struktur

**Deine Aufgabe:**  
Schreibe ein Skript `wochentag.sh`, das:  
1. Den Benutzer nach einem Wochentag fragt (z. B. „Mo“, „Di“, „Mi“).  
2. Mit einer `case`-Struktur je nach Eingabe einen Text ausgibt, z. B.:  
   - „Mo“ → „Wochenstart!“  
   - „Fr“ → „Fast Wochenende!“  
   - alles andere → „Weiter geht’s!“  
3. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.  

**Hinweis:**  
Die Case-Struktur wurde noch nicht so intensiv geübt. Recherchiere bei Bedarf selbstständig.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  
