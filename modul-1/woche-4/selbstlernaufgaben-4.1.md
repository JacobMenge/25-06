# Selbstlernaufgaben - Bedingungen ohne Code

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Einfache Bedingung

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy sein Kostüm wechselt, wenn er den Rand der Bühne berührt.

**Programmverhalten:**
Scratchy soll sich kontinuierlich bewegen. Wenn er den Rand berührt, soll er abprallen und sein Kostüm zum nächsten wechseln.

**Programmlogik:**
```
beim Start:
  wiederhole fortlaufend:
    gehe 3 er-Schritt
    
    falls wird Rand berührt:
      pralle vom Rand ab
      nächstes Kostüm
```

**Formatvorschläge**
- .sb3-Datei

---

## 2. Grundlagenaufgabe - Einfache If-Bedingung

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy reagiert, wenn die Leertaste gedrückt wird.

**Programmverhalten:**
Das Programm soll kontinuierlich prüfen, ob die Leertaste gedrückt wird. Falls ja, soll Scratchy "Hallo!" sagen.

**Programmlogik:**
```
wiederhole fortlaufend:
  falls Leertaste gedrückt:
    sage "Hallo!"
```

**Formatvorschläge**
- .sb3-Datei

---

## 3. Grundlagenaufgabe - If-Else-Bedingung

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, in dem Scratchy unterschiedlich reagiert, je nachdem ob die Maus geklickt wird oder nicht.

**Programmverhalten:**
Das Programm soll kontinuierlich prüfen, ob die Maustaste gedrückt ist. Je nach Zustand soll Scratchy verschiedene Nachrichten anzeigen.

**Programmlogik:**
```
wiederhole fortlaufend:
  falls Maustaste gedrückt:
    sage "Maus geklickt!"
  sonst:
    sage "Warte auf Klick..."
  warte 0.5 Sekunden
```

**Formatvorschläge**
- .sb3-Datei

---

## 4. Weiterführende Selbstlernaufgabe - Bedingung mit Operatoren

**Deine Aufgabe:**

Erstelle in Scratch ein Programm, das prüft, ob eine Zufallszahl größer als 50 ist.

**Programmverhalten:**
Das Programm soll eine Zufallszahl zwischen 1 und 100 erzeugen und dann prüfen, ob diese größer als 50 ist. Je nach Ergebnis soll eine entsprechende Nachricht angezeigt werden, die auch die Zahl enthält.

**Programmlogik:**
```
Variable: Meine_Zahl

beim Start:
  setze Meine_Zahl auf Zufallszahl von 1 bis 100
  
  falls Meine_Zahl > 50:
    sage "Die Zahl " + Meine_Zahl + " ist groß!"
  sonst:
    sage "Die Zahl " + Meine_Zahl + " ist klein!"
```

**Zusatzfrage:**
Wie würdest du das Programm ändern, um drei Kategorien zu haben: "klein" (unter 33), "mittel" (33-66) und "groß" (über 66)?

**Formatvorschläge**
- .sb3-Datei

---

## 5. Bonus Selbstlernaufgabe - Bedingung mit Eingabe

**Deine Aufgabe:**

Diese Aufgabe ist herausfordernd und nur als Bonus gedacht.

Erstelle in Scratch ein einfaches Altersüberprüfungs-Programm.

**Programmverhalten:**
Das Programm fragt nach dem Alter und gibt unterschiedliche Nachrichten aus, je nachdem ob die Person unter 12, zwischen 12 und 17, oder 18 und älter ist.

**Programmlogik:**
```
Variable: Alter

beim Start:
  setze Alter auf frage "Wie alt bist du?" und warte
  
  falls Alter < 12:
    sage "Du bist ein Kind!"
  sonst:
    falls Alter < 18:
      sage "Du bist ein Jugendlicher!"
    sonst:
      sage "Du bist erwachsen!"
```

**Hinweis:**
Du brauchst verschachtelte falls-sonst-Bedingungen für die drei verschiedenen Altersgruppen.

**Formatvorschläge**
- .sb3-Datei