     
# from student import Student as stud
# import numpy as np
# from data_logger import Logger
from info2000_utilities import data_logger, student
def get_user_details():
    my_student = student.Student()
    my_student.name = input("Name")
    my_student.height = input("Height")
    my_student.major = input("What's your major?")
    my_student.year = input("What's your year")

    return my_student
for _ in range(5):
    returned_student = get_user_details() # call function
    print(f"Hello {returned_student.name}, you are {returned_student.height} m tall. \nI hope you're enjoying your {returned_student.major} major")
    returned_student.scores = [90, 95, 100]
    print(f"Your average score is:{returned_student.compute_average_score()}, \nand your grade is{returned_student.compute_grade()} ")

    my_logger = data_logger.Logger('student_data.txt')
    my_logger.logrow(f"{returned_student.name},{returned_student.major},{returned_student.year},{returned_student.scores}")