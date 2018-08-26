import MySQLdb
from connect import db
from datetime import datetime
# import pytz


def saveStudent(data):
    data["user_id"] = 0

    dob = str(data["dob"])
    dob = dob[:-9]
    data["dob"] = datetime.strptime(dob, "%d/%m/%Y").date()

    data["username"] = ""
    data["password"] = ""
    data["role"] = "student"
    data["status"] = "Active"

    c = datetime.now()
    data["created_at"] = c.strftime('%Y-%m-%d %H:%M:%S')

    data["deleted"] = "0"

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """
            INSERT INTO `users`(`user_id`, `first_name`, `last_name`, `surname`, `dob`, `gender`, `username`,
                `password`, `role`, `class_id`, `kcpe_marks`, `birth_cert_no`, `next_of_kin_name`, `next_of_kin_phone`, 
                `address`, `status`, `created_at`, `deleted`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    try:
        # Execute the SQL command
        cursor.execute(sql, (data["user_id"], data["first_name"], data["last_name"], data["surname"], data["dob"], data["gender"],
                             data["username"], data["password"], data["role"], data["class_id"], data["kcpe_marks"], data["birth_cert_no"],
                             data["kin_names"], data["kin_phone"], data["address"], data["status"], data["created_at"], data["deleted"] ))
        # Commit your changes in the database
        db.commit()

        ret = True
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

        # Rollback in case there is any error
        db.rollback()

        ret = False

    # # disconnect from server
    # db.close()

    return ret


def editStudent(data):
    cursor = db.cursor()

    sql = """ UPDATE users SET
                    first_name = %s,
                    last_name = %s,
                    surname = %s,
                    dob = %s,
                    gender = %s,
                    class_id = %s,
                    kcpe_marks = %s,
                    birth_cert_no = %s,
                    next_of_kin_name = %s,
                    next_of_kin_phone = %s                                     
                    WHERE user_id = %s """

    data = (data["first_name"], data["last_name"], data["surname"], data["dob"], data["gender"], data["class_id"],
            data["kcpe_marks"], data["birth_cert_no"], data["kin_names"], data["kin_phone"], data["user_id"])

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


def deleteStudent(id):
    cursor = db.cursor()

    sql = """UPDATE users SET deleted = %s WHERE user_id = %s"""

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


