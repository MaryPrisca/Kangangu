import MySQLdb
from connect import db


def getSubjects(search=""):
    cursor = db.cursor()

    if search == "":
        sql = """SELECT `subject_id`, `subject_name`, `subject_alias`, `compulsory`, `deleted` 
                    FROM `subjects` 
                    WHERE deleted = 0"""
    else:
        sql = """SELECT `subject_id`, `subject_name`, `subject_alias`, `compulsory`, `deleted` 
                    FROM `subjects` 
                    WHERE deleted = 0 AND (subject_name LIKE %s OR subject_alias LIKE %s)"""

    try:
        if search == "":
            cursor.execute(sql)
        else:
            cursor.execute(sql, ('%' + search + '%', '%' + search + '%',))

        data = [{
            'subject_id': row[0],
            'subject_name': row[1],
            'subject_alias': row[2],
            'compulsory': "Yes" if row[3] == 1 else "No"
            } for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getActiveSubjectAliases():  # To be used in query for exam results
    cursor = db.cursor()

    sql = """SELECT `subject_alias` 
                FROM `subjects` 
                WHERE deleted = 0"""

    try:
        cursor.execute(sql)

        data = [item[0].lower() for item in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def checkIfSubjectExists(col):
    cursor = db.cursor()

    sql = "SELECT COLUMN_NAME \
        FROM information_schema.COLUMNS \
        WHERE \
            TABLE_SCHEMA = 'kangangu' \
        AND TABLE_NAME = 'exam_results' \
        AND COLUMN_NAME = '%s'" % col

    try:
        cursor.execute(sql)

        ret = cursor.rowcount

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret