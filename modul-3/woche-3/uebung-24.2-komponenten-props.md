# Komponenten & Props - Praktische Übung

## Übersicht

Willkommen zum Herzstück von React: Komponenten und Props! Hier lernst du, wie du wiederverwendbare UI-Bausteine baust und Daten zwischen Komponenten weitergibst.

In dieser Übung lernst du:
- **Komponenten** - Wiederverwendbare UI-Bausteine erstellen
- **Props** - Daten von Parent zu Child übergeben
- **Destructuring** - Props elegant auslesen
- **Default Values** - Standardwerte für Props im Parameter definieren
- **Children** - Inhalte zwischen Komponenten-Tags übergeben
- **Komponenten-Komposition** - Kleine Bausteine zu größeren kombinieren

Diese Übung baut auf "24.1 React Setup & JSX" auf – stelle sicher, dass du ein funktionierendes React-Projekt hast!

> **Hinweis zu React 19:** Diese Übung verwendet ausschließlich moderne Patterns (Default-Parameter statt `defaultProps`). Die früher üblichen `PropTypes` werden nicht mehr behandelt, da React 19 diese nicht mehr zur Laufzeit prüft. Für Typsicherheit empfehlen wir TypeScript.

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Komponenten-Grundlagen | 5 min (lesen) |
| **Teil 1** | Props verstehen | 15 min |
| **Teil 2** | Props Destructuring | 15 min |
| **Teil 3** | Default Values | 10 min |
| **Teil 4** | Children Props | 15 min |
| **Teil 5** | Mehrere Props & Objekte | 15 min |
| **Teil 6** | Komponenten-Komposition | 20 min |
| **Teil 7** | Praxis: Profilkarten-Komponente | 30 min |
| **Teil 8** | Praxis: Produktliste | 30 min |
| | **Gesamt** | **ca. 2,5 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - Komponenten-Grundlagen auffrischen
2. **Teil 1** - Props verstehen - *Das Kernkonzept*
3. **Teil 2** - Props Destructuring - *Best Practice*
4. **Teil 4** - Children Props - *Flexibilität*
5. **Teil 7** - Praxis: Profilkarten - *Alles zusammen*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast ein funktionierendes React-Projekt (aus Übung 24.1)
2. Der Dev-Server läuft (`npm run dev`)
3. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest komponenten-uebung -- --template react
cd komponenten-uebung
npm install
npm run dev
```

---

## Rückblick: Komponenten-Grundlagen

### Was ist eine Komponente?

Eine **Komponente** ist eine Funktion, die JSX zurückgibt – ein wiederverwendbarer UI-Baustein:

```javascript
// Einfache Komponente
function Greeting() {
  return <h1>Hallo Welt!</h1>;
}

// Verwendung
function App() {
  return (
    <div>
      <Greeting />
      <Greeting />
      <Greeting />
    </div>
  );
}
```

### Das Problem: Statische Komponenten

Unsere `Greeting`-Komponente zeigt immer den gleichen Text. Was, wenn wir verschiedene Namen begrüßen wollen?

```javascript
// Das wollen wir vermeiden:
function GreetingMax() {
  return <h1>Hallo Max!</h1>;
}

function GreetingAnna() {
  return <h1>Hallo Anna!</h1>;
}

// Für jeden Namen eine neue Komponente? Nein!
```

**Die Lösung: Props!**

---

## Teil 1: Props verstehen

### Was sind Props?

**Props** (Properties) sind Parameter, die du an Komponenten übergibst – wie Funktionsargumente!

```javascript
// Komponente mit Props
function Greeting(props) {
  return <h1>Hallo {props.name}!</h1>;
}

// Verwendung mit verschiedenen Werten
function App() {
  return (
    <div>
      <Greeting name="Max" />
      <Greeting name="Anna" />
      <Greeting name="Tom" />
    </div>
  );
}
```

### Wie Props funktionieren

```
┌─────────────────────────────────────────────────────────────┐
│                         PARENT                               │
│                                                              │
│   <Greeting name="Max" />                                    │
│              │                                               │
│              │  Props werden als Objekt übergeben:           │
│              │  { name: "Max" }                              │
│              ▼                                               │
│   ┌──────────────────────────────────────────────┐          │
│   │              CHILD: Greeting                  │          │
│   │                                               │          │
│   │   function Greeting(props) {                  │          │
│   │     return <h1>Hallo {props.name}!</h1>;      │          │
│   │   }                                           │          │
│   │                                               │          │
│   │   Output: <h1>Hallo Max!</h1>                 │          │
│   └──────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### Übung 1: Erste Props

> **Ziel:** Props an Komponenten übergeben
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine Komponente unterschiedliche Werte anzeigt

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/Greeting.jsx`:

> **Ordnerstruktur:** Ab jetzt legen wir alle Komponenten unter `src/components/` ab. Erstelle den Ordner falls noch nicht vorhanden.

```javascript
// src/components/Greeting.jsx

function Greeting(props) {
  // 1. Gib props in der Konsole aus, um zu sehen was ankommt
  console.log('Props:', props);

  // 2. Nutze props.name im JSX
  return (
    <div className="greeting">
      <h2>Hallo {props.name}!</h2>
      <p>Willkommen auf unserer Seite.</p>
    </div>
  );
}

export default Greeting;
```

> **Hinweis: Doppelte Konsolen-Ausgaben?**
> Falls du siehst, dass `Props: ...` zweimal in der Konsole erscheint: Das ist kein Bug! React's `StrictMode` (in `main.jsx`) rendert Komponenten im Dev-Mode absichtlich doppelt, um Probleme mit Side-Effects aufzudecken. In Production passiert das nicht.

2. Verwende die Komponente in `src/App.jsx`:

```javascript
// src/App.jsx
import './App.css'
import Greeting from './components/Greeting'

function App() {
  return (
    <div className="app">
      <h1>Props Demo</h1>

      {/* Aufgabe: Füge drei Greeting-Komponenten mit verschiedenen Namen hinzu */}
      {/* Dein Code hier */}

    </div>
  )
}

export default App
```

3. Erweitere die Greeting-Komponente um einen zweiten Prop `message`:

```javascript
// Ziel: Die Komponente soll so verwendet werden können:
<Greeting name="Max" message="Schön dich zu sehen!" />
<Greeting name="Anna" message="Willkommen zurück!" />
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Greeting.jsx:**

```javascript
function Greeting(props) {
  console.log('Props:', props);

  return (
    <div className="greeting">
      <h2>Hallo {props.name}!</h2>
      <p>{props.message}</p>
    </div>
  );
}

export default Greeting;
```

**src/App.jsx:**

```javascript
import './App.css'
import Greeting from './components/Greeting'

function App() {
  return (
    <div className="app">
      <h1>Props Demo</h1>

      <Greeting name="Max" message="Schön dich zu sehen!" />
      <Greeting name="Anna" message="Willkommen zurück!" />
      <Greeting name="Tom" message="Wie geht's dir heute?" />
    </div>
  )
}

export default App
```

</details>

### Wissensfrage 1

Was passiert, wenn du einen Prop vergisst?

```javascript
<Greeting name="Max" />  // message fehlt!
```

<details>
<summary>Antwort anzeigen</summary>

Der fehlende Prop ist `undefined`. React zeigt keinen Fehler, aber `{props.message}` rendert nichts (undefined wird nicht angezeigt).

Das kann zu unerwarteten Ergebnissen führen – deshalb lernen wir später **Default Props**!

```javascript
console.log(props); // { name: "Max" } - message ist nicht vorhanden
props.message;      // undefined
```

</details>

---

## Teil 2: Props Destructuring

### Das Problem mit props.xyz

Bei vielen Props wird der Code unübersichtlich:

```javascript
// Unübersichtlich
function UserCard(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>{props.email}</p>
      <p>{props.role}</p>
      <p>{props.department}</p>
    </div>
  );
}
```

### Die Lösung: Destructuring

**Destructuring** extrahiert Werte direkt aus dem props-Objekt:

```javascript
// Viel besser!
function UserCard({ name, email, role, department }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>{email}</p>
      <p>{role}</p>
      <p>{department}</p>
    </div>
  );
}
```

### Zwei Varianten

```javascript
// Variante 1: Destructuring im Parameter (empfohlen!)
function UserCard({ name, email }) {
  return <p>{name} - {email}</p>;
}

// Variante 2: Destructuring im Funktionskörper
function UserCard(props) {
  const { name, email } = props;
  return <p>{name} - {email}</p>;
}
```

### Übung 2: Props Destructuring

> **Ziel:** Props mit Destructuring auslesen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Destructuring sicher anwenden kannst

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/ProductCard.jsx`:

```javascript
// src/components/ProductCard.jsx

// Aufgabe: Nutze Destructuring statt props.xyz
function ProductCard(props) {
  return (
    <div className="product-card">
      <h3>{props.title}</h3>
      <p className="price">{props.price} EUR</p>
      <p className="description">{props.description}</p>
      <span className="category">{props.category}</span>
    </div>
  );
}

export default ProductCard;
```

2. Refactore die Komponente mit Destructuring im Parameter.

3. Verwende die Komponente in `App.jsx`:

```javascript
<ProductCard
  title="Laptop Pro"
  price={999.99}
  description="Leistungsstarker Laptop für Profis"
  category="Elektronik"
/>
```

4. Füge etwas CSS hinzu (in `App.css`):

```css
.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin: 10px;
  max-width: 300px;
}

.product-card h3 {
  margin: 0 0 8px 0;
}

.product-card .price {
  font-size: 24px;
  font-weight: bold;
  color: #2ecc71;
}

.product-card .description {
  color: #666;
}

.product-card .category {
  display: inline-block;
  background: #3498db;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/ProductCard.jsx:**

```javascript
function ProductCard({ title, price, description, category }) {
  return (
    <div className="product-card">
      <h3>{title}</h3>
      <p className="price">{price} EUR</p>
      <p className="description">{description}</p>
      <span className="category">{category}</span>
    </div>
  );
}

export default ProductCard;
```

**src/App.jsx:**

```javascript
import './App.css'
import ProductCard from './components/ProductCard'

function App() {
  return (
    <div className="app">
      <h1>Produkte</h1>

      <ProductCard
        title="Laptop Pro"
        price={999.99}
        description="Leistungsstarker Laptop für Profis"
        category="Elektronik"
      />

      <ProductCard
        title="Kopfhörer Max"
        price={249.99}
        description="Noise-Cancelling Kopfhörer"
        category="Audio"
      />

      <ProductCard
        title="Smartwatch"
        price={399.99}
        description="Fitness-Tracker mit GPS"
        category="Wearables"
      />
    </div>
  )
}

export default App
```

</details>

---

## Teil 3: Default Values

### Das Problem: Fehlende Props

Was passiert, wenn ein Prop nicht übergeben wird?

```javascript
<ProductCard title="Laptop" />  // price, description, category fehlen!
```

### Die Lösung: Default Values im Parameter

Mit Destructuring kannst du Standardwerte direkt im Funktionsparameter definieren:

> **Wichtig (React 19):** Die früher übliche Syntax `Component.defaultProps = {...}` ist in React 19 für Function Components entfernt worden. Verwende **immer** Default-Werte im Parameter!

```javascript
function ProductCard({
  title,
  price = 0,                           // Default: 0
  description = "Keine Beschreibung",  // Default: Text
  category = "Sonstiges"               // Default: Text
}) {
  return (
    <div className="product-card">
      <h3>{title}</h3>
      <p className="price">{price} EUR</p>
      <p className="description">{description}</p>
      <span className="category">{category}</span>
    </div>
  );
}
```

### Übung 3: Default Values setzen

> **Ziel:** Standardwerte für Props definieren
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Deine Komponente auch ohne alle Props funktioniert

**Aufgabe:**

1. Erstelle eine `Button`-Komponente mit Default Values:

```javascript
// src/components/Button.jsx

function Button({
  text,       // Pflicht-Prop
  variant,    // Default: "primary"
  size,       // Default: "medium"
  disabled    // Default: false
}) {
  // Aufgabe: Füge Default Values hinzu!

  // Die Klassen sollen so aufgebaut werden:
  // "btn btn-primary btn-medium" oder "btn btn-secondary btn-small"
  const className = `btn btn-${variant} btn-${size}`;

  return (
    <button className={className} disabled={disabled}>
      {text}
    </button>
  );
}

export default Button;
```

2. Teste mit verschiedenen Kombinationen:

```javascript
<Button text="Klick mich" />
<Button text="Speichern" variant="success" />
<Button text="Abbrechen" variant="secondary" size="small" />
<Button text="Löschen" variant="danger" disabled={true} />
```

3. Füge CSS hinzu:

```css
.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.btn-primary { background: #3498db; color: white; }
.btn-secondary { background: #95a5a6; color: white; }
.btn-success { background: #2ecc71; color: white; }
.btn-danger { background: #e74c3c; color: white; }

.btn-small { padding: 6px 12px; font-size: 14px; }
.btn-medium { padding: 10px 20px; font-size: 16px; }
.btn-large { padding: 14px 28px; font-size: 18px; }

.btn:disabled { opacity: 0.5; cursor: not-allowed; }
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Button.jsx:**

```javascript
function Button({
  text,
  variant = "primary",
  size = "medium",
  disabled = false
}) {
  const className = `btn btn-${variant} btn-${size}`;

  return (
    <button className={className} disabled={disabled}>
      {text}
    </button>
  );
}

export default Button;
```

**src/App.jsx:**

```javascript
import './App.css'
import Button from './components/Button'

function App() {
  return (
    <div className="app">
      <h1>Button Demo</h1>

      <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
        <Button text="Klick mich" />
        <Button text="Speichern" variant="success" />
        <Button text="Abbrechen" variant="secondary" size="small" />
        <Button text="Löschen" variant="danger" disabled={true} />
        <Button text="Großer Button" size="large" />
      </div>
    </div>
  )
}

export default App
```

</details>

---

## Teil 4: Children Props

### Das Problem: Inhalte zwischen Tags

Manchmal möchtest du Inhalte **zwischen** den Komponenten-Tags übergeben:

```javascript
// Das geht nicht automatisch:
<Card>
  <h2>Titel</h2>
  <p>Inhalt hier...</p>
</Card>
```

### Die Lösung: children Prop

React übergibt automatisch alles zwischen den Tags als `children` Prop:

```javascript
function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

// Verwendung
<Card>
  <h2>Mein Titel</h2>
  <p>Mein Inhalt</p>
</Card>
```

### Visualisierung

```
<Card>                          function Card({ children }) {
  <h2>Titel</h2>      ──────►     return (
  <p>Text</p>                       <div className="card">
</Card>                               {children}  // ← h2 + p
                                    </div>
                                  );
                                }
```

### Übung 4: Children Props

> **Ziel:** Flexible Komponenten mit children erstellen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du beliebige Inhalte in eine Wrapper-Komponente übergeben kannst

**Aufgabe:**

1. Erstelle eine `Card`-Komponente:

```javascript
// src/components/Card.jsx

function Card({ title, children }) {
  // Aufgabe:
  // - Zeige den title im Header
  // - Rendere children im Body

  return (
    <div className="card">
      {/* Header mit Titel */}

      {/* Body mit children */}

    </div>
  );
}

export default Card;
```

2. Erstelle eine `Alert`-Komponente:

```javascript
// src/components/Alert.jsx

function Alert({ type = "info", children }) {
  // type kann sein: "info", "success", "warning", "error"
  // Default ist bereits gesetzt: "info"

  // Aufgabe: Erstelle eine Alert-Box mit dem übergebenen Inhalt

  return (
    <div className={`alert alert-${type}`}>
      {children}
    </div>
  );
}

export default Alert;
```

3. Verwende beide in `App.jsx`:

```javascript
<Card title="Willkommen">
  <p>Dies ist der Inhalt der Card.</p>
  <Button text="Mehr erfahren" />
</Card>

<Alert type="success">
  Deine Änderungen wurden gespeichert!
</Alert>

<Alert type="error">
  <strong>Fehler:</strong> Bitte fülle alle Felder aus.
</Alert>
```

4. Füge CSS hinzu:

```css
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 20px 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card-header {
  background: #f8f9fa;
  padding: 16px;
  border-bottom: 1px solid #ddd;
  font-weight: bold;
}

.card-body {
  padding: 16px;
}

.alert {
  padding: 16px;
  border-radius: 4px;
  margin: 10px 0;
}

.alert-info { background: #d1ecf1; color: #0c5460; }
.alert-success { background: #d4edda; color: #155724; }
.alert-warning { background: #fff3cd; color: #856404; }
.alert-error { background: #f8d7da; color: #721c24; }
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Card.jsx:**

```javascript
function Card({ title, children }) {
  return (
    <div className="card">
      <div className="card-header">
        {title}
      </div>
      <div className="card-body">
        {children}
      </div>
    </div>
  );
}

export default Card;
```

**src/components/Alert.jsx:**

```javascript
function Alert({ type = "info", children }) {
  return (
    <div className={`alert alert-${type}`}>
      {children}
    </div>
  );
}

export default Alert;
```

**src/App.jsx:**

```javascript
import './App.css'
import Card from './components/Card'
import Alert from './components/Alert'
import Button from './components/Button'

function App() {
  return (
    <div className="app">
      <h1>Children Props Demo</h1>

      <Card title="Willkommen">
        <p>Dies ist der Inhalt der Card.</p>
        <Button text="Mehr erfahren" />
      </Card>

      <Card title="Benutzer-Info">
        <p><strong>Name:</strong> Max Mustermann</p>
        <p><strong>Email:</strong> max@example.com</p>
      </Card>

      <Alert type="success">
        Deine Änderungen wurden gespeichert!
      </Alert>

      <Alert type="error">
        <strong>Fehler:</strong> Bitte fülle alle Felder aus.
      </Alert>

      <Alert type="warning">
        Achtung: Diese Aktion kann nicht rückgängig gemacht werden.
      </Alert>
    </div>
  )
}

export default App
```

</details>

### Wissensfrage 2

Was ist der Unterschied zwischen diesen beiden Verwendungen?

```javascript
// Variante A: Self-closing
<Card title="Test" />

// Variante B: Mit children
<Card title="Test">
  <p>Inhalt</p>
</Card>
```

<details>
<summary>Antwort anzeigen</summary>

**Variante A:** `children` ist `undefined` – es gibt keinen Inhalt zwischen den Tags.

**Variante B:** `children` enthält `<p>Inhalt</p>` – der JSX-Inhalt zwischen den Tags.

In deiner Komponente kannst du prüfen, ob children vorhanden ist:

```javascript
function Card({ title, children }) {
  return (
    <div className="card">
      <div className="card-header">{title}</div>
      {children && (
        <div className="card-body">{children}</div>
      )}
    </div>
  );
}
```

</details>

---

## Teil 5: Mehrere Props & Objekte

### Props als Objekt übergeben

Bei vielen zusammengehörigen Daten ist es oft sinnvoller, ein Objekt zu übergeben:

```javascript
// Statt vieler einzelner Props:
<UserCard
  name="Max"
  email="max@example.com"
  role="Admin"
  avatar="..."
/>

// Ein Objekt übergeben:
const user = {
  name: "Max",
  email: "max@example.com",
  role: "Admin",
  avatar: "..."
};

<UserCard user={user} />
```

### Spread Operator für Props

Mit dem Spread Operator kannst du alle Properties eines Objekts als Props übergeben:

```javascript
const buttonProps = {
  text: "Klick mich",
  variant: "primary",
  size: "large"
};

// Statt:
<Button text={buttonProps.text} variant={buttonProps.variant} size={buttonProps.size} />

// Mit Spread:
<Button {...buttonProps} />
```

### Übung 5: Objekte als Props

> **Ziel:** Komplexe Daten als Props übergeben
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Objekte und Arrays als Props nutzen kannst

**Aufgabe:**

1. Erstelle eine `UserProfile`-Komponente, die ein User-Objekt empfängt:

```javascript
// src/components/UserProfile.jsx

function UserProfile({ user }) {
  // user hat die Struktur:
  // {
  //   name: "Max Mustermann",
  //   email: "max@example.com",
  //   role: "Developer",
  //   skills: ["React", "JavaScript", "CSS"],
  //   isOnline: true
  // }

  // Aufgabe: Rendere alle User-Informationen
  // - Name als Überschrift
  // - Email und Role
  // - Skills als Liste
  // - Online-Status als grüner/roter Punkt

  return (
    <div className="user-profile">
      {/* Dein Code hier */}
    </div>
  );
}

export default UserProfile;
```

2. Verwende in `App.jsx`:

```javascript
import UserProfile from './components/UserProfile'

function App() {
  const users = [
    {
      id: 1,
      name: "Max Mustermann",
      email: "max@example.com",
      role: "Frontend Developer",
      skills: ["React", "JavaScript", "CSS"],
      isOnline: true
    },
    {
      id: 2,
      name: "Anna Schmidt",
      email: "anna@example.com",
      role: "Backend Developer",
      skills: ["Python", "FastAPI", "PostgreSQL"],
      isOnline: false
    },
    {
      id: 3,
      name: "Tom Weber",
      email: "tom@example.com",
      role: "Full Stack Developer",
      skills: ["React", "Node.js", "MongoDB"],
      isOnline: true
    }
  ];

  return (
    <div className="app">
      <h1>Team</h1>
      {users.map(user => (
        <UserProfile key={user.id} user={user} />
      ))}
    </div>
  );
}
```

> **Hinweis zum `key` Prop:** Bei Listen braucht React einen eindeutigen `key` für jedes Element, um effizient updaten zu können. Nutze immer eine stabile ID (hier `user.id`). Index als Key (`key={index}`) nur bei statischen Listen verwenden, die sich nie ändern!
```

3. Füge CSS hinzu:

```css
.user-profile {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 15px 0;
  display: flex;
  gap: 20px;
}

.user-profile .status {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
  margin-right: 8px;
}

.user-profile .status.online { background: #2ecc71; }
.user-profile .status.offline { background: #e74c3c; }

.user-profile .skills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.user-profile .skill-tag {
  background: #3498db;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/UserProfile.jsx:**

```javascript
function UserProfile({ user }) {
  const { name, email, role, skills, isOnline } = user;

  return (
    <div className="user-profile">
      <div className="user-info">
        <h3>
          <span className={`status ${isOnline ? 'online' : 'offline'}`}></span>
          {name}
        </h3>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Role:</strong> {role}</p>

        <div className="skills">
          {/* Index als Key ist hier okay, da Skills sich nicht ändern */}
          {skills.map((skill, index) => (
            <span key={index} className="skill-tag">{skill}</span>
          ))}
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
```

</details>

---

## Teil 6: Komponenten-Komposition

### Kleine Komponenten kombinieren

In React baust du komplexe UIs aus kleinen, wiederverwendbaren Komponenten:

```
┌──────────────────────────────────────────────────┐
│                      App                          │
│  ┌──────────────────────────────────────────┐    │
│  │               ProductList                 │    │
│  │  ┌────────────┐  ┌────────────┐          │    │
│  │  │ ProductCard │  │ ProductCard │   ...   │    │
│  │  │  ┌──────┐  │  │  ┌──────┐  │          │    │
│  │  │  │Badge │  │  │  │Badge │  │          │    │
│  │  │  └──────┘  │  │  └──────┘  │          │    │
│  │  │  ┌──────┐  │  │  ┌──────┐  │          │    │
│  │  │  │Button│  │  │  │Button│  │          │    │
│  │  │  └──────┘  │  │  └──────┘  │          │    │
│  │  └────────────┘  └────────────┘          │    │
│  └──────────────────────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

### Übung 6: Komponenten kombinieren

> **Ziel:** Mehrere kleine Komponenten zu einer größeren zusammensetzen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du eine Komponenten-Hierarchie gebaut hast

**Aufgabe:**

Erstelle folgende Komponenten-Struktur:

1. `Badge` - Ein kleines Label für Kategorien/Status
2. `Avatar` - Ein Bild mit Fallback auf Initialen
3. `ContactCard` - Kombiniert Avatar, Name, Badge und Kontaktinfos

**Badge.jsx:**

```javascript
// src/components/Badge.jsx

function Badge({ text, color = "blue" }) {
  // Farben: blue, green, red, yellow, gray
  return (
    <span className={`badge badge-${color}`}>
      {text}
    </span>
  );
}

export default Badge;
```

**Avatar.jsx:**

```javascript
// src/components/Avatar.jsx

function Avatar({ name, imageUrl, size = "medium" }) {
  // Wenn kein Bild vorhanden, zeige Initialen
  // size: "small", "medium", "large"

  // Aufgabe: Erstelle die Avatar-Komponente
  // - Wenn imageUrl vorhanden: zeige Bild
  // - Sonst: zeige Initialen (erste Buchstaben der Wörter im Namen)

  // Robuste Initialen-Berechnung
  const getInitials = (name = "") => {
    return name
      .trim()
      .split(/\s+/)           // Split bei einem oder mehr Leerzeichen
      .filter(Boolean)         // Leere Strings entfernen
      .map(word => word[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);           // Max 2 Zeichen
  };

  return (
    <div className={`avatar avatar-${size}`}>
      {/* Dein Code hier */}
    </div>
  );
}

export default Avatar;
```

**ContactCard.jsx:**

```javascript
// src/components/ContactCard.jsx
import Avatar from './Avatar';
import Badge from './Badge';

function ContactCard({ contact }) {
  // contact hat die Struktur:
  // {
  //   name: "Max Mustermann",
  //   email: "max@example.com",
  //   phone: "+49 123 456789",
  //   department: "Engineering",
  //   status: "Verfügbar" | "Beschäftigt" | "Abwesend",
  //   imageUrl: "..." (optional)
  // }

  // Aufgabe: Kombiniere Avatar, Badge und Kontaktinfos

  const statusColors = {
    "Verfügbar": "green",
    "Beschäftigt": "yellow",
    "Abwesend": "red"
  };

  return (
    <div className="contact-card">
      {/* Dein Code hier */}
    </div>
  );
}

export default ContactCard;
```

**CSS:**

```css
.badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.badge-blue { background: #3498db; color: white; }
.badge-green { background: #2ecc71; color: white; }
.badge-red { background: #e74c3c; color: white; }
.badge-yellow { background: #f1c40f; color: #333; }
.badge-gray { background: #95a5a6; color: white; }

.avatar {
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #3498db;
  color: white;
  font-weight: bold;
}

.avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.avatar-small { width: 32px; height: 32px; font-size: 12px; }
.avatar-medium { width: 48px; height: 48px; font-size: 16px; }
.avatar-large { width: 64px; height: 64px; font-size: 20px; }

.contact-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 10px 0;
}

.contact-card .contact-info h3 {
  margin: 0 0 4px 0;
}

.contact-card .contact-info p {
  margin: 2px 0;
  color: #666;
  font-size: 14px;
}

.contact-card .contact-meta {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Avatar.jsx:**

```javascript
function Avatar({ name, imageUrl, size = "medium" }) {
  // Robuste Initialen-Berechnung
  const getInitials = (name = "") => {
    return name
      .trim()
      .split(/\s+/)           // Split bei einem oder mehr Leerzeichen
      .filter(Boolean)         // Leere Strings entfernen
      .map(word => word[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);           // Max 2 Zeichen
  };

  return (
    <div className={`avatar avatar-${size}`}>
      {imageUrl ? (
        <img src={imageUrl} alt={name} />
      ) : (
        getInitials(name)
      )}
    </div>
  );
}

export default Avatar;
```

**src/components/ContactCard.jsx:**

```javascript
import Avatar from './Avatar';
import Badge from './Badge';

function ContactCard({ contact }) {
  const { name, email, phone, department, status, imageUrl } = contact;

  const statusColors = {
    "Verfügbar": "green",
    "Beschäftigt": "yellow",
    "Abwesend": "red"
  };

  return (
    <div className="contact-card">
      <Avatar name={name} imageUrl={imageUrl} size="large" />

      <div className="contact-info">
        <h3>{name}</h3>
        <p>{email}</p>
        <p>{phone}</p>

        <div className="contact-meta">
          <Badge text={department} color="blue" />
          <Badge text={status} color={statusColors[status] || "gray"} />
        </div>
      </div>
    </div>
  );
}

export default ContactCard;
```

**src/App.jsx:**

```javascript
import './App.css'
import ContactCard from './components/ContactCard'

function App() {
  const contacts = [
    {
      id: 1,
      name: "Max Mustermann",
      email: "max@example.com",
      phone: "+49 123 456789",
      department: "Engineering",
      status: "Verfügbar"
    },
    {
      id: 2,
      name: "Anna Schmidt",
      email: "anna@example.com",
      phone: "+49 987 654321",
      department: "Design",
      status: "Beschäftigt"
    },
    {
      id: 3,
      name: "Tom Weber",
      email: "tom@example.com",
      phone: "+49 555 123456",
      department: "Marketing",
      status: "Abwesend"
    }
  ];

  return (
    <div className="app">
      <h1>Kontakte</h1>
      {contacts.map(contact => (
        <ContactCard key={contact.id} contact={contact} />
      ))}
    </div>
  )
}

export default App
```

</details>

---

## Teil 7: Praxis - Profilkarten-Komponente

Zeit, alles zusammen anzuwenden!

> **Ziel:** Eine vollständige Profilkarten-Komponente mit allen gelernten Konzepten
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Die Profilkarte alle Features zeigt

### Aufgabe: ProfileCard

Erstelle eine wiederverwendbare `ProfileCard`-Komponente mit:

1. Avatar mit Fallback auf Initialen
2. Name und Titel/Position
3. Kontaktinfos (Email, Telefon)
4. Skills als Tags
5. Social Media Links
6. Online-Status
7. Action-Buttons (children)

**Anforderungen:**

```javascript
// So soll die Komponente verwendet werden:
<ProfileCard
  user={{
    name: "Max Mustermann",
    title: "Senior Frontend Developer",
    email: "max@example.com",
    phone: "+49 123 456789",
    avatar: "https://...",  // optional
    skills: ["React", "TypeScript", "Node.js"],
    social: {
      github: "maxmuster",
      linkedin: "maxmustermann",
      twitter: "maxm"
    },
    isOnline: true
  }}
>
  <Button text="Nachricht senden" />
  <Button text="Profil ansehen" variant="secondary" />
</ProfileCard>
```

**Dateistruktur:**

```
src/
├── components/
│   ├── ProfileCard.jsx
│   ├── Avatar.jsx
│   ├── Badge.jsx
│   ├── Button.jsx
│   └── SocialLinks.jsx
├── App.jsx
└── App.css
```

**Hinweise:**

- Nutze Destructuring für Props
- Setze sinnvolle Default-Werte
- Verwende children für die Action-Buttons
- Erstelle kleine, wiederverwendbare Sub-Komponenten

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Avatar.jsx:**

```javascript
function Avatar({ name, imageUrl, size = "medium", isOnline }) {
  // Robuste Initialen-Berechnung
  const getInitials = (name = "") => {
    return name
      .trim()
      .split(/\s+/)           // Split bei einem oder mehr Leerzeichen
      .filter(Boolean)         // Leere Strings entfernen
      .map(word => word[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);           // Max 2 Zeichen
  };

  return (
    <div className={`avatar avatar-${size}`}>
      {imageUrl ? (
        <img src={imageUrl} alt={name} />
      ) : (
        <span className="initials">{getInitials(name)}</span>
      )}
      {isOnline !== undefined && (
        <span className={`status-dot ${isOnline ? 'online' : 'offline'}`} />
      )}
    </div>
  );
}

export default Avatar;
```

**src/components/SocialLinks.jsx:**

```javascript
function SocialLinks({ social = {} }) {
  const icons = {
    github: 'GH',
    linkedin: 'LI',
    twitter: 'TW'
  };

  const urls = {
    github: (username) => `https://github.com/${username}`,
    linkedin: (username) => `https://linkedin.com/in/${username}`,
    twitter: (username) => `https://twitter.com/${username}`
  };

  // Nur erlaubte Plattformen rendern (verhindert Runtime-Fehler bei unbekannten Keys)
  const allowedPlatforms = ['github', 'linkedin', 'twitter'];

  return (
    <div className="social-links">
      {Object.entries(social)
        .filter(([platform, username]) => allowedPlatforms.includes(platform) && username)
        .map(([platform, username]) => (
          <a
            key={platform}
            href={urls[platform](username)}
            target="_blank"
            rel="noopener noreferrer"
            className={`social-link social-${platform}`}
            title={`${platform}: @${username}`}
          >
            {icons[platform]}
          </a>
        ))}
    </div>
  );
}

export default SocialLinks;
```

**src/components/ProfileCard.jsx:**

```javascript
import Avatar from './Avatar';
import Badge from './Badge';
import SocialLinks from './SocialLinks';

function ProfileCard({ user, children }) {
  const {
    name,
    title,
    email,
    phone,
    avatar,
    skills = [],
    social = {},
    isOnline = false
  } = user;

  return (
    <div className="profile-card">
      <div className="profile-header">
        <Avatar
          name={name}
          imageUrl={avatar}
          size="large"
          isOnline={isOnline}
        />
        <div className="profile-info">
          <h2>{name}</h2>
          <p className="title">{title}</p>
        </div>
      </div>

      <div className="profile-contact">
        <p><span className="label">Email:</span> {email}</p>
        {phone && <p><span className="label">Tel:</span> {phone}</p>}
      </div>

      {skills.length > 0 && (
        <div className="profile-skills">
          {skills.map((skill, index) => (
            <Badge key={index} text={skill} color="blue" />
          ))}
        </div>
      )}

      {Object.keys(social).length > 0 && (
        <SocialLinks social={social} />
      )}

      {children && (
        <div className="profile-actions">
          {children}
        </div>
      )}
    </div>
  );
}

export default ProfileCard;
```

> **Hinweis zur Typsicherheit:** Für echte Projekte empfehlen wir TypeScript statt PropTypes. TypeScript fängt Typfehler bereits beim Schreiben ab, nicht erst zur Laufzeit – und ist der moderne Standard in React-Projekten.

**CSS für ProfileCard:**

```css
.profile-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 24px;
  max-width: 400px;
  background: white;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.profile-info h2 {
  margin: 0 0 4px 0;
}

.profile-info .title {
  color: #666;
  margin: 0;
}

.profile-contact {
  margin-bottom: 16px;
}

.profile-contact p {
  margin: 4px 0;
}

.profile-contact .label {
  color: #888;
  font-size: 14px;
}

.profile-skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.social-links {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}

.social-link {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.social-github { background: #333; }
.social-linkedin { background: #0077b5; }
.social-twitter { background: #1da1f2; }

.profile-actions {
  display: flex;
  gap: 8px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #eee;
}

.avatar {
  position: relative;
}

.status-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2px solid white;
}

.status-dot.online { background: #2ecc71; }
.status-dot.offline { background: #95a5a6; }
```

</details>

---

## Teil 8: Praxis - Produktliste

Eine weitere Übung zur Festigung!

> **Ziel:** Eine komplette Produktlisten-Anwendung bauen
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Die Produktliste alle Produkte anzeigt

### Aufgabe: Produkt-Katalog

Erstelle eine Produktlisten-Anwendung mit folgenden Komponenten:

1. `ProductCard` - Einzelnes Produkt anzeigen
2. `ProductList` - Liste aller Produkte
3. `ProductBadge` - Für Sale, New, etc.

**Anforderungen:**

```javascript
// Produkt-Daten
const products = [
  {
    id: 1,
    name: "Wireless Kopfhörer",
    price: 149.99,
    originalPrice: 199.99,  // optional: für Sale
    image: "https://via.placeholder.com/200",
    category: "Audio",
    rating: 4.5,
    reviews: 128,
    badges: ["sale", "bestseller"],
    inStock: true
  },
  // ... mehr Produkte
];

// Verwendung
<ProductList products={products} />
```

**Features:**

- Sale-Badge wenn `originalPrice` vorhanden und höher als `price`
- Rabatt-Prozent berechnen und anzeigen
- Sterne-Rating (vereinfacht: z.B. "4.5 / 5")
- "Ausverkauft" wenn `inStock: false`
- Kategorie-Badge

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/ProductBadge.jsx:**

```javascript
function ProductBadge({ type }) {
  const badges = {
    sale: { text: "SALE", color: "red" },
    new: { text: "NEU", color: "green" },
    bestseller: { text: "BESTSELLER", color: "yellow" }
  };

  const badge = badges[type];
  if (!badge) return null;

  return (
    <span className={`product-badge badge-${badge.color}`}>
      {badge.text}
    </span>
  );
}

export default ProductBadge;
```

**src/components/ProductCard.jsx:**

```javascript
import ProductBadge from './ProductBadge';

function ProductCard({ product }) {
  const {
    name,
    price,
    originalPrice,
    image,
    category,
    rating,
    reviews,
    badges = [],
    inStock
  } = product;

  // Robuste Rabattberechnung: Nur wenn originalPrice > price
  const hasDiscount = typeof originalPrice === 'number' && originalPrice > price;
  const discount = hasDiscount
    ? Math.round((1 - price / originalPrice) * 100)
    : 0;

  // Rating auf 0-5 begrenzen für die Sterne-Anzeige
  const clampedRating = Math.max(0, Math.min(5, rating));
  const fullStars = Math.floor(clampedRating);
  const emptyStars = 5 - fullStars;

  return (
    <div className={`product-card ${!inStock ? 'out-of-stock' : ''}`}>
      <div className="product-image">
        <img src={image} alt={name} />
        <div className="product-badges">
          {/* Index als Key okay, da badges statisch sind */}
          {badges.map((badge, index) => (
            <ProductBadge key={index} type={badge} />
          ))}
        </div>
      </div>

      <div className="product-info">
        <span className="product-category">{category}</span>
        <h3 className="product-name">{name}</h3>

        <div className="product-rating">
          <span className="stars">{'★'.repeat(fullStars)}{'☆'.repeat(emptyStars)}</span>
          <span className="rating-text">{rating} ({reviews} Bewertungen)</span>
        </div>

        <div className="product-price">
          <span className="current-price">{price.toFixed(2)} EUR</span>
          {hasDiscount && (
            <>
              <span className="original-price">{originalPrice.toFixed(2)} EUR</span>
              <span className="discount">-{discount}%</span>
            </>
          )}
        </div>

        {!inStock && (
          <span className="out-of-stock-label">Ausverkauft</span>
        )}
      </div>
    </div>
  );
}

export default ProductCard;
```

**src/components/ProductList.jsx:**

```javascript
import ProductCard from './ProductCard';

function ProductList({ products = [], title = "Produkte" }) {
  if (products.length === 0) {
    return (
      <div className="product-list-empty">
        <p>Keine Produkte gefunden.</p>
      </div>
    );
  }

  return (
    <div className="product-list">
      <h2>{title}</h2>
      <div className="product-grid">
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default ProductList;
```

**CSS:**

```css
.product-list h2 {
  margin-bottom: 20px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  background: white;
  transition: transform 0.2s, box-shadow 0.2s;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.product-card.out-of-stock {
  opacity: 0.7;
}

.product-image {
  position: relative;
  height: 200px;
  background: #f5f5f5;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-badges {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.product-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: bold;
}

.badge-red { background: #e74c3c; color: white; }
.badge-green { background: #2ecc71; color: white; }
.badge-yellow { background: #f1c40f; color: #333; }

.product-info {
  padding: 16px;
}

.product-category {
  font-size: 12px;
  color: #888;
  text-transform: uppercase;
}

.product-name {
  margin: 8px 0;
  font-size: 18px;
}

.product-rating {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.stars {
  color: #f1c40f;
}

.rating-text {
  font-size: 12px;
  color: #666;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 8px;
}

.current-price {
  font-size: 20px;
  font-weight: bold;
  color: #2ecc71;
}

.original-price {
  font-size: 14px;
  color: #999;
  text-decoration: line-through;
}

.discount {
  background: #e74c3c;
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.out-of-stock-label {
  display: block;
  margin-top: 8px;
  color: #e74c3c;
  font-weight: bold;
}
```

**src/App.jsx:**

```javascript
import './App.css'
import ProductList from './components/ProductList'

function App() {
  const products = [
    {
      id: 1,
      name: "Wireless Kopfhörer Pro",
      price: 149.99,
      originalPrice: 199.99,
      image: "https://via.placeholder.com/200",
      category: "Audio",
      rating: 4.5,
      reviews: 128,
      badges: ["sale", "bestseller"],
      inStock: true
    },
    {
      id: 2,
      name: "Smart Watch Series 5",
      price: 299.99,
      image: "https://via.placeholder.com/200",
      category: "Wearables",
      rating: 4.8,
      reviews: 256,
      badges: ["new"],
      inStock: true
    },
    {
      id: 3,
      name: "Bluetooth Lautsprecher",
      price: 79.99,
      originalPrice: 99.99,
      image: "https://via.placeholder.com/200",
      category: "Audio",
      rating: 4.2,
      reviews: 89,
      badges: ["sale"],
      inStock: false
    },
    {
      id: 4,
      name: "Laptop Stand Pro",
      price: 49.99,
      image: "https://via.placeholder.com/200",
      category: "Zubehör",
      rating: 4.6,
      reviews: 312,
      badges: [],
      inStock: true
    }
  ];

  return (
    <div className="app">
      <h1>Shop</h1>
      <ProductList products={products} title="Unsere Produkte" />
    </div>
  )
}

export default App
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Props** | Daten an Komponenten übergeben | `<Card title="Hallo" />` |
| **Destructuring** | Props elegant auslesen | `function Card({ title })` |
| **Default Values** | Standardwerte im Parameter | `{ title = "Standard" }` |
| **Children** | Inhalte zwischen Tags | `<Card>{children}</Card>` |
| **Objekte als Props** | Komplexe Daten übergeben | `<User user={userData} />` |
| **Komposition** | Kleine Komponenten kombinieren | `Avatar` + `Badge` = `ProfileCard` |

### Props auf einen Blick

```javascript
// Props empfangen mit Destructuring und Default Values
function MyComponent({
  name,                    // Pflicht-Prop
  age = 0,                 // Optional mit Default
  isActive = false,        // Optional mit Default
  children                 // Für Inhalte zwischen Tags
}) {
  return (
    <div>
      <h1>{name}</h1>
      <p>Alter: {age}</p>
      {children}
    </div>
  );
}

export default MyComponent;
```

> **Tipp für Fortgeschrittene:** Für Typsicherheit in größeren Projekten empfehlen wir TypeScript statt PropTypes. TypeScript fängt Fehler bereits beim Schreiben ab und ist der moderne Standard.

### Wichtige Regeln

1. **Props sind read-only** – Ändere sie niemals direkt!
2. **Datenfluss: Nur von oben nach unten** (Parent → Child)
3. **Nutze Destructuring** – Macht den Code lesbarer
4. **Setze Default-Werte im Parameter** – Verhindert undefined-Fehler
5. **Nutze stabile IDs als `key`** – Nicht den Index bei dynamischen Listen

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du verstehst, was Props sind und wozu sie dienen
- [ ] Du kannst Props mit Destructuring auslesen
- [ ] Du kannst Default-Werte im Parameter setzen
- [ ] Du verstehst den children Prop für flexible Komponenten
- [ ] Du kannst Objekte und Arrays als Props übergeben
- [ ] Du verstehst, wann du Index vs. ID als `key` nutzen solltest
- [ ] Du kannst kleine Komponenten zu größeren kombinieren

**Alles abgehakt?** Du bist bereit für State & Events!
