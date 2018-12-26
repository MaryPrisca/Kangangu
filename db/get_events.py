import MySQLdb
from connect import db


def getEvents(search=""):
    cursor = db.cursor()

    if search == "":
        sql = """SELECT `event_id`, `event_name`, `event_date`, `event_desc`
                    FROM `events` WHERE deleted = 0"""
    else:
        sql = """SELECT `event_id`, `event_name`, `event_date`, `event_desc`
                    FROM `events` WHERE deleted = 0 AND (event_name LIKE %s OR event_date LIKE %s OR event_desc LIKE %s)"""

    try:
        if search == "":
            cursor.execute(sql)
        else:
            cursor.execute(sql, ('%' + search + '%', '%' + search + '%', '%' + search + '%',))

        data = [{
            'event_id': row[0],
            'event_name': row[1],
            'event_date': row[2],
            'event_desc': row[3]} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret