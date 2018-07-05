import MySQLdb
from connect import db


def getStudents(class_id=0, search=""):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    if class_id > 0:
        sql = """SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id AND c.class_id='%s'
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % (class_id, 'student')
    # elif search != "":
    #     sql = """SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name
    #                 FROM `users` u
    #                 JOIN classes c
    #                     ON c.class_id = u.class_id AND c.deleted = 0
    #                 WHERE u.deleted = 0 AND (first_name LIKE %s OR last_name LIKE %s OR surname LIKE %s OR dob LIKE %s)"""

    else:
        sql = """SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % 'student'

    try:
        if search != "":
            # cursor.execute(sql, ('%' + search + '%',))
            cursor.execute("SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name \
                           FROM `users` u JOIN classes c ON c.class_id = u.class_id AND c.deleted = 0 \
                           WHERE u.deleted = 0 AND role=%s AND (first_name LIKE %s OR last_name LIKE %s OR surname LIKE %s OR dob LIKE %s or class_name LIKE %s or form_name LIKE %s)", \
                           ('student', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%',))
        else:
            cursor.execute(sql)

        data = [{
            'user_id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'surname': row[3],
            'full_names': row[1] + " " + row[2] + " " + row[3],
            'dob': row[4],
            'gender': "Male" if row[5] == "M" else "Female",
            'class_id': row[6],
            'class': row[7],
            'form': row[8]} for row in cursor.fetchall()]
        # data = [[row[0], row[1], row[2], row[3], row[4], row[5], row[6]] for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret
