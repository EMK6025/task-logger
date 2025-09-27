 CREATE TABLE logs (
    id                  SERIAL PRIMARY KEY,
    name                TEXT NOT NULL,
    date                DATE NOT NULL,
    start_time          TIME NOT NULL,
    duration            INTERVAL NOT NULL,
    description         TEXT,
    distractions        INTEGER DEFAULT 0 CHECK (distractions >= 0),
    context_switches    INTEGER DEFAULT 0 CHECK (context_switches >= 0)
);