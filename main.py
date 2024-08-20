def calculate_score():
    print('----------------------------------------------------------------------------------')
    # make an empty dict
    students = {}

    # number of student, so we have the length of students and their scores.
    number = int( input("how many students you have? "))

    # for loop is for get names and scores and put them into students dict
    for i in range(number):
        name = input("write student's name: ")
        score = float( input("which score he/she get? "))
        students[name] = score

    # showing name and scores together in a dict.
    print(f"so this is their names and their scores {students}")

    #call and print average_scores that we write after this function because our code will be cleaner
    print(f"average of this class is '{average_scores(students.values())}'")

#calculate the average of class's score. calculate sum and divide it to number.
def average_scores(grade):
    total_score = sum(grade)
    answer = total_score/len(grade)
    return answer
# calling the app
calculate_score()