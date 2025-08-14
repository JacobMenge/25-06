# Selbstlernaufgaben - PowerShell Datentypen und Bedingungen 

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Datentypen kennenlernen

**Dokumentation:** Mache von **jedem Code-Block** einen Screenshot der Eingabe UND der Ausgabe. Speichere alle Screenshots in einem Word/PDF-Dokument.

**Deine Aufgabe:**

Lerne die wichtigsten Datentypen in PowerShell kennen und verstehe, wofür sie verwendet werden.

**Was sind Datentypen?**

Datentypen sind wie verschiedene Arten von Informationen:
- **Text** → Namen, Wörter, Sätze (immer in Anführungszeichen)
- **Zahlen** → Alter, Anzahl, Jahre (ohne Anführungszeichen)
- **Ja/Nein** → $true oder $false

**Teil A: Verschiedene Datentypen ausprobieren**

Probiere diese Befehle **einzeln** aus:

```powershell
# Text speichern
$meinName = "Anna"
Write-Host "Mein Name ist: $meinName"
```

```powershell
# Zahl speichern
$meinAlter = 20
Write-Host "Ich bin $meinAlter Jahre alt"
```

```powershell
# Ja/Nein speichern
$istStudent = $true
Write-Host "Student: $istStudent"
```

**Teil B: Text und Zahlen unterscheiden**

```powershell
# Text zusammenfügen
$vorname = "Max"
$nachname = "Müller"
$vollername = $vorname + " " + $nachname
Write-Host "Vollständiger Name: $vollername"
```

```powershell
# Zahlen rechnen
$zahl1 = 10
$zahl2 = 5
$summe = $zahl1 + $zahl2
Write-Host "10 + 5 = $summe"
```

```powershell
# Was passiert mit Text-Zahlen?
$text1 = "10"
$text2 = "5"
$ergebnis = $text1 + $text2
Write-Host "Text 10 + Text 5 = $ergebnis"
```

**Teil C: Verschiedene Beispiele**

```powershell
# Verschiedene Informationen
$name = "Lisa"
$alter = 25
$hatHund = $true
$stadt = "Berlin"

Write-Host "Name: $name"
Write-Host "Alter: $alter"
Write-Host "Hat Hund: $hatHund"
Write-Host "Stadt: $stadt"
```

**Fragen zum Beantworten:**
1. Was ist der Unterschied zwischen `"10"` und `10`?
2. Was kommt bei `"10" + "5"` heraus? Was bei `10 + 5`?
3. Wann benutzt man Anführungszeichen?
4. Was bedeuten $true und $false?

**Erstelle dein eigenes Beispiel:**
Ändere die Werte und probiere es aus:
```powershell
$meinVorname = "Setze hier deinen Namen ein"
$meinAlter = 20
$magPizza = $true
$meineLieblingsfarbe = "Blau"

Write-Host "Ich heiße $meinVorname"
Write-Host "Ich bin $meinAlter Jahre alt"
Write-Host "Ich mag Pizza: $magPizza"
Write-Host "Meine Lieblingsfarbe ist $meineLieblingsfarbe"
```

---

## 2. Grundlagenaufgabe - Einfache Bedingungen (if/else)

**Dokumentation:** Mache von **jedem Code-Block** einen Screenshot. Teste **verschiedene Werte** und dokumentiere die unterschiedlichen Ergebnisse.

**Deine Aufgabe:**

Lerne, wie PowerShell einfache Entscheidungen treffen kann.

**Was ist eine Bedingung?**

Eine Bedingung ist wie eine Frage mit Ja/Nein-Antwort:
- Wenn die Antwort **Ja** ist → mache das
- Wenn die Antwort **Nein** ist → mache etwas anderes

**Grundform:**
```powershell
if (Frage) {
    # Das passiert bei "Ja"
} else {
    # Das passiert bei "Nein"
}
```

**Teil A: Erste einfache Bedingung mit Zahlen**

```powershell
$alter = 18

if ($alter -ge 18) {
    Write-Host "Du bist erwachsen!" -ForegroundColor Green
} else {
    Write-Host "Du bist noch nicht erwachsen." -ForegroundColor Yellow
}
```

**Teste verschiedene Werte:** Ändere `$alter` auf 16, dann auf 25, dann auf 18.

**Wichtige Vergleiche:**
- `-eq` bedeutet "ist gleich"
- `-gt` bedeutet "ist größer"
- `-lt` bedeutet "ist kleiner"
- `-ge` bedeutet "ist größer oder gleich"

**Teil B: Text vergleichen**

```powershell
# Beispiel 1: Exakte Übereinstimmung
$name = "tom"

if ($name -eq "tom") {
    Write-Host "Hallo Tom!" -ForegroundColor Green
} else {
    Write-Host "Du bist nicht Tom." -ForegroundColor Red
}
```

**Wichtig:** Groß- und Kleinschreibung muss exakt stimmen! "Tom" ist nicht gleich "tom".

**Teil C: Zahlen vergleichen**

```powershell
$punkte = 75

if ($punkte -gt 50) {
    Write-Host "Gut gemacht! Du hast bestanden." -ForegroundColor Green
} else {
    Write-Host "Leider nicht bestanden." -ForegroundColor Red
}
```

**Teste verschiedene Werte:** Ändere `$punkte` auf 30, dann auf 85.

**Teil D: Ja/Nein-Werte**

```powershell
$istSonntag = $true

if ($istSonntag -eq $true) {
    Write-Host "Heute ist Sonntag - Ausschlafen!" -ForegroundColor Blue
} else {
    Write-Host "Heute ist ein Werktag." -ForegroundColor Yellow
}
```

**Teste:** Ändere `$istSonntag` auf `$false`.

**Teil E: Mehrfach-Bedingungen**

```powershell
$wetter = "sonnig"

if ($wetter -eq "sonnig") {
    Write-Host "Perfekt für einen Spaziergang!" -ForegroundColor Yellow
} elseif ($wetter -eq "regnerisch") {
    Write-Host "Regenschirm nicht vergessen!" -ForegroundColor Blue
} elseif ($wetter -eq "schnee") {
    Write-Host "Zeit für warme Kleidung!" -ForegroundColor White
} else {
    Write-Host "Wie ist das Wetter denn?" -ForegroundColor Gray
}
```

**Teste verschiedene Werte:** Ändere `$wetter` auf "regnerisch", "schnee", "bewölkt".

**Fragen zum Beantworten:**
1. Was bedeutet `-ge`?
2. Was ist der Unterschied zwischen `if` und `elseif`?
3. Was passiert, wenn keine Bedingung zutrifft und es kein `else` gibt?
4. Warum funktioniert `"Tom" -eq "tom"` nicht?

---

## 3. Weiterführend - Einfache UND/ODER-Bedingungen

**Dokumentation:** Mache Screenshots von **allen Beispielen** und teste **verschiedene Kombinationen** von Werten.

**Deine Aufgabe:**

Lerne, wie du zwei einfache Bedingungen miteinander verbinden kannst.

**UND und ODER erklärt:**

**UND (-and):** Beide Bedingungen müssen stimmen
- "Ich gehe schwimmen, wenn es warm ist UND die Sonne scheint"

**ODER (-or):** Mindestens eine Bedingung muss stimmen  
- "Ich nehme den Regenschirm, wenn es regnet ODER bewölkt ist"

**Teil A: Einfache UND-Bedingung**

```powershell
$wetter = "sonnig"
$istWarm = $true

if (($wetter -eq "sonnig") -and ($istWarm -eq $true)) {
    Write-Host "Perfekt für ein Picknick!" -ForegroundColor Green
} else {
    Write-Host "Heute lieber drinnen bleiben." -ForegroundColor Red
}

Write-Host "Wetter: $wetter, Warm: $istWarm"
```

**Teste verschiedene Kombinationen:**
- `$wetter = "sonnig"` und `$istWarm = $true`
- `$wetter = "regnerisch"` und `$istWarm = $true`
- `$wetter = "sonnig"` und `$istWarm = $false`

**Teil B: Einfache ODER-Bedingung**

```powershell
$wetter = "regnerisch"
$istKalt = $true

if (($wetter -eq "regnerisch") -or ($istKalt -eq $true)) {
    Write-Host "Nimm eine Jacke mit!" -ForegroundColor Yellow
} else {
    Write-Host "T-Shirt reicht heute." -ForegroundColor Green
}

Write-Host "Wetter: $wetter, Kalt: $istKalt"
```

**Teste verschiedene Kombinationen:**
- `$wetter = "regnerisch"` und `$istKalt = $true`
- `$wetter = "sonnig"` und `$istKalt = $true`
- `$wetter = "sonnig"` und `$istKalt = $false`

**Teil C: Praktisches Beispiel**

```powershell
$name = "Lisa"
$tag = "Samstag"

Write-Host "=== Aktivitäten-Check ===" -ForegroundColor Magenta

# UND: Beide müssen stimmen
if (($name -eq "Lisa") -and ($tag -eq "Samstag")) {
    Write-Host "Lisa kann am Samstag lange schlafen!" -ForegroundColor Green
} else {
    Write-Host "Normale Zeiten heute." -ForegroundColor White
}

# ODER: Mindestens eins muss stimmen  
if (($tag -eq "Samstag") -or ($tag -eq "Sonntag")) {
    Write-Host "Wochenende - Zeit zum Entspannen!" -ForegroundColor Yellow
} else {
    Write-Host "Werktag - Zeit für Arbeit oder Schule." -ForegroundColor Gray
}
```

**Teil D: Verschiedene Kombinationen verstehen**

```powershell
$istSommer = $true
$istWarm = $true

Write-Host "=== UND-Test ==="
if (($istSommer -eq $true) -and ($istWarm -eq $true)) {
    Write-Host "Beide Bedingungen sind wahr!" -ForegroundColor Green
} else {
    Write-Host "Mindestens eine Bedingung ist falsch." -ForegroundColor Red
}

Write-Host "=== ODER-Test ==="
if (($istSommer -eq $true) -or ($istWarm -eq $true)) {
    Write-Host "Mindestens eine Bedingung ist wahr!" -ForegroundColor Green
} else {
    Write-Host "Beide Bedingungen sind falsch." -ForegroundColor Red
}
```

**Teste alle Kombinationen:**
- `$istSommer = $true`, `$istWarm = $true`
- `$istSommer = $true`, `$istWarm = $false`
- `$istSommer = $false`, `$istWarm = $true`
- `$istSommer = $false`, `$istWarm = $false`

**Fragen zum Beantworten:**
1. Wann ist eine UND-Bedingung wahr?
2. Wann ist eine ODER-Bedingung wahr?
3. Was passiert bei `($wetter -eq "sonnig") -and ($istKalt -eq $true)` wenn das Wetter sonnig aber es kalt ist?
4. Erstelle eine Wahrheitstabelle für UND und ODER mit allen Kombinationen

---

## 4. Bonus-Aufgabe - Einfacher Name-Rater

**Dokumentation:** Screenshot deines fertigen Codes UND mindestens zwei Testläufe.

**Deine Herausforderung:**

Erstelle ein einfaches Ratespiel mit Namen!

**Konkrete Anforderungen:**
1. Definiere einen geheimen Namen als Variable
2. Frage den Benutzer nach seinem Tipp
3. Vergleiche die Eingabe mit dem geheimen Namen
4. Sage "Richtig!" oder "Falsch! Der Name war..."

**Code-Gerüst:**
```powershell
# Hier deinen Code schreiben:
$geheimerName = "???"
$tipp = Read-Host "???"
if (???) {
    Write-Host "???"
} else {
    Write-Host "???"
}
```

**Erwartete Ausgabe:**
```
Rate meinen Lieblingsnamen: anna
Falsch! Der Name war Tom.
```

**Zusatz-Herausforderung:** Mache das Spiel mit verschiedenen Namen und teste es.

---

## 5. Bonus-Aufgabe - Einfacher Wetter-Berater

**Dokumentation:** Screenshot deines Codes UND mindestens drei verschiedene Testläufe.

**Deine Herausforderung:**

Erstelle einen Berater, der Kleidungsempfehlungen gibt!

**Konkrete Anforderungen:**
1. Frage nach dem Wetter (sonnig/regnerisch/schnee)
2. Frage, ob es warm oder kalt ist
3. Gib eine passende Kleidungsempfehlung
4. Verwende UND/ODER-Bedingungen

**Logik-Hilfe:**
- WENN (regnerisch ODER schnee) → "Nimm eine Jacke!"
- WENN (sonnig UND warm) → "T-Shirt reicht!"
- Alle anderen Fälle → "Zieh dich normal an."

**Code-Gerüst:**
```powershell
Write-Host "=== Wetter-Berater ==="
$wetter = Read-Host "???"
$istWarm = Read-Host "???"

if (($wetter -eq "???") -or ($wetter -eq "???")) {
    Write-Host "???"
} elseif (($wetter -eq "???") -and ($istWarm -eq "???")) {
    Write-Host "???"
} else {
    Write-Host "???"
}
```

**Teste mit:** sonnig+warm, regnerisch+warm, schnee+kalt

---

## 6. Bonus-Aufgabe - Einfacher Punkte-Rechner

**Dokumentation:** Screenshot deines Codes UND Tests mit verschiedenen Punktzahlen.

**Deine Herausforderung:**

Erstelle einen Rechner, der feste Punktzahlen in Noten umwandelt!

**Konkrete Anforderungen:**
1. Definiere verschiedene Punktzahlen als Variablen (nicht Read-Host!)
2. Verwende if/elseif/else für die Notenberechnung
3. Sage auch "bestanden" oder "nicht bestanden"

**Noten-Schema:**
- 90+ Punkte = Note 1
- 75+ Punkte = Note 2  
- 60+ Punkte = Note 3
- 45+ Punkte = Note 4
- Weniger = Note 5
- Bestanden ab Note 4

**Code-Gerüst:**
```powershell
$punkte = 85  # Ändere diesen Wert zum Testen

Write-Host "Punkte: $punkte"

if ($punkte -ge ???) {
    Write-Host "Note: ???"
} elseif ($punkte -ge ???) {
    Write-Host "Note: ???"
} # ... weitere elseif

if ($punkte -ge ???) {
    Write-Host "Bestanden!"
} else {
    Write-Host "Nicht bestanden."
}
```

**Teste mit:** 95, 80, 65, 50, 30 Punkten

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr
- **Pflichtaufgaben:** Aufgaben 1-3 (mit Screenshots aller Code-Blöcke)
- **Bonus-Aufgaben:** Aufgaben 4-6 (Code + Testläufe)
- **Format:** PDF oder Word-Dokument

**Einfache Regeln zum Merken:**
- Text immer in Anführungszeichen: `"Hallo"`
- Zahlen ohne Anführungszeichen: `25`
- `if ($variable -eq "Text")` - Klammern um die Bedingung
- Groß-/Kleinschreibung bei Text beachten: `"Tom" ≠ "tom"`
- `-eq` für "ist gleich", `-gt` für "ist größer"  
- `-and` für "UND" (beide müssen stimmen)
- `-or` für "ODER" (eins muss stimmen)

Bei Fragen melde dich gerne im Kurs-Slackchannel!
