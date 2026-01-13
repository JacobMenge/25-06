# JavaScript Fundamentals - Praktische Übungen

## Übersicht

Willkommen zu deinem ersten Kontakt mit JavaScript! In dieser Übung lernst du die grundlegende Syntax von JavaScript kennen, die Programmiersprache, die im Browser läuft und die Basis für React bildet.

**Gute Nachricht:** Du kannst bereits Python programmieren! Viele Konzepte kennst du schon - heute lernst du nur die JavaScript-Schreibweise dafür.

In dieser Übung vertiefst du dein Wissen über:
- **Von Python zu JavaScript** - Die wichtigsten Syntax-Unterschiede
- **Variablen** - `const` und `let` statt einfacher Zuweisung
- **Arrow Functions** - Die moderne Funktions-Syntax für React
- **Operatoren** - Ternary (`? :`) und Logical (`&&`, `||`, `??`) für JSX
- **Template Literals** - String-Interpolation mit Backticks
- **Console & Debugging** - Dein wichtigstes Werkzeug

Diese Übung bereitet dich auf React vor, das du in den nächsten Tagen lernen wirst.

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | Was du bisher gelernt hast | 5 min (lesen) |
| **Teil 1** | JavaScript verstehen - Wo läuft es? | 10 min |
| **Teil 2** | Python → JavaScript Syntax-Vergleich | 10 min |
| **Teil 3** | Variablen: const und let | 15 min |
| **Teil 4** | Datentypen in JavaScript | 10 min |
| **Teil 5** | Vergleichsoperatoren: === vs == | 10 min |
| **Teil 6** | Arrow Functions | 20 min |
| **Teil 7** | Template Literals | 10 min |
| **Teil 8** | Ternary Operator | 10 min |
| **Teil 9** | Logical Operators: &&, \|\|, ?? | 15 min |
| **Teil 10** | Callback Functions | 10 min |
| **Teil 11** | Console & Debugging | 15 min |
| **Teil 12** | JavaScript in HTML einbinden | 15 min |
| **Teil 13** | Kontrollstrukturen | 5 min (lesen) |
| **Teil 14** | Praktische Gesamtübung | 20 min |
| | **Gesamt** | **ca. 2-3 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Teil 3** - Variablen (const/let) - *Das Fundament*
2. **Teil 6** - Arrow Functions - *React-Standard*
3. **Teil 7** - Template Literals - *String-Interpolation*
4. **Teil 8** - Ternary Operator - *Für JSX*
5. **Teil 9** - Logical Operators - *Für React*
6. **Teil 11** - Console & Debugging - *Dein Werkzeug*

Die anderen Teile kannst du später nachholen oder als Referenz nutzen.

---

## Hinweis zu Semikolons

In diesem Kurs **setzen wir Semikolons** am Ende von JavaScript-Anweisungen:

```javascript
const name = "Max";  // Mit Semikolon - unser Standard
```

Technisch sind Semikolons in JavaScript optional (Automatic Semicolon Insertion), aber wir nutzen sie für Konsistenz und Klarheit. Die meisten Unternehmen und Style-Guides (wie Airbnb) empfehlen ebenfalls Semikolons.

---

## Rückblick: Was du bisher gelernt hast

### Woche 1: Die Grundlagen des Webs

In der ersten Woche hast du die **statischen** Bausteine einer Website kennengelernt:

| Tag | Thema | Was du gelernt hast |
|-----|-------|---------------------|
| Tag 1 | Webarchitektur & HTTP | Wie Browser und Server kommunizieren |
| Tag 2 | HTML | Die **Struktur** einer Website (Überschriften, Absätze, Links, Formulare) |
| Tag 3 | CSS Grundlagen | Das **Aussehen** einer Website (Farben, Schriften, Abstände) |
| Tag 4 | CSS Layout | Flexbox, Grid und Responsive Design |
| Tag 5 | Portfolio-Projekt | Alles zusammen angewendet |

### Das Problem: Statische Websites

Mit HTML und CSS kannst du schöne Websites bauen - aber sie sind **statisch**:

```
┌─────────────────────────────────────────────────────────┐
│                    STATISCHE WEBSITE                     │
│                                                          │
│  HTML = Struktur    →  "Was ist auf der Seite?"         │
│  CSS  = Aussehen    →  "Wie sieht es aus?"              │
│                                                          │
│  Problem: Die Seite kann nicht auf User reagieren!       │
│  - Kein Klick-Feedback                                   │
│  - Keine Formulare, die etwas tun                        │
│  - Keine Daten laden/speichern                           │
│  - Seite muss neu laden für jede Änderung               │
└─────────────────────────────────────────────────────────┘
```

### Die Lösung: JavaScript!

**JavaScript** macht deine Website **interaktiv** und **dynamisch**:

```
┌─────────────────────────────────────────────────────────┐
│                   DYNAMISCHE WEBSITE                     │
│                                                          │
│  HTML = Struktur    →  "Was ist auf der Seite?"         │
│  CSS  = Aussehen    →  "Wie sieht es aus?"              │
│  JS   = Verhalten   →  "Was passiert bei Interaktion?"  │
│                                                          │
│  Mit JavaScript kannst du:                               │
│  - Auf Klicks, Eingaben, Scrollen reagieren             │
│  - Inhalte ändern ohne Seite neu zu laden               │
│  - Daten von deiner API laden (fetch)                   │
│  - Formulare validieren und absenden                    │
│  - Animationen und Übergänge steuern                    │
└─────────────────────────────────────────────────────────┘
```

### Die drei Säulen der Webentwicklung

```
        WEBSITE
           │
    ┌──────┼──────┐
    │      │      │
   HTML   CSS    JS
    │      │      │
Struktur Aussehen Verhalten
  "WAS"   "WIE"   "WANN"
```

**Beispiel: Ein "Like"-Button**

| Technologie | Aufgabe |
|-------------|---------|
| **HTML** | `<button>Like</button>` - Der Button existiert |
| **CSS** | Farbe, Größe, Hover-Effekt - Der Button sieht gut aus |
| **JavaScript** | Was passiert beim Klick? → Zähler erhöhen, an Server senden, Farbe ändern |

### Warum jetzt JavaScript?

Du hast das Fundament gelegt:
- Du weißt, wie **HTML-Dokumente** aufgebaut sind
- Du kannst **CSS-Selektoren** schreiben
- Du verstehst **HTTP-Requests** und wie Browser mit Servern kommunizieren

Jetzt lernst du JavaScript, um:
1. **Diese Woche:** Die Syntax und Grundkonzepte
2. **Nächste Woche:** React - eine moderne Bibliothek zum Bauen von Benutzeroberflächen
3. **Danach:** Dein Python-Backend mit deinem React-Frontend verbinden!

---

## Bevor du startest: Entwicklungsumgebung prüfen

### Wo läuft JavaScript? Browser vs. Node.js

In dieser Übung nutzt du **zwei Möglichkeiten**, JavaScript auszuführen:

| Umgebung | Was ist das? | Wann nutzen? |
|----------|--------------|--------------|
| **Browser Console** | JavaScript-Umgebung im Browser (F12 → Console) | Schnelles Testen, DOM-Manipulation |
| **Node.js** | JavaScript-Runtime für deinen Computer | `.js`-Dateien ausführen, npm-Pakete |

**Wichtig:** Beide führen JavaScript aus, aber haben unterschiedliche Funktionen:
- **Nur im Browser:** `document`, `window`, `alert()`, DOM-Manipulation
- **Nur in Node.js:** `fs` (Dateisystem), `process`, npm-Module

Für diese Übung nutzt du hauptsächlich:
- **Browser Console** für schnelle Tests (Teile 1-10)
- **Node.js** für `.js`-Dateien (Teil 11-14)

---

### Node.js und npm prüfen

Stelle sicher, dass Node.js und npm installiert sind. Öffne dein Terminal und prüfe:

```bash
node --version
```
**Erwartete Ausgabe:** Eine aktuelle LTS-Version (z.B. `v20.x.x`, `v22.x.x` oder neuer)

```bash
npm --version
```
**Erwartete Ausgabe:** `10.x.x` (oder eine andere aktuelle Version)

**Falls nicht installiert:** Folge der separaten Anleitung `anleitung-nodejs-npm-installation.md` in diesem Ordner.

---

## Teil 1: JavaScript verstehen - Wo läuft es?

### JavaScript im Browser

JavaScript ist **DIE** Programmiersprache für Frontend-Entwicklung. Jeder Browser hat eine eingebaute JavaScript-Engine:

| Browser | JavaScript-Engine |
|---------|-------------------|
| Chrome | V8 |
| Firefox | SpiderMonkey |
| Safari | JavaScriptCore |
| Edge | V8 (wie Chrome) |

### Dein Tech-Stack: Backend + Frontend

Du kennst bereits Python/FastAPI für das Backend. Jetzt kommt JavaScript/React für das Frontend dazu:

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│  Python/FastAPI │  <--->  │    REST-API     │  <--->  │ React/JavaScript│
│    (Backend)    │         │  (HTTP-Requests)│         │   (Frontend)    │
│                 │         │                 │         │                 │
│ - API-Endpunkte │         │ GET, POST, etc. │         │ - Benutzerober- │
│ - Datenbank     │         │                 │         │   fläche        │
│ - Geschäftslogik│         │                 │         │ - Interaktionen │
└─────────────────┘         └─────────────────┘         └─────────────────┘
     Server-Seite                                           Browser-Seite
```

**Wichtig:** Euer Backend bleibt Python/FastAPI - JavaScript ist nur für das Frontend!

### Wissensfrage 1

Warum brauchen wir JavaScript, wenn wir doch schon Python können?

<details>
<summary>Antwort anzeigen</summary>

**Browser können kein Python ausführen!**

- Browser haben eine **JavaScript-Engine** eingebaut, aber keinen Python-Interpreter
- JavaScript ist die einzige Programmiersprache, die direkt im Browser läuft
- Euer Python-Backend läuft auf dem **Server**, JavaScript läuft im **Browser** des Nutzers

**Der Datenfluss:**
1. Nutzer öffnet Website → Browser lädt HTML, CSS, JavaScript
2. JavaScript (React) baut die Benutzeroberfläche
3. Bei Bedarf ruft JavaScript eure FastAPI-Endpunkte auf (fetch)
4. Python verarbeitet die Anfrage und sendet Daten zurück
5. JavaScript zeigt die Daten im Browser an

</details>

---

## Teil 2: Python → JavaScript - Der Syntax-Vergleich

### Die gute Nachricht

Du kannst bereits programmieren! Die **Konzepte** sind die gleichen - nur die **Schreibweise** ist anders:

| Konzept | Python | JavaScript |
|---------|--------|------------|
| Variablen | `name = "Max"` | `const name = "Max";` |
| Funktionen | `def greet(name):` | `const greet = (name) => {` |
| Strings | `f"Hallo {name}"` | `` `Hallo ${name}` `` |
| Listen/Arrays | `[1, 2, 3]` | `[1, 2, 3]` |
| Dictionaries/Objects | `{"name": "Max"}` | `{ name: "Max" }` |
| Print/Log | `print("Hallo")` | `console.log("Hallo");` |
| Kommentare | `# Kommentar` | `// Kommentar` |
| Keine Semikolons | Standard | Optional, aber üblich |
| Einrückung | **Pflicht** (definiert Blöcke) | Optional (Blöcke durch `{}`) |

### Vollständiger Vergleich

**Python:**
```python
# Variablen
name = "Max"
age = 25

# Funktion
def greet(name):
    return f"Hallo {name}"

# Bedingung
if age >= 18:
    print("Volljährig")

# Liste & Dictionary
items = [1, 2, 3]
user = {"name": "Max", "age": 25}

# List Comprehension
doubled = [x * 2 for x in items]
```

**JavaScript:**
```javascript
// Variablen
const name = "Max";
let age = 25;

// Funktion (Arrow Function)
const greet = (name) => {
    return `Hallo ${name}`;
};

// Bedingung
if (age >= 18) {
    console.log("Volljährig");
}

// Array & Object
const items = [1, 2, 3];
const user = { name: "Max", age: 25 };

// Array Method (statt List Comprehension)
const doubled = items.map(x => x * 2);
```

### Wichtige Unterschiede auf einen Blick

| Aspekt | Python | JavaScript |
|--------|--------|------------|
| **Blöcke** | Einrückung | Geschweifte Klammern `{ }` |
| **Zeilenende** | Nichts | Semikolon `;` (optional) |
| **Boolean** | `True`, `False` | `true`, `false` |
| **None/Null** | `None` | `null`, `undefined` |
| **And/Or** | `and`, `or`, `not` | `&&`, `||`, `!` |
| **String-Interpolation** | `f"Hallo {x}"` | `` `Hallo ${x}` `` |

---

## Teil 3: Variablen - const und let

### Das Wichtigste zuerst

In Python schreibst du einfach `name = "Max"`. In JavaScript musst du **deklarieren**, ob sich der Wert ändern darf:

```javascript
const name = "Max";    // Konstante - Wert kann NICHT neu zugewiesen werden
let age = 25;          // Variable - Wert KANN neu zugewiesen werden
```

### const - Für Werte, die sich nicht ändern

```javascript
// const = constant (Konstante)
const name = "Jacob";
const PI = 3.14159;
const isActive = true;

// Das funktioniert NICHT - Fehler!
// name = "Anton";  // TypeError: Assignment to constant variable

// ABER: Bei Objects und Arrays kann der INHALT geändert werden!
const user = { name: "Max" };
user.name = "Anna";  // Das funktioniert! (Object-Inhalt ändern)

const numbers = [1, 2, 3];
numbers.push(4);     // Das funktioniert! (Array-Inhalt ändern)

// Was NICHT geht:
// user = { name: "Neu" };  // Fehler! Neue Zuweisung nicht erlaubt
// numbers = [5, 6, 7];     // Fehler! Neue Zuweisung nicht erlaubt
```

### let - Für Werte, die sich ändern müssen

```javascript
// let = veränderliche Variable
let counter = 0;
counter = 1;  // OK
counter = 2;  // OK

let message;           // Deklarieren ohne Wert
message = "Hallo";     // Später zuweisen - OK

// Typischer Anwendungsfall: Schleifen
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

### Die goldene Regel

> **Immer `const` verwenden. Nur `let`, wenn du den Wert wirklich ändern musst.**

In der Praxis sind ca. 90% deiner Variablen `const`!

### Warum kein var?

Du wirst in älterem Code noch `var` sehen. **Verwende es NIEMALS** in neuem Code:

```javascript
// var hat Probleme - NICHT VERWENDEN!
if (true) {
    var x = 10;  // var ignoriert Block-Grenzen
}
console.log(x);  // 10 - Variable "leakt" aus dem Block!

// let verhält sich korrekt
if (true) {
    let y = 10;  // let respektiert Block-Grenzen
}
console.log(y);  // ReferenceError: y is not defined
```

**Probleme mit var:**
1. **Function Scope statt Block Scope** - Variable "leakt" aus if/for-Blöcken
2. **Hoisting** - Deklarationen werden "nach oben gezogen" (verwirrend!)
3. **Doppelte Deklaration erlaubt** - Führt zu schwer findbaren Bugs

### Übung 1: const und let verstehen

> **Ziel:** Unterschied zwischen `const` und `let` praktisch erleben
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du verstehst, warum `const` Neuzuweisung verhindert, aber Object-Inhalte änderbar bleiben

**Aufgabe:**

Öffne die Browser-Konsole (F12 → Console Tab) und tippe folgende Zeilen ein. Beobachte, was passiert:

```javascript
// 1. const ausprobieren
const meinName = "Max";
console.log(meinName);

// 2. Versuche const neu zuzuweisen - was passiert?
// meinName = "Anna";

// 3. let ausprobieren
let zaehler = 0;
console.log(zaehler);
zaehler = 1;
console.log(zaehler);

// 4. const mit Object
const person = { name: "Max", alter: 25 };
console.log(person);
person.alter = 26;  // Inhalt ändern - geht das?
console.log(person);

// 5. Neue Zuweisung bei const Object - geht das?
// person = { name: "Neu" };
```

<details>
<summary>Was passiert?</summary>

1. `const meinName = "Max"` - Erstellt eine Konstante
2. `meinName = "Anna"` - **TypeError!** const kann nicht neu zugewiesen werden
3. `let zaehler` - Erstellt eine Variable, die geändert werden kann
4. `person.alter = 26` - **Funktioniert!** Der Inhalt eines Objects kann geändert werden
5. `person = { name: "Neu" }` - **TypeError!** Das Object selbst kann nicht ersetzt werden

**Merke:** `const` verhindert die **Neuzuweisung**, nicht die **Änderung des Inhalts**!

> **Vorschau auf React:** Obwohl `const arr` technisch `arr.push()` erlaubt, vermeiden wir in React solche Mutationen. Stattdessen erstellen wir neue Arrays/Objects. Warum? Das lernst du bei "Immutability" - ein wichtiges React-Konzept!

</details>

---

## Teil 4: Datentypen in JavaScript

### Primitive Typen (unveränderlich)

| Typ | Beispiel | Python-Äquivalent |
|-----|----------|-------------------|
| **String** | `"Hallo"` oder `'Welt'` | `str` |
| **Number** | `42`, `3.14`, `-10` | `int` / `float` |
| **Boolean** | `true`, `false` | `bool` |
| **null** | `null` (absichtlich leer) | `None` |
| **undefined** | `undefined` (nicht definiert) | - (gibt es nicht in Python) |

### Referenz-Typen (veränderlich)

| Typ | Beispiel | Python-Äquivalent |
|-----|----------|-------------------|
| **Object** | `{ name: "Max", age: 25 }` | `dict` |
| **Array** | `[1, 2, 3, "vier"]` | `list` |
| **Function** | `() => { ... }` | `def` / `lambda` |

### null vs. undefined - Was ist der Unterschied?

```javascript
// undefined = "wurde nie ein Wert zugewiesen"
let x;
console.log(x);  // undefined

// null = "absichtlich leer gesetzt"
let y = null;
console.log(y);  // null

// Praktisches Beispiel:
let user = null;  // Explizit: "Kein User eingeloggt"

// Später, wenn jemand sich einloggt:
user = { name: "Max" };
```

**Faustregel:**
- `undefined` = JavaScript sagt "da ist nichts"
- `null` = Du sagst "da soll nichts sein"

### typeof - Typ prüfen

```javascript
typeof "Hallo"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object"  ⚠️ Historischer Bug in JS!
typeof {}           // "object"
typeof []           // "object"  (Arrays sind Objects)
typeof (() => {})   // "function"
```

### Wissensfrage 2

Was ist der Unterschied zwischen `null` und `undefined`?

<details>
<summary>Antwort anzeigen</summary>

**undefined:**
- Bedeutet "wurde nie ein Wert zugewiesen"
- JavaScript setzt automatisch `undefined` für nicht initialisierte Variablen
- Beispiel: `let x;` → `x` ist `undefined`

**null:**
- Bedeutet "absichtlich leer/kein Wert"
- Du setzt `null` bewusst, um "nichts" auszudrücken
- Beispiel: `let user = null;` → "aktuell ist kein User eingeloggt"

**In Python** gibt es nur `None`, das beide Fälle abdeckt.

</details>

---

## Teil 5: Vergleichsoperatoren - === vs ==

### Das Wichtigste: Immer === verwenden!

JavaScript hat **zwei** Arten von Gleichheitsoperatoren:

```javascript
// === (Strict Equality) - Prüft Wert UND Typ
5 === 5        // true
5 === "5"      // false (Number vs String)
null === undefined  // false

// == (Loose Equality) - Konvertiert Typen (GEFÄHRLICH!)
5 == "5"       // true  😱
null == undefined  // true  😱
"" == false    // true  😱
[] == false    // true  😱
```

### Warum ist == gefährlich?

```javascript
// Diese Vergleiche sind alle true mit ==:
0 == ""        // true (leerer String wird zu 0)
0 == false     // true (false wird zu 0)
"" == false    // true (beide werden zu 0)
null == undefined  // true (Spezialfall)
[] == 0        // true (Array wird zu String wird zu 0)

// Das führt zu schwer findbaren Bugs!
```

### Die goldene Regel

> **Immer `===` und `!==` verwenden. Niemals `==` oder `!=`.**

```javascript
// ✅ Richtig
if (status === "active") { ... }
if (count !== 0) { ... }

// ❌ Falsch (vermeiden!)
if (status == "active") { ... }
if (count != 0) { ... }
```

### Übung 2: Vergleichsoperatoren testen

> **Ziel:** Verstehen warum `===` sicherer ist als `==`
> **Zeitbedarf:** ca. 5 Minuten
> **Du bist fertig, wenn:** Du weißt, dass `==` Typen konvertiert und warum das gefährlich ist

**Aufgabe:**

Teste in der Browser-Konsole:

```javascript
// Was geben diese Vergleiche zurück?
console.log(5 === 5);
console.log(5 === "5");
console.log(5 == "5");

console.log(null === undefined);
console.log(null == undefined);

console.log("" === false);
console.log("" == false);

// Bonus: Erkläre, warum diese Ergebnisse so sind
```

<details>
<summary>Lösung anzeigen</summary>

```javascript
5 === 5           // true (gleicher Wert, gleicher Typ)
5 === "5"         // false (Number vs String)
5 == "5"          // true ("5" wird zu 5 konvertiert)

null === undefined  // false (verschiedene Typen)
null == undefined   // true (Spezialregel in JS)

"" === false      // false (String vs Boolean)
"" == false       // true (beide werden zu 0)
```

**Lektion:** `==` führt zu unerwarteten Ergebnissen. Verwende immer `===`!

</details>

---

## Teil 6: Funktionen - Arrow Functions

### Python def → JavaScript Arrow Function

In React wirst du fast ausschließlich **Arrow Functions** verwenden. Sie sind kürzer und haben ein besseres `this`-Verhalten.

**Python:**
```python
def greet(name):
    return f"Hallo {name}"

# Lambda (kurze Funktion)
add = lambda a, b: a + b
```

**JavaScript - Klassische Funktion:**
```javascript
function greet(name) {
    return `Hallo ${name}`;
}
```

**JavaScript - Arrow Function (React-Standard):**
```javascript
const greet = (name) => {
    return `Hallo ${name}`;
};

// Kurzform (wie lambda):
const add = (a, b) => a + b;
```

### Arrow Function Syntax-Varianten

```javascript
// 1. Mehrere Parameter: Klammern nötig
const add = (a, b) => a + b;

// 2. Ein Parameter: Klammern optional
const double = x => x * 2;
const double2 = (x) => x * 2;  // Auch OK

// 3. Kein Parameter: Leere Klammern nötig
const sayHi = () => "Hi!";

// 4. Mehrzeilig: Geschweifte Klammern + return nötig
const calculate = (a, b) => {
    const result = a + b;
    console.log("Berechne...");
    return result;
};

// 5. Object zurückgeben: In Klammern setzen!
const createUser = (name) => ({ name: name, active: true });
//                           ↑ Klammern nötig, sonst denkt JS es ist ein Block
```

### Wo du Arrow Functions in React siehst

```javascript
// 1. Komponenten definieren
const App = () => {
    return <h1>Hallo Welt!</h1>;
};

// 2. Event Handler
<button onClick={() => setCount(count + 1)}>
    Klick mich
</button>

// 3. Array-Methoden
items.map(item => <li>{item}</li>)

// 4. Kurzform für Komponenten
const Greeting = ({ name }) => <h1>Hallo {name}!</h1>;
```

### Übung 3: Arrow Functions schreiben

> **Ziel:** Arrow Function Syntax verinnerlichen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Alle 4 Funktionen funktionieren und du die Kurzschreibweisen kennst

**Aufgabe:**

Schreibe folgende Funktionen als Arrow Functions und teste sie in der Konsole:

1. Eine Funktion `square`, die eine Zahl quadriert
2. Eine Funktion `isEven`, die prüft ob eine Zahl gerade ist
3. Eine Funktion `greet`, die einen Namen nimmt und "Hallo [Name]!" zurückgibt
4. Eine Funktion `createProduct`, die name und price nimmt und ein Object zurückgibt

```javascript
// Deine Lösungen hier:
const square = // ...
const isEven = // ...
const greet = // ...
const createProduct = // ...

// Teste sie:
console.log(square(5));           // 25
console.log(isEven(4));           // true
console.log(isEven(7));           // false
console.log(greet("Max"));        // "Hallo Max!"
console.log(createProduct("Laptop", 999));  // { name: "Laptop", price: 999 }
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// 1. Zahl quadrieren
const square = x => x * x;
// oder: const square = (x) => x * x;

// 2. Gerade Zahl prüfen
const isEven = x => x % 2 === 0;
// oder: const isEven = (x) => x % 2 === 0;

// 3. Begrüßung
const greet = name => `Hallo ${name}!`;
// oder mit Klammern: const greet = (name) => `Hallo ${name}!`;

// 4. Product Object erstellen
const createProduct = (name, price) => ({ name: name, price: price });
// Kurzschreibweise: const createProduct = (name, price) => ({ name, price });

// Testen:
console.log(square(5));           // 25
console.log(isEven(4));           // true
console.log(isEven(7));           // false
console.log(greet("Max"));        // "Hallo Max!"
console.log(createProduct("Laptop", 999));  // { name: "Laptop", price: 999 }
```

</details>

---

## Teil 7: Template Literals - String-Interpolation

### Python f-Strings → JavaScript Template Literals

**Python:**
```python
name = "Max"
age = 25
message = f"Hallo, ich bin {name} und {age} Jahre alt."
```

**JavaScript:**
```javascript
const name = "Max";
const age = 25;
const message = `Hallo, ich bin ${name} und ${age} Jahre alt.`;
//              ↑ Backticks!      ↑ ${}
```

### Wichtig: Backticks verwenden!

```javascript
// ✅ Richtig: Backticks (` `) für Template Literals
const greeting = `Hallo ${name}!`;

// ❌ Falsch: Normale Anführungszeichen
const wrong = "Hallo ${name}!";  // Gibt wörtlich "${name}" aus
```

**Wo ist die Backtick-Taste?**

Die Position variiert je nach Tastatur-Layout:
- **Deutsche Tastatur (Windows):** Shift + Taste rechts neben ß (Akzent-Taste), dann Leertaste
- **Mac (deutsche Tastatur):** Shift + Taste neben Backspace
- **Notlösung:** Kopiere dieses Zeichen: ` (Backtick)

> **Tipp:** Falls du Probleme hast, kopiere einfach einen Backtick aus einem Codebeispiel!

### Features von Template Literals

```javascript
// 1. Variablen einfügen
const greeting = `Hallo ${name}!`;

// 2. Ausdrücke/Berechnungen
const total = `Summe: ${price * quantity} €`;
const status = `Status: ${isActive ? "Aktiv" : "Inaktiv"}`;

// 3. Funktionsaufrufe
const upper = `Name: ${name.toUpperCase()}`;

// 4. Mehrzeilige Strings (ohne \n!)
const html = `
  <div>
    <h1>${title}</h1>
    <p>${content}</p>
  </div>
`;
```

### Vergleich mit String-Konkatenation

```javascript
// ❌ Umständlich: String-Konkatenation
const message = "Hallo " + name + ", du bist " + age + " Jahre alt.";

// ✅ Elegant: Template Literal
const message = `Hallo ${name}, du bist ${age} Jahre alt.`;
```

### Übung 4: Template Literals

> **Ziel:** String-Interpolation mit Backticks beherrschen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du Variablen und Ausdrücke in Strings einbetten kannst

**Aufgabe:**

Erstelle mit Template Literals:

```javascript
const vorname = "Anna";
const nachname = "Schmidt";
const punkte = 85;
const maxPunkte = 100;

// 1. Vollständiger Name
const vollername = // "Anna Schmidt"

// 2. Prozent berechnen und anzeigen
const prozent = // "Ergebnis: 85%"

// 3. Bewertung mit Bedingung
const bewertung = // "Bestanden" wenn >= 50, sonst "Nicht bestanden"

// 4. Mehrzeilige Ausgabe
const zusammenfassung = // Mehrere Zeilen mit allen Infos
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
const vorname = "Anna";
const nachname = "Schmidt";
const punkte = 85;
const maxPunkte = 100;

// 1. Vollständiger Name
const vollername = `${vorname} ${nachname}`;
console.log(vollername);  // "Anna Schmidt"

// 2. Prozent berechnen und anzeigen
const prozent = `Ergebnis: ${Math.round(punkte / maxPunkte * 100)}%`;
console.log(prozent);  // "Ergebnis: 85%"

// 3. Bewertung mit Bedingung (Ternary Operator)
const bewertung = punkte >= 50 ? "Bestanden" : "Nicht bestanden";
console.log(bewertung);  // "Bestanden"

// 4. Mehrzeilige Ausgabe
const zusammenfassung = `
Teilnehmer: ${vollername}
Punkte: ${punkte} von ${maxPunkte}
Prozent: ${Math.round(punkte / maxPunkte * 100)}%
Status: ${bewertung}
`;
console.log(zusammenfassung);
```

</details>

---

## Teil 8: Ternary Operator - Kurzform für if/else

### Die Syntax

```javascript
// condition ? valueIfTrue : valueIfFalse

const status = age >= 18 ? "Erwachsen" : "Kind";
```

### Vergleich mit if/else

```javascript
// ❌ Mit if/else (länger)
let message;
if (isLoggedIn) {
    message = "Willkommen!";
} else {
    message = "Bitte einloggen";
}

// ✅ Mit Ternary (kürzer)
const message = isLoggedIn ? "Willkommen!" : "Bitte einloggen";
```

### Warum ist das für React wichtig?

In JSX (React's Syntax) kannst du kein `if/else` schreiben. Stattdessen verwendest du den Ternary Operator:

```javascript
// React-Komponente
const App = () => {
    const isLoggedIn = true;

    return (
        <div>
            {isLoggedIn ? <Dashboard /> : <LoginForm />}
        </div>
    );
};
```

### Praktische Beispiele

```javascript
// 1. Einfache Bedingung
const status = count > 0 ? "Aktiv" : "Leer";

// 2. Mit Zahlen
const discount = isPremium ? 20 : 0;

// 3. CSS-Klassen (sehr häufig in React!)
const className = isActive ? "button active" : "button";

// 4. Verschachtelt (sparsam verwenden!)
const grade = score >= 90 ? "A"
            : score >= 80 ? "B"
            : score >= 70 ? "C"
            : "F";
```

### Wissensfrage 3

Was gibt dieser Code aus?

```javascript
const temperature = 25;
const weather = temperature > 30 ? "heiß" : temperature > 20 ? "warm" : "kalt";
console.log(weather);
```

<details>
<summary>Antwort anzeigen</summary>

**Ausgabe: "warm"**

Erklärung:
1. `temperature > 30` → `25 > 30` → `false`
2. Da false, gehe zum else-Teil: `temperature > 20 ? "warm" : "kalt"`
3. `temperature > 20` → `25 > 20` → `true`
4. Da true, nimm "warm"

**Tipp:** Verschachtelte Ternary-Operatoren können schwer lesbar sein. Bei mehr als einer Verschachtelung ist `if/else` oft besser.

</details>

---

## Teil 9: Logical Operators - &&, ||, ??

### Diese drei Operatoren brauchst du ständig in React!

| Operator | Name | Verwendung |
|----------|------|------------|
| `&&` | AND | Bedingtes Rendern |
| `||` | OR | Fallback-Werte |
| `??` | Nullish Coalescing | Fallback nur für null/undefined |

### && (AND) - Bedingtes Rendern

```javascript
// Gibt den rechten Wert zurück, wenn links truthy ist
true && "Hallo"    // "Hallo"
false && "Hallo"   // false

// In React: Bedingt etwas anzeigen
{isAdmin && <AdminPanel />}
// Wenn isAdmin true ist, zeige AdminPanel
// Wenn isAdmin false ist, zeige nichts

// Praktische Beispiele:
const result = user && user.name;  // user.name nur wenn user existiert
{items.length > 0 && <ItemList items={items} />}
```

### || (OR) - Fallback-Werte

```javascript
// Gibt den ersten truthy Wert zurück
null || "Default"      // "Default"
"Wert" || "Default"    // "Wert"
0 || "Default"         // "Default"  ⚠️ 0 ist falsy!
"" || "Default"        // "Default"  ⚠️ "" ist falsy!

// Default-Werte setzen
const name = user.name || "Gast";
const port = config.port || 3000;
```

### ?? (Nullish Coalescing) - Besserer Fallback

```javascript
// Fallback NUR bei null oder undefined
null ?? "Default"      // "Default"
undefined ?? "Default" // "Default"
0 ?? "Default"         // 0  ✅ 0 wird nicht ersetzt!
"" ?? "Default"        // "" ✅ "" wird nicht ersetzt!

// Besser als || wenn 0 oder "" gültige Werte sind
const count = items.count ?? 0;     // Wenn count null/undefined, dann 0
const name = user.name ?? "Gast";   // Wenn name null/undefined, dann "Gast"

// Typisches React-Beispiel:
const label = props.label ?? "Standard-Label";
const maxItems = props.limit ?? 10;  // 0 wäre gültig!
```

### Falsy Values in JavaScript

Diese Werte sind "falsy" (werden in Boolean-Kontext zu false):

```javascript
false      // Boolean false
0          // Zahl Null
""         // Leerer String
null       // Explizit leer
undefined  // Nicht definiert
NaN        // Not a Number
```

**Wichtig:** `||` reagiert auf ALLE falsy Values, `??` nur auf `null` und `undefined`!

### Übung 5: Logical Operators

> **Ziel:** `&&`, `||` und `??` für React-Patterns verstehen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du vorhersagen kannst, was `&&`/`||`/`??` zurückgeben

**Aufgabe:**

Was geben diese Ausdrücke zurück? Überlege erst, dann teste in der Konsole:

```javascript
// && (AND)
console.log(true && "Hallo");
console.log(false && "Hallo");
console.log("Max" && "Anna");
console.log(null && "Test");

// || (OR)
console.log(null || "Default");
console.log("Wert" || "Default");
console.log(0 || 100);
console.log("" || "Leer");

// ?? (Nullish)
console.log(null ?? "Default");
console.log(0 ?? 100);
console.log("" ?? "Leer");
console.log(undefined ?? "Fallback");
```

<details>
<summary>Lösungen anzeigen</summary>

```javascript
// && (AND) - gibt rechten Wert wenn links truthy, sonst linken
true && "Hallo"     // "Hallo" (true ist truthy)
false && "Hallo"    // false (false ist falsy)
"Max" && "Anna"     // "Anna" ("Max" ist truthy)
null && "Test"      // null (null ist falsy)

// || (OR) - gibt ersten truthy Wert
null || "Default"   // "Default" (null ist falsy)
"Wert" || "Default" // "Wert" ("Wert" ist truthy)
0 || 100            // 100 (0 ist falsy!)
"" || "Leer"        // "Leer" ("" ist falsy!)

// ?? (Nullish) - Fallback nur bei null/undefined
null ?? "Default"       // "Default"
0 ?? 100                // 0 (0 ist NICHT null/undefined)
"" ?? "Leer"            // "" ("" ist NICHT null/undefined)
undefined ?? "Fallback" // "Fallback"
```

**Merke:**
- `||` ersetzt 0 und "" (weil falsy)
- `??` behält 0 und "" (nur null/undefined werden ersetzt)

</details>

---

## Teil 10: Callback Functions

### Was ist ein Callback?

Eine **Callback-Funktion** ist eine Funktion, die als Argument an eine andere Funktion übergeben wird:

```javascript
// Die Funktion wird ÜBERGEBEN, nicht aufgerufen
doSomething(callback);  // callback ohne ()

// Die andere Funktion ruft den Callback später auf
function doSomething(callback) {
    // ... mach was ...
    callback();  // Hier wird der Callback aufgerufen
}
```

### Python-Vergleich

Du kennst das Konzept bereits:

```python
# Python: sorted mit key-Funktion
sorted(users, key=lambda x: x['name'])

# Python: FastAPI Route-Handler
@app.get("/users")
def get_users():  # Diese Funktion ist ein "Callback"
    return users
```

### Beispiel 1: setTimeout

```javascript
// setTimeout ruft die Funktion nach X Millisekunden auf
setTimeout(() => {
    console.log("2 Sekunden vorbei!");
}, 2000);

console.log("Das kommt zuerst!");
// Ausgabe:
// "Das kommt zuerst!"
// (nach 2 Sekunden) "2 Sekunden vorbei!"
```

### Beispiel 2: Array.forEach

```javascript
const numbers = [1, 2, 3];

// forEach ruft den Callback für jedes Element auf
numbers.forEach((num) => {
    console.log(num * 2);
});
// Ausgabe: 2, 4, 6
```

### Beispiel 3: Event Handler in React

```javascript
// Die Arrow Function ist ein Callback!
<button onClick={() => setCount(count + 1)}>
    Klick mich
</button>

// onClick erwartet eine Funktion, die bei Klick aufgerufen wird
// Das ist wie: button.addEventListener("click", () => setCount(count + 1))
```

### Wissensfrage 4

Was ist der Unterschied zwischen diesen beiden Zeilen?

```javascript
// Version A
setTimeout(sayHello, 1000);

// Version B
setTimeout(sayHello(), 1000);
```

<details>
<summary>Antwort anzeigen</summary>

**Version A: Korrekt**
- `sayHello` (ohne Klammern) übergibt die Funktion selbst
- setTimeout wird diese Funktion nach 1 Sekunde aufrufen

**Version B: Falsch**
- `sayHello()` (mit Klammern) ruft die Funktion SOFORT auf
- Das Ergebnis des Aufrufs (z.B. `undefined`) wird an setTimeout übergeben
- Nach 1 Sekunde versucht setTimeout `undefined()` aufzurufen → Fehler!

**Merke:** Callbacks werden ohne `()` übergeben!

</details>

---

## Teil 11: Console & DevTools Debugging

### Dein wichtigstes Debugging-Werkzeug

Die Browser Console ist wie `print()` in Python - nur viel mächtiger!

**Console öffnen:**
- Windows/Linux: `F12` oder `Strg + Shift + I`
- Mac: `Cmd + Option + I`

### console.log() - Die Basics

```javascript
// Basis-Ausgabe (wie print in Python)
console.log("Hallo Welt!");

// Mehrere Werte
console.log("Name:", name, "Alter:", age);

// Mit Template Literal
console.log(`User: ${name}, Alter: ${age}`);

// Object ausgeben
console.log(user);
console.log("User:", user);
```

### Weitere nützliche Console-Methoden

```javascript
// Warnung (gelb)
console.warn("Achtung: Dieser Wert ist deprecated!");

// Fehler (rot)
console.error("Fehler: User nicht gefunden!");

// Tabelle für Arrays/Objects (sehr nützlich!)
const users = [
    { name: "Max", age: 25 },
    { name: "Anna", age: 30 }
];
console.table(users);

// Gruppierte Ausgabe
console.group("User Details");
console.log("Name:", user.name);
console.log("Email:", user.email);
console.groupEnd();

// Zeit messen
console.time("Laden");
// ... Code der Zeit braucht ...
console.timeEnd("Laden");  // "Laden: 123ms"
```

### Übung 6: Console-Debugging

> **Ziel:** console.log und andere Console-Methoden kennenlernen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Du eine .js-Datei mit Node ausführen und verschiedene Console-Methoden nutzen kannst

**Aufgabe:**

Erstelle eine JavaScript-Datei `uebung.js` mit folgendem Inhalt und führe sie mit Node.js aus:

```javascript
// uebung.js

// 1. Verschiedene Datentypen loggen
const name = "Max";
const age = 25;
const isActive = true;
const hobbies = ["Coding", "Gaming", "Lesen"];
const user = { name, age, isActive, hobbies };

console.log("=== Variablen ===");
console.log("Name:", name);
console.log("Alter:", age);
console.log("Aktiv:", isActive);
console.log("Hobbies:", hobbies);

// 2. Object als Tabelle
console.log("\n=== User als Object ===");
console.log(user);

// 3. Array als Tabelle
console.log("\n=== Mehrere User als Tabelle ===");
const users = [
    { name: "Max", age: 25, city: "Berlin" },
    { name: "Anna", age: 30, city: "Hamburg" },
    { name: "Tom", age: 28, city: "München" }
];
console.table(users);

// 4. Warn und Error
console.log("\n=== Warnungen & Fehler ===");
console.warn("Das ist eine Warnung!");
console.error("Das ist ein Fehler!");

// 5. Template Literal für formatierte Ausgabe
console.log("\n=== Formatierte Ausgabe ===");
console.log(`
Profil von ${user.name}:
- Alter: ${user.age} Jahre
- Status: ${user.isActive ? "Aktiv" : "Inaktiv"}
- Hobbies: ${user.hobbies.join(", ")}
`);
```

Führe aus mit:
```bash
node uebung.js
```

---

## Teil 12: JavaScript in HTML einbinden

### Drei Wege, JavaScript einzubinden

```html
<!-- 1. Inline Script (nicht empfohlen) -->
<script>
    console.log("Hallo Welt!");
</script>

<!-- 2. Externes Script (empfohlen) -->
<script src="app.js"></script>

<!-- 3. Mit defer (Best Practice) -->
<script src="app.js" defer></script>
```

### Warum defer?

```html
<!-- Im <head> MIT defer - Best Practice! -->
<!DOCTYPE html>
<html>
<head>
    <script src="app.js" defer></script>
</head>
<body>
    <h1 id="title">Hallo</h1>
</body>
</html>
```

**Vorteile von `defer`:**
- Script lädt **parallel** zum HTML-Parsing
- Ausführung erst **nach** vollständigem HTML-Parsing
- DOM ist garantiert verfügbar
- Keine "Element not found" Fehler
- Scripts behalten ihre Reihenfolge

**Ohne defer:** Das Script blockiert das HTML-Parsing!

### Übung 7: Erste interaktive HTML-Seite

> **Ziel:** JavaScript in HTML einbinden und DOM-Manipulation kennenlernen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Die Seite eine personalisierte Begrüßung zeigt und der Button auf Klicks reagiert

**Aufgabe:**

Erstelle folgende zwei Dateien im gleichen Ordner:

**index.html:**
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine erste JS-Seite</title>
    <script src="app.js" defer></script>
</head>
<body>
    <h1>JavaScript Übung</h1>
    <p id="greeting">Warte auf JavaScript...</p>
    <p id="time"></p>
    <button id="btn">Klick mich!</button>
</body>
</html>
```

**app.js:**
```javascript
// 1. Variablen definieren
const name = "Max";
const now = new Date();
const hours = now.getHours();

// 2. Begrüßung basierend auf Tageszeit
let greeting;
if (hours < 12) {
    greeting = "Guten Morgen";
} else if (hours < 18) {
    greeting = "Guten Tag";
} else {
    greeting = "Guten Abend";
}

// 3. DOM-Elemente aktualisieren
document.getElementById("greeting").textContent = `${greeting}, ${name}!`;
document.getElementById("time").textContent = `Es ist ${hours}:${now.getMinutes()} Uhr.`;

// 4. Button mit Event Handler
const button = document.getElementById("btn");
let clickCount = 0;

button.addEventListener("click", () => {
    clickCount++;
    button.textContent = `${clickCount}x geklickt!`;
    console.log(`Button wurde ${clickCount}x geklickt`);
});

// 5. In der Console loggen
console.log("Script geladen!");
console.log("Aktuelle Stunde:", hours);
console.log("Begrüßung:", greeting);
```

**Schritte:**
1. Erstelle beide Dateien
2. Öffne `index.html` im Browser (Doppelklick oder mit Live Server)
3. Öffne die DevTools (F12) und beobachte die Console
4. Klicke den Button mehrfach

---

## Teil 13: Kontrollstrukturen (Kurz-Recap)

Diese Strukturen kennst du von Python - hier die JavaScript-Syntax:

### if / else

```javascript
// JavaScript: Geschweifte Klammern statt Einrückung
if (age >= 18) {
    console.log("Volljährig");
} else if (age >= 16) {
    console.log("Fast volljährig");
} else {
    console.log("Minderjährig");
}

// Python zum Vergleich:
// if age >= 18:
//     print("Volljährig")
// elif age >= 16:
//     print("Fast volljährig")
// else:
//     print("Minderjährig")
```

### for-Schleife

```javascript
// Klassische for-Schleife
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for...of iteriert über WERTE (wie Python: for item in items)
const items = ["a", "b", "c"];
for (const item of items) {
    console.log(item);  // "a", "b", "c"
}

// Python zum Vergleich:
// for item in items:
//     print(item)

// ACHTUNG: for...in iteriert über KEYS/INDICES (nicht verwenden für Arrays!)
// for (const index in items) {
//     console.log(index);  // "0", "1", "2" (Strings!)
// }
// → Verwende for...of oder Array-Methoden wie .forEach()
```

### while-Schleife

```javascript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
```

### Wichtiger Hinweis für React

In React verwendet man **selten** klassische Schleifen. Stattdessen nutzt man **Array-Methoden**:

```javascript
// Statt for-Schleife:
const items = [1, 2, 3];
const doubled = items.map(x => x * 2);  // [2, 4, 6]

// In React-Komponenten:
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

Das lernst du morgen im Detail!

---

## Teil 14: Praktische Gesamtübung

### Aufgabe: User-Profil-Manager

Erstelle ein kleines Programm, das alle gelernten Konzepte kombiniert:

```javascript
// user-manager.js

// ==============================
// 1. VARIABLEN
// ==============================
// Erstelle User-Daten mit const
const currentUser = {
    name: "Max Mustermann",
    email: "max@example.com",
    age: 25,
    isPremium: true,
    loginCount: null  // Noch keine Logins gezählt
};

// ==============================
// 2. FUNKTIONEN (Arrow Functions)
// ==============================
// Funktion: Vollständige Begrüßung erstellen
const createGreeting = (user) => {
    // Verwende Ternary für Premium-Status
    const status = user.isPremium ? "Premium" : "Standard";

    // Verwende Template Literal
    return `Willkommen, ${user.name}! (${status}-Mitglied)`;
};

// Funktion: Altersgruppe bestimmen
// HINWEIS: Diese Funktion gibt aktuell undefined zurück!
// Das siehst du in der Ausgabe als "undefined" - das ist gewollt.
// Deine Aufgabe: Implementiere die Funktion, damit sie einen String zurückgibt.
const getAgeGroup = (age) => {
    // Dein Code hier:
    // < 18: "Minderjährig"
    // 18-30: "Junge Erwachsene"
    // 31-50: "Erwachsene"
    // > 50: "Senioren"
};

// Funktion: Sichere Login-Anzahl abrufen
const getLoginCount = (user) => {
    // Verwende ?? für null/undefined
    return user.loginCount ?? 0;
};

// ==============================
// 3. AUSGABE
// ==============================
console.log("=== User Profil ===");
console.log(createGreeting(currentUser));
console.log(`Alter: ${currentUser.age} (${getAgeGroup(currentUser.age)})`);
console.log(`Logins: ${getLoginCount(currentUser)}`);

// ==============================
// 4. BEDINGTES RENDERN (Vorschau auf React)
// ==============================
// Verwende && für bedingte Ausgabe
currentUser.isPremium && console.log("[Premium] Features freigeschaltet!");

// Verwende || für Fallback
const displayName = currentUser.nickname || currentUser.name;
console.log(`Anzeigename: ${displayName}`);

// ==============================
// 5. BONUS: Mehrere User verarbeiten
// ==============================
const users = [
    { name: "Anna", age: 28, isPremium: true },
    { name: "Tom", age: 17, isPremium: false },
    { name: "Lisa", age: 45, isPremium: true }
];

console.log("\n=== Alle User ===");
// Verwende forEach mit Callback
users.forEach((user) => {
    console.log(`${user.name}: ${getAgeGroup(user.age)}`);
});
```

**Deine Aufgabe:**

1. Vervollständige die `getAgeGroup`-Funktion
2. Führe das Programm aus: `node user-manager.js`
3. Füge einen weiteren User zum `users`-Array hinzu
4. Erstelle eine neue Funktion `isAdult`, die true/false zurückgibt

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// Funktion: Altersgruppe bestimmen
const getAgeGroup = (age) => {
    if (age < 18) {
        return "Minderjährig";
    } else if (age <= 30) {
        return "Junge Erwachsene";
    } else if (age <= 50) {
        return "Erwachsene";
    } else {
        return "Senioren";
    }
};

// Oder kürzer mit Ternary (aber weniger lesbar):
const getAgeGroupShort = (age) =>
    age < 18 ? "Minderjährig" :
    age <= 30 ? "Junge Erwachsene" :
    age <= 50 ? "Erwachsene" : "Senioren";

// Bonus: isAdult Funktion
const isAdult = (age) => age >= 18;

// Test:
console.log(isAdult(25));  // true
console.log(isAdult(16));  // false
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Thema | Python | JavaScript | Beispiel |
|-------|--------|------------|----------|
| **Variablen** | `name = "Max"` | `const name = "Max";` | Immer `const`, nur `let` wenn nötig |
| **Funktionen** | `def fn():` | `const fn = () => {}` | Arrow Functions für React |
| **Strings** | `f"Hallo {x}"` | `` `Hallo ${x}` `` | Backticks + ${} |
| **Bedingung** | `if x else y` | `x ? a : b` | Ternary Operator |
| **And/Or** | `and`, `or` | `&&`, `||`, `??` | Logical Operators |
| **Vergleich** | `==` | `===` | Immer strict equality |
| **Print** | `print()` | `console.log()` | DevTools Console |

### Faustregeln

1. **Immer `const`** verwenden, nur `let` wenn der Wert sich ändern muss
2. **Niemals `var`** verwenden
3. **Immer `===`** statt `==` für Vergleiche
4. **Arrow Functions** sind der React-Standard
5. **Template Literals** mit Backticks für String-Interpolation
6. **`console.log()`** ist dein bester Debugging-Freund

### Vorbereitung auf morgen

Morgen lernst du **Arrays, Objects & Moderne Patterns**:
- Spread Operator: `[...arr]`, `{...obj}`
- Destructuring: `const [a, b] = arr`
- Array Methods: `map()`, `filter()`, `find()`
- ES6 Modules: `import`/`export`

Nach morgen verstehst du Code wie:
```javascript
const [count, setCount] = useState(0);
const newArray = [...items, newItem];
const { name, age } = user;
```

---

## Bonus: Schnellreferenz

### Variablen
```javascript
const name = "Max";      // Konstante (bevorzugt)
let count = 0;           // Veränderlich
// var - NICHT VERWENDEN!
```

### Datentypen
```javascript
"String"                 // String
42, 3.14                 // Number
true, false              // Boolean
null                     // Absichtlich leer
undefined                // Nicht definiert
{ key: "value" }         // Object
[1, 2, 3]               // Array
() => {}                 // Function
```

### Arrow Functions
```javascript
const fn = () => "Hi";              // Ohne Parameter
const fn = x => x * 2;              // Ein Parameter
const fn = (a, b) => a + b;         // Mehrere Parameter
const fn = (x) => {                  // Mehrzeilig
    console.log(x);
    return x * 2;
};
```

### Operatoren
```javascript
// Vergleich (immer ===)
x === y                  // Strict Equal
x !== y                  // Strict Not Equal

// Logical
x && y                   // AND (gibt y wenn x truthy)
x || y                   // OR (gibt x wenn truthy, sonst y)
x ?? y                   // Nullish (y nur wenn x null/undefined)

// Ternary
condition ? a : b        // a wenn true, b wenn false
```

### Template Literals
```javascript
`Hallo ${name}!`         // String-Interpolation
`${a + b}`               // Mit Ausdruck
`Mehrzeilig
erlaubt`                 // Über mehrere Zeilen
```

### Console
```javascript
console.log("Debug");    // Normal
console.warn("Warnung"); // Gelb
console.error("Fehler"); // Rot
console.table(array);    // Tabelle
```

---

## Checkliste

Bevor du mit dem nächsten Tag weitermachst, stelle sicher:

- [ ] Du verstehst den Unterschied zwischen `const` und `let`
- [ ] Du kannst Arrow Functions schreiben
- [ ] Du kennst den Unterschied zwischen `===` und `==`
- [ ] Du kannst Template Literals mit `${}` verwenden
- [ ] Du verstehst `&&`, `||` und `??`
- [ ] Du kannst den Ternary Operator `? :` verwenden
- [ ] Du kannst die Browser Console zum Debuggen nutzen
- [ ] Du weißt, wie man JavaScript in HTML einbindet

**Alles abgehakt?** Dann bist du bereit für Tag 7: Arrays, Objects & Moderne Patterns!
