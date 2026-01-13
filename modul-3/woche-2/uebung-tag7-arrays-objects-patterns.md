# Arrays, Objects & Moderne Patterns - Praktische Übungen

## Übersicht

Listen & Dictionaries kennst du bereits aus Python – heute lernst du die JavaScript-Varianten und die wichtigsten Patterns für React!

In dieser Übung vertiefst du dein Wissen über:
- **Arrays** - Python-Listen in JavaScript-Syntax mit mächtigen Methoden
- **map(), filter(), find()** - Statt List Comprehensions
- **Spread Operator (...)** - Ähnlich wie */**, aber vielseitiger
- **Destructuring** - Elegantes Entpacken (wie Tuple Unpacking)
- **Objects** - Python-Dicts mit Dot Notation
- **Immutability** - Warum React neue Kopien braucht
- **ES6 Modules** - import/export (wie Python-Imports)

Diese Übung bereitet dich auf React vor – alle diese Patterns wirst du dort täglich verwenden!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Von Python zu JavaScript | 5 min (lesen) |
| **Teil 1** | Arrays: Listen von Werten | 10 min |
| **Teil 2** | Basis Array-Methoden | 10 min |
| **Teil 3** | Spread Operator für Arrays | 15 min |
| **Teil 4** | Array Destructuring | 10 min |
| **Teil 5** | Array.map() – Transformieren | 15 min |
| **Teil 6** | Array.filter() – Filtern | 15 min |
| **Teil 7** | Array.find() & findIndex() | 10 min |
| **Teil 8** | Methoden verketten (Chaining) | 15 min |
| **Teil 9** | Objects: Key-Value-Paare | 15 min |
| **Teil 10** | Spread Operator für Objects | 15 min |
| **Teil 11** | Object Destructuring | 15 min |
| **Teil 12** | Immutability: Daten nicht ändern! | 15 min |
| **Teil 13** | ES6 Modules: import/export | 15 min |
| **Teil 14** | Praktische Gesamtübung | 30 min |
| | **Gesamt** | **ca. 3-4 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 90-120 Minuten die wichtigsten Konzepte:**

1. **Teil 5** - Array.map() - *Das wichtigste für React*
2. **Teil 6** - Array.filter() - *Daten filtern*
3. **Teil 8** - Chaining - *Methoden kombinieren*
4. **Teil 10** - Spread für Objects - *State Updates*
5. **Teil 11** - Object Destructuring - *Props & State*
6. **Teil 12** - Immutability - *React-Grundprinzip*

Die anderen Teile kannst du später nachholen oder als Referenz nutzen.

---

## Rückblick: Python-Kenntnisse → JavaScript

### Die Herausforderung

Du kannst das in Python – wie geht das in JavaScript?

```python
# Python: List Comprehension mit Filter
users = [{"name": "Max", "age": 25}, {"name": "Anna", "age": 30}]
names = [u["name"] for u in users if u["age"] > 20]
# Ergebnis: ["Max", "Anna"]
```

**Auflösung kommt am Ende dieser Übung – wenn du `map()` und `filter()` gelernt hast!**

### Was du schon kannst

| Python | JavaScript | Beispiel |
|--------|------------|----------|
| `liste = [1, 2, 3]` | `const arr = [1, 2, 3];` | Listen/Arrays |
| `dict = {"key": "value"}` | `const obj = { key: "value" };` | Dictionaries/Objects |
| `len(liste)` | `arr.length` | Länge ermitteln |
| `liste[0]` | `arr[0]` | Index-Zugriff |
| `dict["key"]` | `obj.key` oder `obj["key"]` | Property-Zugriff |
| `liste.append(x)` | `arr.push(x)` | Element hinzufügen |
| `[x*2 for x in liste]` | `arr.map(x => x * 2)` | Transformation |
| `[x for x in liste if x > 0]` | `arr.filter(x => x > 0)` | Filtern |

---

## Teil 1: Arrays – Listen von Werten

### Python: Liste = [] → JavaScript: Array = []

JS-Arrays funktionieren fast identisch zu Python-Listen. Die Syntax ist nahezu gleich!

### Array erstellen

```javascript
// Array-Literal (empfohlen)
const numbers = [1, 2, 3, 4, 5];
const names = ['Anna', 'Max', 'Lisa'];
const mixed = [1, 'zwei', true, null];

// Leeres Array
const empty = [];
```

### Elemente zugreifen

```javascript
const fruits = ['Apfel', 'Birne', 'Orange'];

fruits[0];        // 'Apfel'
fruits[2];        // 'Orange'
fruits.length;    // 3

// Letztes Element (modern)
fruits.at(-1);    // 'Orange'

// Python: fruits[-1] → JS: fruits.at(-1)
```

### Wissensfrage 1

Was ist der Unterschied zwischen `fruits[-1]` in Python und JavaScript?

<details>
<summary>Antwort anzeigen</summary>

**Python:** `fruits[-1]` gibt das letzte Element zurück.

**JavaScript:** `fruits[-1]` gibt `undefined` zurück! Negative Indizes funktionieren nicht mit der Bracket-Notation.

**Lösung in JavaScript:**
- `fruits[fruits.length - 1]` - klassischer Weg
- `fruits.at(-1)` - moderner Weg (ES2022)

</details>

### Übung 1: Arrays erstellen und zugreifen

> **Ziel:** Array-Syntax in JavaScript verstehen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du Arrays erstellen und auf Elemente zugreifen kannst

**Aufgabe:**

Öffne die Browser-Konsole (F12 → Console) und führe folgende Schritte aus:

```javascript
// 1. Erstelle ein Array mit 5 Programmiersprachen
const languages = // Dein Code hier

// 2. Gib das erste und letzte Element aus
console.log("Erste:", languages[0]);
console.log("Letzte:", languages.at(-1));

// 3. Gib die Länge des Arrays aus
console.log("Anzahl:", languages.length);

// 4. Erstelle ein Array mit verschiedenen Datentypen
const mixed = // Dein Code hier (String, Number, Boolean, null)
console.log(mixed);
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// 1. Array mit Programmiersprachen
const languages = ['JavaScript', 'Python', 'Java', 'C++', 'Ruby'];

// 2. Erstes und letztes Element
console.log("Erste:", languages[0]);     // "JavaScript"
console.log("Letzte:", languages.at(-1)); // "Ruby"

// 3. Länge
console.log("Anzahl:", languages.length); // 5

// 4. Mixed Array
const mixed = ['Hallo', 42, true, null];
console.log(mixed); // ['Hallo', 42, true, null]
```

</details>

---

## Teil 2: Basis Array-Methoden

Arrays haben viele eingebaute Methoden – hier die wichtigsten für den Anfang:

### push() / pop() – Am Ende hinzufügen/entfernen

```javascript
const arr = [1, 2, 3];
arr.push(4);    // [1, 2, 3, 4] - Fügt am Ende hinzu
arr.pop();      // [1, 2, 3]   - Entfernt letztes Element
```

**Python-Vergleich:** `list.append()` = `push()`, `list.pop()` = `pop()`

### unshift() / shift() – Am Anfang hinzufügen/entfernen

```javascript
const arr = [1, 2, 3];
arr.unshift(0); // [0, 1, 2, 3] - Fügt am Anfang hinzu
arr.shift();    // [1, 2, 3]    - Entfernt erstes Element
```

### includes() / indexOf() – Suchen im Array

```javascript
const arr = ['a', 'b', 'c'];
arr.includes('b');  // true  - Ist 'b' enthalten?
arr.indexOf('b');   // 1     - An welcher Position?
arr.indexOf('x');   // -1    - Nicht gefunden
```

**Python-Vergleich:** `'b' in arr` = `arr.includes('b')`

### ⚠️ Wichtiger Hinweis für React

Diese Methoden (`push`, `pop`, `unshift`, `shift`) **ändern das Original-Array**!

```javascript
const arr = [1, 2, 3];
arr.push(4);  // arr ist jetzt [1, 2, 3, 4] - MUTIERT!
```

**In React vermeiden wir Mutationen!** Stattdessen erstellen wir neue Arrays mit dem Spread Operator (siehe Teil 3).

### Übung 2: Array-Methoden testen

> **Ziel:** Basis-Methoden für Arrays kennenlernen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du weißt, welche Methoden das Original ändern

**Aufgabe:**

Teste in der Browser-Konsole:

```javascript
// 1. Erstelle ein Array
const colors = ['rot', 'grün', 'blau'];

// 2. Füge 'gelb' am Ende hinzu
// Dein Code hier

// 3. Füge 'schwarz' am Anfang hinzu
// Dein Code hier

// 4. Entferne das letzte Element
// Dein Code hier

// 5. Prüfe ob 'grün' enthalten ist
// Dein Code hier

// 6. Finde den Index von 'rot'
// Dein Code hier

console.log(colors);
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const colors = ['rot', 'grün', 'blau'];

colors.push('gelb');      // ['rot', 'grün', 'blau', 'gelb']
colors.unshift('schwarz'); // ['schwarz', 'rot', 'grün', 'blau', 'gelb']
colors.pop();              // ['schwarz', 'rot', 'grün', 'blau']

console.log(colors.includes('grün')); // true
console.log(colors.indexOf('rot'));   // 1

console.log(colors); // ['schwarz', 'rot', 'grün', 'blau']
```

**Beachte:** Alle Methoden haben das Original-Array `colors` verändert!

</details>

---

## Teil 3: Spread Operator für Arrays: ...

Der Spread Operator `...` "entpackt" ein Array – ähnlich wie `*args` in Python, aber vielseitiger!

### Array kopieren

```javascript
const original = [1, 2, 3];
const copy = [...original];  // [1, 2, 3]

// original und copy sind UNABHÄNGIG!
original.push(4);  // original: [1, 2, 3, 4]
console.log(copy); // copy bleibt: [1, 2, 3]
```

**Python-Vergleich:** `copy = original[:]` oder `copy = list(original)`

### Arrays kombinieren

```javascript
const arr1 = [1, 2];
const arr2 = [3, 4];

const combined = [...arr1, ...arr2];     // [1, 2, 3, 4]
const withNew = [...arr1, 'X', ...arr2]; // [1, 2, 'X', 3, 4]
```

### Element hinzufügen (immutable)

```javascript
const items = ['a', 'b', 'c'];

// FALSCH (mutiert):
// items.push('d');

// RICHTIG (neues Array):
const newItems = [...items, 'd'];  // ['a', 'b', 'c', 'd']
// items bleibt unverändert: ['a', 'b', 'c']
```

### Element entfernen (immutable)

```javascript
const items = ['a', 'b', 'c', 'd'];
const indexToRemove = 2;

// Neues Array ohne Element an Index 2:
const filtered = items.filter((_, index) => index !== indexToRemove);
// ['a', 'b', 'd']
```

### Wissensfrage 2

Was ist der Unterschied zwischen diesen beiden Zeilen?

```javascript
const copy1 = original;
const copy2 = [...original];
```

<details>
<summary>Antwort anzeigen</summary>

**`copy1 = original`:**
- Erstellt nur eine **Referenz** auf das gleiche Array
- Änderungen an `copy1` ändern auch `original`!
- Das ist wie in Python: `list2 = list1`

**`copy2 = [...original]`:**
- Erstellt eine **echte Kopie** (Shallow Copy)
- `copy2` und `original` sind unabhängig
- Das ist wie in Python: `list2 = list1[:]`

```javascript
const original = [1, 2, 3];

const copy1 = original;
copy1.push(4);
console.log(original); // [1, 2, 3, 4] - AUCH geändert!

const original2 = [1, 2, 3];
const copy2 = [...original2];
copy2.push(4);
console.log(original2); // [1, 2, 3] - NICHT geändert!
```

</details>

### Übung 3: Spread Operator

> **Ziel:** Immutable Array-Operationen mit Spread beherrschen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Arrays kopieren und kombinieren kannst ohne das Original zu ändern

**Aufgabe:**

```javascript
const fruits = ['Apfel', 'Birne'];
const vegetables = ['Karotte', 'Brokkoli'];

// 1. Erstelle eine Kopie von fruits
const fruitsCopy = // Dein Code

// 2. Kombiniere fruits und vegetables
const food = // Dein Code

// 3. Füge 'Orange' zu fruits hinzu (OHNE das Original zu ändern!)
const moreFruits = // Dein Code

// 4. Erstelle ein neues Array mit 'Banane' am Anfang
const withBanana = // Dein Code

// 5. Prüfe: Ist fruits immer noch ['Apfel', 'Birne']?
console.log(fruits);
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const fruits = ['Apfel', 'Birne'];
const vegetables = ['Karotte', 'Brokkoli'];

// 1. Kopie erstellen
const fruitsCopy = [...fruits];
console.log(fruitsCopy); // ['Apfel', 'Birne']

// 2. Arrays kombinieren
const food = [...fruits, ...vegetables];
console.log(food); // ['Apfel', 'Birne', 'Karotte', 'Brokkoli']

// 3. Element hinzufügen (immutable)
const moreFruits = [...fruits, 'Orange'];
console.log(moreFruits); // ['Apfel', 'Birne', 'Orange']

// 4. Element am Anfang
const withBanana = ['Banane', ...fruits];
console.log(withBanana); // ['Banane', 'Apfel', 'Birne']

// 5. Original unverändert!
console.log(fruits); // ['Apfel', 'Birne'] ✓
```

</details>

---

## Teil 4: Array Destructuring

Destructuring extrahiert Werte aus Arrays – wie Tuple Unpacking in Python!

### Python-Vergleich

```python
# Python: Tuple Unpacking
first, second, third = ['rot', 'grün', 'blau']
```

```javascript
// JavaScript: Array Destructuring
const [first, second, third] = ['rot', 'grün', 'blau'];
// first='rot', second='grün', third='blau'
```

### Basis-Beispiel

```javascript
const colors = ['rot', 'grün', 'blau'];

// Mit Destructuring:
const [first, second, third] = colors;
// first='rot', second='grün', third='blau'

// Statt:
const first = colors[0];
const second = colors[1];
const third = colors[2];
```

### Element überspringen

```javascript
const nums = [1, 2, 3, 4, 5];

// Zweites Element überspringen:
const [first, , third] = nums;  // first=1, third=3

// Mehrere überspringen:
const [a, , , d] = nums;  // a=1, d=4
```

### Rest-Operator

```javascript
const nums = [1, 2, 3, 4, 5];

// Rest in ein Array sammeln:
const [head, ...rest] = nums;
// head=1, rest=[2, 3, 4, 5]

// Python-Äquivalent:
// head, *rest = [1, 2, 3, 4, 5]
```

### Default-Werte

```javascript
const arr = ['a'];

const [first, second = 'default'] = arr;
// first='a', second='default'
```

### Wo du das in React siehst

```javascript
// useState gibt ein Array mit 2 Elementen zurück!
const [count, setCount] = useState(0);
//     ↑         ↑
//   Wert   Setter-Funktion

// Das ist Destructuring!
// Equivalent zu:
// const stateArray = useState(0);
// const count = stateArray[0];
// const setCount = stateArray[1];
```

### Übung 4: Array Destructuring

> **Ziel:** Werte aus Arrays elegant extrahieren
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du Destructuring für useState-Pattern verstehst

**Aufgabe:**

```javascript
const coordinates = [10, 20, 30];
const rgb = [255, 128, 0];
const data = ['Header', 'Content1', 'Content2', 'Content3', 'Footer'];

// 1. Extrahiere x, y, z aus coordinates
const [x, y, z] = // Dein Code

// 2. Extrahiere nur red und blue (überspringe green)
const [red, , blue] = // Dein Code - Hinweis: Komma lässt Element aus

// 3. Extrahiere header und footer, rest in "content"
const [header, ...content] = // Dein Code
// Dann: const footer = content.pop() oder anderer Ansatz

// 4. Simuliere useState: Erstelle Array und destructure es
const myState = ['initialValue', () => console.log('setter called')];
const [value, setValue] = // Dein Code
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const coordinates = [10, 20, 30];
const rgb = [255, 128, 0];
const data = ['Header', 'Content1', 'Content2', 'Content3', 'Footer'];

// 1. x, y, z extrahieren
const [x, y, z] = coordinates;
console.log(x, y, z); // 10, 20, 30

// 2. red und blue (green überspringen)
const [red, , blue] = rgb;
console.log(red, blue); // 255, 0

// 3. header, content array, und footer
// Option A: Alles außer letztes in content
const [header, ...middle] = data;
const footer = data.at(-1);
const content = middle.slice(0, -1);
console.log(header);  // 'Header'
console.log(content); // ['Content1', 'Content2', 'Content3']
console.log(footer);  // 'Footer'

// 4. useState-Pattern simulieren
const myState = ['initialValue', () => console.log('setter called')];
const [value, setValue] = myState;
console.log(value);  // 'initialValue'
setValue();          // 'setter called'
```

</details>

---

## Teil 5: Array.map() – Transformieren

`map()` erstellt ein neues Array, indem es eine Funktion auf jedes Element anwendet.

### Python-Vergleich

```python
# Python: List Comprehension
numbers = [1, 2, 3, 4]
doubled = [n * 2 for n in numbers]  # [2, 4, 6, 8]
```

```javascript
// JavaScript: map()
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8]
```

### Zahlen transformieren

```javascript
const numbers = [1, 2, 3, 4];

const doubled = numbers.map(n => n * 2);
// [2, 4, 6, 8]

const squared = numbers.map(n => n * n);
// [1, 4, 9, 16]

const asStrings = numbers.map(n => `Nummer ${n}`);
// ['Nummer 1', 'Nummer 2', 'Nummer 3', 'Nummer 4']
```

### Objects transformieren

```javascript
const users = [
    { name: 'Max', age: 25 },
    { name: 'Anna', age: 30 }
];

// Nur die Namen extrahieren
const names = users.map(u => u.name);
// ['Max', 'Anna']

// Alter um 1 erhöhen (neues Array!)
const olderUsers = users.map(u => ({ ...u, age: u.age + 1 }));
// [{ name: 'Max', age: 26 }, { name: 'Anna', age: 31 }]
```

### map() mit Index

```javascript
const items = ['a', 'b', 'c'];

// Zweiter Parameter ist der Index
const indexed = items.map((item, index) => `${index}: ${item}`);
// ['0: a', '1: b', '2: c']
```

### Wichtig: map() gibt IMMER ein neues Array zurück

```javascript
const original = [1, 2, 3];
const doubled = original.map(n => n * 2);

console.log(original); // [1, 2, 3] - unverändert!
console.log(doubled);  // [2, 4, 6] - neues Array
```

### Übung 5: Array.map()

> **Ziel:** Daten mit map() transformieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du map() für Zahlen und Objects verwenden kannst

**Aufgabe:**

```javascript
const numbers = [1, 2, 3, 4, 5];
const products = [
    { name: 'Laptop', price: 999 },
    { name: 'Mouse', price: 29 },
    { name: 'Keyboard', price: 79 }
];

// 1. Verdreifache alle Zahlen
const tripled = // Dein Code

// 2. Erstelle Array mit "Zahl: X" Strings
const labeled = // Dein Code

// 3. Extrahiere nur die Produktnamen
const productNames = // Dein Code

// 4. Erstelle Array mit formatierten Preisen
// z.B. ['999 €', '29 €', '79 €']
const formattedPrices = // Dein Code

// 5. Erhöhe alle Preise um 10% (neues Array mit neuen Objects!)
const increasedPrices = // Dein Code
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const numbers = [1, 2, 3, 4, 5];
const products = [
    { name: 'Laptop', price: 999 },
    { name: 'Mouse', price: 29 },
    { name: 'Keyboard', price: 79 }
];

// 1. Verdreifachen
const tripled = numbers.map(n => n * 3);
console.log(tripled); // [3, 6, 9, 12, 15]

// 2. Mit Label
const labeled = numbers.map(n => `Zahl: ${n}`);
console.log(labeled); // ['Zahl: 1', 'Zahl: 2', ...]

// 3. Nur Namen
const productNames = products.map(p => p.name);
console.log(productNames); // ['Laptop', 'Mouse', 'Keyboard']

// 4. Formatierte Preise
const formattedPrices = products.map(p => `${p.price} €`);
console.log(formattedPrices); // ['999 €', '29 €', '79 €']

// 5. Preise erhöhen (immutable!)
const increasedPrices = products.map(p => ({
    ...p,
    price: Math.round(p.price * 1.1)
}));
console.log(increasedPrices);
// [{ name: 'Laptop', price: 1099 }, { name: 'Mouse', price: 32 }, ...]
console.log(products[0].price); // 999 - Original unverändert!
```

</details>

---

## Teil 6: Array.filter() – Filtern

`filter()` erstellt ein neues Array mit allen Elementen, die eine Bedingung erfüllen.

### Python-Vergleich

```python
# Python: List Comprehension mit Bedingung
numbers = [1, 2, 3, 4, 5, 6]
even = [n for n in numbers if n % 2 == 0]  # [2, 4, 6]
```

```javascript
// JavaScript: filter()
const numbers = [1, 2, 3, 4, 5, 6];
const even = numbers.filter(n => n % 2 === 0);  // [2, 4, 6]
```

### Zahlen filtern

```javascript
const numbers = [1, 2, 3, 4, 5, 6];

const even = numbers.filter(n => n % 2 === 0);
// [2, 4, 6]

const big = numbers.filter(n => n > 3);
// [4, 5, 6]

const small = numbers.filter(n => n <= 2);
// [1, 2]
```

### Objects filtern

```javascript
const products = [
    { name: 'Laptop', price: 999, inStock: true },
    { name: 'Mouse', price: 29, inStock: true },
    { name: 'Keyboard', price: 79, inStock: false },
    { name: 'Monitor', price: 299, inStock: true }
];

// Nur verfügbare Produkte
const available = products.filter(p => p.inStock);
// [Laptop, Mouse, Monitor]

// Produkte über 100€
const expensive = products.filter(p => p.price > 100);
// [Laptop, Monitor]

// Verfügbar UND unter 100€
const cheapAndAvailable = products.filter(p => p.inStock && p.price < 100);
// [Mouse]
```

### Strings filtern

```javascript
const words = ['apple', 'banana', 'cherry', 'date'];

// Wörter mit mehr als 5 Buchstaben
const long = words.filter(w => w.length > 5);
// ['banana', 'cherry']

// Wörter die mit 'a' beginnen
const startsWithA = words.filter(w => w.startsWith('a'));
// ['apple']
```

### Übung 6: Array.filter()

> **Ziel:** Daten mit filter() selektieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du komplexe Filter-Bedingungen schreiben kannst

**Aufgabe:**

```javascript
const users = [
    { name: 'Max', age: 25, active: true },
    { name: 'Anna', age: 17, active: true },
    { name: 'Tom', age: 32, active: false },
    { name: 'Lisa', age: 28, active: true },
    { name: 'Ben', age: 16, active: true }
];

// 1. Nur aktive User
const activeUsers = // Dein Code

// 2. Nur volljährige User (>= 18)
const adults = // Dein Code

// 3. Aktive UND volljährige User
const activeAdults = // Dein Code

// 4. User deren Name mit 'A' oder 'a' beginnt
const startsWithA = // Dein Code

// 5. User zwischen 20 und 30 Jahren
const twenties = // Dein Code
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const users = [
    { name: 'Max', age: 25, active: true },
    { name: 'Anna', age: 17, active: true },
    { name: 'Tom', age: 32, active: false },
    { name: 'Lisa', age: 28, active: true },
    { name: 'Ben', age: 16, active: true }
];

// 1. Aktive User
const activeUsers = users.filter(u => u.active);
console.log(activeUsers.map(u => u.name)); // ['Max', 'Anna', 'Lisa', 'Ben']

// 2. Volljährige
const adults = users.filter(u => u.age >= 18);
console.log(adults.map(u => u.name)); // ['Max', 'Tom', 'Lisa']

// 3. Aktiv UND volljährig
const activeAdults = users.filter(u => u.active && u.age >= 18);
console.log(activeAdults.map(u => u.name)); // ['Max', 'Lisa']

// 4. Name beginnt mit A
const startsWithA = users.filter(u => u.name.toLowerCase().startsWith('a'));
console.log(startsWithA.map(u => u.name)); // ['Anna']

// 5. Zwischen 20 und 30
const twenties = users.filter(u => u.age >= 20 && u.age <= 30);
console.log(twenties.map(u => u.name)); // ['Max', 'Lisa']
```

</details>

---

## Teil 7: Array.find() & findIndex()

`find()` gibt das **erste** passende Element zurück, `findIndex()` dessen Position.

### find() – Element finden

```javascript
const users = [
    { id: 1, name: 'Max' },
    { id: 2, name: 'Anna' },
    { id: 3, name: 'Lisa' }
];

const anna = users.find(u => u.name === 'Anna');
// { id: 2, name: 'Anna' }

const notFound = users.find(u => u.name === 'Tim');
// undefined
```

**Python-Vergleich:**
```python
# Python
anna = next((u for u in users if u["name"] == "Anna"), None)
```

### findIndex() – Position finden

```javascript
const nums = [10, 20, 30, 40];

const idx = nums.findIndex(n => n > 25);
// 2 (Index von 30)

const notIdx = nums.findIndex(n => n > 100);
// -1 (nicht gefunden)
```

### Unterschied: find() vs filter()

```javascript
const numbers = [1, 2, 3, 4, 5];

// find() gibt EIN Element zurück (oder undefined)
const firstBig = numbers.find(n => n > 2);
// 3

// filter() gibt ALLE als Array zurück
const allBig = numbers.filter(n => n > 2);
// [3, 4, 5]
```

### Wissensfrage 3

Was ist der Rückgabewert, wenn nichts gefunden wird?

```javascript
const arr = [1, 2, 3];
const result1 = arr.find(n => n > 10);
const result2 = arr.findIndex(n => n > 10);
const result3 = arr.filter(n => n > 10);
```

<details>
<summary>Antwort anzeigen</summary>

```javascript
const result1 = arr.find(n => n > 10);      // undefined
const result2 = arr.findIndex(n => n > 10); // -1
const result3 = arr.filter(n => n > 10);    // [] (leeres Array)
```

**Merke:**
- `find()` → `undefined` wenn nicht gefunden
- `findIndex()` → `-1` wenn nicht gefunden
- `filter()` → `[]` (leeres Array) wenn nichts passt

</details>

### Übung 7: find() und findIndex()

> **Ziel:** Einzelne Elemente in Arrays finden
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du den Unterschied zwischen find() und filter() verstehst

**Aufgabe:**

```javascript
const products = [
    { id: 1, name: 'Laptop', price: 999 },
    { id: 2, name: 'Mouse', price: 29 },
    { id: 3, name: 'Keyboard', price: 79 },
    { id: 4, name: 'Monitor', price: 299 }
];

// 1. Finde das Produkt mit id === 3
const product3 = // Dein Code

// 2. Finde den Index des Produkts mit name === 'Mouse'
const mouseIndex = // Dein Code

// 3. Finde das erste Produkt unter 100€
const cheapProduct = // Dein Code

// 4. Finde das Produkt mit id === 99 (existiert nicht)
const notFound = // Dein Code
console.log(notFound); // Was wird ausgegeben?
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const products = [
    { id: 1, name: 'Laptop', price: 999 },
    { id: 2, name: 'Mouse', price: 29 },
    { id: 3, name: 'Keyboard', price: 79 },
    { id: 4, name: 'Monitor', price: 299 }
];

// 1. Produkt mit id 3
const product3 = products.find(p => p.id === 3);
console.log(product3); // { id: 3, name: 'Keyboard', price: 79 }

// 2. Index von Mouse
const mouseIndex = products.findIndex(p => p.name === 'Mouse');
console.log(mouseIndex); // 1

// 3. Erstes günstiges Produkt
const cheapProduct = products.find(p => p.price < 100);
console.log(cheapProduct); // { id: 2, name: 'Mouse', price: 29 }

// 4. Nicht existierendes Produkt
const notFound = products.find(p => p.id === 99);
console.log(notFound); // undefined
```

</details>

---

## Teil 8: Methoden verketten (Chaining)

Da `map()` und `filter()` neue Arrays zurückgeben, können wir sie verketten!

### Beispiel: filter + map

```javascript
const products = [
    { name: 'Laptop', price: 999, inStock: true },
    { name: 'Mouse', price: 29, inStock: true },
    { name: 'Keyboard', price: 79, inStock: false },
    { name: 'Monitor', price: 299, inStock: true }
];

// Nur Namen von verfügbaren, günstigen Produkten
const available = products
    .filter(p => p.inStock)        // Nur verfügbare
    .filter(p => p.price < 500)    // Nur unter 500€
    .map(p => p.name)              // Nur Namen
    .sort();                       // Alphabetisch

console.log(available); // ['Monitor', 'Mouse']
```

### Python-Vergleich

```python
# Python: Alles in einer List Comprehension
available = sorted([
    p["name"]
    for p in products
    if p["inStock"] and p["price"] < 500
])
```

```javascript
// JavaScript: Verkettete Methoden
const available = products
    .filter(p => p.inStock)
    .filter(p => p.price < 500)
    .map(p => p.name)
    .sort();
```

### Tipps zum Chaining

1. **Jede Methode auf neue Zeile** → besser lesbar
2. **filter() vor map()** → effizienter (weniger Elemente zu transformieren)
3. **Reihenfolge ist wichtig!**

```javascript
// FALSCH: map() vor filter() - filter bekommt falsche Daten
const wrong = products
    .map(p => p.name)            // ['Laptop', 'Mouse', ...]
    .filter(p => p.inStock);     // FEHLER! p ist jetzt ein String!

// RICHTIG: filter() vor map()
const correct = products
    .filter(p => p.inStock)      // [{...}, {...}]
    .map(p => p.name);           // ['Laptop', 'Mouse', ...]
```

### Auflösung: Python → JavaScript

Jetzt kannst du die Aufgabe vom Anfang lösen!

**Python:**
```python
users = [{"name": "Max", "age": 25}, {"name": "Anna", "age": 30}]
names = [u["name"] for u in users if u["age"] > 20]
# ["Max", "Anna"]
```

**JavaScript:**
```javascript
const users = [{ name: "Max", age: 25 }, { name: "Anna", age: 30 }];
const names = users
    .filter(u => u.age > 20)
    .map(u => u.name);
// ["Max", "Anna"]
```

### Übung 8: Chaining

> **Ziel:** Methoden elegant verketten
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du komplexe Datenverarbeitungen mit Chaining lösen kannst

**Aufgabe:**

```javascript
const employees = [
    { name: 'Max', department: 'IT', salary: 60000, active: true },
    { name: 'Anna', department: 'HR', salary: 55000, active: true },
    { name: 'Tom', department: 'IT', salary: 70000, active: false },
    { name: 'Lisa', department: 'IT', salary: 65000, active: true },
    { name: 'Ben', department: 'Sales', salary: 50000, active: true }
];

// 1. Namen aller aktiven IT-Mitarbeiter
const activeIT = // Dein Code

// 2. Durchschnittsgehalt der aktiven Mitarbeiter
// Tipp: Verwende reduce() am Ende
const avgSalary = employees
    .filter(e => e.active)
    .map(e => e.salary)
    // .reduce(...) für Durchschnitt

// 3. Liste: "Name (Department)" für alle mit Gehalt > 55000
const highEarners = // Dein Code

// 4. Sortierte Liste aller Departments (ohne Duplikate)
// Tipp: [...new Set(array)] entfernt Duplikate
const departments = // Dein Code
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const employees = [
    { name: 'Max', department: 'IT', salary: 60000, active: true },
    { name: 'Anna', department: 'HR', salary: 55000, active: true },
    { name: 'Tom', department: 'IT', salary: 70000, active: false },
    { name: 'Lisa', department: 'IT', salary: 65000, active: true },
    { name: 'Ben', department: 'Sales', salary: 50000, active: true }
];

// 1. Aktive IT-Mitarbeiter
const activeIT = employees
    .filter(e => e.active)
    .filter(e => e.department === 'IT')
    .map(e => e.name);
console.log(activeIT); // ['Max', 'Lisa']

// 2. Durchschnittsgehalt
const salaries = employees
    .filter(e => e.active)
    .map(e => e.salary);
const avgSalary = salaries.reduce((sum, s) => sum + s, 0) / salaries.length;
console.log(avgSalary); // 57500

// 3. High Earners
const highEarners = employees
    .filter(e => e.salary > 55000)
    .map(e => `${e.name} (${e.department})`);
console.log(highEarners); // ['Max (IT)', 'Tom (IT)', 'Lisa (IT)']

// 4. Sortierte Departments ohne Duplikate
const departments = [...new Set(employees.map(e => e.department))].sort();
console.log(departments); // ['HR', 'IT', 'Sales']
```

</details>

---

## Teil 9: Objects – Key-Value-Paare

Objects speichern Daten als Schlüssel-Wert-Paare – wie Python Dictionaries!

### Python-Vergleich

```python
# Python Dictionary
user = {"name": "Max", "age": 25, "email": "max@example.com"}
print(user["name"])  # "Max"
```

```javascript
// JavaScript Object
const user = { name: "Max", age: 25, email: "max@example.com" };
console.log(user.name);  // "Max" - Dot Notation!
```

### Object erstellen

```javascript
const user = {
    name: 'Max',
    age: 25,
    email: 'max@example.com',
    isActive: true
};

// Verschachtelte Objects
const profile = {
    user: { name: 'Max', age: 25 },
    settings: { theme: 'dark' }
};
```

### Properties zugreifen

```javascript
// Dot Notation (bevorzugt)
user.name;      // 'Max'
user.age;       // 25

// Bracket Notation (für dynamische Keys)
user['name'];   // 'Max'

const key = 'email';
user[key];      // 'max@example.com'

// Verschachtelt
profile.user.name;           // 'Max'
profile.settings.theme;      // 'dark'
```

### Properties hinzufügen/ändern

```javascript
const user = { name: 'Max' };

// Property hinzufügen
user.age = 25;
user['email'] = 'max@example.com';

// Property ändern
user.name = 'Maximilian';

console.log(user);
// { name: 'Maximilian', age: 25, email: 'max@example.com' }
```

### Property Shorthand

Wenn Variable und Property-Name gleich sind:

```javascript
const name = 'Max';
const age = 25;

// Lang:
const user = { name: name, age: age };

// Kurz (ES6 Shorthand):
const user = { name, age };
// Beide ergeben: { name: 'Max', age: 25 }
```

### Übung 9: Objects

> **Ziel:** Objects erstellen und verwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Objects mit Dot und Bracket Notation nutzen kannst

**Aufgabe:**

```javascript
// 1. Erstelle ein Object für ein Buch
const book = {
    // title, author, year, available (boolean)
};

// 2. Greife auf verschiedene Properties zu
console.log(book.title);
console.log(book['author']);

// 3. Verwende Property Shorthand
const title = 'Clean Code';
const author = 'Robert C. Martin';
const year = 2008;

const bookShort = // Erstelle Object mit Shorthand

// 4. Erstelle ein verschachteltes Object
const library = {
    // name: 'Stadtbibliothek',
    // address: { street: '...', city: '...', zip: '...' },
    // books: [book, bookShort]
};

// 5. Greife auf verschachtelte Properties zu
console.log(library.address.city);
console.log(library.books[0].title);
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// 1. Buch-Object
const book = {
    title: 'JavaScript: The Good Parts',
    author: 'Douglas Crockford',
    year: 2008,
    available: true
};

// 2. Zugriff
console.log(book.title);      // 'JavaScript: The Good Parts'
console.log(book['author']);  // 'Douglas Crockford'

// 3. Shorthand
const title = 'Clean Code';
const author = 'Robert C. Martin';
const year = 2008;

const bookShort = { title, author, year, available: true };
console.log(bookShort);

// 4. Verschachteltes Object
const library = {
    name: 'Stadtbibliothek',
    address: {
        street: 'Hauptstraße 1',
        city: 'Berlin',
        zip: '10115'
    },
    books: [book, bookShort]
};

// 5. Verschachtelter Zugriff
console.log(library.address.city);    // 'Berlin'
console.log(library.books[0].title);  // 'JavaScript: The Good Parts'
```

</details>

---

## Teil 10: Spread Operator für Objects

Der Spread Operator funktioniert auch mit Objects – unverzichtbar für React State!

### Object kopieren

```javascript
const original = { name: 'Max', age: 25 };
const copy = { ...original };

// copy ist unabhängig von original
original.age = 26;
console.log(copy.age);  // 25 - nicht geändert!
```

### Objects zusammenführen

```javascript
const defaults = { theme: 'light', language: 'de' };
const userPrefs = { theme: 'dark' };

const settings = { ...defaults, ...userPrefs };
// { theme: 'dark', language: 'de' }
// userPrefs überschreibt defaults!
```

### Property überschreiben (Immutable)

```javascript
const user = { name: 'Max', age: 25, city: 'Berlin' };

// Neues Object mit geändertem age:
const updated = { ...user, age: 26 };
// { name: 'Max', age: 26, city: 'Berlin' }

// Original unverändert:
console.log(user.age); // 25
```

### React State Update Pattern

```javascript
// So sieht das in React aus:
const [user, setUser] = useState({
    name: 'Max',
    age: 25
});

// State aktualisieren (immutable!):
setUser({ ...user, age: 26 });

// FALSCH wäre:
// user.age = 26;  // Mutiert das Original!
// setUser(user);  // React erkennt keine Änderung!
```

### Verschachtelte Updates

```javascript
const profile = {
    user: { name: 'Max', age: 25 },
    settings: { theme: 'dark' }
};

// Nur user.age ändern:
const updated = {
    ...profile,
    user: {
        ...profile.user,
        age: 26
    }
};
```

### Übung 10: Object Spread

> **Ziel:** Immutable Object-Updates mit Spread
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du verstehst wie React State Updates funktionieren

**Aufgabe:**

```javascript
const user = {
    name: 'Max',
    email: 'max@example.com',
    settings: {
        theme: 'light',
        notifications: true
    }
};

// 1. Erstelle eine Kopie von user
const userCopy = // Dein Code

// 2. Erstelle neuen User mit geänderter email
const updatedEmail = // Dein Code

// 3. Erstelle neuen User mit theme: 'dark' (verschachtelt!)
const darkMode = // Dein Code

// 4. Füge eine neue Property 'age: 25' hinzu
const withAge = // Dein Code

// 5. Prüfe: Ist user unverändert?
console.log(user.settings.theme); // Sollte 'light' sein
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const user = {
    name: 'Max',
    email: 'max@example.com',
    settings: {
        theme: 'light',
        notifications: true
    }
};

// 1. Kopie (Shallow Copy)
const userCopy = { ...user };
console.log(userCopy);

// 2. Email ändern
const updatedEmail = { ...user, email: 'newemail@example.com' };
console.log(updatedEmail.email); // 'newemail@example.com'

// 3. Verschachteltes Update
const darkMode = {
    ...user,
    settings: {
        ...user.settings,
        theme: 'dark'
    }
};
console.log(darkMode.settings.theme); // 'dark'

// 4. Property hinzufügen
const withAge = { ...user, age: 25 };
console.log(withAge.age); // 25

// 5. Original prüfen
console.log(user.settings.theme); // 'light' ✓
console.log(user.email);          // 'max@example.com' ✓
console.log(user.age);            // undefined ✓
```

</details>

---

## Teil 11: Object Destructuring

Destructuring extrahiert Properties aus Objects – eleganter als in Python!

### Basis-Beispiel

```javascript
const user = { name: 'Max', age: 25, city: 'Berlin' };

// Mit Destructuring:
const { name, age, city } = user;
// name='Max', age=25, city='Berlin'

// Statt:
const name = user.name;
const age = user.age;
const city = user.city;
```

### Umbenennen

```javascript
const user = { name: 'Max', age: 25 };

// Property 'name' in Variable 'userName' speichern:
const { name: userName, age: userAge } = user;
console.log(userName); // 'Max'
```

### Default-Werte

```javascript
const user = { name: 'Max' };

const { name, age = 18, country = 'DE' } = user;
// name='Max', age=18 (default), country='DE' (default)
```

### Verschachteltes Destructuring

```javascript
const profile = {
    user: { name: 'Max', age: 25 },
    settings: { theme: 'dark' }
};

const { user: { name }, settings: { theme } } = profile;
console.log(name);  // 'Max'
console.log(theme); // 'dark'
```

### In Funktionsparametern (React-Pattern!)

```javascript
// Ohne Destructuring:
const Greeting = (props) => {
    return <h1>Hallo {props.name}!</h1>;
};

// Mit Destructuring (React-Standard):
const Greeting = ({ name, age }) => {
    return <h1>Hallo {name}, du bist {age}!</h1>;
};

// Aufruf:
<Greeting name="Max" age={25} />
```

### Übung 11: Object Destructuring

> **Ziel:** Properties elegant extrahieren
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Destructuring in Funktionsparametern nutzen kannst

**Aufgabe:**

```javascript
const product = {
    id: 1,
    name: 'Laptop',
    price: 999,
    specs: {
        cpu: 'Intel i7',
        ram: '16GB',
        storage: '512GB SSD'
    }
};

// 1. Extrahiere id, name, price
const { id, name, price } = // Dein Code

// 2. Extrahiere name, aber nenne es productName
const { name: productName } = // Dein Code

// 3. Extrahiere price mit Default-Wert
const { price: cost, discount = 0 } = // Dein Code

// 4. Extrahiere cpu und ram aus specs
const { specs: { cpu, ram } } = // Dein Code

// 5. Schreibe eine Funktion mit Destructuring
const formatProduct = ({ name, price }) => {
    // Gib "Name: X €" zurück
};

console.log(formatProduct(product)); // "Laptop: 999 €"
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const product = {
    id: 1,
    name: 'Laptop',
    price: 999,
    specs: {
        cpu: 'Intel i7',
        ram: '16GB',
        storage: '512GB SSD'
    }
};

// 1. Basis-Destructuring
const { id, name, price } = product;
console.log(id, name, price); // 1, 'Laptop', 999

// 2. Umbenennen
const { name: productName } = product;
console.log(productName); // 'Laptop'

// 3. Default-Werte
const { price: cost, discount = 0 } = product;
console.log(cost, discount); // 999, 0

// 4. Verschachtelt
const { specs: { cpu, ram } } = product;
console.log(cpu, ram); // 'Intel i7', '16GB'

// 5. In Funktion
const formatProduct = ({ name, price }) => {
    return `${name}: ${price} €`;
};
console.log(formatProduct(product)); // 'Laptop: 999 €'
```

</details>

---

## Teil 12: Immutability – Daten nicht ändern!

In React ändern wir Daten **NIE** direkt – wir erstellen immer neue Kopien!

### Warum Immutability?

```
React erkennt Änderungen durch Referenz-Vergleich:

const user = { name: 'Max' };

// FALSCH: Direkt ändern
user.name = 'Anna';
setUser(user);  // React sieht: gleiche Referenz → keine Änderung → kein Re-Render!

// RICHTIG: Neue Kopie
setUser({ ...user, name: 'Anna' });  // Neue Referenz → React erkennt Änderung → Re-Render!
```

### Python-Vergleich

```python
# Python: Das gleiche Problem!
list1 = [1, 2, 3]
list2 = list1       # Nur Referenz-Kopie!
list2.append(4)     # Ändert BEIDE Listen!
print(list1)        # [1, 2, 3, 4]
```

### FALSCH: Mutiert Original

```javascript
// ❌ Array mutieren
const items = ['a', 'b'];
items.push('c');     // Mutiert!
setItems(items);     // React merkt nichts!

// ❌ Object mutieren
const user = { name: 'Max' };
user.name = 'Anna';  // Mutiert!
setUser(user);       // React merkt nichts!
```

### RICHTIG: Neue Kopie erstellen

```javascript
// ✅ Array: Neues Array mit Spread
const items = ['a', 'b'];
setItems([...items, 'c']);  // Neues Array!

// ✅ Object: Neues Object mit Spread
const user = { name: 'Max' };
setUser({ ...user, name: 'Anna' });  // Neues Object!
```

### Immutable Patterns für Arrays

```javascript
const items = [1, 2, 3];

// Hinzufügen
const added = [...items, 4];           // [1, 2, 3, 4]
const prepended = [0, ...items];       // [0, 1, 2, 3]

// Entfernen (nach Index)
const removed = items.filter((_, i) => i !== 1);  // [1, 3]

// Entfernen (nach Wert)
const removed = items.filter(x => x !== 2);       // [1, 3]

// Aktualisieren
const updated = items.map(x => x === 2 ? 20 : x); // [1, 20, 3]
```

### Immutable Patterns für Objects

```javascript
const user = { name: 'Max', age: 25, city: 'Berlin' };

// Property ändern
const updated = { ...user, age: 26 };

// Property hinzufügen
const withEmail = { ...user, email: 'max@example.com' };

// Property entfernen
const { city, ...withoutCity } = user;
// withoutCity = { name: 'Max', age: 25 }
```

### Wissensfrage 4

Warum funktioniert dieser React-Code nicht richtig?

```javascript
const [todos, setTodos] = useState(['Task 1', 'Task 2']);

const addTodo = (newTodo) => {
    todos.push(newTodo);
    setTodos(todos);
};
```

<details>
<summary>Antwort anzeigen</summary>

**Problem:** `todos.push(newTodo)` mutiert das Original-Array. Dann wird `setTodos(todos)` aufgerufen – aber `todos` ist immer noch die **gleiche Referenz**!

React vergleicht: `oldTodos === newTodos` → `true` → **Keine Änderung erkannt** → **Kein Re-Render!**

**Lösung:**
```javascript
const addTodo = (newTodo) => {
    setTodos([...todos, newTodo]);  // Neues Array!
};
```

</details>

### Übung 12: Immutability

> **Ziel:** State-Updates ohne Mutation
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du alle Array/Object-Updates immutable durchführen kannst

**Aufgabe:**

```javascript
// Simuliere React State
let todos = [
    { id: 1, text: 'Lernen', done: false },
    { id: 2, text: 'Üben', done: false },
    { id: 3, text: 'Anwenden', done: true }
];

let user = {
    name: 'Max',
    preferences: { theme: 'light', language: 'de' }
};

// 1. Füge ein neues Todo hinzu (immutable!)
const newTodos1 = // [...todos, { id: 4, text: 'Wiederholen', done: false }]

// 2. Entferne Todo mit id === 2 (immutable!)
const newTodos2 = // filter()

// 3. Markiere Todo mit id === 1 als done: true (immutable!)
const newTodos3 = // map() mit Spread für das Object

// 4. Ändere user.preferences.theme zu 'dark' (immutable!)
const newUser = // Verschachtelter Spread

// 5. Prüfe: Sind die Originale unverändert?
console.log(todos[0].done);              // false
console.log(user.preferences.theme);     // 'light'
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
let todos = [
    { id: 1, text: 'Lernen', done: false },
    { id: 2, text: 'Üben', done: false },
    { id: 3, text: 'Anwenden', done: true }
];

let user = {
    name: 'Max',
    preferences: { theme: 'light', language: 'de' }
};

// 1. Todo hinzufügen
const newTodos1 = [...todos, { id: 4, text: 'Wiederholen', done: false }];
console.log(newTodos1.length); // 4

// 2. Todo entfernen
const newTodos2 = todos.filter(t => t.id !== 2);
console.log(newTodos2.length); // 2

// 3. Todo aktualisieren
const newTodos3 = todos.map(t =>
    t.id === 1 ? { ...t, done: true } : t
);
console.log(newTodos3[0].done); // true

// 4. Verschachteltes Update
const newUser = {
    ...user,
    preferences: {
        ...user.preferences,
        theme: 'dark'
    }
};
console.log(newUser.preferences.theme); // 'dark'

// 5. Originale prüfen
console.log(todos[0].done);              // false ✓
console.log(todos.length);               // 3 ✓
console.log(user.preferences.theme);     // 'light' ✓
```

</details>

---

## Teil 13: ES6 Modules – import/export

Module teilen Code in separate Dateien auf – die Basis für React-Komponenten!

### Python-Vergleich

```python
# Python: utils.py
PI = 3.14159
def add(a, b):
    return a + b

# Python: app.py
from utils import PI, add
```

```javascript
// JavaScript: utils.js
export const PI = 3.14159;
export function add(a, b) {
    return a + b;
}

// JavaScript: app.js
import { PI, add } from './utils.js';
```

### Named Exports

```javascript
// math.js - Mehrere Exports
export const PI = 3.14159;
export const E = 2.71828;

export function add(a, b) {
    return a + b;
}

export function multiply(a, b) {
    return a * b;
}
```

```javascript
// app.js - Named Imports
import { PI, add, multiply } from './math.js';

console.log(PI);           // 3.14159
console.log(add(2, 3));    // 5
```

### Default Export

```javascript
// Button.js - Ein Haupt-Export
const Button = ({ label, onClick }) => {
    return <button onClick={onClick}>{label}</button>;
};

export default Button;
```

```javascript
// App.js - Default Import (kein {})
import Button from './Button.js';
// Name kann frei gewählt werden:
import MyButton from './Button.js';  // Auch OK!
```

### Kombiniert: Default + Named

```javascript
// api.js
export const BASE_URL = 'https://api.example.com';
export const API_KEY = 'secret123';

const fetchData = async (endpoint) => {
    const response = await fetch(`${BASE_URL}/${endpoint}`);
    return response.json();
};

export default fetchData;
```

```javascript
// app.js
import fetchData, { BASE_URL, API_KEY } from './api.js';
```

### React-Pattern

```javascript
// components/Button.jsx
const Button = ({ label }) => {
    return <button>{label}</button>;
};

export default Button;
```

```javascript
// App.jsx
import Button from './components/Button';

const App = () => {
    return <Button label="Klick mich" />;
};
```

### Wissensfrage 5

Was ist der Unterschied zwischen diesen Imports?

```javascript
import Button from './Button';
import { Button } from './Button';
```

<details>
<summary>Antwort anzeigen</summary>

**`import Button from './Button'`:**
- Importiert den **default export**
- Die Datei muss `export default` haben
- Name ist frei wählbar: `import MyBtn from './Button'`

**`import { Button } from './Button'`:**
- Importiert einen **named export**
- Die Datei muss `export const Button = ...` haben
- Name muss exakt übereinstimmen (oder mit `as` umbenennen)

```javascript
// Button.js mit beiden:
export const Button = () => { ... };        // Named
export default function MainButton() {...}  // Default

// Import:
import MainButton, { Button } from './Button';
```

</details>

---

## Teil 14: Praktische Gesamtübung

Zeit, alles zusammen anzuwenden!

### Aufgabe: Produkt-Manager

Erstelle eine JavaScript-Datei, die alle gelernten Konzepte kombiniert:

```javascript
// produkt-manager.js

// ==============================
// 1. DATEN (Arrays von Objects)
// ==============================
const products = [
    { id: 1, name: 'Laptop', price: 999, category: 'Electronics', inStock: true },
    { id: 2, name: 'Buch', price: 15, category: 'Books', inStock: true },
    { id: 3, name: 'Kopfhörer', price: 89, category: 'Electronics', inStock: false },
    { id: 4, name: 'Tasse', price: 12, category: 'Home', inStock: true },
    { id: 5, name: 'Tastatur', price: 65, category: 'Electronics', inStock: true }
];

// ==============================
// 2. FILTER-FUNKTIONEN
// ==============================

// Funktion: Nur verfügbare Produkte
const getAvailable = (products) => {
    // Dein Code hier
};

// Funktion: Produkte nach Kategorie filtern
const getByCategory = (products, category) => {
    // Dein Code hier
};

// Funktion: Günstige Produkte (unter maxPrice)
const getCheap = (products, maxPrice) => {
    // Dein Code hier
};

// ==============================
// 3. TRANSFORMATIONEN
// ==============================

// Funktion: Nur Produktnamen
const getNames = (products) => {
    // Dein Code hier
};

// Funktion: Preise mit Rabatt
const applyDiscount = (products, discountPercent) => {
    // Dein Code hier (immutable!)
};

// ==============================
// 4. SUCHE
// ==============================

// Funktion: Produkt nach ID finden
const findById = (products, id) => {
    // Dein Code hier
};

// ==============================
// 5. IMMUTABLE UPDATES
// ==============================

// Funktion: Produkt hinzufügen
const addProduct = (products, newProduct) => {
    // Dein Code hier (immutable!)
};

// Funktion: Produkt entfernen
const removeProduct = (products, id) => {
    // Dein Code hier (immutable!)
};

// Funktion: Preis aktualisieren
const updatePrice = (products, id, newPrice) => {
    // Dein Code hier (immutable!)
};

// ==============================
// 6. TESTS
// ==============================
console.log("=== Filter Tests ===");
console.log("Verfügbar:", getAvailable(products).map(p => p.name));
console.log("Electronics:", getByCategory(products, 'Electronics').map(p => p.name));
console.log("Unter 50€:", getCheap(products, 50).map(p => p.name));

console.log("\n=== Transform Tests ===");
console.log("Namen:", getNames(products));
console.log("10% Rabatt:", applyDiscount(products, 10).map(p => `${p.name}: ${p.price}€`));

console.log("\n=== Find Tests ===");
console.log("ID 3:", findById(products, 3));
console.log("ID 99:", findById(products, 99));

console.log("\n=== Immutable Update Tests ===");
const newProduct = { id: 6, name: 'Monitor', price: 299, category: 'Electronics', inStock: true };
const added = addProduct(products, newProduct);
console.log("Nach Hinzufügen:", added.length, "Original:", products.length);

const removed = removeProduct(products, 2);
console.log("Nach Entfernen:", removed.length, "Original:", products.length);

const updated = updatePrice(products, 1, 899);
console.log("Neuer Preis:", updated.find(p => p.id === 1).price);
console.log("Original Preis:", products.find(p => p.id === 1).price);
```

### Erwartete Ausgabe

```
=== Filter Tests ===
Verfügbar: ['Laptop', 'Buch', 'Tasse', 'Tastatur']
Electronics: ['Laptop', 'Kopfhörer', 'Tastatur']
Unter 50€: ['Buch', 'Tasse']

=== Transform Tests ===
Namen: ['Laptop', 'Buch', 'Kopfhörer', 'Tasse', 'Tastatur']
10% Rabatt: ['Laptop: 899€', 'Buch: 14€', ...]

=== Find Tests ===
ID 3: { id: 3, name: 'Kopfhörer', ... }
ID 99: undefined

=== Immutable Update Tests ===
Nach Hinzufügen: 6 Original: 5
Nach Entfernen: 4 Original: 5
Neuer Preis: 899
Original Preis: 999
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// produkt-manager.js

const products = [
    { id: 1, name: 'Laptop', price: 999, category: 'Electronics', inStock: true },
    { id: 2, name: 'Buch', price: 15, category: 'Books', inStock: true },
    { id: 3, name: 'Kopfhörer', price: 89, category: 'Electronics', inStock: false },
    { id: 4, name: 'Tasse', price: 12, category: 'Home', inStock: true },
    { id: 5, name: 'Tastatur', price: 65, category: 'Electronics', inStock: true }
];

// Filter-Funktionen
const getAvailable = (products) => products.filter(p => p.inStock);

const getByCategory = (products, category) =>
    products.filter(p => p.category === category);

const getCheap = (products, maxPrice) =>
    products.filter(p => p.price < maxPrice);

// Transformationen
const getNames = (products) => products.map(p => p.name);

const applyDiscount = (products, discountPercent) =>
    products.map(p => ({
        ...p,
        price: Math.round(p.price * (1 - discountPercent / 100))
    }));

// Suche
const findById = (products, id) => products.find(p => p.id === id);

// Immutable Updates
const addProduct = (products, newProduct) => [...products, newProduct];

const removeProduct = (products, id) =>
    products.filter(p => p.id !== id);

const updatePrice = (products, id, newPrice) =>
    products.map(p => p.id === id ? { ...p, price: newPrice } : p);

// Tests
console.log("=== Filter Tests ===");
console.log("Verfügbar:", getAvailable(products).map(p => p.name));
console.log("Electronics:", getByCategory(products, 'Electronics').map(p => p.name));
console.log("Unter 50€:", getCheap(products, 50).map(p => p.name));

console.log("\n=== Transform Tests ===");
console.log("Namen:", getNames(products));
console.log("10% Rabatt:", applyDiscount(products, 10).map(p => `${p.name}: ${p.price}€`));

console.log("\n=== Find Tests ===");
console.log("ID 3:", findById(products, 3));
console.log("ID 99:", findById(products, 99));

console.log("\n=== Immutable Update Tests ===");
const newProduct = { id: 6, name: 'Monitor', price: 299, category: 'Electronics', inStock: true };
const added = addProduct(products, newProduct);
console.log("Nach Hinzufügen:", added.length, "Original:", products.length);

const removed = removeProduct(products, 2);
console.log("Nach Entfernen:", removed.length, "Original:", products.length);

const updated = updatePrice(products, 1, 899);
console.log("Neuer Preis:", updated.find(p => p.id === 1).price);
console.log("Original Preis:", products.find(p => p.id === 1).price);
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Thema | Python | JavaScript | Beispiel |
|-------|--------|------------|----------|
| **Arrays** | `liste = []` | `const arr = []` | Listen von Werten |
| **map()** | `[x*2 for x in lst]` | `arr.map(x => x*2)` | Transformieren |
| **filter()** | `[x for x in lst if x>0]` | `arr.filter(x => x>0)` | Filtern |
| **find()** | `next((x for x if ...), None)` | `arr.find(x => ...)` | Erstes Element |
| **Spread Array** | `[*lst1, *lst2]` | `[...arr1, ...arr2]` | Kopieren/Kombinieren |
| **Array Destructuring** | `a, b = lst` | `const [a, b] = arr` | Entpacken |
| **Objects** | `{"key": "value"}` | `{ key: "value" }` | Key-Value |
| **Spread Object** | `{**dict1, **dict2}` | `{...obj1, ...obj2}` | Kopieren/Mergen |
| **Object Destructuring** | - | `const { a, b } = obj` | Properties extrahieren |
| **Modules** | `from x import y` | `import { y } from 'x'` | Code teilen |

### Die wichtigsten Patterns für React

```javascript
// 1. useState mit Destructuring
const [count, setCount] = useState(0);

// 2. Props mit Destructuring
const Button = ({ label, onClick }) => { ... };

// 3. Immutable Array Update
setItems([...items, newItem]);

// 4. Immutable Object Update
setUser({ ...user, name: 'Neuer Name' });

// 5. Liste rendern mit map()
{items.map(item => <li key={item.id}>{item.name}</li>)}

// 6. Gefilterte Liste
{items.filter(i => i.active).map(i => ...)}
```

---

## Vorbereitung auf morgen

Morgen lernst du **DOM, Events & Interaktivität**:

- **DOM verstehen:** Der "Bauplan" der Webseite im Browser
- **Elemente selektieren:** `querySelector`, `getElementById`
- **DOM manipulieren:** Inhalte ändern, Klassen toggeln, Styles setzen
- **Events:** click, submit, input – auf User-Aktionen reagieren
- **Formulare:** Daten erfassen und verarbeiten

Das Event-Handling in React ist sehr ähnlich – onClick, onChange, etc.!

---

## Checkliste

Bevor du mit dem nächsten Tag weitermachst, stelle sicher:

- [ ] Du kannst Arrays mit `map()` transformieren
- [ ] Du kannst Arrays mit `filter()` filtern
- [ ] Du verstehst den Unterschied zwischen `find()` und `filter()`
- [ ] Du kannst den Spread Operator `...` für Arrays und Objects nutzen
- [ ] Du verstehst Array Destructuring (`const [a, b] = arr`)
- [ ] Du verstehst Object Destructuring (`const { name, age } = obj`)
- [ ] Du weißt, warum Immutability in React wichtig ist
- [ ] Du kannst State Updates immutable durchführen
- [ ] Du verstehst `import`/`export` für Module

**Alles abgehakt?** Dann bist du bereit für Tag 8: DOM, Events & Interaktivität!

---

## Bonus: Schnellreferenz

### Array-Methoden

```javascript
// Transformieren
arr.map(x => x * 2)          // Neues Array mit transformierten Werten

// Filtern
arr.filter(x => x > 0)       // Neues Array mit passenden Elementen

// Suchen
arr.find(x => x.id === 1)    // Erstes passendes Element oder undefined
arr.findIndex(x => x > 10)   // Index oder -1
arr.includes('a')            // true/false

// Hinzufügen/Entfernen (MUTIERT!)
arr.push(x)                  // Am Ende hinzufügen
arr.pop()                    // Letztes entfernen
arr.unshift(x)               // Am Anfang hinzufügen
arr.shift()                  // Erstes entfernen

// Immutable Alternativen
[...arr, x]                  // Hinzufügen am Ende
[x, ...arr]                  // Hinzufügen am Anfang
arr.filter((_, i) => i !== index)  // Entfernen nach Index
```

### Spread Operator

```javascript
// Arrays
const copy = [...arr];
const combined = [...arr1, ...arr2];
const added = [...arr, newItem];

// Objects
const copy = { ...obj };
const merged = { ...obj1, ...obj2 };
const updated = { ...obj, key: newValue };
```

### Destructuring

```javascript
// Array
const [first, second, ...rest] = arr;
const [a, , c] = arr;  // Überspringen

// Object
const { name, age } = obj;
const { name: userName } = obj;  // Umbenennen
const { name, city = 'Berlin' } = obj;  // Default
```

### Immutable Patterns

```javascript
// Array: Hinzufügen
const newArr = [...arr, item];

// Array: Entfernen
const newArr = arr.filter(x => x.id !== idToRemove);

// Array: Aktualisieren
const newArr = arr.map(x => x.id === id ? { ...x, changed: true } : x);

// Object: Aktualisieren
const newObj = { ...obj, key: newValue };

// Object: Property entfernen
const { keyToRemove, ...newObj } = obj;
```
