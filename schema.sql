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
    reason TEXT,
    time TIMESTAMP
);