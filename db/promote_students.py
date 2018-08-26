import MySQLdb
from connect import db


def promoteStudents():
    formFours = getAllFormFours()

    moveFormFoursToAlumnus(formFours)


def getAllFormFours():
    cursor = db.cursor()

    sql = """SELECT user_id
                FROM `users` u
                JOIN classes c
                    ON c.class_id = u.class_id AND form_name = 4
                WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % 'student'

    try:
        cursor.execute(sql)

        data = [row[0] for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e

        ret = False

    return ret


def moveFormFoursToAlumnus(formFours):
    cursor = db.cursor()

    user_ids = ""

    no_of_ids = len(formFours) - 1
    for key, val in enumerate(formFours):
        if key == no_of_ids:  # To avoid adding a comma after the last id
            user_ids = user_ids + str(val)
        else:
            user_ids = user_ids + str(val) + ', '

    sql = """UPDATE users SET alumnus = 1 WHERE user_id IN (%s)""" % user_ids

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()

        ret = False

    return ret