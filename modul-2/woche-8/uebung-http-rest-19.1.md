# HTTP und REST
​
## Übersicht
​
In dieser Übung lernst du die grundlegenden Konzepte des Hypertext Transfer Protocols (HTTP), die wichtigsten HTTP-Methoden und deren Eigenschaften, die Bedeutung von HTTP-Statuscodes sowie die Struktur und Anwendung des JSON-Datenformats kennen.
​
---
​
## Übung 1: Grundlagen HTTP
​
Schwierigkeitsgrad: Grundlegend  
Dauer: ~5 Minuten

​
**Aufgabenstellung:** Beantworte die folgenden Fragen zu HTTP:
​
1. Wofür steht die Abkürzung HTTP? 
2. Was ist der Hauptzweck von HTTP im World Wide Web? 
3. Beschreiben Sie kurz das Client-Server-Prinzip, auf dem HTTP basiert. 
4. Was ist der Unterschied zwischen HTTP und HTTPS? 
​
## Übung 2: HTTP-Methoden und deren Zweck
​
Schwierigkeitsgrad: Grundlegend  
Dauer: ~5 Minuten
​

**Aufgabenstellung:** Ordne jeder HTTP-Methode den korrekten Hauptzweck (Lesen, Erstellen, Aktualisieren, Löschen) zu und geben Sie die deutsche Übersetzung der Methode an.
​
1. **GET**
    - Zweck: 
    - Deutsche Übersetzung: 
2. **POST**
    - Zweck: 
    - Deutsche Übersetzung: 
3. **PUT**
    - Zweck: 
    - Deutsche Übersetzung: 
4. **DELETE**
    - Zweck: 
    - Deutsche Übersetzung: 
        
​
## Übung 3: HTTP-Statuscodes zuordnen
​
Schwierigkeitsgrad: Grundlegend  
Dauer: ~5 Minuten
​

**Aufgabenstellung:** Ordne die folgenden HTTP-Statuscodes der entsprechenden Code-Klasse (1xx, 2xx, 3xx, 4xx oder 5xx) zu und gib ein Beispiel an in welcher Situation dieser Code auftreten kann.
​
| **Statuscode**                | **Bedeutung der Code-Klasse** | **Wann kann dieser Statsucode auftreten?** |
| ----------------------------- | --------------- | ----------------------------------------- |
| **200 OK**                    |                 |                                           |
| **404 Not Found**             |                 |                                           |
| **500 Internal Server Error** |                 |                                           |
| **201 Created**               |                 |                                           |
| **400 Bad Request**           |                 |                                           |
​
---
​
## Übung 4: JSON-Objekte erstellen
​
Schwierigkeitsgrad: Mittel  
Dauer: ~10 Minuten
​

**Aufgabenstellung:** Erstelle ein gültiges JSON-Objekt, das Informationen über ein Buch speichert.
​
1. Das JSON-Objekt muss mindestens die folgenden Schlüssel-Wert-Paare enthalten:
    - `titel` (String)
    - `autor` (String)
    - `isbn` (String, als Schlüssel)
    - `erscheinungsjahr` (Zahl, als Schlüssel)
2. Das Objekt soll außerdem einen Schlüssel namens `genres` enthalten, dessen Wert ein JSON-Array mit mindestens zwei Genre-Strings ist. 23
3. Stellen Sie sicher, dass alle Schlüssel **Strings** sind. 24
    
​
---
​
## Übung 5: PUT vs. POST im Detail
​
Schwierigkeitsgrad: Fortgeschritten  
Dauer: ~15 Minuten
​

**Aufgabenstellung:** Beschreibe und vergleiche die HTTP-Methoden `POST` und `PUT` anhand ihrer Eigenschaften und Anwendungsfälle.
​
1. Definieren Sie kurz den Zweck von `POST` und `PUT`.
2. Erklären Sie den Begriff **Idempotenz** und stellen Sie fest, welche der beiden Methoden idempotent ist und welche nicht. Begründen Sie Ihre Antwort.
3. Beschreiben Sie anhand der "Analogie Paketversand" den Unterschied in der Anwendung beider Methoden.
4. In welchem Teil der HTTP-Nachricht werden die Daten bei beiden Methoden gesendet?
Ausblenden
