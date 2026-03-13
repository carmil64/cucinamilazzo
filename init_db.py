import sqlite3

def setup():
    conn = sqlite3.connect('cucinamilazzo.db')
    cursor = conn.cursor()
    # Tabella Ricette
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ricette (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT NOT NULL,
            tempo INTEGER,
            ingredienti TEXT,
            url TEXT UNIQUE,
            categoria TEXT,
            punteggio INTEGER,
            fonte TEXT DEFAULT 'web'
        )
    ''')
    # Tabella Calendario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calendario (
            giorno TEXT,
            pasto TEXT,
            ricetta_id INTEGER,
            FOREIGN KEY(ricetta_id) REFERENCES ricette(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database cucinamilazzo.db inizializzato!")

if __name__ == "__main__":
    setup()