import MySQLdb
from connect import db

from get_subjects import getActiveSubjectAliases
from get_exams import getFormsInExam
from get_classes import getFormClasses
from login import getSchoolDetails
from get_subjects import getCompulsorySciencesHumanities, getSubjectsInGroup, getSubjectsTakenByStudent


def getStudentList(data):
    cursor = db.cursor()

    columns = [data['subject_alias']]
    columnStr = ''
    for x in columns:
        columnStr = columnStr + x

    # If the subject is compulsory get all students in class, else filter those taking subject
    if data['subject_compulsory']:
        sql = """SELECT user_id, first_name, last_name, surname, %s AS mark, er.exam_result_id
                            FROM `users` u
                            JOIN classes c
                                ON c.class_id = u.class_id AND c.class_id='%s'
                            LEFT JOIN exam_results er ON er.student_id = u.user_id AND er.exam_id = '%s'
                            WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" \
              % (columnStr, data['class_id'], data['exam_id'], 'student')
    else:
        sql = """SELECT user_id, first_name, last_name, surname, %s AS mark, er.exam_result_id
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id AND c.class_id='%s'
                    LEFT JOIN exam_results er ON er.student_id = u.user_id AND er.exam_id = '%s'
                    WHERE FIND_IN_SET(%s, subjects_taken) != 0 AND u.deleted = 0 AND c.deleted = 0 AND role='%s'""" \
          % (columnStr, data['class_id'], data['exam_id'], data['subject_id'], 'student')

    try:
        cursor.execute(sql)

        data = [{
            'user_id': row[0],
            'names': row[1] + " " + row[2] + " " + row[3],
            'mark': "" if row[4] is None else row[4],
            'result_id': "0" if row[5] is None else row[5]
        } for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getExamDetails(data):
    cursor = db.cursor()

    form_name = ""
    if data['form'] == 1:
        form_name = "One"
    elif data['form'] == 2:
        form_name = "Two"
    elif data['form'] == 3:
        form_name = "Three"
    elif data['form'] == 4:
        form_name = "Four"

    sql = """SELECT `exam_id`, `exam_name`, `form`, `term`, `year` 
                FROM `exams` 
                WHERE exam_id='%s'""" % data['exam_id']

    try:
        cursor.execute(sql)

        data = [{
            'exam_id': row[0],
            'exam_name': row[1],
            'form': data['form'],
            'term': row[3],
            'year': row[4],
            'form_name': form_name,
            'subject': data['subject_alias'].upper(),
            'class': data['class']} for row in cursor.fetchall()]

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret


def checkIfMarksAlreadyEntered(data, columns):  # For at least One Student
        cursor = db.cursor()

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

            if cursor.rowcount < 1:
                ret = False

            else:
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
                        data[columns[i]] = row[9 + i + 1]

                    dataArray.append(data)

                # print(cursor._last_executed)
                ret = dataArray

        except(MySQLdb.Error, MySQLdb.Warning) as e:
            # print e
            ret = False

        return ret


def saveMarks(insert_data, update_data, exam_id):
    save_complete = True

    # Store all exam_result_ids of rows that are inserted/updated
    # in order to update the total & pos columns in those repective rows

    exam_result_ids = []

    for (k, v) in insert_data.iteritems():
        inserted_id = saveMarksOneRecord(v['exam_id'], v['subject'], v['student_id'], v['mark'])
        if inserted_id:
            exam_result_ids.append(inserted_id)
        else:
            save_complete = False

    for (k, v) in update_data.iteritems():
        if updateMarksOneRecord(v['exam_result_id'], v['mark'], v['subject']):
            exam_result_ids.append(v['exam_result_id'])
        else:
            save_complete = False

    # calculate & update totals and pos in affected rows
    updateTotalsAndPositionsInExam(exam_result_ids, exam_id)

    return save_complete


def saveMarksOneRecord(exam_id, subject, student_id, mark):
    cursor = db.cursor()

    sql = """INSERT INTO `exam_results`(`exam_result_id`, `exam_id`, `student_id`, %s) 
            VALUES (%s, %s, %s, %s)""" % (subject, 0, exam_id, student_id, mark)

    try:
        cursor.execute(sql)
        db.commit()

        ret = cursor.lastrowid
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print(e)

        db.rollback()

        ret = False

    return ret


def updateMarksOneRecord(exam_result_id, mark, subject):
    cursor = db.cursor()

    sql = """UPDATE `exam_results` SET %s = '%s' WHERE exam_result_id = '%s'""" % (subject, mark, exam_result_id)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print(e)

        db.rollback()

        ret = False

    return ret


def updateTotalsAndPositionsInExam(result_ids, exam_id):
    # get subject columns in the exam_results table, equivalent to active subjects (aliases)
    subjects = getActiveSubjectAliases()
    subjects = subjects['aliases']

    # get form in question
    form = getFormsInExam(exam_id)

    completeRowIDs = []

    # For each exam result row affected...
    for result in result_ids:

        # get total for result
        if int(form) < 3:
            stats = getTotalOneRowLowerForms(result, subjects)
        else:
            stats = getTotalOneRowUpperForms(result, subjects)

        # update total
        updateTotalForOneRowExamResults(result, stats)

        # check if al the columns have values so that the row can be marked ready for upload (totalled = 1)
        if checkIfAllSubjectsAreFilledOneRow(result, subjects, form):
            # all exam_result_ids who's rows have all columns filled
            completeRowIDs.append(result)

    if len(completeRowIDs):
        # Set totalled  = 1 in all those rows
        updateTotalledFieldManyRows(completeRowIDs)

    # get form positions with new totals
    form_pos_data = getFormPositionsInExam(exam_id)

    # loop through array updating the form_pos
    for result in form_pos_data:
        updateFormPosition(result)

    # get class positions
    class_pos_data = getClassPositions(exam_id, form)

    # Update class_pos field
    for result in class_pos_data:
        updateClassPosition(result)


def getPointsF3nF4(mark):
    points = 0
    if mark is not None:
        # mark = int(mark)
        if mark >= 75:
            points = 12
        elif 70 <= mark < 75:
            points = 11
        elif 65 <= mark < 70:
            points = 10
        elif 60 <= mark < 65:
            points = 9
        elif 55 <= mark < 60:
            points = 8
        elif 50 <= mark < 55:
            points = 7
        elif 45 <= mark < 50:
            points = 6
        elif 40 <= mark < 45:
            points = 5
        elif 35 <= mark < 40:
            points = 4
        elif 30 <= mark < 35:
            points = 3
        elif 25 <= mark < 30:
            points = 2
        elif mark < 25:
            points = 1

    return points


def getPointsF1nF2(mark):
    points = 0
    if mark is not None:
        # mark = int(mark)
        if mark >= 80:
            points = 12
        elif 75 <= mark < 80:
            points = 11
        elif 70 <= mark < 75:
            points = 10
        elif 65 <= mark < 70:
            points = 9
        elif 60 <= mark < 65:
            points = 8
        elif 55 <= mark < 60:
            points = 7
        elif 50 <= mark < 55:
            points = 6
        elif 45 <= mark < 50:
            points = 5
        elif 40 <= mark < 45:
            points = 4
        elif 35 <= mark < 40:
            points = 3
        elif 30 <= mark < 35:
            points = 2
        elif mark < 30:
            points = 1

    return points


def getTotalOneRowLowerForms(result_id, subjects):
    cursor = db.cursor()

    # to create dynamic string of all subjects in one row eg Eng, Kis, Mat, Bio.....
    cols = ''

    indexes = len(subjects) - 1  # -1 because first index is 0
    for key, val in enumerate(subjects):
        if key == indexes:  # To avoid adding + after the last subject
            cols = cols + val
        else:
            cols = cols + val + ', '

    sql = """SELECT %s FROM `exam_results` WHERE exam_result_id = %s""" % (cols, result_id)

    try:
        cursor.execute(sql)

        # data = [row[0] for row in cursor.fetchall()]
        # ret = data[0]

        points = 0
        total = 0

        for row in cursor:
            for key, value in enumerate(subjects):
                if row[key] is not None:
                    total += row[key]
                    points += getPointsF1nF2(row[key])

        schDets = getSchoolDetails()
        subjects_lower_forms = schDets['lower_subjects']

        ret = {'total': total, 'points': points, 'mean': round((float(points)/subjects_lower_forms), 1)}

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        ret = False

    return ret


def getTotalOneRowUpperForms(result_id, subjects):
    data = getMarksAndStudentIDOneRow(result_id, subjects)
    marks = data['marks']
    student_id = data['student_id']

    total = 0
    points = 0

    # get compulsory subjects i.e. maths & languages
    # maths
    maths = getSubjectsInGroup('Mathematics')
    math_col_name = maths[0]['alias'].lower()

    total += marks[math_col_name]
    points += getPointsF3nF4(marks[math_col_name])

    # languages
    languages = getSubjectsInGroup('Language')
    for lang in languages:
        lang_col_name = lang['alias'].lower()
        total += marks[lang_col_name]
        points += getPointsF3nF4(marks[lang_col_name])

    #
    # OPTIONAL SUBJECTS
    #

    # get sciences and humanities that are compulsory in the school
    compulsory_subjects = getCompulsorySciencesHumanities()

    # find the sort of choices student has e.g. 3 sciences 1 hum 1 tech / 3 sci 2 hum etc etc
    sciences_aliases = []
    humanities_aliases = []
    technicals_aliases = []

    no_of_sciences = 0
    no_of_humanities = 0
    no_of_technicals = 0

    for key, value in enumerate(compulsory_subjects['group_names']):
        if value == 'Science':
            no_of_sciences += 1
            sciences_aliases.append(compulsory_subjects['aliases'][key])

        elif value == 'Humanity':
            no_of_humanities += 1
            humanities_aliases.append(compulsory_subjects['aliases'][key])

        elif value == 'Applied/Technical':
            no_of_technicals += 1
            technicals_aliases.append(compulsory_subjects['aliases'][key])

    #
    # get subjects the student takes
    subjects_taken = getSubjectsTakenByStudent(student_id)
    if len(subjects_taken):
        for key, value in enumerate(subjects_taken['group_names']):
            if value == 'Science':
                no_of_sciences += 1
                sciences_aliases.append(subjects_taken['aliases'][key])

            elif value == 'Humanity':
                no_of_humanities += 1
                humanities_aliases.append(subjects_taken['aliases'][key])

            elif value == 'Applied/Technical':
                no_of_technicals += 1
                technicals_aliases.append(subjects_taken['aliases'][key])

    # LOGIC OF DROPPING ONE SUBJECT

    # Three possibilities
    #     1. 3 sciences, 1 humanity, 1 technical    # 1 humanity + highest 3
    #     2. 3 sciences, 2 humanities, 0 technical  # get the highest 4
    #     3. 2 sciences, 2 humanities, 1 technical  # 2 sciences + highest 2

    #

    # 3 SCIENCES OPTION
    if no_of_sciences == 3:

        # NB the sciences, humanities and technicals arrays are holding the alias names of the subjects, not marks

        # 3 SCIENCES 1 HUMANITY, 1 TECHNICAL
        if no_of_humanities == 1:  # First possibility
            # Add the humanity
            total += marks[humanities_aliases[0]]
            points += getPointsF3nF4(marks[humanities_aliases[0]])

            # put the other four in an array in order to get the highest 3
            marks_array = [marks[sciences_aliases[0]], marks[sciences_aliases[1]], marks[sciences_aliases[2]], marks[technicals_aliases[0]]]
            points_array = [
                getPointsF3nF4(marks[sciences_aliases[0]]),
                getPointsF3nF4(marks[sciences_aliases[1]]),
                getPointsF3nF4(marks[sciences_aliases[2]]),
                getPointsF3nF4(marks[technicals_aliases[0]])
            ]

            lowest_mark = min(marks_array)
            lowest_point = min(points_array)

            sum_of_top_three_marks = sum(marks_array) - lowest_mark
            sum_of_top_three_points = sum(points_array) - lowest_point

            total += sum_of_top_three_marks
            points += sum_of_top_three_points

        # 3 SCIENCES 2 HUMANITIES NO TECHNICAL
        elif no_of_humanities == 2:  # Second possibility
            # put all the five in an array in order to get the highest 4
            marks_array = [marks[sciences_aliases[0]], marks[sciences_aliases[1]], marks[sciences_aliases[2]], marks[humanities_aliases[0]], marks[humanities_aliases[1]]]
            points_array = [
                getPointsF3nF4(marks[sciences_aliases[0]]),
                getPointsF3nF4(marks[sciences_aliases[1]]),
                getPointsF3nF4(marks[sciences_aliases[2]]),
                getPointsF3nF4(marks[humanities_aliases[0]]),
                getPointsF3nF4(marks[humanities_aliases[1]])
            ]

            lowest_mark = min(marks_array)
            lowest_point = min(points_array)

            sum_of_top_four_marks = sum(marks_array) - lowest_mark
            sum_of_top_four_points = sum(points_array) - lowest_point

            total += sum_of_top_four_marks
            points += sum_of_top_four_points

    # 2 SCIENCES OPTION. 2 HUMANITIES 1 TECHNICAL
    else:  # Third possibility
        # Add the two sciences
        total = total + marks[sciences_aliases[0]] + marks[sciences_aliases[1]]
        points = points + getPointsF3nF4(marks[sciences_aliases[0]]) + getPointsF3nF4(marks[sciences_aliases[1]])

        # put the other three in an array in order to get the highest 2
        marks_array = [marks[humanities_aliases[0]], marks[humanities_aliases[1]], marks[technicals_aliases[0]]]
        points_array = [
            getPointsF3nF4(marks[humanities_aliases[0]]),
            getPointsF3nF4(marks[humanities_aliases[1]]),
            getPointsF3nF4(marks[technicals_aliases[0]])
        ]

        lowest_mark = min(marks_array)
        lowest_points = min(points_array)

        sum_of_top_two_marks = sum(marks_array) - lowest_mark
        sum_of_top_two_points = sum(points_array) - lowest_points

        total += sum_of_top_two_marks
        points += sum_of_top_two_points

    return {'total': total, 'points': points, 'mean': round((float(points)/7), 1)}


def getMarksAndStudentIDOneRow(result_id, subjects):  # returns the sum of all marks in that row
    subjects_string = ''

    indexes = len(subjects) - 1  # -1 because first index is 0
    for key, val in enumerate(subjects):
        if key == indexes:  # To avoid adding + after the last subject
            subjects_string = subjects_string + val
        else:
            subjects_string = subjects_string + val + ', '

    cursor = db.cursor()

    sql = """SELECT %s, student_id FROM `exam_results` WHERE exam_result_id = %s""" % (subjects_string, result_id)

    try:
        cursor.execute(sql)

        marks = {}

        for row in cursor.fetchall():
            for key, value in enumerate(subjects):
                marks[value.lower()] = 0 if row[key] is None else row[key]
            student_id = row[len(subjects)]

        data = {
            'marks': marks,
            'student_id': student_id
        }
        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def updateTotalForOneRowExamResults(result_id, stats):
    cursor = db.cursor()

    sql = """ UPDATE `exam_results` SET total = %s, points = %s, mean = %s WHERE exam_result_id = %s """ % (stats['total'], stats['points'], stats['mean'], result_id)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print e
        db.rollback()
        ret = False

    return ret


def getFormPositionsInExam(exam_id):
    cursor = db.cursor()

    # Order by firstname in case totals are equal
    sql = """SELECT `exam_result_id`, `total` 
                FROM exam_results e
                JOIN users u ON u.user_id = e.student_id
                WHERE exam_id = %s ORDER BY total DESC, first_name""" % exam_id

    try:
        cursor.execute(sql)

        dataArray = []

        count = 1
        for row in cursor.fetchall():
            data = {
                'exam_result_id': row[0],
                'form_position': count
            }

            count += 1

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def updateFormPosition(data):
    cursor = db.cursor()

    sql = """ UPDATE `exam_results` SET form_pos = %s WHERE exam_result_id = %s """ % (data['form_position'], data['exam_result_id'])

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret


def getClassPositions(exam_id, form):
    classes_in_form = getFormClasses(int(form))

    class_ids = classes_in_form['ids']

    classes_pos_data = []

    for class_id in class_ids:
        one_class_pos_data = getPositionsOneClass(exam_id, class_id)  # returns array of dicts

        if len(one_class_pos_data):
            # add dicts to classes_pos_data array one by one
            for record in one_class_pos_data:
                classes_pos_data.append(record)

    return classes_pos_data


def getPositionsOneClass(exam_id, class_id):
    cursor = db.cursor()

    # Order by firstname in case totals are equal
    sql = """SELECT `exam_result_id`, `total`
                FROM exam_results e
                JOIN users u ON u.user_id = e.student_id
                JOIN classes c ON c.class_id = u.class_id AND c.class_id = %s
                WHERE exam_id = %s ORDER BY total DESC, first_name""" % (class_id, exam_id)

    try:
        cursor.execute(sql)

        dataArray = []

        count = 1
        for row in cursor.fetchall():
            data = {
                'exam_result_id': row[0],
                'class_position': count
            }

            count += 1

            dataArray.append(data)

        ret = dataArray

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def updateClassPosition(data):
    cursor = db.cursor()

    sql = """ UPDATE `exam_results` SET class_pos = %s WHERE exam_result_id = %s """ % (data['class_position'], data['exam_result_id'])

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret


def checkIfAllSubjectsAreFilledOneRow(result_id, subjects, form):
    form = int(form)
    schDets = getSchoolDetails()
    subjects_lower_forms = schDets['lower_subjects']

    get_cols = ''

    indexes = len(subjects) - 1  # -1 because first index is 0
    for key, val in enumerate(subjects):
        if key == indexes:  # To avoid adding , after the last subject
            get_cols = get_cols + val
        else:
            get_cols = get_cols + val + ', '

    cursor = db.cursor()

    sql = """SELECT %s FROM `exam_results` WHERE exam_result_id = %s""" % (get_cols, result_id)

    try:
        cursor.execute(sql)

        dataArray = []

        # Get all column values that aren't null in order to count how many subjects have been filled
        for row in cursor.fetchall():
            for key, value in enumerate(subjects):
                if row[key] is not None:
                    dataArray.append(row[key])

        no_of_subjects_filled = len(dataArray)

        if form < 3:
            if no_of_subjects_filled < subjects_lower_forms:
                ret = False
            else:
                ret = True
        else:
            if no_of_subjects_filled < 8:
                ret = False
            else:
                ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def updateTotalledFieldManyRows(result_ids):
    result_ids_string = ''

    indexes = len(result_ids) - 1  # -1 because first index is 0
    for key, val in enumerate(result_ids):
        if key == indexes:  # To avoid adding + or , after the last subject
            result_ids_string = result_ids_string + str(val)
        else:
            result_ids_string = result_ids_string + str(val) + ', '

    cursor = db.cursor()

    sql = """ UPDATE `exam_results` SET `totalled`= 1 WHERE exam_result_id IN (%s) """ % result_ids_string

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret
