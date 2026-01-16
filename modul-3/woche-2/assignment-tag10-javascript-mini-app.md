# Optionales Assignment: JavaScript Mini-App (Einzelarbeit)

## Wochenabschluss: Webentwicklung Grundlagen II

### Organisatorische Rahmenbedingungen

**Dieses Assignment ist freiwillig!** Es dient der Vertiefung der Woche und kann eingereicht werden, falls ihr Feedback von uns wünscht.

Falls du abgeben möchtest, reiche folgende Dateien ein (bis Montag, 23:59 Uhr):

- `index.html` - Deine HTML-Datei
- `style.css` - Dein CSS-Stylesheet
- `app.js` - Dein JavaScript-Code
- `README.md` - Kurze Dokumentation (ca. 5-10 Sätze oder Stichpunkte)

Der thematische Umfang dieser Aufgabe erstreckt sich über die Grundlagen der Woche:
- JavaScript Fundamentals (const/let, Arrow Functions, Template Literals)
- Arrays & Objects (map, filter, Spread, Destructuring)
- DOM Manipulation & Events
- Fetch API & Async/Await

---

## Abgabe (optional)

Packe deine Dateien in einen Ordner und lade ihn hoch:

```
vorname_nachname_woche2/
    index.html
    style.css
    app.js
    README.md
```

**Hinweis:** Falls kein Ordner-Upload möglich ist, komprimiere den Ordner als ZIP-Datei.

---

## Hinweis zur Nutzung von KI-Tools

**Die Nutzung von KI-Tools (wie ChatGPT, Claude, Copilot) ist erlaubt!**

**Wichtige Bedingungen:**
- Du musst **jeden Code, den eine KI generiert hat, vollständig verstehen**
- Du solltest in der Lage sein, **jede Zeile deines Codes zu erklären**
- Bei Rückfragen musst du erklären können, was der Code macht und warum

**Tipp:** Wenn du KI nutzt, frage sie auch, dir den Code zu erklären!

---

## Zielsetzung der Aufgabe

Mit diesem Assignment zeigst du, dass du die wichtigsten JavaScript-Grundlagen verstanden hast. Es geht darum, eine **einfache, funktionierende Mini-App** zu erstellen, die Daten von einer API lädt und interaktiv ist.

**Wichtig:** Eine einfache, funktionierende App ist besser als eine komplexe, fehlerhafte!

Du hast die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Thema (Kreativ)

Erstelle eine Mini-App zu einem Thema deiner Wahl, die Daten von einer öffentlichen API lädt.

### Mindestanforderungen:

**JavaScript:**
- Verwende `const` und `let` korrekt
- Mindestens eine Arrow Function
- Mindestens ein Template Literal
- Verwende `async/await` für den API-Aufruf
- Error Handling mit `try/catch`

**Arrays/Objects:**
- Verwende mindestens eine Array-Methode (`map`, `filter` oder `find`)
- Nutze Destructuring an mindestens einer Stelle

**DOM & Events:**
- Mindestens ein Event Listener (z.B. Button-Klick oder Formular-Submit)
- DOM-Manipulation (Inhalte dynamisch anzeigen)
- Loading-State anzeigen während Daten laden

**Struktur:**
- HTML, CSS und JavaScript in separaten Dateien
- Sauberer, lesbarer Code mit Kommentaren

### Kostenlose APIs für Ideen:

| API | URL | Beschreibung |
|-----|-----|--------------|
| JSONPlaceholder | `https://jsonplaceholder.typicode.com/posts` | Fake Blog-Posts & User |
| wttr.in | `https://wttr.in/Berlin?format=j1` | Wetterdaten |
| Random User | `https://randomuser.me/api/?results=5` | Zufällige User-Profile |
| Cat Facts | `https://catfact.ninja/facts?limit=5` | Katzen-Fakten |
| Dog API | `https://dog.ceo/api/breeds/image/random/5` | Hunde-Bilder |
| Pokemon API | `https://pokeapi.co/api/v2/pokemon?limit=20` | Pokemon-Daten |

> **Hinweis:** Falls eine API in eurem Netzwerk (z.B. Firmen-Firewall) blockiert ist, probiert eine Alternative aus der Liste. JSONPlaceholder funktioniert fast immer!

### Ideen für Apps:

- **Wetter-App:** Stadt eingeben, Wetter anzeigen
- **User-Verzeichnis:** Zufällige User laden und filtern
- **Blog-Reader:** Posts laden, nach Titel suchen
- **Pokemon-Finder:** Pokemon laden und nach Name filtern
- **Zitat-Generator:** Zufällige Zitate anzeigen

---

## Weg B: Geführte Aufgabe (Schritt für Schritt)

Falls du lieber einer Anleitung folgen möchtest, baue diese **User-Verzeichnis-App**.

### Was wir bauen:

Eine App, die:
1. User von einer API lädt
2. Die User in einer Liste anzeigt
3. Nach Namen filtern kann
4. Loading- und Error-States hat

**Am Ende hast du automatisch alle Anforderungen erfüllt!**

---

### Schritt 1: HTML-Grundgerüst erstellen

Erstelle eine Datei `index.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Verzeichnis</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <header>
            <h1>User Verzeichnis</h1>
            <p id="status">Bereit</p>
        </header>

        <main>
            <!-- Suchfeld -->
            <div id="search-section">
                <input
                    type="text"
                    id="search-input"
                    placeholder="Nach Namen suchen..."
                >
                <button id="load-btn">User laden</button>
            </div>

            <!-- Hier werden die User angezeigt -->
            <div id="user-list">
                <p class="placeholder">Klicke "User laden" um zu starten.</p>
            </div>
        </main>
    </div>

    <script src="app.js" defer></script>
</body>
</html>
```

**Erklärung:**
- `id="status"` zeigt Loading/Error/Success an
- `id="search-input"` ist das Suchfeld zum Filtern
- `id="user-list"` ist der Container für die User-Karten
- `defer` sorgt dafür, dass JavaScript erst nach HTML-Parsing läuft

---

### Schritt 2: CSS-Styling erstellen

Erstelle eine Datei `style.css`:

```css
/* === GRUNDEINSTELLUNGEN === */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

#app {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    overflow: hidden;
}

/* === HEADER === */
header {
    background: #667eea;
    color: white;
    padding: 20px;
    text-align: center;
}

header h1 {
    margin-bottom: 5px;
}

#status {
    font-size: 14px;
    opacity: 0.9;
}

#status.loading {
    color: #ffd700;
}

#status.error {
    color: #ff6b6b;
}

#status.success {
    color: #51cf66;
}

/* === SEARCH SECTION === */
#search-section {
    display: flex;
    gap: 10px;
    padding: 20px;
    border-bottom: 1px solid #eee;
}

#search-input {
    flex: 1;
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 6px;
    font-size: 16px;
}

#search-input:focus {
    outline: none;
    border-color: #667eea;
}

#load-btn {
    padding: 12px 24px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
}

#load-btn:hover {
    background: #5a67d8;
}

#load-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
}

/* === USER LIST === */
#user-list {
    padding: 20px;
    display: grid;
    gap: 15px;
}

.placeholder {
    text-align: center;
    color: #888;
    padding: 40px;
}

/* === USER CARD === */
.user-card {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.user-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.user-avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
}

.user-info {
    flex: 1;
}

.user-name {
    font-weight: bold;
    font-size: 18px;
    color: #333;
}

.user-email {
    color: #666;
    font-size: 14px;
}

.user-location {
    color: #888;
    font-size: 12px;
    margin-top: 4px;
}

/* === LOADING SPINNER === */
.loading-spinner {
    text-align: center;
    padding: 40px;
    color: #667eea;
}
```

**Erklärung:**
- `.loading`, `.error`, `.success` Klassen für Status-Anzeige
- `.user-card` ist das Styling für einzelne User-Karten
- Grid-Layout für responsive User-Liste

---

### Schritt 3: JavaScript-Grundstruktur

Erstelle eine Datei `app.js` und beginne mit der Grundstruktur:

```javascript
// ============================================
// USER VERZEICHNIS APP
// ============================================

// === 1. DOM ELEMENTE SELEKTIEREN ===
const searchInput = document.querySelector('#search-input');
const loadBtn = document.querySelector('#load-btn');
const userList = document.querySelector('#user-list');
const statusEl = document.querySelector('#status');

// === 2. STATE (Daten-Speicher) ===
let allUsers = [];  // Hier speichern wir alle geladenen User

// === 3. API URL ===
const API_URL = 'https://randomuser.me/api/?results=10';

console.log('App geladen!');
```

**Erklärung:**
- Wir selektieren alle DOM-Elemente, die wir brauchen
- `allUsers` speichert die geladenen User (für die Filter-Funktion)
- `API_URL` ist die Adresse, von der wir User laden

---

### Schritt 4: Status-Anzeige Funktion

Füge diese Funktion hinzu, um den Status zu aktualisieren:

```javascript
// === 4. HILFSFUNKTIONEN ===

// Funktion: Status-Anzeige aktualisieren
const setStatus = (message, type = '') => {
    statusEl.textContent = message;

    // Alle Status-Klassen entfernen
    statusEl.classList.remove('loading', 'error', 'success');

    // Neue Klasse hinzufügen (wenn vorhanden)
    if (type) {
        statusEl.classList.add(type);
    }
};
```

**Erklärung:**
- `setStatus('Laden...', 'loading')` zeigt gelben Text
- `setStatus('Fehler!', 'error')` zeigt roten Text
- `setStatus('5 User geladen', 'success')` zeigt grünen Text

---

### Schritt 5: User-Karte erstellen (XSS-sicher!)

Füge diese Funktion hinzu:

```javascript
// Funktion: Eine User-Karte erstellen (DOM-Elemente, XSS-sicher!)
const createUserCard = (user) => {
    // Destructuring: Daten aus dem User-Object extrahieren
    const { name, email, picture, location } = user;
    const fullName = `${name.first} ${name.last}`;
    const city = `${location.city}, ${location.country}`;

    // DOM-Elemente erstellen (sicherer als innerHTML!)
    const card = document.createElement('div');
    card.classList.add('user-card');

    const avatar = document.createElement('img');
    avatar.classList.add('user-avatar');
    avatar.src = picture.medium;
    avatar.alt = fullName;

    const info = document.createElement('div');
    info.classList.add('user-info');

    const nameEl = document.createElement('div');
    nameEl.classList.add('user-name');
    nameEl.textContent = fullName;  // textContent ist XSS-sicher!

    const emailEl = document.createElement('div');
    emailEl.classList.add('user-email');
    emailEl.textContent = email;

    const locationEl = document.createElement('div');
    locationEl.classList.add('user-location');
    locationEl.textContent = city;

    // Elemente zusammenfügen
    info.appendChild(nameEl);
    info.appendChild(emailEl);
    info.appendChild(locationEl);

    card.appendChild(avatar);
    card.appendChild(info);

    return card;
};
```

**Erklärung:**
- **Destructuring:** `const { name, email } = user` extrahiert Properties
- **Template Literal:** `` `${name.first} ${name.last}` `` kombiniert Strings
- **textContent:** Sicher gegen XSS-Angriffe (im Gegensatz zu innerHTML)

---

### Schritt 6: User-Liste rendern

Füge diese Funktion hinzu:

```javascript
// Funktion: Alle User in der Liste anzeigen
const renderUsers = (users) => {
    // Liste leeren
    userList.innerHTML = '';

    // Wenn keine User vorhanden
    if (users.length === 0) {
        const placeholder = document.createElement('p');
        placeholder.classList.add('placeholder');
        placeholder.textContent = 'Keine User gefunden.';
        userList.appendChild(placeholder);
        return;
    }

    // Für jeden User eine Karte erstellen und anhängen
    users.forEach(user => {
        const card = createUserCard(user);
        userList.appendChild(card);
    });
};
```

**Erklärung:**
- `forEach` geht durch jeden User und erstellt eine Karte
- Wenn keine User da sind, zeigen wir eine Nachricht

---

### Schritt 7: User von API laden (async/await)

Jetzt kommt der wichtigste Teil - die API-Anfrage:

```javascript
// === 5. API FUNKTION ===

// Funktion: User von API laden
const loadUsers = async () => {
    // Loading State
    setStatus('Lade User...', 'loading');
    loadBtn.disabled = true;  // Button deaktivieren
    userList.innerHTML = '<p class="loading-spinner">Laden...</p>';

    try {
        // 1. Fetch-Request starten
        const response = await fetch(API_URL);

        // 2. Prüfen ob Request erfolgreich war
        if (!response.ok) {
            throw new Error(`HTTP Fehler: ${response.status}`);
        }

        // 3. JSON-Daten parsen
        const data = await response.json();

        // 4. User aus Response extrahieren
        allUsers = data.results;

        // 5. User anzeigen
        renderUsers(allUsers);

        // 6. Success Status
        setStatus(`${allUsers.length} User geladen`, 'success');

    } catch (error) {
        // Fehler abfangen und anzeigen
        console.error('Fehler beim Laden:', error);
        setStatus('Fehler beim Laden!', 'error');
        userList.innerHTML = '<p class="placeholder">Fehler beim Laden. Bitte erneut versuchen.</p>';

    } finally {
        // Button wieder aktivieren (egal ob Erfolg oder Fehler)
        loadBtn.disabled = false;
    }
};
```

**Erklärung:**
- **async/await:** Macht asynchronen Code lesbar
- **try/catch:** Fängt Fehler ab (z.B. kein Internet)
- **response.ok:** Prüft ob Status 200-299 ist
- **finally:** Wird IMMER ausgeführt (Aufräumen)

---

### Schritt 8: Filter-Funktion

Füge die Such-Funktion hinzu:

```javascript
// === 6. FILTER FUNKTION ===

// Funktion: User nach Namen filtern
const filterUsers = (searchTerm) => {
    // Noch keine User geladen? Dann nichts tun
    if (allUsers.length === 0) {
        return;
    }

    // Wenn kein Suchbegriff, zeige alle
    if (!searchTerm.trim()) {
        renderUsers(allUsers);
        setStatus(`${allUsers.length} User angezeigt`, 'success');
        return;
    }

    // Suchbegriff in Kleinbuchstaben
    const term = searchTerm.toLowerCase();

    // Array.filter() - nur User behalten, deren Name den Suchbegriff enthält
    const filtered = allUsers.filter(user => {
        const fullName = `${user.name.first} ${user.name.last}`.toLowerCase();
        return fullName.includes(term);
    });

    // Gefilterte User anzeigen
    renderUsers(filtered);
    setStatus(`${filtered.length} von ${allUsers.length} User`, 'success');
};
```

**Erklärung:**
- **filter():** Erstellt neues Array mit Elementen, die die Bedingung erfüllen
- **includes():** Prüft ob String einen anderen String enthält
- **toLowerCase():** Macht Suche case-insensitive

---

### Schritt 9: Event Listeners

Füge die Event-Handler hinzu:

```javascript
// === 7. EVENT LISTENERS ===

// Button-Klick: User laden
loadBtn.addEventListener('click', () => {
    loadUsers();
});

// Input: Bei Eingabe filtern
searchInput.addEventListener('input', (e) => {
    // e.target.value ist der aktuelle Wert im Input-Feld
    const searchTerm = e.target.value;
    filterUsers(searchTerm);
});

// Optional: Enter-Taste im Suchfeld lädt auch User
searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && allUsers.length === 0) {
        loadUsers();
    }
});
```

**Erklärung:**
- **click Event:** Lädt User wenn Button geklickt
- **input Event:** Filtert bei JEDER Eingabe (live)
- **keydown Event:** Enter-Taste als Alternative zum Button (moderner als `keypress`)

---

### Schritt 10: Fertig!

Deine vollständige `app.js` sollte jetzt so aussehen:

```javascript
// ============================================
// USER VERZEICHNIS APP - Vollständig
// ============================================

// === 1. DOM ELEMENTE SELEKTIEREN ===
const searchInput = document.querySelector('#search-input');
const loadBtn = document.querySelector('#load-btn');
const userList = document.querySelector('#user-list');
const statusEl = document.querySelector('#status');

// === 2. STATE (Daten-Speicher) ===
let allUsers = [];

// === 3. API URL ===
const API_URL = 'https://randomuser.me/api/?results=10';

// === 4. HILFSFUNKTIONEN ===

const setStatus = (message, type = '') => {
    statusEl.textContent = message;
    statusEl.classList.remove('loading', 'error', 'success');
    if (type) {
        statusEl.classList.add(type);
    }
};

const createUserCard = (user) => {
    const { name, email, picture, location } = user;
    const fullName = `${name.first} ${name.last}`;
    const city = `${location.city}, ${location.country}`;

    const card = document.createElement('div');
    card.classList.add('user-card');

    const avatar = document.createElement('img');
    avatar.classList.add('user-avatar');
    avatar.src = picture.medium;
    avatar.alt = fullName;

    const info = document.createElement('div');
    info.classList.add('user-info');

    const nameEl = document.createElement('div');
    nameEl.classList.add('user-name');
    nameEl.textContent = fullName;

    const emailEl = document.createElement('div');
    emailEl.classList.add('user-email');
    emailEl.textContent = email;

    const locationEl = document.createElement('div');
    locationEl.classList.add('user-location');
    locationEl.textContent = city;

    info.appendChild(nameEl);
    info.appendChild(emailEl);
    info.appendChild(locationEl);

    card.appendChild(avatar);
    card.appendChild(info);

    return card;
};

const renderUsers = (users) => {
    userList.innerHTML = '';

    if (users.length === 0) {
        const placeholder = document.createElement('p');
        placeholder.classList.add('placeholder');
        placeholder.textContent = 'Keine User gefunden.';
        userList.appendChild(placeholder);
        return;
    }

    users.forEach(user => {
        const card = createUserCard(user);
        userList.appendChild(card);
    });
};

// === 5. API FUNKTION ===

const loadUsers = async () => {
    setStatus('Lade User...', 'loading');
    loadBtn.disabled = true;
    userList.innerHTML = '<p class="loading-spinner">Laden...</p>';

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP Fehler: ${response.status}`);
        }

        const data = await response.json();
        allUsers = data.results;

        renderUsers(allUsers);
        setStatus(`${allUsers.length} User geladen`, 'success');

    } catch (error) {
        console.error('Fehler beim Laden:', error);
        setStatus('Fehler beim Laden!', 'error');
        userList.innerHTML = '<p class="placeholder">Fehler beim Laden. Bitte erneut versuchen.</p>';

    } finally {
        loadBtn.disabled = false;
    }
};

// === 6. FILTER FUNKTION ===

const filterUsers = (searchTerm) => {
    // Noch keine User geladen? Dann nichts tun
    if (allUsers.length === 0) {
        return;
    }

    if (!searchTerm.trim()) {
        renderUsers(allUsers);
        setStatus(`${allUsers.length} User angezeigt`, 'success');
        return;
    }

    const term = searchTerm.toLowerCase();

    const filtered = allUsers.filter(user => {
        const fullName = `${user.name.first} ${user.name.last}`.toLowerCase();
        return fullName.includes(term);
    });

    renderUsers(filtered);
    setStatus(`${filtered.length} von ${allUsers.length} User`, 'success');
};

// === 7. EVENT LISTENERS ===

loadBtn.addEventListener('click', () => {
    loadUsers();
});

searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value;
    filterUsers(searchTerm);
});

searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && allUsers.length === 0) {
        loadUsers();
    }
});

// === 8. INITIALISIERUNG ===
console.log('User Verzeichnis App geladen!');
```

---

## Checkliste: Was du verwendet hast

Wenn du Weg B abgeschlossen hast, hast du folgende Konzepte angewendet:

### JavaScript Fundamentals
- [x] `const` und `let` korrekt verwendet
- [x] Arrow Functions (`const fn = () => {}`)
- [x] Template Literals (`` `${variable}` ``)

### Arrays & Objects
- [x] `filter()` für die Suchfunktion
- [x] `forEach()` zum Durchlaufen
- [x] Destructuring (`const { name, email } = user`)

### DOM & Events
- [x] `querySelector()` zum Selektieren
- [x] `addEventListener()` für Interaktionen
- [x] `createElement()` und `appendChild()` für dynamische Inhalte
- [x] `classList` für CSS-Klassen

### Fetch & Async
- [x] `async/await` Syntax
- [x] `try/catch` für Error Handling
- [x] `response.ok` Prüfung
- [x] Loading State während des Ladens

---

## Bonus-Ideen (optional)

Falls du die Grundaufgabe erledigt hast und mehr machen möchtest:

1. **Sortierung hinzufügen:** Buttons zum Sortieren nach Name oder Land
2. **Mehr Details:** Klick auf User-Karte zeigt mehr Infos
3. **Favoriten:** User als Favorit markieren (mit localStorage speichern)
4. **Pagination:** "Mehr laden" Button für zusätzliche User
5. **Dark Mode:** Toggle für dunkles Design

---

## Hilfreiche Tipps

### Problem: Fetch funktioniert nicht
1. Prüfe die Browser-Konsole (F12) auf Fehler
2. Ist die URL korrekt?
3. CORS-Fehler? Nutze eine der empfohlenen APIs

### Problem: User werden nicht angezeigt
1. Console.log die API-Response: `console.log(data)`
2. Prüfe die Struktur der Daten
3. Ist `data.results` ein Array?

### Problem: Filter funktioniert nicht
1. Sind User geladen? (`allUsers.length > 0`)
2. Console.log den Suchbegriff
3. Wird `filterUsers()` aufgerufen?

### Problem: CSS wird nicht geladen
1. Prüfe den Dateinamen (style.css)
2. Prüfe den Pfad im `<link>` Tag
3. Sind beide Dateien im gleichen Ordner?

---

## README.md Vorlage

Erstelle eine Datei `README.md`:

```markdown
# User Verzeichnis - [Dein Name]

## Beschreibung
Eine Mini-App, die User von einer API lädt und anzeigt.
Man kann nach Namen suchen und die Liste wird live gefiltert.

## Verwendete Techniken
- JavaScript ES6+ (const/let, Arrow Functions, Template Literals)
- Async/Await für API-Calls
- Array-Methoden (filter, forEach)
- DOM Manipulation
- Event Handling

## Weg
Ich habe Weg [A/B] gewählt.

## Was ich gelernt habe
[2-3 Sätze über deine wichtigsten Erkenntnisse]

## Schwierigkeiten
[Optional: Was war herausfordernd?]
```

---

## Viel Erfolg!

Diese Aufgabe soll dir helfen, die JavaScript-Grundlagen zu festigen. Nächste Woche geht es weiter mit React - und dort wirst du alle diese Konzepte wiederverwenden!

**Denk daran:** Das Assignment ist freiwillig. Wenn du es einreichst, bekommst du Feedback. Wenn nicht, ist das auch völlig okay!

Bei Fragen: Frag nach! Das ist keine Schwäche, sondern zeigt, dass du verstehen willst.
