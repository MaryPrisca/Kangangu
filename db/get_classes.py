import MySQLdb
from connect import db


def getFormClasses(form):
    cursor = db.cursor()

    sql = "SELECT class_id, class_name FROM classes \
           WHERE form_name = '%d'" % form
    try:
        cursor.execute(sql)

        ids = []
        names = []

        for row in cursor:
            ids.append(row[0])
            names.append(row[1])

        data = {
            "ids": ids,
            "names": names
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getClassNames():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT class_name FROM classes \
               WHERE deleted = '%d'" % 0
    try:
        # Execute the SQL command
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getClassNamesWithForm():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT class_id, class_name, form_name FROM classes WHERE deleted = 0 ORDER BY form_name"
    try:
        # Execute the SQL command
        cursor.execute(sql)

        ids = []
        names = []
        forms = []

        for row in cursor:
            ids.append(row[0])
            names.append(row[1] if 'Form' in row[1] else str(row[2]) + " " + row[1])  # To avoid having '1 Form 1'
            forms.append(row[2])

        data = {
            "ids": ids,
            "names": names,
            "forms": forms,
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        print cursor._last_executed
        ret = False

    return ret


def getClassDets(search=""):
    cursor = db.cursor()
    # search = "al"

    if search == "":
        sql = """SELECT c.class_id, class_name, form_name, COUNT(user_id) AS students
                        FROM classes c 
                            LEFT JOIN users u 
                                ON c.class_id = u.class_id AND u.deleted = 0 AND u.role = "student"
                        WHERE c.deleted = 0
                        GROUP BY c.class_id
                        ORDER BY c.form_name"""
    else:
        sql = """SELECT c.class_id, class_name, form_name, COUNT(user_id) AS students
                        FROM classes c 
                            LEFT JOIN users u 
                                ON c.class_id = u.class_id AND u.deleted = 0 AND u.role = "student"
                        WHERE c.deleted = 0 AND (class_name LIKE %s OR form_name LIKE %s)
                        GROUP BY c.class_id
                        ORDER BY c.form_name"""
    try:
        if search == "":
            cursor.execute(sql)
        else:
            cursor.execute(sql, ('%' + search + '%', '%' + search + '%',))

        data = [{
            'class_id': row[0],
            'class_name': row[1],
            'students': "0" if row[3] < 1 else row[3],
            'form_name': row[2]} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret


def getNoOfStudentsInClass(class_id):
    cursor = db.cursor()
    sql = """SELECT COUNT(user_id) AS students 
                FROM users u
                JOIN classes c ON c.class_id = u.class_id AND c.deleted = 0
                WHERE u.class_id = %s AND u.deleted = 0""" % class_id
    try:
        cursor.execute(sql)

        data = [0 if row[0] < 1 else row[0] for row in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret


def getNoOfStudentsInForm(form):
    cursor = db.cursor()
    sql = """SELECT COUNT(user_id) AS students 
                FROM users u
                JOIN classes c ON c.class_id = u.class_id AND c.deleted = 0
                WHERE c.form_name = %s AND u.deleted = 0""" % form

    try:
        cursor.execute(sql)

        data = [0 if row[0] < 1 else row[0] for row in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret
