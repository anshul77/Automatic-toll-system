import MySQLdb as db

HOST = "sql12.freemysqlhosting.net"
PORT = 3306
USER = "sql12268782"
PASSWORD = "SFiuFyvFZp"
DB = "sql12268782"

global connection

def createConnection():
    global connection
    try:
        connection = db.Connection(host=HOST, port=PORT,
                                   user=USER, passwd=PASSWORD, db=DB)

    except Exception as e:
        print e


def breakConnection():
    global connection
    try:
        connection.close()

    except Exception as e:
        print e


def getVehicleDetails(vehicleNumber):
    try:
        createConnection()
        sqlQuery = "select * from Vehicles where vehicleNumber = '" + vehicleNumber + "'"
        dbhandler = connection.cursor()
        print sqlQuery
        dbhandler.execute(sqlQuery)
        result = dbhandler.fetchall()
        print result
        return result

    except Exception as e:
        return None
        print e

    finally:
        breakConnection()
def updatebalance(vehicleNumber,balance):
    try:
        createConnection()
        sqlQuery = "update Vehicles set balance = "+ balance+" where vehicleNumber= '" + vehicleNumber + "'"
        dbhandler = connection.cursor()
        print sqlQuery
        dbhandler.execute(sqlQuery)
        result = dbhandler.fetchall()
        # print result
        return result

    except Exception as e:
        return None
        print e

    finally:
        breakConnection()

# getVehicleDetails("abcde89")
