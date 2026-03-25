PRAGMA foreign_keys = 0;

CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                          FROM pm_objects;

DROP TABLE pm_objects;

CREATE TABLE pm_objects (
    id    TEXT    PRIMARY KEY
                  UNIQUE,
    x     INTEGER,
    y     INTEGER,
    fx    INTEGER,
    fy    INTEGER,
    color INTEGER,
    el    REAL    DEFAULT (0.5),
    shape INTEGER DEFAULT (0),
    size  INTEGER DEFAULT (50)
);

INSERT INTO pm_objects (
                           id,
                           x,
                           y,
                           fx,
                           fy,
                           color,
                           el,
                           shape
                       )
                       SELECT id,
                              x,
                              y,
                              fx,
                              fy,
                              color,
                              el,
                              shape
                         FROM sqlitestudio_temp_table;

DROP TABLE sqlitestudio_temp_table;

PRAGMA foreign_keys = 1;
