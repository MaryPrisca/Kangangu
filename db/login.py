import MySQLdb
from connect import db


def login(data):
    cursor = db.cursor()

    # binary keyword to perform case sensitive search
    sql = """SELECT `user_id`, `first_name`, `last_name`, `surname`, `email`, `dob`, `gender`, `username`, 
                `role`, `class_id`, `status`, `created_at`, `reg_no`
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
                'created_at': row[11],
                'reg_no': row[12],
                'school_details': getSchoolDetails()} for row in cursor.fetchall()]

            ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getSchoolDetails():
    cursor = db.cursor()

    sql = """SELECT `school_name`, `subjects_lower_forms`, `setup_complete` FROM `system_setup`"""

    try:
        cursor.execute(sql)
        count = cursor.rowcount

        if count < 1:
            ret = False
        else:
            data = [{
                'school_name': row[0],
                'lower_subjects': row[1]} for row in cursor.fetchall()]

            ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret
