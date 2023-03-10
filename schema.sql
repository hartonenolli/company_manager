CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE work (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    costumer TEXT,
    work_type TEXT,
    price INTEGER,
    status TEXT,
    date DATE
);

CREATE TABLE modify (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    modifier INTEGER REFERENCES users,
    work_id INTEGER REFERENCES work,
    explination TEXT,
    time TIMESTAMP,
    costumer TEXT,
    work_type TEXT,
    price INTEGER,
    status TEXT,
    date DATE
);

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    time TIMESTAMP,
    memo TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    notes_id INTEGER REFERENCES notes,
    time TIMESTAMP,
    comment TEXT
);
