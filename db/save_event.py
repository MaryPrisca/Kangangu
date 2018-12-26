import MySQLdb
from connect import db

from datetime import datetime


def saveEvent(data):
    data["event_id"] = 0

    dte = str(data["event_date"])
    dte = dte[:-9]
    data["event_date"] = datetime.strptime(dte, "%d/%m/%Y").date()

    cursor = db.cursor()

    sql = """INSERT INTO `events`(`event_id`, `event_name`, `event_date`, `event_desc`) 
            VALUES (%s, %s, %s, %s)"""

    try:
        cursor.execute(sql, (data["event_id"], data["event_name"], data["event_date"], data["event_desc"]))

        db.commit()

        ret = cursor.lastrowid
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        # Rollback in case there is any error
        db.rollback()

        ret = False

    return ret


def editEvent(data):
    dte = str(data["event_date"])
    dte = dte[:-9]
    data["event_date"] = datetime.strptime(dte, "%d/%m/%Y").date()

    cursor = db.cursor()

    sql = """ UPDATE events SET
                    event_name = %s,
                    event_desc = %s,
                    event_date = %s
                    WHERE event_id = %s """

    data = (data["event_name"], data["event_desc"], data["event_date"], data["event_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()
        ret = False

    return ret


def deleteEvent(id):
    cursor = db.cursor()

    sql = """ UPDATE events SET deleted = %s WHERE event_id = %s """

    data = (1, id)

    try:
        cursor.execute(sql, data)
        db.commit()
        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret