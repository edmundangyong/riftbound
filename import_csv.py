import csv
import sqlite3

DB_PATH = 'database.db'

def clean(value):
    if value is None:
        return None
    stripped = value.strip()
    return stripped if stripped != "" else None

def import_sets():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    with open('csv/sets.csv', mode='r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO sets (code, name, number)
                VALUES (?, ?, ?)
                ON CONFLICT(code) DO UPDATE SET
                    name = excluded.name,
                    number = excluded.number
            ''', (
                clean(row['code']),
                clean(row['name']),
                int(clean(row['number']))
            ))

    conn.commit()
    conn.close()
    print(f"IMPORTED SETS")

def import_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    with open('csv/cards.csv', mode='r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO cards (id, set_code, number, variant, image_url)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    set_code = excluded.set_code,
                    number = excluded.number,
                    variant = excluded.variant,
                    image_url = excluded.image_url
            ''', (
                clean(row['id']),
                clean(row['set_code']),
                int(clean(row['number'])),
                clean(row.get('variant')),
                clean(row.get('image_url'))
            ))

    conn.commit()
    conn.close()
    print(f"IMPORTED CARDS")

if __name__ == '__main__':
    import_sets()
    import_cards()