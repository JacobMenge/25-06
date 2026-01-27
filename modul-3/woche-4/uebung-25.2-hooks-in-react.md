# Hooks in React - Praktische Übung

## Übersicht

Willkommen zur vertiefenden Übung zu React Hooks! Du hast bereits `useState` und `useEffect` kennengelernt – jetzt geht es darum, das vollständige Hooks-System zu verstehen, weitere wichtige Hooks anzuwenden und eigene Custom Hooks zu erstellen.

In dieser Übung lernst du:
- **Zweck von Hooks** - Warum React Hooks braucht und welche Regeln gelten
- **useRef** - Referenzen auf DOM-Elemente und persistente Werte ohne Re-Render
- **useMemo** - Teure Berechnungen zwischenspeichern
- **useCallback** - Funktionen stabil halten zwischen Re-Renders
- **useReducer** - Komplexen State mit Reducer-Logik verwalten
- **Custom Hooks** - Eigene Hooks erstellen und wiederverwenden

Diese Übung baut auf "24.3 useState & Controlled Inputs" und "24.4 Rendering, Listen & Keys" auf – stelle sicher, dass du State, Events und Listen-Rendering verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Hooks-System verstehen | 5 min (lesen) |
| **Teil 1** | Hook-Regeln & Übersicht | 15 min |
| **Teil 2** | useRef: DOM-Zugriff & persistente Werte | 20 min |
| **Teil 3** | useMemo: Berechnungen cachen | 20 min |
| **Teil 4** | useCallback: Stabile Funktionsreferenzen | 15 min |
| **Teil 5** | useReducer: Komplexer State | 25 min |
| **Teil 6** | Custom Hooks erstellen | 25 min |
| **Teil 7** | Praxis: useLocalStorage Hook | 30 min |
| **Teil 8** | Praxis: Rezept-Suche mit mehreren Hooks | 35 min |
| | **Gesamt** | **ca. 3 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - Hooks-System verstehen
2. **Teil 1** - Hook-Regeln & Übersicht - *Grundverständnis*
3. **Teil 2** - useRef - *Wichtig für DOM-Zugriff*
4. **Teil 5** - useReducer - *Alternative zu useState für komplexen State*
5. **Teil 6** - Custom Hooks - *Kernkonzept dieser Lektion*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast ein funktionierendes React-Projekt (aus den vorherigen Übungen)
2. Der Dev-Server läuft (`npm run dev`)
3. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest hooks-uebung -- --template react
cd hooks-uebung
npm install
npm run dev
```

> **Tipp für diese Übung:** Du wirst mehrere Komponenten und Hooks bauen. Um Verwirrung zu vermeiden: **Rendere immer nur eine Übungskomponente gleichzeitig in `App.jsx`**. Kommentiere die anderen aus, während du an einer neuen arbeitest.

---

## Rückblick: Hooks-System verstehen

### Was sind Hooks eigentlich?

Hooks sind **spezielle Hilfsfunktionen** von React, die du in Funktionskomponenten verwenden kannst. Sie ermöglichen dir, React-Features wie State, Lifecycle und Kontext zu nutzen, ohne Klassen zu schreiben.

### Warum brauchen Komponenten Hooks?

React-Komponenten sind Funktionen, die bei jedem Render neu ausgeführt werden. Dabei entstehen besondere Anforderungen:

```
┌─────────────────────────────────────────────────────────────┐
│                WARUM HOOKS NÖTIG SIND                       │
│                                                             │
│   Komponenten...                                            │
│                                                             │
│   • interagieren mit React's virtuellem DOM                 │
│     → Hooks wie useState signalisieren Re-Renders           │
│                                                             │
│   • brauchen Zugriff auf den echten DOM                     │
│     → useRef gibt Referenz auf DOM-Elemente                 │
│                                                             │
│   • führen Seiteneffekte aus (API-Calls, Timer, etc.)       │
│     → useEffect kontrolliert wann Effekte laufen            │
│                                                             │
│   • werden häufig neu gerendert                             │
│     → useMemo/useCallback vermeiden unnötige Arbeit         │
│                                                             │
│   Diese Anforderungen kann man mit Hooks lösen!             │
└─────────────────────────────────────────────────────────────┘
```

### Hooks die du schon kennst

| Hook | Zweck | Beispiel |
|------|-------|----------|
| **useState** | Zustand verwalten | `const [count, setCount] = useState(0)` |
| **useEffect** | Seiteneffekte ausführen | `useEffect(() => { fetch(...) }, [])` |
| **useRef** | DOM-Referenz halten | `const inputRef = useRef(null)` |
| **useContext** | Kontext-Daten lesen | `const theme = useContext(ThemeContext)` |

In dieser Übung vertiefen wir `useRef` und lernen `useMemo`, `useCallback`, `useReducer` und **Custom Hooks** kennen.

---

## Teil 1: Hook-Regeln & Übersicht

### Die zwei goldenen Regeln

Bevor wir neue Hooks lernen, gibt es zwei Regeln, die für **alle** Hooks gelten:

```
┌─────────────────────────────────────────────────────────────┐
│                    HOOK-REGELN                              │
│                                                             │
│   Regel 1: Nur auf oberster Ebene aufrufen                  │
│   ─────────────────────────────────────────                 │
│   NICHT in Schleifen, Bedingungen oder verschachtelten      │
│   Funktionen. React verlässt sich auf die Reihenfolge       │
│   der Hook-Aufrufe!                                         │
│                                                             │
│   Regel 2: Nur in React-Funktionen aufrufen                 │
│   ─────────────────────────────────────────                 │
│   Nur in Funktionskomponenten ODER in Custom Hooks.         │
│   NICHT in normalen JavaScript-Funktionen.                  │
└─────────────────────────────────────────────────────────────┘
```

### Warum die Reihenfolge wichtig ist

React identifiziert Hooks intern über ihre Aufruf-Reihenfolge. Wenn du einen Hook in eine Bedingung packst, kann sich die Reihenfolge ändern – und React kommt durcheinander:

```javascript
// ❌ FALSCH – Hook in Bedingung
function MyComponent({ user }) {
  if (user) {
    const [name, setName] = useState(user.name); // Nicht erlaubt!
  }
  const [age, setAge] = useState(0);
}

// ✅ RICHTIG – Hook immer aufrufen, Bedingung innen
function MyComponent({ user }) {
  const [name, setName] = useState(user ? user.name : '');
  const [age, setAge] = useState(0);
}
```

### Übersicht: Wichtige React Hooks

React bietet eine Reihe eingebauter Hooks. Die wichtigsten für den Alltag:

| Hook | Kategorie | Kurzbeschreibung |
|------|-----------|------------------|
| `useState` | State | Einfacher Zustand |
| `useReducer` | State | Komplexer Zustand mit Reducer-Pattern |
| `useEffect` | Effekte | Seiteneffekte (API-Calls, Timer, etc.) |
| `useRef` | Referenzen | DOM-Zugriff & persistente Werte |
| `useContext` | Kontext | Globale Daten lesen |
| `useMemo` | Performance | Berechnung zwischenspeichern |
| `useCallback` | Performance | Funktion zwischenspeichern |
| `useId` | Sonstiges | Eindeutige IDs generieren |

### Übung 1: Hook-Regeln erkennen

> **Ziel:** Die Hook-Regeln verstanden haben
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du alle Fehler identifiziert hast

**Aufgabe:** Finde die Fehler in den folgenden Code-Beispielen. Welche Hook-Regel wird verletzt?

**Beispiel A:**

```javascript
function SearchBar({ query }) {
  if (query.length > 0) {
    useEffect(() => {
      console.log('Suche nach:', query);
    }, [query]);
  }

  return <input value={query} />;
}
```

**Beispiel B:**

```javascript
function fetchUserData(userId) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data));
  }, [userId]);

  return user;
}
```

**Beispiel C:**

```javascript
function TodoList({ todos }) {
  const todoStates = [];

  for (const todo of todos) {
    const [done, setDone] = useState(todo.completed);
    todoStates.push({ done, setDone });
  }

  return <ul>{/* ... */}</ul>;
}
```

<details>
<summary>Antworten anzeigen</summary>

**Beispiel A:** Regel 1 verletzt – `useEffect` wird in einer Bedingung (`if`) aufgerufen. **Fix:** Den Hook immer aufrufen, die Bedingung in den Effekt verschieben:

```javascript
function SearchBar({ query }) {
  useEffect(() => {
    if (query.length > 0) {
      console.log('Suche nach:', query);
    }
  }, [query]);

  return <input value={query} />;
}
```

**Beispiel B:** Regel 2 verletzt – `useState` und `useEffect` werden in einer normalen Funktion (`fetchUserData`) aufgerufen, nicht in einer Komponente oder einem Custom Hook. **Fix:** Entweder als Komponente (`function FetchUserData()`) oder als Custom Hook (`function useFetchUser()`) benennen.

**Beispiel C:** Regel 1 verletzt – `useState` wird in einer Schleife (`for`) aufgerufen. Die Anzahl der Hook-Aufrufe ändert sich, wenn sich `todos` ändert. **Fix:** Einen einzigen State für alle Todos verwenden:

```javascript
function TodoList({ todos }) {
  const [todoStates, setTodoStates] = useState(
    todos.map(todo => todo.completed)
  );

  return <ul>{/* ... */}</ul>;
}
```

</details>

---

## Teil 2: useRef – DOM-Zugriff & persistente Werte

### Was ist useRef?

`useRef` erstellt ein Objekt mit einer `.current`-Eigenschaft, die **zwischen Re-Renders erhalten bleibt**, aber **keinen Re-Render auslöst** wenn sie sich ändert:

```javascript
import { useRef } from 'react';

function MyComponent() {
  const myRef = useRef(initialValue);
  // myRef.current === initialValue

  // Wert ändern – KEIN Re-Render!
  myRef.current = 'neuer Wert';
}
```

### Zwei Hauptanwendungen

```
┌─────────────────────────────────────────────────────────────┐
│                     useRef                                  │
│                                                             │
│   Anwendung 1: DOM-Zugriff                                  │
│   ────────────────────────                                  │
│   Referenz auf ein HTML-Element im echten DOM               │
│   → Fokus setzen, Scrollen, Messen, etc.                    │
│                                                             │
│   Anwendung 2: Persistente Werte                            │
│   ─────────────────────────────                             │
│   Werte speichern die zwischen Renders bleiben,             │
│   aber KEINEN Re-Render auslösen                            │
│   → Timer-IDs, vorherige Werte, Zähler                      │
└─────────────────────────────────────────────────────────────┘
```

### DOM-Zugriff mit useRef

```javascript
import { useRef } from 'react';

function AutoFocusInput() {
  const inputRef = useRef(null);

  function handleClick() {
    // Fokus auf das Input-Element setzen
    inputRef.current.focus();
  }

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Tippe hier..." />
      <button onClick={handleClick}>Fokus setzen</button>
    </div>
  );
}
```

### useRef vs useState

| | `useState` | `useRef` |
|--|-----------|---------|
| **Löst Re-Render aus?** | Ja | Nein |
| **Bleibt zwischen Renders?** | Ja | Ja |
| **Für UI-relevante Daten?** | Ja | Nein |
| **Für DOM-Zugriff?** | Nein | Ja |
| **Für Timer-IDs, Zähler etc.?** | Eher nicht | Ja |

### Übung 2: useRef anwenden

> **Ziel:** useRef für DOM-Zugriff und persistente Werte nutzen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Stoppuhr-Timer läuft und du ihn stoppen kannst

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/Stopwatch.jsx`:

```javascript
// src/components/Stopwatch.jsx
import { useState, useRef } from 'react';

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  // Aufgabe 1: Erstelle eine Ref für die Timer-ID
  // Warum useRef statt useState? Weil die Timer-ID
  // keinen Re-Render auslösen soll wenn sie sich ändert!
  // const timerRef = ???

  function start() {
    if (isRunning) return;
    setIsRunning(true);

    // Aufgabe 2: Starte einen Interval-Timer
    // und speichere die ID in timerRef.current
    // Tipp: setInterval(() => { ... }, 1000)
    // Nutze Functional Update: setSeconds(prev => prev + 1)
  }

  function stop() {
    // Aufgabe 3: Stoppe den Timer mit clearInterval
    // und setze isRunning auf false
  }

  function reset() {
    stop();
    setSeconds(0);
  }

  // Aufgabe 4: Formatiere die Zeit als MM:SS
  const minutes = Math.floor(seconds / 60);
  const secs = seconds % 60;
  const display = `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

  return (
    <div className="stopwatch">
      <h2>Stoppuhr</h2>
      <p className="time-display">{display}</p>
      <div className="buttons">
        <button onClick={start} disabled={isRunning}>Start</button>
        <button onClick={stop} disabled={!isRunning}>Stop</button>
        <button onClick={reset}>Reset</button>
      </div>
    </div>
  );
}

export default Stopwatch;
```

2. Verwende die Komponente in `App.jsx`:

```javascript
import Stopwatch from './components/Stopwatch'

function App() {
  return (
    <div className="app">
      <h1>Hooks Demo</h1>
      <Stopwatch />
    </div>
  )
}

export default App
```

3. **Bonus:** Erstelle eine zweite Ref für ein Input-Element. Füge einen Button hinzu, der den Fokus auf das Input setzt, wenn der Timer gestoppt wird (z.B. um eine Runde zu notieren).

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/Stopwatch.jsx
import { useState, useRef, useEffect } from 'react';

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  // Ref für Timer-ID – kein Re-Render nötig wenn sich die ID ändert
  const timerRef = useRef(null);

  // Bonus: Ref für Input-Element
  const noteInputRef = useRef(null);

  // Cleanup: Timer stoppen wenn Komponente entfernt wird
  // (z.B. wenn du in App.jsx zu einer anderen Übung wechselst)
  useEffect(() => {
    return () => clearInterval(timerRef.current);
  }, []);

  function start() {
    if (isRunning) return;
    setIsRunning(true);

    timerRef.current = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);
  }

  function stop() {
    clearInterval(timerRef.current);
    timerRef.current = null;
    setIsRunning(false);

    // Bonus: Fokus auf Input setzen
    if (noteInputRef.current) {
      noteInputRef.current.focus();
    }
  }

  function reset() {
    stop();
    setSeconds(0);
  }

  const minutes = Math.floor(seconds / 60);
  const secs = seconds % 60;
  const display = `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

  return (
    <div className="stopwatch">
      <h2>Stoppuhr</h2>
      <p className="time-display">{display}</p>
      <div className="buttons">
        <button onClick={start} disabled={isRunning}>Start</button>
        <button onClick={stop} disabled={!isRunning}>Stop</button>
        <button onClick={reset}>Reset</button>
      </div>
      {/* Bonus: Notiz-Input */}
      <input
        ref={noteInputRef}
        type="text"
        placeholder="Runde notieren..."
        style={{ marginTop: '16px', padding: '8px', width: '100%', boxSizing: 'border-box' }}
      />
    </div>
  );
}

export default Stopwatch;
```

> **Warum useRef statt useState für die Timer-ID?**
> Die Timer-ID ist kein UI-relevanter Wert -- sie wird nicht im JSX angezeigt. Wenn wir `useState` dafür nutzen würden, würde jedes `setTimerId(...)` einen unnötigen Re-Render auslösen. Mit `useRef` speichern wir den Wert ohne Re-Render.

> **Warum der Cleanup-useEffect?**
> Wenn du in `App.jsx` zu einer anderen Übungskomponente wechselst, wird die Stopwatch aus dem DOM entfernt (unmount). Ohne Cleanup läuft der `setInterval`-Timer im Hintergrund weiter und versucht `setSeconds` auf einer nicht mehr existierenden Komponente aufzurufen. Das erzeugt Warnungen und Memory Leaks. Die Cleanup-Funktion (`return () => clearInterval(...)`) stoppt den Timer beim Unmount.

</details>

### Wissensfrage 1

Was passiert, wenn du `useState` statt `useRef` für die Timer-ID verwendest?

<details>
<summary>Antwort anzeigen</summary>

Es funktioniert technisch, aber:

1. **Unnötige Re-Renders:** Jedes Mal wenn du `setTimerId(id)` aufrufst, rendert React die Komponente neu – obwohl sich an der UI nichts ändert.

2. **Stale Closure Problem:** In der `stop`-Funktion hättest du möglicherweise eine veraltete Timer-ID, weil `useState`-Updates asynchron sind.

**Faustregel:** Wenn ein Wert nicht in der UI angezeigt wird und kein Re-Render auslösen soll → `useRef`. Wenn ein Wert die UI beeinflusst → `useState`.

</details>

---

## Teil 3: useMemo – Berechnungen cachen

### Das Problem: Teure Berechnungen bei jedem Render

Bei jedem Re-Render wird der gesamte Funktionskörper einer Komponente neu ausgeführt – inklusive aller Berechnungen:

```javascript
function ProductList({ products, searchTerm }) {
  // Diese Filterung läuft bei JEDEM Re-Render,
  // auch wenn sich products und searchTerm nicht geändert haben!
  const filteredProducts = products.filter(p =>
    p.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return <ul>{filteredProducts.map(p => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

### Die Lösung: useMemo

`useMemo` speichert das Ergebnis einer Berechnung und gibt den gecachten Wert zurück, solange sich die Abhängigkeiten nicht ändern:

```javascript
import { useMemo } from 'react';

function ProductList({ products, searchTerm }) {
  // Nur neu berechnen wenn sich products ODER searchTerm ändert
  const filteredProducts = useMemo(() => {
    return products.filter(p =>
      p.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [products, searchTerm]);

  return <ul>{filteredProducts.map(p => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

### Wie useMemo funktioniert

```
┌─────────────────────────────────────────────────────────────┐
│                      useMemo                                │
│                                                             │
│   useMemo(() => berechnung(), [dep1, dep2])                 │
│                     │                  │                    │
│                     │                  └── Dependency Array │
│                     └── Berechnung (Callback)               │
│                                                             │
│   Render 1: deps = [A, B] → Berechnung ausführen → Ergebnis │
│   Render 2: deps = [A, B] → Cache zurückgeben (gleiche deps)│
│   Render 3: deps = [A, C] → Neu berechnen (dep2 geändert!)  │
└─────────────────────────────────────────────────────────────┘
```

### Wann useMemo verwenden?

| Situation | useMemo nötig? |
|-----------|---------------|
| Array filtern/sortieren mit vielen Elementen | Ja |
| Einfache Berechnung (`a + b`) | Nein |
| Objekt/Array das als Prop weitergegeben wird | Manchmal |
| Daten transformieren nach API-Call | Ja |

> **Wichtig:** Verwende `useMemo` nicht für alles! Es hat selbst einen Overhead (Vergleich der Dependencies). Nur bei wirklich teuren Berechnungen oder wenn Referenz-Stabilität wichtig ist.

### Übung 3: useMemo anwenden

> **Ziel:** Teure Berechnungen mit useMemo optimieren
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Die Filterung nur bei relevanten Änderungen neu berechnet wird

**Aufgabe:**

1. Erstelle eine Datei `src/components/UserSearch.jsx`:

```javascript
// src/components/UserSearch.jsx
import { useState, useMemo } from 'react';

// Simulierte große Benutzerliste
const ALL_USERS = Array.from({ length: 500 }, (_, i) => ({
  id: i + 1,
  name: `User ${i + 1}`,
  email: `user${i + 1}@example.com`,
  department: ['Engineering', 'Design', 'Marketing', 'Sales'][i % 4]
}));

function UserSearch() {
  const [search, setSearch] = useState('');
  const [department, setDepartment] = useState('all');
  const [highlight, setHighlight] = useState(false);

  // Aufgabe 1: Verwende useMemo um die Filterung zu optimieren
  // Filtere nach Name UND nach Department
  const filteredUsers = // ???

  // Aufgabe 2: Berechne mit useMemo Statistiken über die gefilterten User
  // (Anzahl pro Department)
  const stats = // ???

  return (
    <div className="user-search">
      <h2>Benutzersuche ({filteredUsers.length} Ergebnisse)</h2>

      <div className="filters">
        <input
          type="text"
          placeholder="Name suchen..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={department}
          onChange={(e) => setDepartment(e.target.value)}
        >
          <option value="all">Alle Abteilungen</option>
          <option value="Engineering">Engineering</option>
          <option value="Design">Design</option>
          <option value="Marketing">Marketing</option>
          <option value="Sales">Sales</option>
        </select>

        {/* Dieser Button ändert nur das Styling – die Filterung
            sollte NICHT neu berechnet werden! */}
        <button onClick={() => setHighlight(h => !h)}>
          {highlight ? 'Highlight aus' : 'Highlight an'}
        </button>
      </div>

      {/* Aufgabe 3: Zeige Statistiken an */}

      <ul className="user-list">
        {filteredUsers.slice(0, 20).map(user => (
          <li
            key={user.id}
            style={{ background: highlight ? '#ffffcc' : 'transparent' }}
          >
            <strong>{user.name}</strong> – {user.email} ({user.department})
          </li>
        ))}
        {filteredUsers.length > 20 && (
          <li className="more">... und {filteredUsers.length - 20} weitere</li>
        )}
      </ul>
    </div>
  );
}

export default UserSearch;
```

2. Teste: Klicke den "Highlight"-Button. Wird die Filterung neu berechnet? (Füge ein `console.log` in die useMemo-Callback-Funktion ein, um es zu überprüfen!)

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/UserSearch.jsx
import { useState, useMemo } from 'react';

const ALL_USERS = Array.from({ length: 500 }, (_, i) => ({
  id: i + 1,
  name: `User ${i + 1}`,
  email: `user${i + 1}@example.com`,
  department: ['Engineering', 'Design', 'Marketing', 'Sales'][i % 4]
}));

function UserSearch() {
  const [search, setSearch] = useState('');
  const [department, setDepartment] = useState('all');
  const [highlight, setHighlight] = useState(false);

  // Filterung wird nur neu berechnet wenn search oder department sich ändert
  const filteredUsers = useMemo(() => {
    console.log('Filterung wird berechnet...'); // Zum Testen
    return ALL_USERS.filter(user => {
      const matchesSearch = user.name
        .toLowerCase()
        .includes(search.toLowerCase());
      const matchesDepartment =
        department === 'all' || user.department === department;
      return matchesSearch && matchesDepartment;
    });
  }, [search, department]);

  // Statistiken nur neu berechnen wenn sich filteredUsers ändert
  const stats = useMemo(() => {
    const counts = {};
    for (const user of filteredUsers) {
      counts[user.department] = (counts[user.department] || 0) + 1;
    }
    return counts;
  }, [filteredUsers]);

  return (
    <div className="user-search">
      <h2>Benutzersuche ({filteredUsers.length} Ergebnisse)</h2>

      <div className="filters" style={{ display: 'flex', gap: '10px', marginBottom: '16px' }}>
        <input
          type="text"
          placeholder="Name suchen..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{ padding: '8px', flex: 1 }}
        />

        <select
          value={department}
          onChange={(e) => setDepartment(e.target.value)}
          style={{ padding: '8px' }}
        >
          <option value="all">Alle Abteilungen</option>
          <option value="Engineering">Engineering</option>
          <option value="Design">Design</option>
          <option value="Marketing">Marketing</option>
          <option value="Sales">Sales</option>
        </select>

        <button onClick={() => setHighlight(h => !h)}>
          {highlight ? 'Highlight aus' : 'Highlight an'}
        </button>
      </div>

      {/* Statistiken */}
      <div style={{ display: 'flex', gap: '16px', marginBottom: '16px' }}>
        {Object.entries(stats).map(([dept, count]) => (
          <span key={dept} style={{
            padding: '4px 12px',
            background: '#ecf0f1',
            borderRadius: '20px',
            fontSize: '14px'
          }}>
            {dept}: {count}
          </span>
        ))}
      </div>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {filteredUsers.slice(0, 20).map(user => (
          <li
            key={user.id}
            style={{
              padding: '8px 12px',
              borderBottom: '1px solid #eee',
              background: highlight ? '#ffffcc' : 'transparent'
            }}
          >
            <strong>{user.name}</strong> – {user.email} ({user.department})
          </li>
        ))}
        {filteredUsers.length > 20 && (
          <li style={{ padding: '8px', color: '#888', fontStyle: 'italic' }}>
            ... und {filteredUsers.length - 20} weitere
          </li>
        )}
      </ul>
    </div>
  );
}

export default UserSearch;
```

> **Teste es:** Öffne die Browser-Konsole. Wenn du den "Highlight"-Button klickst, sollte "Filterung wird berechnet..." **nicht** in der Konsole erscheinen – die Berechnung wird aus dem Cache zurückgegeben!

</details>

---

## Teil 4: useCallback – Stabile Funktionsreferenzen

### Das Problem: Neue Funktionen bei jedem Render

In JavaScript sind zwei Funktionen mit gleichem Code **nicht identisch**:

```javascript
const fn1 = () => console.log('hi');
const fn2 = () => console.log('hi');
fn1 === fn2; // false!
```

Das bedeutet: Bei jedem Re-Render werden Event-Handler neu erstellt. Wenn du Funktionen als Props weitergibst, denkt die Kind-Komponente, sie hätte neue Props bekommen.

### Die Lösung: useCallback

`useCallback` gibt dieselbe Funktionsreferenz zurück, solange sich die Abhängigkeiten nicht ändern:

```javascript
import { useState, useCallback } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);

  // Ohne useCallback: Neue Funktion bei jedem Render
  const handleClick = () => setCount(c => c + 1);

  // Mit useCallback: Gleiche Funktion solange Dependencies gleich
  const handleClickStable = useCallback(() => {
    setCount(c => c + 1);
  }, []); // Leeres Array = Funktion ändert sich nie

  return <ChildComponent onClick={handleClickStable} />;
}
```

### useMemo vs useCallback

```
┌─────────────────────────────────────────────────────────────┐
│              useMemo vs useCallback                         │
│                                                             │
│   useMemo:     cached den RÜCKGABEWERT einer Funktion       │
│   useCallback: cached die FUNKTION SELBST                   │
│                                                             │
│   // Diese beiden sind gleichwertig:                        │
│   useCallback(fn, deps)                                     │
│   useMemo(() => fn, deps)                                   │
│                                                             │
│   useMemo    → "Merke dir das ERGEBNIS"                     │
│   useCallback → "Merke dir die FUNKTION"                    │
└─────────────────────────────────────────────────────────────┘
```

### Übung 4: useCallback verstehen

> **Ziel:** Verstehen wann useCallback sinnvoll ist
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du den Unterschied erklären kannst

**Aufgabe:**

1. Erstelle eine Datei `src/components/CallbackDemo.jsx`:

```javascript
// src/components/CallbackDemo.jsx
import { useState, useCallback, useRef } from 'react';

// Kind-Komponente die zählt wie oft sie rendert
function ExpensiveChild({ onClick, label }) {
  const renderCount = useRef(0);
  renderCount.current += 1;

  console.log(`${label} gerendert (${renderCount.current}x)`);

  return (
    <button onClick={onClick}>
      {label} (Renders: {renderCount.current})
    </button>
  );
}

function CallbackDemo() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  // Aufgabe 1: Erstelle eine NICHT-gecachte Increment-Funktion
  const increment = () => setCount(c => c + 1);

  // Aufgabe 2: Erstelle eine gecachte Increment-Funktion mit useCallback
  const incrementStable = useCallback(() => {
    setCount(c => c + 1);
  }, []);

  return (
    <div>
      <h2>useCallback Demo</h2>
      <p>Count: {count}</p>

      {/* Dieses Input löst Re-Renders aus */}
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Tippe hier um Re-Renders auszulösen..."
      />

      <div style={{ display: 'flex', gap: '10px', marginTop: '16px' }}>
        <ExpensiveChild onClick={increment} label="Ohne useCallback" />
        <ExpensiveChild onClick={incrementStable} label="Mit useCallback" />
      </div>
    </div>
  );
}

export default CallbackDemo;
```

2. Tippe etwas in das Input-Feld und beobachte die Konsole. Welcher Button-Bereich wird häufiger neu gerendert?

> **Hinweis:** In der Praxis wirst du `useCallback` vor allem dann brauchen, wenn du Funktionen an `React.memo()`-Komponenten weitergibst. Für diese Übung reicht es zu verstehen, **was** `useCallback` tut und **warum**.

<details>
<summary>Erklärung anzeigen</summary>

Ohne `React.memo()` auf der Kind-Komponente werden **beide** Buttons bei jedem Re-Render neu gerendert – egal ob mit oder ohne `useCallback`. Das liegt daran, dass React standardmäßig alle Kinder neu rendert, wenn der Parent rendert.

`useCallback` wird erst dann wirklich nützlich, wenn du es mit `React.memo()` kombinierst:

```javascript
// Mit React.memo: Nur re-rendern wenn sich Props tatsächlich ändern
const ExpensiveChild = React.memo(function ExpensiveChild({ onClick, label }) {
  console.log(`${label} gerendert`);
  return <button onClick={onClick}>{label}</button>;
});
```

Jetzt wird "Mit useCallback" **nicht** bei jedem Tastendruck neu gerendert, weil `useCallback` sicherstellt, dass die Funktion die gleiche Referenz behält.

**Merke:** `useCallback` allein bringt wenig – es ist erst in Kombination mit `React.memo()` sinnvoll, oder wenn Funktionen in Dependency Arrays von `useEffect` verwendet werden.

</details>

---

## Teil 5: useReducer – Komplexer State

### Das Problem mit vielen useState-Aufrufen

Bei komplexem State wird `useState` schnell unübersichtlich:

```javascript
function ShoppingCart() {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [discount, setDiscount] = useState(0);
  const [isCheckout, setIsCheckout] = useState(false);
  const [error, setError] = useState('');

  // Viele zusammenhängende State-Updates...
  function addItem(item) {
    setItems(prev => [...prev, item]);
    setTotal(prev => prev + item.price);
    setError('');
  }
  // Das wird schnell unübersichtlich!
}
```

### Die Lösung: useReducer

`useReducer` bündelt zusammengehörigen State und die Logik, die ihn verändert:

```javascript
import { useReducer } from 'react';

// 1. Reducer-Funktion: Beschreibt wie sich der State ändert
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + 1 };
    case 'decrement':
      return { ...state, count: state.count - 1 };
    case 'reset':
      return { ...state, count: 0 };
    default:
      return state;
  }
}

// 2. Initial State
const initialState = { count: 0 };

// 3. In der Komponente verwenden
function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+1</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-1</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
}
```

### Wie useReducer funktioniert

```
┌─────────────────────────────────────────────────────────────┐
│                    useReducer                               │
│                                                             │
│   dispatch({ type: 'increment' })                           │
│         │                                                   │
│         ▼                                                   │
│   ┌──────────────────────────────────────┐                  │
│   │  reducer(currentState, action)       │                  │
│   │                                      │                  │
│   │  switch (action.type) {              │                  │
│   │    case 'increment':                 │                  │
│   │      return { count: state.count+1 } │                  │
│   │  }                                   │                  │
│   └──────────────────────────────────────┘                  │
│         │                                                   │
│         ▼                                                   │
│   Neuer State → React rendert Komponente neu                │
└─────────────────────────────────────────────────────────────┘
```

### useState vs useReducer

| Kriterium | `useState` | `useReducer` |
|-----------|-----------|-------------|
| Einfacher State (String, Number, Boolean) | Perfekt | Overkill |
| Zusammenhängender State (Objekt mit mehreren Feldern) | Möglich | Besser |
| State-Updates die voneinander abhängen | Schwierig | Einfach |
| Viele verschiedene Aktionen auf den gleichen State | Unübersichtlich | Klar strukturiert |

### Übung 5: useReducer für eine Todo-App

> **Ziel:** Komplexen State mit useReducer verwalten
> **Zeitbedarf:** ca. 25 Minuten
> **Du bist fertig, wenn:** Du Todos hinzufügen, abhaken und löschen kannst

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/TodoApp.jsx`:

```javascript
// src/components/TodoApp.jsx
import { useReducer, useState } from 'react';

// Aufgabe 1: Definiere den initialState
const initialState = {
  todos: [
    { id: 1, text: 'React Hooks lernen', completed: false },
    { id: 2, text: 'Custom Hook erstellen', completed: false }
  ],
  nextId: 3
};

// Aufgabe 2: Erstelle die Reducer-Funktion
// Unterstütze folgende Actions:
// - { type: 'add', text: '...' }       → Todo hinzufügen
// - { type: 'toggle', id: ... }        → Todo abhaken/enthaken
// - { type: 'delete', id: ... }        → Todo löschen
// - { type: 'clear_completed' }        → Alle erledigten löschen
function todoReducer(state, action) {
  switch (action.type) {
    // Dein Code hier
    default:
      return state;
  }
}

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, initialState);
  const [inputValue, setInputValue] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    if (inputValue.trim() === '') return;

    // Aufgabe 3: Dispatch die 'add' Action
    // dispatch(???)

    setInputValue('');
  }

  const openCount = state.todos.filter(t => !t.completed).length;

  return (
    <div className="todo-app">
      <h2>Todo App (useReducer)</h2>
      <p>{openCount} von {state.todos.length} offen</p>

      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Neues Todo..."
          style={{ flex: 1, padding: '8px' }}
        />
        <button type="submit">Hinzufügen</button>
      </form>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {state.todos.map(todo => (
          <li key={todo.id} style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            padding: '8px',
            borderBottom: '1px solid #eee'
          }}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => dispatch({ type: 'toggle', id: todo.id })}
            />
            <span style={{
              flex: 1,
              textDecoration: todo.completed ? 'line-through' : 'none',
              color: todo.completed ? '#999' : '#333'
            }}>
              {todo.text}
            </span>
            {/* Aufgabe 4: Dispatch die 'delete' Action */}
            <button onClick={() => {/* ??? */}}>
              Löschen
            </button>
          </li>
        ))}
      </ul>

      {state.todos.some(t => t.completed) && (
        <button
          onClick={() => dispatch({ type: 'clear_completed' })}
          style={{ marginTop: '16px' }}
        >
          Erledigte löschen
        </button>
      )}
    </div>
  );
}

export default TodoApp;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/TodoApp.jsx
import { useReducer, useState } from 'react';

const initialState = {
  todos: [
    { id: 1, text: 'React Hooks lernen', completed: false },
    { id: 2, text: 'Custom Hook erstellen', completed: false }
  ],
  nextId: 3
};

function todoReducer(state, action) {
  switch (action.type) {
    case 'add':
      return {
        ...state,
        todos: [
          ...state.todos,
          { id: state.nextId, text: action.text, completed: false }
        ],
        nextId: state.nextId + 1
      };

    case 'toggle':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.id
            ? { ...todo, completed: !todo.completed }
            : todo
        )
      };

    case 'delete':
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.id)
      };

    case 'clear_completed':
      return {
        ...state,
        todos: state.todos.filter(todo => !todo.completed)
      };

    default:
      return state;
  }
}

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, initialState);
  const [inputValue, setInputValue] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    if (inputValue.trim() === '') return;
    dispatch({ type: 'add', text: inputValue.trim() });
    setInputValue('');
  }

  const openCount = state.todos.filter(t => !t.completed).length;

  return (
    <div className="todo-app" style={{ maxWidth: '500px', margin: '40px auto', padding: '24px' }}>
      <h2>Todo App (useReducer)</h2>
      <p style={{ color: '#666' }}>{openCount} von {state.todos.length} offen</p>

      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Neues Todo..."
          style={{ flex: 1, padding: '8px', fontSize: '16px' }}
        />
        <button type="submit" style={{ padding: '8px 16px' }}>Hinzufügen</button>
      </form>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {state.todos.map(todo => (
          <li key={todo.id} style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            padding: '8px',
            borderBottom: '1px solid #eee'
          }}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => dispatch({ type: 'toggle', id: todo.id })}
            />
            <span style={{
              flex: 1,
              textDecoration: todo.completed ? 'line-through' : 'none',
              color: todo.completed ? '#999' : '#333'
            }}>
              {todo.text}
            </span>
            <button
              onClick={() => dispatch({ type: 'delete', id: todo.id })}
              style={{ color: '#e74c3c', border: 'none', background: 'none', cursor: 'pointer' }}
            >
              Löschen
            </button>
          </li>
        ))}
      </ul>

      {state.todos.some(t => t.completed) && (
        <button
          onClick={() => dispatch({ type: 'clear_completed' })}
          style={{ marginTop: '16px', padding: '8px 16px' }}
        >
          Erledigte löschen
        </button>
      )}
    </div>
  );
}

export default TodoApp;
```

> **Vorteile von useReducer hier:**
> - Alle State-Änderungen an einem Ort (im Reducer)
> - Klare Benennung der Aktionen (`'add'`, `'toggle'`, `'delete'`)
> - Der Reducer ist leicht testbar (reine Funktion!)
> - Kein Risiko, dass State-Updates sich gegenseitig überschreiben

</details>

---

## Teil 6: Custom Hooks erstellen

### Was ist ein Custom Hook?

Ein Custom Hook ist eine **normale JavaScript-Funktion**, die:
1. Mit `use` beginnt (Namenskonvention)
2. Andere Hooks verwenden darf
3. Logik aus Komponenten extrahiert

```
┌─────────────────────────────────────────────────────────────┐
│                   CUSTOM HOOKS                              │
│                                                             │
│   Motivation:                                               │
│                                                             │
│   • Aufräumen: Logik aus Komponenten herausziehen           │
│   • Wiederverwenden: Gleiche Logik in mehreren Komponenten  │
│   • Konzeptualisieren: Logik einen klaren Namen geben       │
│   • Testen: Logik unabhängig von UI testbar machen          │
│                                                             │
│   Regel: Name beginnt IMMER mit "use"                       │
│   → useToggle, useFetch, useLocalStorage, useWindowSize     │
└─────────────────────────────────────────────────────────────┘
```

### Beispiel: useToggle

```javascript
// src/hooks/useToggle.js
import { useState } from 'react';

export function useToggle(initial = false) {
  const [value, setValue] = useState(initial);

  function toggle() {
    setValue(prev => !prev);
  }

  return [value, toggle];
}
```

### Verwendung:

```javascript
// src/components/ToggleBox.jsx
import { useToggle } from '../hooks/useToggle';

function ToggleBox() {
  const [isOpen, toggle] = useToggle();

  return (
    <div>
      <button onClick={toggle}>
        {isOpen ? 'Schließen' : 'Öffnen'}
      </button>
      {isOpen && <div>Sichtbarer Inhalt!</div>}
    </div>
  );
}
```

### Übung 6: Eigene Hooks erstellen

> **Ziel:** Zwei Custom Hooks erstellen und verwenden
> **Zeitbedarf:** ca. 25 Minuten
> **Du bist fertig, wenn:** Beide Hooks funktionieren

**Aufgabe A: useCounter Hook**

1. Erstelle einen Ordner `src/hooks/` und darin eine Datei `useCounter.js`:

```javascript
// src/hooks/useCounter.js
import { useState } from 'react';

// Aufgabe: Erstelle einen Hook der einen Counter verwaltet
// Parameter: initialValue (Startwert, default 0), step (Schrittweite, default 1)
// Rückgabe: { count, increment, decrement, reset }

export function useCounter(initialValue = 0, step = 1) {
  // Dein Code hier
}
```

2. Verwende den Hook in einer Komponente:

```javascript
// src/components/CounterDemo.jsx
import { useCounter } from '../hooks/useCounter';

function CounterDemo() {
  const counter1 = useCounter(0, 1);
  const counter5 = useCounter(100, 5);

  return (
    <div>
      <h2>useCounter Demo</h2>

      <div>
        <h3>Counter (Schritt: 1)</h3>
        <p>{counter1.count}</p>
        <button onClick={counter1.decrement}>-1</button>
        <button onClick={counter1.reset}>Reset</button>
        <button onClick={counter1.increment}>+1</button>
      </div>

      <div>
        <h3>Counter (Schritt: 5, Start: 100)</h3>
        <p>{counter5.count}</p>
        <button onClick={counter5.decrement}>-5</button>
        <button onClick={counter5.reset}>Reset</button>
        <button onClick={counter5.increment}>+5</button>
      </div>
    </div>
  );
}

export default CounterDemo;
```

**Aufgabe B: useWindowSize Hook**

3. Erstelle eine Datei `src/hooks/useWindowSize.js`:

```javascript
// src/hooks/useWindowSize.js
import { useState, useEffect } from 'react';

// Aufgabe: Erstelle einen Hook der die aktuelle Fenstergröße zurückgibt
// Rückgabe: { width, height }
// Tipp: window.innerWidth, window.innerHeight
// Tipp: Event 'resize' auf window

export function useWindowSize() {
  // Dein Code hier
  // 1. State für width und height erstellen
  // 2. useEffect mit Event-Listener für 'resize'
  // 3. Cleanup: Event-Listener entfernen!
}
```

4. Verwende den Hook:

```javascript
// In einer beliebigen Komponente
import { useWindowSize } from '../hooks/useWindowSize';

function WindowInfo() {
  const { width, height } = useWindowSize();

  return (
    <div>
      <p>Fensterbreite: {width}px</p>
      <p>Fensterhöhe: {height}px</p>
      <p>Gerät: {width < 768 ? 'Mobile' : width < 1024 ? 'Tablet' : 'Desktop'}</p>
    </div>
  );
}
```

<details>
<summary>Musterlösung anzeigen</summary>

**useCounter:**

```javascript
// src/hooks/useCounter.js
import { useState } from 'react';

export function useCounter(initialValue = 0, step = 1) {
  const [count, setCount] = useState(initialValue);

  function increment() {
    setCount(prev => prev + step);
  }

  function decrement() {
    setCount(prev => prev - step);
  }

  function reset() {
    setCount(initialValue);
  }

  return { count, increment, decrement, reset };
}
```

**useWindowSize:**

```javascript
// src/hooks/useWindowSize.js
import { useState, useEffect } from 'react';

export function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    function handleResize() {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    window.addEventListener('resize', handleResize);

    // Cleanup: Event-Listener entfernen wenn Komponente unmountet
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Leeres Array: Nur einmal beim Mount

  return size;
}
```

> **Wichtig: Cleanup in useEffect!**
> Wenn du Event-Listener hinzufügst, musst du sie im Cleanup entfernen. Sonst bleiben sie aktiv, auch wenn die Komponente nicht mehr angezeigt wird – das führt zu Memory Leaks!

</details>

---

## Teil 7: Praxis - useLocalStorage Hook

Zeit für einen richtig nützlichen Custom Hook!

> **Ziel:** Einen Hook bauen, der State im LocalStorage persistiert
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Dein State überlebt ein Browser-Refresh

### Was ist LocalStorage?

LocalStorage ist ein Browser-Speicher, der Daten dauerhaft speichert (auch nach Schließen des Browsers):

```javascript
// Schreiben
localStorage.setItem('name', 'Max');

// Lesen
const name = localStorage.getItem('name'); // 'Max'

// Löschen
localStorage.removeItem('name');

// Für Objekte/Arrays: JSON verwenden
localStorage.setItem('user', JSON.stringify({ name: 'Max', age: 25 }));
const user = JSON.parse(localStorage.getItem('user'));
```

### Aufgabe: useLocalStorage Hook

Erstelle einen Hook, der wie `useState` funktioniert, aber den Wert automatisch im LocalStorage speichert und beim nächsten Laden wiederherstellt.

1. Erstelle `src/hooks/useLocalStorage.js`:

```javascript
// src/hooks/useLocalStorage.js
import { useState } from 'react';

// Aufgabe: Hook der State mit LocalStorage synchronisiert
// Parameter: key (String für LocalStorage), initialValue (Startwert)
// Rückgabe: [value, setValue] (wie useState)

export function useLocalStorage(key, initialValue) {
  // Aufgabe 1: Initialen Wert aus LocalStorage lesen (falls vorhanden)
  // Tipp: useState akzeptiert auch eine Funktion als Startwert (Lazy Initialization)
  // const [storedValue, setStoredValue] = useState(() => { ... });

  // Aufgabe 2: setValue-Funktion erstellen die BEIDE aktualisiert:
  // a) den React State
  // b) den LocalStorage
  // function setValue(newValue) { ... }

  // Aufgabe 3: Werte zurückgeben
  // return [storedValue, setValue];
}
```

2. Erstelle eine Demo-Komponente `src/components/PersistentForm.jsx`:

```javascript
// src/components/PersistentForm.jsx
import { useLocalStorage } from '../hooks/useLocalStorage';

function PersistentForm() {
  const [name, setName] = useLocalStorage('form-name', '');
  const [theme, setTheme] = useLocalStorage('form-theme', 'light');

  return (
    <div style={{
      maxWidth: '400px',
      margin: '40px auto',
      padding: '24px',
      background: theme === 'dark' ? '#333' : '#fff',
      color: theme === 'dark' ? '#fff' : '#333',
      borderRadius: '12px',
      border: '1px solid #ddd'
    }}>
      <h2>Persistentes Formular</h2>
      <p style={{ fontSize: '14px', color: theme === 'dark' ? '#aaa' : '#666' }}>
        Deine Eingaben überleben ein Browser-Refresh!
      </p>

      <div style={{ marginBottom: '16px' }}>
        <label style={{ display: 'block', marginBottom: '4px' }}>Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Dein Name"
          style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
        />
      </div>

      <div style={{ marginBottom: '16px' }}>
        <label style={{ display: 'block', marginBottom: '4px' }}>Theme:</label>
        <select
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
          style={{ width: '100%', padding: '8px' }}
        >
          <option value="light">Hell</option>
          <option value="dark">Dunkel</option>
        </select>
      </div>

      {name && <p>Hallo, {name}!</p>}

      <p style={{ fontSize: '12px', color: '#999' }}>
        Tipp: Lade die Seite neu (F5) – deine Daten bleiben erhalten!
      </p>
    </div>
  );
}

export default PersistentForm;
```

3. Teste: Gib einen Namen ein, wähle ein Theme, drücke F5 – sind die Daten noch da?

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/hooks/useLocalStorage.js
import { useState } from 'react';

export function useLocalStorage(key, initialValue) {
  // Lazy Initialization: Nur beim ersten Render wird LocalStorage gelesen
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = localStorage.getItem(key);
      // Wenn etwas im LocalStorage steht, parse es
      // Sonst verwende den initialValue
      return item !== null ? JSON.parse(item) : initialValue;
    } catch (error) {
      // Bei Fehlern (z.B. ungültiges JSON) → Fallback
      console.error(`Fehler beim Lesen von localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  // Erweiterte setValue-Funktion
  function setValue(newValue) {
    try {
      // Functional Updates unterstützen (wie useState)
      const valueToStore =
        typeof newValue === 'function' ? newValue(storedValue) : newValue;

      // React State aktualisieren
      setStoredValue(valueToStore);

      // LocalStorage aktualisieren
      localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Fehler beim Schreiben in localStorage key "${key}":`, error);
    }
  }

  return [storedValue, setValue];
}
```

> **Warum Lazy Initialization?**
> `useState(() => { ... })` statt `useState(localStorage.getItem(...))`:
> Mit der Funktionsform wird der LocalStorage nur beim **ersten** Render gelesen, nicht bei jedem Re-Render. Das ist effizienter, da LocalStorage-Zugriffe synchron und relativ langsam sind.

> **Warum try-catch?**
> LocalStorage kann in manchen Situationen fehlschlagen (privater Modus, Speicher voll, etc.). Mit try-catch fängt der Hook solche Fehler ab und funktioniert trotzdem.

</details>

---

## Teil 8: Praxis - Rezept-Suche mit mehreren Hooks

Die Abschlussübung! Hier verwendest du mehrere Hooks zusammen in einer realistischen Anwendung.

> **Ziel:** Eine Rezept-Suche die mehrere Hooks kombiniert
> **Zeitbedarf:** ca. 35 Minuten
> **Du bist fertig, wenn:** Die Suche funktioniert und Favoriten persistiert werden

### Aufgabe: Rezept-Suche

Erstelle eine Rezept-Such-App mit:

1. **useReducer** für den App-State (Rezepte, Filter, Favoriten)
2. **useMemo** für die gefilterte Rezeptliste
3. **useRef** für Auto-Focus auf das Suchfeld
4. **useLocalStorage** (Custom Hook) für persistente Favoriten

**Komponenten-Struktur:**

```
src/
├── hooks/
│   └── useLocalStorage.js     # Aus Teil 7
├── components/
│   ├── RecipeSearch.jsx        # Hauptkomponente
│   └── RecipeCard.jsx          # Einzelnes Rezept
├── data/
│   └── recipes.json            # Rezeptdaten
└── App.jsx
```

**Erstelle `src/data/recipes.json`:**

```json
[
  {
    "id": 1,
    "name": "Spaghetti Carbonara",
    "category": "Pasta",
    "difficulty": "Mittel",
    "time": 30,
    "ingredients": ["Spaghetti", "Eier", "Pecorino", "Guanciale", "Pfeffer"]
  },
  {
    "id": 2,
    "name": "Caesar Salad",
    "category": "Salat",
    "difficulty": "Einfach",
    "time": 15,
    "ingredients": ["Römersalat", "Croutons", "Parmesan", "Caesar-Dressing"]
  },
  {
    "id": 3,
    "name": "Chicken Tikka Masala",
    "category": "Curry",
    "difficulty": "Mittel",
    "time": 45,
    "ingredients": ["Hähnchen", "Joghurt", "Tomaten", "Gewürze", "Reis"]
  },
  {
    "id": 4,
    "name": "Griechischer Salat",
    "category": "Salat",
    "difficulty": "Einfach",
    "time": 10,
    "ingredients": ["Tomaten", "Gurke", "Oliven", "Feta", "Zwiebel"]
  },
  {
    "id": 5,
    "name": "Pad Thai",
    "category": "Nudeln",
    "difficulty": "Mittel",
    "time": 25,
    "ingredients": ["Reisnudeln", "Tofu", "Erdnüsse", "Limette", "Sojasoße"]
  },
  {
    "id": 6,
    "name": "Risotto ai Funghi",
    "category": "Reis",
    "difficulty": "Schwer",
    "time": 50,
    "ingredients": ["Arborio-Reis", "Pilze", "Brühe", "Parmesan", "Weißwein"]
  },
  {
    "id": 7,
    "name": "Tacos al Pastor",
    "category": "Mexikanisch",
    "difficulty": "Mittel",
    "time": 35,
    "ingredients": ["Tortillas", "Schweinefleisch", "Ananas", "Koriander", "Zwiebel"]
  },
  {
    "id": 8,
    "name": "Tomatensuppe",
    "category": "Suppe",
    "difficulty": "Einfach",
    "time": 20,
    "ingredients": ["Tomaten", "Zwiebel", "Knoblauch", "Basilikum", "Sahne"]
  }
]
```

**Starter-Code `src/components/RecipeCard.jsx`:**

```javascript
// src/components/RecipeCard.jsx

function RecipeCard({ recipe, isFavorite, onToggleFavorite }) {
  return (
    <div style={{
      padding: '16px',
      border: '1px solid #ddd',
      borderRadius: '12px',
      background: isFavorite ? '#fff9e6' : '#fff'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
        <h3 style={{ margin: '0 0 8px 0' }}>{recipe.name}</h3>
        <button
          onClick={() => onToggleFavorite(recipe.id)}
          style={{
            background: 'none',
            border: 'none',
            fontSize: '20px',
            cursor: 'pointer'
          }}
        >
          {isFavorite ? '★' : '☆'}
        </button>
      </div>

      <div style={{ display: 'flex', gap: '8px', marginBottom: '8px' }}>
        <span style={{
          padding: '2px 8px',
          background: '#ecf0f1',
          borderRadius: '12px',
          fontSize: '12px'
        }}>
          {recipe.category}
        </span>
        <span style={{
          padding: '2px 8px',
          background: '#ecf0f1',
          borderRadius: '12px',
          fontSize: '12px'
        }}>
          {recipe.difficulty}
        </span>
        <span style={{
          padding: '2px 8px',
          background: '#ecf0f1',
          borderRadius: '12px',
          fontSize: '12px'
        }}>
          {recipe.time} Min.
        </span>
      </div>

      <p style={{ margin: 0, fontSize: '14px', color: '#666' }}>
        {recipe.ingredients.join(', ')}
      </p>
    </div>
  );
}

export default RecipeCard;
```

**Starter-Code `src/components/RecipeSearch.jsx`:**

```javascript
// src/components/RecipeSearch.jsx
import { useReducer, useMemo, useRef, useEffect } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';
import RecipeCard from './RecipeCard';
import recipes from '../data/recipes.json';

// Aufgabe 1: Reducer für Filter-State
const initialState = {
  search: '',
  category: 'all',
  showFavoritesOnly: false
};

function filterReducer(state, action) {
  switch (action.type) {
    // Implementiere: 'set_search', 'set_category', 'toggle_favorites'
    default:
      return state;
  }
}

function RecipeSearch() {
  const [filters, dispatch] = useReducer(filterReducer, initialState);

  // Aufgabe 2: Custom Hook für Favoriten (persistiert im LocalStorage)
  const [favorites, setFavorites] = useLocalStorage('recipe-favorites', []);

  // Aufgabe 3: useRef für Auto-Focus auf Suchfeld
  const searchRef = useRef(null);

  useEffect(() => {
    searchRef.current?.focus();
  }, []);

  // Aufgabe 4: useMemo für gefilterte Rezepte
  const filteredRecipes = useMemo(() => {
    // Filtere nach search, category und favorites
    return recipes; // Ersetze mit deiner Filterlogik
  }, [filters, favorites]);

  // Aufgabe 5: Favoriten-Toggle Funktion
  function toggleFavorite(id) {
    // Wenn id in favorites → entfernen
    // Wenn id nicht in favorites → hinzufügen
  }

  // Kategorien für Dropdown
  const categories = ['all', ...new Set(recipes.map(r => r.category))];

  return (
    <div style={{ maxWidth: '800px', margin: '40px auto', padding: '24px' }}>
      <h1>Rezept-Suche</h1>

      {/* Filter-Bereich */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '24px', flexWrap: 'wrap' }}>
        <input
          ref={searchRef}
          type="text"
          placeholder="Rezept suchen..."
          value={filters.search}
          onChange={(e) => dispatch({ type: 'set_search', value: e.target.value })}
          style={{ flex: 1, padding: '10px', fontSize: '16px', minWidth: '200px' }}
        />

        <select
          value={filters.category}
          onChange={(e) => dispatch({ type: 'set_category', value: e.target.value })}
          style={{ padding: '10px' }}
        >
          {categories.map(cat => (
            <option key={cat} value={cat}>
              {cat === 'all' ? 'Alle Kategorien' : cat}
            </option>
          ))}
        </select>

        <button
          onClick={() => dispatch({ type: 'toggle_favorites' })}
          style={{
            padding: '10px 16px',
            background: filters.showFavoritesOnly ? '#f39c12' : '#ecf0f1',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          {filters.showFavoritesOnly ? '★ Favoriten' : '☆ Favoriten'}
        </button>
      </div>

      {/* Ergebnis-Info */}
      <p style={{ color: '#666', marginBottom: '16px' }}>
        {filteredRecipes.length} Rezepte gefunden
        {favorites.length > 0 && ` | ${favorites.length} Favoriten`}
      </p>

      {/* Rezept-Grid */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
        gap: '16px'
      }}>
        {filteredRecipes.map(recipe => (
          <RecipeCard
            key={recipe.id}
            recipe={recipe}
            isFavorite={favorites.includes(recipe.id)}
            onToggleFavorite={toggleFavorite}
          />
        ))}
      </div>

      {filteredRecipes.length === 0 && (
        <p style={{ textAlign: 'center', color: '#999', padding: '40px' }}>
          Keine Rezepte gefunden. Versuche andere Filter!
        </p>
      )}
    </div>
  );
}

export default RecipeSearch;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/RecipeSearch.jsx
import { useReducer, useMemo, useRef, useEffect } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';
import RecipeCard from './RecipeCard';
import recipes from '../data/recipes.json';

const initialState = {
  search: '',
  category: 'all',
  showFavoritesOnly: false
};

function filterReducer(state, action) {
  switch (action.type) {
    case 'set_search':
      return { ...state, search: action.value };
    case 'set_category':
      return { ...state, category: action.value };
    case 'toggle_favorites':
      return { ...state, showFavoritesOnly: !state.showFavoritesOnly };
    default:
      return state;
  }
}

function RecipeSearch() {
  const [filters, dispatch] = useReducer(filterReducer, initialState);
  const [favorites, setFavorites] = useLocalStorage('recipe-favorites', []);
  const searchRef = useRef(null);

  // Auto-Focus beim Laden
  useEffect(() => {
    searchRef.current?.focus();
  }, []);

  // Gefilterte Rezepte (nur neu berechnen wenn sich Filter oder Favoriten ändern)
  const filteredRecipes = useMemo(() => {
    return recipes.filter(recipe => {
      const matchesSearch = recipe.name
        .toLowerCase()
        .includes(filters.search.toLowerCase());
      const matchesCategory =
        filters.category === 'all' || recipe.category === filters.category;
      const matchesFavorites =
        !filters.showFavoritesOnly || favorites.includes(recipe.id);
      return matchesSearch && matchesCategory && matchesFavorites;
    });
  }, [filters, favorites]);

  function toggleFavorite(id) {
    setFavorites(prev =>
      prev.includes(id)
        ? prev.filter(favId => favId !== id)
        : [...prev, id]
    );
  }

  const categories = ['all', ...new Set(recipes.map(r => r.category))];

  return (
    <div style={{ maxWidth: '800px', margin: '40px auto', padding: '24px' }}>
      <h1>Rezept-Suche</h1>

      <div style={{ display: 'flex', gap: '10px', marginBottom: '24px', flexWrap: 'wrap' }}>
        <input
          ref={searchRef}
          type="text"
          placeholder="Rezept suchen..."
          value={filters.search}
          onChange={(e) => dispatch({ type: 'set_search', value: e.target.value })}
          style={{ flex: 1, padding: '10px', fontSize: '16px', minWidth: '200px' }}
        />

        <select
          value={filters.category}
          onChange={(e) => dispatch({ type: 'set_category', value: e.target.value })}
          style={{ padding: '10px' }}
        >
          {categories.map(cat => (
            <option key={cat} value={cat}>
              {cat === 'all' ? 'Alle Kategorien' : cat}
            </option>
          ))}
        </select>

        <button
          onClick={() => dispatch({ type: 'toggle_favorites' })}
          style={{
            padding: '10px 16px',
            background: filters.showFavoritesOnly ? '#f39c12' : '#ecf0f1',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          {filters.showFavoritesOnly ? '★ Favoriten' : '☆ Favoriten'}
        </button>
      </div>

      <p style={{ color: '#666', marginBottom: '16px' }}>
        {filteredRecipes.length} Rezepte gefunden
        {favorites.length > 0 && ` | ${favorites.length} Favoriten`}
      </p>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
        gap: '16px'
      }}>
        {filteredRecipes.map(recipe => (
          <RecipeCard
            key={recipe.id}
            recipe={recipe}
            isFavorite={favorites.includes(recipe.id)}
            onToggleFavorite={toggleFavorite}
          />
        ))}
      </div>

      {filteredRecipes.length === 0 && (
        <p style={{ textAlign: 'center', color: '#999', padding: '40px' }}>
          Keine Rezepte gefunden. Versuche andere Filter!
        </p>
      )}
    </div>
  );
}

export default RecipeSearch;
```

> **Hooks die du hier verwendest:**
> - `useReducer` – Filter-State zentral verwalten
> - `useMemo` – Filterung nur bei relevanten Änderungen neu berechnen
> - `useRef` + `useEffect` – Auto-Focus auf Suchfeld beim Laden
> - `useLocalStorage` (Custom Hook) – Favoriten im Browser speichern

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Hook-Regeln** | Nur auf Top-Level, nur in React-Funktionen | Keine Hooks in if/for |
| **useRef** | DOM-Zugriff & persistente Werte (ohne Re-Render) | `const ref = useRef(null)` |
| **useMemo** | Teure Berechnungen zwischenspeichern | `useMemo(() => filter(), [deps])` |
| **useCallback** | Stabile Funktionsreferenzen | `useCallback(() => {}, [deps])` |
| **useReducer** | Komplexer State mit Actions | `const [state, dispatch] = useReducer(fn, init)` |
| **Custom Hooks** | Eigene wiederverwendbare Hooks | `function useToggle() { ... }` |

### Hooks auf einen Blick

```javascript
// useRef: DOM-Zugriff
const inputRef = useRef(null);
<input ref={inputRef} />
inputRef.current.focus();

// useMemo: Berechnung cachen
const filtered = useMemo(() => items.filter(...), [items, query]);

// useCallback: Funktion cachen
const handleClick = useCallback(() => { ... }, [dep]);

// useReducer: Komplexer State
const [state, dispatch] = useReducer(reducer, initialState);
dispatch({ type: 'action', payload: data });

// Custom Hook: Logik extrahieren
function useMyHook(param) {
  const [value, setValue] = useState(param);
  // ... Logik ...
  return [value, setValue];
}
```

### Custom Hook auf einen Blick

```javascript
// 1. Datei erstellen: src/hooks/useMyHook.js
// 2. Name beginnt mit "use"
// 3. Kann andere Hooks verwenden
// 4. Gibt Werte/Funktionen zurück

export function useMyHook(initialValue) {
  const [state, setState] = useState(initialValue);

  function doSomething() {
    setState(prev => /* ... */);
  }

  return [state, doSomething];
}
```

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du kennst die zwei Hook-Regeln (Top-Level, React-Funktionen)
- [ ] Du kannst `useRef` für DOM-Zugriff und persistente Werte verwenden
- [ ] Du verstehst den Unterschied zwischen `useState` und `useRef`
- [ ] Du weißt wann `useMemo` sinnvoll ist (und wann nicht)
- [ ] Du verstehst was `useCallback` tut und wann es nötig ist
- [ ] Du kannst `useReducer` mit Reducer-Funktion und Actions verwenden
- [ ] Du kannst eigene Custom Hooks erstellen und verwenden
- [ ] Du verstehst die Vorteile von Custom Hooks (Wiederverwendbarkeit, Aufräumen, Testbarkeit)

**Alles abgehakt?** Du beherrschst das Hooks-System von React!
