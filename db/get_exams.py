import MySQLdb
from connect import db

def getAllExams(search=""):
    cursor = db.cursor()

    if search == "":
        sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                    WHERE deleted = 0"""
    else:
        sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                        WHERE deleted = 0 AND (exam_name LIKE %s OR form LIKE %s)"""
    try:
        if search == "":
            cursor.execute(sql)
        else:
            cursor.execute(sql, ('%' + search + '%', '%' + search + '%',))

        data = [{
            'exam_id': row[0],
            'exam_name': row[1],
            'form': row[2],
            'term': row[3],
            'year': row[4],
            'created_at': row[5]} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = e
        # ret = False

    return ret