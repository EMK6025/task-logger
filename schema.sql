CREATE TABLE logs (
    id                  SERIAL PRIMARY KEY,
    name                TEXT NOT NULL,
    date                DATE NOT NULL,
    start_time          TIME NOT NULL,
    duration            INTERVAL NOT NULL,
    description         TEXT,
    sub_tasks           INTEGER DEFAULT 1 CHECK (sub_tasks >= 1)
);