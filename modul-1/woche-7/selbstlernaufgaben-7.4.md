# Selbstlernaufgaben – Bash für Systemadministration

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.  

---

## 1. Grundlagenaufgabe - Kommandozeilenparameter

**Deine Aufgabe:**  
Schreibe ein Skript `multiply.sh`, das:  
1. Zwei Zahlen **als Kommandozeilenparameter** entgegennimmt (z. B. `./multiply.sh 6 7`).  
2. Das Produkt mit `echo` ausgibt (z. B. `Das Ergebnis ist: 42`).  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 2. Grundlagenaufgabe - Umgebungsvariable & `export`

**Deine Aufgabe:**  
Erstelle zwei Skripte `parent.sh` und `child.sh`, die zeigen, wie `export` wirkt:  
1. `parent.sh` setzt `GREETING="Hello"` und **exportiert** die Variable.  
2. `parent.sh` startet `child.sh`, welches `echo "$GREETING $1!"` ausgibt (Name kommt als Parameter).  
3. Führe `./parent.sh Alice` aus und prüfe, ob die Ausgabe aus `child.sh` stimmt.

**Formatvorschläge**  
- Zwei `.sh`-Dateien  
- Kurzbeschreibung (Text)  

---

## 3. Grundlagenaufgabe - Arrays

**Deine Aufgabe:**  
Schreibe ein Skript `farben_array.sh`, das:  
1. Ein Array `farben=("rot" "gruen" "blau" "gelb")` anlegt.  
2. Die **Länge** des Arrays ausgibt (`${#farben[@]}`).  
3. Alle Elemente in der Form `Farbe X: <Wert>` ausgibt (Index-Schleife über `"${!farben[@]}"`).  
4. Ein neues Element **anhängt** (`farben+=("lila")`) und anschließend **erneut** Länge + alle Elemente ausgibt.

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 4. Weiterführende Aufgabe – `grep` + Wortgrenzen

**Deine Aufgabe:**  
Lege eine Datei `story.txt` an (beliebiger Text) und schreibe ein Skript `count_word.sh`, das:  
1. Ein **Wort** und eine **Datei** als Parameter erwartet (z. B. `./count_word.sh Blatt story.txt`).  
2. Mit **Wortgrenzen** zählt, wie oft das **exakte Wort** vorkommt.  
3. Zusätzlich die Zeilen, in denen das Wort vorkommt, in einer **resultat.txt** abspeichert.

**Formatvorschläge**  
- `.sh`-Datei  
- `story.txt`  
- Kurze Readme  

---

## 5. Bonusaufgabe (schwer) – Eingaben sammeln bis `stop` (Arrays & Schleife)

**Deine Aufgabe:**  
Schreibe ein Skript `liste_array.sh`, das:  
1. Ein **leeres Array** anlegt.  
2. Den Nutzer in einer Schleife mit `read -p` nach Einträgen fragt und jeden Eintrag ins Array schreibt.  
3. Die Schleife endet, wenn der Nutzer **`stop`** eingibt (dieser Wert wird **nicht** gespeichert).  
4. Am Ende die **Anzahl der Elemente** (`${#arr[@]}`) und alle Inhalte in der Form  
   `Das X. Element: <Wert>` ausgibt (Iteration über `"${!arr[@]}"`).  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  
