import MySQLdb
from connect import db


def saveClass(data):
    data["class_id"] = 0
    data["deleted"] = "0"

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """
            INSERT INTO `classes`(`class_id`, `class_name`, `form_name`, `deleted`)
            VALUES (%s, %s, %s, %s)
        """

    try:
        # Execute the SQL command
        cursor.execute(sql, (data["class_id"], data["class_name"], data["form_name"], data["deleted"]))
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


def editClass(data):
    cursor = db.cursor()

    sql = """ UPDATE classes SET
                    class_name = %s,
                    form_name = %s
                    WHERE class_id = %s """

    data = (data["class_name"], data["form_name"], data["class_id"])

    try:
        cursor.execute(sql, data)
        db.commit()

        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        db.rollback()
        ret = False

    return ret


def deleteClass(id):
    cursor = db.cursor()

    sql = """ UPDATE classes SET deleted = %s WHERE class_id = %s """

    data = (1, id)

    try:
        cursor.execute(sql, data)
        db.commit()
        ret = True

    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print e
        db.rollback()
        ret = False

    return ret

