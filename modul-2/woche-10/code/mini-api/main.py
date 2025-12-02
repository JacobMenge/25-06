"""
Mini Notes API - Tag 2: SQLite Version
"""
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI-App erstellen
app = FastAPI(title="Mini Notes API", version="2.0.0")

# Datenbank-Dateiname
DATABASE = "notes.db"

class NoteCreate(BaseModel):
    """Schema für das Erstellen einer Notiz."""
    text: str

def init_db():
    """Datenbank initialisieren und Tabelle erstellen."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Datenbank beim Start initialisieren
init_db()

@app.get("/")
def root():
    """API-Übersicht"""
    return {
        "name": "Mini Notes API",
        "version": "2.0.0",
        "database": "SQLite",
        "endpoints": ["/notes", "/notes/{id}"]
    }

@app.get("/notes")
def get_all_notes():
    """Alle Notizen abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Ermöglicht Dict-Zugriff
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Neue Notiz erstellen"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO notes (text) VALUES (?)",
        (note.text,)  # Tuple mit einem Element (Komma beachten!)
    )
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {"id": new_id, "text": note.text}


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    return dict(row)