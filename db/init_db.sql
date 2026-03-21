CREATE TABLE parameters (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE,
    g        INTEGER,
    friction NUMERIC,
    width    INTEGER,
    height   INTEGER,
    fps      INTEGER
);

CREATE TABLE pm_objects (
    id    TEXT    PRIMARY KEY
                  UNIQUE,
    x     INTEGER,
    y     INTEGER,
    fx    INTEGER,
    fy    INTEGER,
    color INTEGER,
    el REAL DEFAULT (0.5),
    shape INTEGER DEFAULT (0)
);