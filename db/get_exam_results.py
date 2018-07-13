import MySQLdb
from connect import db

from exam_statistics import *


def getPresentYears():
    cursor = db.cursor()

    sql = "SELECT DISTINCT year FROM exams \
               WHERE deleted = '%d' ORDER BY YEAR" % 0
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

    if len(columns) == 0:
        # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
        if data["class_id"] == 0 and data["exam_id"] > 0:
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, u.deleted   \
                                       FROM exam_results er \
                                       JOIN exams e ON e.exam_id = er.exam_id \
                                       JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                       JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                       WHERE e.exam_id = %d" % (0, int(data['form']), 0, data['exam_id'])
        else:
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, u.deleted   \
                                       FROM exam_results er \
                                       JOIN exams e ON e.exam_id = er.exam_id \
                                       JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                       JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                                       WHERE e.exam_id = %d" % (0, data['class_id'], 0, data['exam_id'])

    else:
        if len(columns) == 1:  # If we're getting results for one subject
            columnStr = ''
            for x in columns:
                columnStr = columnStr + x

            # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
            if data["class_id"] == 0 and data["exam_id"] > 0:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s, u.deleted   \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC" % (columnStr, 0, int(data['form']), 0, data['exam_id'], columnStr)
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s, u.deleted   \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC" % (columnStr, 0, data['class_id'], 0, data['exam_id'], columnStr)
        else:  # Results for all subjects
            # to create dynamic sum of all subjects eg IFNULL(Eng, 0)+IFNULL(Kis, 0)+IFNULL(Mat, 0)+...
            sum_cols = ''

            indexes = len(columns) - 1
            for key, val in enumerate(columns):
                if key == indexes:  # To avoid adding + after the last subject
                    sum_cols = sum_cols + 'IFNULL(' + val + ', 0)'
                else:
                    sum_cols = sum_cols + 'IFNULL(' + val + ', 0)' + '+'

            # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
            if data["class_id"] == 0 and data["exam_id"] > 0:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s u.deleted, SUM(%s) AS sum   \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC" % (columnStr, sum_cols, 0, int(data['form']), 0, data['exam_id'])
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, %s u.deleted, SUM(%s) AS sum  \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC" % (columnStr, sum_cols, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        dataArray = []

        stud_means = []

        count = 0

        for row in cursor:
            count = count + 1

            data = {}

            data['number'] = count
            data['exam_result_id'] = row[0]
            data['exam_id'] = row[1]
            data['exam_name'] = row[2]
            data['term'] = row[3]
            data['student_id'] = row[4]
            data['names'] = row[5] + " " + row[6],
            data['class_id'] = row[7]
            data['class_name'] = row[8]
            data['form'] = str(row[9]) + str(row[8])[0]


            all_marks = []
            for i, val in enumerate(columns):  # adding columns dynamically
                # the 9 + i + 1 because the previous item in row before subjects start is 10, + 1 bcoz index starts at 0
                data[columns[i]] = getGrade(row[9+i+1])

                all_marks.append(row[9+i+1] if row[9+i+1] is not None else 0)

            data['student_mean'] = getStudentMean(all_marks)

            dataArray.append(data)

        # print(cursor._last_executed)
        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getSubjectMean(data):
    cursor = db.cursor()

    # if class_id == 0 means all classes in form, exam_id == 0 to make sure there's data
    if data['class_id'] == 0 and data["exam_id"] > 0:
        sql = """SELECT AVG(%s)
                    FROM exam_results er 
                        JOIN exams e ON e.exam_id = er.exam_id 
                        JOIN users u ON u.user_id = er.student_id AND u.deleted = %d 
                        JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d
                    WHERE e.exam_id = %d """ % (data['subject_alias'], 0, int(data['form']), 0, data['exam_id'])
    else:
        sql = "SELECT AVG(%s) \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d" % (data['subject_alias'], 0, data['class_id'], 0, data['exam_id'])

    try:
        cursor.execute(sql)

        mean = [item[0] for item in cursor.fetchall()]
        mean = mean[0]

        if mean is not None:
            mean = getGrade(round(mean, 3))
        else:
            mean = 0

        ret = mean

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getClassMean(data, columns):
    columnStr = ''
    for x in columns:
        columnStr = columnStr + x + ', '

    cursor = db.cursor()

    # to create dynamic sum of all subjects eg IFNULL(Eng, 0)+IFNULL(Kis, 0)+IFNULL(Mat, 0)+...
    sum_cols = ''

    indexes = len(columns) - 1
    for key, val in enumerate(columns):
        if key == indexes:  # To avoid adding + after the last subject
            sum_cols = sum_cols + 'IFNULL(' + val + ', 0)'
        else:
            sum_cols = sum_cols + 'IFNULL(' + val + ', 0)' + '+'

    # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
    if data["class_id"] == 0 and data["exam_id"] > 0:
        sql = "SELECT SUM(%s)/5 AS mean \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (sum_cols, 0, int(data['form']), 0, data['exam_id'])
    else:
        sql = "SELECT SUM(%s)/5 AS mean  \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (sum_cols, 0, int(data['class_id']), 0, data['exam_id'])
    # print sql
    try:
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        mean = calculateMean(data)

        ret = mean

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret