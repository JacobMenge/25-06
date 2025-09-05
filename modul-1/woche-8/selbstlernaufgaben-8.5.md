# Selbstlernaufgaben - Recap Woche 8: Server-Infrastruktur & Kommunikation

**Abgabe:** Bis spätestens **Sonntag um 23:59 Uhr im Google Classroom**

Diese Aufgaben wiederholen und vertiefen die Grundlagen aus Woche 8 durch einfache Recherche und Verständnisfragen.

---

## 1. Grundlagenaufgabe - Servertypen verstehen

**Benötigte Skills:** Grundlagen aus den Folien + einfache Recherche

### **Deine Aufgabe:**

Beantworte die folgenden Fragen zu den 5 wichtigsten Servertypen:

#### **Teil A: Definitionen (aus den Folien)**
Erkläre in **1-2 Sätzen**, was diese Server machen:

1. **Webserver:** _____
2. **Mailserver:** _____
3. **Fileserver:** _____
4. **Datenbankserver:** _____
5. **DNS-Server:** _____

#### **Teil B: Alltags-Zuordnung**
Welcher Server ist hauptsächlich beteiligt, wenn du...

| Aktivität | Servertyp | Kurze Begründung |
|-----------|-----------|------------------|
| Eine Website aufrufst (z.B. google.de) | | |
| Eine E-Mail sendest | | |
| Ein Foto in der iCloud speicherst | | |
| Nach einem Kontakt in einer App suchst | | |
| www.amazon.de im Browser eingibst | | |

#### **Teil C: Einfache Recherche**
Finde heraus und notiere:

1. **Welche 3 Webserver** wurden in der Vorlesung genannt?
   - _____, _____, _____

2. **Welche 2 Hauptaufgaben** hat ein Mailserver?
   - _____
   - _____


**Format:** Einfache Liste oder Tabelle als PDF/Word-Dokument

---

## 2. Grundlagenaufgabe - Client-Server-Kommunikation verstehen

**Benötigte Skills:** TCP/IP-Grundlagen aus den Folien

### **Deine Aufgabe:**

#### **Teil A: Client-Server-Prinzip**
1. **Erkläre den Unterschied:**
   - **Client:** _____
   - **Server:** _____

2. **Ordne zu (Client oder Server):**
   - Dein Browser: _____
   - WhatsApp auf deinem Handy: _____
   - Google's Computer: _____
   - Instagram-App: _____
   - Facebook's Rechenzentrum: _____

#### **Teil B: TCP/IP-Stack (aus den Folien)**
Die 4 Schichten wurden mit dem **Postsystem** verglichen. Ergänze:

| Schicht | Name | Postsystem-Vergleich | Beispiel |
|---------|------|---------------------|----------|
| 4 | Anwendungsschicht | "Ich schreibe einen Brief" | Browser, WhatsApp |
| 3 | ___schicht | "Brief kommt in ___ mit Adresse" | TCP/UDP + ___ |
| 2 | ___schicht | "Postbote plant die ___" | ___-Adresse |
| 1 | ___schicht | "Brief wird transportiert" | WLAN, ___ |

#### **Teil C: Ports verstehen**
1. **Warum gibt es Ports?** (Gebäude-Analogie aus der Vorlesung)
   - Server = _____
   - Ports = _____

2. **Vervollständige die wichtigsten Ports:**
   - Port 80: _____ (unverschlüsselt)
   - Port 443: _____ (verschlüsselt)
   - Port 25: _____ 
   - Port 22: _____
   - Port 53: _____

#### **Teil D: HTTP vs HTTPS**
1. **Erkläre den Unterschied:**
   - HTTP = _____
   - HTTPS = _____

2. **Woran erkennst du HTTPS im Browser?**
   - _____
   - _____

**Format:** Ausgefüllte Tabellen + kurze Antworten

---

## 3. Grundlagenaufgabe - Webserver-Grundlagen

**Benötigte Skills:** Webserver-Grundlagen aus den Folien + Recherche

### **Deine Aufgabe:**

#### **Teil A: Webserver-Software vergleichen**
Fülle die Tabelle aus (nutze die Folien + einfache Recherche):

| Webserver | Entwickelt seit | Stärke | Wann verwenden? |
|-----------|----------------|--------|-----------------|
| **Apache** | | Der _____ | |
| **Nginx** | | Der _____ | |
| **IIS** | | Von _____ | |

#### **Teil B: DocumentRoot verstehen**
Gegeben: DocumentRoot = `/var/www/html/`

Vervollständige die URL-zu-Pfad-Zuordnung:

| URL | Dateipfad auf Server |
|-----|---------------------|
| `http://beispiel.de/` | `/var/www/html/_____` |
| `http://beispiel.de/kontakt.html` | |
| `http://beispiel.de/bilder/logo.png` | |
| `http://beispiel.de/news/` | |


#### **Teil C: Einfache Recherche**
1. **Finde heraus:** Welcher Webserver läuft auf diesen bekannten Websites?
   *Hinweis: Suche nach "nginx vs apache market share" oder nutze Tools wie builtwith.com*
   
   - Wikipedia: _____
   - Netflix: _____
   - WordPress.com: _____

2. **Was bedeutet "404 Not Found"?**
   - _____

**Format:** Ausgefüllte Tabellen + kurze Recherche-Ergebnisse

---

## 4. Vertiefungsaufgabe - Hardware vs. Software & Cloud vs. On-Premise

**Benötigte Skills:** Server-Arten aus den Folien + Recherche

### **Deine Aufgabe:**

#### **Teil A: Hardware vs. Software-Server**
Vervollständige den Vergleich:

| Aspekt | Hardware-Server | Software-Server |
|--------|----------------|-----------------|
| **Was ist das?** | Echter Computer zum _____ | Programme die auf _____ laufen |
| **Wie die Smartphone-Analogie?** | Das Smartphone selbst | Die _____ auf dem Smartphone |
| **Hauptvorteil** | | |
| **Hauptnachteil** | | |

#### **Teil B: Cloud vs. On-Premise**
1. **Vervollständige die Auto-Analogie aus den Folien:**
   - **On-Premise** = Eigenes _____
   - **Cloud** = _____

2. **Entscheidungshilfe - Welche Lösung passt?**
   
   **Szenario A:** Kleines Startup, 5 Mitarbeiter, wenig Budget, will schnell wachsen
   - **Empfehlung:** _____ 
   - **Warum:** _____

   **Szenario B:** Bank mit sensiblen Kundendaten, hohe Sicherheitsanforderungen
   - **Empfehlung:** _____
   - **Warum:** _____

   **Szenario C:** Online-Shop, schwankende Besucherzahlen (mal 100, mal 10.000 gleichzeitig)
   - **Empfehlung:** _____
   - **Warum:** _____

#### **Teil C: Cloud-Anbieter Recherche**
Recherchiere die **3 großen Cloud-Anbieter** und fülle aus:

| Anbieter | Vollständiger Name | Land | Eine bekannte Firma die es nutzt |
|----------|-------------------|------|----------------------------------|
| AWS | | | |
| **Azure** | | | |
| **GCP** | | | |

**Format:** Tabellen + kurze Begründungen für Szenarien

---

## 5. Anwendungsaufgabe - Request-Response verstehen

**Benötigte Skills:** HTTP-Grundlagen aus den Folien

### **Deine Aufgabe:**

#### **Teil A: Request-Response-Ablauf**
Du gibst `www.youtube.com` in deinen Browser ein. Beschreibe Schritt für Schritt:

1. **Schritt 1:** Browser macht einen _____ an den Server
2. **Schritt 2:** Server sendet _____ zurück  
3. **Schritt 3:** Browser macht das _____ (Rendering)
4. **Schritt 4:** Du siehst _____

#### **Teil B: HTTP-Methoden zuordnen**
Welche HTTP-Methode wird verwendet?

| Aktivität | HTTP-Methode | Begründung |
|-----------|--------------|------------|
| Instagram-Feed aufrufen | | |
| Foto auf Instagram posten | | |
| Profil-Info ändern | | |
| Post löschen | | |
| YouTube-Video anschauen | | |

#### **Teil C: Alltags-Beispiel analysieren**
Wähle eine Website die du oft nutzt (z.B. Instagram, YouTube, Amazon) und beantworte:

1. **Website:** _____
2. **Wie viele verschiedene Requests sendet dein Browser ungefähr?**
   *Hinweis: Denk an HTML, CSS, Bilder, Videos...*
   - Antwort: _____

3. **Was passiert, wenn der Server offline ist?**
   - _____

4. **Warum lädt die Seite manchmal langsam?**
   - Mögliche Gründe: _____, _____, _____

**Format:** Schritt-für-Schritt-Liste + ausgefüllte Tabelle

---

## 6. Bonus-Aufgabe - SSH Grundlagen verstehen (freiwillig)

**Benötigte Skills:** SSH-Folien verstehen

### **Deine Aufgabe:**

#### **Teil A: SSH verstehen**
1. **Was bedeutet SSH?**
   - SSH = _____ _____ _____

2. **Wofür wird SSH verwendet?** (4 Einsatzgebiete aus den Folien)
   - _____
   - _____
   - _____
   - _____

#### **Teil B: SSH-Sicherheit**
1. **Welche 4 Sicherheitsziele hat SSH?**
   - _____ → Verschlüsselung schützt Daten vor _____
   - _____ → Prüfsummen verhindern _____
   - _____ → Identität wird _____
   - _____-_____ → Schlüsselbasierte Anmeldung

2. **Was ist sicherer und warum?**
   - **Passwort-Authentifizierung:** _____
   - **SSH-Keys:** _____
   - **Warum sind SSH-Keys besser?** _____

#### **Teil C: SSH-Keys verstehen**
1. **Was ist ein SSH-Key-Paar?**
   - **Privater Schlüssel:** _____
   - **Öffentlicher Schlüssel:** _____

2. **Welcher SSH-Key-Typ wird in der Vorlesung empfohlen?**
   - Antwort: _____
   - **Befehl zum Erstellen:** _____

**Format:** Einfache Liste mit Antworten

---

Hier noch ein paar hilfreiche Videos, falls euch zwischendurch langweilig wird: 

CLIENT-SERVER-MODELL (einfach erklärt)
https://www.youtube.com/watch?v=fZdwOm-6rvs

Die Client-Server-Architektur
https://www.youtube.com/watch?v=N3JlH4HCzXU

* As A Service - Die Grundbegriffe des Cloud Computing
https://www.youtube.com/watch?v=alYIYtIxIVE

Netzwerkprotokolle erklärt: HTTP, FTP, SMTP & DNS
https://www.youtube.com/watch?v=LwYDKiwInm0

SSH Zugang einrichten
https://www.youtube.com/watch?v=hRsKjWgRFac&t=70s-+

SSH einfach erklärt | #Netzwerktechnik
https://www.youtube.com/watch?v=4xcQk6b8RB8
