DROP TABLE IF EXISTS pollar_user;
DROP TABLE IF EXISTS polls;
DROP TABLE IF EXISTS poll_options;
DROP TABLE IF EXISTS privacy;



CREATE TABLE pollar_user (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE privacy (
privacy_id SERIAL PRIMARY KEY,
type TEXT UNIQUE NOT NULL 
);

INSERT INTO privacy (type) VALUES ('public');
INSERT INTO privacy (type) VALUES ('private');


CREATE TABLE polls (
poll_id SERIAL PRIMARY KEY,
author_id INTEGER NOT NULL REFERENCES pollar_user (id),
title TEXT NOT NULL,
description TEXT ,
created_on TIMESTAMP NOT NULL,
deadline TIMESTAMP NOT NULL,
privacy INTEGER NOT NULL REFERENCES privacy (privacy_id) 
);


CREATE TABLE poll_options (
poll_options_id SERIAL PRIMARY KEY,
poll_id INTEGER NOT NULL REFERENCES polls (poll_id) ,
option_title TEXT NOT NULL
);

CREATE TABLE share_link (
poll_id INTEGER UNIQUE NOT NULL REFERENCES polls (poll_id),
link TEXT NOT NULL UNIQUE
);

CREATE TABLE poll_votes (
  vote_id SERIAL PRIMARY KEY,
  vote INTEGER NOT NULL REFERENCES poll_options (poll_options_id),
  voter_id INTEGER NOT NULL REFERENCES pollar_user (id),
  voted_on TIMESTAMP NOT NULL
);

