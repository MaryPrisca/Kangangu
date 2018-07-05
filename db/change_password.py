import MySQLdb
from connect import db
from datetime import datetime

def checkOldPassword(user_id, old_password):
    cursor = db.cursor()

    # binary keyword to perform case sensitive search
    sql = """SELECT user_id, first_name, last_name, surname, dob, gender, username, password
            FROM `users`
            WHERE user_id = %s AND binary password = %s"""

    try:
        cursor.execute(sql, (user_id, old_password, ))

        count = cursor.rowcount

        if count < 1:
            ret = False
        else:
            ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def changePassword(data):
    cursor = db.cursor()

    sql = """ UPDATE users SET password = %s WHERE user_id = %s """

    data = (data["password"], data["user_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        db.rollback()

        # ret = e
        ret = False

    return ret