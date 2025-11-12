# Pflicht-Assignment: Python-Grundlagen (Einzelarbeit)

## Wochenabschluss: Variablen bis Funktionen

### Organisatorische Rahmenbedingungen

Die Abgabe erfolgt bis Montag, 23:59 Uhr. Reiche eine Python-Datei mit dem Dateinamen `vorname_nachname_assignment1.py` ein. Zusätzlich zur Python-Datei erstellst du eine kurze README-Datei im Markdown-Format. Diese README sollte 2 bis 5 Sätze umfassen und folgende Punkte klären: den Zweck deines Programms, wie man es startet und eventuelle Besonderheiten oder Hinweise zur Nutzung.

Der thematische Umfang dieser Aufgabe erstreckt sich über alle Grundlagen, die wir bis einschließlich Funktionen behandelt haben. Dazu gehören Variablen und Datentypen, Operatoren, bedingte Anweisungen, Schleifen, Listen, Dictionaries sowie die Definition und Verwendung von Funktionen.

---

## Zielsetzung der Aufgabe

Mit diesem Assignment zeigst du, dass du die wichtigsten Python-Grundlagen sicher beherrschst und in einem zusammenhängenden Programm anwenden kannst. Es geht darum, ein kleines, aber funktionierendes Programm zu entwickeln, das die verschiedenen Konzepte sinnvoll miteinander verbindet. Du hast dabei die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Mini-Programm

Bei diesem Weg entwickelst du ein Programm zu einem selbstgewählten Thema. Wichtig ist, dass du alle geforderten Techniken und Konzepte verwendest. Dein Programm sollte einen klaren Zweck haben und die verschiedenen Python-Elemente sinnvoll integrieren.

Hier einige Anregungen für mögliche Themen:

**Tagesplaner:** Erstelle eine Anwendung zur Verwaltung von Aufgaben. Das Programm sollte eine Liste von Aufgaben führen, erledigte Aufgaben zählen können und den aktuellen Fortschritt ausgeben. Du könntest beispielsweise Funktionen implementieren, um Aufgaben hinzuzufügen, als erledigt zu markieren und eine Übersicht zu erstellen.

**Notenverwaltung:** Entwickle ein System zur Speicherung und Auswertung von Noten. Das Programm sollte verschiedene Noten erfassen, den Durchschnitt berechnen und die beste Note ermitteln können. Zusätzlich könntest du eine Funktion einbauen, die prüft, ob ein bestimmter Notendurchschnitt erreicht wurde.

**Produktverwaltung:** Baue eine einfache Produktdatenbank mit Preisen. Das Programm sollte in der Lage sein, Produkte zu verwalten, einen Gesamtpreis zu berechnen und eventuell Rabatte anzuwenden. Du könntest auch eine Funktion zur Suche nach Produkten oder zur Sortierung nach Preis implementieren.

**Temperatur-Tracker:** Erstelle ein Programm zur Auswertung von Wochentemperaturen. Es sollte Temperaturdaten speichern, den Durchschnitt berechnen, den Höchstwert ermitteln und beispielsweise zählen, wie viele Tage über 25 Grad Celsius lagen. Zusätzlich könntest du Warnungen ausgeben, wenn bestimmte Temperaturschwellen überschritten werden.

---

## Weg B: Vorgegebene Aufgabe - Mini-Shop mit Warenkorb

Falls du lieber mit einer konkreten Aufgabenstellung arbeiten möchtest, implementiere das folgende Szenario. Diese Aufgabe ist so konzipiert, dass alle geforderten Konzepte automatisch zur Anwendung kommen.

### Ausgangssituation

Du entwickelst ein einfaches Warenkorbsystem für einen kleinen Shop. Gegeben sind folgende Ausgangsdaten:

```python
catalog = {"Apfel": 1.2, "Brot": 2.5, "Milch": 1.5, "Käse": 3.9}
cart = []
```

### Funktionale Anforderungen

Dein Programm soll folgende Funktionen umsetzen:

**Produkte hinzufügen:** Implementiere eine Funktion, die Produkte zum Warenkorb hinzufügt. Dabei muss geprüft werden, ob das gewünschte Produkt überhaupt im Katalog vorhanden ist. Nur verfügbare Produkte dürfen in den Warenkorb gelegt werden.

**Warenkorb ausgeben:** Erstelle eine übersichtliche Ausgabe aller Produkte im Warenkorb. Dabei soll jedes Produkt mit seiner Menge und dem Einzelpreis angezeigt werden. Falls ein Produkt mehrfach im Warenkorb liegt, sollte die Menge entsprechend summiert werden.

**Zwischensumme berechnen:** Implementiere eine Funktion zur Berechnung der Zwischensumme. Diese addiert alle Preise der Produkte im Warenkorb und gibt den Gesamtbetrag zurück.

**Rabatt anwenden:** Entwickle eine Rabattfunktion, die ab einem Einkaufswert von 10 Euro automatisch 10 Prozent Rabatt gewährt. Bei niedrigeren Beträgen bleibt der Preis unverändert.

**Endsumme ausgeben:** Am Ende soll sowohl die Zwischensumme als auch die Endsumme nach Rabattabzug ausgegeben werden. Die Ausgabe sollte übersichtlich formatiert sein, idealerweise mit zwei Dezimalstellen.

### Technische Anforderungen

Dein Programm muss mindestens zwei eigene Funktionen enthalten. Sinnvolle Funktionen wären beispielsweise `add_item()` zum Hinzufügen von Produkten, `total()` zur Berechnung der Summe und `apply_discount()` zur Rabattberechnung. Mindestens eine bedingte Anweisung muss verwendet werden, beispielsweise zur Prüfung, ob ein Produkt existiert oder ob ein Rabatt gewährt wird. Ebenso ist mindestens eine Schleife erforderlich, etwa zur Iteration über die Produkte im Warenkorb. Sowohl eine Liste (der Warenkorb) als auch ein Dictionary (der Katalog) müssen sinnvoll eingesetzt werden.

---

## Bewertungsraster

Die Bewertung erfolgt nach folgenden Kriterien mit insgesamt 100 möglichen Punkten:

**Struktur und Lesbarkeit (15 Punkte):** Hier wird auf korrekte Einrückung, sprechende Variablennamen und sinnvolle Kommentare geachtet. Der Code sollte für andere nachvollziehbar strukturiert sein.

**Funktionen (20 Punkte):** Du musst mindestens zwei eigene Funktionen definieren. Diese sollten Parameter entgegennehmen und einen Rückgabewert liefern. Die Funktionen sollten eine klare Aufgabe erfüllen und wiederverwendbar sein.

**Bedingte Anweisungen (10 Punkte):** If-, elif- und else-Konstrukte müssen logisch korrekt eingesetzt werden. Die Bedingungen sollten sinnvoll formuliert sein und das gewünschte Verhalten herbeiführen. (mindestens eine Bedingung)

**Schleifen (10 Punkte):** For- oder while-Schleifen müssen korrekt verwendet werden. Die Schleifen sollten über geeignete Datenstrukturen iterieren und keine Endlosschleifen produzieren. (mindestens eine Schleife)

**Listen (10 Punkte):** Listen müssen sinnvoll erstellt, befüllt und genutzt werden. Du solltest zeigen, dass du Elemente hinzufügen, durchlaufen und verarbeiten kannst.

**Dictionaries (10 Punkte):** Die strukturierte Speicherung und der Zugriff auf Daten in einem Dictionary müssen demonstriert werden. Du solltest sowohl lesend als auch schreibend auf Dictionary-Einträge zugreifen können.

**Ausgabe (10 Punkte):** Die Ergebnisse müssen verständlich dargestellt werden. Die Ausgabe sollte für den Nutzer nachvollziehbar und gut formatiert sein.

**Dokumentation (5 Punkte):** Eine kurze README-Datei ist erforderlich. Optional können Docstrings in den Funktionen oder Type Hints die Lesbarkeit erhöhen.

**Bonuspunkte (bis zu 10 zusätzliche Punkte):** Für besondere Leistungen wie List Comprehensions, Input-Validierung oder kreative Erweiterungen können Bonuspunkte vergeben werden.

Zum Bestehen sind mindestens 50 Punkte erforderlich.

---

## Checkliste vor der Abgabe

Stelle vor dem Einreichen sicher, dass folgende Punkte erfüllt sind:

- Bedingte Anweisungen (if, elif, else) sind im Programm enthalten
- Mindestens eine Schleife (for oder while) wird verwendet
- Sowohl eine Liste als auch ein Dictionary kommen zum Einsatz
- Zwei eigene Funktionen mit Parametern und Rückgabewerten sind definiert
- Das Programm erzeugt eine klare Ausgabe über print()
- Die Einrückung ist korrekt und Kommentare sind vorhanden
- Eine README-Datei mit Kurzbeschreibung liegt bei

---

## Wichtige Hinweise

Für diese Aufgabe benötigst du keine externen Module. Die Verwendung von `import` ist nicht erforderlich. Es ist nicht erlaubt, Code aus Internetquellen oder KI-Tools zu kopieren. Jede Person schreibt ihr eigenes, individuelles Programm. Bei ähnlichen Lösungen werden Struktur und Kommentare zur Bewertung herangezogen, um die eigenständige Arbeit zu überprüfen.

Ein Tipp: Lieber ein einfaches, aber funktionierendes Programm abgeben als ein komplexes Programm mit vielen Fehlern. Es geht darum zu zeigen, dass du die Grundkonzepte verstanden hast und anwenden kannst.
