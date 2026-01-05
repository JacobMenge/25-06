# Webarchitektur & HTTP - Praktische Übungen

## Übersicht

In dieser Übung vertiefst du dein Wissen über:
- **Internet vs. World Wide Web** - Die grundlegenden Unterschiede
- **Client-Server-Architektur** - Wie Webanwendungen kommunizieren
- **HTTP-Protokoll** - Requests, Responses und Status Codes
- **URLs & DNS** - Wie Adressen funktionieren
- **Browser DevTools** - Dein wichtigstes Debugging-Werkzeug

Diese Übung bereitet dich auf das Freitags-Projekt vor, bei dem du eine eigene Webseite mit HTML und CSS erstellst und deren HTTP-Kommunikation analysierst.

---

## Teil 1: Grundlagen verstehen

### Das Internet vs. World Wide Web

Viele Menschen verwenden diese Begriffe synonym, aber sie beschreiben unterschiedliche Dinge:

**Das Internet** ist die physische Infrastruktur - ein weltweites Netzwerk aus Kabeln, Routern und Servern, das verschiedene Dienste ermöglicht (E-Mail, VoIP, FTP, Web...).

**Das World Wide Web** ist ein Dienst, der auf dem Internet läuft - Webseiten, die über Browser zugänglich sind und durch Hyperlinks verbunden werden.

### Wissensfrage 1

Was ist der Hauptunterschied zwischen Internet und World Wide Web?

<details>
<summary>Antwort anzeigen</summary>

Das **Internet** ist die physische Infrastruktur (Kabel, Router, Server) - sozusagen die "Autobahn".

Das **World Wide Web** ist ein Dienst, der auf dieser Infrastruktur läuft - sozusagen eines der "Fahrzeuge" auf der Autobahn.

Weitere Dienste, die das Internet nutzen:
- E-Mail (SMTP, IMAP, POP3)
- Dateitransfer (FTP)
- Voice over IP (VoIP)
- Streaming-Dienste

</details>

---

## Teil 2: Client-Server-Architektur

### Das Grundprinzip

Bei jeder Webinteraktion gibt es zwei Rollen:

**Client (der "Fragende")**
- Initiiert die Kommunikation
- Beispiele: Browser, Mobile Apps, IoT-Geräte
- Sendet Anfragen (Requests)
- Empfängt und zeigt Antworten an

**Server (der "Antwortende")**
- Wartet auf Anfragen
- Beispiele: Apache, Nginx, Node.js
- Verarbeitet Anfragen
- Sendet Daten zurück

### Übung 1: Request-Kette verstehen

**Aufgabe:**

Beschreibe in eigenen Worten, was passiert, wenn du `https://www.google.com` in deinen Browser eingibst.

Versuche, mindestens 5 Schritte zu identifizieren.

**Hinweise:**
- Denke an DNS, TCP, HTTP
- Was macht der Browser zuerst?
- Was passiert, bevor die Seite angezeigt wird?

<details>
<summary>Musterlösung anzeigen</summary>

Der Weg einer Webanfrage:

1. **URL parsen** (~1ms)
   - Browser zerlegt die URL in ihre Bestandteile (Protokoll, Domain, Pfad)

2. **DNS-Auflösung** (~50ms)
   - Domain `www.google.com` wird in IP-Adresse übersetzt (z.B. 142.250.185.14)
   - Browser prüft erst lokalen Cache, dann DNS-Resolver

3. **TCP-Verbindung** (~30ms)
   - 3-Way-Handshake zwischen Client und Server
   - Verbindung wird aufgebaut

4. **TLS-Handshake** (~50ms)
   - Bei HTTPS: Verschlüsselung wird ausgehandelt
   - Server-Zertifikat wird überprüft

5. **HTTP-Request** (~5ms)
   - Browser sendet GET-Anfrage an den Server
   - Enthält Header wie User-Agent, Accept, etc.

6. **Server-Verarbeitung** (variabel)
   - Server verarbeitet die Anfrage
   - Bereitet die Antwort vor

7. **HTTP-Response** (~10ms)
   - Server sendet HTML-Dokument zurück
   - Status Code 200 OK

8. **Rendering** (~100ms)
   - Browser parst HTML
   - Lädt weitere Ressourcen (CSS, JS, Bilder)
   - Baut die Seite auf und zeigt sie an

**Gesamtzeit:** Ca. 200-500ms für eine typische Seite

</details>

---

## Teil 3: HTTP-Protokoll

### HTTP-Methoden

Die HTTP-Methode sagt dem Server, was mit einer Ressource passieren soll:

| Methode | Beschreibung | Beispiel | Safe? |
|---------|--------------|----------|-------|
| GET | Daten abrufen | Seite laden | Ja |
| POST | Neue Ressource erstellen | Formular absenden | Nein |
| PUT | Ressource vollständig ersetzen | Profil aktualisieren | Nein |
| PATCH | Ressource teilweise aktualisieren | Nur E-Mail ändern | Nein |
| DELETE | Ressource löschen | Account löschen | Nein |

**Safe** bedeutet: Die Methode ändert keine Daten auf dem Server.

### Wissensfrage 2

Du möchtest einen neuen Benutzer in einer Datenbank anlegen. Welche HTTP-Methode verwendest du?

<details>
<summary>Antwort anzeigen</summary>

**POST** - Diese Methode wird verwendet, um neue Ressourcen zu erstellen.

Der Request könnte so aussehen:
```
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Max Mustermann",
  "email": "max@example.com"
}
```

Der Server würde mit Status Code **201 Created** antworten, wenn der Benutzer erfolgreich angelegt wurde.

</details>

### HTTP Status Codes

Der Status Code sagt dir auf einen Blick, was passiert ist:

**2xx - Erfolg**
- 200 OK - Alles hat geklappt
- 201 Created - Neue Ressource wurde erstellt
- 204 No Content - Erfolgreich, aber keine Daten zurück

**3xx - Umleitung**
- 301 Moved Permanently - Dauerhaft umgezogen
- 302 Found - Temporär umgeleitet
- 304 Not Modified - Ressource unverändert (aus Cache)

**4xx - Client-Fehler (dein Fehler)**
- 400 Bad Request - Ungültige Anfrage
- 401 Unauthorized - Nicht authentifiziert
- 403 Forbidden - Keine Berechtigung
- 404 Not Found - Ressource nicht gefunden

**5xx - Server-Fehler (Serverproblem)**
- 500 Internal Server Error - Allgemeiner Serverfehler
- 502 Bad Gateway - Ungültige Antwort vom Backend
- 503 Service Unavailable - Server überlastet

### Übung 2: Status Codes zuordnen

**Aufgabe:**

Ordne folgende Szenarien dem richtigen Status Code zu:

1. Du rufst eine Seite auf, die nicht existiert
2. Du versuchst, auf einen geschützten Bereich zuzugreifen, ohne eingeloggt zu sein
3. Die Seite wurde erfolgreich geladen
4. Der Server hat einen Fehler und kann die Anfrage nicht verarbeiten
5. Du sendest ein Formular mit ungültigen Daten

<details>
<summary>Lösungen anzeigen</summary>

1. **404 Not Found** - Die angeforderte Ressource existiert nicht
2. **401 Unauthorized** - Authentifizierung erforderlich
3. **200 OK** - Erfolgreiche Anfrage
4. **500 Internal Server Error** - Server-seitiger Fehler
5. **400 Bad Request** - Ungültige Anfrage (oder 422 Unprocessable Entity)

**Merkhilfe:**
- 2xx = Alles OK
- 3xx = Woanders schauen
- 4xx = Du (Client) hast etwas falsch gemacht
- 5xx = Der Server hat ein Problem

</details>

---

## Teil 4: URLs verstehen

### Aufbau einer URL

```
https://www.example.com:443/path/page?query=value#section
```

| Teil | Bedeutung |
|------|-----------|
| `https://` | Protokoll (HTTP oder HTTPS) |
| `www.example.com` | Domain (Host) |
| `:443` | Port (optional, Standard: 80 für HTTP, 443 für HTTPS) |
| `/path/page` | Pfad zur Ressource |
| `?query=value` | Query-Parameter (Key=Value Paare) |
| `#section` | Fragment (Position auf der Seite, nur Client-seitig) |

### Übung 3: URL analysieren

**Aufgabe:**

Analysiere folgende URL und identifiziere alle Bestandteile:

```
https://shop.example.com:8080/products/electronics?category=phones&sort=price#reviews
```

<details>
<summary>Lösung anzeigen</summary>

| Bestandteil | Wert | Erklärung |
|-------------|------|-----------|
| Protokoll | `https://` | Verschlüsselte Verbindung |
| Domain | `shop.example.com` | Subdomain "shop" auf "example.com" |
| Port | `:8080` | Nicht-Standard-Port (nicht 443) |
| Pfad | `/products/electronics` | Ressource auf dem Server |
| Query-Parameter 1 | `category=phones` | Filter nach Kategorie |
| Query-Parameter 2 | `sort=price` | Sortierung nach Preis |
| Fragment | `#reviews` | Springe zum Reviews-Abschnitt |

**Hinweis:** Query-Parameter werden mit `?` eingeleitet und mit `&` getrennt. Das Fragment wird NICHT an den Server gesendet - es wird nur vom Browser verwendet!

</details>

---

## Teil 5: DNS verstehen

### Was ist DNS?

DNS (Domain Name System) ist wie das "Telefonbuch des Internets". Computer verstehen nur IP-Adressen (z.B. 142.250.185.14), aber wir Menschen merken uns lieber Namen (z.B. google.com).

DNS übersetzt: `www.google.com` → `142.250.185.14`

### Der DNS-Ablauf

1. Browser prüft lokalen Cache
2. Anfrage an DNS-Resolver (meist vom Internetanbieter)
3. Resolver fragt: Root-Server → TLD-Server (.com) → Autoritativer Server
4. IP-Adresse wird zurückgegeben
5. Browser speichert Ergebnis im Cache (TTL = Time To Live)

### Wissensfrage 3

Warum wird die zweite Anfrage an die gleiche Domain oft schneller geladen?

<details>
<summary>Antwort anzeigen</summary>

Wegen **DNS-Caching**!

Nach der ersten DNS-Auflösung speichert:
- Der Browser die IP-Adresse
- Das Betriebssystem die IP-Adresse
- Der DNS-Resolver die IP-Adresse

Bei der zweiten Anfrage wird die IP-Adresse aus dem Cache gelesen, ohne den gesamten DNS-Prozess zu wiederholen.

Die **TTL (Time To Live)** bestimmt, wie lange der Cache gültig ist. Typische Werte: 300 Sekunden (5 Minuten) bis 86400 Sekunden (1 Tag).

**Terminal-Befehle zum Testen:**
- Windows: `nslookup google.com`
- Mac/Linux: `dig google.com`

</details>

---

## Teil 6: Praktische Übung mit DevTools

### Vorbereitung

Öffne deinen Browser und die DevTools:
- **Windows/Linux:** F12 oder Strg+Shift+I
- **Mac:** Cmd+Option+I

Wechsle zum **Network Tab**.

### Übung 4: HTTP-Kommunikation analysieren

**Aufgabe:**

1. Öffne die DevTools (F12) und gehe zum Network Tab
2. Aktiviere "Preserve log" (damit Requests erhalten bleiben)
3. Rufe eine beliebige Website auf (z.B. `https://example.com`)
4. Beantworte folgende Fragen:

**Frage 1:** Wie viele HTTP-Requests wurden ausgelöst?

**Frage 2:** Was ist die HTTP-Methode des ersten Requests?

**Frage 3:** Welchen Status Code hat der erste Request?

**Frage 4:** Welchen Content-Type hat die Antwort?

**Frage 5:** Findest du einen Request mit Status 304? Was bedeutet das?

<details>
<summary>Hinweise zur Lösung</summary>

**Frage 1:** Die Anzahl siehst du unten im Network Tab (z.B. "15 requests")

**Frage 2:** Klicke auf den ersten Request und schaue im "Headers" Tab unter "Request Method" (sollte GET sein)

**Frage 3:** Steht in der Spalte "Status" (sollte 200 sein)

**Frage 4:** Im "Headers" Tab unter "Response Headers" bei "Content-Type" (z.B. "text/html")

**Frage 5:** Status 304 = "Not Modified" - der Browser hat die Ressource aus dem Cache verwendet, weil sie sich nicht geändert hat

**Pro-Tipps:**
- Filter nach Typ: Doc, CSS, JS, Img, etc.
- Klicke auf "Initiator" um zu sehen, was den Request ausgelöst hat
- Der "Timing" Tab zeigt die Ladezeit-Aufschlüsselung

</details>

### Übung 5: Request-Details verstehen

**Aufgabe:**

Analysiere einen beliebigen Request im Network Tab genauer:

1. Klicke auf einen Request
2. Gehe zum "Headers" Tab
3. Notiere dir:
   - Request URL
   - Request Method
   - Status Code
   - Mindestens 3 Request Headers
   - Mindestens 3 Response Headers

<details>
<summary>Beispiel-Analyse</summary>

**Request URL:** `https://example.com/`

**Request Method:** GET

**Status Code:** 200 OK

**Request Headers (Beispiele):**
| Header | Wert | Bedeutung |
|--------|------|-----------|
| Host | example.com | Ziel-Server |
| User-Agent | Mozilla/5.0... | Browser-Identifikation |
| Accept | text/html,application/xhtml+xml | Akzeptierte Formate |
| Accept-Language | de-DE,de;q=0.9 | Bevorzugte Sprache |
| Accept-Encoding | gzip, deflate, br | Akzeptierte Komprimierung |

**Response Headers (Beispiele):**
| Header | Wert | Bedeutung |
|--------|------|-----------|
| Content-Type | text/html; charset=UTF-8 | Format der Antwort |
| Content-Length | 1256 | Größe in Bytes |
| Cache-Control | max-age=604800 | Caching für 7 Tage |
| Date | Mon, 01 Jan 2024 12:00:00 GMT | Server-Zeit |

</details>

---

## Teil 7: REST APIs verstehen

### Was ist REST?

REST (Representational State Transfer) ist ein Architekturstil für Web-APIs. Es nutzt HTTP optimal:

- **Ressourcen-basiert:** Alles ist eine Ressource mit eindeutiger URL
- **HTTP-Methoden:** GET, POST, PUT, DELETE für CRUD-Operationen
- **Zustandslos:** Jede Anfrage enthält alle nötigen Informationen
- **JSON als Standard:** Leichtgewichtiges Datenformat

### CRUD-Operationen

| Operation | HTTP-Methode | Beispiel-URL | Beschreibung |
|-----------|--------------|--------------|--------------|
| Create | POST | `/api/users` | Neuen User erstellen |
| Read | GET | `/api/users` | Alle User abrufen |
| Read | GET | `/api/users/1` | User mit ID 1 abrufen |
| Update | PUT | `/api/users/1` | User 1 aktualisieren |
| Delete | DELETE | `/api/users/1` | User 1 löschen |

### Wissensfrage 4

Du möchtest alle Produkte aus einer REST API abrufen. Welche HTTP-Methode und welchen Endpunkt verwendest du?

<details>
<summary>Antwort anzeigen</summary>

**Methode:** GET

**Endpunkt:** `/api/products`

Der vollständige Request:
```
GET /api/products HTTP/1.1
Host: api.example.com
Accept: application/json
```

Die Antwort könnte so aussehen:
```json
[
  { "id": 1, "name": "Laptop", "price": 999.99 },
  { "id": 2, "name": "Mouse", "price": 29.99 },
  { "id": 3, "name": "Keyboard", "price": 79.99 }
]
```

</details>

---

## Zusammenfassung

### Was du gelernt hast:

| Thema | Key Takeaway |
|-------|--------------|
| Internet vs. Web | Internet = Infrastruktur, Web = Dienst darauf |
| Client-Server | Client fragt, Server antwortet |
| HTTP-Methoden | GET liest, POST erstellt, PUT aktualisiert, DELETE löscht |
| Status Codes | 2xx = OK, 4xx = Client-Fehler, 5xx = Server-Fehler |
| URLs | Protokoll + Domain + Pfad + Query + Fragment |
| DNS | Übersetzt Domain-Namen in IP-Adressen |
| DevTools | Network Tab für HTTP-Analyse |

### Vorbereitung auf morgen

Morgen lernst du **HTML** - die Sprache, die der Server als Response schickt. Du wirst verstehen:
- Wie ein HTML-Dokument aufgebaut ist
- Dass HTML weitere Requests auslöst (CSS, Bilder, JS)
- Wie Formulare Daten an den Server senden

Die DevTools-Kenntnisse von heute wirst du morgen wieder brauchen!

---

## Bonus: Selbsttest

Beantworte diese Fragen, um dein Wissen zu prüfen:

1. Was ist der Unterschied zwischen HTTP und HTTPS?
2. Welchen Status Code erhältst du, wenn eine Seite nicht gefunden wird?
3. Was macht DNS?
4. Welche HTTP-Methode ist "safe"?
5. Wo siehst du im Browser, welche HTTP-Requests eine Seite auslöst?

<details>
<summary>Antworten anzeigen</summary>

1. **HTTPS** ist die verschlüsselte Version von HTTP. Es verwendet TLS/SSL, um die Kommunikation zu sichern. Port 80 (HTTP) vs. Port 443 (HTTPS).

2. **404 Not Found** - Die angeforderte Ressource existiert nicht.

3. **DNS** übersetzt menschenlesbare Domain-Namen (google.com) in IP-Adressen (142.250.185.14).

4. **GET** (und HEAD) sind "safe" - sie ändern keine Daten auf dem Server.

5. In den **Browser DevTools** im **Network Tab** (F12).

</details>
