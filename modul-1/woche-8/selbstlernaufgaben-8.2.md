# Selbstlernaufgaben - Client-Server-Kommunikation

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Client-Server verstehen

**Deine Aufgabe:**

Beantworte folgende Fragen in **deinen eigenen Worten**:

1. **Erkläre das Client-Server-Prinzip:**
   - Was ist ein Client und welche Aufgabe hat er?
   - Was ist ein Server und welche Aufgabe hat er?
   - Nenne 3 Beispiele für Client-Server-Kommunikation aus deinem Alltag

2. **Praktische Zuordnung:**
   - WhatsApp auf deinem Handy: Client oder Server?
   - YouTube-Website: Client oder Server?
   - Chrome Browser: Client oder Server?
   - Instagram-Server von Meta: Client oder Server?

**Formatvorschläge:**
- Kurze Antworten in Stichpunkten
- PDF oder Word-Dokument

---

## 2. Grundlagenaufgabe - TCP/IP-Stack verstehen

**Deine Aufgabe:**

Das Internet funktioniert wie das Postsystem mit 4 Schichten. Beantworte:

1. **Erkläre jede Schicht in einem Satz:**
   - Schicht 1 (Netzzugang): 
   - Schicht 2 (Internet): 
   - Schicht 3 (Transport): 
   - Schicht 4 (Anwendung): 

2. **Alltagsbeispiele:**
   - Nenne 2 Beispiele für Schicht 1 (Netzzugang)
   - Was passiert in Schicht 2 mit der Domain "google.de"?

**Formatvorschläge:**
- Übersichtliche Liste oder Tabelle
- Kurze, präzise Antworten

---

## 3. Grundlagenaufgabe - Ports und Sicherheit

**Deine Aufgabe:**

1. **Ports erklären:**
   - Warum braucht ein Server verschiedene Ports?
   - Vervollständige die Haus-Analogie: "Ein Server ist wie ein Bürogebäude. Die IP-Adresse ist _____, die Ports sind _____"


2. **HTTP vs HTTPS:**
   - Erkläre den Unterschied zwischen HTTP und HTTPS in 2-3 Sätzen
   - Woran erkennst du eine sichere HTTPS-Verbindung im Browser?
   - Warum solltest du niemals Passwörter auf HTTP-Seiten eingeben?

3. **Sicherheits-Check:**
   Schau dir 5 verschiedene Websites an, die du regelmäßig nutzt. Notiere:
   - Name der Website
   - HTTP oder HTTPS?
   - Schloss-Symbol vorhanden? (Ja/Nein)

**Formatvorschläge:**
- Strukturiertes Dokument mit Überschriften
- Tabelle für den Sicherheits-Check

---

## 4. Grundlagenaufgabe - Request-Response verstehen

**Deine Aufgabe:**

1. **Ablauf beschreiben:**
   Du gibst "www.youtube.com" in deinen Browser ein und drückst Enter. Beschreibe Schritt für Schritt, was passiert:
   - Schritt 1: Browser macht _____ an den Server
   - Schritt 2: Server sendet _____ zurück
   - Schritt 3: Browser macht _____
   - Schritt 4: Du siehst _____

2. **HTTP-Methoden zuordnen:**
   Welche HTTP-Methode wird verwendet?
   - YouTube-Startseite aufrufen: _____
   - Kommentar unter Video schreiben: _____
   - Dein Profilbild ändern: _____
   - Video aus Playlist löschen: _____

3. **Analyse deiner Lieblings-Website:**
   Gehe auf eine Website deiner Wahl und beantworte:
   - Wie viele verschiedene Requests sendest du ungefähr? (Denk an: HTML, Bilder, CSS, etc.)
   - Was passiert, wenn der Server offline ist?
   - Warum lädt die Seite manchmal langsam?

**Formatvorschläge:**
- Schritt-für-Schritt-Beschreibung
- Kurze Analyse als Text

---

## 5. Bonus-Aufgabe - Praktische Netzwerk-Erkundung (freiwillig)

**Deine Aufgabe:**

**Teil A: Einfache Curl-Befehle verstehen**

Curl ist ein Kommandozeilen-Tool, um HTTP-Requests zu senden. Hier lernst du die Grundlagen:

**Was ist Curl?**
Curl = Client URL, ein Programm das HTTP-Requests senden kann, genau wie ein Browser, aber ohne grafische Oberfläche.

**Schritt-für-Schritt Anleitung:**

1. **Terminal/Eingabeaufforderung öffnen:**
   - Windows: Win+R, "cmd" eingeben
   - Mac: Cmd+Leertaste, "Terminal" eingeben
   - Linux: Ctrl+Alt+T

2. **Grundlegender GET-Request:**
   ```bash
   curl http://httpbin.org/get
   ```
   **Was passiert:** Du sendest eine GET-Anfrage an httpbin.org (Test-Website für HTTP)
   **Ergebnis:** Du siehst die JSON-Antwort des Servers mit Informationen über deine Anfrage

3. **Headers anzeigen:**
   ```bash
   curl -I https://www.google.com
   ```
   **Was passiert:** Du sendest nur eine Header-Anfrage (-I flag)
   **Ergebnis:** Du siehst HTTP-Status-Code, Content-Type, Server-Informationen, etc.

4. **POST-Request mit Daten:**
   ```bash
   curl -X POST -d "name=Max&age=20" http://httpbin.org/post
   ```
   **Was passiert:** Du sendest Daten an den Server (wie ein Formular)
   **Ergebnis:** Server zeigt dir, welche Daten er erhalten hat

**Teil B: Deine Curl-Experimente**

Probiere folgende Befehle aus und dokumentiere, was passiert:

1. `curl -I https://github.com`
   - Was ist der Status-Code?
   - Welcher Server läuft da?

2. `curl https://api.github.com/users/octocat`
   - Was für Daten kommen zurück?
   - In welchem Format sind sie?

3. `curl -A "MeinBrowser" http://httpbin.org/user-agent`
   - Was zeigt "User-Agent" an?
   - Warum ist das wichtig?

**Teil C: Reflexion**

Beantworte nach deinen Experimenten:
- Welche HTTP-Methoden hast du verwendet?
- Welche Ports wurden wahrscheinlich verwendet? (Tipp: http = ?, https = ?)
- Was ist der Unterschied zwischen Curl und deinem Browser?
- Welche Schichten des TCP/IP-Stack hat Curl verwendet?

**Formatvorschläge:**
- Dokumentiere deine Befehle und Ergebnisse
- Screenshots der Terminal-Ausgaben
- Kurze Erklärung, was du gelernt hast

---
