import MySQLdb
from connect import db


def getStudents(class_id=0, search=""):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    if class_id > 0:
        sql = """SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name, reg_no
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id AND c.class_id='%s'
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % (class_id, 'student')

    else:
        sql = """SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name, reg_no
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % 'student'

    try:
        if search != "":
            cursor.execute("SELECT user_id, first_name, last_name, surname, dob, gender, u.class_id, class_name, form_name, reg_no \
                           FROM `users` u JOIN classes c ON c.class_id = u.class_id AND c.deleted = 0 \
                           WHERE u.deleted = 0 AND role=%s AND (reg_no LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR surname LIKE %s OR dob LIKE %s or class_name LIKE %s or form_name LIKE %s)", \
                           ('student', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%',))
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
            'form': row[8],
            'reg_no': row[9]} for row in cursor.fetchall()]
        # data = [[row[0], row[1], row[2], row[3], row[4], row[5], row[6]] for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret


def getStudentByIDAllDetails(id):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """SELECT `user_id`,`first_name`, `last_name`, `surname`, `dob`, `gender`, u.class_id, `subjects_taken`, `kcpe_marks`, 
                    `birth_cert_no`, `next_of_kin_name`, `next_of_kin_phone`, `address`, `created_at`, class_name, form_name, reg_no
                FROM `users` u
                JOIN classes c
                    ON c.class_id = u.class_id
                WHERE u.deleted = 0 AND user_id = %s AND role='%s'""" % (id, 'student')

    try:
        cursor.execute(sql)

        data = [{
            'user_id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'surname': row[3],
            'dob': row[4],
            'gender': "Male" if row[5] == "M" else "Female",
            'class_id': row[6],
            'subjects_taken': row[7],
            'kcpe_marks': "" if row[8] is None else row[8],
            'birth_cert_no': "" if row[9] is None else row[9],
            'next_of_kin_name': "" if row[10] is None else row[10],
            'next_of_kin_phone': "" if row[11] is None else row[11],
            'address': "" if row[12] is None else row[12],
            'created_at': row[13],
            'class': row[14],
            'form': row[15],
            'reg_no': row[16]} for row in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret


def getStudentByID(id):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """SELECT first_name, last_name, surname, class_name, form_name, reg_no
                        FROM `users` u
                        JOIN classes c
                            ON c.class_id = u.class_id
                        WHERE u.deleted = 0 AND user_id = %s AND role='%s'""" % (id, 'student')

    try:
        cursor.execute(sql)

        data = [{
            'full_names': row[2] + " " + row[0] + " " + row[1],
            'class': row[3],
            'form': row[4],
            'reg_no': row[5]} for row in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret


# def getNumberOfStudentsTakingSubject(subject_id, form, compulsory):
#     """"""
