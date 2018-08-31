import MySQLdb
from connect import db
from datetime import datetime


def saveExam(data):
    forms = []
    if data['form'] == "0": # Representing the "All" Option
        forms = ['1', '2', '3', '4']
    else:
        forms = [data['form']]

    all_saved = True

    for exam in forms:
        data['form'] = exam
        if not saveOneExam(data):
            all_saved = False

    return all_saved


def saveOneExam(data):
    c = datetime.now()
    data["created_at"] = c.strftime('%Y-%m-%d')

    cursor = db.cursor()

    sql = """
            INSERT INTO `exams`(`exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted`)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (0, data["exam_name"], data["form"], data["term"], data["year"], data["created_at"], 0))
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    # db.close()

    return ret


def editExam(data):
    cursor = db.cursor()

    sql = """ UPDATE exams SET
                    exam_name = %s,
                    form = %s,
                    term = %s,
                    year = %s
                    WHERE exam_id = %s """

    data = (data["exam_name"], data["form"], data["term"], data["year"], data["exam_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret


def deleteExam(id):
    cursor = db.cursor()

    sql = """ UPDATE exams SET deleted = %s WHERE exam_id = %s """

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
