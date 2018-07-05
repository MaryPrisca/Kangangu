import MySQLdb
from connect import db


def login(data):
    cursor = db.cursor()

    # binary keyword to perform case sensitive search
    sql = """SELECT `user_id`, `first_name`, `last_name`, `surname`, `email`, `dob`, `gender`, `username`, 
                `role`, `class_id`, `status`, `created_at`
            FROM `users`
            WHERE deleted = 0 AND binary username = %s AND binary password = %s """

    try:
        cursor.execute(sql, (data['username'], data['password'], ))

        count = cursor.rowcount

        if count < 1:
            ret = False
        else:
            data = [{
                'user_id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'surname': row[3],
                'email': row[4],
                'dob': row[5],
                'gender': row[6],
                'username': row[7],
                'role': row[8],
                'class_id': row[9],
                'status': row[10],
                'created_at': row[11]} for row in cursor.fetchall()]

            ret = data

            # data = [item[0] for item in cursor.fetchall()]
            #
            # # Save the id of the user that has just logged in to access it from the rest of the app
            # cursor = db.cursor()
            #
            # sql = "UPDATE `logged_in` SET `user_id`=%d" % data[0]
            #
            # try:
            #     cursor.execute(sql)
            #
            #     db.commit()
            #     ret = True
            #
            # except(MySQLdb.Error, MySQLdb.Warning) as e:
            #     print(e)
            #
            #     db.rollback()
            #     ret = False

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret
