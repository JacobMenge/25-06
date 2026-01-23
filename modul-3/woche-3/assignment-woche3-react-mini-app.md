# Optionales Assignment: React Mini-App (Einzelarbeit)

## Wochenabschluss: React Grundlagen

### Organisatorische Rahmenbedingungen

**Dieses Assignment ist freiwillig!** Es dient der Vertiefung der Woche und kann eingereicht werden, falls ihr Feedback von uns wünscht.

Falls du abgeben möchtest, reiche deinen Projektordner ein (bis Montag, 23:59 Uhr):

```
vorname_nachname_woche3/
    src/
        components/
            ... (deine Komponenten)
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

Der thematische Umfang dieser Aufgabe erstreckt sich über die React-Grundlagen der Woche:
- React Setup mit Vite
- JSX und Komponenten
- Props für Datenübergabe
- useState für State Management
- Controlled Inputs
- Listen rendern mit map()
- Keys für Listen
- Konditionales Rendering

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

Mit diesem Assignment zeigst du, dass du die wichtigsten React-Grundlagen verstanden hast. Es geht darum, eine **einfache, funktionierende React-App** zu erstellen, die State, Props, Listen und konditionales Rendering verwendet.

**Wichtig:** Eine einfache, funktionierende App ist besser als eine komplexe, fehlerhafte!

Du hast die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Thema (Kreativ)

Erstelle eine React Mini-App zu einem Thema deiner Wahl.

### Mindestanforderungen:

**Komponenten:**
- Mindestens 3 eigene Komponenten (z.B. App, ItemList, ItemCard)
- Mindestens eine Komponente erhält Props
- Sinnvolle Komponenten-Aufteilung

**State:**
- Verwende `useState` für mindestens einen State
- Der State soll durch User-Interaktion verändert werden können

**Listen:**
- Rendere eine Liste von mindestens 3 Elementen mit `map()`
- Verwende korrekte `key` Props

**Konditionales Rendering:**
- Mindestens eine bedingte Anzeige (z.B. mit `&&` oder Ternary `? :`)

**Struktur:**
- Komponenten in separaten Dateien im `components/` Ordner
- Sauberer, lesbarer Code

### Ideen für Apps:

| App-Idee | Beschreibung |
|----------|--------------|
| **Einkaufsliste** | Items hinzufügen, abhaken, löschen |
| **Notiz-App** | Notizen erstellen, anzeigen, löschen |
| **Rezept-Sammlung** | Rezepte aus JSON laden, nach Kategorie filtern |
| **Filmsammlung** | Filme anzeigen, als "gesehen" markieren |
| **Quiz-App** | Fragen anzeigen, Antworten auswählen |
| **Bookmarks** | Links speichern und kategorisieren |

---

## Weg B: Geführte Aufgabe (Schritt für Schritt)

Falls du lieber einer Anleitung folgen möchtest, baue diese **Aufgaben-Manager-App**.

### Was wir bauen:

Eine App, die:
1. Eine Liste von Aufgaben anzeigt
2. Neue Aufgaben hinzufügen kann
3. Aufgaben als erledigt markieren kann
4. Aufgaben nach Status filtern kann (Alle/Offen/Erledigt)
5. Die Anzahl offener Aufgaben anzeigt

**Am Ende hast du automatisch alle Anforderungen erfüllt!**

---

### Schritt 1: Projekt erstellen

Falls du noch kein Projekt hast:

```bash
npm create vite@latest aufgaben-manager -- --template react
cd aufgaben-manager
npm install
npm run dev
```

---

### Schritt 2: Projektstruktur vorbereiten

Erstelle folgende Ordnerstruktur:

```
src/
├── components/
│   ├── TaskForm.jsx
│   ├── TaskList.jsx
│   ├── TaskItem.jsx
│   └── FilterButtons.jsx
├── App.jsx
├── App.css
└── main.jsx
```

---

### Schritt 3: App.jsx - Grundstruktur und State

Ersetze den Inhalt von `src/App.jsx`:

```javascript
// src/App.jsx
import { useState } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import FilterButtons from './components/FilterButtons';
import './App.css';

function App() {
  // State für alle Aufgaben
  const [tasks, setTasks] = useState([
    { id: 1, text: 'React lernen', completed: true },
    { id: 2, text: 'Assignment machen', completed: false },
    { id: 3, text: 'Code reviewen', completed: false }
  ]);

  // State für den aktuellen Filter
  const [filter, setFilter] = useState('all'); // 'all', 'open', 'completed'

  // Nächste verfügbare ID für neue Tasks
  const [nextId, setNextId] = useState(4);

  // Aufgabe hinzufügen
  const addTask = (text) => {
    const newTask = {
      id: nextId,
      text: text,
      completed: false
    };
    setTasks([...tasks, newTask]);
    setNextId(nextId + 1);
  };

  // Aufgabe als erledigt/offen markieren
  const toggleTask = (id) => {
    setTasks(tasks.map(task =>
      task.id === id
        ? { ...task, completed: !task.completed }
        : task
    ));
  };

  // Aufgabe löschen
  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  // Gefilterte Aufgaben berechnen
  const filteredTasks = tasks.filter(task => {
    if (filter === 'open') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true; // 'all'
  });

  // Anzahl offener Aufgaben
  const openCount = tasks.filter(task => !task.completed).length;

  return (
    <div className="app">
      <header className="app-header">
        <h1>Aufgaben-Manager</h1>
        <p className="task-count">
          {openCount === 0
            ? 'Alle Aufgaben erledigt! 🎉'
            : `${openCount} ${openCount === 1 ? 'Aufgabe' : 'Aufgaben'} offen`
          }
        </p>
      </header>

      <main className="app-main">
        <TaskForm onAddTask={addTask} />

        <FilterButtons
          currentFilter={filter}
          onFilterChange={setFilter}
          counts={{
            all: tasks.length,
            open: openCount,
            completed: tasks.length - openCount
          }}
        />

        <TaskList
          tasks={filteredTasks}
          onToggle={toggleTask}
          onDelete={deleteTask}
        />
      </main>
    </div>
  );
}

export default App;
```

**Erklärung:**
- `useState` speichert die Aufgaben, den Filter und die nächste ID
- `addTask`, `toggleTask`, `deleteTask` sind Handler-Funktionen
- `filteredTasks` wird aus dem State berechnet (derived state)
- Props werden an die Kind-Komponenten übergeben

> **Hinweis zu `nextId`:** Die `nextId` muss immer größer sein als die höchste vorhandene ID. Wenn du später die initialen Tasks änderst oder aus localStorage lädst, achte darauf, dass `nextId` entsprechend angepasst wird!

---

### Schritt 4: TaskForm.jsx - Neue Aufgaben hinzufügen

Erstelle `src/components/TaskForm.jsx`:

```javascript
// src/components/TaskForm.jsx
import { useState } from 'react';

function TaskForm({ onAddTask }) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Leere Eingabe ignorieren
    const trimmedValue = inputValue.trim();
    if (!trimmedValue) return;

    // Task hinzufügen (über Props-Funktion)
    onAddTask(trimmedValue);

    // Input leeren
    setInputValue('');
  };

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <input
        type="text"
        className="task-input"
        placeholder="Neue Aufgabe eingeben..."
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <button type="submit" className="add-button">
        Hinzufügen
      </button>
    </form>
  );
}

export default TaskForm;
```

**Erklärung:**
- **Controlled Input:** `value={inputValue}` + `onChange` kontrolliert das Input
- **Props-Funktion:** `onAddTask` wird von App.jsx übergeben
- **preventDefault:** Verhindert Seiten-Reload beim Submit

---

### Schritt 5: FilterButtons.jsx - Filter-Auswahl

Erstelle `src/components/FilterButtons.jsx`:

```javascript
// src/components/FilterButtons.jsx

function FilterButtons({ currentFilter, onFilterChange, counts }) {
  const filters = [
    { value: 'all', label: 'Alle' },
    { value: 'open', label: 'Offen' },
    { value: 'completed', label: 'Erledigt' }
  ];

  return (
    <div className="filter-buttons">
      {filters.map(filter => (
        <button
          type="button"
          key={filter.value}
          className={`filter-btn ${currentFilter === filter.value ? 'active' : ''}`}
          onClick={() => onFilterChange(filter.value)}
        >
          {filter.label} ({counts[filter.value]})
        </button>
      ))}
    </div>
  );
}

export default FilterButtons;
```

**Erklärung:**
- **type="button":** Verhindert, dass der Button als Submit interpretiert wird (wichtig, falls er später in einem Form landet)
- **Liste rendern:** `filters.map()` erzeugt die Buttons dynamisch
- **Korrekter Key:** `key={filter.value}` ist stabil und eindeutig
- **Aktiver Button:** Klasse `active` wird bedingt hinzugefügt
- **Counts:** Zeigt Anzahl pro Kategorie in Klammern

---

### Schritt 6: TaskList.jsx - Aufgaben-Liste

Erstelle `src/components/TaskList.jsx`:

```javascript
// src/components/TaskList.jsx
import TaskItem from './TaskItem';

function TaskList({ tasks, onToggle, onDelete }) {
  // Leere Liste
  if (tasks.length === 0) {
    return (
      <div className="task-list empty">
        <p>Keine Aufgaben vorhanden.</p>
      </div>
    );
  }

  return (
    <ul className="task-list">
      {tasks.map(task => (
        <TaskItem
          key={task.id}
          task={task}
          onToggle={onToggle}
          onDelete={onDelete}
        />
      ))}
    </ul>
  );
}

export default TaskList;
```

**Erklärung:**
- **Early Return:** Bei leerer Liste wird eine Nachricht angezeigt
- **Liste rendern:** `tasks.map()` erzeugt TaskItem-Komponenten
- **Key:** `key={task.id}` verwendet die eindeutige ID
- **Props durchreichen:** `onToggle` und `onDelete` gehen an TaskItem

---

### Schritt 7: TaskItem.jsx - Einzelne Aufgabe

Erstelle `src/components/TaskItem.jsx`:

```javascript
// src/components/TaskItem.jsx

function TaskItem({ task, onToggle, onDelete }) {
  return (
    <li className={`task-item ${task.completed ? 'completed' : ''}`}>
      <label className="task-label">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggle(task.id)}
        />
        <span className="task-text">{task.text}</span>
      </label>

      <button
        className="delete-btn"
        onClick={() => onDelete(task.id)}
        title="Aufgabe löschen"
      >
        ✕
      </button>
    </li>
  );
}

export default TaskItem;
```

**Erklärung:**
- **Bedingte Klasse:** `completed` wird bei erledigten Aufgaben hinzugefügt
- **Checkbox:** `checked={task.completed}` zeigt den Status
- **Event Handler:** `onChange` und `onClick` rufen die Props-Funktionen auf
- **ID übergeben:** `onToggle(task.id)` sagt App.jsx, welche Aufgabe gemeint ist

---

### Schritt 8: App.css - Styling

> **Hinweis:** Das CSS ist optional – **funktional ist wichtiger als schön!** Wenn du wenig Zeit hast, kannst du auch nur minimale Styles verwenden oder diesen Schritt überspringen. Der Fokus liegt auf React, nicht auf CSS.

Ersetze den Inhalt von `src/App.css`:

```css
/* === GRUNDEINSTELLUNGEN === */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  padding: 20px;
}

/* === APP CONTAINER === */
.app {
  max-width: 500px;
  margin: 0 auto;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

/* === HEADER === */
.app-header {
  background: #667eea;
  color: white;
  padding: 24px;
  text-align: center;
}

.app-header h1 {
  margin-bottom: 8px;
  font-size: 24px;
}

.task-count {
  font-size: 14px;
  opacity: 0.9;
}

/* === MAIN === */
.app-main {
  padding: 24px;
}

/* === TASK FORM === */
.task-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.task-input {
  flex: 1;
  padding: 12px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.2s;
}

.task-input:focus {
  outline: none;
  border-color: #667eea;
}

.add-button {
  padding: 12px 20px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s;
}

.add-button:hover {
  background: #5a67d8;
}

/* === FILTER BUTTONS === */
.filter-buttons {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.filter-btn {
  flex: 1;
  padding: 10px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #667eea;
}

.filter-btn.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

/* === TASK LIST === */
.task-list {
  list-style: none;
}

.task-list.empty {
  text-align: center;
  color: #888;
  padding: 40px 20px;
  font-style: italic;
}

/* === TASK ITEM === */
.task-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-bottom: 1px solid #f0f0f0;
  transition: background 0.2s;
}

.task-item:hover {
  background: #f8f8f8;
}

.task-item:last-child {
  border-bottom: none;
}

.task-item.completed .task-text {
  text-decoration: line-through;
  color: #999;
}

.task-label {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
  cursor: pointer;
}

.task-label input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #667eea;
}

.task-text {
  font-size: 16px;
}

.delete-btn {
  padding: 6px 10px;
  background: transparent;
  color: #e53e3e;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  opacity: 0.5;
  transition: opacity 0.2s;
}

.delete-btn:hover {
  opacity: 1;
  background: #fed7d7;
}

/* === RESPONSIVE === */
@media (max-width: 480px) {
  body {
    padding: 10px;
  }

  .app-header {
    padding: 20px;
  }

  .app-main {
    padding: 16px;
  }

  .task-form {
    flex-direction: column;
  }

  .filter-buttons {
    flex-wrap: wrap;
  }

  .filter-btn {
    flex: 1 1 calc(33% - 8px);
    min-width: 80px;
  }
}
```

---

### Schritt 9: Testen!

1. Starte den Dev-Server (falls nicht bereits laufend):
   ```bash
   npm run dev
   ```

2. Öffne die App im Browser

3. Teste alle Funktionen:
   - [ ] Neue Aufgabe hinzufügen
   - [ ] Aufgabe als erledigt markieren
   - [ ] Aufgabe wieder als offen markieren
   - [ ] Aufgabe löschen
   - [ ] Filter "Alle" zeigt alle Aufgaben
   - [ ] Filter "Offen" zeigt nur offene Aufgaben
   - [ ] Filter "Erledigt" zeigt nur erledigte Aufgaben
   - [ ] Anzahl offener Aufgaben wird korrekt angezeigt

---

## Checkliste: Was du verwendet hast

Wenn du Weg B abgeschlossen hast, hast du folgende Konzepte angewendet:

### Komponenten & Props
- [x] Mehrere Komponenten erstellt (App, TaskForm, TaskList, TaskItem, FilterButtons)
- [x] Props für Datenübergabe verwendet
- [x] Callback-Funktionen als Props übergeben

### State & Events
- [x] `useState` für State Management
- [x] State wird durch User-Interaktion verändert
- [x] Controlled Input mit `value` und `onChange`
- [x] Form Submit mit `onSubmit` und `preventDefault`

### Listen & Keys
- [x] Listen mit `map()` gerendert
- [x] Korrekte `key` Props verwendet (stabile IDs)
- [x] Array-Methoden: `map()`, `filter()`

### Konditionales Rendering
- [x] `&&` für bedingte Anzeige
- [x] Ternary `? :` für Entweder/Oder
- [x] Early Return für leere Listen
- [x] Bedingte CSS-Klassen

---

## Bonus-Ideen (optional)

> **Wichtig:** Die Bonus-Aufgaben sind **nur für diejenigen gedacht, die die Grundaufgabe vollständig abgeschlossen haben** und noch Zeit/Energie haben. Sie sind NICHT notwendig für eine gute Abgabe!

Falls du die Grundaufgabe erledigt hast und mehr machen möchtest:

1. **Bearbeiten:** Aufgaben-Text nachträglich ändern können
2. **Prioritäten:** Aufgaben als "wichtig" markieren können
3. **Kategorien:** Aufgaben nach Kategorien gruppieren
4. **Datum:** Fälligkeitsdatum hinzufügen
5. **localStorage:** Aufgaben im Browser speichern (siehe unten)

### Beispiel: localStorage Integration (Fortgeschritten!)

> ** Achtung:** Dieses Beispiel verwendet `useEffect`, das erst **nächste Woche** behandelt wird. Nur einbauen, wenn du experimentierfreudig bist! Falls du es nutzt, erwähne es in deinem README als "Extra".

```javascript
// In App.jsx
import { useState, useEffect } from 'react';

// State aus localStorage laden (oder Default verwenden)
const [tasks, setTasks] = useState(() => {
  const saved = localStorage.getItem('tasks');
  return saved ? JSON.parse(saved) : [
    { id: 1, text: 'React lernen', completed: true },
    { id: 2, text: 'Assignment machen', completed: false }
  ];
});

// Bei Änderungen in localStorage speichern
useEffect(() => {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}, [tasks]);

// WICHTIG: nextId muss auch aus localStorage abgeleitet werden!
const [nextId, setNextId] = useState(() => {
  const saved = localStorage.getItem('tasks');
  if (saved) {
    const tasks = JSON.parse(saved);
    return tasks.length ? Math.max(...tasks.map(t => t.id)) + 1 : 1;
  }
  return 3; // Passend zu den Default-Tasks
});
```

---

## Hilfreiche Tipps

### Problem: Komponente wird nicht angezeigt
1. Prüfe, ob die Komponente exportiert wird: `export default KomponentenName`
2. Prüfe den Import-Pfad: `import TaskItem from './TaskItem'`
3. Prüfe die Browser-Konsole auf Fehlermeldungen

### Problem: State ändert sich nicht
1. Verwendest du `setTasks()` statt `tasks = ...`?
2. Erzeugst du ein neues Array/Object? (`[...tasks]`, `{...task}`)
3. Console.log den neuen Wert vor dem `set`-Aufruf

### Problem: Key-Warnung in der Konsole
1. Verwendest du `key={item.id}` in `map()`?
2. Ist der Key eindeutig und stabil?
3. Der Key muss auf dem äußersten Element in `map()` sein

### Problem: Filter funktioniert nicht
1. Wird `setFilter()` aufgerufen?
2. Wird `filteredTasks` korrekt berechnet?
3. Console.log `filter` und `filteredTasks`

### Problem: Input lässt sich nicht tippen
1. Hast du `value={inputValue}` UND `onChange` gesetzt?
2. Ruft `onChange` tatsächlich `setInputValue` auf?

---

## README.md Vorlage

Erstelle eine Datei `README.md` im Projektordner:

```markdown
# Aufgaben-Manager - [Dein Name]

## Beschreibung
Eine React-App zum Verwalten von Aufgaben. Man kann Aufgaben hinzufügen,
als erledigt markieren, löschen und nach Status filtern.

## Verwendete Techniken
- React (Vite Setup)
- Komponenten & Props
- useState für State Management
- Controlled Inputs
- Listen rendern mit map() und Keys
- Konditionales Rendering (&&, Ternary, Early Return)

## Weg
Ich habe Weg [A/B] gewählt.

## Komponenten-Struktur
- **App.jsx** - Hauptkomponente mit State
- **TaskForm.jsx** - Formular zum Hinzufügen
- **FilterButtons.jsx** - Filter-Auswahl
- **TaskList.jsx** - Liste der Aufgaben
- **TaskItem.jsx** - Einzelne Aufgabe

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

Diese Aufgabe soll dir helfen, die React-Grundlagen zu festigen. Du hast jetzt alle wichtigen Konzepte gelernt, um interaktive React-Apps zu bauen!

**Denk daran:** Das Assignment ist freiwillig. Wenn du es einreichst, bekommst du Feedback. Wenn nicht, ist das auch völlig okay!

Bei Fragen: Frag nach! Das ist keine Schwäche, sondern zeigt, dass du verstehen willst.
