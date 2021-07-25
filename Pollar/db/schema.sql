DROP TABLE IF EXISTS Pollar_user;
DROP TABLE IF EXISTS Polls;
DROP TABLE IF EXISTS Pollar_user;
DROP TABLE IF EXISTS privacy;
DROP TABLE IF EXISTS Poll_options;


CREATE TABLE Pollar_user (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE Privacy (
privacy_id SERIAL PRIMARY KEY,
type TEXT UNIQUE NOT NULL 
);

INSERT INTO privacy (type) VALUES ('public');
INSERT INTO privacy (type) VALUES ('private');


CREATE TABLE Polls (
poll_id SERIAL PRIMARY KEY,
author_id INTEGER NOT NULL REFERENCES Pollar_user (id) ON DELETE CASCADE,
title TEXT NOT NULL,
description TEXT ,
created_on TIMESTAMP NOT NULL,
deadline TIMESTAMP NOT NULL,
privacy INTEGER NOT NULL REFERENCES Privacy (privacy_id) ON DELETE CASCADE
);


CREATE TABLE Poll_options (
poll_options_id SERIAL PRIMARY KEY,
poll_id INTEGER NOT NULL REFERENCES Polls (poll_id) ON DELETE CASCADE,
option_title TEXT NOT NULL
);



