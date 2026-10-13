# riftbound

database containing (almost) all riftbound cards

## schema

### sets
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    number INTEGER NOT NULL

### cards (main deck)
    domains TEXT,
    type TEXT NOT NULL,
    energy INTEGER NOT NULL,
    power INTEGER NOT NULL DEFAULT 0,
    might TEXT,
    tags TEXT,
    name TEXT NOT NULL,
    keywords TEXT,
    text TEXT,
    flavour TEXT,
    id TEXT PRIMARY KEY,
    set_code TEXT NOT NULL,
    number INTEGER NOT NULL,
    variant TEXT,
    image_url TEXT NOT NULL,
    FOREIGN KEY (set_code) REFERENCES sets(code)

### legends
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