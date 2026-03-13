import sqlite3
import random

def genera():
    conn = sqlite3.connect('cucinamilazzo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM calendario')
    
    giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    for g in giorni:
        # Pranzo
        cursor.execute("SELECT id FROM ricette WHERE categoria='pasta' ORDER BY RANDOM() LIMIT 1")
        p = cursor.fetchone()
        if p: cursor.execute('INSERT INTO calendario VALUES (?, "Pranzo", ?)', (g, p[0]))
        # Cena
        cursor.execute("SELECT id FROM ricette ORDER BY RANDOM() LIMIT 1")
        c = cursor.fetchone()
        if c: cursor.execute('INSERT INTO calendario VALUES (?, "Cena", ?)', (g, c[0]))
    
    conn.commit()
    conn.close()
    print("📅 Calendario generato!")

if __name__ == "__main__":
    genera()
