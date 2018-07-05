import MySQLdb
from connect import db


def login(data):
    cursor = db.cursor()

    # binary keyword to perform case sensitive search
    sql = """SELECT user_id, first_name, last_name, surname, dob, gender, username, password
            FROM `users`
            WHERE deleted = 0 AND binary username = %s AND binary password = %s """

    try:
        cursor.execute(sql, (data['username'], data['password'], ))

        count = cursor.rowcount

        if count < 1:
            ret = False
        else:
            data = [item[0] for item in cursor.fetchall()]

            # Save the id of the user that has just logged in to access it from the rest of the app
            cursor = db.cursor()

            sql = "UPDATE `logged_in` SET `user_id`=%d" % data[0]

            try:
                cursor.execute(sql)

                db.commit()
                ret = True

            except(MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)

                db.rollback()
                ret = False

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret
