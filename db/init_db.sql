DROP TABLE IF EXISTS portfolio_positions;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL
);

CREATE TABLE portfolio_positions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    symbol TEXT NOT NULL,
    amount REAL NOT NULL,
    value REAL NOT NULL
);

INSERT INTO users (id, email) VALUES ("2", "qa+portfolio@example.com");

INSERT INTO portfolio_positions (user_id, symbol, amount, value) VALUES
    ("2", "ETH", 1.25, 3200.50),
    ("2", "MATIC", 1500.00, 1800.75);
