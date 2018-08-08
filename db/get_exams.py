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
        # ret = e
        ret = False

    return ret


def getExamsInForm(form):
    if form == "1":
        form = "One"
    elif form == "2":
        form = "Two"
    elif form == "3":
        form = "Three"
    elif form == "4":
        form = "Four"
    else:
        form = ""

    cursor = db.cursor()

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                WHERE deleted = 0 AND (form = '%s' OR form = '%s') ORDER BY year DESC""" % (form, "All")

    try:
        cursor.execute(sql)

        ids = []
        full_names = []
        exam_name = []
        term = []
        year = []

        for row in cursor:
            ids.append(row[0])
            full_names.append(" Term " + row[3] + " " + row[1] + ", " + str(row[4]))
            exam_name.append(row[1])
            term.append(row[3])
            year.append(row[4])

        data = {
            "ids": ids,
            "full_names": full_names,
            "exam_names": exam_name,
            "terms": term,
            "years": year,
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret


def getExamsInFormAndYear(form, year):
    if form == "1" or form == 1:
        form = "One"
    elif form == "2" or form == 2:
        form = "Two"
    elif form == "3" or form == 3:
        form = "Three"
    elif form == "4" or form == 4:
        form = "Four"
    else:
        form = ""

    cursor = db.cursor()

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                WHERE deleted = 0 AND (form = '%s' OR form = '%s') AND year = %s ORDER BY year DESC""" % (form, "All", year)

    try:
        cursor.execute(sql)

        ids = []
        full_names = []
        exam_name = []
        term = []
        year = []

        for row in cursor:
            if row[3] == "One":
                term_no = "1"
            elif row[3] == "Two":
                term_no = "2"
            elif row[3] == "Three":
                term_no = "3"

            ids.append(row[0])
            full_names.append("Term " + term_no + " " + row[1] + ", " + str(row[4]))
            exam_name.append(row[1])
            term.append(row[3])
            year.append(row[4])

        data = {
            "ids": ids,
            "full_names": full_names,
            "exam_names": exam_name,
            "terms": term,
            "years": year,
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret


def getPreviousExam(data):  # Most previous similar exam. Ie same form. To get deviation.

    if data['form'] == "1":
        form = "One"
    elif data['form'] == "2":
        form = "Two"
    elif data['form'] == "3":
        form = "Three"
    elif data['form'] == "4":
        form = "Four"
    else:
        form = "0"

    cursor = db.cursor()

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`  
                FROM `exams` 
                WHERE deleted = 0 
                AND (form = '%s' OR form = "All") 
                AND exam_id < %s
                ORDER BY exam_id DESC """ % (form, data['exam_id'])

    try:
        cursor.execute(sql)

        if cursor.rowcount < 1:
            ret = 0
        else:
            data = [{
                'exam_id': row[0],
                'exam_name': row[1],
                'form': row[2],
                'term': row[3],
                'year': row[4]} for row in cursor.fetchall()]

            ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret


def getFormsInExam(id):  # Get the forms that did exam
    cursor = db.cursor()

    sql = """SELECT `form` FROM `exams` WHERE deleted = 0 AND exam_id = %s""" % id

    try:
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        ret = data[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # ret = e
        ret = False

    return ret