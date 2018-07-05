import MySQLdb
from connect import db


def saveSubject(data):
    data["deleted"] = "0"

    cursor = db.cursor()

    sql = """
            INSERT INTO `subjects`(`subject_id`, `subject_name`, `subject_alias`, `compulsory`, `deleted`)
            VALUES (%s, %s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (0, data["subject_name"], data["subject_alias"], data["compulsory"], data["deleted"]))
        db.commit()

        # Add subject as column to exam_results table
        data["subject_alias"] = data["subject_alias"].lower()

        sql = "ALTER TABLE exam_results ADD COLUMN %s DOUBLE" % data["subject_alias"]

        try:
            cursor.execute(sql)
            db.commit()

            ret = True

        except(MySQLdb.Error, MySQLdb.Warning) as e:
            print e
            db.rollback()
    except(MySQLdb.Error, MySQLdb.Warning) as e:

        db.rollback()

        ret = False

    db.close()

    return ret


def editSubject(data):
    cursor = db.cursor()

    sql = """ UPDATE subjects SET
                    subject_name = %s,
                    subject_alias = %s,
                    compulsory = %s
                    WHERE subject_id = %s """

    data = (data["subject_name"], data["subject_alias"], data["compulsory"], data["subject_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()
        ret = False

    return ret


def deleteSubject(id):
    cursor = db.cursor()

    sql = """ UPDATE subjects SET deleted = %s WHERE subject_id = %s """

    data = (1, id)

    try:
        cursor.execute(sql, data)
        db.commit()
        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret