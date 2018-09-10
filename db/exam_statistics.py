import MySQLdb
from connect import db

from login import getSchoolDetails


def getGradePlusMark(mark):
    grade = ""
    if mark is not None:
        # mark = int(mark)
        if mark >= 75:
            grade = str(mark) + " A"
        elif 70 <= mark < 75:
            grade = str(mark) + " A-"
        elif 65 <= mark < 70:
            grade = str(mark) + " B+"
        elif 60 <= mark < 65:
            grade = str(mark) + " B"
        elif 55 <= mark < 60:
            grade = str(mark) + " B-"
        elif 50 <= mark < 55:
            grade = str(mark) + " C+"
        elif 45 <= mark < 50:
            grade = str(mark) + " C"
        elif 40 <= mark < 45:
            grade = str(mark) + " C-"
        elif 35 <= mark < 40:
            grade = str(mark) + " D+"
        elif 30 <= mark < 35:
            grade = str(mark) + " D"
        elif 25 <= mark < 30:
            grade = str(mark) + " D-"
        elif mark < 25:
            grade = str(mark) + " E"

    return grade


def getGrade(mark):
    grade = ""
    if mark is not None:
        # mark = int(mark)
        if mark >= 75:
            grade = "A"
        elif 70 <= mark < 75:
            grade = "A-"
        elif 65 <= mark < 70:
            grade = "B+"
        elif 60 <= mark < 65:
            grade = "B"
        elif 55 <= mark < 60:
            grade = "B-"
        elif 50 <= mark < 55:
            grade = "C+"
        elif 45 <= mark < 50:
            grade = "C"
        elif 40 <= mark < 45:
            grade = "C-"
        elif 35 <= mark < 40:
            grade = "D+"
        elif 30 <= mark < 35:
            grade = "D"
        elif 25 <= mark < 30:
            grade = "D-"
        elif mark < 25:
            grade = "E"

    return grade


def getStudentMean(marks_array, form):
    schDets = getSchoolDetails()

    subjects_lower_forms = schDets['lower_subjects']

    if form == 1 or 2:
        no_of_subjects = subjects_lower_forms
    else:
        no_of_subjects = 8

    avg = sum(marks_array) / no_of_subjects
    return round(avg, 2)


def calculateMean(marks_array):
    avg = ""
    if len(marks_array) > 0:
        avg = sum(marks_array) / len(marks_array)
        avg = round(avg, 3)

    return avg


def calculateDeviation(prev, curr):

    if prev is not None and curr is not None and prev != "" and curr != "":
        dev = float(curr) - float(prev)

        if dev == curr:
            dev = "--"

        return dev
    else:
        return "--"


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
        print e
        ret = False
        db.rollback()

    return ret


def getClassMean(data, columns):
    schDets = getSchoolDetails()

    subjects_lower_forms = schDets['lower_subjects']

    if data['form'] == 1 or 2:
        no_of_subjects = subjects_lower_forms
    else:
        no_of_subjects = 8

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
        sql = "SELECT SUM(%s)/%s AS mean \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.form_name = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (no_of_subjects, sum_cols, 0, int(data['form']), 0, data['exam_id'])
    else:
        sql = "SELECT SUM(%s)/%s AS mean  \
                    FROM exam_results er \
                    JOIN exams e ON e.exam_id = er.exam_id \
                    JOIN users u ON u.user_id = er.student_id AND u.deleted = %d \
                    JOIN classes c ON c.class_id = u.class_id AND c.class_id = %d AND u.deleted = %d \
                    WHERE e.exam_id = %d GROUP BY er.exam_result_id ORDER BY mean DESC" % (no_of_subjects, sum_cols, 0, int(data['class_id']), 0, data['exam_id'])

    try:
        cursor.execute(sql)

        data = [item[0] for item in cursor.fetchall()]

        mean = calculateMean(data)
        # mean = getGrade(mean)

        ret = mean

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False
        db.rollback()

    return ret


def allSubjectsMean(data, subjects, prev_data):
    resultsArray = []

    exam_data = data.copy()
    prev_exam_data = prev_data.copy()

    if exam_data['term'] == "One":
        exam_data['term'] = "1"
    elif exam_data['term'] == "Two":
        exam_data['term'] = "2"
    if exam_data['term'] == "Three":
        exam_data['term'] = "3"

    if prev_exam_data['term'] == "One":
        prev_exam_data['term'] = "1"
    elif prev_exam_data['term'] == "Two":
        prev_exam_data['term'] = "2"
    if prev_exam_data['term'] == "Three":
        prev_exam_data['term'] = "3"

    subject_mean = {
        'subject': "T" + exam_data['term'] + " " + exam_data['exam_name'] + ", " + str(exam_data['year']) + " "
    }
    prev_subject_mean = {
        'subject': "T" + prev_exam_data['term'] + " " + prev_exam_data['exam_name'] + ", " + str(prev_exam_data['year']) + " "
    }

    deviation = {
        'subject': 'Deviation'
    }

    for key, val in enumerate(subjects):  # Get mean of every subject one by one
        exam_data['subject_alias'] = val
        prev_exam_data['subject_alias'] = val

        curr_mean = getSubjectMean(exam_data)
        prev_mean = getSubjectMean(prev_exam_data)

        subject_mean[val] = getGradePlusMark(curr_mean)
        prev_subject_mean[val] = getGradePlusMark(prev_mean)
        deviation[val] = calculateDeviation(prev_mean, curr_mean)

    overall_mean_curr = getClassMean(data, subjects)
    overall_mean_prev = getClassMean(prev_data, subjects)

    subject_mean['mean_grade'] = getGradePlusMark(overall_mean_curr)
    prev_subject_mean['mean_grade'] = getGradePlusMark(overall_mean_prev)
    deviation['mean_grade'] = calculateDeviation(overall_mean_prev, overall_mean_curr)

    resultsArray.append(subject_mean)
    resultsArray.append(prev_subject_mean)
    resultsArray.append(deviation)

    return resultsArray
