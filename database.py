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
            set_code TEXT NOT NULL,
            number INTEGER NOT NULL,
            variant TEXT,
            image_url TEXT,
            name TEXT,
            text TEXT,
            rarity TEXT,
            quantity_en INTEGER NOT NULL DEFAULT 0,
            quantity_foil_en INTEGER NOT NULL DEFAULT 0,
            quantity_promo_en INTEGER NOT NULL DEFAULT 0,
            quantity_cn INTEGER NOT NULL DEFAULT 0,
            quantity_foil_cn INTEGER NOT NULL DEFAULT 0,
            quantity_promo_cn INTEGER NOT NULL DEFAULT 0,
            quantity_fr INTEGER NOT NULL DEFAULT 0,
            quantity_foil_fr INTEGER NOT NULL DEFAULT 0,
            quantity_promo_fr INTEGER NOT NULL DEFAULT 0,
            quantity_kr INTEGER NOT NULL DEFAULT 0,
            quantity_foil_kr INTEGER NOT NULL DEFAULT 0,
            quantity_promo_kr INTEGER NOT NULL DEFAULT 0,
            banned INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (set_code) REFERENCES sets(code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main_deck (
            id TEXT PRIMARY KEY,
            domains TEXT,
            type TEXT,
            energy INTEGER,
            power INTEGER,
            might INTEGER,
            tags TEXT,
            keywords TEXT,
            flavour TEXT,
            FOREIGN KEY (id) REFERENCES cards(id) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS legends (
            id TEXT PRIMARY KEY,
            domains TEXT,
            tags TEXT,
            FOREIGN KEY (id) REFERENCES cards(id) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS battlefields (
            id TEXT PRIMARY KEY,
            FOREIGN KEY (id) REFERENCES cards(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()
    print("SUCCESS MESSAGE")

def get_card(card_id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    clean_id = card_id.strip().upper()

    cursor.execute('''
        SELECT
            id, set_code, number, variant, image_url, name, rarity, banned,
            quantity_en, quantity_foil_en, quantity_promo_en,
            quantity_cn, quantity_foil_cn, quantity_promo_cn,
            quantity_fr, quantity_foil_fr, quantity_promo_fr,
            quantity_kr, quantity_foil_kr, quantity_promo_kr
        FROM cards
        WHERE id = ?
    ''', (clean_id,))

    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None

if __name__ == '__main__':
    init_db()