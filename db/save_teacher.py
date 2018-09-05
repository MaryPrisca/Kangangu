import MySQLdb
from connect import db
from datetime import datetime

import hashlib


def saveTeacher(data):
    data["user_id"] = 0

    dob = str(data["dob"])
    dob = dob[:-9]
    data["dob"] = datetime.strptime(dob, "%d/%m/%Y").date()

    m = hashlib.md5()
    m.update(data['password'])
    data['password'] = m.hexdigest()

    data["role"] = "teacher"
    data["status"] = "Active"

    c = datetime.now()
    data["created_at"] = c.strftime('%Y-%m-%d %H:%M:%S')

    data["deleted"] = "0"

    cursor = db.cursor()

    sql = """
            INSERT INTO `users`(`user_id`, `first_name`, `last_name`, `surname`, `email`, `phone_number`, `dob`, `gender`, `username`,
                `password`, `role`, `subject1`, `subject2`, `address`, `national_id`, `tsc_no`, `status`, `created_at`, `deleted`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    try:
        cursor.execute(sql, (data["user_id"], data["first_name"], data["last_name"], data["surname"], data["email"], data["phone"], data["dob"], data["gender"],
                             data["username"], data["password"], data["role"], data["subjectOneID"], data["subjectTwoID"], data["address"], data["national_id"],
                             data["tsc_no"], data["status"], data["created_at"], data["deleted"]))
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        db.rollback()

        ret = False

    # # disconnect from server
    # db.close()

    return ret


def editTeacher(data):
    cursor = db.cursor()

    sql = """ UPDATE users SET
                    first_name = %s,
                    last_name = %s,
                    surname = %s,
                    email = %s,
                    username = %s,
                    dob = %s,
                    gender = %s,
                    subject1 = %s,               
                    subject2 = %s               
                    WHERE user_id = %s """

    data = (data["first_name"], data["last_name"], data["surname"], data["email"], data["username"], data["dob"], data["gender"], data["subjectOneID"], data["subjectTwoID"], data["user_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        db.rollback()

        # ret = e
        ret = False

    return ret


def deleteTeacher(id):
    cursor = db.cursor()

    sql = """ UPDATE users SET deleted = %s WHERE user_id = %s """

    data = (1, id)

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        # print(e)
        db.rollback()
        ret = False

    return ret


