import ipdb
import psycopg2

#db stuff
dbName = 'fabshare'
dbUser = 'postgres'
__conn = None #db connection

def testDB():
    returnVal = None
    conn = psycopg2.connect("dbname=%s user=%s" % (dbName, dbUser))

    # Open a cursor to perform database operations
    cur = conn.cursor()

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
    cur.execute("SELECT * FROM test;")
    returnVal = cur.fetchone()
    # returns cur.execute("SELECT * FROM test;")
    # ipdb.set_trace()
    cur.close()
    return returnVal

def init():
    # Connect to an existing database
    global __conn
    if __conn is None:
        __conn = psycopg2.connect("dbname=%s user=%s" % (dbName, dbUser))


def shutdown():
    # Close communication with the database
    # ipdb.set_trace() #for debug
    __conn.close()