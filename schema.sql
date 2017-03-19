CREATE TABLE human (
  email VARCHAR(64) PRIMARY KEY
);

CREATE TABLE vehicle (
  vid   VARCHAR(64) PRIMARY KEY,
  email VARCHAR(64) REFERENCES human (email)
);

CREATE TABLE trip (
  tid   VARCHAR(64) PRIMARY KEY,
  vid   VARCHAR(64) REFERENCES vehicle (vid),
  email VARCHAR(64) REFERENCES human (email),
  startCity VARCHAR(64),
  endCity VARCHAR(64),
  distance REAL,
  efficiency REAL,
  date TIMESTAMP
);

CREATE TABLE event (
  etime TIMESTAMP PRIMARY KEY,
  tid   VARCHAR(64) REFERENCES trip (tid)
  --other EVENT params here
);

CREATE TABLE trip_participants (
  tid   VARCHAR(64) REFERENCES trip (tid),
  email VARCHAR(64) REFERENCES human (email),
  PRIMARY KEY (tid, email)
);

CREATE TABLE vehicle_ownership (
  email VARCHAR(64) REFERENCES human (email),
  vid   VARCHAR(64) REFERENCES vehicle (vid),
  PRIMARY KEY (email, vid)
);

