# useState & Controlled Inputs - Praktische Übung

## Übersicht

Willkommen zu einem der wichtigsten Konzepte in React: State! Hier lernst du, wie du deinen Komponenten ein "Gedächtnis" gibst und interaktive Formulare erstellst.

In dieser Übung lernst du:
- **Events** - Auf Benutzerinteraktionen reagieren
- **Forms** - Formulare in React mit `e.preventDefault()` nutzen
- **useState** - State in Komponenten verwalten
- **Controlled Inputs** - Formularfelder mit State verbinden
- **Stateful vs Stateless** - Komponenten-Design verstehen
- **Lokalität von State** - Unabhängige Komponenten-Instanzen

Diese Übung baut auf "24.2 Komponenten & Props" auf – stelle sicher, dass du Props und Komponenten verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Von Props zu State | 5 min (lesen) |
| **Teil 1** | Events in React | 15 min |
| **Teil 2** | Forms & preventDefault | 15 min |
| **Teil 3** | useState verstehen | 20 min |
| **Teil 4** | Controlled Inputs | 20 min |
| **Teil 5** | Mehrere State-Variablen | 15 min |
| **Teil 6** | Stateful vs Stateless | 15 min |
| **Teil 7** | Praxis: Login-Formular | 30 min |
| **Teil 8** | Praxis: Todo-Eingabe | 30 min |
| | **Gesamt** | **ca. 2,5 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - Von Props zu State
2. **Teil 1** - Events in React - *Grundlage für Interaktivität*
3. **Teil 3** - useState verstehen - *Das Kernkonzept*
4. **Teil 4** - Controlled Inputs - *Formulare mit State*
5. **Teil 7** - Praxis: Login-Formular - *Alles zusammen*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast ein funktionierendes React-Projekt (aus Übung 24.1 oder 24.2)
2. Der Dev-Server läuft (`npm run dev`)
3. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest state-uebung -- --template react
cd state-uebung
npm install
npm run dev
```

> **Tipp für diese Übung:** Du wirst mehrere Komponenten bauen (DatePrinter, SimpleForm, Counter, etc.). Um Verwirrung zu vermeiden: **Rendere immer nur eine Übungskomponente gleichzeitig in `App.jsx`**. Kommentiere die anderen aus, während du an einer neuen arbeitest.

---

## Rückblick: Von Props zu State

### Das Problem mit Props

Props sind **read-only** – sie können nur von außen gesetzt werden:

```javascript
function Greeting({ name }) {
  // name kann hier NICHT verändert werden!
  return <h1>Hallo {name}!</h1>;
}
```

### Was wenn sich etwas ändern soll?

Stell dir einen Counter vor:

```javascript
// Das funktioniert NICHT wie erwartet!
function Counter() {
  let count = 0;

  function increment() {
    count = count + 1;  // Wert ändert sich...
    console.log(count); // ...aber React merkt es nicht!
  }

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+1</button>
    </div>
  );
}
```

**Das Problem:** React weiß nicht, dass sich `count` geändert hat und rendert die Komponente nicht neu!

**Die Lösung: State!** Mit `useState` kann React Änderungen tracken und die UI automatisch aktualisieren.

```
┌─────────────────────────────────────────────────────────────┐
│                    PROPS vs STATE                           │
│                                                             │
│   Props                         State                       │
│   ─────                         ─────                       │
│   • Von außen übergeben         • Intern verwaltet          │
│   • Read-only                   • Veränderbar               │
│   • Parent kontrolliert         • Komponente kontrolliert   │
│   • Wie Funktions-Parameter     • Wie Komponenten-Gedächtnis│
└─────────────────────────────────────────────────────────────┘
```

---

## Teil 1: Events in React

### Events in HTML vs React

In HTML verwendest du `onclick` mit einem String, in React `onClick` mit einer Funktion:

```javascript
// HTML
<button onclick="handleClick()">Klick mich</button>

// React (JSX)
<button onClick={handleClick}>Klick mich</button>
```

### Wichtige Unterschiede

| HTML | React |
|------|-------|
| `onclick` | `onClick` |
| `onsubmit` | `onSubmit` |
| `onchange` | `onChange` |
| String: `"handleClick()"` | Funktion: `{handleClick}` |

### Übung 1: Button-Events

> **Ziel:** Click-Events in React verstehen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Dein Button bei Klick eine Meldung in der Konsole ausgibt

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/DatePrinter.jsx`:

```javascript
// src/components/DatePrinter.jsx

function DatePrinter() {
  // Aufgabe 1: Erstelle eine Funktion printDate()
  // die das aktuelle Datum in der Konsole ausgibt
  // Tipp: new Date().toString()

  function printDate() {
    // Dein Code hier
  }

  return (
    <div className="date-printer">
      <h2>Datum Drucker</h2>
      {/* Aufgabe 2: Verbinde den Button mit der Funktion */}
      <button>Datum anzeigen</button>
    </div>
  );
}

export default DatePrinter;
```

2. Verwende die Komponente in `App.jsx`:

```javascript
import DatePrinter from './components/DatePrinter'

function App() {
  return (
    <div className="app">
      <h1>Events Demo</h1>
      <DatePrinter />
    </div>
  )
}

export default App
```

3. Erweitere die Komponente um einen zweiten Button, der eine Begrüßung ausgibt.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/DatePrinter.jsx

function DatePrinter() {
  function printDate() {
    const currentDate = new Date();
    console.log(currentDate.toString());
  }

  function printGreeting() {
    console.log('Hallo! Schön, dass du hier bist!');
  }

  return (
    <div className="date-printer">
      <h2>Datum Drucker</h2>
      <button onClick={printDate}>Datum anzeigen</button>
      <button onClick={printGreeting}>Begrüßung</button>
    </div>
  );
}

export default DatePrinter;
```

</details>

### Wissensfrage 1

Was ist der Unterschied zwischen diesen beiden Varianten?

```javascript
// Variante A
<button onClick={printDate}>Klick</button>

// Variante B
<button onClick={printDate()}>Klick</button>
```

<details>
<summary>Antwort anzeigen</summary>

**Variante A:** Korrekt! Die Funktion `printDate` wird als Referenz übergeben und erst beim Klick ausgeführt.

**Variante B:** Falsch! Die Funktion wird sofort beim Rendern ausgeführt (wegen der Klammern `()`), nicht beim Klick!

**Merke:** Bei Event-Handlern immer die Funktion ohne Klammern übergeben – es sei denn, du verwendest eine Arrow-Function:

```javascript
// Auch korrekt: Arrow-Function
<button onClick={() => printDate()}>Klick</button>

// Nützlich wenn du Parameter übergeben willst:
<button onClick={() => printDate("Heute")}>Klick</button>
```

</details>

---

## Teil 2: Forms & preventDefault

### Das Problem mit Forms

In HTML laden Formulare standardmäßig die Seite neu:

```html
<form>
  <input type="text" />
  <button type="submit">Absenden</button>
</form>
<!-- Seite lädt neu beim Submit! -->
```

In Single-Page-Apps (SPAs) wollen wir das verhindern – wir möchten selbst entscheiden, was mit den Daten passiert!

### Die Lösung: preventDefault()

```javascript
function Form() {
  function handleSubmit(event) {
    event.preventDefault();  // Verhindert Neuladen!
    console.log('Formular wurde abgeschickt');
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Absenden</button>
    </form>
  );
}
```

### Das Event-Objekt

React übergibt automatisch ein Event-Objekt an den Handler:

```javascript
function handleChange(event) {
  // event (oder kurz: e) enthält Informationen über das Event
  event.target;               // Das Element, das das Event ausgelöst hat
  event.target.value;         // Der Wert des Elements
}
```

> **Wichtig – `event.target` ist kontextabhängig:**
> - Bei `onChange` auf einem Input: `event.target` = das Input-Element → `event.target.value` enthält den eingegebenen Text
> - Bei `onSubmit` auf einem Form: `event.target` = das Form-Element → `event.target.value` ist hier **nicht sinnvoll**
>
> **Merke:** Bei Controlled Inputs liest du die Werte aus dem **State**, nicht aus `event.target`!

### Übung 2: Form mit preventDefault

> **Ziel:** Formulare in React kontrollieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Dein Formular die Seite nicht mehr neu lädt

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/SimpleForm.jsx`:

```javascript
// src/components/SimpleForm.jsx

function SimpleForm() {
  // Aufgabe 1: Erstelle einen handleSubmit Handler
  // der preventDefault() aufruft und eine Nachricht loggt

  return (
    <form>
      <h2>Einfaches Formular</h2>

      <div>
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" placeholder="Dein Name" />
      </div>

      <div>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" placeholder="deine@email.de" />
      </div>

      {/* Aufgabe 2: Verbinde das Form mit dem Handler */}
      <button type="submit">Absenden</button>
    </form>
  );
}

export default SimpleForm;
```

2. Teste, ob die Seite beim Absenden NICHT mehr neu lädt.

3. Erweitere den Handler, um auch `'Formular erfolgreich abgeschickt!'` anzuzeigen.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/SimpleForm.jsx

function SimpleForm() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log('Formular erfolgreich abgeschickt!');
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Einfaches Formular</h2>

      <div>
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" placeholder="Dein Name" />
      </div>

      <div>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" placeholder="deine@email.de" />
      </div>

      <button type="submit">Absenden</button>
    </form>
  );
}

export default SimpleForm;
```

</details>

---

## Teil 3: useState verstehen

### Was ist useState?

`useState` ist ein **React Hook**, der es Komponenten ermöglicht, sich Werte zu "merken":

```javascript
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  //     │       │              │
  //     │       │              └── Startwert
  //     │       └── Setter-Funktion (zum Ändern)
  //     └── Aktueller Wert

  return <p>Count: {count}</p>;
}
```

### Wie useState funktioniert

```
┌─────────────────────────────────────────────────────────────┐
│                       useState(0)                           │
│                           │                                 │
│                           ▼                                 │
│              ┌────────────────────────┐                     │
│              │  Gibt Array zurück:    │                     │
│              │  [0, setCount]         │                     │
│              └────────────────────────┘                     │
│                           │                                 │
│           ┌───────────────┴───────────────┐                 │
│           ▼                               ▼                 │
│    ┌─────────────┐                ┌─────────────┐           │
│    │   count     │                │  setCount   │           │
│    │   = 0       │                │  (Funktion) │           │
│    └─────────────┘                └─────────────┘           │
│                                          │                  │
│                                          ▼                  │
│                              setCount(1) → React rendert    │
│                                            Komponente neu   │
└─────────────────────────────────────────────────────────────┘
```

### Array-Destrukturierung

`useState` gibt ein Array mit genau zwei Elementen zurück. Wir nutzen Array-Destrukturierung:

```javascript
// Das passiert im Hintergrund:
const stateArray = useState(0);
const count = stateArray[0];      // Wert
const setCount = stateArray[1];   // Setter

// Kurzform mit Destrukturierung:
const [count, setCount] = useState(0);
```

### Übung 3: Erster Counter

> **Ziel:** useState verstehen und anwenden
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Counter hoch und runter zählt

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/Counter.jsx`:

```javascript
// src/components/Counter.jsx
import { useState } from 'react';

function Counter() {
  // Aufgabe 1: Erstelle einen State für count mit Startwert 0
  // const [count, setCount] = ???

  // Aufgabe 2: Erstelle eine increment Funktion
  function increment() {
    // Erhöhe count um 1
  }

  // Aufgabe 3: Erstelle eine decrement Funktion
  function decrement() {
    // Verringere count um 1
  }

  return (
    <div className="counter">
      <h2>Counter</h2>
      <p className="count">{/* Zeige count hier an */}</p>
      <div className="buttons">
        {/* Aufgabe 4: Verbinde die Buttons mit den Funktionen */}
        <button>-1</button>
        <button>+1</button>
      </div>
    </div>
  );
}

export default Counter;
```

2. Füge etwas CSS hinzu (in `App.css`):

```css
.counter {
  text-align: center;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 300px;
  margin: 20px auto;
}

.counter .count {
  font-size: 48px;
  font-weight: bold;
  color: #3498db;
  margin: 20px 0;
}

.counter .buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.counter button {
  padding: 10px 20px;
  font-size: 18px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #3498db;
  color: white;
}

.counter button:hover {
  background: #2980b9;
}
```

3. **Bonus:** Füge einen "Reset"-Button hinzu, der count auf 0 zurücksetzt.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/Counter.jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  function increment() {
    // Functional Update: Nutzt den vorherigen Wert
    setCount(prevCount => prevCount + 1);
  }

  function decrement() {
    setCount(prevCount => prevCount - 1);
  }

  function reset() {
    setCount(0);
  }

  return (
    <div className="counter">
      <h2>Counter</h2>
      <p className="count">{count}</p>
      <div className="buttons">
        <button onClick={decrement}>-1</button>
        <button onClick={reset}>Reset</button>
        <button onClick={increment}>+1</button>
      </div>
    </div>
  );
}

export default Counter;
```

> **Best Practice: Functional Updates**
> Statt `setCount(count + 1)` nutzen wir `setCount(prevCount => prevCount + 1)`.
> Das ist robuster, wenn mehrere Updates schnell hintereinander passieren oder wenn der State von seinem vorherigen Wert abhängt.

</details>

### Wissensfrage 2

Warum funktioniert das nicht?

```javascript
function Counter() {
  const [count, setCount] = useState(0);

  function increment() {
    count = count + 1;  // Direkte Zuweisung
  }

  // ...
}
```

<details>
<summary>Antwort anzeigen</summary>

**Zwei Probleme:**

1. **`count` ist eine Konstante** (`const`) – sie kann nicht direkt geändert werden.

2. **React weiß nicht von der Änderung** – selbst wenn es technisch ginge, würde React die Komponente nicht neu rendern.

**Die Setter-Funktion (`setCount`) ist wichtig, weil sie:**
- Den neuen Wert speichert
- React signalisiert, dass ein Re-Render nötig ist

**Merke:** State immer nur über die Setter-Funktion ändern!

</details>

---

## Teil 4: Controlled Inputs

### Was sind Controlled Inputs?

Ein **Controlled Input** ist ein Formularfeld, dessen Wert von React-State kontrolliert wird:

```javascript
function ControlledInput() {
  const [text, setText] = useState('');

  return (
    <input
      type="text"
      value={text}              // Wert kommt aus State
      onChange={(e) => setText(e.target.value)}  // Änderungen gehen in State
    />
  );
}
```

### Der Datenfluss

```
┌─────────────────────────────────────────────────────────────┐
│                   CONTROLLED INPUT                          │
│                                                             │
│   ┌─────────────┐         value={text}           ┌─────────┐│
│   │             │ ──────────────────────────────>│         ││
│   │    State    │                                │  Input  ││
│   │  text=""    │ <──────────────────────────────│         ││
│   │             │    onChange → setText(value)   │         ││
│   └─────────────┘                                └─────────┘│
│                                                             │
│   Der State ist die "Single Source of Truth"                │
└─────────────────────────────────────────────────────────────┘
```

### Übung 4: Controlled Input erstellen

> **Ziel:** Ein Controlled Input mit useState erstellen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Input den Text in Echtzeit anzeigt

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/NameInput.jsx`:

```javascript
// src/components/NameInput.jsx
import { useState } from 'react';

function NameInput() {
  // Aufgabe 1: Erstelle einen State für den Namen
  const [name, setName] = useState('');

  return (
    <div className="name-input">
      <h2>Wie heißt du?</h2>

      {/* Aufgabe 2: Mache das Input "controlled" */}
      <input
        type="text"
        placeholder="Dein Name"
        // value={???}
        // onChange={???}
      />

      {/* Aufgabe 3: Zeige eine Begrüßung wenn ein Name eingegeben wurde */}
      <p className="greeting">
        {/* Zeige "Hallo [name]!" wenn name nicht leer ist */}
      </p>
    </div>
  );
}

export default NameInput;
```

2. Füge CSS hinzu:

```css
.name-input {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 400px;
  margin: 20px auto;
}

.name-input input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.name-input input:focus {
  border-color: #3498db;
  outline: none;
}

.name-input .greeting {
  margin-top: 16px;
  font-size: 20px;
  color: #2ecc71;
}
```

3. **Bonus:** Zeige zusätzlich die Anzahl der eingegebenen Zeichen an.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/NameInput.jsx
import { useState } from 'react';

function NameInput() {
  const [name, setName] = useState('');

  return (
    <div className="name-input">
      <h2>Wie heißt du?</h2>

      <input
        type="text"
        placeholder="Dein Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <p className="greeting">
        {name && `Hallo ${name}!`}
      </p>

      <p className="char-count">
        {name.length} Zeichen
      </p>
    </div>
  );
}

export default NameInput;
```

</details>

---

## Teil 5: Mehrere State-Variablen

### Ein State pro Wert

Für jedes unabhängige Datenstück verwendest du einen eigenen `useState`:

```javascript
function UserForm() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState(0);

  // Jeder State ist unabhängig voneinander
}
```

### Übung 5: Multi-Input Formular

> **Ziel:** Mehrere Controlled Inputs verwalten
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Alle Felder korrekt funktionieren

> **Wichtig:** Bei Controlled Forms liest du die Werte im `handleSubmit` aus dem **State** – nicht aus `event.target`! Das ist der Vorteil von Controlled Inputs: Du hast jederzeit Zugriff auf alle Werte.

**Aufgabe:**

1. Erstelle eine `ProfileForm`-Komponente mit mehreren Feldern:

```javascript
// src/components/ProfileForm.jsx
import { useState } from 'react';

function ProfileForm() {
  // Aufgabe: Erstelle States für alle Felder
  const [firstName, setFirstName] = useState('');
  // Weitere States hier...

  function handleSubmit(event) {
    event.preventDefault();
    // Gib alle Werte in der Konsole aus
    console.log('Profil:', {
      firstName,
      // Weitere Werte...
    });
  }

  return (
    <form className="profile-form" onSubmit={handleSubmit}>
      <h2>Profil erstellen</h2>

      <div className="form-group">
        <label htmlFor="firstName">Vorname:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>

      {/* Aufgabe: Füge Felder hinzu für:
          - lastName (Nachname)
          - email (Email)
          - bio (Textarea für Biografie)
      */}

      <button type="submit">Profil speichern</button>
    </form>
  );
}

export default ProfileForm;
```

2. Füge CSS hinzu:

```css
.profile-form {
  max-width: 500px;
  margin: 20px auto;
  padding: 24px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 4px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.profile-form button {
  width: 100%;
  padding: 12px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.profile-form button:hover {
  background: #2980b9;
}
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/ProfileForm.jsx
import { useState } from 'react';

function ProfileForm() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [bio, setBio] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    console.log('Profil:', {
      firstName,
      lastName,
      email,
      bio
    });
  }

  return (
    <form className="profile-form" onSubmit={handleSubmit}>
      <h2>Profil erstellen</h2>

      <div className="form-group">
        <label htmlFor="firstName">Vorname:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label htmlFor="lastName">Nachname:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label htmlFor="bio">Über mich:</label>
        <textarea
          id="bio"
          value={bio}
          onChange={(e) => setBio(e.target.value)}
          placeholder="Erzähl etwas über dich..."
        />
      </div>

      <button type="submit">Profil speichern</button>
    </form>
  );
}

export default ProfileForm;
```

</details>

---

## Teil 6: Stateful vs Stateless

### Die Konzepte

**Stateful (zustandsbehaftet):**
- Komponente verwendet `useState`
- Verwaltet eigene Daten
- Kann sich selbst verändern

**Stateless (zustandslos):**
- Komponente verwendet kein `useState`
- Erhält alle Daten über Props
- "Dumme" Komponente – zeigt nur an

### Best Practice: State an einer Stelle sammeln

```
┌─────────────────────────────────────────────────────────────┐
│                      KOMPONENTEN-DESIGN                     │
│                                                             │
│   EMPFOHLEN:                    VERMEIDEN:                  │
│   ──────────                    ─────────                   │
│                                                             │
│   ┌─────────────┐              ┌─────────────┐              │
│   │ LoginForm   │              │ LoginForm   │              │
│   │ (stateful)  │              │ (stateful)  │              │
│   │ email, pwd  │              │             │              │
│   └──────┬──────┘              └──────┬──────┘              │
│          │                            │                     │
│    ┌─────┴─────┐               ┌─────┴─────┐                │
│    │           │               │           │                │
│    ▼           ▼               ▼           ▼                │
│  ┌─────┐   ┌─────┐         ┌─────┐   ┌─────┐                │
│  │Input│   │Input│         │Input│   │Input│                │
│  │(-)  │   │(-)  │         │(St) │   │(St) │                │
│  └─────┘   └─────┘         └─────┘   └─────┘                │
│                                                             │
│  Input-Komponenten           Jede Komponente hat            │
│  sind stateless –            eigenen State –                │
│  Form kontrolliert           schwer zu koordinieren         │
└─────────────────────────────────────────────────────────────┘
```

### Lokalität von State

Jede Komponenten-Instanz hat ihren **eigenen, unabhängigen State**:

```javascript
function App() {
  return (
    <div>
      <Counter />  {/* Hat eigenen count */}
      <Counter />  {/* Hat eigenen count */}
      <Counter />  {/* Hat eigenen count */}
    </div>
  );
}
```

Wenn du einen Counter erhöhst, ändern sich die anderen nicht!

### Übung 6: Lokalität testen

> **Ziel:** Verstehen, dass State lokal zur Instanz ist
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du mehrere unabhängige Counter hast

**Aufgabe:**

1. Verwende deine Counter-Komponente mehrfach in `App.jsx`:

```javascript
// src/App.jsx
import Counter from './components/Counter'

function App() {
  return (
    <div className="app">
      <h1>Lokalität von State</h1>

      <div className="counter-grid">
        <Counter />
        <Counter />
        <Counter />
      </div>
    </div>
  )
}

export default App
```

2. Füge CSS für die Grid-Ansicht hinzu:

```css
.counter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}
```

3. Teste: Erhöhe den ersten Counter auf 5, den zweiten auf 3, den dritten auf 10. Sind sie unabhängig?

4. **Bonus:** Füge jedem Counter einen Namen als Prop hinzu:

```javascript
<Counter name="Counter A" />
<Counter name="Counter B" />
<Counter name="Counter C" />
```

<details>
<summary>Musterlösung mit Namen</summary>

```javascript
// src/components/Counter.jsx
import { useState } from 'react';

function Counter({ name = "Counter" }) {
  const [count, setCount] = useState(0);

  return (
    <div className="counter">
      <h2>{name}</h2>
      <p className="count">{count}</p>
      <div className="buttons">
        <button onClick={() => setCount(c => c - 1)}>-1</button>
        <button onClick={() => setCount(0)}>Reset</button>
        <button onClick={() => setCount(c => c + 1)}>+1</button>
      </div>
    </div>
  );
}

export default Counter;
```

</details>

---

## Teil 7: Praxis - Login-Formular

Zeit für ein vollständiges Beispiel!

> **Ziel:** Ein funktionales Login-Formular mit State bauen
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Login und Logout funktionieren

### Aufgabe: SignInForm

Erstelle ein Login-Formular mit:

1. Email- und Passwort-Felder (Controlled Inputs)
2. Form-Submit mit preventDefault
3. Einfache Validierung (Email = "test@test.de", Passwort = "123456")
4. Nach erfolgreichem Login: Zeige "Willkommen!" statt Formular
5. Logout-Button zum Ausloggen
6. Nach Submit: **Passwort zurücksetzen** (Sicherheit) – Email bleibt erhalten, da sie im eingeloggten Zustand angezeigt wird

**Starter-Code:**

```javascript
// src/components/SignInForm.jsx
import { useState } from 'react';

function SignInForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [error, setError] = useState('');

  function handleSubmit(event) {
    event.preventDefault();

    // Aufgabe: Validierung hier
    // Wenn email === "test@test.de" und password === "123456"
    // → setIsLoggedIn(true)
    // Sonst → setError("Ungültige Anmeldedaten!")

    // Nach Versuch: Passwort zurücksetzen (Sicherheit)
    // Email bleibt erhalten (wird im eingeloggten Zustand angezeigt)
  }

  function handleLogout() {
    setIsLoggedIn(false);
  }

  // Wenn eingeloggt, zeige Willkommensnachricht
  if (isLoggedIn) {
    return (
      <div className="welcome">
        <h2>Willkommen!</h2>
        <p>Du bist eingeloggt als {email}</p>
        <button onClick={handleLogout}>Ausloggen</button>
      </div>
    );
  }

  // Sonst zeige Login-Formular
  return (
    <form className="signin-form" onSubmit={handleSubmit}>
      <h2>Anmelden</h2>

      {error && <p className="error">{error}</p>}

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          placeholder="test@test.de"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label htmlFor="password">Passwort:</label>
        <input
          type="password"
          id="password"
          placeholder="123456"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      <button type="submit">Anmelden</button>
    </form>
  );
}

export default SignInForm;
```

**CSS:**

```css
.signin-form,
.welcome {
  max-width: 400px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
}

.signin-form h2,
.welcome h2 {
  margin-top: 0;
  text-align: center;
}

.signin-form .error {
  background: #f8d7da;
  color: #721c24;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 16px;
}

.signin-form .form-group {
  margin-bottom: 16px;
}

.signin-form label {
  display: block;
  margin-bottom: 4px;
  font-weight: bold;
}

.signin-form input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.signin-form button,
.welcome button {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.signin-form button:hover,
.welcome button:hover {
  background: #2980b9;
}

.welcome {
  text-align: center;
}

.welcome button {
  background: #e74c3c;
}

.welcome button:hover {
  background: #c0392b;
}
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/SignInForm.jsx
import { useState } from 'react';

function SignInForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [error, setError] = useState('');

  function handleSubmit(event) {
    event.preventDefault();

    // Einfache Validierung
    if (email === 'test@test.de' && password === '123456') {
      setIsLoggedIn(true);
      setError('');
    } else {
      setError('Ungültige Anmeldedaten!');
    }

    // Passwort immer zurücksetzen (Sicherheit)
    setPassword('');
  }

  function handleLogout() {
    setIsLoggedIn(false);
    // Email beim Logout zurücksetzen (frischer Start für nächsten Login)
    setEmail('');
  }

  if (isLoggedIn) {
    return (
      <div className="welcome">
        <h2>Willkommen!</h2>
        <p>Du bist eingeloggt als {email}</p>
        <button onClick={handleLogout}>Ausloggen</button>
      </div>
    );
  }

  return (
    <form className="signin-form" onSubmit={handleSubmit}>
      <h2>Anmelden</h2>

      {error && <p className="error">{error}</p>}

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          placeholder="test@test.de"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
            setError(''); // Fehlermeldung beim Tippen löschen
          }}
        />
      </div>

      <div className="form-group">
        <label htmlFor="password">Passwort:</label>
        <input
          type="password"
          id="password"
          placeholder="123456"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
            setError(''); // Fehlermeldung beim Tippen löschen
          }}
        />
      </div>

      <button type="submit">Anmelden</button>
    </form>
  );
}

export default SignInForm;
```

> **Hinweis:** Wir löschen die Fehlermeldung beim Tippen (`setError('')`), damit sie nicht "kleben bleibt", wenn der Nutzer seine Eingabe korrigiert. Das ist eine gute UX-Practice!

</details>

---

## Teil 8: Praxis - Todo-Eingabe

Eine weitere praktische Übung!

> **Ziel:** Eine Todo-Eingabe mit dynamischer Liste bauen
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Du Todos hinzufügen und anzeigen kannst

### Aufgabe: TodoInput

Erstelle eine Komponente, die:

1. Ein Eingabefeld für neue Todos hat
2. Einen "Hinzufügen"-Button hat
3. Todos in einer Liste anzeigt
4. Das Eingabefeld nach dem Hinzufügen leert

**Anforderungen:**

```javascript
// So soll die Komponente funktionieren:
// 1. Nutzer tippt "Einkaufen gehen"
// 2. Nutzer klickt "Hinzufügen" oder drückt Enter (Form-Submit!)
// 3. "Einkaufen gehen" erscheint in der Liste
// 4. Eingabefeld ist wieder leer
```

> **Tipp:** Da wir `<form onSubmit={...}>` verwenden, wird Enter im Input automatisch den Submit auslösen – du musst dafür nichts extra programmieren!

**Starter-Code:**

```javascript
// src/components/TodoInput.jsx
import { useState } from 'react';

function TodoInput() {
  const [inputValue, setInputValue] = useState('');
  const [todos, setTodos] = useState([]);

  function handleSubmit(event) {
    event.preventDefault();

    // Aufgabe:
    // 1. Prüfe ob inputValue nicht leer ist
    // 2. Füge inputValue zu todos hinzu
    // 3. Setze inputValue zurück

    // Tipp für Array-Update:
    // setTodos([...todos, neuerWert])
  }

  return (
    <div className="todo-input">
      <h2>Meine Todos</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Was möchtest du tun?"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit">Hinzufügen</button>
      </form>

      {/* Aufgabe: Zeige die Todos als Liste an */}
      <ul className="todo-list">
        {/* todos.map(...) */}
      </ul>

      {todos.length === 0 && (
        <p className="empty">Keine Todos vorhanden. Füge eines hinzu!</p>
      )}
    </div>
  );
}

export default TodoInput;
```

**CSS:**

```css
.todo-input {
  max-width: 500px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.todo-input h2 {
  margin-top: 0;
}

.todo-input form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.todo-input input {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.todo-input button {
  padding: 12px 24px;
  background: #2ecc71;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.todo-input button:hover {
  background: #27ae60;
}

.todo-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.todo-list li {
  padding: 12px;
  border-bottom: 1px solid #eee;
  display: flex;
  align-items: center;
}

.todo-list li:last-child {
  border-bottom: none;
}

.empty {
  text-align: center;
  color: #888;
  font-style: italic;
}
```

**Bonus-Aufgaben:**

1. Füge einen "Löschen"-Button zu jedem Todo hinzu
2. Zeige die Anzahl der Todos an
3. Füge einen "Alle löschen"-Button hinzu

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/TodoInput.jsx
import { useState } from 'react';

function TodoInput() {
  const [inputValue, setInputValue] = useState('');
  const [todos, setTodos] = useState([]);

  function handleSubmit(event) {
    event.preventDefault();

    // Leere Eingaben ignorieren
    if (inputValue.trim() === '') return;

    // Todo hinzufügen (Functional Update für Konsistenz)
    setTodos(prevTodos => [...prevTodos, inputValue.trim()]);

    // Eingabefeld leeren
    setInputValue('');
  }

  function deleteTodo(indexToDelete) {
    setTodos(prevTodos => prevTodos.filter((_, index) => index !== indexToDelete));
  }

  function clearAll() {
    setTodos([]);
  }

  return (
    <div className="todo-input">
      <h2>Meine Todos ({todos.length})</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Was möchtest du tun?"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit">Hinzufügen</button>
      </form>

      {/* Hinweis: key={index} ist für diese Lernübung ok.
          In echten Apps mit dynamischen Listen solltest du
          stabile IDs verwenden (z.B. id aus Datenbank). */}
      <ul className="todo-list">
        {todos.map((todo, index) => (
          <li key={index}>
            <span>{todo}</span>
            <button
              className="delete-btn"
              onClick={() => deleteTodo(index)}
            >
              Löschen
            </button>
          </li>
        ))}
      </ul>

      {todos.length === 0 && (
        <p className="empty">Keine Todos vorhanden. Füge eines hinzu!</p>
      )}

      {todos.length > 0 && (
        <button className="clear-all" onClick={clearAll}>
          Alle löschen
        </button>
      )}
    </div>
  );
}

export default TodoInput;
```

**Zusätzliches CSS:**

```css
.todo-list li {
  justify-content: space-between;
}

.delete-btn {
  padding: 4px 8px;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
}

.delete-btn:hover {
  background: #c0392b;
}

.clear-all {
  width: 100%;
  padding: 10px;
  background: #95a5a6;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 16px;
}

.clear-all:hover {
  background: #7f8c8d;
}
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Events** | Auf Benutzeraktionen reagieren | `onClick={handleClick}` |
| **preventDefault** | Standard-Verhalten verhindern | `e.preventDefault()` |
| **useState** | State in Komponenten verwalten | `const [x, setX] = useState(0)` |
| **Controlled Inputs** | Inputs mit State verbinden | `value={x} onChange={...}` |
| **Stateful** | Komponente mit eigenem State | Verwendet `useState` |
| **Stateless** | Komponente ohne State | Nur Props |
| **Lokalität** | Jede Instanz hat eigenen State | Mehrere unabhängige Counter |

### useState auf einen Blick

```javascript
import { useState } from 'react';

function MyComponent() {
  // State deklarieren
  const [value, setValue] = useState(initialValue);

  // State lesen
  console.log(value);

  // State ändern (einfacher Wert)
  setValue(newValue);

  // State mit vorherigem Wert ändern (Functional Update - empfohlen!)
  setValue(prevValue => prevValue + 1);

  return <div>{value}</div>;
}
```

> **Best Practice:** Wenn der neue State vom vorherigen abhängt, nutze immer das Functional Update Pattern: `setValue(prev => prev + 1)` statt `setValue(value + 1)`.

### Controlled Inputs auf einen Blick

```javascript
function ControlledForm() {
  const [text, setText] = useState('');

  return (
    <input
      value={text}                           // Wert aus State
      onChange={(e) => setText(e.target.value)}  // Änderung in State
    />
  );
}
```

### Wichtige Regeln

1. **State nie direkt ändern** – Immer die Setter-Funktion verwenden!
2. **useState nur auf oberster Ebene** – Nicht in Schleifen oder Bedingungen
3. **Ein State pro Wert** – Für jedes unabhängige Datenstück einen eigenen State
4. **State ist lokal** – Jede Komponenten-Instanz hat eigenen State
5. **Controlled Inputs** – value + onChange für volle Kontrolle

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du verstehst den Unterschied zwischen Props und State
- [ ] Du kannst Events in React verwenden (onClick, onSubmit, onChange)
- [ ] Du kannst `e.preventDefault()` bei Forms anwenden
- [ ] Du kannst useState importieren und verwenden
- [ ] Du verstehst Array-Destrukturierung bei useState
- [ ] Du kannst Controlled Inputs erstellen
- [ ] Du verstehst den Unterschied zwischen stateful und stateless
- [ ] Du verstehst, dass State lokal zur Komponenten-Instanz ist

**Alles abgehakt?** Du bist bereit für fortgeschrittene State-Patterns!
