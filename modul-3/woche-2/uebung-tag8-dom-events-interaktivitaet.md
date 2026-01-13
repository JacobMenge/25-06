# DOM, Events & Interaktivität - Praktische Übungen

## Übersicht

Heute machen wir Webseiten interaktiv – das Fundament für React-Komponenten!

In dieser Übung lernst du:
- **Das DOM verstehen** - Der "Bauplan" der Webseite im Browser
- **Elemente selektieren** - querySelector() und querySelectorAll()
- **DOM manipulieren** - Inhalte ändern, Klassen toggeln, Styles setzen
- **Events** - click, submit, input – auf User-Aktionen reagieren
- **Event Handler** - Callbacks für Interaktivität
- **Formulare** - Daten erfassen und verarbeiten

Diese Übung bereitet dich auf React vor – Event Handling in React funktioniert fast identisch!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Teil 1** | Das DOM verstehen | 10 min |
| **Teil 2** | Elemente selektieren | 15 min |
| **Teil 3** | DOM Manipulation: Inhalte ändern | 15 min |
| **Teil 4** | Klassen & Styles manipulieren | 15 min |
| **Teil 5** | Events & Event Listener | 20 min |
| **Teil 6** | Das Event-Objekt | 15 min |
| **Teil 7** | Formulare & Input Events | 20 min |
| **Teil 8** | Elemente erstellen & einfügen | 20 min |
| **Teil 9** | Event Delegation | 15 min |
| **Teil 10** | Data Attributes | 10 min |
| **Teil 11** | Praxis: Interaktive Todo-Liste | 45 min |
| | **Gesamt** | **ca. 3-4 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 90-120 Minuten die wichtigsten Konzepte:**

1. **Teil 2** - Elemente selektieren - *Grundlage für alles*
2. **Teil 3** - DOM Manipulation - *Inhalte ändern*
3. **Teil 5** - Events & Event Listener - *Interaktivität*
4. **Teil 7** - Formulare - *User-Input verarbeiten*
5. **Teil 11** - Praxis Todo-Liste - *Alles zusammen*

---

## Wichtiger Hinweis zur Arbeitsweise

> **Jeder Teil hat seine eigene JavaScript-Datei!**
>
> Um Fehler durch doppelte Variablen-Deklarationen zu vermeiden, erstelle für jeden Teil eine separate Datei:
> - `teil2.js`, `teil3.js`, `teil4.js`, usw.
>
> In der `index.html` bindest du immer nur **eine** Datei ein:
> ```html
> <!-- Wechsle diese Zeile je nach Teil -->
> <script src="teil3.js" defer></script>
> ```

---

## Projekt-Setup

Erstelle einen neuen Ordner `dom-uebung` mit folgenden Dateien:

### index.html

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM Übungen</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <h1 id="main-title">DOM Übungen</h1>
        <p id="intro" class="text">Willkommen zu den DOM-Übungen!</p>

        <!-- Für Teil 3: Beispiel-Elemente für innerHTML/Attribute -->
        <div id="content">Dieser Inhalt kann geändert werden.</div>
        <img id="demo-image" src="https://via.placeholder.com/150" alt="Beispielbild">

        <div id="demo-section">
            <button id="demo-btn" class="btn">Klick mich!</button>
            <button id="dec-btn" class="btn">-1</button>
            <span id="click-count">0</span> Klicks
        </div>

        <div id="box" class="box">Eine Box zum Stylen</div>

        <ul id="item-list">
            <li class="item" data-id="1">
                <span class="item-text">Erstes Item</span>
                <button class="delete-btn" data-id="1">X</button>
            </li>
            <li class="item" data-id="2">
                <span class="item-text">Zweites Item</span>
                <button class="delete-btn" data-id="2">X</button>
            </li>
            <li class="item" data-id="3">
                <span class="item-text">Drittes Item</span>
                <button class="delete-btn" data-id="3">X</button>
            </li>
        </ul>
    </div>

    <!-- WICHTIG: Wechsle diese Zeile je nach Teil! -->
    <script src="teil3.js" defer></script>
</body>
</html>
```

### style.css

```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f5f5f5;
}

#app {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    margin-bottom: 20px;
    color: #333;
}

.text {
    margin-bottom: 20px;
    color: #666;
}

#content {
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 4px;
}

#demo-image {
    display: block;
    margin-bottom: 20px;
    border-radius: 4px;
}

.btn {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    margin-right: 5px;
}

.btn:hover {
    background-color: #0056b3;
}

.box {
    padding: 20px;
    margin: 20px 0;
    background-color: #e9ecef;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.box.active {
    background-color: #007bff;
    color: white;
}

.box.highlight {
    border: 3px solid #ffc107;
}

#item-list {
    list-style: none;
    margin-top: 20px;
}

.item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    margin: 5px 0;
    background-color: #f8f9fa;
    border-radius: 4px;
    cursor: pointer;
}

.item:hover {
    background-color: #e9ecef;
}

.item.selected {
    background-color: #007bff;
    color: white;
}

.item.done {
    text-decoration: line-through;
    opacity: 0.6;
}

.item-text {
    flex: 1;
}

.delete-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
}

.delete-btn:hover {
    background-color: #c82333;
}

.hidden {
    display: none;
}

.error {
    color: #dc3545;
    font-size: 14px;
}

.success {
    color: #28a745;
    font-size: 14px;
}

/* Demo Section */
#demo-section {
    margin: 20px 0;
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 4px;
}

#click-count {
    font-weight: bold;
    font-size: 24px;
    color: #007bff;
}
```

### app.js (Startdatei)

```javascript
// Hier schreibst du deinen JavaScript-Code
console.log('App geladen!');
```

---

## Teil 1: Das DOM verstehen

### Was ist das DOM?

DOM = **D**ocument **O**bject **M**odel – die Browser-Repräsentation deiner HTML-Seite als Objekt-Baum.

```
HTML Code                          DOM Baum
─────────────────────             ─────────────────────
<!DOCTYPE html>                   document
<html>                              └── html
  <head>                                ├── head
    <title>Seite</title>                │   └── title
  </head>                               └── body
  <body>                                    ├── h1
    <h1>Hallo</h1>                          ├── p#intro
    <p id="intro">Text</p>                  └── button.btn
    <button class="btn">Klick</button>
  </body>
</html>
```

**Wichtig:**
- Jedes HTML-Element wird zu einem "Node" (Knoten) im DOM
- JavaScript kann jeden Node lesen, ändern, löschen oder neue erstellen
- React erstellt einen "Virtual DOM" und updated nur das, was sich ändert

### Wissensfrage 1

Öffne die Browser-Konsole (F12 → Console) und gib ein:

```javascript
console.log(document);
console.log(document.body);
console.log(document.head);
```

Was siehst du? Was ist `document`?

<details>
<summary>Antwort anzeigen</summary>

**`document`** ist das globale Objekt, das die gesamte HTML-Seite repräsentiert.

- `document` → Das gesamte HTML-Dokument
- `document.body` → Das `<body>`-Element
- `document.head` → Das `<head>`-Element

Das `document`-Objekt ist dein Einstiegspunkt für alle DOM-Manipulationen!

</details>

---

## Teil 2: Elemente selektieren

> **Datei:** Erstelle `teil2.js` und binde sie in `index.html` ein.

Um ein Element zu ändern, musst du es erst "finden" – mit Selektoren wie in CSS!

### querySelector() – Ein Element

```javascript
// EIN Element (das erste, das passt)
const btn = document.querySelector('.btn');
const intro = document.querySelector('#intro');
const h1 = document.querySelector('h1');

// Wie CSS-Selektoren!
const firstItem = document.querySelector('.item');
const nested = document.querySelector('#app .box');
```

### querySelectorAll() – Alle Elemente

```javascript
// ALLE passenden Elemente (NodeList)
const allBtns = document.querySelectorAll('.btn');
const allItems = document.querySelectorAll('.item');

// Iteration mit forEach
allItems.forEach(item => console.log(item));
```

### Klassische Methoden

```javascript
// Ältere, aber noch verwendete Methoden
document.getElementById('intro');          // Einzelnes Element
document.getElementsByClassName('btn');    // HTMLCollection
document.getElementsByTagName('p');        // HTMLCollection
```

### Übung 2: Elemente selektieren

> **Ziel:** Elemente mit verschiedenen Selektoren finden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du querySelector() sicher anwenden kannst

Öffne die Browser-Konsole und führe folgende Schritte aus:

```javascript
// ========================================
// TEIL 2: Elemente selektieren
// Datei: teil2.js
// ========================================

// 1. Selektiere das Element mit id="main-title"
const title = // Dein Code hier
console.log('Titel:', title);

// 2. Selektiere das Element mit id="intro"
const introText = // Dein Code hier
console.log('Intro:', introText);

// 3. Selektiere den Button mit id="demo-btn"
const mainButton = // Dein Code hier
console.log('Button:', mainButton);

// 4. Selektiere ALLE Elemente mit class="item"
const allItems = // Dein Code hier
console.log('Alle Items:', allItems);
console.log('Anzahl Items:', allItems.length);

// 5. Selektiere das erste .item innerhalb von #item-list
const firstListItem = // Dein Code hier
console.log('Erstes Item:', firstListItem);
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 2: Elemente selektieren
// Datei: teil2.js
// ========================================

// 1. Element mit id="main-title"
const title = document.querySelector('#main-title');
console.log('Titel:', title);

// 2. Element mit id="intro"
const introText = document.querySelector('#intro');
console.log('Intro:', introText);

// 3. Button mit id="demo-btn"
const mainButton = document.querySelector('#demo-btn');
console.log('Button:', mainButton);

// 4. ALLE Elemente mit class="item"
const allItems = document.querySelectorAll('.item');
console.log('Alle Items:', allItems);
console.log('Anzahl Items:', allItems.length); // 3

// 5. Erstes .item in #item-list
const firstListItem = document.querySelector('#item-list .item');
console.log('Erstes Item:', firstListItem);
```

</details>

### Wissensfrage 2

Was ist der Unterschied zwischen `querySelector()` und `querySelectorAll()`?

<details>
<summary>Antwort anzeigen</summary>

**`querySelector()`:**
- Gibt **ein Element** zurück (das erste, das passt)
- Gibt `null` zurück, wenn nichts gefunden wird

**`querySelectorAll()`:**
- Gibt **alle passenden Elemente** als NodeList zurück
- Gibt eine **leere NodeList** zurück, wenn nichts gefunden wird
- NodeList kann mit `forEach()` durchlaufen werden

```javascript
const btn = document.querySelector('.btn');     // Ein Element oder null
const btns = document.querySelectorAll('.btn'); // NodeList (kann leer sein)
```

</details>

---

## Teil 3: DOM Manipulation - Inhalte ändern

> **Datei:** Erstelle `teil3.js` und binde sie in `index.html` ein.
> **Wichtig:** Kommentiere oder entferne den vorherigen Script-Tag!

Wenn du ein Element hast, kannst du es nach Belieben ändern!

### textContent – Text ändern

```javascript
const h1 = document.querySelector('h1');

// Text lesen
console.log(h1.textContent);  // "DOM Übungen"

// Text ändern
h1.textContent = 'Neuer Titel';
```

### innerHTML – HTML einfügen

```javascript
// Element existiert in unserem HTML als <div id="content">
const contentDiv = document.querySelector('#content');

// HTML einfügen
contentDiv.innerHTML = '<p>Neuer <strong>Inhalt</strong></p>';

// ⚠️ VORSICHT: XSS-Gefahr bei User-Input!
// NIE: element.innerHTML = userInput;
```

### Attribute ändern

```javascript
// Element existiert in unserem HTML als <img id="demo-image">
const img = document.querySelector('#demo-image');

// Attribute setzen
img.setAttribute('src', 'https://via.placeholder.com/200');
img.setAttribute('alt', 'Neues Bild');

// Kurzform für Standard-Attribute
img.src = 'https://via.placeholder.com/200';
img.alt = 'Neues Bild';

// Attribute lesen
console.log(img.src);
console.log(img.getAttribute('alt'));
```

### Übung 3: Inhalte ändern

> **Ziel:** DOM-Elemente mit JavaScript ändern
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du Text und Attribute ändern kannst

```javascript
// ========================================
// TEIL 3: Inhalte ändern
// Datei: teil3.js
// ========================================

// 1. Ändere den Titel
const pageTitle = document.querySelector('#main-title');
// Ändere den Text zu "Meine DOM App"
// Dein Code hier

// 2. Ändere den Intro-Text
const pageIntro = document.querySelector('#intro');
// Ändere den Text zu "JavaScript macht Webseiten interaktiv!"
// Dein Code hier

// 3. Ändere den Button-Text
const demoButton = document.querySelector('#demo-btn');
// Ändere den Text zu "Los geht's!"
// Dein Code hier

// 4. Ändere den Inhalt der Content-Box mit innerHTML
const contentBox = document.querySelector('#content');
// Füge HTML ein: "<strong>Neuer Inhalt!</strong> Mit HTML formatiert."
// Dein Code hier

// 5. Ändere das Bild
const demoImg = document.querySelector('#demo-image');
// Ändere src zu "https://via.placeholder.com/200x100"
// Ändere alt zu "Geändertes Bild"
// Dein Code hier

// 6. Lies den Text der Item-Texte aus und gib sie in der Konsole aus
const itemTexts = document.querySelectorAll('.item-text');
itemTexts.forEach((item, index) => {
    console.log(`Item ${index + 1}:`, item.textContent);
});
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 3: Inhalte ändern
// Datei: teil3.js
// ========================================

// 1. Ändere den Titel
const pageTitle = document.querySelector('#main-title');
pageTitle.textContent = 'Meine DOM App';

// 2. Ändere den Intro-Text
const pageIntro = document.querySelector('#intro');
pageIntro.textContent = 'JavaScript macht Webseiten interaktiv!';

// 3. Ändere den Button-Text
const demoButton = document.querySelector('#demo-btn');
demoButton.textContent = "Los geht's!";

// 4. Ändere den Inhalt der Content-Box mit innerHTML
const contentBox = document.querySelector('#content');
contentBox.innerHTML = '<strong>Neuer Inhalt!</strong> Mit HTML formatiert.';

// 5. Ändere das Bild
const demoImg = document.querySelector('#demo-image');
demoImg.src = 'https://via.placeholder.com/200x100';
demoImg.alt = 'Geändertes Bild';

// 6. Lies den Text der Item-Texte aus
const itemTexts = document.querySelectorAll('.item-text');
itemTexts.forEach((item, index) => {
    console.log(`Item ${index + 1}:`, item.textContent);
});
```

</details>

---

## Teil 4: Klassen & Styles manipulieren

> **Datei:** Erstelle `teil4.js` und binde sie in `index.html` ein.

### classList – Klassen manipulieren

```javascript
const box = document.querySelector('.box');

// Klasse hinzufügen
box.classList.add('active');

// Klasse entfernen
box.classList.remove('hidden');

// Klasse toggeln (an/aus)
box.classList.toggle('highlight');

// Prüfen ob Klasse vorhanden
if (box.classList.contains('active')) {
    console.log('Box ist aktiv!');
}

// Mehrere Klassen auf einmal
box.classList.add('class1', 'class2');
box.classList.remove('class1', 'class2');
```

### style – Inline-Styles setzen

```javascript
const box = document.querySelector('.box');

// Einzelne Styles setzen
box.style.backgroundColor = 'blue';
box.style.color = 'white';
box.style.padding = '20px';
box.style.borderRadius = '8px';

// Achtung: CSS kebab-case → JS camelCase
// background-color → backgroundColor
// border-radius → borderRadius
// font-size → fontSize
```

### Best Practice

```javascript
// ❌ Schlecht: Viele Inline-Styles
box.style.backgroundColor = 'blue';
box.style.color = 'white';
box.style.padding = '20px';

// ✅ Besser: CSS-Klasse definieren und toggeln
box.classList.add('active');
// In CSS: .active { background: blue; color: white; padding: 20px; }
```

### Übung 4: Klassen & Styles

> **Ziel:** Klassen und Styles mit JavaScript steuern
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du classList sicher anwenden kannst

```javascript
// ========================================
// TEIL 4: Klassen & Styles
// Datei: teil4.js
// ========================================

const styleBox = document.querySelector('#box');
const listItems = document.querySelectorAll('.item');

// 1. Füge der Box die Klasse "active" hinzu
// Dein Code hier

// 2. Warte 2 Sekunden, dann entferne "active" wieder
setTimeout(() => {
    // Dein Code hier
    console.log('Active-Klasse entfernt!');
}, 2000);

// 3. Toggle "highlight" bei der Box
// Dein Code hier

// 4. Prüfe, ob die Box die Klasse "box" hat
if (/* Dein Code hier */) {
    console.log('Die Box hat die Klasse "box"');
}

// 5. Füge dem ersten Item die Klasse "selected" hinzu
// Dein Code hier

// 6. Setze einen Inline-Style: Box soll einen blauen Rahmen haben
// Dein Code hier

// 7. Toggle "selected" bei jedem Klick auf ein Item
listItems.forEach(item => {
    item.addEventListener('click', () => {
        // Dein Code hier
    });
});
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 4: Klassen & Styles
// Datei: teil4.js
// ========================================

const styleBox = document.querySelector('#box');
const listItems = document.querySelectorAll('.item');

// 1. Füge der Box die Klasse "active" hinzu
styleBox.classList.add('active');

// 2. Warte 2 Sekunden, dann entferne "active" wieder
setTimeout(() => {
    styleBox.classList.remove('active');
    console.log('Active-Klasse entfernt!');
}, 2000);

// 3. Toggle "highlight" bei der Box
styleBox.classList.toggle('highlight');

// 4. Prüfe, ob die Box die Klasse "box" hat
if (styleBox.classList.contains('box')) {
    console.log('Die Box hat die Klasse "box"');
}

// 5. Füge dem ersten Item die Klasse "selected" hinzu
listItems[0].classList.add('selected');

// 6. Setze einen Inline-Style: Box soll einen blauen Rahmen haben
styleBox.style.border = '3px solid blue';

// 7. Toggle "selected" bei jedem Klick auf ein Item
listItems.forEach(item => {
    item.addEventListener('click', () => {
        item.classList.toggle('selected');
    });
});
```

</details>

---

## Teil 5: Events & Event Listener

> **Datei:** Erstelle `teil5.js` und binde sie in `index.html` ein.

Events sind "Signale" vom Browser: Klicks, Tastatureingaben, Formular-Submits, etc.

### Wichtige Event-Typen

| Kategorie | Events |
|-----------|--------|
| **Maus** | `click`, `dblclick`, `mouseenter`, `mouseleave` |
| **Tastatur** | `keydown`, `keyup`, `keypress` |
| **Formular** | `submit`, `input`, `change`, `focus`, `blur` |
| **Window** | `load`, `resize`, `scroll` |

### addEventListener() – Der moderne Weg

```javascript
const btn = document.querySelector('button');

// Event Listener hinzufügen
btn.addEventListener('click', () => {
    console.log('Button geklickt!');
});

// Mit benannter Funktion
function handleClick() {
    console.log('Geklickt!');
}
btn.addEventListener('click', handleClick);

// Listener wieder entfernen (nur mit benannter Funktion möglich!)
btn.removeEventListener('click', handleClick);
```

### Übung 5: Events

> **Ziel:** Event Listener hinzufügen und auf Klicks reagieren
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du einen funktionierenden Counter gebaut hast

Erstelle einen Counter, der bei Klick hochzählt:

```javascript
// ========================================
// TEIL 5: Counter mit Events
// Datei: teil5.js
// ========================================

// Elemente selektieren
const incrementBtn = document.querySelector('#demo-btn');
const decrementBtn = document.querySelector('#dec-btn');
const countDisplay = document.querySelector('#click-count');

// State (Zähler-Variable)
let counter = 0;

// 1. Füge einen click Event Listener zum Increment-Button hinzu
// Bei jedem Klick soll:
// - counter um 1 erhöht werden
// - die Anzeige aktualisiert werden
incrementBtn.addEventListener('click', () => {
    // Dein Code hier
});

// 2. Füge einen click Event Listener zum Decrement-Button hinzu
// Bei jedem Klick soll:
// - counter um 1 verringert werden (aber nicht unter 0!)
// - die Anzeige aktualisiert werden
decrementBtn.addEventListener('click', () => {
    // Dein Code hier
});

// 3. Bonus: Zeige eine Nachricht wenn counter 10 erreicht
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 5: Counter mit Events
// Datei: teil5.js
// ========================================

// Elemente selektieren
const incrementBtn = document.querySelector('#demo-btn');
const decrementBtn = document.querySelector('#dec-btn');
const countDisplay = document.querySelector('#click-count');

// State
let counter = 0;

// 1. Increment Button
incrementBtn.addEventListener('click', () => {
    counter++;
    countDisplay.textContent = counter;

    // 3. Bonus: Nachricht bei 10
    if (counter === 10) {
        alert('Du hast 10 erreicht!');
    }
});

// 2. Decrement Button mit Minimum 0
decrementBtn.addEventListener('click', () => {
    if (counter > 0) {
        counter--;
        countDisplay.textContent = counter;
    }
});
```

**React-Vergleich:**

```javascript
// Das gleiche in React - sehr ähnlich!
function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <span>{count}</span>
            <button onClick={() => setCount(count + 1)}>+1</button>
            <button onClick={() => setCount(Math.max(0, count - 1))}>-1</button>
        </div>
    );
}
```

</details>

---

## Teil 6: Das Event-Objekt

> **Datei:** Erstelle `teil6.js` und binde sie in `index.html` ein.

Jeder Event Handler bekommt ein Event-Objekt mit nützlichen Infos.

### Event-Objekt nutzen

```javascript
btn.addEventListener('click', (e) => {
    console.log(e);                    // Das gesamte Event-Objekt
    console.log(e.type);               // 'click'
    console.log(e.target);             // Das geklickte Element
    console.log(e.currentTarget);      // Element mit dem Listener
    console.log(e.clientX, e.clientY); // Mausposition
});
```

### Wichtige Methoden

```javascript
// Standard-Verhalten verhindern
form.addEventListener('submit', (e) => {
    e.preventDefault();  // Kein Seiten-Reload!
    // Eigene Logik...
});

// Link-Klick verhindern
link.addEventListener('click', (e) => {
    e.preventDefault();  // Nicht zur URL navigieren
    console.log('Link geklickt, aber nicht gefolgt');
});

// Event-Bubbling stoppen
child.addEventListener('click', (e) => {
    e.stopPropagation();  // Parent bekommt Event nicht
});
```

### Übung 6: Event-Objekt

> **Ziel:** Das Event-Objekt verstehen und nutzen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du e.target und e.preventDefault() nutzen kannst

```javascript
// ========================================
// TEIL 6: Event-Objekt
// Datei: teil6.js
// ========================================

const clickBox = document.querySelector('#box');

// 1. Bei Klick auf die Box: Zeige die Mausposition an
clickBox.addEventListener('click', (e) => {
    // Gib e.clientX und e.clientY in der Konsole aus
    // Dein Code hier

    // Zeige die Position auch in der Box an
    // Dein Code hier
});

// 2. Bei Klick auf ein Item: Zeige an, welches Item geklickt wurde
// Nutze Event Delegation auf der Liste
const itemListEl = document.querySelector('#item-list');

itemListEl.addEventListener('click', (e) => {
    // Prüfe ob ein .item-text geklickt wurde
    if (e.target.classList.contains('item-text')) {
        // Gib den Text des geklickten Items aus
        // Dein Code hier
    }
});

// 3. Wissensfrage: Was ist der Unterschied zwischen e.target und e.currentTarget?
// Antwort in der Konsole ausgeben nach Nachdenken!
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 6: Event-Objekt
// Datei: teil6.js
// ========================================

const clickBox = document.querySelector('#box');

// 1. Mausposition bei Klick
clickBox.addEventListener('click', (e) => {
    console.log(`Klick bei X: ${e.clientX}, Y: ${e.clientY}`);
    clickBox.textContent = `Klick bei X: ${e.clientX}, Y: ${e.clientY}`;
});

// 2. Geklicktes Item anzeigen (Event Delegation)
const itemListEl = document.querySelector('#item-list');

itemListEl.addEventListener('click', (e) => {
    if (e.target.classList.contains('item-text')) {
        console.log('Geklickter Text:', e.target.textContent);
    }
});

// 3. Unterschied e.target vs e.currentTarget:
// - e.target: Das Element, das TATSÄCHLICH geklickt wurde
// - e.currentTarget: Das Element, an dem der Listener hängt
// Bei Event Delegation kann das unterschiedlich sein!
console.log('e.target = tatsächlich geklicktes Element');
console.log('e.currentTarget = Element mit dem Listener');
```

</details>

---

## Teil 7: Formulare & Input Events

> **Datei:** Erstelle `teil7.js` und binde sie in `index.html` ein.

Formulare sind essentiell für User-Input!

### Formular-Submit verarbeiten

```javascript
const form = document.querySelector('#myForm');

form.addEventListener('submit', (e) => {
    e.preventDefault();  // WICHTIG: Verhindert Seiten-Reload!

    // Werte auslesen
    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;

    console.log('Login:', { email, password });

    // Hier würde normalerweise ein API-Call kommen
});
```

### Input Events: Live-Feedback

```javascript
const searchInput = document.querySelector('#search');

// Bei JEDER Eingabe (Tastendruck)
searchInput.addEventListener('input', (e) => {
    const query = e.target.value;
    console.log('Suche nach:', query);
});

// Nur wenn Feld verlassen wird
searchInput.addEventListener('change', (e) => {
    console.log('Eingabe abgeschlossen:', e.target.value);
});
```

### Übung 7: Formular bauen

> **Ziel:** Ein Formular mit JavaScript verarbeiten
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du Formular-Daten auslesen kannst

Füge dieses HTML zu deiner `index.html` hinzu (innerhalb von `#app`):

```html
<!-- Füge dies in index.html ein, vor dem schließenden </div> von #app -->
<div id="form-section">
    <h2>Kontaktformular</h2>
    <form id="contact-form">
        <div>
            <label for="userName">Name:</label>
            <input type="text" id="userName" name="userName" required>
        </div>
        <div>
            <label for="userEmail">E-Mail:</label>
            <input type="email" id="userEmail" name="userEmail" required>
        </div>
        <div>
            <label for="userMessage">Nachricht:</label>
            <textarea id="userMessage" name="userMessage" rows="4"></textarea>
        </div>
        <button type="submit" class="btn">Absenden</button>
    </form>
    <div id="form-output"></div>
</div>
```

Füge dieses CSS hinzu:

```css
/* Füge dies in style.css ein */
#form-section {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
}

#form-section > div {
    margin-bottom: 15px;
}

#form-section label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

#form-section input,
#form-section textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

#form-section input:focus,
#form-section textarea:focus {
    outline: none;
    border-color: #007bff;
}

#form-output {
    margin-top: 20px;
    padding: 15px;
    background-color: #d4edda;
    border-radius: 4px;
    display: none;
}

#form-output.show {
    display: block;
}
```

Jetzt der JavaScript-Code:

```javascript
// ========================================
// TEIL 7: Formular verarbeiten
// Datei: teil7.js
// ========================================

const contactForm = document.querySelector('#contact-form');
const formOutput = document.querySelector('#form-output');

// 1. Füge einen submit Event Listener hinzu
contactForm.addEventListener('submit', (e) => {
    // 2. Verhindere den Standard-Submit (Seiten-Reload)
    // Dein Code hier

    // 3. Lese die Werte aus den Eingabefeldern
    const userName = // Dein Code hier
    const userEmail = // Dein Code hier
    const userMessage = // Dein Code hier

    // 4. Gib die Daten in der Konsole aus
    console.log('Formular-Daten:', { userName, userEmail, userMessage });

    // 5. Zeige die Daten im Output-Bereich an
    // Nutze textContent statt innerHTML für User-Input (XSS-Schutz!)
    formOutput.textContent = `Vielen Dank, ${userName}! Wir werden uns bei ${userEmail} melden.`;
    formOutput.classList.add('show');

    // 6. Setze das Formular zurück
    // Dein Code hier
});

// 7. Live-Validierung für E-Mail
const emailField = document.querySelector('#userEmail');
emailField.addEventListener('input', (e) => {
    const emailValue = e.target.value;
    // Prüfe ob @ und . enthalten ist und zeige visuelles Feedback
    // Dein Code hier
});
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 7: Formular verarbeiten
// Datei: teil7.js
// ========================================

const contactForm = document.querySelector('#contact-form');
const formOutput = document.querySelector('#form-output');

// 1. & 2. Submit Event Listener mit preventDefault
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // 3. Werte auslesen
    const userName = document.querySelector('#userName').value;
    const userEmail = document.querySelector('#userEmail').value;
    const userMessage = document.querySelector('#userMessage').value;

    // 4. Konsolen-Ausgabe
    console.log('Formular-Daten:', { userName, userEmail, userMessage });

    // 5. Im Output anzeigen (textContent für XSS-Schutz!)
    formOutput.textContent = `Vielen Dank, ${userName}! Wir werden uns bei ${userEmail} melden.`;
    formOutput.classList.add('show');

    // 6. Formular zurücksetzen
    contactForm.reset();
});

// 7. Live-Validierung für E-Mail
const emailField = document.querySelector('#userEmail');
emailField.addEventListener('input', (e) => {
    const emailValue = e.target.value;

    if (emailValue.includes('@') && emailValue.includes('.')) {
        emailField.style.borderColor = '#28a745';  // Grün
    } else if (emailValue.length > 0) {
        emailField.style.borderColor = '#dc3545';  // Rot
    } else {
        emailField.style.borderColor = '#ddd';     // Standard
    }
});
```

</details>

---

## Teil 8: Elemente erstellen & einfügen

> **Datei:** Erstelle `teil8.js` und binde sie in `index.html` ein.

Du kannst auch komplett neue Elemente erstellen und ins DOM einfügen.

### Element erstellen

```javascript
// 1. Element erstellen
const newItem = document.createElement('li');

// 2. Inhalt/Attribute setzen (XSS-sicher mit textContent!)
newItem.textContent = 'Neuer Eintrag';
newItem.classList.add('item');
newItem.dataset.id = '999';

// 3. In DOM einfügen
const list = document.querySelector('#item-list');
list.appendChild(newItem);     // Am Ende
list.prepend(newItem);         // Am Anfang
```

### Komplexere Elemente sicher erstellen

```javascript
// ✅ XSS-sichere Variante: Elemente einzeln erstellen
function createListItem(text, id) {
    const li = document.createElement('li');
    li.classList.add('item');
    li.dataset.id = id;

    const span = document.createElement('span');
    span.classList.add('item-text');
    span.textContent = text;  // textContent ist sicher!

    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('delete-btn');
    deleteBtn.dataset.id = id;
    deleteBtn.textContent = 'X';

    li.appendChild(span);
    li.appendChild(deleteBtn);

    return li;
}
```

### Element entfernen

```javascript
// Element direkt entfernen
const item = document.querySelector('.item');
item.remove();

// Alle Kinder entfernen
const parent = document.querySelector('#list');
parent.innerHTML = '';  // Schnell, aber nur wenn kein User-Input!
```

### Übung 8: Elemente erstellen

> **Ziel:** Neue DOM-Elemente dynamisch erstellen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du Items hinzufügen und entfernen kannst

Füge dieses HTML hinzu:

```html
<!-- Füge dies in index.html ein -->
<div id="list-section">
    <h2>Dynamische Liste</h2>
    <form id="add-item-form">
        <input type="text" id="new-item-input" placeholder="Neues Item..." required>
        <button type="submit" class="btn">Hinzufügen</button>
    </form>
    <ul id="dynamic-list"></ul>
</div>
```

```css
/* Füge dies in style.css ein */
#list-section {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
}

#add-item-form {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

#add-item-form input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

#dynamic-list .item {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

```javascript
// ========================================
// TEIL 8: Elemente erstellen & entfernen
// Datei: teil8.js
// ========================================

const addItemForm = document.querySelector('#add-item-form');
const newItemInput = document.querySelector('#new-item-input');
const dynamicList = document.querySelector('#dynamic-list');

let currentItemId = 0;  // Zähler für eindeutige IDs

// Hilfsfunktion: Erstellt ein neues List-Item (XSS-sicher!)
function createNewItem(text, id) {
    // 1. Erstelle das li-Element
    const li = document.createElement('li');
    li.classList.add('item');
    li.dataset.id = id;

    // 2. Erstelle den Text-Span
    const textSpan = document.createElement('span');
    textSpan.classList.add('item-text');
    textSpan.textContent = text;  // textContent ist XSS-sicher!

    // 3. Erstelle den Delete-Button
    const delBtn = document.createElement('button');
    delBtn.classList.add('delete-btn');
    delBtn.dataset.id = id;
    delBtn.textContent = 'X';

    // 4. Füge alles zusammen
    li.appendChild(textSpan);
    li.appendChild(delBtn);

    return li;
}

addItemForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const text = newItemInput.value.trim();
    if (!text) return;  // Leere Eingaben ignorieren

    currentItemId++;

    // 5. Nutze die Hilfsfunktion um ein neues Item zu erstellen
    const newListItem = // Dein Code hier

    // 6. Füge das Item zur Liste hinzu
    // Dein Code hier

    // 7. Leere das Input-Feld und setze Fokus
    // Dein Code hier
});

// 8. Event Delegation für Delete-Buttons
dynamicList.addEventListener('click', (e) => {
    // Prüfe ob ein Delete-Button geklickt wurde
    if (e.target.classList.contains('delete-btn')) {
        // Entferne das Parent-Element (das li)
        // Tipp: e.target.closest('.item') findet das übergeordnete .item
        // Dein Code hier
    }
});
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 8: Elemente erstellen & entfernen
// Datei: teil8.js
// ========================================

const addItemForm = document.querySelector('#add-item-form');
const newItemInput = document.querySelector('#new-item-input');
const dynamicList = document.querySelector('#dynamic-list');

let currentItemId = 0;

// Hilfsfunktion: Erstellt ein neues List-Item (XSS-sicher!)
function createNewItem(text, id) {
    const li = document.createElement('li');
    li.classList.add('item');
    li.dataset.id = id;

    const textSpan = document.createElement('span');
    textSpan.classList.add('item-text');
    textSpan.textContent = text;

    const delBtn = document.createElement('button');
    delBtn.classList.add('delete-btn');
    delBtn.dataset.id = id;
    delBtn.textContent = 'X';

    li.appendChild(textSpan);
    li.appendChild(delBtn);

    return li;
}

addItemForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const text = newItemInput.value.trim();
    if (!text) return;

    currentItemId++;

    // 5. Neues Item erstellen
    const newListItem = createNewItem(text, currentItemId);

    // 6. Zur Liste hinzufügen
    dynamicList.appendChild(newListItem);

    // 7. Input leeren und Fokus setzen
    newItemInput.value = '';
    newItemInput.focus();
});

// 8. Event Delegation für Delete-Buttons
dynamicList.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-btn')) {
        const itemToRemove = e.target.closest('.item');
        itemToRemove.remove();
    }
});
```

</details>

---

## Teil 9: Event Delegation

> **Datei:** Erstelle `teil9.js` und binde sie in `index.html` ein.

Statt 100 Listenern auf 100 Buttons: EIN Listener auf dem Parent-Element.

### Das Problem

```javascript
// ❌ Ineffizient: Listener auf JEDEM Button
const buttons = document.querySelectorAll('.delete-btn');

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        // Löschen...
    });
});

// Problem: Neue Buttons haben keinen Listener!
```

### Die Lösung: Event Delegation

```javascript
// ✅ EIN Listener auf dem Parent
const list = document.querySelector('#item-list');

list.addEventListener('click', (e) => {
    // Prüfen, ob ein Delete-Button geklickt wurde
    if (e.target.classList.contains('delete-btn')) {
        const itemId = e.target.dataset.id;
        console.log('Lösche Item:', itemId);
        e.target.closest('.item').remove();
    }

    // Prüfen, ob der Item-Text geklickt wurde
    if (e.target.classList.contains('item-text')) {
        e.target.closest('.item').classList.toggle('done');
    }
});
```

### Vorteile

- **Weniger Listener** = bessere Performance
- **Dynamisch hinzugefügte Elemente** funktionieren automatisch
- **Einfacher zu verwalten**

### Übung 9: Event Delegation

> **Ziel:** Event Delegation anwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du das Konzept der Event Delegation verstehst

```javascript
// ========================================
// TEIL 9: Event Delegation
// Datei: teil9.js
// ========================================

const mainItemList = document.querySelector('#item-list');

// EIN Event Listener für alle Aktionen in der Liste
mainItemList.addEventListener('click', (e) => {
    // Debug: Zeige was geklickt wurde
    console.log('Geklicktes Element:', e.target);
    console.log('Element-Klassen:', e.target.classList);

    // 1. Wenn ein Item-Text geklickt wurde: Toggle "done" Klasse
    if (e.target.classList.contains('item-text')) {
        // Dein Code hier
        // Tipp: e.target.closest('.item') findet das umgebende .item
        console.log('Item-Text geklickt:', e.target.textContent);
    }

    // 2. Wenn ein Delete-Button geklickt wurde: Item entfernen
    if (e.target.classList.contains('delete-btn')) {
        // Dein Code hier
        console.log('Lösche Item mit ID:', e.target.dataset.id);
    }
});

// Frage zum Nachdenken:
// Warum funktionieren die Delete-Buttons, obwohl wir keinen
// direkten Event Listener auf sie gesetzt haben?
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 9: Event Delegation
// Datei: teil9.js
// ========================================

const mainItemList = document.querySelector('#item-list');

mainItemList.addEventListener('click', (e) => {
    console.log('Geklicktes Element:', e.target);

    // 1. Item-Text geklickt → Toggle "done"
    if (e.target.classList.contains('item-text')) {
        const parentItem = e.target.closest('.item');
        parentItem.classList.toggle('done');
        console.log('Item-Text geklickt:', e.target.textContent);
    }

    // 2. Delete-Button geklickt → Item entfernen
    if (e.target.classList.contains('delete-btn')) {
        const itemToDelete = e.target.closest('.item');
        itemToDelete.remove();
        console.log('Item gelöscht mit ID:', e.target.dataset.id);
    }
});

// Antwort auf die Frage:
// Event Delegation nutzt das "Event Bubbling":
// Klick-Events steigen vom geklickten Element zum Parent hoch.
// Der Listener auf #item-list fängt ALLE Klicks ab,
// die innerhalb der Liste passieren - auch auf dynamisch
// hinzugefügten Elementen!
```

</details>

---

## Teil 10: Data Attributes

> **Datei:** Erstelle `teil10.js` und binde sie in `index.html` ein.

Mit `data-*` Attributen kannst du beliebige Daten an HTML-Elemente hängen.

### HTML data-* Attribute

```html
<button
    class="delete-btn"
    data-id="123"
    data-user-name="Max"
    data-is-admin="true"
>
    Löschen
</button>
```

### JavaScript dataset API

```javascript
const btn = document.querySelector('.delete-btn');

// Daten auslesen (camelCase in JS!)
console.log(btn.dataset.id);        // "123"
console.log(btn.dataset.userName);  // "Max" (data-user-name → userName)
console.log(btn.dataset.isAdmin);   // "true" (String!)

// Daten setzen
btn.dataset.newProp = 'value';
// → <button data-new-prop="value">

// WICHTIG: dataset-Werte sind IMMER Strings!
// Für Zahlen: Number(btn.dataset.id)
// Für Boolean: btn.dataset.isAdmin === "true"
```

### Übung 10: Data Attributes

> **Ziel:** Data Attributes nutzen um Daten zu speichern
> **Zeitbedarf:** ca. 10 Minuten

```javascript
// ========================================
// TEIL 10: Data Attributes
// Datei: teil10.js
// ========================================

const dataItems = document.querySelectorAll('#item-list .item');

dataItems.forEach((item, index) => {
    // 1. Lies die data-id jedes Items aus
    const itemId = // Dein Code hier
    console.log(`Item ${index + 1} hat ID:`, itemId);

    // 2. Füge ein neues data-Attribut hinzu: data-created mit aktuellem Timestamp
    // Dein Code hier

    // 3. Füge data-index hinzu mit dem aktuellen Index
    // Dein Code hier
});

// 4. Event Delegation: Bei Klick alle data-Attribute anzeigen
const dataItemList = document.querySelector('#item-list');
dataItemList.addEventListener('click', (e) => {
    const clickedItem = e.target.closest('.item');
    if (clickedItem) {
        console.log('Alle data-Attribute:', clickedItem.dataset);
        console.log('Als Objekt:', { ...clickedItem.dataset });
    }
});
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// ========================================
// TEIL 10: Data Attributes
// Datei: teil10.js
// ========================================

const dataItems = document.querySelectorAll('#item-list .item');

dataItems.forEach((item, index) => {
    // 1. data-id auslesen
    const itemId = item.dataset.id;
    console.log(`Item ${index + 1} hat ID:`, itemId);

    // 2. data-created hinzufügen
    item.dataset.created = Date.now();

    // 3. data-index hinzufügen
    item.dataset.index = index;
});

// 4. Event Delegation: Bei Klick alle data-Attribute anzeigen
const dataItemList = document.querySelector('#item-list');
dataItemList.addEventListener('click', (e) => {
    const clickedItem = e.target.closest('.item');
    if (clickedItem) {
        console.log('Alle data-Attribute:', clickedItem.dataset);
        // Ausgabe: DOMStringMap { id: "1", created: "...", index: "0" }
        console.log('Als Objekt:', { ...clickedItem.dataset });
    }
});
```

</details>

---

## Teil 11: Praxis - Interaktive Todo-Liste

Zeit, alles zusammen anzuwenden! Baue eine vollständige Todo-App.

### Aufgabe: Todo-App

Erstelle eine neue HTML-Datei `todo.html` (separate Datei, nicht in index.html):

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }

        .container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        header {
            background: #667eea;
            color: white;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            margin-bottom: 5px;
        }

        #stats {
            font-size: 14px;
            opacity: 0.9;
        }

        #todo-form {
            display: flex;
            padding: 20px;
            gap: 10px;
            border-bottom: 1px solid #eee;
        }

        #todo-input {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
        }

        #todo-input:focus {
            outline: none;
            border-color: #667eea;
        }

        #todo-form button {
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }

        #todo-form button:hover {
            background: #5a67d8;
        }

        #filter-buttons {
            display: flex;
            padding: 10px 20px;
            gap: 10px;
            border-bottom: 1px solid #eee;
        }

        .filter-btn {
            padding: 8px 16px;
            border: 1px solid #ddd;
            background: white;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }

        .filter-btn.active {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        #todo-list {
            list-style: none;
            max-height: 400px;
            overflow-y: auto;
        }

        .todo-item {
            display: flex;
            align-items: center;
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
            transition: background 0.2s;
        }

        .todo-item:hover {
            background: #f8f9fa;
        }

        .todo-item.done {
            background: #f0fff4;
        }

        .todo-item.done .todo-text {
            text-decoration: line-through;
            color: #888;
        }

        .todo-checkbox {
            width: 22px;
            height: 22px;
            margin-right: 15px;
            cursor: pointer;
        }

        .todo-text {
            flex: 1;
            font-size: 16px;
        }

        .todo-delete-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.2s;
        }

        .todo-item:hover .todo-delete-btn {
            opacity: 1;
        }

        .todo-delete-btn:hover {
            background: #c82333;
        }

        .empty-state {
            padding: 40px;
            text-align: center;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Todo Liste</h1>
            <div id="stats">0 Aufgaben, 0 erledigt</div>
        </header>

        <form id="todo-form">
            <input type="text" id="todo-input" placeholder="Was muss erledigt werden?" required>
            <button type="submit">Hinzufügen</button>
        </form>

        <div id="filter-buttons">
            <button class="filter-btn active" data-filter="all">Alle</button>
            <button class="filter-btn" data-filter="active">Offen</button>
            <button class="filter-btn" data-filter="done">Erledigt</button>
        </div>

        <ul id="todo-list">
            <!-- Todos werden hier eingefügt -->
        </ul>
    </div>

    <script src="todo.js" defer></script>
</body>
</html>
```

Erstelle `todo.js` und vervollständige den Code:

```javascript
// ========================================
// TODO APP - Vervollständige den Code!
// Datei: todo.js
// ========================================

// ============ ELEMENTE SELEKTIEREN ============
const todoForm = document.querySelector('#todo-form');
const todoInput = document.querySelector('#todo-input');
const todoList = document.querySelector('#todo-list');
const statsDisplay = document.querySelector('#stats');
const filterBtns = document.querySelectorAll('.filter-btn');

// ============ STATE ============
let todos = [];
let activeFilter = 'all';
let todoIdCounter = 1;

// ============ FUNKTIONEN ============

// Todo hinzufügen
function addTodo(text) {
    const newTodo = {
        id: todoIdCounter++,
        text: text,
        done: false,
        createdAt: Date.now()
    };

    // 1. Füge newTodo zum todos-Array hinzu
    // Dein Code hier

    // 2. Rendere die Liste neu
    renderTodoList();
}

// Todo löschen
function deleteTodo(id) {
    // 3. Filtere das todo mit der id aus dem Array
    // Tipp: todos = todos.filter(...)
    // Dein Code hier

    renderTodoList();
}

// Todo als erledigt markieren
function toggleTodo(id) {
    // 4. Finde das todo und toggle dessen done-Status
    // Tipp: todos = todos.map(...)
    // Dein Code hier

    renderTodoList();
}

// Gefilterte Todos zurückgeben
function getFilteredTodos() {
    // 5. Gib je nach activeFilter die richtigen Todos zurück
    // 'all' → alle todos
    // 'active' → todos wo done === false
    // 'done' → todos wo done === true

    // Dein Code hier

    return todos; // Ersetze dies mit der gefilterten Liste
}

// Einzelnes Todo-Element erstellen (XSS-sicher!)
function createTodoElement(todo) {
    const li = document.createElement('li');
    li.classList.add('todo-item');
    if (todo.done) {
        li.classList.add('done');
    }
    li.dataset.id = todo.id;

    // Checkbox
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.classList.add('todo-checkbox');
    checkbox.checked = todo.done;

    // Text (XSS-sicher mit textContent!)
    const textSpan = document.createElement('span');
    textSpan.classList.add('todo-text');
    textSpan.textContent = todo.text;

    // Delete Button
    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('todo-delete-btn');
    deleteBtn.textContent = 'Löschen';

    li.appendChild(checkbox);
    li.appendChild(textSpan);
    li.appendChild(deleteBtn);

    return li;
}

// Todos rendern
function renderTodoList() {
    const filteredTodos = getFilteredTodos();

    // Liste leeren
    todoList.innerHTML = '';

    // 6. Wenn keine Todos vorhanden, zeige Empty State
    if (filteredTodos.length === 0) {
        const emptyLi = document.createElement('li');
        emptyLi.classList.add('empty-state');
        emptyLi.textContent = 'Keine Aufgaben vorhanden';
        todoList.appendChild(emptyLi);
    } else {
        // 7. Für jedes Todo ein Element erstellen und anhängen
        filteredTodos.forEach(todo => {
            const todoElement = createTodoElement(todo);
            todoList.appendChild(todoElement);
        });
    }

    // 8. Stats aktualisieren
    updateStats();
}

// Statistiken aktualisieren
function updateStats() {
    const totalCount = todos.length;
    const doneCount = todos.filter(t => t.done).length;

    // 9. Aktualisiere den statsDisplay-Text
    // Dein Code hier
}

// Filter setzen
function setActiveFilter(filter) {
    activeFilter = filter;

    // 10. Active-Klasse bei Filter-Buttons aktualisieren
    filterBtns.forEach(btn => {
        // Dein Code hier
    });

    renderTodoList();
}

// ============ EVENT LISTENERS ============

// 11. Form Submit Handler
todoForm.addEventListener('submit', (e) => {
    // Dein Code hier
});

// 12. Event Delegation für Todo-Liste
todoList.addEventListener('click', (e) => {
    // Finde das übergeordnete Todo-Item
    const todoItem = e.target.closest('.todo-item');
    if (!todoItem) return;

    const todoId = Number(todoItem.dataset.id);

    // 13. Checkbox geklickt → Toggle todo
    if (e.target.classList.contains('todo-checkbox')) {
        // Dein Code hier
    }

    // 14. Delete-Button geklickt → Lösche todo
    if (e.target.classList.contains('todo-delete-btn')) {
        // Dein Code hier
    }
});

// 15. Filter-Buttons Event Delegation
document.querySelector('#filter-buttons').addEventListener('click', (e) => {
    if (e.target.classList.contains('filter-btn')) {
        const selectedFilter = e.target.dataset.filter;
        // Dein Code hier
    }
});

// ============ INITIALISIERUNG ============

// 16. Füge ein paar Start-Todos hinzu zum Testen
addTodo('DOM Manipulation lernen');
addTodo('Event Listener verstehen');
addTodo('Todo-App fertig bauen');
```

<details>
<summary>Vollständige Musterlösung anzeigen</summary>

```javascript
// ========================================
// TODO APP - Musterlösung
// Datei: todo.js
// ========================================

// ============ ELEMENTE SELEKTIEREN ============
const todoForm = document.querySelector('#todo-form');
const todoInput = document.querySelector('#todo-input');
const todoList = document.querySelector('#todo-list');
const statsDisplay = document.querySelector('#stats');
const filterBtns = document.querySelectorAll('.filter-btn');

// ============ STATE ============
let todos = [];
let activeFilter = 'all';
let todoIdCounter = 1;

// ============ FUNKTIONEN ============

function addTodo(text) {
    const newTodo = {
        id: todoIdCounter++,
        text: text,
        done: false,
        createdAt: Date.now()
    };

    // 1. Todo zum Array hinzufügen
    todos.push(newTodo);

    renderTodoList();
}

function deleteTodo(id) {
    // 3. Todo aus Array entfernen
    todos = todos.filter(todo => todo.id !== id);

    renderTodoList();
}

function toggleTodo(id) {
    // 4. done-Status toggeln
    todos = todos.map(todo => {
        if (todo.id === id) {
            return { ...todo, done: !todo.done };
        }
        return todo;
    });

    renderTodoList();
}

function getFilteredTodos() {
    // 5. Nach Filter filtern
    switch (activeFilter) {
        case 'active':
            return todos.filter(todo => !todo.done);
        case 'done':
            return todos.filter(todo => todo.done);
        default:
            return todos;
    }
}

function createTodoElement(todo) {
    const li = document.createElement('li');
    li.classList.add('todo-item');
    if (todo.done) {
        li.classList.add('done');
    }
    li.dataset.id = todo.id;

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.classList.add('todo-checkbox');
    checkbox.checked = todo.done;

    const textSpan = document.createElement('span');
    textSpan.classList.add('todo-text');
    textSpan.textContent = todo.text;

    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('todo-delete-btn');
    deleteBtn.textContent = 'Löschen';

    li.appendChild(checkbox);
    li.appendChild(textSpan);
    li.appendChild(deleteBtn);

    return li;
}

function renderTodoList() {
    const filteredTodos = getFilteredTodos();

    todoList.innerHTML = '';

    // 6. Empty State
    if (filteredTodos.length === 0) {
        const emptyLi = document.createElement('li');
        emptyLi.classList.add('empty-state');
        emptyLi.textContent = 'Keine Aufgaben vorhanden';
        todoList.appendChild(emptyLi);
    } else {
        // 7. Todos rendern
        filteredTodos.forEach(todo => {
            const todoElement = createTodoElement(todo);
            todoList.appendChild(todoElement);
        });
    }

    updateStats();
}

function updateStats() {
    const totalCount = todos.length;
    const doneCount = todos.filter(t => t.done).length;

    // 9. Stats aktualisieren
    statsDisplay.textContent = `${totalCount} Aufgaben, ${doneCount} erledigt`;
}

function setActiveFilter(filter) {
    activeFilter = filter;

    // 10. Active-Klasse aktualisieren
    filterBtns.forEach(btn => {
        if (btn.dataset.filter === filter) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    renderTodoList();
}

// ============ EVENT LISTENERS ============

// 11. Form Submit
todoForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const text = todoInput.value.trim();
    if (!text) return;

    addTodo(text);
    todoInput.value = '';
    todoInput.focus();
});

// 12. - 14. Todo-Liste Event Delegation
todoList.addEventListener('click', (e) => {
    const todoItem = e.target.closest('.todo-item');
    if (!todoItem) return;

    const todoId = Number(todoItem.dataset.id);

    // 13. Checkbox
    if (e.target.classList.contains('todo-checkbox')) {
        toggleTodo(todoId);
    }

    // 14. Delete
    if (e.target.classList.contains('todo-delete-btn')) {
        deleteTodo(todoId);
    }
});

// 15. Filter-Buttons
document.querySelector('#filter-buttons').addEventListener('click', (e) => {
    if (e.target.classList.contains('filter-btn')) {
        const selectedFilter = e.target.dataset.filter;
        setActiveFilter(selectedFilter);
    }
});

// ============ INITIALISIERUNG ============

// 16. Start-Todos
addTodo('DOM Manipulation lernen');
addTodo('Event Listener verstehen');
addTodo('Todo-App fertig bauen');
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Thema | Methode | Beispiel |
|-------|---------|----------|
| **Selektieren** | `querySelector()` | `document.querySelector('.btn')` |
| **Alle selektieren** | `querySelectorAll()` | `document.querySelectorAll('.item')` |
| **Text ändern** | `textContent` | `el.textContent = 'Neu'` |
| **Klassen** | `classList` | `el.classList.add('active')` |
| **Styles** | `style` | `el.style.color = 'red'` |
| **Events** | `addEventListener()` | `el.addEventListener('click', fn)` |
| **Event-Objekt** | `e.target`, `e.preventDefault()` | Im Event Handler |
| **Erstellen** | `createElement()` | `document.createElement('li')` |
| **Einfügen** | `appendChild()` | `parent.appendChild(child)` |
| **Entfernen** | `remove()` | `el.remove()` |
| **Data Attributes** | `dataset` | `el.dataset.id` |

### Die wichtigsten Patterns für React

```javascript
// DOM (Vanilla JS)                    // React
// ─────────────────────────────────   ─────────────────────────────
document.querySelector('#btn')         // useRef() oder direkte Props
el.addEventListener('click', fn)       // onClick={fn}
e.preventDefault()                     // e.preventDefault() (gleich!)
el.textContent = 'Neu'                 // State: setText('Neu')
el.classList.toggle('active')          // State: setIsActive(!isActive)
document.createElement('li')           // JSX: <li>...</li>
```

---

## Checkliste

Bevor du mit dem nächsten Tag weitermachst, stelle sicher:

- [ ] Du kannst Elemente mit `querySelector()` selektieren
- [ ] Du verstehst den Unterschied zwischen `querySelector()` und `querySelectorAll()`
- [ ] Du kannst `textContent` und `classList` nutzen
- [ ] Du kannst Event Listener mit `addEventListener()` hinzufügen
- [ ] Du verstehst `e.preventDefault()` bei Formularen
- [ ] Du kannst neue DOM-Elemente mit `createElement()` erstellen
- [ ] Du verstehst das Konzept der Event Delegation
- [ ] Du kannst `data-*` Attribute nutzen

**Alles abgehakt?** Dann bist du bereit für Tag 9: Asynchrones JavaScript!

---

## Bonus: Schnellreferenz

### Elemente selektieren

```javascript
document.querySelector('.class')       // Erstes Element
document.querySelector('#id')          // Nach ID
document.querySelectorAll('.class')    // Alle Elemente
document.getElementById('id')          // Klassisch
```

### DOM Manipulation

```javascript
// Inhalt
el.textContent = 'Text';              // Nur Text (XSS-sicher!)
el.innerHTML = '<p>HTML</p>';         // HTML (Vorsicht: nie mit User-Input!)

// Klassen
el.classList.add('class');
el.classList.remove('class');
el.classList.toggle('class');
el.classList.contains('class');

// Attribute
el.setAttribute('attr', 'value');
el.getAttribute('attr');
el.dataset.customAttr;                // data-custom-attr
```

### Events

```javascript
// Listener hinzufügen
el.addEventListener('click', (e) => {
    e.target;                         // Geklicktes Element
    e.currentTarget;                  // Element mit Listener
    e.preventDefault();               // Standard verhindern
    e.stopPropagation();              // Bubbling stoppen
});

// Wichtige Events
'click', 'dblclick'                   // Maus
'keydown', 'keyup'                    // Tastatur
'submit', 'input', 'change'           // Formulare
'focus', 'blur'                       // Fokus
```

### Elemente erstellen (XSS-sicher)

```javascript
// Sicher: Elemente einzeln erstellen
const el = document.createElement('div');
el.textContent = userInput;           // textContent ist sicher!
el.classList.add('class');
parent.appendChild(el);

// Element finden
el.closest('.parent-class');          // Nächstes Parent mit Klasse

// Element entfernen
el.remove();
```
