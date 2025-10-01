# Selbstlernübung – Linux Texte & Streams


---

## 1. Grundlagenübung – Reguläre Ausdrücke testen (mit „1000 Wörter“)  

**Deine Aufgabe:**  
1. Kopiere den Text von **„1000 Wörter“** in eine Datei `story.txt`.  
2. Suche mit `grep` alle Zeilen, die mit „Sie“ beginnen.  
3. Suche mit `grep` alle Zeilen, die auf einem Ausrufezeichen enden.  
4. Suche mit `grep` alle Zeilen, die mindestens einmal die Buchstabenfolge „ab“ enthalten.  


---

## 2. Grundlagenaufgabe – Zeichenklassen nutzen (mit „1000 Wörter“)  

**Deine Aufgabe:**  
1. Verwende dieselbe Datei `story.txt` aus Aufgabe 1.  
2. Finde mit `grep` alle Wörter, die mit einem Großbuchstaben „M“ oder „S“ beginnen.  
3. Finde mit `grep` alle Wörter, die auf „er“ enden.   


---

## 3. Grundlagenübung – Pipes anwenden  

**Deine Aufgabe:**  
Alle folgenden Schritte sollen in **einer einzigen Zeile Code mit Pipes** erledigt werden.  

1. Verwende `cat /etc/passwd`, um den Inhalt der Datei anzuzeigen.  
2. Filtere die Ausgabe mit grep so, dass nur Zeilen mit dem Wort „bin“ erscheinen.  
3. Zähle, wie viele Treffer es gibt. (**Hinweis:** nutze dazu `wc -l`)  
 

---

## 4. Weiterführende Übnung – Endliche Automaten entwerfen  

**Deine Aufgabe:**  
Entwirf jeweils einen endlichen Automaten (als Skizze oder Zustandsdiagramm) für die folgenden regulären Ausdrücke und füge einen kurzen Erklärungssatz hinzu:  

1. `hallo`  
   → Erkennt genau das Wort „hallo“ in dieser Reihenfolge.  

2. `cat|dog`  
   → Erkennt entweder das Wort „cat“ oder das Wort „dog“.  

3. `a+b`  
   → Erkennt eine oder mehrere Wiederholungen von „a“, gefolgt von genau einem „b“.  
 

---

## 5. Bonusübung (schwer) – Weitere Automaten  

**Deine Aufgabe:**  
Entwirf jeweils einen endlichen Automaten (als Skizze oder Zustandsdiagramm) für die folgenden regulären Ausdrücke und füge einen kurzen Erklärungssatz hinzu:  

1. `(ha){2,}[!?]`  
   → Erkennt mindestens zweimal „ha“ hintereinander, gefolgt von genau einem der Zeichen „!“ oder „?“.  

2. `(0|1){8}`  
   → Erkennt exakt achtstellige Folgen aus Nullen und Einsen.  

3. `[a-z]{3,}@(gmail|outlook|yahoo)\.com`  
   → Erkennt einfache E-Mail-Adressen mit mindestens drei Kleinbuchstaben vor dem @ und einer der drei Domains.  



