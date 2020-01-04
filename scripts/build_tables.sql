CREATE TABLE IF NOT EXISTS students (
	id   TEXT PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS activity (
	id       TEXT NOT NULL,
	checkin  INTEGER,
	checkout INTEGER,
	FOREIGN KEY(id) REFERENCES students(id)
);

.quit
