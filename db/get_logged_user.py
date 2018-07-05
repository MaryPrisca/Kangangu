import MySQLdb
from connect import db


def get_logged_in_user():
    cursor = db.cursor()

    sql = """SELECT logged_in.user_id, `first_name`, `last_name`, `surname`, `email`, `dob`, `gender`, `username`, 
                `role`, `class_id`, `status`, `created_at`
            FROM `logged_in` 
            JOIN users 
                ON users.user_id = logged_in.user_id"""

    try:
        cursor.execute(sql)

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

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret
