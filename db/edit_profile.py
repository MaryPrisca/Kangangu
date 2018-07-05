import MySQLdb
from connect import db
from datetime import datetime
# import pytz

def editProfile(data):
    cursor = db.cursor()

    sql = """ UPDATE users SET
                    first_name = %s,
                    last_name = %s,
                    surname = %s,
                    email = %s,
                    username = %s,
                    dob = %s,
                    gender = %s               
                    WHERE user_id = %s """

    data = (data["first_name"], data["last_name"], data["surname"], data["email"], data["username"], data["dob"], data["gender"], data["user_id"])

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