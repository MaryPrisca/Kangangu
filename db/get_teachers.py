import MySQLdb
from connect import db


def getTeachers(class_id=0, search=""):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # if class_id > 0:
    #     sql = """SELECT user_id, first_name, last_name, surname, email, username, dob, gender
    #                 FROM `users` u
    #                 WHERE u.deleted = 0 AND role='%s'""" % 'teacher'
    #
    # else:
    sql = """SELECT user_id, first_name, last_name, surname, email, username, dob, gender
                FROM `users` u
                WHERE u.deleted = 0 AND role='%s'""" % 'teacher'

    sql = """SELECT user_id, first_name, last_name, surname, email, username, dob, gender, s.subject_alias AS subject1, s2.subject_alias AS subject2
                FROM users u
                JOIN subjects s ON u.subject1 = s.subject_id
                LEFT JOIN subjects s2 ON u.subject2 = s2.subject_id
                WHERE u.deleted = 0 AND role='%s'""" % 'teacher'

    try:
        if search != "":
            cursor.execute("SELECT user_id, first_name, last_name, surname, email, username, dob, gender, s.subject_alias AS subject1, s2.subject_alias AS subject2 \
                           FROM `users` u \
                           JOIN subjects s ON u.subject1 = s.subject_id \
                           LEFT JOIN subjects s2 ON u.subject2 = s2.subject_id \
                           WHERE u.deleted = 0 AND role=%s AND (first_name LIKE %s OR last_name LIKE %s OR surname LIKE %s OR email like %s OR username like %s OR dob LIKE %s OR s.subject_alias LIKE %s OR s2.subject_alias LIKE %s)", \
                           ('teacher', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%',))
        else:
            cursor.execute(sql)

        data = [{
            'user_id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'surname': row[3],
            'full_names': row[1] + " " + row[2] + " " + row[3],
            'email': row[4],
            'username': row[5],
            'dob': row[6],
            'gender': "Male" if row[7] == "M" else "Female",
            'subject1': row[8].lower().capitalize(),
            'subject2': "--" if row[9] == None else row[9].lower().capitalize()} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        # ret = e
        ret = False

    return ret
