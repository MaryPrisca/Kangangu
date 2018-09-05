import MySQLdb
from connect import db

from datetime import datetime
import hashlib


def checkIfSetupIsComplete():
    cursor = db.cursor()

    sql = "SELECT setup_complete FROM system_setup"

    try:
        ret = False
        cursor.execute(sql)

        if cursor.rowcount < 1:
            ret = False
        else:
            for row in cursor:
                ret = row[0]

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        ret = False

    return ret


def getSubjectGroups():
    cursor = db.cursor()

    sql = """SELECT `group_id`, `group_name` FROM `subject_groups`"""

    try:
        cursor.execute(sql)

        names = []
        ids = []

        for row in cursor:
            ids.append(row[0])
            names.append(row[1])

        data = {
            "names": names,
            "ids": ids
        }

        ret = data

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        ret = False

    return ret


def getSetupData(setup_data):
    # Save admin
    userdata = saveAdminDetails(setup_data['adminDets'])

    userdata['school_details'] = {
                'school_name': setup_data['school_name'],
                'lower_subjects': setup_data['subjects_lower_form']
            }

    classes = setup_data['class_names']

    # save classes and forms
    for key, value in enumerate(classes):
        # key+1 reps form
        saveOneForm(key+1, len(value))

        for class_name in value:
            if class_name == "No Streams":
                class_name = "Form " + str(key+1)
            saveOneClass(class_name, key+1)

    # save subjects
    for subject in setup_data['subjects']:
        saveOneSubject(subject)

    saveSchDetails(setup_data['school_name'], setup_data['subjects_lower_form'])

    return userdata


def saveAdminDetails(data):
    data["user_id"] = 0

    dob = str(data["dob"])
    dob = dob[:-9]
    data["dob"] = datetime.strptime(dob, "%d/%m/%Y").date()

    m = hashlib.md5()
    m.update(data['password'])
    data['password'] = m.hexdigest()

    data["role"] = "admin"
    data["status"] = "Active"

    c = datetime.now()
    data["created_at"] = c.strftime('%Y-%m-%d %H:%M:%S')

    data["deleted"] = "0"

    cursor = db.cursor()

    sql = """
            INSERT INTO `users`(`user_id`, `first_name`, `last_name`, `surname`, `email`, `phone_number`, `dob`, `gender`,
                `username`, `password`, `role`, `status`, `created_at`, `deleted`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (data["user_id"], data["first_name"], data["last_name"], data["surname"], data["email"], data["phone"], data["dob"], data["gender"],
                             data["username"], data["password"], data["role"], data["status"], data["created_at"], data["deleted"]))
        db.commit()

        data['user_id'] = cursor.lastrowid
        data['class_id'] = 0
        data['reg_no'] = 0


        ret = data
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    # disconnect from server
    cursor.close()

    return ret


def saveOneForm(form_name, streams):
    cursor = db.cursor()

    sql = """INSERT INTO `forms`(`form_name`, `no_of_streams`) VALUES (%s, %s)"""

    try:
        cursor.execute(sql, (form_name, streams))
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    return ret


def saveOneClass(class_name, form_name):
    class_id = 0
    deleted = "0"

    cursor = db.cursor()

    sql = """
            INSERT INTO `classes`(`class_id`, `class_name`, `form_name`, `deleted`)
            VALUES (%s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (class_id, class_name, form_name, deleted))
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print(e)

        # print cursor._last_executed

        db.rollback()

        ret = False

    return ret


def saveOneSubject(data):
    alias = data['alias']
    # Remove spaces and special characters from the alias
    alias = ''.join(e for e in alias if e.isalnum())
    data['alias'] = alias

    data["deleted"] = "0"

    cursor = db.cursor()

    sql = """
            INSERT INTO `subjects`(`subject_id`, `subject_name`, `subject_alias`, `compulsory`, `group_id`, `deleted`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (0, data["name"], data["alias"], data["compulsory"], data["group_id"], data["deleted"]))
        db.commit()

        # Add subject as column to exam_results table
        data["alias"] = data["alias"].lower()

        sql = "ALTER TABLE exam_results ADD COLUMN %s DOUBLE DEFAULT NULL" % data["alias"]

        try:
            cursor.execute(sql)
            db.commit()

            ret = True

        except(MySQLdb.Error, MySQLdb.Warning) as e:
            ret = False
            print e
            db.rollback()
    except(MySQLdb.Error, MySQLdb.Warning) as e:

        db.rollback()

        ret = False

    return ret


def saveSchDetails(school_name, no_of_subjects):
    cursor = db.cursor()

    sql = """INSERT INTO `system_setup`(`id`, `school_name`, `subjects_lower_forms`, `setup_complete`) 
                VALUES (%s, %s, %s, %s)"""

    try:
        cursor.execute(sql, (0, school_name, no_of_subjects, 1))
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    return ret
