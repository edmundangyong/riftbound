import sqlite3

def init_db():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sets (
            code TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            number INTEGER NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            domains TEXT,
            type TEXT,
            energy INTEGER,
            power INTEGER,
            might TEXT,
            tags TEXT,
            name TEXT,
            keywords TEXT,
            text TEXT,
            flavour TEXT,
            id TEXT PRIMARY KEY,
            set_code TEXT,
            number INTEGER,
            variant TEXT,
            image_url TEXT,
            quantity INTEGER NOT NULL DEFAULT 0,
            quantity_foil INTEGER NOT NULL DEFAULT 0,
            quantity_promo INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (set_code) REFERENCES sets(code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS legends (
            domains TEXT,
            tags TEXT,
            name TEXT NOT NULL,
            text TEXT NOT NULL,
            id TEXT PRIMARY KEY,
            set_code TEXT NOT NULL,
            number INTEGER NOT NULL,
            variant TEXT,
            image_url TEXT NOT NULL,
            FOREIGN KEY (set_code) REFERENCES sets(code)
        )
    ''')

    conn.commit()
    conn.close()
    print("SUCCESS MESSAGE")

if __name__ == '__main__':
    init_db()