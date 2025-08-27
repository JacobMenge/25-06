# Selbstlernaufgaben – Bash For-/While-Schleifen & Bedingungen

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.  

---

## 1. Grundlagenaufgabe – For-Schleife über Zahlen

**Deine Aufgabe:**  
Schreibe ein Skript `zahlen_for.sh`, das:  
1. Mit einer For-Schleife über die Zahlen von 1 bis 10 iteriert.  
2. In jeder Runde den aktuellen Wert mit `echo` ausgibt.  
3. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 2. Grundlagenaufgabe – For-Schleife über Wörter

**Deine Aufgabe:**  
Erstelle ein Skript `fruechte_for.sh`, das:  
1. Eine Liste von drei Früchten direkt in die For-Schleife schreibt, z. B. Apfel, Birne, Kiwi.  
2. Jede Frucht mit einem kurzen Satz ausgibt, z. B. „Ich mag Apfel“.  
3. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 3. Weiterführende Aufgabe – While-Schleife mit Zähler

**Deine Aufgabe:**  
Schreibe ein Skript `zaehler_while.sh`, das:  
1. Einen Zähler bei 0 starten lässt.  
2. So lange läuft, bis der Zähler den Wert 5 erreicht hat.  
3. In jeder Runde den aktuellen Stand anzeigt und den Zähler erhöht.  
4. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 4. Weiterführende Aufgabe – Eingaben wiederholen

**Deine Aufgabe:**  
Erstelle ein Skript `eingaben_loop.sh`, das:  
1. Den Benutzer wiederholt nach einer Eingabe fragt.  
2. Solange weiterläuft, bis der Benutzer ein bestimmtes Wort eingibt (z. B. „ende“).  
3. Jede Eingabe mit einer passenden Rückmeldung ausgibt.  
4. Passe mit `chmod` die Rechte an und führe das Skript mindestens einmal aus.

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 5. Bonusaufgabe (schwer) – Zahlenraten-Spiel

**Deine Aufgabe:**  
Schreibe ein Skript `zahlenraten.sh`, das:  
1. Eine zufällige Zahl zwischen 1 und 50 erzeugt, z. B. mit:  
   ```bash
   ziel=$((RANDOM % 50 + 1))
   ```
   $RANDOM ist eine eingebaute Bash-Variable, die eine zufällige Zahl liefert.
   Mit dem Modulo-Operator % kannst du den Wertebereich begrenzen, hier auf 0–49. Durch +1 entsteht der Bereich 1–50.
2. Den Benutzer wiederholt nach einer Zahl fragt.
3. Rückmeldungen gibt, ob die Eingabe zu klein, zu groß oder genau richtig ist.
4. Das Spiel endet, wenn die richtige Zahl erraten wurde oder die maximale Anzahl an Versuchen erreicht ist.
5. Passe mit chmod die Rechte an und führe das Skript mindestens einmal aus.

**Formatvorschläge**
- `.sh`-Datei
- Textdatei



