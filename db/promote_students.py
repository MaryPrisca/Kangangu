import MySQLdb
from connect import db

from save_class import saveClass


def promoteStudents():
    formFours = getAllFormFours()

    updateFormFoursToAlumnus(formFours)

    forms = [3, 2, 1]

    for form in forms:
        # Get all classes per form
        formClasses = getAllClassesInForm(form)

        # for each of those classes get the corresponding class_id in next form
        for clas in formClasses:
            current_class = clas['class_id']

            # If there's a class in next form with respective class_name, get it's class ID
            if getClassIDNextForm(clas):
                next_class = getClassIDNextForm(clas)

            else:  # Else, create the class afresh and get it's id
                data = {
                    "class_name": clas['class_name'],
                    "form_name": clas['form_name'] + 1
                }

                next_class = saveClass(data)

            # Update the class_id in users table for all students in that class
            updateStudentsToNextClass(current_class, next_class)


def getAllFormFours():
    cursor = db.cursor()

    sql = """SELECT user_id
                FROM `users` u
                JOIN classes c
                    ON c.class_id = u.class_id AND form_name = 4
                WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s' AND alumnus = 0 """ % 'student'

    try:
        cursor.execute(sql)

        data = [row[0] for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e

        ret = False

    return ret


def updateFormFoursToAlumnus(formFours):
    cursor = db.cursor()

    user_ids = ""

    no_of_ids = len(formFours) - 1
    for key, val in enumerate(formFours):
        if key == no_of_ids:  # To avoid adding a comma after the last id
            user_ids = user_ids + str(val)
        else:
            user_ids = user_ids + str(val) + ', '

    sql = """UPDATE users SET alumnus = 1 WHERE user_id IN (%s) AND deleted = 0""" % user_ids

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()

        ret = False

    return ret


def getAllClassesInForm(form):
    cursor = db.cursor()

    sql = """SELECT class_id, class_name, form_name 
                FROM classes 
                WHERE deleted = 0 AND form_name = %d""" % form

    try:
        cursor.execute(sql)

        data = [{
            'class_id': row[0],
            'class_name': row[1],
            'form_name': row[2]} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getClassIDNextForm(clas):
    next_form = clas['form_name'] + 1
    curr_class = clas['class_name']
    cursor = db.cursor()

    sql = "SELECT class_id FROM classes \
           WHERE class_name = '%s' AND form_name = %d" % (curr_class, next_form)

    try:
        cursor.execute(sql)

        if cursor.rowcount:
            data = [row[0] for row in cursor.fetchall()]

            ret = data[0]
        else:
            ret = False

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def updateStudentsToNextClass(current_id, next_id):
    cursor = db.cursor()

    sql = """UPDATE users SET class_id = %s WHERE class_id = %s AND alumnus = 0 AND deleted = 0 AND role = 'student'""" % (next_id, current_id)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret
