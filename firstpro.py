def calculate_student():
    
    # make an empty dict
    students = {}

    # number of student, so we have the length of students and their scores.
    number = int( input("how many students you have? "))

    # for loop is for get names and scores and put them into students dict
    for i in range(number):
        name = input("write student's name: ")
        score = int( input("which score he/she get? "))
        students[name] = score

    # showing name and scores together in a dict.
    print(f"so this is their names and their scores {students}")

    #calculate the average of class's score. calculate sum and divide it to number.
    def average():
        total_score = sum(students.values())
        average_score = total_score/number
        print(f"average of this class is {average_score}")
    return average()

calculate_student()
