import ipdb
import globals
import psycopg2

def getID():
    # Open a cursor to perform database operations
    cur = globals.__conn.cursor()
    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM human;")
    returnVal = cur.fetchone()
    # returns cur.execute("SELECT * FROM test;")
    # ipdb.set_trace()
    cur.close()
    return returnVal

def createTestDB():
        # conn = psycopg2.connect("dbname=fabshare user=postgres")

    # Open a cursor to perform database operations
    cur = globals.__conn.cursor()

    # Execute a command: this creates a new table
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")
    returnVal = cur.fetchone()
    # returns cur.execute("SELECT * FROM test;")

    # Make the changes to the database persistent
    globals.__conn.commit()

    # Close communication with the database
    cur.close()
    globals.__conn.close()
    return returnVal

def insertEmail(userEmail):
    cur = globals.__conn.cursor()

    # string = "INSERT INTO human (email) VALUES ('test@test.com')"
    # cur.execute(string)
    try:
        cur.execute("INSERT INTO human (email) VALUES (%s)", (userEmail,)) #super hacky
    except:
        print("Email already exists in the db")

    globals.__conn.commit()

    cur.close()
    return

def insertVehicles(filteredTrips, userEmail):
    cur = globals.__conn.cursor()

    vidList = set()
    for trip in filteredTrips:
        vidList.add(trip["vid"])

    for vid in vidList:
        try:
            print("%s %s" % (vid, userEmail))
            cur.execute("INSERT INTO vehicle (vid, email) VALUES (%s, %s)", (vid, userEmail))
        except:
            print("Vehicle already exists in the db")

    globals.__conn.commit()

    cur.close()
    return

def insertTrips(filteredTrips, userEmail):
    cur = globals.__conn.cursor()

    #   tid   VARCHAR(64) PRIMARY KEY,
    #   vid   VARCHAR(64) REFERENCES vehicle (vid),
    #   email VARCHAR(64) REFERENCES human (email),
    #   startCity VARCHAR(64),
    #   endCity VARCHAR(64),
    #   distance REAL,
    #   efficiency REAL,
    #   date TIMESTAMP


    for trip in filteredTrips:
        try:
            print( "%s, %s, %s, %s, %s, %s, %s, %s)",
            (trip["tid"], trip["vid"], userEmail, trip["startCity"], trip["endCity"],
             trip["distance"], trip["efficiency"], trip["startTimestamp"]))

            cur.execute("INSERT INTO trip (tid, vid, email, startCity, endCity, distance, efficiency, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (trip["tid"], trip["vid"], userEmail, trip["startCity"], trip["endCity"], trip["distance"], trip["efficiency"], trip["startTimestamp"]))

        except:
            print("Trip already exists in the db")

    globals.__conn.commit()

    cur.close()
    return


def init():
    # Connect to an existing database
    if globals.__conn is None:
        globals.__conn = psycopg2.connect("dbname=%s user=%s" % (globals.dbName, globals.dbUser))


def shutdown():
    # Close communication with the database
    # ipdb.set_trace() #for debug
    globals.__conn.close()