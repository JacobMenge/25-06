# Rendering, Listen & Keys - Praktische Übung

## Übersicht

Willkommen zur vierten React-Übung! Hier lernst du, wie du dynamische Listen in React darstellst und warum Keys so wichtig sind.

In dieser Übung lernst du:
- **map()** - Arrays in React-Elemente transformieren
- **Arrow Functions** - Kompakte Funktionssyntax für map()
- **Listen rendern** - Arrays als UI-Elemente darstellen
- **Keys** - Warum React eindeutige Identifikatoren braucht
- **Grids** - Listen als Grid-Layout anzeigen
- **Konditionales Rendering** - Elemente bedingt anzeigen
- **Daten aus JSON** - Externe Daten laden und anzeigen

Diese Übung baut auf "24.3 useState & Controlled Inputs" auf – stelle sicher, dass du State und Events verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | map() und Arrow Functions | 5 min (lesen) |
| **Teil 1** | map() Grundlagen | 15 min |
| **Teil 2** | Arrow Functions verstehen | 15 min |
| **Teil 3** | Listen in React rendern | 20 min |
| **Teil 4** | Keys verstehen | 15 min |
| **Teil 5** | Daten aus JSON laden | 15 min |
| **Teil 6** | Grids erstellen | 15 min |
| **Teil 7** | Konditionales Rendering | 20 min |
| **Teil 8** | Praxis: Produkt-Katalog | 30 min |
| **Teil 9** | Praxis: Todo-Liste mit Filter | 30 min |
| | **Gesamt** | **ca. 3 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Rückblick** - map() und Arrow Functions auffrischen
2. **Teil 3** - Listen in React rendern - *Das Kernkonzept*
3. **Teil 4** - Keys verstehen - *Wichtig für Performance*
4. **Teil 7** - Konditionales Rendering - *Flexibilität*
5. **Teil 8** - Praxis: Produkt-Katalog - *Alles zusammen*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast ein funktionierendes React-Projekt (aus Übung 24.1, 24.2 oder 24.3)
2. Der Dev-Server läuft (`npm run dev`)
3. Du kannst Änderungen im Browser sehen

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest listen-uebung -- --template react
cd listen-uebung
npm install
npm run dev
```

> **Tipp für diese Übung:** Du wirst mehrere Komponenten bauen. Um Verwirrung zu vermeiden: **Rendere immer nur eine Übungskomponente gleichzeitig in `App.jsx`**. Kommentiere die anderen aus, während du an einer neuen arbeitest.

---

## Rückblick: map() und Arrow Functions

### Die map() Funktion

`map()` ist eine Array-Methode, die jedes Element transformiert und ein neues Array zurückgibt:

```javascript
const names = ['Alice', 'Bob', 'Charlie'];

// Jedes Element transformieren
const capitalizedNames = names.map(function(name) {
  return name.toUpperCase();
});

console.log(capitalizedNames);
// => ['ALICE', 'BOB', 'CHARLIE']
```

### Arrow Functions

Für Funktionen gibt es eine Kurzschreibweise – die "Arrow-Syntax":

```javascript
// Normale Funktion
function capitalize(name) {
  return name.toUpperCase();
}

// Arrow Function (mit Block)
const capitalize = (name) => {
  return name.toUpperCase();
};

// Arrow Function (Kurzform - eine Zeile, kein return nötig)
const capitalize = name => name.toUpperCase();
```

### map() + Arrow Function kombiniert

```javascript
const names = ['Alice', 'Bob', 'Charlie'];

// Kombination: map() mit Arrow Function
const capitalizedNames = names.map(name => name.toUpperCase());

console.log(capitalizedNames);
// => ['ALICE', 'BOB', 'CHARLIE']
```

### Warum ist das wichtig für React?

In React nutzen wir `map()` um Arrays in JSX zu transformieren. **Wichtig:** `map()` gibt immer ein **Array** zurück – und React kann Arrays von JSX-Elementen direkt rendern!

```javascript
const names = ['Alice', 'Bob', 'Charlie'];

// Array von Strings → Array von JSX-Elementen
const listItems = names.map(name => <li>{name}</li>);
// Ergebnis: [<li>Alice</li>, <li>Bob</li>, <li>Charlie</li>]

// Dieses Array kann React direkt rendern!
```

---

## Teil 1: map() Grundlagen

### Die map() Funktion verstehen

```
┌─────────────────────────────────────────────────────────────┐
│                       map() FUNKTION                         │
│                                                              │
│   Original Array:     ['Alice', 'Bob', 'Charlie']           │
│                            │                                 │
│                            ▼                                 │
│            ┌──────────────────────────────┐                 │
│            │  name => name.toUpperCase()  │                 │
│            └──────────────────────────────┘                 │
│                            │                                 │
│                            ▼                                 │
│   Neues Array:        ['ALICE', 'BOB', 'CHARLIE']           │
│                                                              │
│   • Funktion wird auf JEDES Element angewandt               │
│   • Gibt NEUES Array zurück (Original bleibt unverändert)   │
│   • Neues Array ist GLEICH LANG                             │
└─────────────────────────────────────────────────────────────┘
```

### map() mit Index

`map()` kann auch den Index des aktuellen Elements liefern:

```javascript
const names = ['Alice', 'Bob', 'Charlie'];

// Mit Index als zweitem Parameter
const numberedNames = names.map((name, index) => {
  return `${index + 1}. ${name}`;
});

console.log(numberedNames);
// => ['1. Alice', '2. Bob', '3. Charlie']
```

### Übung 1: map() üben

> **Ziel:** Die map() Funktion verstehen und anwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Arrays transformieren kannst

**Aufgabe 1: Lieblingstiere**

Erstelle eine neue Datei `src/playground.js` (oder teste in der Browser-Konsole):

```javascript
// Aufgabe 1: Lieblingstiere in Großbuchstaben
const animals = ['Hund', 'Katze', 'Papagei', 'Hamster'];

// Transformiere zu Großbuchstaben mit map()
const animalsUppercase = // Dein Code hier

console.log(animalsUppercase);
// Erwartete Ausgabe: ['HUND', 'KATZE', 'PAPAGEI', 'HAMSTER']
```

**Aufgabe 2: Preise formatieren**

```javascript
// Aufgabe 2: Preise aufrunden und formatieren
const prices = [9.99, 24.50, 3.25, 149.99];

// Runde auf mit Math.ceil() und hänge " €" an
const formattedPrices = // Dein Code hier

console.log(formattedPrices);
// Erwartete Ausgabe: ['10 €', '25 €', '4 €', '150 €']
```

**Aufgabe 3: Nummerierte Liste**

```javascript
// Aufgabe 3: Nummerierte Liste erstellen
const tasks = ['Einkaufen', 'Kochen', 'Abwaschen'];

// Erstelle nummerierte Liste: "1. Einkaufen", "2. Kochen", etc.
const numberedTasks = // Dein Code hier (nutze den Index!)

console.log(numberedTasks);
// Erwartete Ausgabe: ['1. Einkaufen', '2. Kochen', '3. Abwaschen']
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// Aufgabe 1: Lieblingstiere in Großbuchstaben
const animals = ['Hund', 'Katze', 'Papagei', 'Hamster'];
const animalsUppercase = animals.map(animal => animal.toUpperCase());
console.log(animalsUppercase);
// => ['HUND', 'KATZE', 'PAPAGEI', 'HAMSTER']

// Aufgabe 2: Preise aufrunden und formatieren
const prices = [9.99, 24.50, 3.25, 149.99];
const formattedPrices = prices.map(price => `${Math.ceil(price)} €`);
console.log(formattedPrices);
// => ['10 €', '25 €', '4 €', '150 €']

// Aufgabe 3: Nummerierte Liste erstellen
const tasks = ['Einkaufen', 'Kochen', 'Abwaschen'];
const numberedTasks = tasks.map((task, index) => `${index + 1}. ${task}`);
console.log(numberedTasks);
// => ['1. Einkaufen', '2. Kochen', '3. Abwaschen']
```

</details>

---

## Teil 2: Arrow Functions verstehen

### Die verschiedenen Schreibweisen

> **Hinweis:** Die folgenden Beispiele zeigen jeweils alternative Schreibweisen derselben Funktion. Kopiere sie **einzeln** – nicht als kompletten Block, sonst gibt es Fehler wegen doppelter Variablennamen!

```javascript
// 1. Normale Funktion
function double(x) {
  return x * 2;
}

// 2. Arrow Function mit Block und return
const double = (x) => {
  return x * 2;
};

// 3. Arrow Function ohne Klammern (bei einem Parameter)
const double = x => {
  return x * 2;
};

// 4. Arrow Function Kurzform (eine Zeile, implizites return)
const double = x => x * 2;
```

### Wann welche Variante?

| Variante | Wann verwenden |
|----------|----------------|
| Mit `{}` und `return` | Bei mehreren Zeilen Logik |
| Ohne `()` um Parameter | Bei genau einem Parameter |
| Kurzform (ohne `{}`) | Bei einfachen Einzeilern |

### Wichtig: Klammern bei Parametern

```javascript
// Keine Parameter: Klammern NÖTIG
const greet = () => 'Hallo!';

// Ein Parameter: Klammern OPTIONAL
const double = x => x * 2;
const double = (x) => x * 2;  // Auch ok

// Mehrere Parameter: Klammern NÖTIG
const add = (a, b) => a + b;
```

### Übung 2: Arrow Functions üben

> **Ziel:** Arrow Functions sicher verwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du verschiedene Arrow Function Varianten kennst

**Aufgabe:** Schreibe diese normalen Funktionen als Arrow Functions um:

```javascript
// 1. Normale Funktion -> Arrow Function (Kurzform)
function square(n) {
  return n * n;
}
// Deine Arrow Function:
const squareArrow = // ???

// 2. Normale Funktion -> Arrow Function (mit Index für map)
function addIndex(item, index) {
  return `${index}: ${item}`;
}
// Deine Arrow Function:
const addIndexArrow = // ???

// 3. Normale Funktion -> Arrow Function (für Objekte)
function createUser(name, age) {
  return { name: name, age: age };
}
// Deine Arrow Function (Tipp: Bei Objekten Klammern drum!):
const createUserArrow = // ???
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// 1. Quadrat berechnen
const squareArrow = n => n * n;

// Test:
console.log(squareArrow(5)); // => 25

// 2. Mit Index
const addIndexArrow = (item, index) => `${index}: ${item}`;

// Test:
console.log(['a', 'b', 'c'].map(addIndexArrow));
// => ['0: a', '1: b', '2: c']

// 3. Objekt erstellen
// WICHTIG: Bei Objekten als Rückgabe: Klammern drum!
const createUserArrow = (name, age) => ({ name, age });
// Kurzschreibweise: { name: name, age: age } → { name, age }

// Test:
console.log(createUserArrow('Max', 25));
// => { name: 'Max', age: 25 }
```

**Warum Klammern bei Objekten?**

Ohne Klammern denkt JavaScript, die `{}` wären ein Funktions-Block:

```javascript
// FALSCH - {} wird als Block interpretiert
const createUser = (name) => { name: name };  // Syntax Error!

// RICHTIG - () zeigt an, dass es ein Objekt ist
const createUser = (name) => ({ name: name });
```

</details>

---

## Teil 3: Listen in React rendern

### Von Array zu React-Elementen

In React nutzen wir `map()` um Arrays in JSX zu transformieren:

```javascript
function NamesList() {
  const names = ['Alice', 'Bob', 'Charlie'];

  return (
    <ul>
      {names.map(name => {
        return <li>{name}</li>
      })}
    </ul>
  );
}
```

### Kurzschreibweise

```javascript
function NamesList() {
  const names = ['Alice', 'Bob', 'Charlie'];

  return (
    <ul>
      {names.map(name => <li>{name}</li>)}
    </ul>
  );
}
```

### Visualisierung

```
┌─────────────────────────────────────────────────────────────┐
│                   LISTEN RENDERN                              │
│                                                              │
│   Array:              ['Alice', 'Bob', 'Charlie']           │
│                                │                             │
│                                ▼                             │
│                      names.map(name =>                       │
│                        <li>{name}</li>                       │
│                      )                                       │
│                                │                             │
│                                ▼                             │
│   JSX-Elemente:       [<li>Alice</li>,                      │
│                        <li>Bob</li>,                         │
│                        <li>Charlie</li>]                     │
│                                │                             │
│                                ▼                             │
│   Gerendert:          • Alice                               │
│                       • Bob                                  │
│                       • Charlie                              │
└─────────────────────────────────────────────────────────────┘
```

### Übung 3: Erste React-Liste

> **Ziel:** Eine Liste von Elementen in React rendern
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Deine Liste im Browser angezeigt wird

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/FruitList.jsx`:

```javascript
// src/components/FruitList.jsx

function FruitList() {
  const fruits = ['Apfel', 'Banane', 'Orange', 'Mango', 'Kiwi'];

  return (
    <div className="fruit-list">
      <h2>Meine Lieblingsobst</h2>

      {/* Aufgabe: Rendere die Früchte als <ul> mit <li> Elementen */}
      {/* Nutze map() um das Array zu transformieren */}

    </div>
  );
}

export default FruitList;
```

2. Verwende die Komponente in `App.jsx`:

```javascript
import FruitList from './components/FruitList'

function App() {
  return (
    <div className="app">
      <h1>Listen Demo</h1>
      <FruitList />
    </div>
  )
}

export default App
```

3. **Bonus:** Erweitere die Komponente, sodass sie die Anzahl der Früchte anzeigt.

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/FruitList.jsx

function FruitList() {
  const fruits = ['Apfel', 'Banane', 'Orange', 'Mango', 'Kiwi'];

  return (
    <div className="fruit-list">
      <h2>Meine Lieblingsfrüchte ({fruits.length})</h2>

      <ul>
        {fruits.map(fruit => (
          <li>{fruit}</li>
        ))}
      </ul>
    </div>
  );
}

export default FruitList;
```

> **Hinweis:** Die Musterlösung hat **absichtlich** keinen `key` – öffne die Browser-Konsole (F12), und du siehst die Warnung: "Each child in a list should have a unique 'key' prop." Warum Keys wichtig sind und wie du sie richtig verwendest, lernst du im nächsten Teil!

</details>

### Wissensfrage 1

Warum kannst du `map()` direkt in JSX verwenden, aber nicht `forEach()`?

<details>
<summary>Antwort anzeigen</summary>

**`map()` gibt ein neues Array zurück** – genau das, was React zum Rendern braucht!

**`forEach()` gibt `undefined` zurück** – nichts zum Rendern.

```javascript
// map() → gibt Array zurück → funktioniert!
{fruits.map(fruit => <li>{fruit}</li>)}

// forEach() → gibt undefined zurück → funktioniert NICHT!
{fruits.forEach(fruit => <li>{fruit}</li>)}  // Zeigt nichts an!
```

**Merke:** In JSX immer `map()` für Listen verwenden!

</details>

---

## Teil 4: Keys verstehen

### Das Problem ohne Keys

Öffne die Browser-Konsole (F12) – du siehst wahrscheinlich diese Warnung:

```
Warning: Each child in a list should have a unique "key" prop.
```

### Warum braucht React Keys?

Keys helfen React zu verstehen, welche Elemente sich geändert haben:

```
┌─────────────────────────────────────────────────────────────┐
│                    OHNE KEYS                                  │
│                                                              │
│   Vorher:    [Alice] [Bob] [Charlie]                        │
│   Nachher:   [Zoe] [Alice] [Bob] [Charlie]                  │
│                                                              │
│   React denkt:                                               │
│   "Alice → Zoe? Bob → Alice? Charlie → Bob? Neues Element?" │
│   → ALLES neu rendern (ineffizient!)                        │
│                                                              │
│────────────────────────────────────────────────────────────│
│                    MIT KEYS                                   │
│                                                              │
│   Vorher:    [key:1 Alice] [key:2 Bob] [key:3 Charlie]      │
│   Nachher:   [key:4 Zoe] [key:1 Alice] [key:2 Bob] [key:3..]│
│                                                              │
│   React erkennt:                                             │
│   "Zoe ist neu, der Rest bleibt gleich."                    │
│   → Nur Zoe einfügen (effizient!)                           │
└─────────────────────────────────────────────────────────────┘
```

### Keys richtig verwenden

```javascript
function UserList() {
  const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
    { id: 3, name: 'Charlie' }
  ];

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name}
        </li>
      ))}
    </ul>
  );
}
```

### Welche Keys sind gut?

| Key-Typ | Geeignet? | Warum? |
|---------|-----------|--------|
| Datenbank-ID | ✅ Ideal | Eindeutig und stabil |
| Eindeutiger String | ✅ Gut | z.B. `user.email` |
| Index als Key | ⚠️ Notfall | Nur bei statischen Listen! |
| Math.random() | ❌ Niemals | Ändert sich bei jedem Render! |

### Wann ist Index als Key okay?

> **⚠️ Wichtig:** Index als Key ist nur bei **wirklich statischen Listen** akzeptabel – also Listen, die sich **niemals** ändern!

Nur wenn **alle** diese Bedingungen erfüllt sind:
1. Die Liste wird **nie** sortiert
2. Die Liste wird **nie** gefiltert
3. Elemente werden **nie** hinzugefügt
4. Elemente werden **nie** entfernt oder verschoben
5. Elemente haben **keine** eigene ID (z.B. aus einer Datenbank)

```javascript
// Index als Key: NUR für wirklich statische Listen!
// ✅ OK – Wochentage ändern sich nie
const weekdays = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'];

{weekdays.map((day, index) => (
  <li key={index}>{day}</li>
))}

// ❌ FALSCH – Todo-Liste kann sich ändern!
// Beim Löschen/Einfügen bekommt React falsche Zuordnungen
{todos.map((todo, index) => (
  <TodoItem key={index} todo={todo} />  // BUG-Gefahr!
))}
```

**Was passiert bei falscher Verwendung?**

Wenn du Index als Key für dynamische Listen verwendest und ein Element in der Mitte löschst oder einfügst, verliert React den Überblick: Die Keys verschieben sich, aber React denkt die Elemente mit dem gleichen Key sind dieselben. Das führt zu:
- Falschen Daten in Input-Feldern
- Animations-Fehlern
- Schwer zu findenden Bugs

### Übung 4: Keys hinzufügen

> **Ziel:** Keys korrekt verwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Keine Key-Warnung mehr in der Konsole erscheint

**Aufgabe:**

1. Erstelle eine neue Datei `src/components/UserList.jsx`:

```javascript
// src/components/UserList.jsx

function UserList() {
  const users = [
    { id: 1, name: 'Max Mustermann', role: 'Developer' },
    { id: 2, name: 'Anna Schmidt', role: 'Designer' },
    { id: 3, name: 'Tom Weber', role: 'Manager' },
    { id: 4, name: 'Lisa Braun', role: 'Developer' }
  ];

  return (
    <div className="user-list">
      <h2>Team-Mitglieder</h2>

      <ul>
        {/* Aufgabe: Füge den korrekten key hinzu! */}
        {users.map(user => (
          <li>
            <strong>{user.name}</strong> - {user.role}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
```

2. Füge den korrekten `key` hinzu, sodass keine Warnung mehr erscheint.

3. **Bonus:** Erstelle eine `UserCard`-Komponente und rendere sie für jeden User:

```javascript
// Die UserCard soll so aussehen:
function UserCard({ user }) {
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.role}</p>
    </div>
  );
}
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/UserList.jsx

function UserCard({ user }) {
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.role}</p>
    </div>
  );
}

function UserList() {
  const users = [
    { id: 1, name: 'Max Mustermann', role: 'Developer' },
    { id: 2, name: 'Anna Schmidt', role: 'Designer' },
    { id: 3, name: 'Tom Weber', role: 'Manager' },
    { id: 4, name: 'Lisa Braun', role: 'Developer' }
  ];

  return (
    <div className="user-list">
      <h2>Team-Mitglieder</h2>

      {/* Variante 1: Einfache Liste */}
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <strong>{user.name}</strong> - {user.role}
          </li>
        ))}
      </ul>

      {/* Variante 2: Mit UserCard-Komponente */}
      <div className="user-cards">
        {users.map(user => (
          <UserCard key={user.id} user={user} />
        ))}
      </div>
    </div>
  );
}

export default UserList;
```

> **Wichtig:** Der `key` muss immer auf dem äußersten Element innerhalb von `map()` sein – hier also auf `<li>` oder `<UserCard>`, nicht auf einem inneren Element!

</details>

---

## Teil 5: Daten aus JSON laden

### Daten in separater Datei

Für größere Datenmengen ist es sinnvoll, die Daten auszulagern:

```javascript
// src/data/users.json
[
  { "id": 1, "name": "Alice", "profession": "Developer" },
  { "id": 2, "name": "Bob", "profession": "Designer" },
  { "id": 3, "name": "Charlie", "profession": "Manager" }
]
```

### JSON importieren

```javascript
// In deiner Komponente (z.B. src/components/UserList.jsx)
// Der Pfad hängt davon ab, wo deine Komponente liegt:
// - Komponente in src/           → import from './data/users.json'
// - Komponente in src/components/ → import from '../data/users.json'

import users from '../data/users.json';

function UserList() {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} - {user.profession}
        </li>
      ))}
    </ul>
  );
}
```

### Übung 5: Daten aus JSON laden

> **Ziel:** Externe Daten in React anzeigen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine Komponente Daten aus einer JSON-Datei anzeigt

**Aufgabe:**

1. Erstelle einen Ordner `src/data/` und darin eine Datei `products.json`:

```json
[
  {
    "id": 1,
    "name": "Laptop Pro",
    "price": 999.99,
    "category": "Elektronik"
  },
  {
    "id": 2,
    "name": "Wireless Kopfhörer",
    "price": 149.99,
    "category": "Audio"
  },
  {
    "id": 3,
    "name": "Smart Watch",
    "price": 299.99,
    "category": "Wearables"
  },
  {
    "id": 4,
    "name": "USB-C Hub",
    "price": 49.99,
    "category": "Zubehör"
  }
]
```

2. Erstelle eine Komponente `src/components/ProductList.jsx`:

```javascript
// src/components/ProductList.jsx

// Aufgabe: Importiere die Produkte aus der JSON-Datei
// import products from ???

function ProductList() {
  // Aufgabe: Rendere die Produkte als Liste
  // Zeige Name, Preis (formatiert) und Kategorie an

  return (
    <div className="product-list">
      <h2>Unsere Produkte</h2>
      {/* Dein Code hier */}
    </div>
  );
}

export default ProductList;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/ProductList.jsx
import products from '../data/products.json';

function ProductList() {
  return (
    <div className="product-list">
      <h2>Unsere Produkte ({products.length})</h2>

      <ul>
        {products.map(product => (
          <li key={product.id}>
            <strong>{product.name}</strong>
            <span className="price"> - {product.price.toFixed(2)} €</span>
            <span className="category"> ({product.category})</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
```

</details>

---

## Teil 6: Grids erstellen

### Von Liste zu Grid

Statt einer vertikalen Liste kannst du Elemente auch als Grid anzeigen:

```javascript
function UsersGrid() {
  const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
    { id: 3, name: 'Charlie' },
    { id: 4, name: 'Diana' }
  ];

  return (
    <div className="grid">
      {users.map(user => (
        <div key={user.id} className="grid-item">
          {user.name}
        </div>
      ))}
    </div>
  );
}
```

### CSS für Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);  /* 2 Spalten */
  gap: 16px;
  padding: 16px;
}

.grid-item {
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-align: center;
}

/* Responsive: Auf größeren Bildschirmen mehr Spalten */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);  /* 4 Spalten */
  }
}
```

### Übung 6: Produkt-Grid

> **Ziel:** Produkte als Grid anzeigen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine Produkte als Grid angezeigt werden

**Aufgabe:**

1. Erstelle eine Komponente `src/components/ProductGrid.jsx`:

```javascript
// src/components/ProductGrid.jsx
import products from '../data/products.json';

function ProductGrid() {
  return (
    <div className="product-grid">
      <h2>Produkte</h2>

      {/* Aufgabe: Rendere die Produkte als Grid */}
      <div className="grid">
        {/* Dein Code hier */}
      </div>
    </div>
  );
}

export default ProductGrid;
```

2. Füge CSS in `App.css` hinzu:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  padding: 16px;
}

.product-card {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
  text-align: center;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.product-card h3 {
  margin: 0 0 8px 0;
}

.product-card .price {
  font-size: 24px;
  font-weight: bold;
  color: #2ecc71;
}

.product-card .category {
  display: inline-block;
  margin-top: 8px;
  padding: 4px 12px;
  background: #3498db;
  color: white;
  border-radius: 20px;
  font-size: 12px;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/ProductGrid.jsx
import products from '../data/products.json';

function ProductGrid() {
  return (
    <div className="product-grid">
      <h2>Produkte ({products.length})</h2>

      <div className="grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <h3>{product.name}</h3>
            <p className="price">{product.price.toFixed(2)} €</p>
            <span className="category">{product.category}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductGrid;
```

</details>

---

## Teil 7: Konditionales Rendering

### Elemente bedingt anzeigen

In React gibt es mehrere Wege, Inhalte bedingt anzuzeigen:

### 1. Logisches UND (&&)

Zeigt etwas nur an, wenn die Bedingung `true` ist:

```javascript
{isLoggedIn && <Dashboard />}
// Wenn isLoggedIn true → Dashboard anzeigen
// Wenn isLoggedIn false → nichts anzeigen
```

### 2. Ternärer Operator (? :)

Zeigt eins von zwei Elementen an:

```javascript
{isLoggedIn
  ? <Dashboard />    // Wenn true
  : <LoginScreen />  // Wenn false
}
```

### 3. Logisches ODER (||) für Fallbacks

Zeigt einen Fallback wenn der Wert fehlt:

```javascript
{user.nickname || 'Anonymer Nutzer'}
// Wenn nickname vorhanden → nickname anzeigen
// Wenn nickname fehlt → "Anonymer Nutzer" anzeigen
```

### 4. Early Returns

Für größere bedingte Bereiche:

```javascript
function UserProfile({ user }) {
  // Fehlerfall zuerst abfangen
  if (!user) {
    return <p>Kein Benutzer gefunden.</p>;
  }

  // Erfolgsfall
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

### Was wird gerendert (und was nicht)?

```javascript
// Diese Werte rendern NICHTS:
{null}          // → nichts
{undefined}     // → nichts
{false}         // → nichts
{[]}            // → nichts (leeres Array)
{<></>}         // → nichts (leeres Fragment)

// Diese Werte WERDEN gerendert:
{0}             // → "0" (Achtung!)
{""}            // → "" (leerer String, unsichtbar)
{" "}           // → " " (Leerzeichen)
```

> **Häufiger Fehler:** `{count && <span>{count}</span>}` zeigt "0" an wenn count = 0, weil 0 gerendert wird! Besser: `{count > 0 && <span>{count}</span>}`

### Arrays direkt in JSX rendern

Wenn du ein Array direkt in JSX einfügst, wird es mit Kommas getrennt ausgegeben:

```javascript
function Demo() {
  const numbers = [1, 2, 3, 4];

  return (
    <div>
      {/* Ausgabe: "1,2,3,4" – das Array wird via toString() umgewandelt! */}
      <p>Direkt: {numbers}</p>

      {/* So macht man es richtig – mit map(): */}
      <p>Mit map: {numbers.map(n => <span key={n}>{n} </span>)}</p>
    </div>
  );
}
```

> **Warum passiert das?** Arrays in JSX werden implizit zu Strings konvertiert (`toString()`), was die Kommas erzeugt. Mit `map()` erzeugst du stattdessen ein Array von JSX-Elementen, das React korrekt rendert – ohne Kommas!

### Übung 7: Konditionales Rendering

> **Ziel:** Inhalte bedingt anzeigen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Deine Komponente verschiedene Zustände korrekt anzeigt

**Aufgabe:**

1. Erstelle eine Komponente `src/components/ProductCard.jsx`:

```javascript
// src/components/ProductCard.jsx

function ProductCard({ product }) {
  const { name, price, originalPrice, inStock, isNew, isSale } = product;

  // Robuste Rabatt-Berechnung: nur wenn originalPrice > price
  const hasDiscount = typeof originalPrice === 'number' && originalPrice > price;
  const discount = hasDiscount
    ? Math.round((1 - price / originalPrice) * 100)
    : 0;

  return (
    <div className="product-card">
      {/* Aufgabe 1: Zeige "NEU" Badge wenn isNew true ist */}
      {/* Aufgabe 2: Zeige "SALE" Badge wenn isSale true ist */}

      <h3>{name}</h3>

      <div className="price-info">
        <span className="price">{price.toFixed(2)} €</span>

        {/* Aufgabe 3: Zeige originalPrice durchgestrichen wenn hasDiscount true */}
        {/* Aufgabe 4: Zeige Rabatt-Prozent wenn hasDiscount true */}
      </div>

      {/* Aufgabe 5: Zeige "Ausverkauft" ODER "Auf Lager" je nach inStock */}
    </div>
  );
}

export default ProductCard;
```

2. Erstelle Test-Daten und verwende die Komponente:

```javascript
// In App.jsx
const testProduct = {
  name: "Wireless Kopfhörer",
  price: 79.99,
  originalPrice: 129.99,
  inStock: true,
  isNew: false,
  isSale: true
};

<ProductCard product={testProduct} />
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/ProductCard.jsx

function ProductCard({ product }) {
  const { name, price, originalPrice, inStock, isNew, isSale } = product;

  // Robuste Rabatt-Berechnung: nur wenn originalPrice > price
  const hasDiscount = typeof originalPrice === 'number' && originalPrice > price;
  const discount = hasDiscount
    ? Math.round((1 - price / originalPrice) * 100)
    : 0;

  return (
    <div className={`product-card ${!inStock ? 'out-of-stock' : ''}`}>
      {/* Badges */}
      <div className="badges">
        {isNew && <span className="badge badge-new">NEU</span>}
        {isSale && <span className="badge badge-sale">SALE</span>}
      </div>

      <h3>{name}</h3>

      <div className="price-info">
        <span className="price">{price.toFixed(2)} €</span>

        {/* Originalpreis und Rabatt (nur wenn tatsächlich reduziert) */}
        {hasDiscount && (
          <>
            <span className="original-price">{originalPrice.toFixed(2)} €</span>
            <span className="discount">-{discount}%</span>
          </>
        )}
      </div>

      {/* Verfügbarkeit */}
      <p className="stock-status">
        {inStock
          ? <span className="in-stock">Auf Lager</span>
          : <span className="out-of-stock">Ausverkauft</span>
        }
      </p>
    </div>
  );
}

export default ProductCard;
```

**CSS dazu:**

```css
.product-card {
  position: relative;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
}

.product-card.out-of-stock {
  opacity: 0.6;
}

.badges {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.badge-new {
  background: #2ecc71;
  color: white;
}

.badge-sale {
  background: #e74c3c;
  color: white;
}

.price-info {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 12px 0;
}

.price {
  font-size: 24px;
  font-weight: bold;
  color: #2ecc71;
}

.original-price {
  text-decoration: line-through;
  color: #999;
}

.discount {
  background: #e74c3c;
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
}

.in-stock {
  color: #2ecc71;
}

.out-of-stock {
  color: #e74c3c;
}
```

</details>

---

## Teil 8: Praxis - Produkt-Katalog

Zeit, alles zusammen anzuwenden!

> **Ziel:** Ein vollständiger Produkt-Katalog mit Listen, Keys und konditionellem Rendering
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Der Katalog alle Produkte als Grid mit Badges anzeigt

### Aufgabe: Vollständiger Produkt-Katalog

Erstelle einen Produkt-Katalog mit:

1. Produkte aus JSON-Datei laden
2. Produkte als Grid anzeigen
3. Badges für "Neu", "Sale", "Bestseller"
4. Preise mit optionalem Rabatt
5. Lagerbestand-Anzeige

**Erweitere deine `products.json`:**

```json
[
  {
    "id": 1,
    "name": "Laptop Pro",
    "price": 999.99,
    "originalPrice": 1299.99,
    "category": "Elektronik",
    "inStock": true,
    "badges": ["sale", "bestseller"]
  },
  {
    "id": 2,
    "name": "Wireless Kopfhörer",
    "price": 149.99,
    "category": "Audio",
    "inStock": true,
    "badges": ["new"]
  },
  {
    "id": 3,
    "name": "Smart Watch",
    "price": 299.99,
    "originalPrice": 399.99,
    "category": "Wearables",
    "inStock": false,
    "badges": ["sale"]
  },
  {
    "id": 4,
    "name": "USB-C Hub",
    "price": 49.99,
    "category": "Zubehör",
    "inStock": true,
    "badges": []
  },
  {
    "id": 5,
    "name": "Mechanische Tastatur",
    "price": 179.99,
    "category": "Zubehör",
    "inStock": true,
    "badges": ["new", "bestseller"]
  },
  {
    "id": 6,
    "name": "4K Monitor",
    "price": 449.99,
    "originalPrice": 549.99,
    "category": "Elektronik",
    "inStock": true,
    "badges": ["sale"]
  }
]
```

**Komponenten-Struktur:**

```
src/
├── components/
│   ├── ProductCatalog.jsx    # Hauptkomponente
│   ├── ProductCard.jsx       # Einzelnes Produkt
│   └── Badge.jsx             # Badge-Komponente
├── data/
│   └── products.json
└── App.jsx
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Badge.jsx:**

```javascript
function Badge({ type }) {
  const badgeConfig = {
    new: { text: 'NEU', color: 'green' },
    sale: { text: 'SALE', color: 'red' },
    bestseller: { text: 'BESTSELLER', color: 'orange' }
  };

  const config = badgeConfig[type];
  if (!config) return null;

  return (
    <span className={`badge badge-${config.color}`}>
      {config.text}
    </span>
  );
}

export default Badge;
```

**src/components/ProductCard.jsx:**

```javascript
import Badge from './Badge';

function ProductCard({ product }) {
  const { id, name, price, originalPrice, category, inStock, badges } = product;

  // Robuste Rabatt-Berechnung: nur wenn originalPrice > price
  const hasDiscount = typeof originalPrice === 'number' && originalPrice > price;
  const discount = hasDiscount
    ? Math.round((1 - price / originalPrice) * 100)
    : 0;

  return (
    <div className={`product-card ${!inStock ? 'out-of-stock' : ''}`}>
      {/* Badges */}
      {badges.length > 0 && (
        <div className="badges">
          {badges.map(badge => (
            <Badge key={`${id}-${badge}`} type={badge} />
          ))}
        </div>
      )}

      <h3>{name}</h3>
      <span className="category">{category}</span>

      <div className="price-info">
        <span className="price">{price.toFixed(2)} €</span>
        {hasDiscount && (
          <>
            <span className="original-price">{originalPrice.toFixed(2)} €</span>
            <span className="discount">-{discount}%</span>
          </>
        )}
      </div>

      <p className="stock-status">
        {inStock
          ? <span className="in-stock">✓ Auf Lager</span>
          : <span className="sold-out">✗ Ausverkauft</span>
        }
      </p>
    </div>
  );
}

export default ProductCard;
```

**src/components/ProductCatalog.jsx:**

```javascript
import products from '../data/products.json';
import ProductCard from './ProductCard';

function ProductCatalog() {
  const availableCount = products.filter(p => p.inStock).length;

  return (
    <div className="product-catalog">
      <header className="catalog-header">
        <h1>Unser Sortiment</h1>
        <p>{products.length} Produkte ({availableCount} verfügbar)</p>
      </header>

      <div className="product-grid">
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default ProductCatalog;
```

**CSS:**

```css
.product-catalog {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.catalog-header {
  text-align: center;
  margin-bottom: 30px;
}

.catalog-header h1 {
  margin: 0;
}

.catalog-header p {
  color: #666;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}

.product-card {
  position: relative;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
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

.badges {
  display: flex;
  gap: 6px;
  margin-bottom: 12px;
}

.badge {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: bold;
  text-transform: uppercase;
}

.badge-green { background: #2ecc71; color: white; }
.badge-red { background: #e74c3c; color: white; }
.badge-orange { background: #f39c12; color: white; }

.product-card h3 {
  margin: 0 0 8px 0;
}

.category {
  display: inline-block;
  padding: 4px 12px;
  background: #ecf0f1;
  border-radius: 20px;
  font-size: 12px;
  color: #666;
}

.price-info {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 16px 0;
}

.price {
  font-size: 24px;
  font-weight: bold;
  color: #2ecc71;
}

.original-price {
  text-decoration: line-through;
  color: #999;
  font-size: 14px;
}

.discount {
  background: #e74c3c;
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.stock-status {
  margin: 0;
  font-size: 14px;
}

.in-stock { color: #27ae60; }
.sold-out { color: #e74c3c; }
```

</details>

---

## Teil 9: Praxis - Todo-Liste mit Filter

Eine weitere praktische Übung!

> **Ziel:** Eine Todo-Liste mit Filtern und konditionellem Rendering
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Du Todos filtern und anzeigen kannst

### Aufgabe: Todo-Liste mit Filtern

Erstelle eine Todo-App mit:

1. Liste von Todos anzeigen
2. Filter: Alle / Offen / Erledigt
3. Leere-Liste-Meldung wenn keine Todos
4. Anzahl der offenen Todos anzeigen

**Starter-Code:**

```javascript
// src/components/TodoList.jsx
import { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'React lernen', completed: true },
    { id: 2, text: 'Projekt erstellen', completed: false },
    { id: 3, text: 'Tests schreiben', completed: false },
    { id: 4, text: 'Dokumentation erstellen', completed: true },
    { id: 5, text: 'Code Review', completed: false }
  ]);

  const [filter, setFilter] = useState('all'); // 'all', 'open', 'completed'

  // Aufgabe 1: Filtere die Todos basierend auf dem aktuellen Filter
  const filteredTodos = // ???

  // Aufgabe 2: Zähle die offenen Todos
  const openCount = // ???

  // Aufgabe 3: Toggle Todo-Status
  function toggleTodo(id) {
    // ???
  }

  return (
    <div className="todo-list">
      <h2>Meine Todos</h2>

      {/* Aufgabe 4: Zeige Anzahl offener Todos */}
      <p className="todo-count">
        {/* ??? */}
      </p>

      {/* Filter-Buttons */}
      <div className="filters">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          Alle
        </button>
        <button
          className={filter === 'open' ? 'active' : ''}
          onClick={() => setFilter('open')}
        >
          Offen
        </button>
        <button
          className={filter === 'completed' ? 'active' : ''}
          onClick={() => setFilter('completed')}
        >
          Erledigt
        </button>
      </div>

      {/* Aufgabe 5: Zeige Meldung wenn keine Todos (nach Filter) */}
      {/* Aufgabe 6: Rendere die gefilterten Todos */}

    </div>
  );
}

export default TodoList;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/TodoList.jsx
import { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'React lernen', completed: true },
    { id: 2, text: 'Projekt erstellen', completed: false },
    { id: 3, text: 'Tests schreiben', completed: false },
    { id: 4, text: 'Dokumentation erstellen', completed: true },
    { id: 5, text: 'Code Review', completed: false }
  ]);

  const [filter, setFilter] = useState('all');

  // Gefilterte Todos
  const filteredTodos = todos.filter(todo => {
    if (filter === 'open') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true; // 'all'
  });

  // Anzahl offener Todos
  const openCount = todos.filter(todo => !todo.completed).length;

  // Todo-Status umschalten
  function toggleTodo(id) {
    setTodos(prevTodos =>
      prevTodos.map(todo =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    );
  }

  return (
    <div className="todo-list">
      <h2>Meine Todos</h2>

      <p className="todo-count">
        {openCount === 0
          ? 'Alle Aufgaben erledigt! 🎉'
          : `${openCount} ${openCount === 1 ? 'Aufgabe' : 'Aufgaben'} offen`
        }
      </p>

      <div className="filters">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          Alle ({todos.length})
        </button>
        <button
          className={filter === 'open' ? 'active' : ''}
          onClick={() => setFilter('open')}
        >
          Offen ({openCount})
        </button>
        <button
          className={filter === 'completed' ? 'active' : ''}
          onClick={() => setFilter('completed')}
        >
          Erledigt ({todos.length - openCount})
        </button>
      </div>

      {/* Leere-Liste-Meldung */}
      {filteredTodos.length === 0 ? (
        <p className="empty-message">
          {filter === 'open' && 'Keine offenen Aufgaben.'}
          {filter === 'completed' && 'Noch keine Aufgaben erledigt.'}
          {filter === 'all' && 'Keine Aufgaben vorhanden.'}
        </p>
      ) : (
        <ul className="todos">
          {filteredTodos.map(todo => (
            <li
              key={todo.id}
              className={todo.completed ? 'completed' : ''}
            >
              <label>
                <input
                  type="checkbox"
                  checked={todo.completed}
                  onChange={() => toggleTodo(todo.id)}
                />
                <span>{todo.text}</span>
              </label>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TodoList;
```

**CSS:**

```css
.todo-list {
  max-width: 500px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #ddd;
  border-radius: 12px;
  background: white;
}

.todo-count {
  color: #666;
  margin-bottom: 16px;
}

.filters {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.filters button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 20px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}

.filters button:hover {
  background: #f5f5f5;
}

.filters button.active {
  background: #3498db;
  color: white;
  border-color: #3498db;
}

.todos {
  list-style: none;
  padding: 0;
  margin: 0;
}

.todos li {
  padding: 12px;
  border-bottom: 1px solid #eee;
}

.todos li:last-child {
  border-bottom: none;
}

.todos li.completed span {
  text-decoration: line-through;
  color: #999;
}

.todos label {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.todos input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.empty-message {
  text-align: center;
  color: #999;
  font-style: italic;
  padding: 20px;
}
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **map()** | Array transformieren | `items.map(item => ...)` |
| **Arrow Functions** | Kurzschreibweise für Funktionen | `x => x * 2` |
| **Listen rendern** | Array zu JSX-Elementen | `{items.map(i => <li>{i}</li>)}` |
| **Keys** | Eindeutige Identifikatoren | `key={item.id}` |
| **JSON import** | Daten aus Datei laden | `import data from './data.json'` |
| **Grids** | Listen als Grid anzeigen | `display: grid` |
| **&& Operator** | Bedingtes Anzeigen | `{isActive && <Badge />}` |
| **Ternärer Operator** | Entweder/Oder | `{a ? <A /> : <B />}` |
| **\|\| Operator** | Fallback-Werte | `{name \|\| 'Anonym'}` |

### Listen auf einen Blick

```javascript
// Array zu Liste
function ItemList({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

### Konditionales Rendering auf einen Blick

```javascript
// && für "wenn dann"
{isLoggedIn && <Dashboard />}

// ? : für "wenn dann sonst"
{isLoggedIn ? <Dashboard /> : <Login />}

// || für Fallback
{user.name || 'Anonymer Nutzer'}

// Early Return für Fehlerfälle
if (!data) return <p>Keine Daten</p>;
return <DataDisplay data={data} />;
```

### Key-Regeln auf einen Blick

```javascript
// ✅ RICHTIG - Stabile ID
{users.map(user => <User key={user.id} />)}

// ✅ OK - Eindeutiger String
{emails.map(email => <Item key={email} />)}

// ⚠️ NUR bei wirklich statischen Listen (kein Sortieren/Einfügen/Löschen!)
{weekdays.map((day, index) => <Day key={index} />)}

// ❌ FALSCH - Random (ändert sich bei jedem Render!)
{items.map(item => <Item key={Math.random()} />)}

// ❌ FALSCH - Index bei dynamischen Listen (Bug-Gefahr!)
{todos.map((todo, index) => <TodoItem key={index} />)}
```

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du verstehst, wie `map()` funktioniert
- [ ] Du kannst Arrow Functions in verschiedenen Varianten schreiben
- [ ] Du kannst Arrays in React als Listen rendern
- [ ] Du verstehst, warum Keys wichtig sind
- [ ] Du weißt, wann welche Art von Key geeignet ist
- [ ] Du kannst Daten aus JSON-Dateien importieren
- [ ] Du kannst Listen als Grid anzeigen
- [ ] Du kennst die verschiedenen Methoden für konditionales Rendering
- [ ] Du weißt, welche Werte in JSX gerendert werden und welche nicht

**Alles abgehakt?** Du bist bereit für fortgeschrittene React-Patterns!
