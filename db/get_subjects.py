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

        dataArray = []
        for row in cursor.fetchall():
            if row[3] == 0:
                compulsory = "No"
            if row[3] == 1:
                compulsory = "Yes"
            if row[3] == 2:
                compulsory = "Partially"

            data = {
                'subject_id': row[0],
                'subject_name': row[1],
                'subject_alias': row[2],
                'compulsory': compulsory
            }

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getActiveSubjectAliases():  # To be used in query for exam results
    cursor = db.cursor()

    sql = """SELECT `subject_alias`, `subject_name`, `subject_id`
                FROM `subjects` 
                WHERE deleted = 0"""

    try:
        cursor.execute(sql)

        data = [item[0].lower() for item in cursor.fetchall()]

        aliases = []
        names = []
        ids = []

        for row in cursor:
            aliases.append(row[0].lower().capitalize())
            names.append(row[1])
            ids.append(row[2])

        data = {
            "aliases": aliases,
            "names": names,
            "ids": ids
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getOptionalSubjects():  # used in query for subject selection
    cursor = db.cursor()

    sql = """SELECT `subject_alias`, `subject_name`, `subject_id`
                FROM `subjects` 
                WHERE compulsory NOT IN (1)
                AND deleted = 0 """

    try:
        cursor.execute(sql)

        data = [item[0].lower() for item in cursor.fetchall()]

        aliases = []
        names = []
        ids = []

        for row in cursor:
            aliases.append(row[0].lower().capitalize())
            names.append(row[1])
            ids.append(row[2])

        data = {
            "aliases": aliases,
            "names": names,
            "ids": ids
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getSubjectsByTeacher(user_id):
    cursor = db.cursor()

    sql = """SELECT u.user_id, s1.subject_id AS subject_id1, s1.subject_name AS subject_name1, s1.subject_alias AS subject_alias1, 
                    s2.subject_id AS subject_id2, s2.subject_name As subject_name2, s2.subject_alias AS subject_alias2
                FROM users u 
                    JOIN subjects s1 ON s1.subject_id = u.subject1 AND s1.deleted = 0
                    LEFT JOIN subjects s2 ON s2.subject_id = u.subject2 AND s2.deleted = 0
                WHERE u.user_id = '%s'""" % user_id

    try:
        cursor.execute(sql)

        data = {}

        for row in cursor:
            data['user_id'] = row[0]
            data['subject_id1'] = row[1]
            data['subject_name1'] = row[2]
            data['subject_alias1'] = row[3]
            data['subject_id2'] = row[4]
            data['subject_name2'] = row[5]
            data['subject_alias2'] = row[6]

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


def getSubjectByID(id):
    cursor = db.cursor()

    sql = """SELECT `subject_id`, `subject_name`, `subject_alias`, `compulsory`, `deleted` 
                            FROM `subjects` 
                            WHERE deleted = 0 AND subject_id = %s""" % id
    try:
        cursor.execute(sql)

        data = [{
            'subject_id': row[0],
            'subject_name': row[1],
            'subject_alias': row[2],
            'compulsory': "Yes" if row[3] == 1 else "No"
        } for row in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret