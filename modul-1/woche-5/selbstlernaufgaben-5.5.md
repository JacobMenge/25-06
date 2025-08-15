# Selbstlernaufgaben - Eigene Skripte programmieren

Du erhältst die Anforderungen und ein Code-Gerüst - den Rest programmierst du selbständig. Das ist deine Gelegenheit, das Gelernte praktisch anzuwenden und eigene Lösungen zu entwickeln.

**Erlaubte Konzepte:**
- Variablen mit Text, Zahlen und $true/$false
- `Read-Host` für Benutzereingaben
- `Write-Host` für Ausgaben (gerne mit Farben)
- `if`, `elseif`, `else` Bedingungen
- Vergleiche: `-eq`, `-gt`, `-lt`, `-ge`, `-le`
- Logische Operatoren: `-and`, `-or`
- andere Kozepte nur, wenn ihr sie auch versteht!

**Eigene Ideen willkommen!**
Du kannst dir gerne auch eigene Skript-Ideen überlegen. Du kannst zum Beispiel eine KI fragen, um kreative Ideen zu finden. **Wichtig:** Deine eigenen Skripte müssen sich auf die Themen **If-Else-Bedingungen und Variablen** beschränken. Die Aufgaben sind **nicht verpflichtend** - bearbeite das, was dich interessiert.

**Abgabe:** Nur dein fertiges .ps1-Skript (Screenshots nicht nötig)
---
## Bonus-Aufgabe 1 - Filmtyp-Berater (Einstieg)
**Aufgabenstellung:**
Erstelle einen einfachen Berater, der einen Filmtyp empfiehlt.

**Pseudocode (Denkweise):**
```
1. Begrüße den Benutzer
2. Frage nach der Stimmung
3. WENN Stimmung = "fröhlich" DANN empfehle "Komödie"
4. ANSONSTEN WENN Stimmung = "traurig" DANN empfehle "Drama"
5. ANSONSTEN empfehle "Action"
6. Gib eine Begründung aus
```

**Konkrete Anforderungen:**
- Frage: "Wie fühlst du dich? (fröhlich/traurig/anders)"
- 3 verschiedene Empfehlungen mit if/elseif/else
- **Tipp:** PowerShell ist case-insensitive, "FRÖHLICH" = "fröhlich"

**Erwartete Ausgabe:**
```
=== Filmtyp-Berater ===
Wie fühlst du dich? fröhlich
Empfehlung: Komödie
Begründung: Komödien passen gut zu fröhlicher Stimmung
```

**Code-Struktur:**
```powershell
Write-Host "=== Filmtyp-Berater ==="
$stimmung = Read-Host "Wie fühlst du dich? (fröhlich/traurig/anders)"
if ($stimmung -eq "fröhlich") {
    Write-Host "Empfehlung: Komödie"
    Write-Host "Begründung: Komödien passen gut zu fröhlicher Stimmung"
} elseif ($stimmung -eq "traurig") {
    # Dein Code hier
} else {
    # Dein Code hier
}
```
---
## Bonus-Aufgabe 2 - Alters-Checker (Zahlen-Vergleiche)
**Aufgabenstellung:**
Erstelle einen Checker, der basierend auf dem Alter verschiedene Nachrichten anzeigt.

**Pseudocode (Denkweise):**
```
1. Frage nach dem Alter (als Zahl)
2. WENN Alter kleiner als 18 DANN "Du bist minderjährig"
3. ANSONSTEN WENN Alter größer als 65 DANN "Du bist im Rentenalter"
4. ANSONSTEN "Du bist erwachsen"
```

**Konkrete Anforderungen:**
- Frage: "Wie alt bist du?"
- Verwende Zahlen-Vergleiche: `-lt` (kleiner), `-gt` (größer)
- 3 verschiedene Altersgruppen

**Erwartete Ausgabe:**
```
=== Alters-Checker ===
Wie alt bist du? 25
Status: Du bist erwachsen
Info: Arbeiten und Steuern zahlen gehören dazu
```

**Code-Struktur:**
```powershell
Write-Host "=== Alters-Checker ==="
$alter = Read-Host "Wie alt bist du?"
$alter = [int]$alter  # Wandelt Text in Zahl um
if ($alter -lt 18) {
    Write-Host "Status: Du bist minderjährig"
    # Deine Info hier
} elseif ($alter -gt 65) {
    # Dein Code hier
} else {
    # Dein Code hier
}
```
---
## Bonus-Aufgabe 3 - Einfacher Wetter-Kleidungs-Berater (-and Operator)
**Aufgabenstellung:**
Erstelle einen Berater mit zwei Fragen und dem -and Operator.

**Pseudocode (Denkweise):**
```
1. Frage nach Temperatur (warm/kalt)
2. Frage nach Regen (ja/nein)
3. WENN warm UND kein Regen DANN "T-Shirt und Sonnenbrille"
4. WENN warm UND Regen DANN "Leichte Regenjacke"
5. ANSONSTEN "Warme Jacke"
```

**Konkrete Anforderungen:**
- Nur **2 einfache** -and Kombinationen, Rest mit else
- Verwende `-and` um zwei Bedingungen zu verknüpfen

**Erwartete Ausgabe:**
```
=== Kleidungs-Berater ===
Temperatur? (warm/kalt) warm
Regnet es? (ja/nein) nein
Empfehlung: T-Shirt und Sonnenbrille
```

**Code-Struktur:**
```powershell
Write-Host "=== Kleidungs-Berater ==="
$temperatur = Read-Host "Temperatur? (warm/kalt)"
$regen = Read-Host "Regnet es? (ja/nein)"
if (($temperatur -eq "warm") -and ($regen -eq "nein")) {
    Write-Host "Empfehlung: T-Shirt und Sonnenbrille"
} elseif (($temperatur -eq "warm") -and ($regen -eq "ja")) {
    # Dein Code hier
} else {
    Write-Host "Empfehlung: Warme Jacke"
    Write-Host "Bei Kälte immer warm anziehen!"
}
```
---
**Erinnerung - Grundstruktur (je nach Aufgabe):**
```powershell
# Titel
Write-Host "=== Mein Berater ==="
# Eingabe(n) sammeln
$eingabe1 = Read-Host "Frage 1"
# Optional: $eingabe2 = Read-Host "Frage 2"
# Entscheidung treffen
if (Bedingung) {
    Write-Host "Empfehlung"
} else {
    Write-Host "Andere Empfehlung"
}
```
Bei Fragen melde dich gerne im Kurs-Slackchannel!
