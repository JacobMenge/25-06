## 1. Der erste statische GET-Endpunkt

Schwierigkeitsgrad: **Grundlegend** 

Dauer: **~20 Minuten**

Aufgabenstellung: Schreibe den minimalen Code, um eine FastAPI-Anwendung zu erstellen und einen einfachen, statischen Endpunkt zu definieren.

1. Erstelle eine Python-Datei (z.B. `server.py`). Schreibe den Code, um die `FastAPI`-Klasse zu importieren und die Hauptanwendungsinstanz zu initialisieren .
    
2. Definiere einen **GET-Endpunkt** für den Pfad **`/status`**.
    
3. Die Funktion unter dem Endpunkt soll ein **Python Dictionary** zurückgeben, das den Schlüssel `"service"` und den Wert `"aktiv"` enthält.
    
4. Wenn der Endpunkt im Browser aufgerufen wird, in welches Datenformat wird das Python Dictionary automatisch konvertiert, bevor es angezeigt wird?
    

---

## 2. Path Operation Decorator und Datenrückgabe

Schwierigkeitsgrad: **Mittel** 

Dauer: **~25 Minuten**

Aufgabenstellung: Erkläre die Funktion des Decorators und demonstriere die Rückgabe einer komplexeren Datenstruktur (Liste von Objekten).

1. Was genau ist der **Path Operation Decorator** (z.B. `@app.get("/artikel")`) und welche **zwei** wesentlichen Informationen legst du damit für den Server fest?

    
2. Definiere einen neuen GET-Endpunkt für den Pfad **`/mitarbeiter`**. Die Funktion darunter soll eine **Liste** zurückgeben, die zwei Python-Dictionaries mit den Schlüsseln `"id"` und `"abteilung"` enthält (z.B. `[{"id": 101, "abteilung": "Vertrieb"}, {"id": 102, "abteilung": "IT"}]`).
    
3. Wenn der Endpunkt erfolgreich aufgerufen wird, welchen Standard-HTTP-Statuscode sendet FastAPI als Antwort zurück?
    

---

## 3. Interaktive Dokumentation und API-Test

Schwierigkeitsgrad: **Mittel** 

Dauer: **~30 Minuten**

Aufgabenstellung: Nutze die automatisch generierte Dokumentation, um deinen Service zu testen und seine Vorteile zu verstehen.

1. Welche URL musst du im Browser aufrufen, um die interaktive Dokumentation deiner laufenden FastAPI-Anwendung zu sehen?
    
2. Wie wird die Benutzeroberfläche der interaktiven Dokumentation genannt, die FastAPI automatisch generiert?
    
3. Erkläre in eigenen Worten, warum diese automatische Dokumentation für andere Entwickler, die deine API nutzen wollen, so nützlich ist.
    
4. Beschreibe die **drei Schritte** (Button-Klicks), die du in der interaktiven Dokumentation ausführen musst, um einen statischen GET-Endpunkt (wie z.B. `/status` aus Aufgabe 1) direkt in der UI zu testen.
    

---

## 4. GET-Endpunkt mit Pfad-Parametern und Typisierung

Schwierigkeitsgrad: **Fortgeschritten** 

Dauer: **~30 Minuten**

Aufgabenstellung: Definiere einen Endpunkt, der dynamische Daten über den Pfad entgegennimmt, und erzwinge den Datentyp zur Validierung.

1. Definiere in deiner `server.py` einen neuen GET-Endpunkt, der eine **Warennummer** entgegennimmt. Der Pfad soll so aussehen: **`/waren/{waren_nr}`**.
    
2. Die Funktion unter diesem Decorator soll den Parameter `waren_nr` als **Gleitkommazahl** (`float`) erwarten. **Schreibe den Code-Ausschnitt des Funktions-Headers** mit dem passenden Python **Type Hint**.
    
3. Lasse die Funktion ein Dictionary zurückgeben, das die empfangene `waren_nr` und den Text `"Warennummer empfangen: [Nummer]"` enthält.
    
4. Was passiert automatisch (welche Fehlerbehandlung greift), wenn du versuchst, diesen Endpunkt mit einem **String** (z.B. `http://127.0.0.1:8000/waren/keine-zahl`) aufzurufen, obwohl der Parameter als `float` deklariert ist? Welchen HTTP-Statuscode würdest du in diesem Fehlerfall erwarten?
