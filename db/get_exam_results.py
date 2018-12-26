import MySQLdb
from connect import db

from login import getSchoolDetails
from get_classes import getNoOfStudentsInClass, getNoOfStudentsInForm
# from get_students import getNumberOfStudentsTakingSubject

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

    exam_data = data.copy()
    cursor = db.cursor()

    # placeholder = '%s'
    # param_subs = ', '.join((placeholder,) * len(columns))

    columnStr = ''
    for x in columns:
        columnStr = columnStr + x + ', '

    if len(columns) == 0:
        # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
        if data["class_id"] == 0 and data["exam_id"] > 0:
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, u.deleted   \
                                       FROM exam_results er \
                                       JOIN exams e ON e.exam_id = er.exam_id \
                                       JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                       JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                       WHERE e.exam_id = %d" % (0, int(data['form']), 0, data['exam_id'])
        else:
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, u.deleted   \
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
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, reg_no, points, mean, %s  \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC, first_name" % (columnStr, 0, int(data['form']), 0, data['exam_id'], columnStr)
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, reg_no, points, mean, %s  \
                            FROM exam_results er \
                            JOIN exams e ON e.exam_id = er.exam_id \
                            JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                            JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                            WHERE e.exam_id = %d ORDER BY %s DESC, first_name" % (columnStr, 0, data['class_id'], 0, data['exam_id'], columnStr)
        else:  # Results for all subjects
            # to create dynamic sum of all subjects eg IFNULL(Eng, 0)+IFNULL(Kis, 0)+IFNULL(Mat, 0)+...
            # sum_cols = ''
            #
            # indexes = len(columns) - 1
            # for key, val in enumerate(columns):
            #     if key == indexes:  # To avoid adding + after the last subject
            #         sum_cols = sum_cols + 'IFNULL(' + val + ', 0)'
            #     else:
            #         sum_cols = sum_cols + 'IFNULL(' + val + ', 0)' + '+'

            # To get all classes ie if class_id =0, exam_id > 0 ie exam has been selected
            if data["class_id"] == 0 and data["exam_id"] > 0:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, reg_no, points, mean, %s u.deleted   \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY total DESC, first_name" % (columnStr, 0, int(data['form']), 0, data['exam_id'])
            else:
                sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.surname, u.class_id, c.class_name, c.form_name, reg_no, points, mean, %s u.deleted  \
                                FROM exam_results er \
                                JOIN exams e ON e.exam_id = er.exam_id \
                                JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                                JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                                WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY total DESC, first_name" % (columnStr, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        dataArray = []

        count = 0

        for row in cursor:
            count = count + 1

            data = {
                'number': count,
                'exam_result_id': row[0],
                'exam_id': row[1],
                'exam_name': row[2],
                'term': row[3],
                'student_id': row[4],
                'names': row[5] + " " + row[6] + " " + row[7],
                'class_id': row[8],
                'class_name': row[9],
                'form': ('F '+str(row[10])) if 'Form' in row[9] else (str(row[10]) + str(row[9])[0]),
                'reg_no': row[11],
                'points': row[12],
                'student_mean': str(row[13]) + " " + getMeanGrade(row[13]),
            }

            all_marks = []
            for i, val in enumerate(columns):  # adding columns dynamically
                # the 13 + i + 1 because the previous item in row before subjects start is 13, + 1 bcoz index starts at 0
                # data[columns[i]] = getGradePlusMark(row[13 + i + 1])
                if int(exam_data['form']) < 3:
                    # data[columns[i]] = str(row[13 + i + 1]) + " " + getGradeForm1n2(row[13 + i + 1])
                    data[columns[i]] = "" if row[13 + i + 1] is None else str(row[13 + i + 1]) + " " + getGradeForm1n2(row[13 + i + 1])
                else:
                    data[columns[i]] = "" if row[13 + i + 1] is None else str(row[13 + i + 1]) + " " + getGradeForm3n4(row[13 + i + 1])

                # all_marks.append(row[13+i+1] if row[13+i+1] is not None else 0)

            # data['student_mean'] = getGradePlusMark(getStudentMean(all_marks, data['form']))

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getResultsByStudentAndExamID(exam_data, columns, subject_names, subject_ids, compulsory):
    schDets = getSchoolDetails()
    lower_subjects = schDets['lower_subjects']

    data = exam_data.copy()

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

    sql = """SELECT `exam_result_id`, `student_id`, er.exam_id, form, form_pos, class_pos, total, points, mean, %s
                FROM exam_results er
                JOIN exams e ON e.exam_id = er.exam_id
                WHERE er.exam_id = %s AND student_id = %s""" % (columnStr, data['exam_id'], data['student_id'])

    try:
        cursor.execute(sql)

        # Sample data to prevent error on first load
        oneSubjectResult = {
            'subject': "No data available",
            'mean': "",
            'grade': "",
            'rank': ""
        }
        resultData = {
            'exam_result_id': 0,
            'student_id': 0,
            'exam_id': 0,
            'form': 0,
            'form_pos': 0,
            'class_pos': 0,
            'total': 0,
            'points': 0,
            'mean': 0,
            'mean_grade': 0,
            'subjectData': [oneSubjectResult],
            'students_in_class': 0,
            'students_in_form': 0,
        }

        dataArray = []

        for row in cursor:
            resultData = {
                'exam_result_id': row[0],
                'student_id': row[1],
                'exam_id': row[2],
                'form': row[3],
                'form_pos': row[4],
                'class_pos': row[5],
                'total': row[6],
                'points': row[7],
                'mean': row[8],
                'students_in_class': getNoOfStudentsInClass(data['class_id']),
                'students_in_form': getNoOfStudentsInForm(data['form']),
            }

            if int(data['form']) < 3:
                # resultData['mean_grade'] = getGradeForm1n2(resultData['points'])
                resultData['mean_grade'] = getMeanGrade(resultData['mean'])
            else:
                # resultData['mean_grade'] = getGradeForm3n4(resultData['points']/7)
                resultData['mean_grade'] = getMeanGrade(resultData['mean'])

            for key, val in enumerate(columns):
                subjectData = {
                    'subject': subject_names[key],
                    'mean': "" if row[8 + 1 + key] is None else row[8 + 1 + key],
                }
                if int(data['form']) < 3:
                    subjectData['grade'] = getGradeForm1n2(row[8 + 1 + key])
                else:
                    subjectData['grade'] = getGradeForm3n4(row[8 + 1 + key])

                if row[8 + 1 + key] is not None:
                    # Get position in form
                    # set class_id value to 0 in order to get position in form
                    data['class_id'] = 0
                    class_results = getExamResults(data, [val])
                    for result in class_results:
                        if result['student_id'] == data['student_id']:
                            subjectData['rank'] = result['number']

                else:
                    subjectData['rank'] = ""

                dataArray.append(subjectData)

            resultData['subjectData'] = dataArray

        ret = resultData

    except(MySQLdb.Error, MySQLdb.Warning) as e:

        ret = False

    return ret


def getStudentTrendInExams(student_id):
    cursor = db.cursor()

    sql = """SELECT form, term, year, AVG(points) 
                FROM exam_results er 
                JOIN exams e ON e.exam_id = er.exam_id 
                WHERE student_id = %s
                GROUP BY CONCAT(term, '_', year)""" % student_id

    try:
        cursor.execute(sql)

        dataArray = []

        for row in cursor:
            term = ""
            if row[1] == "One":
                term = "1"
            elif row[1] == "Two":
                term = "2"
            elif row[1] == "Three":
                term = "3"

            period = 'Form ' + str(row[0]) + " Term " + term

            data = {
                'label': period,
                'points': str(row[3])
            }

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getAllResultsForExam(data, columns):
    exam_data = data.copy()
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
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, points, mean, %s u.deleted, SUM(%s) AS sum   \
                        FROM exam_results er \
                        JOIN exams e ON e.exam_id = er.exam_id \
                        JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                        JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                        WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY sum DESC" % (columnStr, sum_cols, 0, int(data['form']), 0, data['exam_id'])
        else:
            sql = "SELECT `exam_result_id`, er.exam_id, e.exam_name, e.term, `student_id`, u.first_name, u.last_name, u.class_id, c.class_name, c.form_name, points, mean, %s u.deleted, SUM(%s) AS sum  \
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
            data['points'] = row[10]
            data['student_mean'] = str(row[11]) + " " + getMeanGrade(row[11])

            all_marks = []
            for i, val in enumerate(columns):  # adding columns dynamically
                # the 11 + i + 1 because the previous item in row before subjects start is 11, + 1 bcoz index starts at 0
                #     data[columns[i]] = getGradePlusMark(row[11 + i + 1])
                #
                #     all_marks.append(row[9+i+1] if row[11+i+1] is not None else 0)
                #
                # data['student_mean'] = getGradePlusMark(getStudentMean(all_marks))

                if int(exam_data['form']) < 3:
                    data[columns[i]] = str(row[13 + i + 1]) + " " + getGradeForm1n2(row[13 + i + 1])
                else:
                    data[columns[i]] = str(row[13 + i + 1]) + " " + getGradeForm3n4(row[13 + i + 1])

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
