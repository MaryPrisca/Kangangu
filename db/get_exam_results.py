import MySQLdb
from connect import db

from login import getSchoolDetails

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

    sql = "SELECT exam_id, exam_name, form FROM exams \
            WHERE deleted = '%d' \
            AND year = '%s' \
            AND term = '%s'" % (0, year, term)
    try:
        cursor.execute(sql)

        ids = []
        names = []
        forms = []
        names_n_form = []

        for row in cursor:
            ids.append(row[0])
            names.append(row[1])
            forms.append(row[2])
            names_n_form.append("Form " + row[2] + " " + row[1])

        data = {
            "ids": ids,
            "names": names,
            "forms": forms,
            "names_n_form": names_n_form
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getExamResults(data, columns):
    if data['form'] == "":
        data['form'] = 0
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
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, reg_no, %s, u.deleted   \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC, first_name" % (columnStr, 0, int(data['form']), 0, data['exam_id'], columnStr)
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, reg_no, %s, u.deleted   \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC, first_name" % (columnStr, 0, data['class_id'], 0, data['exam_id'], columnStr)
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
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, reg_no, %s u.deleted, SUM(%s) AS sum   \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC, first_name" % (columnStr, sum_cols, 0, int(data['form']), 0, data['exam_id'])
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, reg_no, %s u.deleted, SUM(%s) AS sum  \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC, first_name" % (columnStr, sum_cols, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        dataArray = []

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
            data['reg_no'] = row[10]

            all_marks = []
            for i, val in enumerate(columns):  # adding columns dynamically
                # the 10 + i + 1 because the previous item in row before subjects start is 10, + 1 bcoz index starts at 0
                data[columns[i]] = getGradePlusMark(row[10 + i + 1])

                all_marks.append(row[10+i+1] if row[10+i+1] is not None else 0)

            data['student_mean'] = getGradePlusMark(getStudentMean(all_marks, data['form']))

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getResultsByStudentAndExamID(data, columns, subject_names):

    cursor = db.cursor()

    columnStr = ''
    # for x in columns:
    #     columnStr = columnStr + x + ', '

    indexes = len(columns) - 1
    for key, val in enumerate(columns):
        if key == indexes:  # To avoid adding , after the last subject
            columnStr = columnStr + val
        else:
            columnStr = columnStr + val + ', '

    sql = """SELECT `exam_result_id`, `student_id`, %s, `exam_id` 
                FROM `exam_results` 
                WHERE exam_id = %s AND student_id = %s""" % (columnStr, data['exam_id'], data['student_id'])

    try:
        cursor.execute(sql)

        dataArray = []

        for row in cursor:
            for key, val in enumerate(columns):
                resultData = {
                    'subject': subject_names[key],
                    'mean': "" if row[1 + 1 + key] is None else row[1 + 1 + key],
                    'grade': getGrade(row[1 + 1 + key])
                }

                if row[1 + 1 + key] is not None:
                    # Get position in class
                    class_results = getExamResults(data, [val])
                    for result in class_results:
                        if result['student_id'] == data['student_id']:
                            resultData['rank'] = result['number']
                else:
                    resultData['rank'] = ""

                dataArray.append(resultData)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getAllResultsForExam(data, columns):
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
                data[columns[i]] = getGradePlusMark(row[9 + i + 1])

                all_marks.append(row[9+i+1] if row[9+i+1] is not None else 0)

            data['student_mean'] = getGradePlusMark(getStudentMean(all_marks))

            dataArray.append(data)


        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:

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

        if mean is None:
            mean = 0

        ret = round(mean, 3)

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getClassMean(data, columns):
    columnStr = ''
    for x in columns:
        columnStr = columnStr + x + ', '

    schDets = getSchoolDetails()

    subjects_lower_forms = schDets['lower_subjects']

    if data['form'] == 1 or 2:
        no_of_subjects = subjects_lower_forms
    else:
        no_of_subjects = 8

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
        sql = "SELECT SUM(%s)/%s AS mean \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (sum_cols, no_of_subjects, 0, int(data['form']), 0, data['exam_id'])
    else:
        sql = "SELECT SUM(%s)/%s AS mean  \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (sum_cols, no_of_subjects, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        if data[0] is not None:
            mean = calculateMean(data)
            # mean = getGrade(data[0])
        else:
            mean = ""

        ret = mean

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getMarksAndStudentId(data, columns):
    cursor = db.cursor()

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
                sql = "SELECT `exam_result_id`, `student_id`, u.first_name, %s, u.deleted   \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC" % (columnStr, 0, int(data['form']), 0, data['exam_id'], columnStr)
            else:
                sql = "SELECT `exam_result_id`, `student_id`, u.first_name, %s, u.deleted  \
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
                sql = "SELECT `exam_result_id`, `student_id`, u.first_name, %s u.deleted, SUM(%s) AS sum   \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC" % (columnStr, sum_cols, 0, int(data['form']), 0, data['exam_id'])
            else:
                sql = "SELECT `exam_result_id`, `student_id`, u.first_name, %s u.deleted, SUM(%s) AS sum  \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC" % (columnStr, sum_cols, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        dataArray = []

        for row in cursor:
            data = {}

            all_marks = []
            for i, val in enumerate(columns):  # adding columns dynamically
                # the 2 + i + 1 because the previous item in row before subjects start is 2, + 1 bcoz index starts at 0
                # data[columns[i]] = row[2 + i + 1]

                all_marks.append(row[2 + i + 1] if row[2 + i + 1] is not None else 0)

            if len(columns) > 1:
                data[row[1]] = getStudentMean(all_marks, 1)
            else:
                data[row[1]] = all_marks[0]

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getMostImproved(prev_exam_data, curr_exam_data, subjects):
    prev_results = getMarksAndStudentId(prev_exam_data, subjects)
    curr_results = getMarksAndStudentId(curr_exam_data, subjects)

    deviations = {}

    for item in curr_results:
        for (key, value) in item.iteritems():  # Key reps the student_id, value is the mark
            # Check if student Id is in prev_results, if so, get deviation

            # Returns true if dict with given key is found in list
            if any(key in d for d in prev_results):
                # Returns index of dict that contains given key in list of dicts
                prev_mark_index = next(i for i, d in enumerate(prev_results) if key in d)

                # Get full dict by index
                prev_mark_dict = prev_results[prev_mark_index]

                # Get deviation
                dev = calculateDeviation(prev_mark_dict[key], value)

                if dev != "--":
                    dev = round(dev, 2)

                deviations[key] = dev

    if len(deviations):
        student_ids = deviations.keys()
        devs = deviations.values()

        max_dev = max(devs)  # Most improved

        # Get all indexes in which max_dev occure (In case it occurs more than once
        indices = [i for i, x in enumerate(devs) if x == max_dev]

        max_dev_student_ids = []
        for item in indices:
            max_dev_student_ids.append(student_ids[item])

        # Return the student id and the marks they improved by
        ret = {
            'student_id': max_dev_student_ids,
            'mark': max_dev
        }

        # Check if there was an improvement. If max dev is negative then all dropped, will return the least drop
        if max_dev < 0:
            ret['nature'] = "Decline"
        else:
            ret['nature'] = "Improve"

        return ret

    else:
        return False
