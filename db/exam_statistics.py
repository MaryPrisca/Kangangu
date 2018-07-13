def getGrade(mark):
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


def getStudentMean(marks_array):
    # print marks_array
    avg = sum(marks_array) / 5
    return getGrade(avg)


def calculateMean(marks_array):
    mean = ""

    if len(marks_array) > 0 :
        avg = sum(marks_array) / len(marks_array)
        avg = round(avg, 3)
        mean = getGrade(avg)

    return mean