from fastapi import FastAPI

app = FastAPI(title="Mini Notes API")

# Dummy-Daten (später: echte Datenbank)
notes = [
    {"id": 1, "text": "Erste Notiz", "created_at": "2025-12-01T10:00:00"},
    {"id": 2, "text": "Zweite Notiz", "created_at": "2025-12-01T14:30:00"},
]

@app.get("/health")
def health_check():
    """Health-Check Endpoint."""
    return {"status": "ok"}

@app.get("/notes")
def get_all_notes():
    """Gibt alle Notizen zurück."""
    return notes


