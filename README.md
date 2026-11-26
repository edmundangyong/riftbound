# riftbound

database containing (almost) all riftbound cards

## schema

### sets
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    number INTEGER NOT NULL

### cards
    id TEXT PRIMARY KEY,
    set_code TEXT NOT NULL,
    number INTEGER NOT NULL,
    variant TEXT,
    name TEXT,
    text TEXT,
    image_url TEXT,
    quantity INTEGER NOT NULL DEFAULT 0,
    quantity_foil INTEGER NOT NULL DEFAULT 0,
    quantity_promo INTEGER NOT NULL DEFAULT 0,
    banned INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (set_code) REFERENCES sets(code)

### main_deck
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

### legends
    id TEXT PRIMARY KEY,
    domains TEXT,
    tags TEXT,
    FOREIGN KEY (id) REFERENCES cards(id) ON DELETE CASCADE

### battlefields
    id TEXT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES cards(id) ON DELETE CASCADE