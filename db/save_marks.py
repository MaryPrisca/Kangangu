import MySQLdb
from connect import db


def getStudentList(data):
    cursor = db.cursor()

    columns = [data['subject_alias']]
    columnStr = ''
    for x in columns:
        columnStr = columnStr + x

    # sql = """SELECT user_id, first_name, last_name, surname
    #                 FROM `users` u
    #                 JOIN classes c
    #                     ON c.class_id = u.class_id AND c.class_id='%s'
    #                 WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % (data['class_id'], 'student')

    sql = """SELECT user_id, first_name, last_name, surname, %s AS mark, er.exam_result_id
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id AND c.class_id='%s'
                    LEFT JOIN exam_results er ON er.student_id = u.user_id AND er.exam_id = '%s'
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % (columnStr, data['class_id'], data['exam_id'], 'student')

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
        # ret = e
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
        print e
        # ret = e
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
            print e
            ret = False

        return ret


def saveMarks(insert_data, update_data):
    save_complete = True

    for (k, v) in insert_data.iteritems():
        if not saveMarksOneRecord(v['exam_id'], v['subject'], v['student_id'], v['mark']):
            save_complete = False

    for (k, v) in update_data.iteritems():
        if not updateMarksOneRecord(v['exam_result_id'], v['mark'], v['subject']):
            save_complete = False

    return save_complete


def saveMarksOneRecord(exam_id, subject, student_id, mark):
    cursor = db.cursor()

    sql = """INSERT INTO `exam_results`(`exam_result_id`, `exam_id`, `student_id`, %s) 
            VALUES (%s, %s, %s, %s)""" % (subject, 0, exam_id, student_id, mark)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    return ret


def updateMarksOneRecord(exam_result_id, mark, subject ):
    cursor = db.cursor()

    sql = """UPDATE `exam_results` SET %s = '%s' WHERE exam_result_id = '%s'""" % (subject, mark, exam_result_id)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    return ret