import MySQLdb
from connect import db


def getAllExams(search=""):
    cursor = db.cursor()

    if search == "":
        sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                    WHERE deleted = 0 ORDER BY year DESC"""
    else:
        sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                        WHERE deleted = 0 AND (exam_name LIKE %s OR form LIKE %s) ORDER BY year DESCgetPreviousExam"""
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


def getExamsInForm(form, year, curr_exam_id):

    cursor = db.cursor()

    condition = ""

    # To generate query like "...AND ((form = 4 AND year = 2018) OR (form = 3 AND year = 2017) OR ...)
    if form == "1":
        condition = condition + " form = 1 AND year = " + year

    if form == "2":
        form1yr = str(int(year) - 1)
        condition = condition + " ((form = 2 AND year = " + year + ") OR (form = 1 AND year = " + form1yr + "))"

    if form == "3":
        form2yr = str(int(year) - 1)
        form1yr = str(int(year) - 2)
        condition = condition + " ((form = 3 AND year = " + year + ") OR (form = 2 AND year = " + form2yr + ") OR (form = 1 AND year = " + form1yr + "))"

    # sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
    #             WHERE deleted = 0 AND %s ORDER BY year DESC""" % (form)

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                WHERE deleted = 0 AND %s AND exam_id NOT IN (%s) ORDER BY year DESC""" % (condition, curr_exam_id)

    try:
        cursor.execute(sql)

        ids = []
        full_names = []
        exam_name = []
        forms = []
        term = []
        year = []

        for row in cursor:
            ids.append(row[0])
            full_names.append(" Term " + row[3] + " " + row[1] + ", " + str(row[4]))
            exam_name.append(row[1])
            forms.append(row[2])
            term.append(row[3])
            year.append(row[4])

        data = {
            "ids": ids,
            "full_names": full_names,
            "exam_names": exam_name,
            "forms": forms,
            "terms": term,
            "years": year,
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret


def getExamsInFormAndYear(form, year):

    cursor = db.cursor()

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted` FROM `exams`
                WHERE deleted = 0 AND form = '%s' AND year = %s ORDER BY year DESC""" % (form, year)

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

    cursor = db.cursor()

    condition = ""

    # To generate query like "...AND ((form = 4 AND year = 2018) OR (form = 3 AND year = 2017) OR ...)
    if data['form'] == "1":
        condition = condition + " form = 1 AND year = " + data['year']

    if data['form'] == "2":
        form1yr = str(int(data['year']) - 1)
        condition = condition + " ((form = 2 AND year = " + data['year'] + ") OR (form = 1 AND year = " + form1yr + "))"

    if data['form'] == "3":
        form2yr = str(int(data['year']) - 1)
        form1yr = str(int(data['year']) - 2)
        condition = condition + " ((form = 3 AND year = " + data['year'] + ") " \
                                            "OR (form = 2 AND year = " + form2yr + ") " \
                                            "OR (form = 1 AND year = " + form1yr + "))"
    if data['form'] == "4":
        form3yr = str(int(data['year']) - 1)
        form2yr = str(int(data['year']) - 2)
        form1yr = str(int(data['year']) - 3)
        condition = condition + " ((form = 4 AND year = " + data['year'] + ") " \
                                        "OR (form = 3 AND year = " + form3yr + ") " \
                                        "OR (form = 2 AND year = " + form2yr + ") " \
                                        "OR (form = 1 AND year = " + form1yr + "))"

    # sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`
    #             FROM `exams`
    #             WHERE deleted = 0
    #             AND exam_id < %s
    #             AND form = '%s'
    #             ORDER BY exam_id DESC """ % (data['exam_id'], data['form'])

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year`  
                    FROM `exams` 
                    WHERE deleted = 0 
                    AND exam_id < %s
                    AND %s 
                    ORDER BY exam_id DESC """ % (data['exam_id'], condition)

    try:
        cursor.execute(sql)

        if cursor.rowcount < 1:
            ret = False
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