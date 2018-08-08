import MySQLdb
from connect import db


def getStudentList(class_id, subject_id):
    cursor = db.cursor()

    sql = """SELECT user_id, first_name, last_name, surname, subjects_taken
                    FROM `users` u
                    JOIN classes c
                        ON c.class_id = u.class_id AND c.class_id='%s'
                    WHERE u.deleted = 0 AND c.deleted = 0 AND role='%s'""" % (class_id, 'student')

    try:
        cursor.execute(sql)

        students_in_subject = []  # Store students that already selected subject before

        dataArray = []

        for row in cursor:
            data = {}

            data['user_id'] = row[0]
            data['student_name'] = row[1] + " " + row[2] + " " + row[3]
            data['subjects'] = row[4].split(",") if row[4] is not None else ""

            # Check if student already selected subject in question
            if data['subjects'] != "":
                if data['subjects'].count(str(subject_id)) == 0:  # Returns number of times item occurs in list
                    data['subject_ticked'] = False
                else:
                    data['subject_ticked'] = True

                    stud = {}

                    stud["user_id"] = data['user_id']
                    stud["student_name"] = data['student_name']

                    students_in_subject.append(stud)

            else:
                data['subject_ticked'] = False

            dataArray.append(data)

        data = {
            'student_list': dataArray,
            'students_present': students_in_subject
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def chooseSubjects(data):
    all_saved = True
    for student in data:
        subjects = ','.join(map(str, student['subject_taken']))  # Stringify subject taken array

        if not updateSubjectsTakenOneStudent(student['user_id'], subjects):
            all_saved = False

    return all_saved


def updateSubjectsTakenOneStudent(user_id, subjects_taken):
    cursor = db.cursor()

    sql = """UPDATE users SET subjects_taken = '%s' WHERE user_id = %s """ % (subjects_taken, user_id)

    try:
        cursor.execute(sql)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()

        ret = False

    return ret