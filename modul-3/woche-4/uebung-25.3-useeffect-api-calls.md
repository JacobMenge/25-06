# useEffect & API Calls - Praktische Übung

## Übersicht

Willkommen zur Übung zu `useEffect` und API Calls in React! Du hast bereits `useState` kennengelernt und weißt, wie du Komponenten ein Gedächtnis gibst. Jetzt lernst du, wie du **Daten von externen APIs lädst** und in deinen Komponenten anzeigst – ein absolutes Kernkonzept für jede echte React-Anwendung.

In dieser Übung lernst du:
- **APIs verstehen** - Was APIs sind und wie der Request-Response-Cycle funktioniert
- **fetch & Promises** - Die fetch API und Promise-Syntax auffrischen
- **async/await** - Die moderne, lesbare Alternative zu `.then()`-Ketten
- **useEffect** - Seiteneffekte in React kontrolliert ausführen
- **Dependency Array** - Steuern, wann ein Effekt erneut ausgeführt wird
- **Loading & Error States** - Professionelle UX mit Lade- und Fehlerzuständen
- **Custom Hook: useFetch** - Einen wiederverwendbaren Daten-Hook erstellen

Diese Übung baut auf "24.3 useState & Controlled Inputs" und "25.2 Hooks in React" auf – stelle sicher, dass du `useState`, `useEffect`-Grundlagen und Custom Hooks verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | APIs & Asynchrones JavaScript | 5 min (lesen) |
| **Teil 1** | fetch & Promises auffrischen | 15 min |
| **Teil 2** | async/await: Die moderne Syntax | 15 min |
| **Teil 3** | useEffect verstehen | 20 min |
| **Teil 4** | useEffect mit API Calls | 25 min |
| **Teil 5** | Dependency Array verstehen | 20 min |
| **Teil 6** | Loading & Error States | 25 min |
| **Teil 7** | Custom Hook: useFetch | 30 min |
| **Teil 8** | Praxis: Wetter-Dashboard mit API | 40 min |
| | **Gesamt** | **ca. 3 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - APIs & Async-Grundlagen
2. **Teil 2** - async/await - *Syntax verstehen*
3. **Teil 3** - useEffect verstehen - *Kernkonzept*
4. **Teil 4** - useEffect mit API Calls - *Wichtigste Anwendung*
5. **Teil 6** - Loading & Error States - *Professionelle UX*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast **Node.js v20.19+** oder **v22.12+** installiert (ältere Versionen wie Node 18 funktionieren mit aktuellen Vite-Versionen nicht mehr – prüfe mit `node -v`)
2. Du hast ein funktionierendes React-Projekt (aus den vorherigen Übungen)
3. Der Dev-Server läuft (`npm run dev`)
4. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest api-uebung -- --template react
cd api-uebung
npm install
npm run dev
```

> **Tipp für diese Übung:** Du wirst mehrere Komponenten bauen. Um Verwirrung zu vermeiden: **Rendere immer nur eine Übungskomponente gleichzeitig in `App.jsx`**. Kommentiere die anderen aus, während du an einer neuen arbeitest.

> **Wichtig:** Für API Calls brauchst du eine aktive Internetverbindung. Die APIs, die wir verwenden, sind kostenlos und benötigen keinen API-Key.

---

## Rückblick: APIs & Asynchrones JavaScript

### Was ist eine API?

API steht für **Application Programming Interface** – eine Schnittstelle, über die wir mit einem Server kommunizieren. Im Web-Kontext senden wir HTTP-Anfragen und bekommen Daten (meist als JSON) zurück.

```
┌─────────────────────────────────────────────────────────────┐
│              REQUEST-RESPONSE CYCLE                         │
│                                                             │
│   Browser (Client)                Server (API)              │
│   ┌──────────┐                     ┌──────────┐             │
│   │          │ ── HTTP Request ──> │          │             │
│   │  React   │                     │  Daten-  │             │
│   │   App    │ <── HTTP Response ──│  bank    │             │
│   └──────────┘                     └──────────┘             │
│                                                             │
│   Beispiel:                                                 │
│   GET https://api.example.com/users                         │
│   → Response: [{ "name": "Max" }, { "name": "Lisa" }]       │
└─────────────────────────────────────────────────────────────┘
```

### Warum asynchron?

API-Calls dauern Zeit (Netzwerk, Server-Verarbeitung). JavaScript ist **synchron** – es führt eine Zeile nach der anderen aus. Ohne asynchrone Mechanismen würde die gesamte App einfrieren, während wir auf eine API-Antwort warten.

### Zwei Wege für asynchronen Code

| Ansatz | Syntax | Lesbarkeit |
|--------|--------|------------|
| **Promises mit `.then()`** | `fetch(url).then(res => ...)` | Verkettung, kann unübersichtlich werden |
| **async/await** | `const res = await fetch(url)` | Liest sich wie synchroner Code |

Wir verwenden in dieser Übung bevorzugt **async/await** – die modernere und lesbarere Variante.

---

## Teil 1: fetch & Promises auffrischen

### Wie funktioniert fetch?

`fetch()` ist eine eingebaute Browser-API, die HTTP-Anfragen durchführt. Sie gibt ein **Promise** zurück:

```javascript
// fetch gibt ein Promise zurück
const promise = fetch('https://jsonplaceholder.typicode.com/users');
// promise ist NICHT die Antwort, sondern ein "Versprechen" auf eine Antwort
```

### Die Promise-Kette mit .then()

```javascript
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())  // Response zu JSON umwandeln
  .then(data => {
    console.log(data);                // Daten verwenden
  })
  .catch(error => {
    console.error('Fehler:', error);  // Fehler abfangen
  });
```

### Warum zwei .then()?

```
┌─────────────────────────────────────────────────────────────┐
│              FETCH IN ZWEI SCHRITTEN                        │
│                                                             │
│   fetch(url)                                                │
│     │                                                       │
│     ▼                                                       │
│   1. .then(response => response.json())                     │
│      → Response-Objekt kommt an (Headers, Status, etc.)     │
│      → .json() liest den Body und parsed ihn                │
│      → Gibt NEUES Promise zurück!                           │
│     │                                                       │
│     ▼                                                       │
│   2. .then(data => { ... })                                 │
│      → Jetzt haben wir die echten Daten als JS-Objekt       │
│                                                             │
│   Wichtig: response.json() ist selbst asynchron!            │
└─────────────────────────────────────────────────────────────┘
```

### Übung 1: fetch ausprobieren

> **Ziel:** Die fetch-Syntax in der Browserkonsole ausprobieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Daten von einer API in der Konsole siehst

**Aufgabe:**

1. Öffne deinen Browser und drücke F12 (DevTools)
2. Gehe in den **Console**-Tab
3. Führe folgenden Code aus:

```javascript
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => response.json())
  .then(data => {
    console.log('Name:', data.name);
    console.log('Email:', data.email);
    console.log('Stadt:', data.address.city);
  })
  .catch(error => console.error('Fehler:', error));
```

4. Probiere auch diese URL: `https://jsonplaceholder.typicode.com/posts?_limit=3`

5. **Teste einen Fehler:** Was passiert, wenn du eine falsche URL verwendest?

```javascript
fetch('https://jsonplaceholder.typicode.com/FALSCHE_URL')
  .then(response => {
    console.log('Status:', response.status); // Was steht hier?
    console.log('OK?', response.ok);         // true oder false?
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Fehler:', error));
```

<details>
<summary>Wichtige Erkenntnis anzeigen</summary>

**Achtung:** `fetch` wirft bei HTTP-Fehlern (404, 500) **keinen** Fehler! Der `.catch()`-Block wird nur bei Netzwerkfehlern ausgeführt (z.B. kein Internet). Bei einem 404 kommt trotzdem eine Response – du musst `response.ok` selbst prüfen!

```javascript
// FALSCH – Das fängt KEINEN 404-Fehler ab:
fetch('https://api.example.com/not-found')
  .then(res => res.json())  // Wird trotzdem ausgeführt!
  .catch(err => ...)        // Wird NICHT ausgeführt bei 404

// RICHTIG – So prüfst du korrekt:
fetch('https://api.example.com/not-found')
  .then(res => {
    if (!res.ok) {
      throw new Error(`HTTP-Fehler: ${res.status}`);
    }
    return res.json();
  })
  .catch(err => console.error(err)); // Jetzt wird der 404 gefangen
```

</details>

---

## Teil 2: async/await – Die moderne Syntax

### Das Problem mit .then()-Ketten

Die Promise-Syntax mit `.then()` funktioniert, wird aber schnell unübersichtlich – besonders mit Fehlerbehandlung:

```javascript
// SCHLECHT – Schwer zu lesen bei komplexerer Logik
fetch(url)
  .then(response => {
    if (!response.ok) throw new Error(`Fehler: ${response.status}`);
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
```

### Die Lösung: async/await

`async/await` lässt asynchronen Code aussehen wie synchronen Code:

```javascript
// GUT – Gut lesbar mit async/await
async function fetchUser() {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP-Fehler: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);

    return data;
  } catch (error) {
    console.error('Fehler beim Fetch:', error);
  }
}
```

### Die Regeln von async/await

```
┌─────────────────────────────────────────────────────────────┐
│              ASYNC/AWAIT REGELN                             │
│                                                             │
│   1. async vor die Funktion schreiben                       │
│      → async function myFunc() { ... }                      │
│      → const myFunc = async () => { ... }                   │
│                                                             │
│   2. await vor jeden Aufruf der ein Promise zurückgibt      │
│      → const res = await fetch(url)                         │
│      → const data = await res.json()                        │
│                                                             │
│   3. await darf NUR in async-Funktionen stehen              │
│      → Nicht auf Top-Level in Komponenten!                  │
│                                                             │
│   4. Fehlerbehandlung mit try/catch                         │
│      → Bekannt aus synchronem Code                          │
│      → Fängt Netzwerk-Fehler automatisch                    │
│      → Fängt HTTP-Fehler (404, 500) NUR wenn du selbst      │
│        bei !response.ok einen Error wirfst!                 │
└─────────────────────────────────────────────────────────────┘
```

### Übung 2: async/await verwenden

> **Ziel:** Eine async/await Funktion schreiben und aufrufen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du eine wiederverwendbare Fetch-Funktion hast

**Aufgabe:**

1. Erstelle eine Datei `src/api/fetchUsers.js`:

```javascript
// src/api/fetchUsers.js

// Aufgabe 1: Schreibe eine async-Funktion die User von der API lädt
// URL: https://jsonplaceholder.typicode.com/users
// Die Funktion soll:
// - fetch mit await aufrufen
// - Prüfen ob response.ok ist (sonst Error werfen)
// - Die JSON-Daten zurückgeben
// - Fehler mit try/catch abfangen und loggen

export async function fetchUsers() {
  // Dein Code hier
}

// Aufgabe 2: Schreibe eine Funktion die einen einzelnen User lädt
// URL: https://jsonplaceholder.typicode.com/users/{id}
// Parameter: id (Number)

export async function fetchUserById(id) {
  // Dein Code hier
}
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/api/fetchUsers.js

export async function fetchUsers() {
  try {
    const response = await fetch(
      'https://jsonplaceholder.typicode.com/users'
    );

    if (!response.ok) {
      throw new Error(`HTTP-Fehler: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fehler beim Laden der User:', error);
    throw error; // Fehler weiterwerfen, damit der Aufrufer reagieren kann
  }
}

export async function fetchUserById(id) {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/users/${id}`
    );

    if (!response.ok) {
      throw new Error(`HTTP-Fehler: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error(`Fehler beim Laden von User ${id}:`, error);
    throw error;
  }
}
```

> **Warum `throw error` im catch?**
> Wir loggen den Fehler, werfen ihn aber weiter (`throw error`). So kann die Komponente, die unsere Funktion aufruft, selbst entscheiden, wie sie den Fehler dem User anzeigt.

</details>

### Wissensfrage 1

Was ist der Unterschied zwischen `.then().catch()` und `async/await` mit `try/catch`?

<details>
<summary>Antwort anzeigen</summary>

Funktional gibt es **keinen Unterschied** – beide arbeiten mit Promises. Der Unterschied liegt in der **Lesbarkeit**:

- `.then().catch()` verkettet Callbacks – bei komplexer Logik verschachtelt und schwer zu lesen
- `async/await` mit `try/catch` liest sich wie synchroner Code – linearer Ablauf, vertraute Fehlerbehandlung

`async/await` ist **syntaktischer Zucker** über Promises. Unter der Haube passiert dasselbe.

**Faustregel:** Verwende `async/await` für neue Projekte – es ist die bevorzugte Schreibweise in der React-Community.

</details>

---

## Teil 3: useEffect verstehen

### Das Problem: Wo den API-Call machen?

Du könntest versucht sein, den API-Call direkt im Funktionskörper der Komponente zu machen:

```javascript
// FALSCH – API-Call direkt im Render
function UserList() {
  const [users, setUsers] = useState([]);

  // Das wird bei JEDEM Render aufgerufen!
  // setUsers löst einen Re-Render aus → erneuter fetch → erneutes setUsers → ...
  // → ENDLOSSCHLEIFE!
  fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then(data => setUsers(data));

  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

### Die Lösung: useEffect

`useEffect` gibt dir die Kontrolle darüber, **wann** ein Seiteneffekt ausgeführt wird:

```javascript
import { useState, useEffect } from 'react';

// RICHTIG – API-Call in useEffect
function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Dieser Code läuft NACH dem Render
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []); // ← Leeres Array = nur beim ersten Mount

  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

### Wie useEffect funktioniert

```
┌─────────────────────────────────────────────────────────────┐
│                    useEffect                                │
│                                                             │
│   useEffect(callback, dependencyArray)                      │
│                │                │                           │
│                │                └── WANN soll der Effekt    │
│                │                    ausgeführt werden?      │
│                └── WAS soll ausgeführt werden?              │
│                                                             │
│   Drei Varianten des Dependency Arrays:                     │
│                                                             │
│   useEffect(() => { ... })        → Bei JEDEM Render        │
│   useEffect(() => { ... }, [])    → Nur beim ERSTEN Mount   │
│   useEffect(() => { ... }, [a,b]) → Wenn a ODER b sich      │
│                                     ändert                  │
│                                                             │
│  Für API-Calls beim Laden: useEffect(..., [])               │
│  Für API-Calls bei Änderungen: useEffect(..., [suchbegriff])│
└─────────────────────────────────────────────────────────────┘
```

### Wichtig: async und useEffect

Die useEffect-Callback-Funktion darf **nicht** direkt `async` sein! Stattdessen definierst du eine async-Funktion **innerhalb** des useEffect und rufst sie auf:

```javascript
// FALSCH – useEffect-Callback darf nicht async sein
useEffect(async () => {
  const data = await fetch(url);
  // ...
}, []);

// RICHTIG – async-Funktion im useEffect definieren und aufrufen
useEffect(() => {
  async function loadData() {
    const response = await fetch(url);
    const data = await response.json();
    setUsers(data);
  }

  loadData();
}, []);
```

> **Warum?** `useEffect` erwartet, dass der Callback entweder `undefined` oder eine **Cleanup-Funktion** zurückgibt. Eine `async`-Funktion gibt immer ein Promise zurück – das kann React nicht als Cleanup verwenden.

### Übung 3: Erster useEffect mit API

> **Ziel:** Daten von einer API laden und anzeigen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Eine Liste von Usern im Browser angezeigt wird

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/UserList.jsx`:

```javascript
// src/components/UserList.jsx
import { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);

  // Aufgabe 1: Verwende useEffect um User von der API zu laden
  // URL: https://jsonplaceholder.typicode.com/users
  // Tipp: Definiere eine async-Funktion INNERHALB des useEffect
  // Tipp: Verwende ein leeres Dependency Array []

  // useEffect(() => {
  //   ???
  // }, []);

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', padding: '24px' }}>
      <h2>Benutzerliste</h2>
      <p>{users.length} Benutzer geladen</p>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map(user => (
          <li key={user.id} style={{
            padding: '12px',
            borderBottom: '1px solid #eee',
            display: 'flex',
            justifyContent: 'space-between'
          }}>
            <div>
              <strong>{user.name}</strong>
              <br />
              <span style={{ color: '#666', fontSize: '14px' }}>
                {user.email}
              </span>
            </div>
            <span style={{ color: '#999', fontSize: '14px' }}>
              {user.company.name}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
```

2. Binde die Komponente in `App.jsx` ein:

```javascript
import UserList from './components/UserList'

function App() {
  return (
    <div className="app">
      <h1>useEffect & API Calls</h1>
      <UserList />
    </div>
  )
}

export default App
```

3. **Bonus:** Öffne die DevTools (F12) → Network-Tab. Siehst du den API-Call? Wie oft wird er gemacht?

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/UserList.jsx
import { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function loadUsers() {
      try {
        const response = await fetch(
          'https://jsonplaceholder.typicode.com/users'
        );

        if (!response.ok) {
          throw new Error(`HTTP-Fehler: ${response.status}`);
        }

        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error('Fehler beim Laden:', error);
      }
    }

    loadUsers();
  }, []); // Leeres Array = nur einmal beim Mount

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', padding: '24px' }}>
      <h2>Benutzerliste</h2>
      <p>{users.length} Benutzer geladen</p>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map(user => (
          <li key={user.id} style={{
            padding: '12px',
            borderBottom: '1px solid #eee',
            display: 'flex',
            justifyContent: 'space-between'
          }}>
            <div>
              <strong>{user.name}</strong>
              <br />
              <span style={{ color: '#666', fontSize: '14px' }}>
                {user.email}
              </span>
            </div>
            <span style={{ color: '#999', fontSize: '14px' }}>
              {user.company.name}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
```

> **Zum Network-Tab:** Du solltest genau **einen** Fetch-Request sehen (oder zwei im StrictMode in der Entwicklung – das ist normal und passiert nur in `npm run dev`). Das leere Dependency Array `[]` stellt sicher, dass der Effekt nur beim Mount ausgeführt wird.
>
> **Wichtig zu wissen:** React garantiert nicht, dass ein Effekt nur *genau einmal* läuft – der StrictMode führt absichtlich einen extra Setup+Cleanup-Zyklus aus, um Bugs aufzudecken. Deshalb gilt: Effekte sollten **idempotent** sein (d.h. es schadet nicht, wenn sie mehrfach laufen). Bei API-Calls ist das normalerweise kein Problem, da ein zweiter GET-Request nur die gleichen Daten nochmal holt.

</details>

---

## Teil 4: useEffect mit API Calls – Pattern vertiefen

### Das Standard-Pattern für API Calls in React

```javascript
import { useState, useEffect } from 'react';

function DataComponent() {
  // 1. State für die Daten
  const [data, setData] = useState(null);

  // 2. useEffect für den API Call
  useEffect(() => {
    async function fetchData() {
      const response = await fetch('https://api.example.com/data');
      const result = await response.json();
      setData(result);
    }

    fetchData();
  }, []);

  // 3. Render – mit Null-Check!
  if (!data) return <p>Lade Daten...</p>;

  return <div>{/* data verwenden */}</div>;
}
```

### Übung 4: Posts mit User-Auswahl laden

> **Ziel:** API-Calls abhängig von User-Input machen
> **Zeitbedarf:** ca. 25 Minuten
> **Du bist fertig, wenn:** Du Posts eines ausgewählten Users siehst

**Aufgabe:**

Erstelle eine Komponente, die:
1. Beim Laden alle User von der API holt
2. Den ausgewählten User in einem Dropdown anzeigt
3. Die Posts des ausgewählten Users lädt und anzeigt

1. Erstelle `src/components/UserPosts.jsx`:

```javascript
// src/components/UserPosts.jsx
import { useState, useEffect } from 'react';

function UserPosts() {
  const [users, setUsers] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState('');
  const [posts, setPosts] = useState([]);

  // Aufgabe 1: Lade alle User beim Mount
  // URL: https://jsonplaceholder.typicode.com/users
  useEffect(() => {
    // Dein Code hier
  }, []);

  // Aufgabe 2: Lade Posts wenn sich selectedUserId ändert
  // URL: https://jsonplaceholder.typicode.com/posts?userId={selectedUserId}
  // Tipp: Lade KEINE Posts wenn selectedUserId leer ist!
  // Tipp: Was muss ins Dependency Array?
  useEffect(() => {
    // Dein Code hier
  }, [/* ??? */]);

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', padding: '24px' }}>
      <h2>User Posts</h2>

      {/* Aufgabe 3: User-Dropdown */}
      <select
        value={selectedUserId}
        onChange={(e) => setSelectedUserId(e.target.value)}
        style={{ padding: '10px', fontSize: '16px', width: '100%', marginBottom: '24px' }}
      >
        <option value="">-- Benutzer auswählen --</option>
        {users.map(user => (
          <option key={user.id} value={user.id}>
            {user.name}
          </option>
        ))}
      </select>

      {/* Posts anzeigen */}
      {selectedUserId === '' ? (
        <p style={{ color: '#999', textAlign: 'center' }}>
          Wähle einen Benutzer aus, um seine Posts zu sehen.
        </p>
      ) : (
        <div>
          <h3>{posts.length} Posts gefunden</h3>
          {posts.map(post => (
            <div key={post.id} style={{
              padding: '16px',
              marginBottom: '12px',
              border: '1px solid #eee',
              borderRadius: '8px'
            }}>
              <h4 style={{ margin: '0 0 8px 0' }}>{post.title}</h4>
              <p style={{ margin: 0, color: '#666', fontSize: '14px' }}>
                {post.body}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default UserPosts;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/UserPosts.jsx
import { useState, useEffect } from 'react';

function UserPosts() {
  const [users, setUsers] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState('');
  const [posts, setPosts] = useState([]);

  // User laden beim Mount
  useEffect(() => {
    async function loadUsers() {
      try {
        const response = await fetch(
          'https://jsonplaceholder.typicode.com/users'
        );

        if (!response.ok) {
          throw new Error(`HTTP-Fehler: ${response.status}`);
        }

        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error('Fehler beim Laden der User:', error);
      }
    }

    loadUsers();
  }, []);

  // Posts laden wenn User ausgewählt wird
  useEffect(() => {
    // Nichts laden wenn kein User ausgewählt
    if (!selectedUserId) {
      setPosts([]);
      return;
    }

    async function loadPosts() {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/posts?userId=${selectedUserId}`
        );

        if (!response.ok) {
          throw new Error(`HTTP-Fehler: ${response.status}`);
        }

        const data = await response.json();
        setPosts(data);
      } catch (error) {
        console.error('Fehler beim Laden der Posts:', error);
      }
    }

    loadPosts();
  }, [selectedUserId]); // ← Erneut ausführen wenn sich die User-ID ändert!

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', padding: '24px' }}>
      <h2>User Posts</h2>

      <select
        value={selectedUserId}
        onChange={(e) => setSelectedUserId(e.target.value)}
        style={{ padding: '10px', fontSize: '16px', width: '100%', marginBottom: '24px' }}
      >
        <option value="">-- Benutzer auswählen --</option>
        {users.map(user => (
          <option key={user.id} value={user.id}>
            {user.name}
          </option>
        ))}
      </select>

      {selectedUserId === '' ? (
        <p style={{ color: '#999', textAlign: 'center' }}>
          Wähle einen Benutzer aus, um seine Posts zu sehen.
        </p>
      ) : (
        <div>
          <h3>{posts.length} Posts gefunden</h3>
          {posts.map(post => (
            <div key={post.id} style={{
              padding: '16px',
              marginBottom: '12px',
              border: '1px solid #eee',
              borderRadius: '8px'
            }}>
              <h4 style={{ margin: '0 0 8px 0' }}>{post.title}</h4>
              <p style={{ margin: 0, color: '#666', fontSize: '14px' }}>
                {post.body}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default UserPosts;
```

> **Warum `[selectedUserId]` im Dependency Array?**
> Wir wollen, dass der Posts-Fetch **erneut** ausgeführt wird, sobald der Benutzer einen anderen User auswählt. React vergleicht den alten mit dem neuen Wert von `selectedUserId` – hat sich etwas geändert, läuft der Effekt erneut.

> **Warum der Early Return bei leerem `selectedUserId`?**
> Ohne den Check würden wir `posts?userId=` ohne ID an die API senden. Das wäre entweder ein Fehler oder würde alle Posts zurückgeben – beides ungewollt. Der Early Return setzt die Posts auf ein leeres Array zurück.

</details>

---

## Teil 5: Dependency Array verstehen

### Die drei Varianten im Überblick

```javascript
// Variante 1: Kein Dependency Array → bei JEDEM Render
useEffect(() => {
  console.log('Läuft bei jedem Render');
});

// Variante 2: Leeres Array → nur beim Mount (einmal)
useEffect(() => {
  console.log('Läuft nur einmal beim ersten Mount');
}, []);

// Variante 3: Mit Dependencies → wenn sich Werte ändern
useEffect(() => {
  console.log('Läuft wenn searchTerm sich ändert');
}, [searchTerm]);
```

### Wann welche Variante?

| Dependency Array | Wann es läuft | Typischer Anwendungsfall |
|-----------------|---------------|-------------------------|
| Kein Array | Bei jedem Render | Fast nie sinnvoll! |
| `[]` | Einmal beim Mount | Initiale Daten laden |
| `[variable]` | Wenn `variable` sich ändert | Suche, Filter, Navigation |
| `[a, b]` | Wenn `a` ODER `b` sich ändert | Mehrere Abhängigkeiten |

### Übung 5: Dependency Array erkunden

> **Ziel:** Das Verhalten des Dependency Arrays verstehen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du vorhersagen kannst wann ein Effekt läuft

**Aufgabe:** Erstelle `src/components/EffectDemo.jsx` und beobachte die Konsole:

```javascript
// src/components/EffectDemo.jsx
import { useState, useEffect } from 'react';

function EffectDemo() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  // Aufgabe 1: Was wird in der Konsole erscheinen?
  // Tipp: Klicke den Button und tippe in das Input

  useEffect(() => {
    console.log('Effekt A: Läuft bei jedem Render');
  });

  useEffect(() => {
    console.log('Effekt B: Läuft nur beim Mount');
  }, []);

  useEffect(() => {
    console.log('Effekt C: count hat sich geändert:', count);
  }, [count]);

  useEffect(() => {
    console.log('Effekt D: text hat sich geändert:', text);
  }, [text]);

  useEffect(() => {
    console.log('Effekt E: count ODER text hat sich geändert');
  }, [count, text]);

  return (
    <div style={{ maxWidth: '400px', margin: '40px auto', padding: '24px' }}>
      <h2>Dependency Array Demo</h2>

      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Count +1
      </button>

      <div style={{ marginTop: '16px' }}>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Tippe etwas..."
          style={{ padding: '8px', width: '100%', boxSizing: 'border-box' }}
        />
      </div>

      <p style={{ fontSize: '12px', color: '#999', marginTop: '16px' }}>
        Öffne die Konsole (F12) und beobachte welche Effekte laufen!
      </p>
    </div>
  );
}

export default EffectDemo;
```

**Fragen zum Nachdenken:**

1. Welche Effekte laufen beim ersten Laden der Seite?
2. Welche Effekte laufen, wenn du den Button klickst?
3. Welche Effekte laufen, wenn du ins Textfeld tippst?
4. Gibt es einen Effekt, der bei beiden Aktionen läuft?

<details>
<summary>Antworten anzeigen</summary>

1. **Beim ersten Laden:** ALLE Effekte (A, B, C, D, E) laufen – jeder Effekt wird mindestens einmal beim Mount ausgeführt.

2. **Button klicken:** Effekte A, C und E laufen
   - A: Läuft bei jedem Render (kein Dependency Array)
   - C: `count` hat sich geändert
   - E: `count` ODER `text` – da `count` sich geändert hat

3. **Ins Textfeld tippen:** Effekte A, D und E laufen
   - A: Läuft bei jedem Render
   - D: `text` hat sich geändert
   - E: `count` ODER `text` – da `text` sich geändert hat

4. **Effekt A und E** laufen bei beiden Aktionen (A immer, E weil beide Variablen im Array stehen).

**Wichtige Erkenntnis:** Effekt B läuft **nur einmal** beim Mount – egal was danach passiert. Das ist das Pattern für initiale API-Calls!

</details>

---

## Teil 6: Loading & Error States

### Das Problem: Leere Seite beim Laden

Ohne Loading-State sieht der User kurz eine leere Seite, bevor die Daten da sind. Ohne Error-State erfährt er nie, wenn etwas schiefgeht.

### Professionelles Pattern: Drei States

```
┌─────────────────────────────────────────────────────────────┐
│              DREI STATES FÜR API CALLS                      │
│                                                             │
│   ┌─────────┐    ┌─────────┐    ┌──────────┐                │
│   │ Loading │ ──>│ Success │    │  Error   │                │
│   │  true   │    │  data   │    │ message  │                │
│   └─────────┘    └─────────┘    └──────────┘                │
│        │              ▲               ▲                     │
│        └──────────────┴───────────────┘                     │
│           fetch()   Response OK    Response Error           │
│                                                             │
│   State-Variablen:                                          │
│   const [data, setData] = useState(null);                   │
│   const [loading, setLoading] = useState(true);             │
│   const [error, setError] = useState(null);                 │
└─────────────────────────────────────────────────────────────┘
```

### Übung 6: Loading & Error States implementieren

> **Ziel:** Professionelle Lade- und Fehlerzustände in einer Komponente
> **Zeitbedarf:** ca. 25 Minuten
> **Du bist fertig, wenn:** Du Loading-Spinner, Daten und Fehlermeldungen siehst

**Aufgabe:**

1. Erstelle `src/components/PostList.jsx`:

```javascript
// src/components/PostList.jsx
import { useState, useEffect } from 'react';

function PostList() {
  // Aufgabe 1: Drei State-Variablen anlegen
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);  // Startet als true!
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadPosts() {
      // Aufgabe 2: Implementiere den Fetch mit allen drei States
      // 1. setLoading(true) am Anfang
      // 2. setError(null) um vorherige Fehler zu löschen
      // 3. try: fetch, response.ok prüfen, setPosts
      // 4. catch: setError mit Fehlermeldung
      // 5. finally: setLoading(false) – egal ob Erfolg oder Fehler!
    }

    loadPosts();
  }, []);

  // Aufgabe 3: Bedingte Anzeige je nach State
  // Loading → Lade-Anzeige
  // Error → Fehlermeldung mit "Erneut laden" Button
  // Success → Posts anzeigen

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <p>Lade Posts...</p>
        {/* Bonus: Füge eine CSS-Animation hinzu */}
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', padding: '40px', color: '#e74c3c' }}>
        <p>Fehler: {error}</p>
        {/* Aufgabe 4: "Erneut laden" Button
            Tipp: Du brauchst eine Funktion die den useEffect-Code erneut ausführt
            Einfachste Lösung: Seite neu laden mit window.location.reload()
            Bessere Lösung: Den Fetch in eine eigene Funktion auslagern */}
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', padding: '24px' }}>
      <h2>Blog Posts ({posts.length})</h2>

      {posts.map(post => (
        <article key={post.id} style={{
          padding: '16px',
          marginBottom: '16px',
          border: '1px solid #eee',
          borderRadius: '8px'
        }}>
          <h3 style={{ margin: '0 0 8px 0' }}>{post.title}</h3>
          <p style={{ margin: 0, color: '#666' }}>{post.body}</p>
        </article>
      ))}
    </div>
  );
}

export default PostList;
```

2. **Teste den Error-State:** Ändere die URL absichtlich zu einer falschen URL (z.B. `https://jsonplaceholder.typicode.com/FALSCH`) und prüfe ob die Fehlermeldung erscheint.

3. **Teste den Loading-State:** Öffne DevTools → Network → Throttle auf "Slow 3G" stellen, um den Loading-State länger zu sehen.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/PostList.jsx
import { useState, useEffect, useCallback } from 'react';

function PostList() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch-Logik als eigene Funktion – damit wir sie erneut aufrufen können
  const loadPosts = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(
        'https://jsonplaceholder.typicode.com/posts?_limit=10'
      );

      if (!response.ok) {
        throw new Error(`HTTP-Fehler: ${response.status}`);
      }

      const data = await response.json();
      setPosts(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadPosts();
  }, [loadPosts]);

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <div style={{
          width: '40px',
          height: '40px',
          border: '4px solid #eee',
          borderTop: '4px solid #3498db',
          borderRadius: '50%',
          animation: 'spin 1s linear infinite',
          margin: '0 auto 16px'
        }} />
        <p>Lade Posts...</p>
        <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <p style={{ color: '#e74c3c', fontSize: '18px' }}>
          Fehler: {error}
        </p>
        <button
          onClick={loadPosts}
          style={{
            padding: '10px 24px',
            fontSize: '16px',
            cursor: 'pointer',
            background: '#3498db',
            color: '#fff',
            border: 'none',
            borderRadius: '4px'
          }}
        >
          Erneut laden
        </button>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', padding: '24px' }}>
      <h2>Blog Posts ({posts.length})</h2>

      {posts.map(post => (
        <article key={post.id} style={{
          padding: '16px',
          marginBottom: '16px',
          border: '1px solid #eee',
          borderRadius: '8px'
        }}>
          <h3 style={{ margin: '0 0 8px 0' }}>{post.title}</h3>
          <p style={{ margin: 0, color: '#666' }}>{post.body}</p>
        </article>
      ))}
    </div>
  );
}

export default PostList;
```

> **Warum `finally`?**
> `finally` wird IMMER ausgeführt – egal ob der `try`-Block erfolgreich war oder der `catch` einen Fehler abgefangen hat. Damit stellen wir sicher, dass `loading` auf `false` gesetzt wird, egal was passiert. Ohne `finally` könnte der Loading-Spinner bei einem Fehler ewig angezeigt werden.

> **Warum `setError(null)` am Anfang?**
> Wenn der User "Erneut laden" klickt, wollen wir die alte Fehlermeldung sofort entfernen. Sonst sieht er gleichzeitig die alte Fehlermeldung und den Loading-Spinner.

</details>

### Wissensfrage 2

Warum starten wir `loading` mit `true` statt `false`?

<details>
<summary>Antwort anzeigen</summary>

Weil der API-Call sofort beim Mount startet (im `useEffect`). Zwischen dem ersten Render und der fertigen API-Antwort vergeht Zeit. In dieser Zeit wollen wir den Loading-State anzeigen.

Wenn wir mit `false` starten würden, gäbe es einen kurzen Moment, in dem weder Loading noch Daten angezeigt werden – die Komponente wäre kurz leer. Mit `loading: true` als Startwert sieht der User sofort den Loading-Spinner.

</details>

---

## Teil 7: Custom Hook – useFetch

### Das Problem: Code-Duplikation

In jeder Komponente mit API-Call schreiben wir dasselbe Pattern:

```javascript
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  async function load() {
    setLoading(true);
    setError(null);
    try { ... } catch { ... } finally { setLoading(false); }
  }
  load();
}, [dependency]);
```

### Die Lösung: useFetch Custom Hook

Wir extrahieren dieses Pattern in einen wiederverwendbaren Hook!

> **Ziel:** Einen generischen `useFetch`-Hook erstellen
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Du den Hook in mehreren Komponenten verwenden kannst

**Aufgabe:**

1. Erstelle `src/hooks/useFetch.js`:

```javascript
// src/hooks/useFetch.js
import { useState, useEffect } from 'react';

// Aufgabe: Erstelle einen Hook der:
// - Eine URL als Parameter erhält
// - data, loading und error als States verwaltet
// - Beim Mount (und bei URL-Änderung) die Daten lädt
// - { data, loading, error } zurückgibt

export function useFetch(url) {
  // Aufgabe 1: State-Variablen erstellen
  // const [data, setData] = ???
  // const [loading, setLoading] = ???
  // const [error, setError] = ???

  // Aufgabe 2: useEffect mit Fetch-Logik
  // Tipp: url ins Dependency Array!
  // Tipp: Was passiert wenn url null oder leer ist?

  // Aufgabe 3: Ergebnisse zurückgeben
  // return { data, loading, error };
}
```

2. Verwende den Hook in einer Komponente `src/components/UserCard.jsx`:

```javascript
// src/components/UserCard.jsx
import { useState } from 'react';
import { useFetch } from '../hooks/useFetch';

function UserCard() {
  const [userId, setUserId] = useState(1);

  // So einfach wird Daten laden mit dem Custom Hook!
  const { data: user, loading, error } = useFetch(
    `https://jsonplaceholder.typicode.com/users/${userId}`
  );

  if (loading) return <p>Lade User...</p>;
  if (error) return <p style={{ color: 'red' }}>Fehler: {error}</p>;
  if (!user) return null;

  return (
    <div style={{ maxWidth: '400px', margin: '40px auto', padding: '24px' }}>
      <h2>User Details</h2>

      <div style={{
        padding: '20px',
        border: '1px solid #ddd',
        borderRadius: '12px',
        marginBottom: '16px'
      }}>
        <h3 style={{ margin: '0 0 8px 0' }}>{user.name}</h3>
        <p style={{ margin: '4px 0', color: '#666' }}>{user.email}</p>
        <p style={{ margin: '4px 0', color: '#666' }}>{user.phone}</p>
        <p style={{ margin: '4px 0', color: '#999', fontSize: '14px' }}>
          {user.company.name} | {user.address.city}
        </p>
      </div>

      <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
        {[1, 2, 3, 4, 5].map(id => (
          <button
            key={id}
            onClick={() => setUserId(id)}
            style={{
              padding: '8px 16px',
              background: userId === id ? '#3498db' : '#ecf0f1',
              color: userId === id ? '#fff' : '#333',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer'
            }}
          >
            User {id}
          </button>
        ))}
      </div>
    </div>
  );
}

export default UserCard;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/hooks/useFetch.js
import { useState, useEffect } from 'react';

export function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Nichts tun wenn keine URL – alten State aufräumen
    if (!url) {
      setData(null);
      setError(null);
      setLoading(false);
      return;
    }

    async function fetchData() {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP-Fehler: ${response.status}`);
        }

        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [url]); // Neu laden wenn sich die URL ändert!

  return { data, loading, error };
}
```

> **Warum `url` im Dependency Array?**
> Wenn sich die URL ändert (z.B. weil der User einen anderen User auswählt und sich die ID in der URL ändert), soll automatisch ein neuer Fetch ausgeführt werden. React erkennt die Änderung und führt den Effekt erneut aus.

> **Wiederverwendbarkeit:**
> Jetzt kannst du in jeder Komponente mit einer einzigen Zeile Daten laden:
> ```javascript
> const { data, loading, error } = useFetch('https://api.example.com/data');
> ```
> Kein Copy-Paste von Loading/Error-State mehr!

</details>

### Wichtig: Race Conditions & Cleanup

> **Für echte Apps:** Wenn sich die URL schnell ändert (z.B. der User klickt schnell mehrere Buttons oder tippt schnell in ein Suchfeld), kann ein **älterer** Request **nach** einem neueren zurückkommen und dessen Ergebnis überschreiben. Das nennt man eine **Race Condition**.
>
> React empfiehlt dafür eine **Cleanup-Funktion** in useEffect. Die einfachste Lösung ist ein `ignore`-Flag oder ein `AbortController`:
>
> ```javascript
> useEffect(() => {
>   let ignore = false; // Flag für Cleanup
>
>   async function fetchData() {
>     const res = await fetch(url);
>     const data = await res.json();
>
>     if (!ignore) {   // Nur setzen wenn NICHT gecleant
>       setData(data);
>     }
>   }
>
>   fetchData();
>
>   return () => {     // Cleanup-Funktion
>     ignore = true;   // Alte Requests ignorieren
>   };
> }, [url]);
> ```
>
> Auch der **StrictMode** in der Entwicklung (ab React 18) führt Setup+Cleanup doppelt aus, genau um solche Probleme aufzudecken. React garantiert nicht, dass ein Effekt nur einmal läuft – deshalb ist es wichtig, **Cleanup/Idempotenz** mitzudenken.
>
> In unserer Übung lassen wir Cleanup bewusst weg, um den Fokus auf die Grundlagen zu halten. Aber merke dir: **In Produktions-Apps gehört Cleanup dazu!**

---

## Teil 8: Praxis – Wetter-Dashboard mit API

Die Abschlussübung! Hier kombinierst du alles, was du gelernt hast, in einer realistischen Anwendung.

> **Ziel:** Ein Wetter-Dashboard das echte Daten von einer API anzeigt
> **Zeitbedarf:** ca. 40 Minuten
> **Du bist fertig, wenn:** Du nach Städten suchen und Wetterdaten sehen kannst

### Die API: Open-Meteo

Wir verwenden die **Open-Meteo API** – komplett kostenlos und ohne API-Key!

```
Geocoding (Stadt suchen):
https://geocoding-api.open-meteo.com/v1/search?name={stadtname}&count=5&language=de

Wetter (Daten holen):
https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code&timezone=auto
```

### Komponenten-Struktur

```
src/
├── hooks/
│   └── useFetch.js          # Aus Teil 7
├── components/
│   ├── WeatherDashboard.jsx # Hauptkomponente
│   ├── CitySearch.jsx       # Suchfeld & Ergebnisse
│   └── WeatherDisplay.jsx   # Wetteranzeige
└── App.jsx
```

### Aufgabe

1. **Erstelle `src/components/CitySearch.jsx`:**

```javascript
// src/components/CitySearch.jsx
import { useState, useEffect } from 'react';

function CitySearch({ onCitySelect }) {
  const [search, setSearch] = useState('');
  const [cities, setCities] = useState([]);
  const [loading, setLoading] = useState(false);

  // Aufgabe 1: Suche Städte wenn search sich ändert
  // Aber: Nicht bei jedem Tastendruck suchen!
  // Tipp: Suche nur wenn search mindestens 3 Zeichen lang ist
  // URL: https://geocoding-api.open-meteo.com/v1/search?name={search}&count=5&language=de
  useEffect(() => {
    // Dein Code hier
  }, [search]);

  return (
    <div style={{ marginBottom: '24px' }}>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Stadt suchen (z.B. Berlin)..."
        style={{
          width: '100%',
          padding: '12px',
          fontSize: '16px',
          boxSizing: 'border-box',
          borderRadius: '8px',
          border: '1px solid #ddd'
        }}
      />

      {loading && <p style={{ color: '#999' }}>Suche...</p>}

      {cities.length > 0 && (
        <ul style={{ listStyle: 'none', padding: 0, marginTop: '8px' }}>
          {cities.map(city => (
            <li
              key={city.id}
              onClick={() => {
                onCitySelect(city);
                setSearch('');
                setCities([]);
              }}
              style={{
                padding: '10px 12px',
                borderBottom: '1px solid #eee',
                cursor: 'pointer',
                display: 'flex',
                justifyContent: 'space-between'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = '#f5f5f5'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <span>{city.name}</span>
              <span style={{ color: '#999', fontSize: '14px' }}>
                {city.country}
                {city.admin1 ? `, ${city.admin1}` : ''}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default CitySearch;
```

2. **Erstelle `src/components/WeatherDisplay.jsx`:**

```javascript
// src/components/WeatherDisplay.jsx
import { useFetch } from '../hooks/useFetch';

// Wettercode zu Beschreibung
function getWeatherDescription(code) {
  const descriptions = {
    0: 'Klar',
    1: 'Überwiegend klar',
    2: 'Teilweise bewölkt',
    3: 'Bedeckt',
    45: 'Nebel',
    48: 'Nebel mit Reif',
    51: 'Leichter Nieselregen',
    53: 'Nieselregen',
    55: 'Starker Nieselregen',
    61: 'Leichter Regen',
    63: 'Regen',
    65: 'Starker Regen',
    71: 'Leichter Schnee',
    73: 'Schnee',
    75: 'Starker Schnee',
    80: 'Regenschauer',
    81: 'Starke Regenschauer',
    95: 'Gewitter'
  };
  return descriptions[code] || 'Unbekannt';
}

function WeatherDisplay({ city }) {
  // Aufgabe 2: Verwende den useFetch Hook um Wetterdaten zu laden
  // URL: https://api.open-meteo.com/v1/forecast?latitude={city.latitude}&longitude={city.longitude}&current=temperature_2m,wind_speed_10m,weather_code&timezone=auto
  const { data, loading, error } = useFetch(
    // Dein Code hier – baue die URL zusammen
  );

  if (loading) return <p>Lade Wetterdaten...</p>;
  if (error) return <p style={{ color: '#e74c3c' }}>Fehler: {error}</p>;
  if (!data) return null;

  const current = data.current;

  return (
    <div style={{
      padding: '24px',
      border: '1px solid #ddd',
      borderRadius: '12px',
      textAlign: 'center'
    }}>
      <h2 style={{ margin: '0 0 4px 0' }}>{city.name}</h2>
      <p style={{ margin: '0 0 16px 0', color: '#999' }}>
        {city.country}{city.admin1 ? `, ${city.admin1}` : ''}
      </p>

      <p style={{ fontSize: '48px', margin: '0 0 8px 0', fontWeight: 'bold' }}>
        {Math.round(current.temperature_2m)}°C
      </p>

      <p style={{ fontSize: '18px', color: '#666', margin: '0 0 16px 0' }}>
        {getWeatherDescription(current.weather_code)}
      </p>

      <div style={{ display: 'flex', justifyContent: 'center', gap: '24px' }}>
        <div>
          <p style={{ margin: 0, fontSize: '14px', color: '#999' }}>Wind</p>
          <p style={{ margin: 0, fontWeight: 'bold' }}>
            {current.wind_speed_10m} km/h
          </p>
        </div>
      </div>
    </div>
  );
}

export default WeatherDisplay;
```

3. **Erstelle `src/components/WeatherDashboard.jsx`:**

```javascript
// src/components/WeatherDashboard.jsx
import { useState } from 'react';
import CitySearch from './CitySearch';
import WeatherDisplay from './WeatherDisplay';

function WeatherDashboard() {
  const [selectedCity, setSelectedCity] = useState(null);

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', padding: '24px' }}>
      <h1 style={{ textAlign: 'center' }}>Wetter-Dashboard</h1>

      <CitySearch onCitySelect={setSelectedCity} />

      {selectedCity ? (
        <WeatherDisplay city={selectedCity} />
      ) : (
        <p style={{ textAlign: 'center', color: '#999', padding: '40px' }}>
          Suche nach einer Stadt, um das Wetter anzuzeigen.
        </p>
      )}
    </div>
  );
}

export default WeatherDashboard;
```

4. Binde `WeatherDashboard` in `App.jsx` ein und teste die App!

<details>
<summary>Musterlösung anzeigen</summary>

**CitySearch.jsx (vollständig):**

```javascript
// src/components/CitySearch.jsx
import { useState, useEffect } from 'react';

function CitySearch({ onCitySelect }) {
  const [search, setSearch] = useState('');
  const [cities, setCities] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Nicht suchen bei weniger als 3 Zeichen
    if (search.length < 3) {
      setCities([]);
      return;
    }

    async function searchCities() {
      setLoading(true);
      try {
        const response = await fetch(
          `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(search)}&count=5&language=de`
        );

        if (!response.ok) {
          throw new Error(`HTTP-Fehler: ${response.status}`);
        }

        const data = await response.json();
        setCities(data.results || []);
      } catch (error) {
        console.error('Fehler bei Stadtsuche:', error);
        setCities([]);
      } finally {
        setLoading(false);
      }
    }

    searchCities();
  }, [search]);

  return (
    <div style={{ marginBottom: '24px' }}>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Stadt suchen (z.B. Berlin)..."
        style={{
          width: '100%',
          padding: '12px',
          fontSize: '16px',
          boxSizing: 'border-box',
          borderRadius: '8px',
          border: '1px solid #ddd'
        }}
      />

      {loading && <p style={{ color: '#999' }}>Suche...</p>}

      {cities.length > 0 && (
        <ul style={{
          listStyle: 'none',
          padding: 0,
          marginTop: '8px',
          border: '1px solid #eee',
          borderRadius: '8px',
          overflow: 'hidden'
        }}>
          {cities.map(city => (
            <li
              key={city.id}
              onClick={() => {
                onCitySelect(city);
                setSearch('');
                setCities([]);
              }}
              style={{
                padding: '10px 12px',
                borderBottom: '1px solid #eee',
                cursor: 'pointer',
                display: 'flex',
                justifyContent: 'space-between'
              }}
              onMouseEnter={(e) => e.currentTarget.style.background = '#f5f5f5'}
              onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
            >
              <span>{city.name}</span>
              <span style={{ color: '#999', fontSize: '14px' }}>
                {city.country}
                {city.admin1 ? `, ${city.admin1}` : ''}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default CitySearch;
```

> **Bonus: Debounce mit useEffect-Cleanup**
>
> Aktuell wird bei jedem Tastendruck sofort ein API-Request gesendet. In echten Apps verwendet man ein **Debounce** – der Request wird erst gesendet, wenn der User kurz aufhört zu tippen. Das spart Requests und ist professioneller:
>
> ```javascript
> useEffect(() => {
>   if (search.length < 3) {
>     setCities([]);
>     return;
>   }
>
>   // Timer starten – Request erst nach 300ms Pause senden
>   const timer = setTimeout(() => {
>     async function searchCities() {
>       setLoading(true);
>       try {
>         const response = await fetch(
>           `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(search)}&count=5&language=de`
>         );
>         if (!response.ok) throw new Error(`HTTP-Fehler: ${response.status}`);
>         const data = await response.json();
>         setCities(data.results || []);
>       } catch (error) {
>         console.error('Fehler bei Stadtsuche:', error);
>         setCities([]);
>       } finally {
>         setLoading(false);
>       }
>     }
>     searchCities();
>   }, 300);
>
>   // Cleanup: Timer abbrechen wenn User weiter tippt
>   return () => clearTimeout(timer);
> }, [search]);
> ```
>
> Das ist ein perfektes Beispiel für die **Cleanup-Funktion** in useEffect: Bei jeder neuen Eingabe wird der alte Timer gelöscht und ein neuer gestartet. Erst wenn 300ms lang keine Eingabe kommt, wird der Request tatsächlich gesendet.

**WeatherDisplay.jsx (vollständig):**

```javascript
// src/components/WeatherDisplay.jsx
import { useFetch } from '../hooks/useFetch';

function getWeatherDescription(code) {
  const descriptions = {
    0: 'Klar',
    1: 'Überwiegend klar',
    2: 'Teilweise bewölkt',
    3: 'Bedeckt',
    45: 'Nebel',
    48: 'Nebel mit Reif',
    51: 'Leichter Nieselregen',
    53: 'Nieselregen',
    55: 'Starker Nieselregen',
    61: 'Leichter Regen',
    63: 'Regen',
    65: 'Starker Regen',
    71: 'Leichter Schnee',
    73: 'Schnee',
    75: 'Starker Schnee',
    80: 'Regenschauer',
    81: 'Starke Regenschauer',
    95: 'Gewitter'
  };
  return descriptions[code] || 'Unbekannt';
}

function WeatherDisplay({ city }) {
  const { data, loading, error } = useFetch(
    `https://api.open-meteo.com/v1/forecast?latitude=${city.latitude}&longitude=${city.longitude}&current=temperature_2m,wind_speed_10m,weather_code&timezone=auto`
  );

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <p>Lade Wetterdaten...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', padding: '40px', color: '#e74c3c' }}>
        <p>Fehler: {error}</p>
      </div>
    );
  }

  if (!data) return null;

  const current = data.current;

  return (
    <div style={{
      padding: '24px',
      border: '1px solid #ddd',
      borderRadius: '12px',
      textAlign: 'center'
    }}>
      <h2 style={{ margin: '0 0 4px 0' }}>{city.name}</h2>
      <p style={{ margin: '0 0 16px 0', color: '#999' }}>
        {city.country}{city.admin1 ? `, ${city.admin1}` : ''}
      </p>

      <p style={{ fontSize: '48px', margin: '0 0 8px 0', fontWeight: 'bold' }}>
        {Math.round(current.temperature_2m)}°C
      </p>

      <p style={{ fontSize: '18px', color: '#666', margin: '0 0 16px 0' }}>
        {getWeatherDescription(current.weather_code)}
      </p>

      <div style={{ display: 'flex', justifyContent: 'center', gap: '24px' }}>
        <div>
          <p style={{ margin: 0, fontSize: '14px', color: '#999' }}>Wind</p>
          <p style={{ margin: 0, fontWeight: 'bold' }}>
            {current.wind_speed_10m} km/h
          </p>
        </div>
      </div>
    </div>
  );
}

export default WeatherDisplay;
```

> **Hooks die du hier verwendest:**
> - `useState` – Ausgewählte Stadt speichern, Suchtext verwalten
> - `useEffect` – API-Calls beim Tippen und bei Stadt-Auswahl
> - `useFetch` (Custom Hook) – Wiederverwendbare Fetch-Logik in WeatherDisplay
> - Dependency Array – Steuert wann neue Daten geladen werden

> **Was du gelernt hast:**
> Diese App zeigt das vollständige Pattern für API-Calls in React:
> 1. User-Input mit useState erfassen
> 2. API-Call mit useEffect bei Änderungen ausführen
> 3. Loading/Error/Success States korrekt verwalten
> 4. Wiederverwendbare Logik in Custom Hooks auslagern

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **fetch API** | HTTP-Requests im Browser | `fetch(url).then(res => res.json())` |
| **async/await** | Lesbare asynchrone Syntax | `const data = await fetch(url)` |
| **useEffect** | Seiteneffekte kontrollieren | `useEffect(() => { ... }, [deps])` |
| **Dependency Array** | Steuert wann Effekte laufen | `[]` = Mount, `[x]` = wenn x sich ändert |
| **Loading State** | UX während Daten laden | `const [loading, setLoading] = useState(true)` |
| **Error State** | Fehler sichtbar machen | `const [error, setError] = useState(null)` |
| **useFetch Hook** | Wiederverwendbare Fetch-Logik | `const { data, loading, error } = useFetch(url)` |

### Das Standard-Pattern auf einen Blick

```javascript
import { useState, useEffect } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch('https://api.example.com/data');
        if (!res.ok) throw new Error(`HTTP-Fehler: ${res.status}`);
        const json = await res.json();
        setData(json);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []); // Dependency Array

  if (loading) return <p>Laden...</p>;
  if (error) return <p>Fehler: {error}</p>;
  if (!data) return null;

  return <div>{/* data verwenden */}</div>;
}
```

### Häufige Fehler vermeiden

```
┌─────────────────────────────────────────────────────────────┐
│              HÄUFIGE FEHLER MIT useEffect                   │
│                                                             │
│   FEHLER: useEffect Callback als async markieren            │
│      useEffect(async () => { ... })                         │
│      → Fix: async-Funktion INNERHALB definieren             │
│                                                             │
│   FEHLER: Dependency Array vergessen                        │
│      useEffect(() => { fetch(...) })                        │
│      → Endlosschleife! Fetch bei jedem Render               │
│                                                             │
│   FEHLER: fetch-Ergebnis direkt im Render verwenden         │
│      const data = fetch(url)  // Im Funktionskörper         │
│      → Endlosschleife! Immer useEffect verwenden            │
│                                                             │
│   FEHLER: response.ok nicht prüfen                          │
│      fetch wirft bei 404/500 keinen Fehler!                 │
│      → Immer if (!response.ok) prüfen                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du verstehst den Unterschied zwischen fetch (Promises) und async/await
- [ ] Du weißt warum API-Calls in useEffect gehören (und nicht direkt im Render)
- [ ] Du kannst useEffect mit leerem Dependency Array `[]` für einmaliges Laden verwenden
- [ ] Du kannst useEffect mit Dependencies `[x]` für reaktive API-Calls verwenden
- [ ] Du weißt warum der useEffect-Callback nicht direkt async sein darf
- [ ] Du implementierst Loading- und Error-States für jede API-Anfrage
- [ ] Du kannst einen Custom Hook (useFetch) für wiederverwendbare Fetch-Logik erstellen
- [ ] Du weißt dass fetch bei HTTP-Fehlern (404, 500) keinen Fehler wirft

**Alles abgehakt?** Du beherrschst API-Calls in React!
