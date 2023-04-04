# define a student class
class Student:
    def __init__(self, name= 'Andrew', height=1.7, year = '1st', major='music', scores = [100,90,95]):
        self.name = name
        self.height = height
        self.major = major
        self.year = year
        self.scores = scores.copy()
    def compute_average_score(self):
        #compute average
        if len(self.scores) == 0:
            return 0
        else:
            return sum(self.scores)/len(self.scores)
    
    def compute_grade(self):
        avg = self.compute_average_score()
        if avg > 90:
            return 'A'
        elif 80<avg<90:
            return 'B'
        elif 70<avg<80:
            return 'C'
        else:
            return 'D'
