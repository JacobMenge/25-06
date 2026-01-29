# React Router - Praktische Übung

## Übersicht

Willkommen zur Übung zu React Router! Du hast bereits gelernt, wie du mit `useState`, `useEffect` und Custom Hooks arbeitest. Jetzt lernst du, wie du **Navigation** in React-Anwendungen umsetzt – ein absolutes Kernkonzept für jede echte Web-App mit mehreren Seiten.

In dieser Übung lernst du:
- **SPA-Navigation verstehen** - Warum React Router statt klassischer `<a>`-Tags
- **React Router installieren** - Das Package einrichten
- **Statische Routen** - Feste Pfade zu Pages definieren
- **Catch-All Route** - 404-Seiten für unbekannte Pfade
- **Parametrisierte Routen** - Dynamische URLs mit Parametern
- **useParams Hook** - Parameter in Komponenten auslesen
- **Link-Komponente** - Ohne Neuladen navigieren
- **Nested Routes** - Hierarchische Navigation strukturieren

Diese Übung baut auf "25.3 useEffect & API Calls" auf – stelle sicher, dass du Hooks und API-Calls verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | SPA vs. klassische Navigation | 5 min (lesen) |
| **Teil 1** | React Router installieren & einrichten | 15 min |
| **Teil 2** | Statische Routen erstellen | 20 min |
| **Teil 3** | Catch-All Route (404-Seite) | 10 min |
| **Teil 4** | Navigation mit Link | 15 min |
| **Teil 5** | Parametrisierte Routen | 20 min |
| **Teil 6** | useParams Hook | 15 min |
| **Teil 7** | Nested Routes (Subrouten) | 20 min |
| **Teil 8** | Praxis: Blog-App mit Navigation | 40 min |
| | **Gesamt** | **ca. 2,5 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - SPA-Navigation verstehen
2. **Teil 1** - React Router installieren - *Setup*
3. **Teil 2** - Statische Routen - *Kernkonzept*
4. **Teil 4** - Navigation mit Link - *Wichtig für UX*
5. **Teil 5 & 6** - Parametrisierte Routen & useParams - *Dynamische Seiten*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast **Node.js v20.19+** oder **v22.12+** installiert
2. Du hast ein funktionierendes React-Projekt (aus den vorherigen Übungen)
3. Der Dev-Server läuft (`npm run dev`)
4. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest router-uebung -- --template react
cd router-uebung
npm install
npm run dev
```

> **Tipp für diese Übung:** Du wirst mehrere "Pages" (Seiten-Komponenten) bauen. Erstelle einen Ordner `src/pages/` für diese Komponenten, um sie von normalen Komponenten zu unterscheiden.

---

## Rückblick: SPA vs. klassische Navigation

### Das Problem mit klassischer Navigation

In traditionellen Websites navigiert man mit `<a href="/about">`:

```html
<!-- Klassische Navigation -->
<a href="/about">Über uns</a>
```

**Was passiert dabei?**
1. Browser sendet neue HTTP-Anfrage an Server
2. Server antwortet mit komplett neuer HTML-Seite
3. Browser lädt alles neu (HTML, CSS, JS)
4. Seite "blinkt" kurz weiß beim Laden

### Single Page Applications (SPAs)

React-Apps sind **SPAs** – es gibt nur eine HTML-Seite, und der Inhalt wird per JavaScript ausgetauscht:

```
┌─────────────────────────────────────────────────────────────┐
│              KLASSISCH vs. SPA                              │
│                                                             │
│   Klassische Website:                                       │
│   ┌────────┐  Request  ┌────────┐                           │
│   │ Browser│ ────────> │ Server │                           │
│   │        │ <──────── │        │  Neue HTML-Seite          │
│   └────────┘           └────────┘                           │
│   → Komplettes Neuladen, langsam, "blinkt"                  │
│                                                             │
│   SPA (React):                                              │
│   ┌────────┐           ┌────────┐                           │
│   │ Browser│           │ React  │                           │
│   │        │  Klick    │ Router │                           │
│   └────────┘ ────────> └────────┘                           │
│   → JS tauscht Komponente aus, schnell, flüssig             │
│                                                             │
│   React Router ändert nur den sichtbaren Bereich,           │
│   ohne die Seite neu zu laden!                              │
└─────────────────────────────────────────────────────────────┘
```

### Wann welche Navigation?

| Navigation | Verwendung |
|------------|------------|
| **React Router (`<Link>`)** | Interne Navigation innerhalb deiner App |
| **Klassisch (`<a href>`)** | Externe Links zu anderen Websites |

---

## Teil 1: React Router installieren & einrichten

### Installation

React Router ist eine externe Library, die wir über NPM installieren:

```bash
npm install react-router-dom
```

Nach der Installation findest du `react-router-dom` in deiner `package.json` unter `dependencies`.

### BrowserRouter einrichten

Bevor wir Routen definieren können, müssen wir unsere App in einen `BrowserRouter` einwickeln. Das passiert in `main.jsx`:

```javascript
// src/main.jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
```

> **Warum BrowserRouter?** Der `BrowserRouter` "lauscht" auf URL-Änderungen und teilt React Router mit, welche Komponente angezeigt werden soll. Ohne ihn funktionieren `<Routes>`, `<Link>` und die Router-Hooks nicht.

### Übung 1: React Router installieren

> **Ziel:** React Router in deinem Projekt einrichten
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Die App ohne Fehler startet und BrowserRouter eingerichtet ist

**Aufgabe:**

1. Öffne ein Terminal in deinem Projektordner
2. Installiere React Router:

```bash
npm install react-router-dom
```

3. Öffne `src/main.jsx` und füge den `BrowserRouter` hinzu:

```javascript
// src/main.jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
```

4. Starte den Dev-Server (`npm run dev`) und prüfe, ob die App ohne Fehler läuft.

<details>
<summary>Fehlerbehebung anzeigen</summary>

**Fehler: "Cannot find module 'react-router-dom'"**
→ Hast du `npm install react-router-dom` ausgeführt? Prüfe, ob es in `package.json` steht.

**Fehler: "useHref() may be used only in the context of a Router component"**
→ Du hast vergessen, `<BrowserRouter>` in `main.jsx` einzufügen.

**Dev-Server zeigt alte Version**
→ Stoppe den Server (Strg+C) und starte ihn neu mit `npm run dev`.

</details>

### Wichtig: Deployment-Hinweis (später relevant!)

> **Achtung beim Deployment!** Im Dev-Server (`npm run dev`) funktioniert alles – Deep Links wie `/about` oder `/users/123` laden korrekt. **Aber:** Bei statischem Hosting (GitHub Pages, Netlify ohne Config, etc.) bekommst du beim Refresh auf `/about` einen **echten 404 vom Server**, weil der Server die Datei `/about.html` sucht, die nicht existiert.
>
> **Lösungen:**
> - **Vite/Netlify/Vercel:** SPA-Fallback konfigurieren (alle Anfragen → `index.html`)
> - **GitHub Pages:** Entweder `HashRouter` statt `BrowserRouter` verwenden, oder ein 404.html-Workaround
> - **Unterordner-Deployment** (z.B. `github.io/mein-repo/`): Du brauchst **zwei** Einstellungen:
>   ```javascript
>   // vite.config.js – damit Assets korrekt laden
>   export default defineConfig({
>     base: '/mein-repo/',
>     // ...
>   })
>   ```
>   ```javascript
>   // main.jsx – damit React Router die URLs korrekt interpretiert
>   <BrowserRouter basename="/mein-repo">
>   ```
>   Ohne `base` in Vite laden JS/CSS-Dateien nicht; ohne `basename` im Router stimmen die Pfade nicht.
>
> Für diese Übung im Dev-Modus ist das kein Problem – aber merke es dir für später!

---

## Teil 2: Statische Routen erstellen

### Was sind Routen?

Eine **Route** verbindet einen URL-Pfad mit einer Komponente:

```
URL: /about  →  Komponente: <About />
URL: /contact  →  Komponente: <Contact />
```

### Routes und Route Komponenten

```javascript
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
  );
}
```

### Wie funktioniert das Matching?

```
┌─────────────────────────────────────────────────────────────┐
│                    ROUTE MATCHING (v6/v7)                   │
│                                                             │
│   URL im Browser: /about                                    │
│                      │                                      │
│                      ▼                                      │
│   <Routes>                                                  │
│     <Route path="/" .../>        ❌ Kein Match              │
│     <Route path="/about" .../>   ✅ Best Match! → <About /> │
│     <Route path="/contact" .../>                            │
│   </Routes>                                                 │
│                                                             │
│   React Router v6/v7 wählt automatisch die SPEZIFISCHSTE    │
│   Route (Best Match). Die Reihenfolge im Code ist meist     │
│   egal – aber für Lesbarkeit: Wildcards (*) ans Ende.       │
└─────────────────────────────────────────────────────────────┘
```

> **Wichtig (v6/v7):** Anders als in älteren Versionen (v5 mit `<Switch>`) prüft React Router v6/v7 **nicht** einfach von oben nach unten. Stattdessen berechnet es einen "Ranking Score" für alle Routen und wählt die spezifischste. `/users/123` gewinnt gegen `/users/:id`, und `/users/:id` gewinnt gegen `*`. Du kannst die Reihenfolge trotzdem logisch sortieren – für Menschen, nicht für den Router.

### Übung 2: Erste Routen erstellen

> **Ziel:** Statische Routen für mehrere Pages einrichten
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du zwischen Home, About und Contact wechseln kannst (über die URL-Leiste)

**Aufgabe:**

1. Erstelle einen Ordner `src/pages/`

2. Erstelle `src/pages/Home.jsx`:

```javascript
// src/pages/Home.jsx

function Home() {
  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h1>Willkommen!</h1>
      <p>Dies ist die Startseite unserer React Router App.</p>
    </div>
  );
}

export default Home;
```

3. Erstelle `src/pages/About.jsx`:

```javascript
// src/pages/About.jsx

function About() {
  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h1>Über uns</h1>
      <p>Wir sind ein Team, das React liebt!</p>
    </div>
  );
}

export default About;
```

4. Erstelle `src/pages/Contact.jsx`:

```javascript
// src/pages/Contact.jsx

function Contact() {
  return (
    <div style={{ padding: '40px', textAlign: 'center' }}>
      <h1>Kontakt</h1>
      <p>Schreib uns eine E-Mail an: hello@example.com</p>
    </div>
  );
}

export default Contact;
```

5. Aktualisiere `src/App.jsx`:

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <div className="app">
      <Routes>
        {/* Aufgabe: Erstelle die Routen für Home, About und Contact */}
        {/* path="/" → Home */}
        {/* path="/about" → About */}
        {/* path="/contact" → Contact */}
      </Routes>
    </div>
  );
}

export default App;
```

6. Teste die Routen, indem du die URLs direkt im Browser eingibst:
   - `http://localhost:5173/`
   - `http://localhost:5173/about`
   - `http://localhost:5173/contact`

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </div>
  );
}

export default App;
```

> **Wichtig:** Das `element`-Attribut erwartet JSX, daher `element={<Home />}` und nicht `element={Home}`.

</details>

---

## Teil 3: Catch-All Route (404-Seite)

### Was passiert bei unbekannten URLs?

Wenn jemand `/xyz` eingibt und keine Route dafür existiert, zeigt React Router... nichts. Das ist keine gute User Experience!

### Die Lösung: Catch-All Route mit `*`

```javascript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />

  {/* Catch-All: Fängt alle nicht gematchten URLs */}
  <Route path="*" element={<NotFound />} />
</Routes>
```

Der Pfad `*` (Asterisk/Wildcard) matcht **alle** URLs, die von keiner anderen Route gefangen wurden.

> **Wichtig:** Die Catch-All Route sollte im Code am **Ende** stehen – nicht weil React Router v6/v7 zwingend in Reihenfolge prüft (tut es nicht!), sondern weil es für Menschen lesbarer ist. Der Wildcard `*` hat automatisch die niedrigste Priorität beim Matching.

### Übung 3: 404-Seite erstellen

> **Ziel:** Eine benutzerfreundliche 404-Seite anzeigen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Bei unbekannten URLs die NotFound-Seite erscheint

**Aufgabe:**

1. Erstelle `src/pages/NotFound.jsx`:

```javascript
// src/pages/NotFound.jsx

function NotFound() {
  return (
    <div style={{
      padding: '40px',
      textAlign: 'center',
      minHeight: '60vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center'
    }}>
      <h1 style={{ fontSize: '72px', margin: '0' }}>404</h1>
      <h2>Seite nicht gefunden</h2>
      <p style={{ color: '#666' }}>
        Die gesuchte Seite existiert leider nicht.
      </p>
      {/* Bonus: Füge später einen Link zur Startseite hinzu */}
    </div>
  );
}

export default NotFound;
```

2. Füge die Catch-All Route in `App.jsx` hinzu (am Ende der Routes!)

3. Teste: Gib eine ungültige URL ein wie `http://localhost:5173/xyz`

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import NotFound from './pages/NotFound';

function App() {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />

        {/* Catch-All Route - MUSS am Ende stehen! */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

</details>

---

## Teil 4: Navigation mit Link

### Das Problem mit `<a href>`

Wenn du normale HTML-Links verwendest, lädt der Browser die komplette Seite neu:

```javascript
// ❌ FALSCH – Lädt die Seite neu!
<a href="/about">Über uns</a>
```

### Die Lösung: `<Link>` Komponente

React Router bietet die `<Link>` Komponente, die Navigation **ohne** Neuladen ermöglicht:

```javascript
import { Link } from 'react-router-dom';

// ✅ RICHTIG – Kein Neuladen!
<Link to="/about">Über uns</Link>
```

### Link vs. a-Tag

| | `<a href>` | `<Link to>` |
|--|-----------|-------------|
| **Neuladen** | Ja, komplette Seite | Nein, nur Komponente |
| **Geschwindigkeit** | Langsam | Schnell |
| **State-Erhalt** | Geht verloren | Bleibt erhalten |
| **Verwendung** | Externe Links | Interne Navigation |

### Übung 4: Navigation-Komponente erstellen

> **Ziel:** Eine Navigationsleiste mit Links erstellen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du per Klick zwischen den Seiten navigieren kannst

**Aufgabe:**

1. Erstelle `src/components/Navigation.jsx`:

```javascript
// src/components/Navigation.jsx
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav style={{
      padding: '16px 24px',
      background: '#333',
      display: 'flex',
      gap: '24px'
    }}>
      {/* Aufgabe: Erstelle Links zu /, /about und /contact */}
      {/* Tipp: Verwende <Link to="...">Text</Link> */}
      {/* Style die Links mit style={{ color: '#fff', textDecoration: 'none' }} */}
    </nav>
  );
}

export default Navigation;
```

2. Binde die Navigation in `App.jsx` ein (außerhalb von `<Routes>`!):

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
// ... andere Imports

function App() {
  return (
    <div className="app">
      <Navigation />

      <Routes>
        {/* ... deine Routen */}
      </Routes>
    </div>
  );
}
```

3. Teste: Klicke auf die Links und beobachte die URL-Leiste – die Seite sollte **nicht** neu laden!

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/Navigation.jsx
import { Link } from 'react-router-dom';

function Navigation() {
  const linkStyle = {
    color: '#fff',
    textDecoration: 'none',
    padding: '8px 16px',
    borderRadius: '4px',
    transition: 'background 0.2s'
  };

  return (
    <nav style={{
      padding: '16px 24px',
      background: '#333',
      display: 'flex',
      gap: '8px'
    }}>
      <Link to="/" style={linkStyle}>
        Home
      </Link>
      <Link to="/about" style={linkStyle}>
        Über uns
      </Link>
      <Link to="/contact" style={linkStyle}>
        Kontakt
      </Link>
    </nav>
  );
}

export default Navigation;
```

> **Tipp:** Du kannst den DevTools Network-Tab öffnen und beobachten: Bei Klick auf einen `<Link>` werden **keine** neuen Requests gesendet – der Seitenwechsel passiert rein clientseitig!

</details>

### Wissensfrage 1

Wann verwendest du `<a href>` und wann `<Link to>`?

<details>
<summary>Antwort anzeigen</summary>

**`<Link to>`** für interne Navigation innerhalb deiner React-App:
```javascript
<Link to="/about">Über uns</Link>
<Link to="/users/123">Profil</Link>
```

**`<a href>`** für externe Links zu anderen Websites:
```javascript
<a href="https://github.com" target="_blank" rel="noopener noreferrer">
  GitHub
</a>
```

**Faustregel:** Wenn die URL mit `/` beginnt (interner Pfad) → `<Link>`. Wenn die URL mit `http` beginnt (externe Website) → `<a>`.

</details>

---

## Teil 5: Parametrisierte Routen

### Das Problem: Dynamische URLs

Stell dir vor, du hast eine User-Liste und willst für jeden User eine Profilseite:

```
/users/1    → Profil von User 1
/users/2    → Profil von User 2
/users/42   → Profil von User 42
```

Du kannst nicht für jeden User eine eigene Route schreiben!

### Die Lösung: URL-Parameter mit `:`

```javascript
<Route path="/users/:userId" element={<UserProfile />} />
```

Der `:userId` Teil ist ein **Parameter** – er matcht jeden Wert an dieser Stelle:

```
┌─────────────────────────────────────────────────────────────┐
│              PARAMETRISIERTE ROUTEN                         │
│                                                             │
│   Route:  /users/:userId                                    │
│                                                             │
│   URL: /users/1     → Match! userId = "1"                   │
│   URL: /users/42    → Match! userId = "42"                  │
│   URL: /users/anna  → Match! userId = "anna"                │
│   URL: /users       → Kein Match (Parameter fehlt)          │
│   URL: /users/1/2   → Kein Match (zu viele Segmente)        │
│                                                             │
│   Der Parameterwert ist IMMER ein String!                   │
└─────────────────────────────────────────────────────────────┘
```

### Mehrere Parameter

Du kannst auch mehrere Parameter kombinieren:

```javascript
<Route path="/posts/:year/:month/:slug" element={<BlogPost />} />
// Matcht: /posts/2024/01/mein-erster-post
```

### Übung 5: User-Routen mit Parameter

> **Ziel:** Dynamische Routen mit URL-Parametern erstellen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Die Route `/users/123` die UserProfile-Seite anzeigt

**Aufgabe:**

1. Erstelle `src/pages/Users.jsx` (Übersichtsseite):

```javascript
// src/pages/Users.jsx

function Users() {
  // Simulierte User-Daten
  const users = [
    { id: 1, name: 'Max Mustermann' },
    { id: 2, name: 'Anna Schmidt' },
    { id: 3, name: 'Tom Weber' }
  ];

  return (
    <div style={{ padding: '40px' }}>
      <h1>Benutzer</h1>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map(user => (
          <li key={user.id} style={{ marginBottom: '8px' }}>
            {/* Aufgabe: Füge einen Link zu /users/{user.id} hinzu */}
            {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
```

2. Erstelle `src/pages/UserProfile.jsx` (Detailseite):

```javascript
// src/pages/UserProfile.jsx

function UserProfile() {
  return (
    <div style={{ padding: '40px' }}>
      <h1>Benutzerprofil</h1>
      <p>Hier wird später das Profil angezeigt.</p>
      {/* Im nächsten Teil lernen wir, wie wir die userId auslesen */}
    </div>
  );
}

export default UserProfile;
```

3. Füge die Routen in `App.jsx` hinzu:

```javascript
// In App.jsx – füge diese Routen hinzu:
<Route path="/users" element={<Users />} />
<Route path="/users/:userId" element={<UserProfile />} />
```

4. Füge einen "Benutzer"-Link zur Navigation hinzu

5. Teste: Gehe zu `/users` und dann zu `/users/1`, `/users/42`, etc.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/pages/Users.jsx
import { Link } from 'react-router-dom';

function Users() {
  const users = [
    { id: 1, name: 'Max Mustermann' },
    { id: 2, name: 'Anna Schmidt' },
    { id: 3, name: 'Tom Weber' }
  ];

  return (
    <div style={{ padding: '40px' }}>
      <h1>Benutzer</h1>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map(user => (
          <li key={user.id} style={{ marginBottom: '12px' }}>
            <Link
              to={`/users/${user.id}`}
              style={{
                color: '#3498db',
                textDecoration: 'none',
                fontSize: '18px'
              }}
            >
              {user.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
```

```javascript
// src/App.jsx (vollständig)
import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Users from './pages/Users';
import UserProfile from './pages/UserProfile';
import NotFound from './pages/NotFound';

function App() {
  return (
    <div className="app">
      <Navigation />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/users" element={<Users />} />
        <Route path="/users/:userId" element={<UserProfile />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

> **Hinweis:** Beachte, dass `/users` und `/users/:userId` zwei separate Routen sind. Die erste matcht exakt `/users`, die zweite matcht `/users/irgendwas`.

</details>

---

## Teil 6: useParams Hook

### Das Problem: Wie komme ich an den Parameter?

Wir haben jetzt eine Route `/users/:userId`, aber wie lesen wir den `userId`-Wert in der Komponente aus?

### Die Lösung: useParams Hook

```javascript
import { useParams } from 'react-router-dom';

function UserProfile() {
  // useParams gibt ein Objekt mit allen URL-Parametern zurück
  const { userId } = useParams();

  return <h1>Profil von User {userId}</h1>;
}
```

### Wie useParams funktioniert

```
┌─────────────────────────────────────────────────────────────┐
│                    useParams                                │
│                                                             │
│   Route:    /users/:userId                                  │
│   URL:      /users/42                                       │
│                                                             │
│   const params = useParams();                               │
│   // params = { userId: "42" }                              │
│                                                             │
│   const { userId } = useParams();                           │
│   // userId = "42"                                          │
│                                                             │
│   WICHTIG: Parameter sind IMMER Strings!                    │
│   Für Zahlen: Number(userId) oder parseInt(userId)          │
└─────────────────────────────────────────────────────────────┘
```

### Übung 6: Parameter auslesen und verwenden

> **Ziel:** Den URL-Parameter in der Komponente nutzen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Die UserProfile-Seite den korrekten User anzeigt

**Aufgabe:**

1. Aktualisiere `src/pages/UserProfile.jsx`:

```javascript
// src/pages/UserProfile.jsx
import { useParams } from 'react-router-dom';

// Simulierte User-Datenbank
const usersData = {
  1: { id: 1, name: 'Max Mustermann', email: 'max@example.com', role: 'Developer' },
  2: { id: 2, name: 'Anna Schmidt', email: 'anna@example.com', role: 'Designer' },
  3: { id: 3, name: 'Tom Weber', email: 'tom@example.com', role: 'Manager' }
};

function UserProfile() {
  // Aufgabe 1: Hole den userId Parameter mit useParams
  // const { userId } = ???

  // Aufgabe 2: Finde den User in usersData
  // const user = usersData[???]

  // Aufgabe 3: Zeige "User nicht gefunden" wenn der User nicht existiert
  // if (!user) { return ??? }

  return (
    <div style={{ padding: '40px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Benutzerprofil</h1>

      {/* Aufgabe 4: Zeige die User-Daten an */}
      <div style={{
        padding: '24px',
        border: '1px solid #ddd',
        borderRadius: '12px',
        marginTop: '20px'
      }}>
        {/* Name, Email, Role anzeigen */}
      </div>
    </div>
  );
}

export default UserProfile;
```

2. Teste verschiedene User-IDs:
   - `/users/1` → Max Mustermann
   - `/users/2` → Anna Schmidt
   - `/users/99` → User nicht gefunden

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/pages/UserProfile.jsx
import { useParams, Link } from 'react-router-dom';

const usersData = {
  1: { id: 1, name: 'Max Mustermann', email: 'max@example.com', role: 'Developer' },
  2: { id: 2, name: 'Anna Schmidt', email: 'anna@example.com', role: 'Designer' },
  3: { id: 3, name: 'Tom Weber', email: 'tom@example.com', role: 'Manager' }
};

function UserProfile() {
  const { userId } = useParams();

  // User aus "Datenbank" holen
  const user = usersData[userId];

  // User nicht gefunden
  if (!user) {
    return (
      <div style={{ padding: '40px', textAlign: 'center' }}>
        <h1>User nicht gefunden</h1>
        <p>Es gibt keinen User mit der ID {userId}.</p>
        <Link to="/users" style={{ color: '#3498db' }}>
          Zurück zur Übersicht
        </Link>
      </div>
    );
  }

  return (
    <div style={{ padding: '40px', maxWidth: '600px', margin: '0 auto' }}>
      <Link to="/users" style={{ color: '#3498db', textDecoration: 'none' }}>
        ← Zurück zur Übersicht
      </Link>

      <h1 style={{ marginTop: '20px' }}>Benutzerprofil</h1>

      <div style={{
        padding: '24px',
        border: '1px solid #ddd',
        borderRadius: '12px',
        marginTop: '20px'
      }}>
        <h2 style={{ margin: '0 0 16px 0' }}>{user.name}</h2>
        <p style={{ margin: '8px 0', color: '#666' }}>
          <strong>E-Mail:</strong> {user.email}
        </p>
        <p style={{ margin: '8px 0', color: '#666' }}>
          <strong>Rolle:</strong> {user.role}
        </p>
        <p style={{ margin: '8px 0', color: '#999', fontSize: '14px' }}>
          User-ID: {user.id}
        </p>
      </div>
    </div>
  );
}

export default UserProfile;
```

> **Wichtig:** `useParams()` gibt IMMER Strings zurück! Wenn du den Parameter als Zahl brauchst (z.B. für Vergleiche), musst du ihn konvertieren: `Number(userId)` oder `parseInt(userId, 10)`.

</details>

### Wissensfrage 2

Warum ist `userId` aus `useParams()` ein String und keine Zahl?

<details>
<summary>Antwort anzeigen</summary>

URL-Parameter kommen aus der Browser-URL, die immer ein String ist. React Router parst diese nicht automatisch zu Zahlen, weil:

1. **Nicht alle IDs sind Zahlen** – manchmal verwendet man UUIDs wie `a1b2c3d4` oder Slugs wie `mein-artikel`
2. **Typsicherheit** – du entscheidest selbst, ob und wie du konvertierst
3. **Konsistenz** – alle Parameter werden gleich behandelt

Wenn du eine Zahl brauchst:
```javascript
const { userId } = useParams();
const userIdNumber = Number(userId);  // oder parseInt(userId, 10)
```

</details>

---

## Teil 7: Nested Routes (Subrouten)

### Das Problem: Viele ähnliche Pfade

Bei komplexeren Apps hast du oft viele verwandte Routen:

```javascript
<Route path="/users" element={<Users />} />
<Route path="/users/:userId" element={<UserProfile />} />
<Route path="/users/:userId/posts" element={<UserPosts />} />
<Route path="/users/:userId/settings" element={<UserSettings />} />
```

Das wird schnell unübersichtlich und fehleranfällig.

### Die Lösung: Nested Routes

Mit Subrouten kannst du zusammengehörige Routen gruppieren:

```javascript
<Route path="/users">
  <Route index element={<Users />} />
  <Route path=":userId" element={<UserProfile />} />
  <Route path=":userId/posts" element={<UserPosts />} />
</Route>
```

### Wichtige Konzepte

> **Wichtig: `<Outlet>` bei Layout-Komponenten!**
> In dieser Übung nutzen wir Nested Routes **ohne** Parent-Element (nur als Pfad-Gruppierung). Wenn du später eine Parent-Route mit eigenem `element` verwendest (z.B. ein Layout), muss dieses Layout ein `<Outlet />` rendern – sonst erscheinen die Child-Routen nicht!
>
> ```javascript
> // Layout mit Outlet
> import { Outlet } from 'react-router-dom';
>
> function UsersLayout() {
>   return (
>     <div>
>       <h1>Benutzerbereich</h1>
>       <Outlet />  {/* ← Hier werden Child-Routen gerendert! */}
>     </div>
>   );
> }
>
> // Verwendung:
> <Route path="/users" element={<UsersLayout />}>
>   <Route index element={<Users />} />
>   <Route path=":userId" element={<UserProfile />} />
> </Route>
> ```

```
┌─────────────────────────────────────────────────────────────┐
│                  NESTED ROUTES                              │
│                                                             │
│   <Route path="/users">                                     │
│     ├── <Route index .../>        →  /users                 │
│     ├── <Route path=":id" .../>   →  /users/123             │
│     └── <Route path=":id/posts"/> →  /users/123/posts       │
│   </Route>                                                  │
│                                                             │
│   Wichtig:                                                  │
│   • index = Route ohne eigenen Pfad (Default-Child)         │
│   • Kinder-Pfade sind RELATIV (kein führendes /)            │
│   • :id/posts = /users/:id/posts (automatisch kombiniert)   │
└─────────────────────────────────────────────────────────────┘
```

### Übung 7: Navigation mit Subrouten

> **Ziel:** Routen hierarchisch strukturieren
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Deine User-Routen als Nested Routes organisiert sind

**Aufgabe:**

1. Refaktoriere deine User-Routen in `App.jsx` zu Nested Routes:

```javascript
// Vorher (flache Struktur):
<Route path="/users" element={<Users />} />
<Route path="/users/:userId" element={<UserProfile />} />

// Nachher (nested):
<Route path="/users">
  <Route index element={<Users />} />
  <Route path=":userId" element={<UserProfile />} />
</Route>
```

2. Erstelle eine zusätzliche Seite `src/pages/UserPosts.jsx`:

```javascript
// src/pages/UserPosts.jsx
import { useParams, Link } from 'react-router-dom';

function UserPosts() {
  const { userId } = useParams();

  // Simulierte Posts
  const posts = [
    { id: 1, title: 'Mein erster Post' },
    { id: 2, title: 'React ist toll!' },
    { id: 3, title: 'Heute gelernt: Routing' }
  ];

  return (
    <div style={{ padding: '40px' }}>
      <Link to={`/users/${userId}`} style={{ color: '#3498db' }}>
        ← Zurück zum Profil
      </Link>

      <h1 style={{ marginTop: '20px' }}>Posts von User {userId}</h1>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {posts.map(post => (
          <li key={post.id} style={{
            padding: '12px',
            marginBottom: '8px',
            background: '#f5f5f5',
            borderRadius: '8px'
          }}>
            {post.title}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserPosts;
```

3. Füge die Route als Subroute hinzu

4. Füge in `UserProfile.jsx` einen Link zu den Posts hinzu:
   ```javascript
   <Link to={`/users/${userId}/posts`}>Posts anzeigen</Link>
   ```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Users from './pages/Users';
import UserProfile from './pages/UserProfile';
import UserPosts from './pages/UserPosts';
import NotFound from './pages/NotFound';

function App() {
  return (
    <div className="app">
      <Navigation />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />

        {/* Nested Routes für Users */}
        <Route path="/users">
          <Route index element={<Users />} />
          <Route path=":userId" element={<UserProfile />} />
          <Route path=":userId/posts" element={<UserPosts />} />
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

```javascript
// Ergänzung in src/pages/UserProfile.jsx
// Füge diesen Link nach den User-Details hinzu:

<Link
  to={`/users/${userId}/posts`}
  style={{
    display: 'inline-block',
    marginTop: '16px',
    padding: '10px 20px',
    background: '#3498db',
    color: '#fff',
    borderRadius: '6px',
    textDecoration: 'none'
  }}
>
  Posts anzeigen
</Link>
```

> **Vorteile von Nested Routes:**
> - Bessere Übersicht bei vielen Routen
> - Weniger Wiederholung (kein `/users/` überall)
> - Logische Gruppierung zusammengehöriger Seiten
> - Einfacher zu refaktorieren (Pfad nur an einer Stelle ändern)

</details>

---

## Teil 8: Praxis - Blog-App mit Navigation

Zeit für die Abschlussübung! Du baust eine kleine Blog-App, die alles Gelernte kombiniert.

> **Ziel:** Eine Blog-App mit mehreren Seiten und dynamischen Routen
> **Zeitbedarf:** ca. 40 Minuten
> **Du bist fertig, wenn:** Du zwischen Blog-Übersicht und einzelnen Artikeln navigieren kannst

### Anforderungen

1. **Home-Seite** (`/`) – Willkommenstext
2. **Blog-Übersicht** (`/blog`) – Liste aller Artikel
3. **Artikel-Detail** (`/blog/:slug`) – Einzelner Artikel
4. **404-Seite** – Für unbekannte URLs und unbekannte Artikel
5. **Navigation** – Links zu allen Hauptseiten

### Datenstruktur

Erstelle `src/data/posts.js`:

```javascript
// src/data/posts.js
export const posts = [
  {
    slug: 'react-einfuehrung',
    title: 'Einführung in React',
    date: '2024-01-15',
    excerpt: 'React ist eine JavaScript-Bibliothek für User Interfaces...',
    content: `
      React wurde von Facebook entwickelt und ist heute eine der beliebtesten
      Frontend-Bibliotheken. In diesem Artikel lernst du die Grundlagen.

      React verwendet eine deklarative Syntax namens JSX, die HTML-ähnlich ist
      aber JavaScript ermöglicht. Komponenten sind wiederverwendbare UI-Bausteine.
    `
  },
  {
    slug: 'react-router-guide',
    title: 'React Router verstehen',
    date: '2024-01-20',
    excerpt: 'Navigation in Single Page Applications leicht gemacht...',
    content: `
      React Router ermöglicht clientseitige Navigation in React-Apps.
      Statt die Seite neu zu laden, werden nur Komponenten ausgetauscht.

      Die wichtigsten Konzepte sind Routes, Links und der useParams Hook.
      Mit diesen Bausteinen kannst du komplexe Navigation aufbauen.
    `
  },
  {
    slug: 'hooks-erklaert',
    title: 'React Hooks erklärt',
    date: '2024-01-25',
    excerpt: 'useState, useEffect und mehr – alles über Hooks...',
    content: `
      Hooks wurden in React 16.8 eingeführt und erlauben es,
      State und andere React-Features in Funktionskomponenten zu nutzen.

      Die wichtigsten Hooks sind useState für lokalen State,
      useEffect für Seiteneffekte und useRef für DOM-Zugriff.
    `
  }
];

// Hilfsfunktion: Post by Slug finden
export function getPostBySlug(slug) {
  return posts.find(post => post.slug === slug);
}
```

### Komponenten-Struktur

```
src/
├── components/
│   └── Navigation.jsx
├── pages/
│   ├── Home.jsx
│   ├── Blog.jsx
│   ├── BlogPost.jsx
│   └── NotFound.jsx
├── data/
│   └── posts.js
├── App.jsx
└── main.jsx
```

### Aufgabe

1. **Erstelle `src/pages/Blog.jsx`:**

```javascript
// src/pages/Blog.jsx
import { Link } from 'react-router-dom';
import { posts } from '../data/posts';

function Blog() {
  return (
    <div style={{ padding: '40px', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Blog</h1>
      <p style={{ color: '#666', marginBottom: '32px' }}>
        {posts.length} Artikel verfügbar
      </p>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        {/* Aufgabe: Rendere die Posts als Karten mit Link zum Detail */}
        {posts.map(post => (
          <article key={post.slug} style={{
            padding: '24px',
            border: '1px solid #ddd',
            borderRadius: '12px'
          }}>
            {/* Titel als Link zu /blog/{post.slug} */}
            {/* Datum */}
            {/* Excerpt */}
            {/* "Weiterlesen" Link */}
          </article>
        ))}
      </div>
    </div>
  );
}

export default Blog;
```

2. **Erstelle `src/pages/BlogPost.jsx`:**

```javascript
// src/pages/BlogPost.jsx
import { useParams, Link } from 'react-router-dom';
import { getPostBySlug } from '../data/posts';

function BlogPost() {
  // Aufgabe 1: Hole den slug Parameter

  // Aufgabe 2: Finde den Post mit getPostBySlug(slug)

  // Aufgabe 3: Zeige 404-ähnliche Meldung wenn Post nicht existiert

  return (
    <article style={{ padding: '40px', maxWidth: '800px', margin: '0 auto' }}>
      {/* Aufgabe 4: Zurück-Link */}

      {/* Aufgabe 5: Titel, Datum, Content anzeigen */}
    </article>
  );
}

export default BlogPost;
```

3. **Aktualisiere die Navigation**

4. **Füge die Routen in `App.jsx` hinzu** (als Nested Routes!)

<details>
<summary>Musterlösung anzeigen</summary>

**src/pages/Blog.jsx:**

```javascript
import { Link } from 'react-router-dom';
import { posts } from '../data/posts';

function Blog() {
  return (
    <div style={{ padding: '40px', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Blog</h1>
      <p style={{ color: '#666', marginBottom: '32px' }}>
        {posts.length} Artikel verfügbar
      </p>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        {posts.map(post => (
          <article key={post.slug} style={{
            padding: '24px',
            border: '1px solid #ddd',
            borderRadius: '12px',
            transition: 'box-shadow 0.2s'
          }}>
            <Link
              to={`/blog/${post.slug}`}
              style={{ textDecoration: 'none', color: 'inherit' }}
            >
              <h2 style={{ margin: '0 0 8px 0', color: '#333' }}>
                {post.title}
              </h2>
            </Link>

            <p style={{ margin: '0 0 12px 0', color: '#999', fontSize: '14px' }}>
              {new Date(post.date).toLocaleDateString('de-DE', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
              })}
            </p>

            <p style={{ margin: '0 0 16px 0', color: '#666' }}>
              {post.excerpt}
            </p>

            <Link
              to={`/blog/${post.slug}`}
              style={{
                color: '#3498db',
                textDecoration: 'none',
                fontWeight: '500'
              }}
            >
              Weiterlesen →
            </Link>
          </article>
        ))}
      </div>
    </div>
  );
}

export default Blog;
```

**src/pages/BlogPost.jsx:**

```javascript
import { useParams, Link } from 'react-router-dom';
import { getPostBySlug } from '../data/posts';

function BlogPost() {
  const { slug } = useParams();
  const post = getPostBySlug(slug);

  if (!post) {
    return (
      <div style={{ padding: '40px', textAlign: 'center' }}>
        <h1>Artikel nicht gefunden</h1>
        <p style={{ color: '#666' }}>
          Es gibt keinen Artikel mit dem Slug "{slug}".
        </p>
        <Link
          to="/blog"
          style={{
            display: 'inline-block',
            marginTop: '16px',
            padding: '10px 20px',
            background: '#3498db',
            color: '#fff',
            borderRadius: '6px',
            textDecoration: 'none'
          }}
        >
          Zurück zum Blog
        </Link>
      </div>
    );
  }

  return (
    <article style={{ padding: '40px', maxWidth: '800px', margin: '0 auto' }}>
      <Link
        to="/blog"
        style={{ color: '#3498db', textDecoration: 'none' }}
      >
        ← Zurück zum Blog
      </Link>

      <h1 style={{ marginTop: '24px', marginBottom: '8px' }}>
        {post.title}
      </h1>

      <p style={{ color: '#999', marginBottom: '32px' }}>
        {new Date(post.date).toLocaleDateString('de-DE', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        })}
      </p>

      <div style={{
        lineHeight: '1.8',
        color: '#333',
        whiteSpace: 'pre-line'
      }}>
        {post.content}
      </div>
    </article>
  );
}

export default BlogPost;
```

**src/components/Navigation.jsx (aktualisiert):**

```javascript
import { Link } from 'react-router-dom';

function Navigation() {
  const linkStyle = {
    color: '#fff',
    textDecoration: 'none',
    padding: '8px 16px'
  };

  return (
    <nav style={{
      padding: '16px 24px',
      background: '#333',
      display: 'flex',
      gap: '8px'
    }}>
      <Link to="/" style={linkStyle}>Home</Link>
      <Link to="/blog" style={linkStyle}>Blog</Link>
      <Link to="/users" style={linkStyle}>Benutzer</Link>
      <Link to="/about" style={linkStyle}>Über uns</Link>
      <Link to="/contact" style={linkStyle}>Kontakt</Link>
    </nav>
  );
}

export default Navigation;
```

**src/App.jsx (vollständig):**

```javascript
import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Users from './pages/Users';
import UserProfile from './pages/UserProfile';
import UserPosts from './pages/UserPosts';
import Blog from './pages/Blog';
import BlogPost from './pages/BlogPost';
import NotFound from './pages/NotFound';

function App() {
  return (
    <div className="app">
      <Navigation />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />

        {/* User Routes (nested) */}
        <Route path="/users">
          <Route index element={<Users />} />
          <Route path=":userId" element={<UserProfile />} />
          <Route path=":userId/posts" element={<UserPosts />} />
        </Route>

        {/* Blog Routes (nested) */}
        <Route path="/blog">
          <Route index element={<Blog />} />
          <Route path=":slug" element={<BlogPost />} />
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

> **Was du gebaut hast:**
> - Multi-Page React-App mit clientseitiger Navigation
> - Dynamische Routen mit Slug-Parametern
> - Saubere Nested Route Struktur
> - Fehlerbehandlung für nicht existierende Artikel
> - Zurück-Navigation zwischen Seiten

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **BrowserRouter** | Aktiviert React Router | `<BrowserRouter><App /></BrowserRouter>` |
| **Routes & Route** | Routen definieren | `<Route path="/about" element={<About />} />` |
| **Catch-All Route** | 404-Seite | `<Route path="*" element={<NotFound />} />` |
| **Link** | Ohne Neuladen navigieren | `<Link to="/about">Über uns</Link>` |
| **URL-Parameter** | Dynamische Pfadsegmente | `path="/users/:userId"` |
| **useParams** | Parameter auslesen | `const { userId } = useParams()` |
| **Nested Routes** | Hierarchische Routen | `<Route path="/users"><Route index .../></Route>` |

### React Router auf einen Blick

```javascript
// Setup in main.jsx
import { BrowserRouter } from 'react-router-dom';
<BrowserRouter><App /></BrowserRouter>

// Routen in App.jsx
import { Routes, Route, Link } from 'react-router-dom';

<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/users/:id" element={<User />} />
  <Route path="*" element={<NotFound />} />
</Routes>

// Navigation
<Link to="/users/123">User 123</Link>

// Parameter auslesen
import { useParams } from 'react-router-dom';
const { id } = useParams();
```

### Häufige Fehler vermeiden

```
┌─────────────────────────────────────────────────────────────┐
│              HÄUFIGE FEHLER MIT REACT ROUTER                │
│                                                             │
│   FEHLER: <a href> statt <Link to>                          │
│      <a href="/about">  → Seite lädt neu!                   │
│      → Fix: <Link to="/about">                              │
│                                                             │
│   FEHLER: BrowserRouter vergessen                           │
│      → "useHref() may be used only in context of Router"    │
│      → Fix: BrowserRouter in main.jsx einbinden             │
│                                                             │
│   FEHLER: Parameter mit / beginnen in nested routes         │
│      <Route path="/users">                                  │
│        <Route path="/:id" />  ← FALSCH (/ am Anfang)        │
│        <Route path=":id" />   ← RICHTIG (relativ)           │
│      </Route>                                               │
│                                                             │
│   FEHLER: <Outlet> vergessen bei Layout-Routen              │
│      Parent mit element={<Layout />} braucht <Outlet />     │
│      in der Layout-Komponente, sonst: leere Seite!          │
│                                                             │
│   FEHLER: 404 nach Deployment (Refresh auf /about)          │
│      → Server kennt /about nicht, nur React Router          │
│      → Fix: SPA-Fallback konfigurieren oder HashRouter      │
└─────────────────────────────────────────────────────────────┘
```

> **Hinweis zu "Post nicht gefunden":** Die Catch-All Route (`path="*"`) greift nur bei **unbekannten URLs**. Wenn `/blog/xyz` als Route existiert, aber der Artikel `xyz` nicht in deinen Daten ist, musst du das **in der Komponente selbst** abfangen (wie in `BlogPost.jsx` gezeigt). Die 404-Page ist für URL-Ebene, nicht für Daten-Ebene.

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du verstehst den Unterschied zwischen SPA und klassischer Navigation
- [ ] Du kannst React Router installieren und BrowserRouter einrichten
- [ ] Du kannst statische Routen mit `<Route path element>` erstellen
- [ ] Du kannst eine Catch-All Route (`path="*"`) für 404-Seiten einrichten
- [ ] Du verwendest `<Link>` statt `<a>` für interne Navigation
- [ ] Du kannst parametrisierte Routen mit `:parameter` erstellen
- [ ] Du kannst mit `useParams()` URL-Parameter auslesen
- [ ] Du kannst Routen mit Nested Routes hierarchisch strukturieren

**Alles abgehakt?** Du beherrschst React Router!
