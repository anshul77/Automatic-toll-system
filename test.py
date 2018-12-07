import MySQLdb as db

HOST = "sql12.freemysqlhosting.net"
PORT = 3306
USER = "sql12268782"
PASSWORD = "SFiuFyvFZp"
DB = "sql12268782"

try:
    connection = db.Connection(host=HOST, port=PORT,
                               user=USER, passwd=PASSWORD, db=DB)

    dbhandler = connection.cursor()
    dbhandler.execute("Select * from Vehicles")
    result = dbhandler.fetchall()
    for item in result:
        print item

except Exception as e:
    print e

finally:
    connection.close()
