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
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            domains TEXT,
            set_code TEXT NOT NULL,
            number INTEGER NOT NULL,
            variant TEXT,
            energy INTEGER NOT NULL,
            power INTEGER NOT NULL DEFAULT 0,
            text TEXT,
            flavour TEXT,
            keywords TEXT,
            might TEXT,
            image_url TEXT NOT NULL,
            FOREIGN KEY (set_code) REFERENCES sets(code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS legends (
            id TEXT PRIMARY KEY,
            set_code TEXT NOT NULL,
            number INTEGER NOT NULL,
            variant TEXT,
            name TEXT NOT NULL,
            text TEXT NOT NULL,
            domains TEXT,
            image_url TEXT NOT NULL,
            FOREIGN KEY (set_code) REFERENCES sets(code)
        )
    ''')

    conn.commit()
    conn.close()
    print("SUCCESS MESSAGE")

if __name__ == '__main__':
    init_db()