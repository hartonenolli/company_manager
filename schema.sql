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