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

def getTestData():
    print(globals.__conn)
    # Open a cursor to perform database operations
    cur = globals.__conn.cursor()
    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")
    returnVal = cur.fetchone()
    # returns cur.execute("SELECT * FROM test;")
    # ipdb.set_trace()
    cur.close()
    return returnVal

def init():
    # Connect to an existing database
    if globals.__conn is None:
        globals.__conn = psycopg2.connect("dbname=%s user=%s" % (globals.dbName, globals.dbUser))


def shutdown():
    # Close communication with the database
    # ipdb.set_trace() #for debug
    globals.__conn.close()