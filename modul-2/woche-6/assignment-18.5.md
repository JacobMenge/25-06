# Pflicht-Assignment: Objektorientierte Programmierung in Python (Einzelarbeit)

## Wochenabschluss: OOP-Grundlagen

### Organisatorische Rahmenbedingungen

Die Abgabe erfolgt bis Montag, 23:59 Uhr. Reiche eine Python-Datei mit dem Dateinamen `vorname_nachname_assignment2.py` ein. Zusätzlich zur Python-Datei erstellst du eine kurze README-Datei im Markdown-Format. Diese README sollte 2 bis 5 Sätze umfassen und folgende Punkte klären: den Zweck deines Programms, wie man es startet und eventuelle Besonderheiten oder Hinweise zur Nutzung.

Der thematische Umfang dieser Aufgabe erstreckt sich über die Grundlagen der objektorientierten Programmierung. Dazu gehören Klassen, Objekte/Instanzen, Attribute, Methoden sowie die Definition und Verwendung von `__init__` und `self`.

---

## Zielsetzung der Aufgabe

Mit diesem Assignment zeigst du, dass du die grundlegenden Konzepte der objektorientierten Programmierung verstanden hast und in einem zusammenhängenden Programm anwenden kannst. Es geht darum, ein kleines, aber funktionierendes Programm zu entwickeln, das mindestens eine Klasse mit Attributen und Methoden verwendet. Du hast dabei die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Mini-Programm

Bei diesem Weg entwickelst du ein Programm zu einem selbstgewählten Thema. Wichtig ist, dass du die geforderten OOP-Konzepte verwendest. Dein Programm sollte einen klaren Zweck haben und mindestens eine Klasse sinnvoll nutzen.

Hier einige Anregungen für mögliche Themen:

**Kontaktverwaltung:** Erstelle eine Anwendung zur Verwaltung von Kontakten. Das Programm sollte Kontakte mit Namen, Telefonnummer und E-Mail-Adresse speichern können. Du könntest Methoden implementieren, um neue Kontakte hinzuzufügen, bestehende anzuzeigen und die Gesamtanzahl der Kontakte auszugeben.

**Buch-Bibliothek:** Entwickle ein System zur Verwaltung einer kleinen Büchersammlung. Das Programm sollte Bücher mit Titel, Autor und Seitenzahl verwalten können. Implementiere Methoden zum Hinzufügen von Büchern, zum Anzeigen aller Bücher und zum Berechnen der durchschnittlichen Seitenzahl.

**Fitness-Tracker:** Baue einen einfachen Fitness-Tracker für Trainingseinheiten. Das Programm sollte Trainings mit Aktivität, Dauer (in Minuten) und Datum speichern können. Du könntest Methoden zur Ausgabe der Trainingsdetails und zur Berechnung der Gesamttrainingsdauer implementieren.

**Rezeptverwaltung:** Erstelle ein Programm zur Verwaltung von Kochrezepten. Jedes Rezept sollte einen Namen, eine Zutatenliste und eine Zubereitungszeit haben. Implementiere Methoden zum Hinzufügen von Rezepten, zum Anzeigen aller Rezepte und zum Finden von Rezepten unter einer bestimmten Zubereitungszeit.

---

## Weg B: Vorgegebene Aufgabe - Haustier-Tamagotchi

Falls du lieber mit einer konkreten Aufgabenstellung arbeiten möchtest, implementiere das folgende Szenario. Diese Aufgabe ist so konzipiert, dass alle geforderten Konzepte automatisch zur Anwendung kommen.

### Ausgangssituation

Du entwickelst ein einfaches virtuelles Haustier-System (ähnlich wie ein Tamagotchi). Jedes Haustier hat verschiedene Bedürfnisse, die sich im Laufe der Zeit ändern, und benötigt entsprechende Pflege.

### Funktionale Anforderungen

Dein Programm soll folgende Funktionen umsetzen:

**Haustier erstellen:** Erstelle eine Klasse `Haustier` mit folgenden Attributen:
- `name` (Name des Haustiers als String)
- `tierart` (z.B. "Hund", "Katze", "Hamster" als String)
- `hunger` (Hungerlevel von 0-100, Startwert: 50)
- `glueck` (Glückslevel von 0-100, Startwert: 50)
- `energie` (Energielevel von 0-100, Startwert: 50)

**Füttern:** Implementiere eine Methode `fuettern()`, die das Hungerlevel um 20 Punkte reduziert (mindestens jedoch auf 0). Die Methode sollte eine passende Nachricht ausgeben, wie "Mampf mampf! [Name] hat gefressen und ist zufrieden."

**Spielen:** Entwickle eine Methode `spielen()`, die das Glückslevel um 15 Punkte erhöht (maximal jedoch auf 100) und gleichzeitig das Energielevel um 10 Punkte reduziert (mindestens auf 0). Gib eine kreative Nachricht aus.

**Schlafen:** Implementiere eine Methode `schlafen()`, die das Energielevel um 30 Punkte erhöht (maximal auf 100) und gleichzeitig das Hungerlevel um 10 Punkte erhöht (maximal auf 100). Gib eine entsprechende Nachricht aus.

**Status anzeigen:** Erstelle eine Methode `status()`, die alle aktuellen Werte übersichtlich ausgibt (Name, Tierart, Hunger, Glück, Energie) und zusätzlich eine Einschätzung des Gesamtzustands gibt (z.B. "Es geht [Name] gut!" wenn alle Werte im grünen Bereich sind).

**Zustandswarnung:** Entwickle eine Methode `zustand_pruefen()`, die Warnungen ausgibt, wenn ein Wert kritisch ist (Hunger > 80, Glück < 30 oder Energie < 20).

### Beispiel für die Verwendung

Dein Programm könnte so verwendet werden:

```python
# Haustier erstellen
haustier1 = Haustier("Bello", "Hund")

# Mit dem Haustier interagieren
haustier1.status()
haustier1.spielen()
haustier1.spielen()
haustier1.fuettern()
haustier1.status()
haustier1.zustand_pruefen()

# Zweites Haustier erstellen
haustier2 = Haustier("Mimi", "Katze")
haustier2.spielen()
haustier2.schlafen()
haustier2.status()
```

### Technische Anforderungen

Dein Programm muss eine Klasse mit `__init__`-Methode enthalten. Die `__init__`-Methode sollte die Attribute `name` und `tierart` als Parameter entgegennehmen und `hunger`, `glueck` und `energie` auf Startwerte setzen. Mindestens vier Instanzmethoden (z.B. `fuettern()`, `spielen()`, `schlafen()`, `status()`) müssen implementiert werden. Alle Methoden müssen `self` als ersten Parameter verwenden und auf die Instanzattribute zugreifen. Es sollten mindestens zwei Instanzen der Klasse erstellt und verwendet werden. Die Werte sollten in sinnvollen Grenzen bleiben (0-100). Achte darauf, dass Werte nicht unter 0 oder über 100 gehen.

---

## Bewertungsraster

Die Bewertung erfolgt nach folgenden Kriterien mit insgesamt 100 möglichen Punkten:

**Struktur und Lesbarkeit (15 Punkte):** Hier wird auf korrekte Einrückung, sprechende Variablen- und Klassennamen sowie sinnvolle Kommentare geachtet. Der Code sollte für andere nachvollziehbar strukturiert sein.

**Klassendefinition (20 Punkte):** Die Klasse muss korrekt mit dem Schlüsselwort `class` definiert sein. Der Klassenname sollte der Python-Konvention folgen (UpperCamelCase). Die Struktur der Klasse sollte logisch aufgebaut sein.

**Konstruktor (__init__) (15 Punkte):** Der `__init__`-Konstruktor muss korrekt implementiert sein. Er sollte `self` als ersten Parameter haben und weitere Parameter für die Initialisierung der Attribute entgegennehmen. Die Attribute müssen mit `self.attributname` gesetzt werden.

**Instanzattribute (10 Punkte):** Mindestens drei Instanzattribute müssen definiert sein. Die Attribute sollten mit `self` referenziert werden. Die Werte der Attribute sollten sinnvoll für die jeweilige Instanz sein.

**Instanzmethoden (20 Punkte):** Mindestens drei Instanzmethoden (außer `__init__`) müssen definiert werden. Alle Methoden müssen `self` als ersten Parameter haben. Die Methoden sollten auf Instanzattribute zugreifen und/oder diese ändern.

**Objekterstellung (10 Punkte):** Mindestens zwei verschiedene Instanzen der Klasse müssen erstellt werden. Die Objekte sollten unterschiedliche Attributwerte haben. Es sollte demonstriert werden, dass jede Instanz unabhängig ist.

**Ausgabe (10 Punkte):** Die Ergebnisse müssen verständlich dargestellt werden. Die Ausgabe sollte zeigen, dass die Methoden korrekt funktionieren. Die Ausgabe sollte für den Nutzer gut lesbar und kreativ formatiert sein.

**Dokumentation (5 Punkte):** Eine kurze README-Datei ist erforderlich. Optional können Docstrings in den Methoden oder Type Hints die Lesbarkeit erhöhen.

**Bonuspunkte (bis zu 15 zusätzliche Punkte):** Für besondere Leistungen wie kreative Erweiterungen (z.B. weitere Aktionen oder Bedürfnisse), Verwendung von Klassenattributen (z.B. Zähler für alle erstellten Haustiere), Implementierung einer Vererbung (z.B. spezielle Haustierarten als Kindklassen), besonders durchdachte Logik für Zustandsänderungen oder umfangreiche und kreative Ausgaben mit ASCII-Art oder Emojis können Bonuspunkte vergeben werden.

Zum Bestehen sind mindestens 50 Punkte erforderlich.

---

## Checkliste vor der Abgabe

Stelle vor dem Einreichen sicher, dass folgende Punkte erfüllt sind:

- Eine Klasse ist mit dem `class`-Schlüsselwort definiert
- Der `__init__`-Konstruktor ist implementiert und initialisiert Attribute
- Mindestens drei Instanzattribute sind vorhanden
- Mindestens drei Instanzmethoden (zusätzlich zu `__init__`) sind definiert
- Alle Methoden verwenden `self` als ersten Parameter
- Mindestens zwei Objekte/Instanzen der Klasse werden erstellt
- Die Methoden greifen auf `self.attributname` zu
- Das Programm erzeugt eine klare Ausgabe über print()
- Die Einrückung ist korrekt und Kommentare sind vorhanden
- Eine README-Datei mit Kurzbeschreibung liegt bei

---

## Wichtige Hinweise

Für diese Aufgabe benötigst du keine externen Module. Die Verwendung von `import` ist nicht erforderlich. Es ist nicht erlaubt, Code aus Internetquellen oder KI-Tools zu kopieren. Jede Person schreibt ihr eigenes, individuelles Programm. Bei ähnlichen Lösungen werden Struktur und Kommentare zur Bewertung herangezogen, um die eigenständige Arbeit zu überprüfen.

Ein Tipp: Lieber ein einfaches, aber funktionierendes Programm abgeben als ein komplexes Programm mit vielen Fehlern. Es geht darum zu zeigen, dass du die Grundkonzepte der objektorientierten Programmierung verstanden hast und anwenden kannst. Konzentriere dich auf eine saubere Implementierung der Basiskonzepte. Sei kreativ bei den Ausgaben und hab Spaß beim Programmieren!

**Hinweis zu fortgeschrittenen Konzepten:** Vererbung, die `super()`-Methode und das Überschreiben von Methoden sind fortgeschrittene Konzepte und für diese Aufgabe nicht erforderlich. Wenn du diese Konzepte bereits verstanden hast und anwenden möchtest (z.B. spezielle Haustierklassen wie `Hund` und `Katze`, die von `Haustier` erben), kannst du damit Bonuspunkte sammeln, aber sie sind nicht Teil der Grundanforderungen.
