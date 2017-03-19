import ipdb
import psycopg2

#db stuff
dbName = 'fabshare'
dbUser = 'postgres'
dbPass = 'space1'
__conn = None #db connection

def testDB():
    returnVal = None
    conn = psycopg2.connect("dbname=%s user=%s password=%s" % (dbName, dbUser, dbPass))

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute("CREATE TABLE human (email VARCHAR(64) PRIMARY KEY);")
    conn.commit()

    # cur.execute("CREATE TABLE vehicle (vid VARCHAR(64) PRIMARY KEY, email VARCHAR(64) REFERENCES human(email));")
    # conn.commit()   

    # cur.execute("CREATE TABLE trip (tid   VARCHAR(64) PRIMARY KEY,vid   VARCHAR(64) REFERENCES vehicle (vid),email VARCHAR(64) REFERENCES human (email),startCity     VARCHAR(64),endCity       VARCHAR(64),distance      REAL,efficiency    REAL,date  TIMESTAMP);") 
    # conn.commit()    

    # cur.execute("CREATE TABLE event (etime TIMESTAMP PRIMARY KEY, tid   VARCHAR(64) REFERENCES trip (tid));")
    # conn.commit() 

    # cur.execute("CREATE TABLE trip_participants (tid   VARCHAR(64) REFERENCES trip (tid),email VARCHAR(64) REFERENCES human (email),PRIMARY KEY (tid, email));")
    # conn.commit()
    
    # cur.execute("CREATE TABLE vehicle_ownership (email VARCHAR(64) REFERENCES human (email),vid   VARCHAR(64) REFERENCES vehicle (vid),PRIMARY KEY (email, vid));")
    # conn.commit()

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO human(email) VALUES (%s)", ("hello@hello.com",))
    conn.commit()

    cur.execute("INSERT INTO human(email) VALUES (%s)", ("bye@bye.com",))
    conn.commit()

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM human;")
    returnVal = cur.fetchall()
    # returns cur.execute("SELECT * FROM test;")

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    return returnVal

def getTestData():
    print(__conn)
    # Open a cursor to perform database operations
    cur = __conn.cursor()
    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM human;")
    returnVal = cur.fetchall()
    # returns cur.execute("SELECT * FROM test;")
    # ipdb.set_trace()
    cur.close()
    return returnVal

def init():
    # Connect to an existing database
    global __conn
    if __conn is None:
        __conn = psycopg2.connect("dbname=%s user=%s password=%s" % (dbName, dbUser, dbPass))


def shutdown():
    # Close communication with the database
    # ipdb.set_trace() #for debug
    __conn.close()


testDB()
getTestData()
init()
shutdown()
