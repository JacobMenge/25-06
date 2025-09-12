# Networking-Tools – Selbstlernaufgaben

Dieses Übungsblatt führt dich **schrittweise** durch vier zentrale Netzwerk-Tools auf Linux/Unix-Systemen.  
Ziel: **Grundverständnis** + **sichere, kleine Praxisaufgaben** + **Reflexion**.  
Schwierigkeit: **leicht bis mittel**. Umfang: **viele kleine Schritte**, alle gut machbar.

---

## Voraussetzungen (kurz prüfen)
- Du arbeitest auf **Linux** (Ubuntu/Debian empfohlen). macOS-Hinweise stehen jeweils dabei.
- Installiert: `iproute2`, `net-tools`, `curl`, `wget`, `nmap`, `ncat` (oder `nc`), `procps` (für `watch`), `dnsutils` (für `dig`).  
  ```bash
  # Ubuntu/Debian
  sudo apt update && sudo apt install -y iproute2 net-tools curl wget nmap ncat procps dnsutils
  ```
- **Root-Rechte** (per `sudo`) sind **nicht immer** nötig. Wenn ein Befehl Root erfordert, steht es explizit dabei.
- **macOS-Alternativen**:
  - `ss` gibt es nicht → nutze `netstat -an` oder `lsof -iTCP -sTCP:LISTEN -n -P`
  - `watch` ggf. via Homebrew installieren oder per `while sleep`-Loop ersetzen
  - `md5sum` heißt `md5`

---

## Mini-Glossar (die wichtigsten Begriffe)
- **Socket**: Endpunkt einer Netzwerkkommunikation (z. B. `127.0.0.1:80`).
- **Port**: Nummer zur Adressierung eines Dienstes (z. B. 22=SSH, 80=HTTP).
- **TCP**: verbindungsorientiert (Handshake, Zustände wie `LISTEN`, `ESTABLISHED`).
- **UDP**: verbindungslos (kein Handshake, oft `UNCONN` statt `LISTEN`).
- **Prozess (PID)**: laufendes Programm (z. B. `sshd`), eindeutige Prozess-ID.
- **HTTP**: Protokoll fürs Web; **Request** (Client) ↔ **Response** (Server).
- **Status-Codes**: `200 OK`, `301 Moved Permanently`, `404 Not Found`, `500 Internal Server Error`.
- **TLS/HTTPS**: Verschlüsselte Variante von HTTP (sicherer Transport).
- **Nmap**: Portscanner (nur legal/autorisiert einsetzen!).
- **Netcat (ncat/nc)**: „Schweizer Taschenmesser“ für TCP/UDP (Chat, Porttests, Dateiübertragung).

---

# Grundlagenaufgabe 1: Netzwerkverbindungen beobachten (`ss` / `netstat`)

### Lernziele
- Du erkennst aktive Verbindungen und lauschende Ports.
- Du verstehst die wichtigsten `ss`-Optionen und TCP-Zustände.
- Du kannst die Ausgabe lesen und kurz interpretieren.

### Theorie kompakt
- **Warum `ss`?** Modernes Tool zum Anzeigen von Sockets/Verbindungen. Alternativ: `netstat` (älter).
- **Wichtige `ss`-Optionen**:  
  `-t` (TCP), `-u` (UDP), `-l` (listening/gebunden), `-n` (numerisch, keine DNS-Namen), `-p` (Prozessname/PID – oft nur mit `sudo`), `-a` (alle).
- **TCP-Zustände**:  
  `LISTEN` (wartet auf Verbindungen), `SYN-SENT`/`SYN-RECV` (Handshake), `ESTABLISHED` (Datenfluss), `TIME-WAIT`/`CLOSE-WAIT` (Abbauphase).  
  **UDP** hat keine „Verbindung“ → oft `UNCONN` (unconnected).

### Schritte

1) **Ist `ss` verfügbar?**  
   ```bash
   ss --version
   ```
   ➤ Bedeutung: Prüft Tool & Version.  
   ✍️ Notiere: Version/Ausgabe.

2) **Nur TCP-Verbindungen anzeigen**  
   ```bash
   ss -t
   ```
   ➤ Bedeutung: Filter auf TCP.  
   ✍️ Frage: Welche Zustände siehst du (z. B. `LISTEN`, `ESTABLISHED`)?

3) **TCP numerisch (ohne DNS-Auflösung)**  
   ```bash
   ss -tn
   ```
   ➤ Warum? Schneller & eindeutiger (IP/Port statt Namen).  
   ✍️ Notiere eine Zeile mit `lokale IP:Port`, `remote IP:Port`, `State`.

4) **Lauschende Ports (TCP+UDP) numerisch**  
   ```bash
   ss -tuln
   ```
   ➤ Bedeutung: Zeigt, welche Ports offen sind und auf Verbindungen warten.  
   ✍️ Frage: Lauscht etwas auf Port **22** (SSH) oder **80/443** (HTTP/HTTPS)?

5) **Prozesse zu Ports anzeigen (Root)**  
   ```bash
   sudo ss -tulnp
   ```
   ➤ Bedeutung: `-p` zeigt PID/Prozess (z. B. `sshd`).  
   ✍️ Notiere 1–2 Einträge: Port → Prozessname/PID.

6) **(Optional) Vergleich mit `netstat`**  
   ```bash
   netstat -tuln
   ```
   ➤ Bedeutung: Ähnlicher Blick, andere Formatierung.  
   ✍️ Kurzvergleich: Welche Unterschiede fallen dir auf?

Screenshot (am Ende der Aufgabe): Ausgabe von Schritt 4 **oder** 5.

---

# Grundlagenaufgabe 2: Webseiten testen (`curl` & `wget`)

### Lernziele
- Du verstehst den Aufbau von HTTP-Anfrage/Antwort.
- Du kannst eine Seite abrufen und Header lesen.
- Du kennst die Rollen: `curl` (Anfragen/Debug) vs. `wget` (Downloads).

### Theorie kompakt
- **HTTP-Request**: Startzeile (`GET / HTTP/1.1`), Header (z. B. `Host`), Leerzeile, ggf. Body.  
- **HTTP-Response**: Statuszeile (`HTTP/1.1 200 OK`), Header (z. B. `Content-Type`), Leerzeile, Body (HTML/JSON).  
- **`curl`**: ideal für APIs & Debug (`-v`, `-I`, `-H`, `-d`).  
- **`wget`**: ideal für robuste Downloads/Spiegelungen (`-O`, `--tries`, `--wait`).

### Schritte

1) **Seite abrufen (Body ansehen)**  
   ```bash
   curl https://example.com
   ```
   ➤ Bedeutung: Zeigt HTML-Quelltext.  
   ✍️ Frage: Welcher Titel steht im `<title>`?

2) **Nur Header abrufen (Status & Metadaten)**  
   ```bash
   curl -I https://example.com
   ```
   ➤ Bedeutung: `-I` = HEAD-Request (nur Header).  
   ✍️ Fragen: Welcher Status-Code? Welcher Content-Type?

3) **Verbose-Modus (Details/Handshake/Redirects)**  
   ```bash
   curl -v https://httpbin.org/get
   ```
   ➤ Bedeutung: `-v` zeigt Request/Response-Zeilen (`>`, `<`) & interne Hinweise (`*`).  
   ✍️ Notiere 2 Dinge, die du hier zusätzlich siehst.

4) **Download mit `wget` (Datei speichern)**  
   ```bash
   wget https://example.com -O test.html
   ls -lh test.html
   ```
   ➤ Bedeutung: `-O` = Dateiname. `ls -lh` = Größe anzeigen.  
   ✍️ Frage: Wie groß ist die Datei?

5) **Kleiner Speedtest (Zeit messen)**  
   ```bash
   time wget -q https://example.com -O speedtest.html
   ```
   ➤ Bedeutung: Grober Zeitvergleich.  
   ✍️ Notiere: Gemessene Zeit.

Screenshot (am Ende der Aufgabe): Deine `curl -I` Ausgabe und `ls -lh test.html`.

---

# Weiterführende Aufgabe 3: Offene Ports finden (`nmap`)

### Lernziele
- Du scannst nur deinen eigenen Rechner (legal & sicher).
- Du liest einfache nmap-Ausgaben (Port → Service).
- Du verstehst Unterschiede von Scan-Typen auf hoher Ebene.

### Theorie kompakt
- **Rechtliches:** Scanne nur Systeme, für die du Erlaubnis hast (hier: `localhost`).  
- **Scan-Arten:**  
  - `-sT` (Connect-Scan): echte Verbindungen, kein Root nötig.  
  - `-sS` (SYN-Scan): schneller/leiser; Root empfohlen.  
  - `-sU` (UDP): langsam/schwierig; Root empfohlen.  
- **Standard-Scan:** ohne Optionen → 1000 häufige TCP-Ports.

### Schritte

1) **Version prüfen**  
   ```bash
   nmap --version
   ```
   ➤ Bedeutung: Prüft Installation.  
   ✍️ Notiz: Version.

2) **Standard-Scan auf localhost**  
   ```bash
   nmap localhost
   ```
   ➤ Bedeutung: Checkt die häufigsten TCP-Ports.  
   ✍️ Frage: Welche Ports sind open?

3) **Kleiner Portbereich**  
   ```bash
   nmap -p 1-100 localhost
   ```
   ➤ Bedeutung: Nur Ports 1–100.  
   Screenshot: Ausgabe sichern.

4) **Einfache Diensterkennung**  
   ```bash
   nmap -sV localhost
   ```
   ➤ Bedeutung: Versucht Service/Version zu erkennen.  
   ✍️ Frage: Welcher Dienst wurde erkannt?

5) **(Optional) SYN-Scan mit Root**  
   ```bash
   sudo nmap -sS localhost
   ```

Interpretieren: `open`, `closed`, `filtered`.

---

# Weiterführende Aufgabe 4: Chatten im Terminal (`netcat`)

### Lernziele
- Du baust eine einfache Verbindung zwischen zwei Terminals auf.
- Du verstehst, was ein TCP-Listener ist und was ein Client ist.
- Du probierst Mehrbenutzer-Chat aus.

### Theorie kompakt
- **Netcat:** liest/schreibt Bytes über TCP/UDP.  
- **Server/Listener:** wartet auf Verbindungen (z. B. `-l 12345`).  
- **Client:** verbindet sich (`localhost 12345`).  
- **Varianten:** `ncat` (modern), `nc` (BSD).

### Schritte

1) **Server starten (Terminal 1)**  
   ```bash
   ncat -l 12345
   ```

2) **Client verbinden (Terminal 2)**  
   ```bash
   ncat localhost 12345
   ```

3) **Nachricht austauschen**  
   ✍️ Frage: Erscheint die Client-Nachricht im Server-Terminal?

4) **Antwort vom Server**  
   Screenshot: Zeige 1–2 Zeilen Chatverlauf.

5) **(Optional) Mehrere Clients**  
   ```bash
   ncat -l --keep-open --broker 12346
   ncat localhost 12346
   ncat localhost 12346
   ```

---

# Weiterführende Aufgabe 5: Mini-Integration – Webserver testen

### Lernziele
- Du startest einen kleinen lokalen Webserver.
- Du testest ihn mit `curl` und beobachtest Verbindungen mit `ss`.
- Du erkennst den Zusammenhang zwischen Server, Client, Port.

### Theorie kompakt
- **`python3 -m http.server <port>`** startet einfachen Webserver.
- **`curl`** testet ihn.
- **`ss`** zeigt lauschende Ports und aktive Verbindungen.

### Schritte

1) **Testordner & Datei erstellen**  
   ```bash
   mkdir -p webtest && cd webtest
   printf "<h1>Hallo Netzwerk</h1>\n" > index.html
   ls -l
   ```

2) **Webserver starten (Port 8000)**  
   ```bash
   python3 -m http.server 8000
   ```

3) **Neues Terminal öffnen: Verbindung prüfen**  
   ```bash
   curl -I http://localhost:8000/
   curl http://localhost:8000/
   ```

4) **Lauschende Ports & Verbindungen beobachten**  
   ```bash
   ss -tuln | grep 8000
   ss -t state established | grep 8000 || true
   ```

5) **Kleiner nmap-Check (nur Port 8000)**  
   ```bash
   nmap -p 8000 -sV localhost
   ```

6) **Aufräumen**  
   ```bash
   cd ..
   rm -rf webtest
   ```

---


## Troubleshooting

- **`command not found`** → Paket installieren (siehe Voraussetzungen).
- **Keine Prozesse bei `ss -p`** → mit `sudo` erneut probieren.
- **`curl` zeigt nichts oder „Connection refused“** → läuft der Server? Richtiger Port?
- **`nmap` dauert lange** → kleiner Portbereich, `localhost`, kein `-A`/`-sU`.
- **`ncat`/`nc` Chat geht nicht** → Port schon belegt? Anderen Port nehmen (z. B. 12346).

---

