# Selbstlernaufgaben – Bash For-/While-Schleifen & Bedingungen II

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.  

---

## 1. Grundlagenaufgabe – Gerade oder ungerade  

**Deine Aufgabe:**  
Schreibe ein Skript `gerade_ungerade.sh`, das:  
1. Mit einer For-Schleife die Zahlen von 1 bis 10 durchläuft.  
2. Zu jeder Zahl prüft, ob sie **gerade** oder **ungerade** ist.  
3. Bei geraden Zahlen `X ist gerade` und bei ungeraden `X ist ungerade` ausgibt.  

**Hinweise:**  
- Eine Zahl ist gerade, wenn sie durch 2 teilbar ist (Rest = 0).  
- Überprüfen kannst du das mit dem Modulo-Operator `%`.  
- Beispiel: `7 % 2` ergibt 1 → ungerade.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 2. Grundlagenaufgabe – Eingaben mit While-Schleife prüfen  

**Deine Aufgabe:**  
Erstelle ein Skript `eingaben_check.sh`, das:  
1. Den Benutzer wiederholt nach einer Zahl fragt.  
2. Mit einer if-Abfrage prüft, ob die Zahl größer als 10 ist.  
3. Rückmeldungen gibt:  
   - „größer als 10“  
   - „10 oder kleiner“  
4. Beendet wird, wenn der Benutzer `q` eingibt.  

**Hinweise:**  
- Denke daran, dass Eingaben mit `read` eingelesen werden.  
- Vergiss nicht, die Bedingung für das Beenden abzufangen.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 3. Weiterführende Aufgabe – Multiplikationstabelle  

**Deine Aufgabe:**  
Schreibe ein Skript `multiplikation.sh`, das:  
1. Den Benutzer nach einer Zahl fragt (z. B. im Bereich 1–10).  
2. Mit einer For-Schleife die Multiplikationstabelle für diese Zahl von 1 bis 10 ausgibt.  
3. Mit einer if-Abfrage prüft, ob das Produkt genau durch 5 teilbar ist. Wenn ja, soll hinter der Ausgabe ein `*` erscheinen.  

**Beispiel (für Eingabe 3):**  
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15*
...
```  

**Hinweise:**  
- Berechne das Produkt mit `p=$(( ... ))`.  
- Prüfe mit `%`, ob eine Zahl genau durch 5 teilbar ist.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 4. Weiterführende Aufgabe – Passwortprüfung  

**Deine Aufgabe:**  
Erstelle ein Skript `passwort_check.sh`, das:  
1. Den Benutzer bis zu 3-mal nach einem Passwort fragt.  
2. Mit if-Abfragen prüft:  
   - Passwort hat mindestens 8 Zeichen  
   - Passwort enthält mindestens eine Zahl  
3. Wenn das Passwort gültig ist: Erfolgsmeldung und Ende.  
4. Wenn nach 3 Fehlversuchen kein gültiges Passwort eingegeben wurde: Fehlermeldung und Ende.  

**Hinweise:**  
- Die Länge eines Strings kannst du mit `${#pw}` herausfinden.  
- Einfache Prüfungen wie „enthält Zahl“ lassen sich mit `[[ "$pw" =~ [0-9] ]]` umsetzen.  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  

---

## 5. Bonusaufgabe (schwer) – Array verwalten  

**Deine Aufgabe:**  
Schreibe ein Skript `array_manager.sh`, das:  
1. Ein **leeres Array** anlegt.  
2. In einer While-Schleife Eingaben vom Benutzer entgegennimmt:  
   - `add <Text>` → fügt einen Wert ins Array ein  
   - `list` → gibt alle Werte mit Index aus  
   - `q` → beendet das Skript  
3. Nach jeder Eingabe (außer `q`) soll das gesamte Array ausgegeben werden.  

**Hinweis (nur als Schnipsel):**  
So kannst du ein Array mit einer For-Schleife durchlaufen:  
```bash
for (( i=0; i<${#arr[@]}; i++ )); do
  echo "Index $i: ${arr[$i]}"
done
```  

**Formatvorschläge**  
- `.sh`-Datei  
- Textdatei  


