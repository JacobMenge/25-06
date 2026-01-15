# Fetch, Async/Await & APIs - Praktische Übungen

## Übersicht

Heute verbinden wir Frontend mit Backend – der Schlüssel für echte Web-Apps!

In dieser Übung lernst du:
- **Die Fetch API** - HTTP-Requests aus JavaScript
- **Promises verstehen** - Asynchrone Operationen
- **Async/Await** - Moderne, lesbare Syntax
- **JSON** - Das Datenformat für Web-APIs
- **Error Handling** - try/catch für Fehlerbehandlung
- **Loading & Error States** - Bessere User Experience

Diese Übung bereitet dich auf React vor – dort wirst du `fetch()` mit `useEffect()` und `useState()` kombinieren!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Synchron vs. Asynchron | 5 min (lesen) |
| **Teil 1** | Die Fetch API verstehen | 15 min |
| **Teil 2** | Promises: Das Versprechen | 15 min |
| **Teil 3** | Async/Await: Moderne Syntax | 20 min |
| **Teil 4** | JSON: Das Datenformat | 10 min |
| **Teil 5** | HTTP-Methoden mit Fetch | 20 min |
| **Teil 6** | Error Handling richtig machen | 20 min |
| **Teil 7** | Loading & Error States | 15 min |
| **Teil 8** | CORS verstehen | 10 min |
| **Teil 9** | Fetch + FastAPI: Euer Stack | 20 min |
| **Teil 10** | Praxis: User-Verzeichnis App | 45 min |
| **Teil 11** | Bonus: Wetter-App | 30 min |
| | **Gesamt** | **ca. 3-4 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 90-120 Minuten die wichtigsten Konzepte:**

#### Kernkompetenzen (MUSS)
Diese Teile sind prüfungsrelevant und sollten sicher sitzen:

1. **Teil 1** - Fetch API - *HTTP-Requests aus dem Browser*
2. **Teil 3** - Async/Await - *Moderne, lesbare Syntax*
3. **Teil 6** - Error Handling - *Fehler richtig behandeln*
4. **Teil 7** - Loading States - *Bessere UX*

#### Praxis & Vertiefung (KANN)
Diese Teile festigen das Gelernte, sind aber optional:

5. **Teil 10** - Praxis-Übung - *Alles zusammen anwenden* (empfohlen, wenn Zeit)
6. **Teil 11** - Bonus: Wetter-App - *Für Schnelle*

Die anderen Teile (2, 4, 5, 8, 9) kannst du als Referenz nutzen oder später nachholen.

---

## Voraussetzungen & Setup

**Bevor du startest, stelle sicher:**

### Editor & Tools
- **VS Code** (oder ein anderer Code-Editor) ist installiert
- **Live Server Extension** für VS Code installiert (empfohlen!)
  - Installieren: Extensions (Strg+Shift+X) → "Live Server" suchen → Install
  - Nutzen: Rechtsklick auf HTML-Datei → "Open with Live Server"

### Warum Live Server?
- HTML-Dateien direkt öffnen (`file://`) funktioniert oft nicht mit `fetch()`
- Live Server startet einen lokalen Webserver (`http://localhost:5500`)
- Änderungen werden automatisch im Browser aktualisiert

### Browser & DevTools
- **Chrome** oder **Firefox** (Edge geht auch)
- **DevTools öffnen:** F12 oder Rechtsklick → "Untersuchen"
- **Console-Tab:** Hier siehst du `console.log()` Ausgaben und Fehler
- **Network-Tab:** Hier siehst du alle HTTP-Requests

### Typische Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| `fetch()` funktioniert nicht | Live Server nutzen statt `file://` |
| CORS-Fehler | API unterstützt kein CORS oder Backend-Config fehlt |
| Daten erscheinen nicht | Console auf Fehler prüfen (F12) |
| Alte Version im Browser | Hard Reload: Strg+Shift+R |

---

## Rückblick: Synchron vs. Asynchron

### Das Problem: JavaScript ist single-threaded

JavaScript kann nur eine Sache gleichzeitig tun. Aber was, wenn wir auf eine Antwort vom Server warten müssen? Soll der Browser einfrieren?

### Synchron vs. Asynchron

**Synchron** = Eine Aufgabe nach der anderen, jede blockiert die nächste

```
Analogie: Du holst Pizza und WARTEST vor dem Laden bis sie fertig ist.
→ Du kannst nichts anderes tun!
```

**Asynchron** = Aufgaben starten, weitermachen, Ergebnis später verarbeiten

```
Analogie: Du bestellst Pizza und machst weiter bis die Lieferung kommt.
→ Du kannst in der Zwischenzeit andere Dinge tun!
```

### Code-Vergleich

**Synchron (blockierend) - SO NICHT!**
```javascript
// Hypothetisch - würde Browser einfrieren!
console.log('Anfang');
const data = loadDataSync();  // BLOCKIERT: 3 Sekunden...
console.log('Ende');
// User kann nichts tun während der 3 Sek!
```

**Asynchron (nicht-blockierend) - SO MACHEN WIR ES!**
```javascript
console.log('Anfang');

loadDataAsync().then(data => {
    console.log('Daten:', data);  // Später!
});

console.log('Ende');  // Sofort!

// Ausgabe: Anfang → Ende → Daten
```

### Wissensfrage 1

Warum ist die Ausgabereihenfolge `Anfang → Ende → Daten` und nicht `Anfang → Daten → Ende`?

<details>
<summary>Antwort anzeigen</summary>

Die asynchrone Operation `loadDataAsync()` **startet** sofort, aber das Ergebnis kommt **später**. JavaScript wartet nicht darauf, sondern führt direkt die nächste Zeile aus (`console.log('Ende')`).

Wenn die Daten dann vom Server ankommen, wird der `.then()`-Callback ausgeführt.

**Das ist das Kernkonzept von asynchronem JavaScript!**

</details>

---

## Teil 1: Die Fetch API verstehen

`fetch()` ist die moderne Art, HTTP-Requests aus dem Browser zu machen – wie `curl` oder `wget`, aber im Browser!

### Fetch Grundlagen

```javascript
// Fetch gibt ein Promise zurück
fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => {
        // Response ist erstmal nur Metadaten
        console.log(response.status);  // 200
        console.log(response.ok);      // true

        // JSON parsen (auch async!)
        return response.json();
    })
    .then(data => {
        console.log(data);  // Die echten Daten!
    });
```

### Was passiert Schritt für Schritt?

1. **`fetch()` startet HTTP-Request**
   → Browser sendet GET an URL

2. **Server antwortet**
   → Response-Objekt mit Status & Headers

3. **`response.json()` parsed Body**
   → JavaScript-Objekt mit den Daten

4. **Promise resolved**
   → `.then()` callback wird ausgeführt

### Das Response-Objekt

```javascript
fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => {
        // Wichtige Properties:
        console.log(response.status);     // 200, 404, 500, etc.
        console.log(response.ok);         // true wenn status 200-299
        console.log(response.statusText); // "OK", "Not Found", etc.
        console.log(response.headers);    // Response-Headers
        console.log(response.url);        // Die finale URL

        return response.json();
    });
```

### ⚠️ Wichtig: response.json() kann fehlschlagen!

`response.json()` ist selbst ein Promise und kann aus mehreren Gründen fehlschlagen:

```javascript
// Diese Situationen verursachen einen Fehler bei response.json():

// 1. Leere Response (z.B. bei 204 No Content)
// → Der Body ist leer, JSON.parse("") schlägt fehl

// 2. Server gibt kein JSON zurück (z.B. HTML-Fehlerseite)
// → JSON.parse("<html>...") schlägt fehl

// 3. Ungültiges JSON vom Server
// → Syntax-Fehler beim Parsen
```

**Best Practice:** Bei DELETE-Requests oder APIs, die manchmal kein JSON zurückgeben:

```javascript
async function safeJsonParse(response) {
    const text = await response.text();

    // Leere Response?
    if (!text) {
        return null;
    }

    // Versuche JSON zu parsen
    try {
        return JSON.parse(text);
    } catch {
        console.warn('Response war kein gültiges JSON:', text);
        return null;
    }
}
```

### Übung 1: Erster Fetch

> **Ziel:** Die Fetch API in der Browser-Konsole ausprobieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Daten von einer API abrufen kannst

**Aufgabe:**

Öffne die Browser-Konsole (F12 → Console) und führe folgende Schritte aus:

```javascript
// 1. Einfacher GET-Request
fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => {
        console.log('Status:', response.status);
        console.log('OK?:', response.ok);
        return response.json();
    })
    .then(users => {
        console.log('Anzahl User:', users.length);
        console.log('Erster User:', users[0].name);
    });

// 2. Einzelnen User abrufen
fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => response.json())
    .then(user => {
        console.log('Name:', user.name);
        console.log('Email:', user.email);
        console.log('Stadt:', user.address.city);
    });

// 3. Posts eines Users abrufen
fetch('https://jsonplaceholder.typicode.com/posts?userId=1')
    .then(response => response.json())
    .then(posts => {
        console.log('Anzahl Posts:', posts.length);
        posts.forEach(post => {
            console.log('-', post.title);
        });
    });
```

**Fragen zum Nachdenken:**
- Was passiert, wenn du eine nicht existierende URL aufrufst?
- Wie groß ist der erste Datensatz (users)?

<details>
<summary>Erwartete Ausgabe</summary>

```
Status: 200
OK?: true
Anzahl User: 10
Erster User: Leanne Graham

Name: Leanne Graham
Email: Sincere@april.biz
Stadt: Gwenborough

Anzahl Posts: 10
- sunt aut facere repellat provident occaecati excepturi optio reprehenderit
- qui est esse
- ...
```

</details>

---

## Teil 2: Promises - Das Versprechen

Ein **Promise** ist ein "Versprechen" auf einen zukünftigen Wert – wie eine Bestellbestätigung für die Pizza.

### Promise States

Ein Promise hat immer einen von drei Zuständen:

| State | Bedeutung | Handler |
|-------|-----------|---------|
| **PENDING** | Promise läuft noch, Ergebnis unbekannt | - |
| **FULFILLED** (resolved) | Erfolgreich! Daten sind da | `.then()` |
| **REJECTED** | Fehler aufgetreten | `.catch()` |

**Wichtig:** Ein Promise kann nur **EINMAL** resolved oder rejected werden – dann ist es fertig!

### Promise Chain

Promises können verkettet werden – jedes `.then()` gibt ein neues Promise zurück:

```javascript
fetch('/api/user/123')
    .then(response => response.json())      // → Promise!
    .then(user => fetch('/api/posts/' + user.id))
    .then(response => response.json())      // → Promise!
    .then(posts => {
        console.log(posts);
    })
    .catch(error => {
        // Fängt ALLE Fehler der gesamten Chain!
        console.error('Irgendwo ging was schief:', error);
    });
```

### Python-Vergleich

Du kennst asynchrone Konzepte bereits aus Python:

```python
# Python: async/await
import asyncio
import aiohttp

async def fetch_user(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/users/{user_id}') as response:
            return await response.json()
```

```javascript
// JavaScript: Promise mit .then()
fetch('/api/users/' + userId)
    .then(response => response.json())
    .then(user => console.log(user));
```

### Übung 2: Promise Chain

> **Ziel:** Promise-Verkettung verstehen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du verstehst, wie `.then()` Werte weitergibt

**Aufgabe:**

```javascript
// Baue eine Promise Chain, die:
// 1. Einen User lädt
// 2. Dessen Posts lädt
// 3. Alle Post-Titel ausgibt

fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => {
        console.log('Schritt 1: User-Response erhalten');
        return response.json();
    })
    .then(user => {
        console.log('Schritt 2: User geparst:', user.name);
        // Lade die Posts dieses Users
        return fetch(`https://jsonplaceholder.typicode.com/posts?userId=${user.id}`);
    })
    .then(response => {
        console.log('Schritt 3: Posts-Response erhalten');
        return response.json();
    })
    .then(posts => {
        console.log('Schritt 4: Posts geparst');
        console.log(`${posts.length} Posts gefunden:`);
        posts.forEach((post, index) => {
            console.log(`  ${index + 1}. ${post.title}`);
        });
    })
    .catch(error => {
        console.error('Fehler in der Chain:', error);
    });
```

**Fragen zum Nachdenken:**
- Warum müssen wir zwei Mal `response.json()` aufrufen?
- Was passiert, wenn Schritt 2 fehlschlägt?

<details>
<summary>Antworten</summary>

**Warum zwei Mal `response.json()`?**
Jeder `fetch()`-Aufruf gibt ein neues Response-Objekt zurück. Das erste für den User, das zweite für die Posts. Jedes Response-Objekt muss separat geparst werden.

**Was passiert bei Fehler in Schritt 2?**
Der `.catch()` am Ende fängt den Fehler auf und verhindert, dass die Chain weitermacht. Die Schritte 3 und 4 werden übersprungen.

</details>

---

## Teil 3: Async/Await - Moderne Syntax

`async/await` macht asynchronen Code lesbar wie synchronen Code – **das ist der moderne Standard!**

### Die Transformation

**Mit .then() (alt):**
```javascript
function loadUser(id) {
    return fetch('/api/users/' + id)
        .then(response => response.json())
        .then(user => {
            console.log(user.name);
            return fetch('/api/posts?userId=' + user.id);
        })
        .then(response => response.json())
        .then(posts => console.log(posts))
        .catch(error => console.error(error));
}
```

**Mit async/await (modern):**
```javascript
async function loadUser(id) {
    try {
        const response = await fetch('/api/users/' + id);
        const user = await response.json();

        console.log(user.name);

        const postsRes = await fetch('/api/posts?userId=' + user.id);
        const posts = await postsRes.json();
        console.log(posts);
    } catch (error) {
        console.error(error);
    }
}
```

### Die Regeln

1. **`async`** vor der Funktion macht sie asynchron
2. **`await`** wartet auf ein Promise und gibt dessen Wert zurück
3. **`await`** kann **NUR** in `async` Funktionen verwendet werden!
4. **`try/catch`** ersetzt `.catch()` für Error Handling

### Arrow Function Syntax

```javascript
// Normale async function
async function fetchData() {
    const response = await fetch('/api/data');
    return response.json();
}

// Async Arrow Function
const fetchData = async () => {
    const response = await fetch('/api/data');
    return response.json();
};

// Async Arrow Function mit Parameter
const fetchUser = async (id) => {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
};
```

### Übung 3: Von .then() zu async/await

> **Ziel:** Code von Promise Chains zu async/await umschreiben
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du async/await sicher anwenden kannst

**Aufgabe:**

Erstelle eine Datei `async-uebung.js` und schreibe die folgenden Funktionen:

```javascript
// ========================================
// TEIL 3: Async/Await Übungen
// Datei: async-uebung.js
// ========================================

// 1. Einfache async Funktion
// Schreibe eine Funktion, die einen User lädt
async function getUser(id) {
    // Dein Code hier:
    // - fetch von https://jsonplaceholder.typicode.com/users/{id}
    // - await die Response
    // - await response.json()
    // - return den User
}

// Teste:
// getUser(1).then(user => console.log(user.name));

// 2. Async Funktion mit Error Handling
async function getUserSafe(id) {
    try {
        // Dein Code hier
    } catch (error) {
        console.error('Fehler beim Laden:', error.message);
        return null;
    }
}

// 3. Mehrere Requests nacheinander (abhängig)
async function getUserWithPosts(id) {
    try {
        // 1. User laden
        // 2. Posts des Users laden
        // 3. Objekt zurückgeben: { user, posts }
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;
    }
}

// 4. Mehrere Requests parallel (unabhängig)
async function getAllData() {
    try {
        // Promise.all für parallele Requests!
        const [usersRes, postsRes] = await Promise.all([
            fetch('https://jsonplaceholder.typicode.com/users'),
            fetch('https://jsonplaceholder.typicode.com/posts')
        ]);

        const [users, posts] = await Promise.all([
            usersRes.json(),
            postsRes.json()
        ]);

        return { users, posts };
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;
    }
}

// Teste alle Funktionen:
async function runTests() {
    console.log('=== Test 1: getUser ===');
    const user = await getUser(1);
    console.log('User:', user?.name);

    console.log('\n=== Test 2: getUserSafe ===');
    const userSafe = await getUserSafe(999); // Existiert nicht
    console.log('Result:', userSafe);

    console.log('\n=== Test 3: getUserWithPosts ===');
    const data = await getUserWithPosts(1);
    console.log('User:', data?.user?.name);
    console.log('Posts:', data?.posts?.length);

    console.log('\n=== Test 4: getAllData ===');
    const all = await getAllData();
    console.log('Users:', all?.users?.length);
    console.log('Posts:', all?.posts?.length);
}

runTests();
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 3: Async/Await - Musterlösung
// ========================================

// 1. Einfache async Funktion
async function getUser(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await response.json();
    return user;
}

// 2. Mit Error Handling
async function getUserSafe(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const user = await response.json();
        return user;
    } catch (error) {
        console.error('Fehler beim Laden:', error.message);
        return null;
    }
}

// 3. Mehrere abhängige Requests
async function getUserWithPosts(id) {
    try {
        // User laden
        const userRes = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        const user = await userRes.json();

        // Posts des Users laden
        const postsRes = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${id}`);
        const posts = await postsRes.json();

        return { user, posts };
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;
    }
}

// 4. Parallele Requests
async function getAllData() {
    try {
        const [usersRes, postsRes] = await Promise.all([
            fetch('https://jsonplaceholder.typicode.com/users'),
            fetch('https://jsonplaceholder.typicode.com/posts')
        ]);

        const [users, posts] = await Promise.all([
            usersRes.json(),
            postsRes.json()
        ]);

        return { users, posts };
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;
    }
}
```

</details>

### Wissensfrage 2

Was ist der Unterschied zwischen diesen beiden Varianten?

```javascript
// Variante A: Nacheinander
const user = await fetchUser(1);
const posts = await fetchPosts(1);

// Variante B: Parallel
const [user, posts] = await Promise.all([
    fetchUser(1),
    fetchPosts(1)
]);
```

<details>
<summary>Antwort anzeigen</summary>

**Variante A (Nacheinander):**
- Posts werden erst geladen, wenn User fertig ist
- Gesamtzeit = Zeit für User + Zeit für Posts
- Nutzen wenn: Der zweite Request vom ersten abhängt

**Variante B (Parallel mit Promise.all):**
- Beide Requests starten gleichzeitig
- Gesamtzeit = Längerer der beiden Requests
- Nutzen wenn: Requests unabhängig voneinander sind

**Beispiel:** Wenn beide Requests je 1 Sekunde dauern:
- Variante A: 2 Sekunden
- Variante B: 1 Sekunde

**→ Promise.all ist schneller, wenn Requests unabhängig sind!**

</details>

---

## Teil 4: JSON - JavaScript Object Notation

JSON ist **DAS** Standard-Format für Daten im Web.

### JSON Format

```json
{
    "name": "Max Mustermann",
    "age": 28,
    "isStudent": false,
    "courses": ["React", "Python"],
    "address": {
        "city": "Berlin",
        "zip": "10115"
    }
}
```

**Wichtige Regeln:**
- Schlüssel **MÜSSEN** in `"quotes"` sein!
- Keine trailing commas erlaubt!
- Nur diese Datentypen: String, Number, Boolean, null, Array, Object

### JSON Methoden in JavaScript

```javascript
// JSON String → JavaScript Object
const jsonString = '{"name": "Max", "age": 28}';
const obj = JSON.parse(jsonString);
console.log(obj.name);  // "Max"

// JavaScript Object → JSON String
const user = { name: 'Max', age: 28 };
const json = JSON.stringify(user);
console.log(json);  // '{"name":"Max","age":28}'

// Schön formatiert (für Debugging):
console.log(JSON.stringify(user, null, 2));
// {
//   "name": "Max",
//   "age": 28
// }
```

### JSON bei Fetch

```javascript
// GET: JSON empfangen
const response = await fetch('/api/users');
const users = await response.json();  // Parst automatisch!

// POST: JSON senden
const response = await fetch('/api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'  // Wichtig!
    },
    body: JSON.stringify({
        name: 'Max',
        email: 'max@example.com'
    })
});
```

### Übung 4: JSON Parsing

> **Ziel:** JSON parsen und erstellen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du JSON.parse() und JSON.stringify() verstehst

**Aufgabe:**

Öffne die Browser-Konsole und führe aus:

```javascript
// 1. JSON String parsen
const jsonString = '{"name": "Max", "age": 28, "hobbies": ["Coding", "Gaming"]}';
const user = JSON.parse(jsonString);
console.log(user.name);
console.log(user.hobbies[0]);

// 2. Object zu JSON String
const product = {
    id: 1,
    name: 'Laptop',
    price: 999.99,
    inStock: true
};
const productJson = JSON.stringify(product);
console.log(productJson);

// 3. Schön formatiert
console.log(JSON.stringify(product, null, 2));

// 4. Was passiert bei ungültigem JSON?
try {
    const invalid = JSON.parse('{name: "Max"}');  // Fehler! Keine Quotes um name
} catch (error) {
    console.error('JSON Parse Error:', error.message);
}
```

---

## Teil 5: HTTP-Methoden mit Fetch

`fetch()` unterstützt alle HTTP-Methoden – nicht nur GET!

### GET - Daten abrufen

```javascript
// GET ist die Default-Methode
const response = await fetch('/api/users');
const users = await response.json();

// Mit Query-Parametern
const search = await fetch('/api/users?role=admin&active=true');
```

### POST - Neue Daten erstellen

```javascript
const response = await fetch('/api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'Max',
        email: 'max@example.com'
    })
});

const newUser = await response.json();
console.log('Neuer User erstellt:', newUser);
```

### PUT - Daten komplett ersetzen

```javascript
const response = await fetch('/api/users/1', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        id: 1,
        name: 'Maximilian',
        email: 'max@example.com'
    })
});
```

### PATCH - Daten teilweise ändern

```javascript
const response = await fetch('/api/users/1', {
    method: 'PATCH',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: 'newemail@example.com'  // Nur email ändern
    })
});
```

### DELETE - Daten löschen

```javascript
const response = await fetch('/api/users/1', {
    method: 'DELETE'
});

if (response.ok) {
    console.log('User gelöscht!');
}
```

### Übung 5: CRUD-Operationen

> **Ziel:** Alle HTTP-Methoden mit Fetch ausprobieren
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du POST, PUT, PATCH und DELETE Requests machen kannst

**Aufgabe:**

JSONPlaceholder simuliert einen REST-Server – perfekt zum Üben!

```javascript
// ========================================
// TEIL 5: CRUD mit Fetch
// ========================================

const API_BASE = 'https://jsonplaceholder.typicode.com';

// 1. CREATE: Neuen Post erstellen
async function createPost(title, body, userId) {
    const response = await fetch(`${API_BASE}/posts`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title,
            body,
            userId
        })
    });

    const newPost = await response.json();
    console.log('Erstellt:', newPost);
    return newPost;
}

// 2. READ: Post lesen (GET haben wir schon)
async function getPost(id) {
    const response = await fetch(`${API_BASE}/posts/${id}`);
    return response.json();
}

// 3. UPDATE: Post komplett ersetzen
async function updatePost(id, title, body, userId) {
    const response = await fetch(`${API_BASE}/posts/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id,
            title,
            body,
            userId
        })
    });

    const updatedPost = await response.json();
    console.log('Aktualisiert:', updatedPost);
    return updatedPost;
}

// 4. PARTIAL UPDATE: Nur Titel ändern
async function updatePostTitle(id, newTitle) {
    const response = await fetch(`${API_BASE}/posts/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: newTitle
        })
    });

    const updatedPost = await response.json();
    console.log('Titel geändert:', updatedPost);
    return updatedPost;
}

// 5. DELETE: Post löschen
async function deletePost(id) {
    const response = await fetch(`${API_BASE}/posts/${id}`, {
        method: 'DELETE'
    });

    console.log('Gelöscht:', response.ok);
    return response.ok;
}

// Teste alle Operationen:
async function testCRUD() {
    console.log('=== CREATE ===');
    const newPost = await createPost('Mein Titel', 'Mein Inhalt', 1);

    console.log('\n=== READ ===');
    const post = await getPost(1);
    console.log('Gelesen:', post.title);

    console.log('\n=== UPDATE ===');
    await updatePost(1, 'Neuer Titel', 'Neuer Inhalt', 1);

    console.log('\n=== PATCH ===');
    await updatePostTitle(1, 'Nur Titel geändert');

    console.log('\n=== DELETE ===');
    await deletePost(1);
}

testCRUD();
```

<details>
<summary>Erwartete Ausgabe</summary>

```
=== CREATE ===
Erstellt: { id: 101, title: 'Mein Titel', body: 'Mein Inhalt', userId: 1 }

=== READ ===
Gelesen: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

=== UPDATE ===
Aktualisiert: { id: 1, title: 'Neuer Titel', body: 'Neuer Inhalt', userId: 1 }

=== PATCH ===
Titel geändert: { id: 1, title: 'Nur Titel geändert', ... }

=== DELETE ===
Gelöscht: true
```

**Hinweis:** JSONPlaceholder simuliert nur – die Daten werden nicht wirklich gespeichert!

</details>

---

## Teil 6: Error Handling richtig machen

Netzwerk-Requests können aus vielen Gründen fehlschlagen – wir müssen darauf vorbereitet sein!

### Das Problem: fetch() wirft nicht bei 404/500!

```javascript
// ⚠️ ACHTUNG: Das wirft KEINEN Error!
const response = await fetch('/api/user/999');  // 404 Not Found

// response.ok ist false bei 4xx/5xx
console.log(response.ok);      // false
console.log(response.status);  // 404

// fetch() wirft nur Error bei NETZWERK-Fehler
// (z.B. kein Internet, Server nicht erreichbar)
```

### Die Lösung: response.ok prüfen!

```javascript
async function fetchUser(id) {
    try {
        const response = await fetch(`/api/users/${id}`);

        // WICHTIG: Status prüfen!
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;  // Oder Error-State setzen
    }
}
```

### Verschiedene Fehlerarten behandeln

```javascript
async function fetchData(url) {
    try {
        const response = await fetch(url);

        // HTTP-Fehler prüfen
        if (!response.ok) {
            // Verschiedene Status-Codes behandeln
            if (response.status === 404) {
                throw new Error('Ressource nicht gefunden');
            } else if (response.status === 401) {
                throw new Error('Nicht autorisiert - bitte einloggen');
            } else if (response.status === 403) {
                throw new Error('Zugriff verweigert');
            } else if (response.status >= 500) {
                throw new Error('Server-Fehler - bitte später versuchen');
            } else {
                throw new Error(`HTTP ${response.status}`);
            }
        }

        return await response.json();

    } catch (error) {
        // Unterscheide: Netzwerk-Fehler vs. HTTP-Fehler
        if (error.name === 'TypeError') {
            // Netzwerk-Fehler (kein Internet, CORS, etc.)
            console.error('Netzwerk-Fehler:', error.message);
        } else {
            // Unser geworfener HTTP-Fehler
            console.error('API-Fehler:', error.message);
        }
        return null;
    }
}
```

### Übung 6: Robustes Error Handling

> **Ziel:** Fehler richtig behandeln und dem User zeigen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Code alle Fehlerarten abfängt

**Aufgabe:**

Erstelle eine robuste Fetch-Funktion:

```javascript
// ========================================
// TEIL 6: Error Handling
// ========================================

/**
 * Robuste Fetch-Funktion mit Error Handling
 * @param {string} url - Die URL zum Abrufen
 * @returns {Promise<{data: any, error: string|null}>}
 */
async function safeFetch(url) {
    try {
        const response = await fetch(url);

        // 1. HTTP-Status prüfen
        if (!response.ok) {
            // Dein Code: Verschiedene Status behandeln
            // 404 → "Nicht gefunden"
            // 401 → "Bitte einloggen"
            // 500+ → "Server-Fehler"
        }

        // 2. JSON parsen
        const data = await response.json();

        // 3. Erfolg zurückgeben
        return { data, error: null };

    } catch (error) {
        // 4. Fehler zurückgeben
        return { data: null, error: error.message };
    }
}

// Teste mit verschiedenen URLs:
async function testErrorHandling() {
    console.log('=== Test 1: Gültige URL ===');
    const result1 = await safeFetch('https://jsonplaceholder.typicode.com/users/1');
    console.log(result1);

    console.log('\n=== Test 2: Nicht existierende Ressource ===');
    const result2 = await safeFetch('https://jsonplaceholder.typicode.com/users/9999');
    console.log(result2);

    console.log('\n=== Test 3: Ungültige URL ===');
    const result3 = await safeFetch('https://invalid-domain-12345.com/api');
    console.log(result3);
}

testErrorHandling();
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
async function safeFetch(url) {
    try {
        const response = await fetch(url);

        // HTTP-Status prüfen
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('Nicht gefunden');
            } else if (response.status === 401) {
                throw new Error('Bitte einloggen');
            } else if (response.status === 403) {
                throw new Error('Zugriff verweigert');
            } else if (response.status >= 500) {
                throw new Error('Server-Fehler - bitte später versuchen');
            } else {
                throw new Error(`HTTP ${response.status}`);
            }
        }

        const data = await response.json();
        return { data, error: null };

    } catch (error) {
        // Unterscheide Netzwerk- und HTTP-Fehler
        let errorMessage = error.message;

        if (error.name === 'TypeError') {
            errorMessage = 'Netzwerk-Fehler - bitte Verbindung prüfen';
        }

        return { data: null, error: errorMessage };
    }
}
```

</details>

---

## Teil 7: Loading & Error States

Eine gute User Experience braucht **drei Zustände**: Loading, Error, Success.

### Die drei States

```javascript
let state = {
    data: null,
    isLoading: false,
    error: null
};

async function loadData() {
    // 1. Loading starten
    state.isLoading = true;
    state.error = null;
    updateUI();  // UI zeigt Spinner

    try {
        const response = await fetch('/api/data');

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        // 2. Success!
        state.data = await response.json();
        state.error = null;

    } catch (error) {
        // 3. Error!
        state.error = error.message;
        state.data = null;

    } finally {
        // 4. Loading beenden (immer!)
        state.isLoading = false;
        updateUI();  // UI zeigt Daten oder Fehler
    }
}
```

### UI für verschiedene States

```javascript
function updateUI() {
    const container = document.querySelector('#content');

    if (state.isLoading) {
        container.innerHTML = '<div class="spinner">Lädt...</div>';
        return;
    }

    if (state.error) {
        container.innerHTML = `
            <div class="error">
                <p>Fehler: ${state.error}</p>
                <button onclick="loadData()">Erneut versuchen</button>
            </div>
        `;
        return;
    }

    if (state.data) {
        container.innerHTML = `
            <div class="success">
                <h2>${state.data.name}</h2>
                <p>${state.data.email}</p>
            </div>
        `;
    }
}
```

### Übung 7: Loading States implementieren

> **Ziel:** Alle drei Zustände in einer App implementieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine App Loading, Error und Success States zeigt

Erstelle `loading-states.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading States Demo</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background: #f5f5f5;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        h1 {
            margin-bottom: 20px;
        }

        .btn {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-right: 10px;
            margin-bottom: 20px;
        }

        .btn:hover {
            background: #0056b3;
        }

        .btn:disabled {
            background: #ccc;
            cursor: not-allowed;
        }

        #content {
            min-height: 200px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .loading {
            text-align: center;
            color: #666;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid #007bff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
        }

        .error button {
            margin-top: 10px;
            padding: 8px 16px;
            background: #721c24;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .user-card {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        .user-card h3 {
            margin-bottom: 5px;
            color: #333;
        }

        .user-card p {
            color: #666;
            margin-bottom: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Loading States Demo</h1>

        <button class="btn" id="loadBtn" onclick="loadUsers()">
            User laden
        </button>
        <button class="btn" id="errorBtn" onclick="loadInvalid()">
            Fehler simulieren
        </button>

        <div id="content">
            <p style="color: #666; text-align: center;">
                Klicke auf einen Button um Daten zu laden.
            </p>
        </div>
    </div>

    <script>
        // ========================================
        // State Management
        // ========================================
        let state = {
            users: [],
            isLoading: false,
            error: null
        };

        // ========================================
        // UI Update Funktion
        // ========================================
        function updateUI() {
            const content = document.querySelector('#content');
            const loadBtn = document.querySelector('#loadBtn');
            const errorBtn = document.querySelector('#errorBtn');

            // Buttons während Loading deaktivieren
            loadBtn.disabled = state.isLoading;
            errorBtn.disabled = state.isLoading;

            // Loading State
            if (state.isLoading) {
                content.innerHTML = `
                    <div class="loading">
                        <div class="spinner"></div>
                        <p>Lädt Daten...</p>
                    </div>
                `;
                return;
            }

            // Error State
            if (state.error) {
                content.innerHTML = `
                    <div class="error">
                        <p><strong>Fehler!</strong></p>
                        <p>${state.error}</p>
                        <button onclick="loadUsers()">Erneut versuchen</button>
                    </div>
                `;
                return;
            }

            // Success State
            if (state.users.length > 0) {
                const usersHtml = state.users.map(user => `
                    <div class="user-card">
                        <h3>${escapeHtml(user.name)}</h3>
                        <p>Email: ${escapeHtml(user.email)}</p>
                        <p>Stadt: ${escapeHtml(user.address.city)}</p>
                    </div>
                `).join('');

                content.innerHTML = usersHtml;
                return;
            }

            // Empty State
            content.innerHTML = `
                <p style="color: #666; text-align: center;">
                    Keine Daten vorhanden.
                </p>
            `;
        }

        // XSS-Schutz Helper
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        // ========================================
        // Data Loading Funktionen
        // ========================================
        async function loadUsers() {
            // 1. Loading starten
            state.isLoading = true;
            state.error = null;
            updateUI();

            try {
                // Künstliche Verzögerung für Demo
                await new Promise(resolve => setTimeout(resolve, 1000));

                const response = await fetch('https://jsonplaceholder.typicode.com/users');

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}`);
                }

                // 2. Success!
                state.users = await response.json();
                state.error = null;

            } catch (error) {
                // 3. Error!
                state.error = error.message;
                state.users = [];

            } finally {
                // 4. Loading beenden
                state.isLoading = false;
                updateUI();
            }
        }

        async function loadInvalid() {
            state.isLoading = true;
            state.error = null;
            updateUI();

            try {
                await new Promise(resolve => setTimeout(resolve, 1000));

                // Ungültige URL für Fehler-Demo
                const response = await fetch('https://jsonplaceholder.typicode.com/invalid-endpoint');

                if (!response.ok) {
                    throw new Error(`Ressource nicht gefunden (${response.status})`);
                }

                state.users = await response.json();

            } catch (error) {
                state.error = error.message;
                state.users = [];

            } finally {
                state.isLoading = false;
                updateUI();
            }
        }
    </script>
</body>
</html>
```

**Teste die App:**
1. Öffne die HTML-Datei im Browser
2. Klicke "User laden" → Spinner → Daten
3. Klicke "Fehler simulieren" → Spinner → Fehlermeldung
4. Klicke "Erneut versuchen" → funktioniert!

---

## Teil 8: CORS verstehen

Wenn dein `fetch()` nicht funktioniert, liegt es oft an **CORS**!

### Was ist CORS?

**CORS** = **C**ross-**O**rigin **R**esource **S**haring

Der Browser blockiert Requests zu **anderen Domains** aus Sicherheitsgründen:

```
Deine Seite:     http://localhost:3000
API-Server:      https://api.example.com

→ Browser: "Verschiedene Origins! Ich blockiere den Request!"
```

### Wann tritt CORS auf?

| Deine Seite | API | CORS? |
|-------------|-----|-------|
| localhost:3000 | localhost:3000 | Nein (Same Origin) |
| localhost:3000 | localhost:8000 | **Ja** (anderer Port!) |
| meinsite.de | api.meinsite.de | **Ja** (andere Subdomain!) |
| meinsite.de | anderesite.de | **Ja** (andere Domain!) |

### Die CORS-Fehlermeldung

```
Access to fetch at 'https://api.example.com/data' from origin
'http://localhost:3000' has been blocked by CORS policy:
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

### Lösungen

**1. Backend konfigurieren (FastAPI):**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS aktivieren (für Development)
# WICHTIG: Bei allow_credentials=True KEINE Wildcard "*" verwenden!
app.add_middleware(
    CORSMiddleware,
    # Für Development: Konkrete Origins angeben
    allow_origins=["http://localhost:5500", "http://localhost:3000"],
    allow_credentials=True,  # Nur wenn du Cookies/Auth brauchst
    allow_methods=["*"],
    allow_headers=["*"],
)

# Alternative OHNE Credentials (einfacher für Demos):
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Wildcard OK wenn keine Credentials
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
```

**2. Öffentliche APIs nutzen:**
Diese APIs haben CORS bereits aktiviert:
- `https://jsonplaceholder.typicode.com` ✓
- `https://api.github.com` ✓
- `https://wttr.in` ✓

**3. Eigenes Backend nutzen:**
Dein FastAPI-Backend auf dem gleichen Server → Same Origin, kein CORS!

### Wissensfrage 3

Warum funktioniert `fetch()` in der Browser-Konsole zu `jsonplaceholder.typicode.com`, aber nicht zu deiner lokalen FastAPI ohne CORS-Config?

<details>
<summary>Antwort anzeigen</summary>

**JSONPlaceholder** hat den CORS-Header `Access-Control-Allow-Origin: *` gesetzt. Das bedeutet: "Requests von überall erlaubt."

**Deine FastAPI** ohne CORS-Config sendet diesen Header nicht. Der Browser sieht: "Keine Erlaubnis" → Blockiert!

**Merke:** CORS ist ein **Browser**-Sicherheits-Feature. Server-zu-Server (z.B. Python → API) funktioniert immer, weil dort kein Browser dazwischen ist!

</details>

---

## Teil 9: Fetch + FastAPI - Euer Stack!

So verbindet ihr euer JavaScript-Frontend mit eurem Python-Backend.

### FastAPI Backend

```python
# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS aktivieren (für Development)
# WICHTIG: Für Production spezifische Origins angeben!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://localhost:3000", "http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datenmodell
class User(BaseModel):
    name: str
    email: str

# In-Memory Datenbank (für Demo)
users_db = [
    {"id": 1, "name": "Max", "email": "max@example.com"},
    {"id": 2, "name": "Anna", "email": "anna@example.com"},
]

# GET: Alle User
@app.get("/api/users")
def get_users():
    return users_db

# GET: Einzelner User
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    # Best Practice: HTTPException für Fehler-Responses
    raise HTTPException(status_code=404, detail="User nicht gefunden")

# POST: Neuer User
@app.post("/api/users")
def create_user(user: User):
    new_id = max(u["id"] for u in users_db) + 1
    new_user = {"id": new_id, "name": user.name, "email": user.email}
    users_db.append(new_user)
    return new_user
```

### JavaScript Frontend

```javascript
// api.js
const API_URL = 'http://localhost:8000';

// GET: Alle User laden
async function loadUsers() {
    try {
        const response = await fetch(`${API_URL}/api/users`);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Fehler beim Laden:', error.message);
        return [];
    }
}

// POST: Neuen User erstellen
async function createUser(name, email) {
    try {
        const response = await fetch(`${API_URL}/api/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Fehler beim Erstellen:', error.message);
        return null;
    }
}

// Verwendung
async function main() {
    // Alle User laden
    const users = await loadUsers();
    console.log('Users:', users);

    // Neuen User erstellen
    const newUser = await createUser('Lisa', 'lisa@example.com');
    console.log('Neuer User:', newUser);
}

main();
```

### Workflow

1. **FastAPI starten:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Frontend öffnen:**
   Öffne deine HTML-Datei oder starte einen Dev-Server

3. **fetch() ruft Backend:**
   JavaScript → HTTP → FastAPI → Response → JavaScript

### Übung 9: Frontend + Backend verbinden

> **Ziel:** Ein vollständiges Frontend-Backend-Setup
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein JavaScript User von FastAPI lädt und erstellt

**Voraussetzung:** FastAPI ist installiert (`pip install fastapi uvicorn`)

**Aufgabe:**

1. Erstelle `main.py` mit dem FastAPI-Code oben
2. Starte FastAPI: `uvicorn main:app --reload`
3. Teste im Browser: `http://localhost:8000/api/users`
4. Erstelle `frontend.html` und teste die JavaScript-Aufrufe

---

## Teil 10: Praxis - User-Verzeichnis App

Zeit, alles zusammen anzuwenden! Baue eine vollständige App.

> **Ziel:** Eine komplette App mit Loading States, Error Handling und Suche
> **Zeitbedarf:** ca. 45 Minuten
> **Du bist fertig, wenn:** Die App User lädt, filtert und Fehler anzeigt

### Aufgabe: User-Verzeichnis

Erstelle `user-app.html` und **vervollständige die markierten TODO-Stellen**:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User-Verzeichnis</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        header {
            background: #667eea;
            color: white;
            padding: 25px;
            text-align: center;
        }
        header h1 { margin-bottom: 8px; }
        header p { opacity: 0.9; }
        .controls {
            padding: 20px;
            background: #f8f9fa;
            border-bottom: 1px solid #eee;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .search-input {
            flex: 1;
            min-width: 200px;
            padding: 12px 16px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        .search-input:focus { outline: none; border-color: #667eea; }
        .btn {
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover { background: #5a67d8; }
        .btn:disabled { background: #ccc; cursor: not-allowed; }
        #content { padding: 20px; min-height: 400px; }
        .loading { text-align: center; padding: 60px 20px; color: #666; }
        .spinner {
            width: 50px; height: 50px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .error {
            background: #fee2e2;
            color: #991b1b;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
        }
        .error button {
            margin-top: 15px;
            padding: 10px 20px;
            background: #991b1b;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .user-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }
        .user-card {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .user-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        .user-card h3 { color: #333; margin-bottom: 10px; font-size: 18px; }
        .user-card p { color: #666; margin-bottom: 6px; font-size: 14px; }
        .user-card .label {
            color: #888;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .stats {
            padding: 15px 20px;
            background: #f8f9fa;
            border-top: 1px solid #eee;
            color: #666;
            font-size: 14px;
        }
        .empty { text-align: center; padding: 60px 20px; color: #888; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>User-Verzeichnis</h1>
            <p>Daten von JSONPlaceholder API</p>
        </header>

        <div class="controls">
            <input type="text" id="search" class="search-input" placeholder="User suchen…">
            <button class="btn" id="loadBtn" onclick="loadUsers()">Neu laden</button>
        </div>

        <div id="content"></div>
        <div class="stats" id="stats"></div>
    </div>

    <script>
        // ========================================
        // USER-VERZEICHNIS APP - Vervollständige die TODOs!
        // ========================================

        const API_URL = 'https://jsonplaceholder.typicode.com';

        // State
        let state = {
            users: [],
            filteredUsers: [],
            isLoading: false,
            error: null,
            searchQuery: ''
        };

        // ========================================
        // TODO 1: API FUNKTION
        // ========================================

        async function fetchUsers() {
            // TODO: Implementiere die Fetch-Funktion
            // 1. Fetch von API_URL + '/users'
            // 2. Prüfe response.ok - wenn nicht ok, wirf Error
            // 3. Parse und return JSON

            // Dein Code hier:

        }

        // ========================================
        // TODO 2: LOADING LOGIC
        // ========================================

        async function loadUsers() {
            // TODO: Implementiere das Loading-Pattern
            // 1. Setze isLoading = true, error = null
            // 2. Rufe updateUI() auf
            // 3. try: fetchUsers() aufrufen, users + filteredUsers setzen
            // 4. catch: error.message in state.error speichern
            // 5. finally: isLoading = false, updateUI()

            // Dein Code hier:

        }

        // ========================================
        // TODO 3: SUCH-FILTER
        // ========================================

        function filterUsers(query) {
            // TODO: Implementiere die Suche
            // 1. Speichere query.toLowerCase() in state.searchQuery
            // 2. Wenn query leer: filteredUsers = users
            // 3. Sonst: Filtere users nach name ODER email (includes)
            // 4. Rufe updateUI() auf

            // Dein Code hier:

        }

        // ========================================
        // UI RENDERING (bereits fertig!)
        // ========================================

        function updateUI() {
            const content = document.querySelector('#content');
            const stats = document.querySelector('#stats');
            const loadBtn = document.querySelector('#loadBtn');

            loadBtn.disabled = state.isLoading;

            if (state.isLoading) {
                content.innerHTML = `
                    <div class="loading">
                        <div class="spinner"></div>
                        <p>Lädt User...</p>
                    </div>
                `;
                stats.textContent = 'Lädt...';
                return;
            }

            if (state.error) {
                content.innerHTML = `
                    <div class="error">
                        <p><strong>Fehler beim Laden!</strong></p>
                        <p>${escapeHtml(state.error)}</p>
                        <button onclick="loadUsers()">Erneut versuchen</button>
                    </div>
                `;
                stats.textContent = 'Fehler aufgetreten';
                return;
            }

            if (state.filteredUsers.length === 0) {
                content.innerHTML = `
                    <div class="empty">
                        <p>Keine User gefunden.</p>
                        ${state.searchQuery ? '<p>Versuche einen anderen Suchbegriff.</p>' : ''}
                    </div>
                `;
                stats.textContent = `0 von ${state.users.length} Usern`;
                return;
            }

            const usersHtml = state.filteredUsers.map(user => `
                <div class="user-card">
                    <h3>${escapeHtml(user.name)}</h3>
                    <p class="label">Email</p>
                    <p>${escapeHtml(user.email)}</p>
                    <p class="label">Stadt</p>
                    <p>${escapeHtml(user.address.city)}</p>
                    <p class="label">Firma</p>
                    <p>${escapeHtml(user.company.name)}</p>
                </div>
            `).join('');

            content.innerHTML = `<div class="user-grid">${usersHtml}</div>`;
            stats.textContent = `${state.filteredUsers.length} von ${state.users.length} Usern`;
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        // ========================================
        // EVENT LISTENER (bereits fertig!)
        // ========================================

        document.querySelector('#search').addEventListener('input', (e) => {
            filterUsers(e.target.value);
        });

        // ========================================
        // INITIALISIERUNG
        // ========================================

        loadUsers();
    </script>
</body>
</html>
```

### Hinweise zur Lösung

**TODO 1 - fetchUsers():**
- Nutze `await fetch(url)`
- Prüfe `if (!response.ok)` und wirf dann `throw new Error(...)`
- Return `response.json()`

**TODO 2 - loadUsers():**
- Nutze `try/catch/finally`
- `finally` wird IMMER ausgeführt (auch bei Fehler)

**TODO 3 - filterUsers():**
- `String.includes()` prüft ob Teilstring enthalten
- `.toLowerCase()` für case-insensitive Suche

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// TODO 1: API FUNKTION
async function fetchUsers() {
    const response = await fetch(`${API_URL}/users`);

    if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
    }

    return response.json();
}

// TODO 2: LOADING LOGIC
async function loadUsers() {
    state.isLoading = true;
    state.error = null;
    updateUI();

    try {
        const users = await fetchUsers();
        state.users = users;
        state.filteredUsers = users;
        state.error = null;
    } catch (error) {
        state.error = error.message;
        state.users = [];
        state.filteredUsers = [];
    } finally {
        state.isLoading = false;
        updateUI();
    }
}

// TODO 3: SUCH-FILTER
function filterUsers(query) {
    state.searchQuery = query.toLowerCase();

    if (!query.trim()) {
        state.filteredUsers = state.users;
    } else {
        state.filteredUsers = state.users.filter(user =>
            user.name.toLowerCase().includes(state.searchQuery) ||
            user.email.toLowerCase().includes(state.searchQuery)
        );
    }

    updateUI();
}
```

</details>

### Teste die App

1. Öffne die HTML-Datei im Browser
2. User sollten automatisch laden (Loading → Success)
3. Gib einen Namen in die Suche ein → Live-Filter
4. Trenne dein Internet und klicke "Neu laden" → Error State
5. Verbinde Internet und klicke "Erneut versuchen" → Success

---

## Teil 11: Bonus - Wetter-App

Baue eine Wetter-App mit einer echten API!

### Aufgabe

Erstelle `wetter-app.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wetter-App</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #74b9ff, #0984e3);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }

        .search-form {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }

        .search-input {
            flex: 1;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
        }

        .search-input:focus {
            outline: none;
            border-color: #0984e3;
        }

        .search-btn {
            padding: 15px 25px;
            background: #0984e3;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
        }

        .search-btn:hover {
            background: #0770c2;
        }

        .search-btn:disabled {
            background: #ccc;
        }

        #result {
            min-height: 200px;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid #0984e3;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .error {
            background: #fee2e2;
            color: #991b1b;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .weather {
            text-align: center;
        }

        .weather-city {
            font-size: 28px;
            color: #333;
            margin-bottom: 10px;
        }

        .weather-temp {
            font-size: 64px;
            font-weight: bold;
            color: #0984e3;
            margin-bottom: 10px;
        }

        .weather-desc {
            font-size: 20px;
            color: #666;
            margin-bottom: 20px;
        }

        .weather-details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }

        .detail {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
        }

        .detail-label {
            font-size: 12px;
            color: #888;
            text-transform: uppercase;
        }

        .detail-value {
            font-size: 18px;
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Wetter-App</h1>

        <form class="search-form" onsubmit="handleSearch(event)">
            <input
                type="text"
                id="cityInput"
                class="search-input"
                placeholder="Stadt eingeben..."
                required
            >
            <button type="submit" class="search-btn" id="searchBtn">
                Suchen
            </button>
        </form>

        <div id="result">
            <p style="text-align: center; color: #888;">
                Gib eine Stadt ein, um das Wetter zu sehen.
            </p>
        </div>
    </div>

    <script>
        // ========================================
        // WETTER-APP
        // ========================================

        // wttr.in ist eine kostenlose Wetter-API ohne API-Key!
        const API_BASE = 'https://wttr.in';

        let state = {
            weather: null,
            isLoading: false,
            error: null
        };

        // ========================================
        // API FUNKTION
        // ========================================

        async function fetchWeather(city) {
            // wttr.in gibt JSON zurück mit ?format=j1
            const url = `${API_BASE}/${encodeURIComponent(city)}?format=j1`;

            const response = await fetch(url);

            if (!response.ok) {
                throw new Error('Stadt nicht gefunden');
            }

            const data = await response.json();

            // Daten extrahieren
            const current = data.current_condition[0];
            const location = data.nearest_area[0];

            return {
                city: location.areaName[0].value,
                country: location.country[0].value,
                temp: current.temp_C,
                feelsLike: current.FeelsLikeC,
                humidity: current.humidity,
                windSpeed: current.windspeedKmph,
                description: current.weatherDesc[0].value
            };
        }

        // ========================================
        // EVENT HANDLER
        // ========================================

        async function handleSearch(event) {
            event.preventDefault();

            const cityInput = document.querySelector('#cityInput');
            const city = cityInput.value.trim();

            if (!city) return;

            // Loading starten
            state.isLoading = true;
            state.error = null;
            updateUI();

            try {
                state.weather = await fetchWeather(city);
                state.error = null;
            } catch (error) {
                state.error = error.message;
                state.weather = null;
            } finally {
                state.isLoading = false;
                updateUI();
            }
        }

        // ========================================
        // UI RENDERING
        // ========================================

        function updateUI() {
            const result = document.querySelector('#result');
            const searchBtn = document.querySelector('#searchBtn');

            searchBtn.disabled = state.isLoading;

            // Loading
            if (state.isLoading) {
                result.innerHTML = `
                    <div class="loading">
                        <div class="spinner"></div>
                        <p>Lädt Wetter...</p>
                    </div>
                `;
                return;
            }

            // Error
            if (state.error) {
                result.innerHTML = `
                    <div class="error">
                        <p><strong>Fehler!</strong></p>
                        <p>${escapeHtml(state.error)}</p>
                    </div>
                `;
                return;
            }

            // Success
            if (state.weather) {
                const w = state.weather;
                result.innerHTML = `
                    <div class="weather">
                        <div class="weather-city">${escapeHtml(w.city)}, ${escapeHtml(w.country)}</div>
                        <div class="weather-temp">${w.temp}°C</div>
                        <div class="weather-desc">${escapeHtml(w.description)}</div>

                        <div class="weather-details">
                            <div class="detail">
                                <div class="detail-label">Gefühlt</div>
                                <div class="detail-value">${w.feelsLike}°C</div>
                            </div>
                            <div class="detail">
                                <div class="detail-label">Luftfeuchtigkeit</div>
                                <div class="detail-value">${w.humidity}%</div>
                            </div>
                            <div class="detail">
                                <div class="detail-label">Wind</div>
                                <div class="detail-value">${w.windSpeed} km/h</div>
                            </div>
                        </div>
                    </div>
                `;
            }
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    </script>
</body>
</html>
```

**Teste die App:**
1. Öffne im Browser
2. Gib "Berlin" ein → Wetter wird geladen
3. Gib "xyz123" ein → Fehler wird gezeigt
4. Probiere verschiedene Städte: München, Wien, Zürich

---

## Zusammenfassung

### Was du heute gelernt hast

| Thema | Konzept | Beispiel |
|-------|---------|----------|
| **Fetch** | HTTP-Requests aus dem Browser | `fetch('/api/users')` |
| **Promises** | Asynchrone Operationen | `.then()`, `.catch()` |
| **Async/Await** | Moderne, lesbare Syntax | `const data = await fetch()` |
| **JSON** | Datenformat für Web-APIs | `JSON.parse()`, `JSON.stringify()` |
| **Error Handling** | Fehler richtig behandeln | `try/catch`, `response.ok` |
| **Loading States** | Bessere User Experience | Loading → Error → Success |
| **CORS** | Cross-Origin Sicherheit | Server muss Header setzen |

### Die wichtigsten Patterns

```javascript
// 1. Basic Fetch mit async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Fehler:', error.message);
        return null;
    }
}

// 2. POST Request
async function createItem(data) {
    const response = await fetch('/api/items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return response.json();
}

// 3. Loading State Pattern
let state = { data: null, isLoading: false, error: null };

async function loadData() {
    state.isLoading = true;
    updateUI();

    try {
        state.data = await fetchData();
    } catch (error) {
        state.error = error.message;
    } finally {
        state.isLoading = false;
        updateUI();
    }
}
```

### React Vorschau

In React macht ihr das Gleiche – nur eleganter:

```javascript
// React mit useState und useEffect
function UserList() {
    const [users, setUsers] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function loadUsers() {
            try {
                const response = await fetch('/api/users');
                setUsers(await response.json());
            } catch (err) {
                setError(err.message);
            } finally {
                setIsLoading(false);
            }
        }
        loadUsers();
    }, []);

    if (isLoading) return <Spinner />;
    if (error) return <Error message={error} />;
    return <UserGrid users={users} />;
}
```

**Die Konzepte bleiben gleich, nur die Syntax ändert sich!**

---

## Checkliste

Bevor du mit dem nächsten Tag weitermachst, stelle sicher:

- [ ] Du verstehst den Unterschied zwischen synchron und asynchron
- [ ] Du kannst `fetch()` für GET und POST Requests verwenden
- [ ] Du verstehst Promise States (Pending, Fulfilled, Rejected)
- [ ] Du kannst async/await sicher anwenden
- [ ] Du weißt, warum `response.ok` geprüft werden muss
- [ ] Du kannst JSON parsen und erstellen
- [ ] Du weißt, was CORS ist und wie man es löst


---

## Bonus: Schnellreferenz

### Fetch Grundlagen

```javascript
// GET (Standard)
const response = await fetch('/api/data');
const data = await response.json();

// POST
const response = await fetch('/api/data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ key: 'value' })
});

// PUT, PATCH, DELETE
const response = await fetch('/api/data/1', {
    method: 'PUT',  // oder 'PATCH' oder 'DELETE'
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ key: 'newValue' })
});
```

### Async/Await

```javascript
// Async Function
async function fetchData() {
    const response = await fetch('/api');
    return response.json();
}

// Async Arrow Function
const fetchData = async () => {
    const response = await fetch('/api');
    return response.json();
};

// Parallele Requests
const [users, posts] = await Promise.all([
    fetch('/api/users').then(r => r.json()),
    fetch('/api/posts').then(r => r.json())
]);
```

### Error Handling

```javascript
async function safeFetch(url) {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return { data: await response.json(), error: null };
    } catch (error) {
        return { data: null, error: error.message };
    }
}
```

### JSON

```javascript
// String → Object
const obj = JSON.parse('{"name": "Max"}');

// Object → String
const json = JSON.stringify({ name: 'Max' });

// Schön formatiert
const pretty = JSON.stringify(obj, null, 2);
```

### Loading States

```javascript
let state = { data: null, isLoading: false, error: null };

async function loadData() {
    // Spread-Operator (...) kopiert alle bisherigen Properties
    state = { ...state, isLoading: true, error: null };
    updateUI();

    try {
        state.data = await fetchData();
    } catch (error) {
        state.error = error.message;
    } finally {
        state.isLoading = false;
        updateUI();
    }
}
```
