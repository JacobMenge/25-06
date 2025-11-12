# Pflicht-Assignment: REST-APIs mit FastAPI (Einzelarbeit)

## Wochenabschluss: HTTP, REST & FastAPI-Grundlagen

### Organisatorische Rahmenbedingungen

Die Abgabe erfolgt bis Montag, 23:59 Uhr. Reiche eine Python-Datei mit dem Dateinamen `vorname_nachname_assignment3.py` ein. Zusätzlich zur Python-Datei erstellst du eine kurze README-Datei im Markdown-Format. Diese README sollte 2 bis 5 Sätze umfassen und folgende Punkte klären: den Zweck deiner API, wie man sie startet, welche Endpunkte verfügbar sind und eventuelle Besonderheiten oder Hinweise zur Nutzung.

Der thematische Umfang dieser Aufgabe erstreckt sich über die Grundlagen von HTTP, REST und FastAPI. Dazu gehören HTTP-Methoden (GET, POST), Statuscodes, JSON-Datenformate, Pydantic-Modelle sowie die Verwendung der Swagger UI.

---

## Zielsetzung der Aufgabe

Mit diesem Assignment zeigst du, dass du die grundlegenden Konzepte von REST-APIs und FastAPI verstanden hast und in einem zusammenhängenden Programm anwenden kannst. Es geht darum, eine kleine, aber funktionierende API zu entwickeln, die mindestens zwei verschiedene Endpunkte mit unterschiedlichen HTTP-Methoden verwendet. Du hast dabei die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigene Mini-API

Bei diesem Weg entwickelst du eine API zu einem selbstgewählten Thema. Wichtig ist, dass du die geforderten REST- und FastAPI-Konzepte verwendest. Deine API sollte einen klaren Zweck haben und mindestens zwei verschiedene Endpunkte sinnvoll nutzen.

Hier einige Anregungen für mögliche Themen:

**Rezept-API:** Erstelle eine API zur Verwaltung von Rezepten. Die API sollte Rezepte mit Name, Zutaten und Zubereitungszeit speichern können. Implementiere einen GET-Endpunkt zum Abrufen aller Rezepte und einen POST-Endpunkt zum Hinzufügen neuer Rezepte.

**Film-Datenbank-API:** Entwickle eine API zur Verwaltung einer Filmsammlung. Die API sollte Filme mit Titel, Regisseur und Erscheinungsjahr verwalten können. Erstelle Endpunkte zum Abrufen der Filmliste und zum Hinzufügen neuer Filme.

**Zitate-API:** Baue eine API für inspirierende Zitate. Die API sollte Zitate mit Text und Autor speichern können. Implementiere einen Endpunkt zum Abrufen eines zufälligen Zitats und einen zum Hinzufügen neuer Zitate.

**Wetter-Tagebuch-API:** Erstelle eine API zum Festhalten von Wetterbeobachtungen. Jede Beobachtung sollte Datum, Temperatur und Wetterbeschreibung enthalten. Entwickle Endpunkte zum Abrufen aller Beobachtungen und zum Speichern neuer Einträge.

**Workout-Tracker-API:** Baue eine API zur Verwaltung von Trainingseinheiten. Die API sollte Übungen mit Name, Dauer und Kalorienverbrauch speichern können. Implementiere Endpunkte zum Anzeigen aller Übungen und zum Hinzufügen neuer Trainings.

---

## Weg B: Vorgegebene Aufgabe - Bibliotheks-API

Falls du lieber mit einer konkreten Aufgabenstellung arbeiten möchtest, implementiere das folgende Szenario. Diese Aufgabe ist so konzipiert, dass alle geforderten Konzepte automatisch zur Anwendung kommen.

### Ausgangssituation

Du entwickelst eine einfache Bibliotheks-API zur Verwaltung von Büchern. Die API soll es ermöglichen, Bücher zu speichern, abzurufen und grundlegende Informationen über die Sammlung bereitzustellen.

### Funktionale Anforderungen

Deine API soll folgende Funktionen umsetzen:

**Datenmodell erstellen:** Erstelle ein Pydantic-Modell `Buch` mit folgenden Attributen:
- `titel` (Name des Buches als String)
- `autor` (Autor des Buches als String)
- `isbn` (ISBN-Nummer als String)
- `erscheinungsjahr` (Jahr als Integer)
- `verfuegbar` (Boolean, ob das Buch verfügbar ist, Standardwert: True)

**Datenspeicher:** Verwende eine einfache Liste, um die Bücher während der Laufzeit zu speichern. Füge mindestens zwei Beispiel-Bücher beim Start hinzu.

**GET-Endpunkt für alle Bücher:** Implementiere einen Endpunkt `GET /buecher`, der alle gespeicherten Bücher als JSON-Liste zurückgibt. Die Antwort sollte den Statuscode 200 haben.

**GET-Endpunkt für einzelnes Buch:** Entwickle einen Endpunkt `GET /buecher/{isbn}`, der ein spezifisches Buch anhand seiner ISBN zurückgibt. Wenn das Buch nicht gefunden wird, soll der Statuscode 404 zurückgegeben werden mit einer entsprechenden Fehlermeldung.

**POST-Endpunkt zum Hinzufügen:** Erstelle einen Endpunkt `POST /buecher`, der ein neues Buch zur Sammlung hinzufügt. Der Request-Body sollte das Pydantic-Modell verwenden. Bei Erfolg sollte der Statuscode 201 zurückgegeben werden zusammen mit dem hinzugefügten Buch.

**GET-Endpunkt für Statistiken:** Implementiere einen Endpunkt `GET /statistik`, der grundlegende Statistiken zurückgibt:
  - Gesamtanzahl der Bücher
  - Anzahl verfügbarer Bücher
  - Anzahl ausgeliehener Bücher

**Validierung:** Stelle sicher, dass keine zwei Bücher mit derselben ISBN hinzugefügt werden können. Bei einem Versuch, ein Duplikat hinzuzufügen, soll der Statuscode 400 mit einer entsprechenden Fehlermeldung zurückgegeben werden.

### Beispiel für die Verwendung

Deine API könnte so verwendet werden:

**Server starten:**
```bash
fastapi dev vorname_nachname_assignment3.py
```

**Alle Bücher abrufen (GET):**
```
GET http://127.0.0.1:8000/buecher
```

**Einzelnes Buch abrufen (GET):**
```
GET http://127.0.0.1:8000/buecher/978-3-16-148410-0
```

**Neues Buch hinzufügen (POST):**
```json
POST http://127.0.0.1:8000/buecher
{
    "titel": "Python für Einsteiger",
    "autor": "Max Mustermann",
    "isbn": "978-3-16-148410-0",
    "erscheinungsjahr": 2024
}
```

**Statistiken abrufen (GET):**
```
GET http://127.0.0.1:8000/statistik
```

### Technische Anforderungen

Dein Programm muss FastAPI korrekt importieren und eine FastAPI-Instanz erstellen. Du solltest mindestens drei verschiedene Endpunkte implementieren. Mindestens ein GET-Endpunkt und ein POST-Endpunkt müssen vorhanden sein. Verwende Pydantic für das Datenmodell. Alle Antworten müssen im JSON-Format erfolgen. Verwende korrekte HTTP-Statuscodes (200, 201, 400, 404). Die API muss über Swagger UI testbar sein. Füge hilfreiche Kommentare hinzu, die deine Implementierung erklären.

---

## Bewertungsraster

Die Bewertung erfolgt nach folgenden Kriterien mit insgesamt 100 möglichen Punkten:

**Code-Struktur und Lesbarkeit (15 Punkte):** Hier wird auf korrekte Einrückung, sprechende Variablennamen, sinnvolle Kommentare und eine logische Struktur geachtet. Der Code sollte für andere nachvollziehbar sein.

**FastAPI-Setup (15 Punkte):** FastAPI muss korrekt importiert und initialisiert werden. Die App-Instanz sollte korrekt benannt sein (üblicherweise `app`). Die grundlegende Struktur einer FastAPI-Anwendung muss erkennbar sein.

**Pydantic-Modell (15 Punkte):** Ein Pydantic-Modell muss korrekt von `BaseModel` erben. Mindestens drei Attribute mit korrekten Type Hints müssen definiert sein. Das Modell sollte sinnvoll für den gewählten Use-Case sein.

**GET-Endpunkte (20 Punkte):** Mindestens zwei GET-Endpunkte müssen implementiert sein. Sie sollten korrekte Pfade haben und JSON-Daten zurückgeben. Mindestens ein Endpunkt sollte dynamische Daten verwenden (z.B. eine Liste durchsuchen).

**POST-Endpunkt (20 Punkte):** Mindestens ein POST-Endpunkt muss implementiert sein. Er sollte ein Pydantic-Modell als Request-Body verwenden. Die empfangenen Daten sollten verarbeitet werden (z.B. zu einer Liste hinzugefügt). Eine sinnvolle Antwort muss zurückgegeben werden.

**HTTP-Statuscodes (10 Punkte):** Korrekte Statuscodes sollten verwendet werden (200 für erfolgreiche GET-Anfragen, 201 für erfolgreiche POST-Anfragen, 404 für nicht gefundene Ressourcen, 400 für fehlerhafte Anfragen).

**Funktionalität (10 Punkte):** Die API muss starten und über Swagger UI erreichbar sein. Alle Endpunkte müssen funktionieren. Die API sollte den beschriebenen Zweck erfüllen.

**Dokumentation (5 Punkte):** Eine README-Datei mit Kurzbeschreibung ist erforderlich. Optional können Docstrings in den Funktionen die Lesbarkeit erhöhen.

**Bonuspunkte (bis zu 15 zusätzliche Punkte):** Für besondere Leistungen wie zusätzliche Endpunkte (z.B. PUT für Updates, DELETE zum Löschen), erweiterte Validierung und Fehlerbehandlung, Verwendung von Path-Parametern und Query-Parametern, besonders durchdachte Datenstruktur oder kreative API-Ideen können Bonuspunkte vergeben werden.

Zum Bestehen sind mindestens 50 Punkte erforderlich.

---

## Checkliste vor der Abgabe

Stelle vor dem Einreichen sicher, dass folgende Punkte erfüllt sind:

- FastAPI ist korrekt importiert und initialisiert
- Ein Pydantic-Modell mit `BaseModel` ist definiert
- Mindestens zwei GET-Endpunkte sind implementiert
- Mindestens ein POST-Endpunkt ist implementiert
- Alle Endpunkte verwenden korrekte Decorators (@app.get, @app.post)
- Die Endpunkte geben JSON-Daten zurück
- Korrekte HTTP-Statuscodes werden verwendet
- Die API startet mit `fastapi dev dateiname.py`
- Die Swagger UI ist unter http://127.0.0.1:8000/docs erreichbar
- Alle Endpunkte sind über Swagger UI testbar
- Die Einrückung ist korrekt und Kommentare sind vorhanden
- Eine README-Datei mit Kurzbeschreibung liegt bei

---

## Wichtige Hinweise

FastAPI muss installiert sein (`pip3 install "fastapi[standard]"`). Es ist nicht erlaubt, Code aus Internetquellen oder KI-Tools zu kopieren. Jede Person schreibt ihre eigene, individuelle API. Bei ähnlichen Lösungen werden Struktur und Kommentare zur Bewertung herangezogen, um die eigenständige Arbeit zu überprüfen.

Ein Tipp: Lieber eine einfache, aber funktionierende API abgeben als eine komplexe API mit vielen Fehlern. Es geht darum zu zeigen, dass du die Grundkonzepte von FastAPI und REST verstanden hast und anwenden kannst. Konzentriere dich auf eine saubere Implementierung der Basiskonzepte. Teste deine API ausgiebig über Swagger UI, bevor du sie abgibst, und hab Spaß beim Entwickeln deiner ersten eigenen API!

**Hinweis zu fortgeschrittenen Konzepten:** Datenbankanbindung, Authentifizierung, Middleware und komplexe Validierung sind fortgeschrittene Konzepte und für diese Aufgabe nicht erforderlich. Wenn du diese Konzepte bereits verstanden hast und anwenden möchtest, kannst du damit Bonuspunkte sammeln, aber sie sind nicht Teil der Grundanforderungen.

**Hilfreiche Ressourcen:**
- FastAPI-Dokumentation: https://fastapi.tiangolo.com/
- Pydantic-Dokumentation: https://docs.pydantic.dev/
- HTTP-Statuscodes Übersicht: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

**Viel Erfolg bei deinem ersten API-Projekt!**
