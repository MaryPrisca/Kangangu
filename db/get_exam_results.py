import MySQLdb
from connect import db


def getPresentYears():
    cursor = db.cursor()

    sql = "SELECT DISTINCT year FROM exams \
               WHERE deleted = '%d'" % 0
    try:
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getExamsinTerm(term, year):

    cursor = db.cursor()

    sql = "SELECT exam_id, exam_name FROM exams \
            WHERE deleted = '%d' \
            AND year = '%s' \
            AND term = '%s'" % (0, year, term)
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


def getExamResults(data, columns):
    cursor = db.cursor()

    # placeholder = '%s'
    # param_subs = ', '.join((placeholder,) * len(columns))

    columnStr = ''
    for x in columns:
        columnStr = columnStr + x + ', '

    # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
    if data["class_id"] == 0 and data["exam_id"] > 0:
        sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s u.deleted   \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d" % (columnStr, 0, int(data['form']), 0, data['exam_id'])
    else:
        sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s u.deleted   \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d" % (columnStr, 0, data['class_id'], 0, data['exam_id'])

    try:
        cursor.execute(sql)

        dataArray = []

        for row in cursor:
            data = {}

            data['exam_result_id'] = row[0]
            data['exam_id'] = row[1]
            data['exam_name'] = row[2]
            data['term'] = row[3]
            data['student_id'] = row[4]
            data['names'] = row[5] + " " + row[6],
            data['class_id'] = row[7]
            data['class_name'] = row[8]
            data['form'] = str(row[9]) + str(row[8])[0]

            for i, val in enumerate(columns):  # adding columns dynamically
                # the 9 + i + 1 because the previous item in row before subjects start is 9, + 1 bcoz index starts at 0
                data[columns[i]] = row[9+i+1]

            dataArray.append(data)

        # print(cursor._last_executed)
        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret