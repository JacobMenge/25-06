# Optionales Assignment: React App mit Routing (Einzelarbeit)

## Wochenabschluss: React Fortgeschritten (Woche 4)

### Organisatorische Rahmenbedingungen

**Dieses Assignment ist freiwillig!** Es dient der Vertiefung der Woche und kann eingereicht werden, falls ihr Feedback von uns wünscht.

Falls du abgeben möchtest, reiche deinen Projektordner ein (bis Montag, 23:59 Uhr):

```
vorname_nachname_woche4/
    src/
        components/
            ... (deine Komponenten)
        pages/
            ... (deine Pages)
        hooks/
            ... (optional: Custom Hooks)
        data/
            ... (optional: JSON-Dateien)
        App.jsx
        App.css
        main.jsx
    index.html
    package.json
    README.md
```

**Hinweis:** Lade NICHT den `node_modules` Ordner hoch! Komprimiere deinen Projektordner als ZIP-Datei (ohne `node_modules`).

Der thematische Umfang dieser Aufgabe erstreckt sich über die React-Fortgeschrittenen-Themen der Woche:
- CSS in React (Inline Styles, CSS Modules oder Styled Components)
- React Hooks (useState, useEffect, Custom Hooks)
- API Calls mit useEffect und fetch
- React Router (Routes, Link, useParams, Nested Routes)

---

## Abgabe (optional)

**Wichtig vor dem Hochladen:**

1. Lösche den `node_modules` Ordner (dieser kann sehr groß sein!)
2. Komprimiere den Ordner als ZIP-Datei
3. Lade die ZIP-Datei hoch

Zum Testen kann die App mit folgenden Befehlen wiederhergestellt werden:
```bash
npm install
npm run dev
```

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

Mit diesem Assignment zeigst du, dass du die fortgeschrittenen React-Konzepte verstanden hast. Es geht darum, eine **funktionierende React-App mit mehreren Seiten** zu erstellen, die Daten von einer API lädt und React Router für die Navigation verwendet.

**Wichtig:** Eine einfache, funktionierende App ist besser als eine komplexe, fehlerhafte!

Du hast die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Thema (Kreativ)

Erstelle eine React-App zu einem Thema deiner Wahl mit mehreren Seiten und API-Anbindung.

### Mindestanforderungen:

**React Router:**
- Mindestens 3 verschiedene Pages (z.B. Home, Liste, Detail)
- Mindestens eine parametrisierte Route (z.B. `/items/:id`)
- Navigation mit `<Link>` Komponente
- Eine Catch-All Route (404-Seite)

**Hooks:**
- `useState` für State Management
- `useEffect` für API-Calls oder Side Effects
- `useParams` zum Auslesen von URL-Parametern

**API & Daten:**
- Daten von einer öffentlichen API laden (oder lokale JSON-Datei)
- Loading-State während des Ladens anzeigen
- Error Handling implementieren

**Komponenten:**
- Mindestens 4 eigene Komponenten
- Props für Datenübergabe zwischen Komponenten
- Sinnvolle Komponenten-Aufteilung (Pages vs. Components)

**Styling:**
- Konsistentes Styling (Inline Styles, CSS-Datei oder CSS Modules)
- Responsive Grundlagen (App sollte auf verschiedenen Bildschirmgrößen funktionieren)

### Kostenlose APIs für Ideen:

| API | URL | Beschreibung |
|-----|-----|--------------|
| JSONPlaceholder | `https://jsonplaceholder.typicode.com` | Fake Blog-Posts, User, Todos |
| Pokemon API | `https://pokeapi.co/api/v2/pokemon` | Pokemon-Daten |
| Rick and Morty | `https://rickandmortyapi.com/api` | Charaktere, Episoden |
| Open Library | `https://openlibrary.org/search.json?q=` | Bücher-Suche |
| Dog API | `https://dog.ceo/api` | Hunde-Bilder |
| The Meal DB | `https://www.themealdb.com/api/json/v1/1` | Rezepte |

### Ideen für Apps:

| App-Idee | Beschreibung |
|----------|--------------|
| **Pokemon-Dex** | Pokemon-Liste, Klick auf Pokemon zeigt Detail-Seite |
| **Blog-Reader** | Posts-Übersicht, einzelne Post-Seite, Autor-Seite |
| **Rezept-Finder** | Rezepte durchsuchen, Detail-Ansicht mit Zutaten |
| **Film-Datenbank** | Filme auflisten, Detail-Seite mit Infos |
| **Bücher-Suche** | Bücher suchen, Detail-Ansicht |
| **User-Verzeichnis** | User-Liste, Profil-Seite mit Details |

---

## Weg B: Geführte Aufgabe (Schritt für Schritt)

Falls du lieber einer Anleitung folgen möchtest, baue diese **Blog-App mit Navigation**.

### Was wir bauen:

Eine Blog-App, die:
1. Eine Startseite mit Willkommenstext hat
2. Blog-Posts von einer API lädt und als Liste anzeigt
3. Einzelne Blog-Posts auf einer Detail-Seite zeigt
4. User-Profile anzeigen kann (Autor des Posts)
5. Eine 404-Seite für unbekannte URLs hat
6. Loading- und Error-States korrekt behandelt

**Am Ende hast du automatisch alle Anforderungen erfüllt!**

---

### Schritt 1: Projekt erstellen und React Router installieren

Falls du noch kein Projekt hast:

```bash
npm create vite@latest blog-app -- --template react
cd blog-app
npm install
npm install react-router-dom
npm run dev
```

Falls du ein bestehendes Projekt verwendest:

```bash
npm install react-router-dom
```

> **Wichtig: Node.js Version!**
> React Router v7 (aktuell) erfordert **mindestens Node.js 20**. Prüfe deine Version mit `node -v`. Falls du Node 18 verwendest, installiere stattdessen explizit v6:
> ```bash
> npm install react-router-dom@6
> ```
> Der Code in diesem Assignment funktioniert mit beiden Versionen identisch.

---

### Schritt 2: Projektstruktur vorbereiten

Erstelle folgende Ordnerstruktur:

```
src/
├── components/
│   ├── Navigation.jsx
│   ├── PostCard.jsx
│   └── LoadingSpinner.jsx
├── pages/
│   ├── Home.jsx
│   ├── Posts.jsx
│   ├── PostDetail.jsx
│   ├── UserProfile.jsx
│   └── NotFound.jsx
├── App.jsx
├── App.css
├── index.css
└── main.jsx
```

---

### Schritt 3: main.jsx - BrowserRouter einrichten

Aktualisiere `src/main.jsx`:

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

**Erklärung:**
- `BrowserRouter` muss die gesamte App umschließen
- Dadurch können alle Komponenten React Router nutzen

---

### Schritt 4: Navigation-Komponente erstellen

Erstelle `src/components/Navigation.jsx`:

```javascript
// src/components/Navigation.jsx
import { Link } from 'react-router-dom';

function Navigation() {
  const navStyle = {
    display: 'flex',
    gap: '24px',
    padding: '16px 24px',
    background: '#2c3e50',
    listStyle: 'none',
    margin: 0
  };

  const linkStyle = {
    color: '#ecf0f1',
    textDecoration: 'none',
    fontSize: '16px',
    padding: '8px 16px',
    borderRadius: '4px'
  };

  return (
    <nav>
      <ul style={navStyle}>
        <li>
          <Link to="/" style={linkStyle}>Home</Link>
        </li>
        <li>
          <Link to="/posts" style={linkStyle}>Blog</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
```

**Erklärung:**
- `<Link to="...">` statt `<a href="...">` für interne Navigation
- Dadurch wird die Seite nicht neu geladen (SPA-Verhalten)

---

### Schritt 5: LoadingSpinner-Komponente erstellen

Erstelle `src/components/LoadingSpinner.jsx`:

```javascript
// src/components/LoadingSpinner.jsx

function LoadingSpinner({ message = 'Laden...' }) {
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '60px 20px',
    color: '#7f8c8d'
  };

  const spinnerStyle = {
    width: '40px',
    height: '40px',
    border: '4px solid #ecf0f1',
    borderTop: '4px solid #3498db',
    borderRadius: '50%',
    animation: 'spin 1s linear infinite'
  };

  return (
    <div style={containerStyle}>
      <div style={spinnerStyle}></div>
      <p style={{ marginTop: '16px' }}>{message}</p>
    </div>
  );
}

export default LoadingSpinner;
```

> **Hinweis:** Für die Spinner-Animation füge in `App.css` hinzu:
> ```css
> @keyframes spin {
>   0% { transform: rotate(0deg); }
>   100% { transform: rotate(360deg); }
> }
> ```

---

### Schritt 6: PostCard-Komponente erstellen

Erstelle `src/components/PostCard.jsx`:

```javascript
// src/components/PostCard.jsx
import { Link } from 'react-router-dom';

function PostCard({ post }) {
  const cardStyle = {
    padding: '20px',
    marginBottom: '16px',
    background: '#fff',
    borderRadius: '8px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    transition: 'transform 0.2s, box-shadow 0.2s'
  };

  const titleStyle = {
    margin: '0 0 12px 0',
    color: '#2c3e50',
    fontSize: '20px'
  };

  const excerptStyle = {
    color: '#7f8c8d',
    lineHeight: '1.6',
    marginBottom: '16px'
  };

  const linkStyle = {
    color: '#3498db',
    textDecoration: 'none',
    fontWeight: '500'
  };

  // Post-Body auf 100 Zeichen kürzen für Vorschau
  const excerpt = post.body.length > 100
    ? post.body.substring(0, 100) + '...'
    : post.body;

  return (
    <article style={cardStyle}>
      <h2 style={titleStyle}>{post.title}</h2>
      <p style={excerptStyle}>{excerpt}</p>
      <Link to={`/posts/${post.id}`} style={linkStyle}>
        Weiterlesen →
      </Link>
    </article>
  );
}

export default PostCard;
```

**Erklärung:**
- Die Komponente erhält einen `post` als Prop
- `Link to={`/posts/${post.id}`}` navigiert zur Detail-Seite
- Template Literal für dynamische URL

---

### Schritt 7: Home-Page erstellen

Erstelle `src/pages/Home.jsx`:

```javascript
// src/pages/Home.jsx
import { Link } from 'react-router-dom';

function Home() {
  const containerStyle = {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '60px 20px',
    textAlign: 'center'
  };

  const headingStyle = {
    fontSize: '48px',
    color: '#2c3e50',
    marginBottom: '24px'
  };

  const subtitleStyle = {
    fontSize: '20px',
    color: '#7f8c8d',
    marginBottom: '40px',
    lineHeight: '1.6'
  };

  const buttonStyle = {
    display: 'inline-block',
    padding: '16px 32px',
    background: '#3498db',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '8px',
    fontSize: '18px',
    fontWeight: '500',
    transition: 'background 0.2s'
  };

  return (
    <div style={containerStyle}>
      <h1 style={headingStyle}>Willkommen zum Blog</h1>
      <p style={subtitleStyle}>
        Entdecke interessante Artikel zu verschiedenen Themen.
        Diese App demonstriert React Router mit API-Integration.
      </p>
      <Link to="/posts" style={buttonStyle}>
        Zu den Artikeln
      </Link>
    </div>
  );
}

export default Home;
```

---

### Schritt 8: Posts-Page erstellen (mit useEffect & fetch)

Erstelle `src/pages/Posts.jsx`:

```javascript
// src/pages/Posts.jsx
import { useState, useEffect } from 'react';
import PostCard from '../components/PostCard';
import LoadingSpinner from '../components/LoadingSpinner';

function Posts() {
  // State für Posts, Loading und Error
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch-Funktion (außerhalb von useEffect, damit wir sie für Retry nutzen können)
  const fetchPosts = async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await fetch(
        'https://jsonplaceholder.typicode.com/posts?_limit=10'
      );

      if (!response.ok) {
        throw new Error(`HTTP Fehler: ${response.status}`);
      }

      const data = await response.json();
      setPosts(data);

    } catch (err) {
      console.error('Fehler beim Laden:', err);
      setError(err.message);

    } finally {
      setLoading(false);
    }
  };

  // Posts beim ersten Rendern laden
  useEffect(() => {
    fetchPosts();
  }, []); // Leeres Array = nur beim ersten Rendern ausführen

  const containerStyle = {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px 20px'
  };

  const headingStyle = {
    fontSize: '32px',
    color: '#2c3e50',
    marginBottom: '8px'
  };

  const countStyle = {
    color: '#7f8c8d',
    marginBottom: '32px'
  };

  const errorStyle = {
    padding: '20px',
    background: '#fee',
    color: '#c0392b',
    borderRadius: '8px',
    textAlign: 'center'
  };

  // Loading State
  if (loading) {
    return <LoadingSpinner message="Lade Blog-Posts..." />;
  }

  // Error State
  if (error) {
    return (
      <div style={containerStyle}>
        <div style={errorStyle}>
          <h2>Fehler beim Laden</h2>
          <p>{error}</p>
          <button
            onClick={fetchPosts}
            style={{
              marginTop: '16px',
              padding: '10px 20px',
              background: '#3498db',
              color: '#fff',
              border: 'none',
              borderRadius: '6px',
              cursor: 'pointer'
            }}
          >
            Erneut versuchen
          </button>
        </div>
      </div>
    );
  }

  // Success State
  return (
    <div style={containerStyle}>
      <h1 style={headingStyle}>Blog-Artikel</h1>
      <p style={countStyle}>{posts.length} Artikel gefunden</p>

      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  );
}

export default Posts;
```

**Erklärung:**
- **useState** für drei States: `posts`, `loading`, `error`
- **useEffect** mit leerem Dependency Array `[]` = einmalig beim Mount
- **fetchPosts außerhalb von useEffect:** So können wir die Funktion auch für den Retry-Button verwenden (SPA-konform, ohne `window.location.reload()`)
- **try/catch/finally** für sauberes Error Handling
- **Konditionales Rendering** für Loading/Error/Success States

> **Hinweis zu StrictMode (doppelte Fetches im Dev-Mode):**
> Falls du in der Browser-Konsole siehst, dass der API-Call zweimal ausgeführt wird: Das ist **normal** und kein Fehler! React's `<StrictMode>` in `main.jsx` führt Effects im Development-Modus absichtlich doppelt aus, um Probleme frühzeitig zu erkennen. Im Production-Build passiert das nicht. Du kannst das ignorieren oder `<StrictMode>` temporär entfernen, um es zu testen.

---

### Schritt 9: PostDetail-Page erstellen (mit useParams)

Erstelle `src/pages/PostDetail.jsx`:

```javascript
// src/pages/PostDetail.jsx
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import LoadingSpinner from '../components/LoadingSpinner';

function PostDetail() {
  // URL-Parameter auslesen: /posts/:postId
  const { postId } = useParams();

  const [post, setPost] = useState(null);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPostAndUser = async () => {
      try {
        setLoading(true);
        setError(null);

        // 1. Post laden
        const postResponse = await fetch(
          `https://jsonplaceholder.typicode.com/posts/${postId}`
        );

        if (!postResponse.ok) {
          throw new Error('Post nicht gefunden');
        }

        const postData = await postResponse.json();
        setPost(postData);

        // 2. User (Autor) laden
        const userResponse = await fetch(
          `https://jsonplaceholder.typicode.com/users/${postData.userId}`
        );

        if (userResponse.ok) {
          const userData = await userResponse.json();
          setUser(userData);
        }

      } catch (err) {
        console.error('Fehler:', err);
        setError(err.message);

      } finally {
        setLoading(false);
      }
    };

    fetchPostAndUser();
  }, [postId]); // Neu laden wenn sich postId ändert

  const containerStyle = {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px 20px'
  };

  const backLinkStyle = {
    color: '#3498db',
    textDecoration: 'none',
    display: 'inline-block',
    marginBottom: '24px'
  };

  const titleStyle = {
    fontSize: '36px',
    color: '#2c3e50',
    marginBottom: '16px',
    lineHeight: '1.3'
  };

  const metaStyle = {
    color: '#7f8c8d',
    marginBottom: '32px',
    paddingBottom: '16px',
    borderBottom: '1px solid #ecf0f1'
  };

  const bodyStyle = {
    fontSize: '18px',
    lineHeight: '1.8',
    color: '#34495e'
  };

  const authorLinkStyle = {
    color: '#3498db',
    textDecoration: 'none'
  };

  const errorStyle = {
    padding: '40px 20px',
    textAlign: 'center',
    color: '#c0392b'
  };

  if (loading) {
    return <LoadingSpinner message="Lade Artikel..." />;
  }

  if (error || !post) {
    return (
      <div style={containerStyle}>
        <div style={errorStyle}>
          <h2>Artikel nicht gefunden</h2>
          <p>Der Artikel mit der ID {postId} existiert nicht.</p>
          <Link to="/posts" style={backLinkStyle}>
            ← Zurück zur Übersicht
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div style={containerStyle}>
      <Link to="/posts" style={backLinkStyle}>
        ← Zurück zur Übersicht
      </Link>

      <article>
        <h1 style={titleStyle}>{post.title}</h1>

        <div style={metaStyle}>
          {user ? (
            <span>
              Von{' '}
              <Link to={`/users/${user.id}`} style={authorLinkStyle}>
                {user.name}
              </Link>
            </span>
          ) : (
            <span style={{ color: '#95a5a6' }}>Autor unbekannt</span>
          )}
        </div>

        <div style={bodyStyle}>
          <p>{post.body}</p>
        </div>
      </article>
    </div>
  );
}

export default PostDetail;
```

**Erklärung:**
- **useParams()** gibt Objekt mit URL-Parametern zurück
- **postId im Dependency Array:** useEffect läuft neu wenn sich ID ändert
- **Verkettete API-Calls:** Erst Post laden, dann User mit `userId` aus Post

---

### Schritt 10: UserProfile-Page erstellen

Erstelle `src/pages/UserProfile.jsx`:

```javascript
// src/pages/UserProfile.jsx
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import LoadingSpinner from '../components/LoadingSpinner';

function UserProfile() {
  const { userId } = useParams();

  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUserAndPosts = async () => {
      try {
        setLoading(true);
        setError(null);

        // User laden
        const userResponse = await fetch(
          `https://jsonplaceholder.typicode.com/users/${userId}`
        );

        if (!userResponse.ok) {
          throw new Error('User nicht gefunden');
        }

        const userData = await userResponse.json();
        setUser(userData);

        // Posts des Users laden
        const postsResponse = await fetch(
          `https://jsonplaceholder.typicode.com/posts?userId=${userId}`
        );

        if (postsResponse.ok) {
          const postsData = await postsResponse.json();
          setPosts(postsData);
        }

      } catch (err) {
        console.error('Fehler:', err);
        setError(err.message);

      } finally {
        setLoading(false);
      }
    };

    fetchUserAndPosts();
  }, [userId]);

  const containerStyle = {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px 20px'
  };

  const backLinkStyle = {
    color: '#3498db',
    textDecoration: 'none',
    display: 'inline-block',
    marginBottom: '24px'
  };

  const profileCardStyle = {
    background: '#fff',
    padding: '32px',
    borderRadius: '12px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
    marginBottom: '32px'
  };

  const nameStyle = {
    fontSize: '28px',
    color: '#2c3e50',
    marginBottom: '8px'
  };

  const infoStyle = {
    color: '#7f8c8d',
    marginBottom: '4px'
  };

  const sectionTitleStyle = {
    fontSize: '24px',
    color: '#2c3e50',
    marginBottom: '16px'
  };

  const postListStyle = {
    listStyle: 'none',
    padding: 0
  };

  const postItemStyle = {
    padding: '12px 0',
    borderBottom: '1px solid #ecf0f1'
  };

  const postLinkStyle = {
    color: '#3498db',
    textDecoration: 'none'
  };

  if (loading) {
    return <LoadingSpinner message="Lade Profil..." />;
  }

  if (error || !user) {
    return (
      <div style={containerStyle}>
        <h2>User nicht gefunden</h2>
        <Link to="/posts" style={backLinkStyle}>
          ← Zurück zu den Posts
        </Link>
      </div>
    );
  }

  return (
    <div style={containerStyle}>
      <Link to="/posts" style={backLinkStyle}>
        ← Zurück zu den Posts
      </Link>

      <div style={profileCardStyle}>
        <h1 style={nameStyle}>{user.name}</h1>
        <p style={infoStyle}>@{user.username}</p>
        <p style={infoStyle}>{user.email}</p>
        <p style={infoStyle}>{user.company?.name}</p>
        <p style={infoStyle}>
          {user.address?.city}, {user.address?.street}
        </p>
      </div>

      <h2 style={sectionTitleStyle}>
        Artikel von {user.name} ({posts.length})
      </h2>

      {posts.length > 0 ? (
        <ul style={postListStyle}>
          {posts.map(post => (
            <li key={post.id} style={postItemStyle}>
              <Link to={`/posts/${post.id}`} style={postLinkStyle}>
                {post.title}
              </Link>
            </li>
          ))}
        </ul>
      ) : (
        <p style={infoStyle}>Keine Artikel vorhanden.</p>
      )}
    </div>
  );
}

export default UserProfile;
```

**Erklärung:**
- Optional Chaining (`user.company?.name`) verhindert Fehler bei fehlenden Daten
- Lädt sowohl User-Daten als auch dessen Posts

---

### Schritt 11: NotFound-Page erstellen

Erstelle `src/pages/NotFound.jsx`:

```javascript
// src/pages/NotFound.jsx
import { Link } from 'react-router-dom';

function NotFound() {
  const containerStyle = {
    maxWidth: '600px',
    margin: '0 auto',
    padding: '80px 20px',
    textAlign: 'center'
  };

  const codeStyle = {
    fontSize: '120px',
    fontWeight: 'bold',
    color: '#3498db',
    margin: '0'
  };

  const titleStyle = {
    fontSize: '32px',
    color: '#2c3e50',
    marginBottom: '16px'
  };

  const textStyle = {
    color: '#7f8c8d',
    marginBottom: '32px',
    fontSize: '18px'
  };

  const linkStyle = {
    display: 'inline-block',
    padding: '14px 28px',
    background: '#3498db',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '8px',
    fontSize: '16px'
  };

  return (
    <div style={containerStyle}>
      <p style={codeStyle}>404</p>
      <h1 style={titleStyle}>Seite nicht gefunden</h1>
      <p style={textStyle}>
        Die gesuchte Seite existiert leider nicht.
        Vielleicht wurde sie verschoben oder gelöscht.
      </p>
      <Link to="/" style={linkStyle}>
        Zur Startseite
      </Link>
    </div>
  );
}

export default NotFound;
```

---

### Schritt 12: App.jsx - Alle Routen zusammenführen

Aktualisiere `src/App.jsx`:

```javascript
// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import Posts from './pages/Posts';
import PostDetail from './pages/PostDetail';
import UserProfile from './pages/UserProfile';
import NotFound from './pages/NotFound';
import './App.css';

function App() {
  const appStyle = {
    minHeight: '100vh',
    background: '#f5f6fa'
  };

  return (
    <div style={appStyle}>
      <Navigation />

      <Routes>
        {/* Statische Routen */}
        <Route path="/" element={<Home />} />

        {/* Blog Routen (können auch als Nested Routes geschrieben werden) */}
        <Route path="/posts" element={<Posts />} />
        <Route path="/posts/:postId" element={<PostDetail />} />

        {/* User Routen */}
        <Route path="/users/:userId" element={<UserProfile />} />

        {/* Catch-All Route für 404 */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

**Erklärung:**
- `Navigation` steht außerhalb von `Routes` = erscheint auf allen Seiten
- `:postId` und `:userId` sind URL-Parameter
- `path="*"` fängt alle unbekannten URLs ab

---

### Schritt 13: App.css - Basis-Styling

Aktualisiere `src/App.css`:

```css
/* === GRUNDEINSTELLUNGEN === */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.5;
  color: #2c3e50;
}

/* === SPINNER ANIMATION === */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* === LINKS === */
a {
  transition: opacity 0.2s;
}

a:hover {
  opacity: 0.8;
}

/* === BUTTONS === */
button {
  cursor: pointer;
  font-family: inherit;
}

/* === RESPONSIVE === */
@media (max-width: 600px) {
  h1 {
    font-size: 28px !important;
  }
}
```

---

### Schritt 14: Testen!

1. Starte den Dev-Server:
   ```bash
   npm run dev
   ```

2. Teste alle Routen:
   - [ ] `http://localhost:5173/` → Home-Seite
   - [ ] `http://localhost:5173/posts` → Posts-Liste
   - [ ] `http://localhost:5173/posts/1` → Post-Detail
   - [ ] `http://localhost:5173/users/1` → User-Profil
   - [ ] `http://localhost:5173/xyz` → 404-Seite

3. Teste die Navigation:
   - [ ] Links in der Navigation funktionieren
   - [ ] "Weiterlesen" Links in Post-Karten funktionieren
   - [ ] "Zurück" Links funktionieren
   - [ ] Autor-Links führen zum User-Profil

4. Teste Loading & Error States:
   - [ ] Beim Laden wird Spinner angezeigt
   - [ ] Bei ungültiger Post-ID wird Fehlermeldung gezeigt

---

## Wichtig: Deployment-Hinweis (für später)

> **Achtung beim Deployment auf statischen Hosts!**
>
> Im lokalen Dev-Server (`npm run dev`) funktioniert alles perfekt. **Aber:** Wenn du deine App auf GitHub Pages, Netlify (ohne Config) oder anderen statischen Hosts deployst, bekommst du beim **Refresh** auf `/posts/1` einen **echten 404-Fehler vom Server**.
>
> **Warum?** Der Server sucht nach einer Datei `/posts/1/index.html`, die nicht existiert. React Router funktioniert nur clientseitig – der Server weiß nichts davon.
>
> **Lösungen:**
> - **Netlify/Vercel:** SPA-Fallback konfigurieren (alle Anfragen → `index.html`)
> - **GitHub Pages:** `HashRouter` statt `BrowserRouter` verwenden, oder ein 404.html-Workaround
> - **Für dieses Assignment:** Nicht relevant, da wir nur lokal testen!

---

## Bonus: Nested Routes mit Layout (optional)

Wenn du die Blog-Routen übersichtlicher strukturieren möchtest und/oder ein gemeinsames Layout für bestimmte Routen haben willst, kannst du **Nested Routes mit Outlet** verwenden.

> **Wichtig:** Wenn eine Parent-Route ein `element` hat, muss dieses Element ein `<Outlet />` rendern – sonst werden die Child-Routen nicht angezeigt!

**Schritt 1:** Erstelle eine Layout-Komponente (z.B. `src/components/PostsLayout.jsx`):

```javascript
// src/components/PostsLayout.jsx
import { Outlet } from 'react-router-dom';

function PostsLayout() {
  // Outlet rendert die jeweilige Child-Route
  // Hier könntest du auch gemeinsame UI-Elemente hinzufügen
  return <Outlet />;
}

export default PostsLayout;
```

**Schritt 2:** Verwende das Layout in deinen Routes:

```javascript
// Alternative Struktur mit Nested Routes in App.jsx
import { Outlet } from 'react-router-dom';
import PostsLayout from './components/PostsLayout';

// In deinen Routes:
<Routes>
  <Route path="/" element={<Home />} />

  {/* Nested Routes für Posts MIT Layout */}
  <Route path="/posts" element={<PostsLayout />}>
    <Route index element={<Posts />} />
    <Route path=":postId" element={<PostDetail />} />
  </Route>

  {/* Nested Routes für Users OHNE Layout (nur Pfad-Gruppierung) */}
  <Route path="/users">
    <Route path=":userId" element={<UserProfile />} />
  </Route>

  <Route path="*" element={<NotFound />} />
</Routes>
```

**Wann brauchst du `<Outlet />`?**
- **Mit Layout-Element:** Wenn die Parent-Route ein `element` hat → `<Outlet />` im Layout nötig
- **Ohne Layout-Element:** Wenn die Parent-Route nur zur Pfad-Gruppierung dient (kein `element`) → kein Outlet nötig

**Vorteile von Nested Routes:**
- Bessere Übersicht bei vielen Routen
- Pfade sind relativ (kein `/posts/` Wiederholung)
- Gemeinsame Layouts für Routen-Gruppen möglich

---

## Checkliste: Was du verwendet hast

Wenn du Weg B abgeschlossen hast, hast du folgende Konzepte angewendet:

### React Router
- [x] `BrowserRouter` in main.jsx eingerichtet
- [x] `Routes` und `Route` für Routing-Konfiguration
- [x] Statische Routen (`/`, `/posts`)
- [x] Parametrisierte Routen (`/posts/:postId`, `/users/:userId`)
- [x] Catch-All Route (`path="*"`) für 404
- [x] `Link` Komponente für Navigation
- [x] `useParams` Hook zum Auslesen von URL-Parametern

### Hooks
- [x] `useState` für State Management (posts, loading, error)
- [x] `useEffect` für Side Effects (API-Calls beim Mount)
- [x] Dependency Array verstanden (leer vs. mit Werten)

### API & Async
- [x] `fetch` mit `async/await`
- [x] `try/catch/finally` für Error Handling
- [x] Loading State während API-Call
- [x] Error State bei Fehlern

### Komponenten & Props
- [x] Mehrere Pages (Home, Posts, PostDetail, UserProfile, NotFound)
- [x] Wiederverwendbare Komponenten (Navigation, PostCard, LoadingSpinner)
- [x] Props für Datenübergabe (post an PostCard)

### Styling
- [x] Inline Styles für Komponenten
- [x] CSS-Datei für globale Styles

---

## Bonus-Ideen (optional)

Falls du die Grundaufgabe erledigt hast und mehr machen möchtest:

1. **Suche:** Suchfeld auf der Posts-Seite zum Filtern nach Titel
2. **Pagination:** "Mehr laden" Button oder Seitenzahlen
3. **Favoriten:** Posts als Favorit markieren (mit useState)
4. **Dark Mode:** Toggle für dunkles Design
5. **Kommentare:** Kommentare unter Posts laden und anzeigen
6. **CSS Modules:** Styling in separate `.module.css` Dateien auslagern
7. **Custom Hook:** `useFetch` Hook für API-Calls erstellen
8. **Breadcrumbs:** Navigations-Pfad anzeigen (Home > Posts > Post #1)

---

## Hilfreiche Tipps

### Problem: Routes funktionieren nicht
1. Ist `BrowserRouter` in `main.jsx` um die `<App />` gewickelt?
2. Verwendest du `<Link to="...">` statt `<a href="...">`?
3. Prüfe die Browser-Konsole auf Fehlermeldungen

### Problem: useParams gibt undefined zurück
1. Stimmt der Parametername mit der Route überein?
   - Route: `path="/posts/:postId"` → useParams: `const { postId } = useParams()`
2. Ist die Komponente innerhalb von `<Routes>` gerendert?

### Problem: useEffect läuft mehrfach
1. Hast du `<StrictMode>` in main.jsx? (Normal in Dev-Mode, 2x Ausführung)
2. Prüfe dein Dependency Array - fehlen Abhängigkeiten?

### Problem: API-Daten werden nicht angezeigt
1. Console.log die Response: `console.log(data)`
2. Prüfe ob der State korrekt gesetzt wird
3. Wird der Loading-State auf `false` gesetzt?

### Problem: 404-Seite erscheint bei gültigen URLs
1. Prüfe die Schreibweise deiner Pfade (Tippfehler?)
2. **Best Practice:** Schreibe `path="*"` ans Ende deiner Routes – nicht weil React Router v6/v7 strikt von oben nach unten prüft (es verwendet Ranking-basiertes Matching), sondern weil es für Menschen lesbarer ist

---

## README.md Vorlage

Erstelle eine Datei `README.md` im Projektordner:

```markdown
# Blog-App - [Dein Name]

## Beschreibung
Eine React-App mit mehreren Seiten, die Blog-Posts von einer API lädt.
Man kann Posts durchstöbern, Detail-Ansichten öffnen und Autor-Profile sehen.

## Verwendete Techniken
- React 18 mit Vite
- React Router v6/v7 (BrowserRouter, Routes, Route, Link, useParams)
- Hooks (useState, useEffect)
- Fetch API mit async/await
- Conditional Rendering (Loading, Error, Success States)
- Komponenten-Architektur (Pages vs. Components)

## Seiten
- **Home** (`/`) - Startseite mit Willkommen
- **Posts** (`/posts`) - Liste aller Blog-Posts
- **Post Detail** (`/posts/:id`) - Einzelner Artikel
- **User Profile** (`/users/:id`) - Autor-Profil mit seinen Posts
- **404** (`/*`) - Fehlerseite für unbekannte URLs

## Weg
Ich habe Weg [A/B] gewählt.

## Was ich gelernt habe
[2-3 Sätze über deine wichtigsten Erkenntnisse]

## Schwierigkeiten
[Optional: Was war herausfordernd?]

## Starten
```bash
npm install
npm run dev
```


---

## Viel Erfolg!

Diese Aufgabe soll dir helfen, die fortgeschrittenen React-Konzepte zu festigen. Du hast jetzt gelernt, wie man eine echte Multi-Page-Anwendung mit React baut!

**Denk daran:** Das Assignment ist freiwillig. Wenn du es einreichst, bekommst du Feedback. Wenn nicht, ist das auch völlig okay!

Bei Fragen: Frag nach! Das ist keine Schwäche, sondern zeigt, dass du verstehen willst.
