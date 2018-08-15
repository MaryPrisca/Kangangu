import MySQLdb
from connect import db


def checkIfSetupIsComplete():
    cursor = db.cursor()

    sql = "SELECT setup_complete FROM system_setup"

    try:
        cursor.execute(sql)

        if cursor.rowcount < 1:
            ret = False
        else:
            for row in cursor:
                ret = row[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret