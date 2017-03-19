CREATE TABLE user (
	email	VARCHAR(64)	PRIMARY KEY,
);

CREATE TABLE vehicle (
	vid		VARCHAR(64)	PRIMARY KEY,
	email	VARCHAR(64)	REFERENCES user(email),
);

CREATE TABLE trip (
	tid		VARCHAR(64)	PRIMARY KEY,
	vid		VARCHAR(64)	REFERENCES vehicle(vid),
	email 	VARCHAR(64)	REFERENCES user(email),
);

CREATE TABLE event (
	etime 	TIME 		PRIMARY KEY,
	tid 	VARCHAR(64)	REFERENCES trip(tid) 
	# other event params here 
);

CREATE TABLE trip_participants (
	email 	VARCHAR(64) REFERENCES user(email),
	tid		VARCHAR(64) REFERENCES trip(tid)
	UNIQUE (email,vid)
);

CREATE TABLE vehicle_ownership (
	email 	VARCHAR(64)	REFERENCES user(email),
	vid 	VARCHAR(64)	REFERENCES vehicle(vid),
	UNIQUE (email,vid)
);

