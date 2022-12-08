class Course:
    def __init__(self,t,m):
        self.__CourseTitle=t
        self.__MaxStudents=m
        self.__NumberOfLessons=0
        self.__CourseAssessment=Assessment
    def AddAssessment(self,t,m):
        self.__CourseAssessment=Assessment(t,m)
    def Print_Course(self):
        self.__CourseAssessment.Print_Data()
class Assessment:
    def __init__(self,t,m):
        self.__AssessmentTitle=t
        self.__MaxMarks=m
    def Print_Data(self):
        print(self.__AssessmentTitle,self.__MaxMarks)
ThisCourse=Course("computing",100)
ThisCourse.AddAssessment("programming",100)
ThisCourse.Print_Course()

