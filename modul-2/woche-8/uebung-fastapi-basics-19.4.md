## 1. Grundlagen: Pydantic und Schemadefinition

Schwierigkeitsgrad: **Grundlegend** 

Dauer: **~15 Minuten**

Aufgabenstellung: Beantworte die folgenden Fragen zur Rolle und Struktur von Pydantic-Modellen in FastAPI.

1. FastAPI nutzt die Bibliothek **Pydantic**. Welchen Hauptzweck erfüllt Pydantic für die Daten, die du von einem Client **empfängst** (Request Body)?
    
2. Was ist ein **Pydantic BaseModel**? Beschreibe kurz, wie du ein solches Modell in deinem Code definierst (Schlüsselwort und von welcher Klasse es erben muss).
    
3. Pydantic erzwingt die Datentypen, die du mit Python **Type Hints** festlegst. Welchen **HTTP-Statuscode** sendet FastAPI automatisch an den Client zurück, wenn die gesendeten Daten nicht dem definierten Schema entsprechen (z.B. ein fehlendes Feld)?
    
4. Nenne zwei konkrete Feldtypen (z.B. String) und die zugehörigen Python Type Hints, die du in einem Pydantic-Modell verwenden kannst.
    

---

## 2. Pydantic-Modell als Response-Schema (GET)

Schwierigkeitsgrad: **Mittel** 

Dauer: **~20 Minuten**

Aufgabenstellung: Definiere ein Pydantic-Modell für einen Kunden und nutze es, um die Antwort (Output) eines GET-Endpunktes zu strukturieren.

1. Definiere ein Pydantic-Modell mit dem Namen **`Kunde`**, das folgende Felder enthält: `id` (`int`), `name` (`str`) und `ist_premium` (`bool`).
    
2. Definiere einen **GET-Endpunkt** für den Pfad **`/profil`**.
    
3. Die Funktion des Endpunkts soll ein **neues Objekt des `Kunde`-Modells** mit Beispieldaten erstellen und zurückgeben. Schreibe den Code-Ausschnitt, der zeigt, wie das Objekt erstellt wird (z.B. `Kunde(...)`).
    
4. Erkläre, wie FastAPI das definierte Modell **`Kunde`** nutzt, um die **Ausgabe** (Response) an den Client zu validieren, bevor sie als JSON gesendet wird.
    

---

## 3. POST-Endpunkt und Request-Body (Eingabevalidierung)

Schwierigkeitsgrad: **Mittel** 

Dauer: **~30 Minuten**

Aufgabenstellung: Schreibe einen **POST**-Endpunkt, der ein Pydantic-Modell als Eingabe (Request Body) erwartet und dieses verarbeitet.

1. Definiere ein Pydantic-Modell mit dem Namen **`Produkt`**, das die Felder `titel` (`str`) und `lagerbestand` (`int`) enthält.
    
2. Definiere einen **POST-Endpunkt** für den Pfad **`/lager/verbuchen`**.
    
3. Die Funktion dieses Endpunkts soll das erstellte **`Produkt`-Modell** als Parameter entgegennehmen. Schreibe den Code-Ausschnitt des **Funktions-Headers** (z.B. `def inventar_verbuchen(...)`) und nutze den korrekten Python Type Hint für die Übergabe.
    
4. Die Funktion soll das **empfangene `Produkt`-Objekt** zurückgeben, um die erfolgreiche Verarbeitung zu bestätigen. Welchen **HTTP-Statuscode** sollte ein POST-Endpunkt für eine erfolgreiche **Neuanlage** idealerweise zurückgeben?
    

---

## 4. Testen des POST-Endpunktes in der UI

Schwierigkeitsgrad: **Mittel** 

Dauer: **~20 Minuten**

Aufgabenstellung: Beschreibe, wie du den in Aufgabe 3 erstellten POST-Endpunkt in der interaktiven Dokumentation testest und was dabei die Schlüsselrolle spielt.

1. Welche URL musst du im Browser aufrufen, um die interaktive Dokumentation deiner laufenden FastAPI-Anwendung zu sehen?
    
2. Wenn du den POST-Endpunkt **`/lager/verbuchen`** in der Dokumentation auswählst, wird automatisch ein **Schema** für den Request Body angezeigt. Basierend auf welchem Element in deinem Python-Code wird dieses Schema generiert?
    
3. Welchen **Button** musst du in der Dokumentation drücken, um das Test-Formular zu öffnen und die Eingabefelder für `titel` und `lagerbestand` zu sehen?
    
4. Beschreibe, was in der Dokumentation passiert, wenn du für das Feld `lagerbestand` absichtlich einen **String** (z.B. `"zwanzig"`) statt einer Ganzzahl eingibst und den Test ausführst. Welchen Statuscode erhältst du dann?
    

---

## 5. Fortgeschritten: Modell-Validierung und Status-Rückgabe

Schwierigkeitsgrad: **Fortgeschritten** 

Dauer: **~20 Minuten**

Aufgabenstellung: Implementiere eine erweiterte Validierungslogik und setze spezifische HTTP-Statuscodes über das Decorator-Argument.

1. Definiere zwei Pydantic-Modelle: **`Lieferung`** (Input: `gewicht_kg` (`float`)) und **`Rückmeldung`** (Output: `status` (`str`), `detail` (`str`)).
    
2. Erstelle einen **POST-Endpunkt** für den Pfad **`/lieferung/anmelden`**. Die Funktion soll das `Lieferung`-Modell als Eingabe verwenden und das `Rückmeldung`-Modell als Ausgabe (Response Model) definieren.
    
3. Implementiere eine Logik: Wenn das `gewicht_kg` **größer als 500** ist, soll die Funktion ein **`Rückmeldung`-Objekt** zurückgeben, das den Fehler beschreibt (`status="FEHLER"`). Setze in der Endpunkt-Deklaration (Decorator) für diesen Endpunkt den **Statuscode 400** (Bad Request) für Fehlerfälle.
    
4. Wenn das `gewicht_kg` **kleiner oder gleich 500** ist, soll die Funktion ebenfalls ein **`Rückmeldung`-Objekt** zurückgeben (`status="ERFOLG"`). Setze den **Statuscode 201** (Created) in der Endpunkt-Deklaration. Schreibe den Code-Ausschnitt des **Decorators** und der **Funktion** (mit Logik), der zeigt, wie du die Statuscodes bedingt im Decorator festlegst oder überschreibst. (Hinweis: Du kannst den `status_code` Parameter im `@app.post` Decorator nutzen, um den Erfolgscode 201 zu setzen und für den Fehlerfall den Statuscode 400 im Code zu behandeln, indem du das `Response` Objekt importierst und nutzt).
