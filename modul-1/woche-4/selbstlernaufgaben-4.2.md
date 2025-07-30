# Selbstlernaufgaben - Schleifen

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Einfache For-Schleife

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy 4-mal vorwärts geht und dabei ein Quadrat läuft.

**Programmverhalten:**
Scratchy soll sich 4-mal bewegen und nach jedem Schritt um 90 Grad drehen, sodass ein Quadrat entsteht. Nach dem Quadrat soll er "Quadrat fertig!" sagen.

**Programmlogik:**
```
beim Start:
  wiederhole 4 mal:
    gehe 100 er-Schritt
    drehe dich um 90 Grad
    
  sage "Quadrat fertig!" für 2 Sekunden
```

**Formatvorschläge**
- .sb3-Datei

---


## 2. Grundlagenaufgabe - While-Schleife

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy sich dreht bis die Leertaste gedrückt wird.

**Programmverhalten:**
Scratchy soll sich kontinuierlich im Kreis drehen. Sobald die Leertaste gedrückt wird, soll er aufhören und "Stopp!" sagen.

**Programmlogik:**
```
beim Start:
  wiederhole bis Leertaste gedrückt:
    drehe dich um 10 Grad
    warte 0.1 Sekunden
    
  sage "Stopp!" für 2 Sekunden
```

**Formatvorschläge**
- .sb3-Datei

---

## 3. Grundlagenaufgabe - Schleife mit Variable

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy von 1 bis 5 zählt und dabei immer größere Schritte macht.

**Programmverhalten:**
Scratchy soll 5-mal vorwärts gehen. Bei jedem Schritt soll er die aktuelle Zahl sagen und so viele Schritte gehen, wie die Zahl groß ist (1. Durchlauf: 1 Schritt, 2. Durchlauf: 2 Schritte, usw.).

**Programmlogik:**
```
Variable: Schrittanzahl

beim Start:
  setze Schrittanzahl auf 1
  
  wiederhole 5 mal:
    sage Schrittanzahl für 1 Sekunde
    gehe Schrittanzahl * 20 er-Schritt
    ändere Schrittanzahl um 1
    warte 0.5 Sekunden
```

**Formatvorschläge**
- .sb3-Datei

---

## 4. Weiterführende Selbstlernaufgabe - Verschachtelte Schleifen

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy 3 verschiedene Dreiecke zeichnet.

**Programmverhalten:**
Scratchy soll 3-mal ein Dreieck zeichnen. Nach jedem Dreieck soll er seine Position wechseln (z.B. zur Mitte gehen) und das nächste Dreieck zeichnen.

**Programmlogik:**
```
beim Start:
  wiederhole 3 mal:
    // Ein Dreieck zeichnen
    wiederhole 3 mal:
      gehe 80 er-Schritt
      drehe dich um 120 Grad
      
    // Position für nächstes Dreieck wechseln
    gehe zu x: 0 y: 0
    drehe dich um 45 Grad
    warte 1 Sekunde
    
  sage "3 Dreiecke fertig!"
```

**Hinweis:**
Den "gehe zu x: y:"-Block findest du in der Kategorie "Bewegung".

**Formatvorschläge**
- .sb3-Datei

---

## 5. Bonus Selbstlernaufgabe - Schleifen + Bedingungen + Variablen

**Deine Aufgabe:**

Erstelle in Scratch ein Zahlenspiel: Scratchy soll von 1 bis 10 zählen, aber nur die geraden Zahlen laut sagen.

**Programmverhalten:**
Scratchy soll von 1 bis 10 zählen. Bei geraden Zahlen (2, 4, 6, 8, 10) soll er die Zahl laut sagen und einen Schritt vorwärts gehen. Bei ungeraden Zahlen soll er nur einen halben Schritt gehen ohne etwas zu sagen. Am Ende soll er sagen, wie viele gerade Zahlen er gefunden hat.

**Programmlogik:**
```
Variablen: Zähler, Gerade_Zahlen

beim Start:
  setze Zähler auf 1
  setze Gerade_Zahlen auf 0
  
  wiederhole bis Zähler > 10:
    falls Zähler mod 2 = 0:  // gerade Zahl
      sage Zähler für 1 Sekunde
      gehe 30 er-Schritt
      ändere Gerade_Zahlen um 1
    sonst:  // ungerade Zahl
      gehe 15 er-Schritt
      
    ändere Zähler um 1
    warte 0.5 Sekunden
    
  sage "Ich habe " + Gerade_Zahlen + " gerade Zahlen gefunden!"
```

**Hinweis:**
Der "mod"-Operator gibt den Rest einer Division zurück. Eine Zahl ist gerade, wenn sie durch 2 teilbar ist (Rest = 0). Den "mod"-Block findest du in der Kategorie "Operatoren".

**Formatvorschläge**
- .sb3-Datei


## 6. Experten Bonus Selbstlernaufgabe - Komplexe verschachtelte Schleifen

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, dass ein 4x4 Gitter aus verschiedenen Formen zeichnet. In jeder Reihe soll eine andere Form gezeichnet werden (Reihe 1: Quadrate, Reihe 2: Dreiecke, Reihe 3: Sechsecke, Reihe 4: Kreise mit Stempel).

**Programmverhalten:**
Das Programm soll ein 4x4 Gitter erstellen. Jede der 4 Reihen soll eine andere geometrische Form enthalten. Die Formen sollen an den richtigen Positionen gezeichnet werden. Am Ende soll gezählt werden, wie viele Formen insgesamt gezeichnet wurden.

**Programmlogik:**
```
Variablen: Reihe, Spalte, Formen_Gesamt, Start_X, Start_Y

beim Start:
  setze Formen_Gesamt auf 0
  setze Start_X auf -150
  setze Start_Y auf 120
  setze Reihe auf 1
  
  wiederhole 4 mal:  // 4 Reihen
    setze Spalte auf 1
    
    wiederhole 4 mal:  // 4 Spalten pro Reihe
      // Position berechnen
      gehe zu x: (Start_X + (Spalte * 80)) y: (Start_Y - (Reihe * 80))
      
      // Form je nach Reihe zeichnen
      falls Reihe = 1:  // Quadrate
        wiederhole 4 mal:
          gehe 40 er-Schritt
          drehe dich um 90 Grad
          
      falls Reihe = 2:  // Dreiecke
        wiederhole 3 mal:
          gehe 40 er-Schritt
          drehe dich um 120 Grad
          
      falls Reihe = 3:  // Sechsecke
        wiederhole 6 mal:
          gehe 25 er-Schritt
          drehe dich um 60 Grad
          
      falls Reihe = 4:  // Kreise (mit Stempel)
        setze Größe auf 50%
        stempel ab
        setze Größe auf 100%
      
      ändere Formen_Gesamt um 1
      ändere Spalte um 1
      warte 0.2 Sekunden
      
    ändere Reihe um 1
    
  gehe zu x: 0 y: -150
  sage "Gitter fertig! " + Formen_Gesamt + " Formen gezeichnet!" für 3 Sekunden
```

**Hinweise:**
- Du brauchst drei verschachtelte Strukturen: Reihen-Schleife, Spalten-Schleife, und Form-Schleifen
- Die Position wird für jede Form neu berechnet
- Jede Reihe hat eine andere Form mit unterschiedlichen Wiederholungen
- Den "gehe zu x: y:"-Block findest du in der Kategorie "Bewegung"
- Den "stempel ab"-Block findest du in der Kategorie "Malstift"
- Den "setze Größe auf"-Block findest du in der Kategorie "Aussehen"
- Vergiss nicht den Malstift einzuschalten für die gezeichneten Formen!

**Formatvorschläge**
- .sb3-Datei

---
