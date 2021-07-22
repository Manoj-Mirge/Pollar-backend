DROP TABLE IF EXISTS Pollar_user;


CREATE TABLE Pollar_user (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
