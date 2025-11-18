## 1. Grundlagen API und API-Call

Schwierigkeitsgrad: **Grundlegend** 

Dauer: **~10 Minuten**

Aufgabenstellung: Beantworte die folgenden Fragen, um die Konzepte von API, API-Call und deren Struktur zu definieren.

1.  Wofür steht die Abkürzung ***API*** und welche Funktion hat eine API?
    
2. Was ist der Zweck eines **API-Calls** und wie wird der Kommunikationsfluss dabei beschrieben?
    
3. Der Beispiel-API-Call lautet: `GET https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata`. Welchen Bestandteil des Calls repräsentiert `?s=Arrabiata` und wie wird dieser genannt?
    

---

## 2. API-Bereitstellung und Parameter

Schwierigkeitsgrad: **Grundlegend** 

Dauer: **~15 Minuten**

Aufgabenstellung: Beantworte die Fragen zur Bereitstellung und den Regeln der API-Nutzung.

1. Wer erstellt und stellt APIs in der Regel bereit?
    
2. Warum ist das Lesen der **Dokumentation** einer API essentiell, bevor du einen Call durchführst?
    
3. Die URL-Zusammensetzung der OpenWeatherMap API zeigt, dass der Parameter `lat` (Latitude) als **required** (erforderlich) angegeben ist. Was bedeutet dies für deinen API-Call?
    
4. Viele APIs benötigen eine zusätzliche **Authentication** zur Abfrage. Wie wird dieser **Authentifizierungsschlüssel** genannt und wofür wird er benötigt?
    

---

## 3. Postman-Analyse und Statusprüfung

Schwierigkeitsgrad: **Mittel** 

Dauer: **~15 Minuten**

Aufgabenstellung: Postman wird zum Testen von API-Anfragen verwendet. Führe einen Call durch und analysiere das Ergebnis.

1. Was ist die primäre Funktion des Tools **Postman** und wo kannst du es verwenden?
    
2. Der HTTP-Statuscode **`200 OK`** wird in der Antwort angezeigt. Was bedeutet dieser Code allgemein für den API-Call?
    
3. Die Antwort der API wird unten im **JSON-Format** angezeigt. Was ist JSON und woraus besteht es immer (zwei Hauptelemente)?
    
4. Angenommen, du würdest eine Ressource anfragen, die nicht existiert (z. B. eine falsche ID). Welchen Statuscode im Bereich **`4xx`** würdest du dann als Antwort erwarten?
    

---

## 4. Das REST-Prinzip und `requests`-Statusprüfung

Schwierigkeitsgrad: **Mittel** 

Dauer: **~20 Minuten**

Aufgabenstellung: Das REST-Prinzip und die Statuscode-Prüfung sind Kernbestandteile der Web-API-Kommunikation.

1. Nenne die **zwei zentralen Elemente** des **REST-Prinzips**.
    
2. Wenn du in Python die `requests`-Bibliothek verwendest, wie greifst du auf den Statuscode der API-Antwort zu?
    
3. Beschreibe die "weitere Art" der Statuscode-Überprüfung in Python (`if response:`). Welche Statuscodes werden dabei automatisch als Erfolg gewertet?


---

## 5. Implementierung eines API-Calls mit Python

Schwierigkeitsgrad: **Fortgeschritten** 

Dauer: **~50 Minuten**

Aufgabenstellung: Implementiere ein vollständiges Python-Skript, das einen API-Call mit der `requests`-Bibliothek durchführt und das Ergebnis basierend auf dem Statuscode analysiert.

1. **Vorbereitung:** Installiere die `requests`-Library: `pip install requests`
    
2. **Ziel-URL:** Verwende die API für zufällige Chuck Norris Sprüche oder eine beliebige andere API:
		'https://api.chucknorris.io/jokes/random'
    
3. **Skript erstellen:**
    
    - Schreibe ein Python-Skript, das die `requests`-Bibliothek importiert.
        
    - Führe einen **GET**-Aufruf an die Ziel-URL aus und speichere die Antwort in der Variablen `response`.
        
    - Überprüfe den Erfolg des Aufrufs mit der einfachen Methode (`if response:`).
        
4. **Ausgabe:**
    
    - **Bei Erfolg:** Gib den Statuscode (`response.status_code`) und den gesamten **JSON-Inhalt** der Antwort (`response.json()`) aus.
        
    - **Bei Misserfolg:** Gib eine Fehlermeldung und den zurückgegebenen Statuscode (`response.status_code`) aus.
