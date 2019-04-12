#!/usr/bin/python

class Student:
    auto_roll_no = 1
    def __init__(self, name, address, dob, course, division):
        self.__roll_no = Student.auto_roll_no
        Student.auto_roll_no += 1
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__course = course
        self.__division = division
        self.__marks = dict()
    def getRollNo(self):
        return self.__roll_no
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getDOB(self):
        return self.__dob
    def getCourse(self):
        return self.__course
    def getDivision(self):
        return self.__division
    def getMarks(self):
        return self.__marks
    def updateAddress(self, address):
        self.__address = address
    def updateMarks(self, subject, marks):
        self.__marks[subject] = marks
    def updateCourse(self, course):
        self.__course = course
    def updateDivision(self, division):
        self.__division = division
    def __repr__(self):
        return "Name:"+self.__name+"\nAddress:"+self.__address+"\nDOB:"+self.__dob+"\nRoll No:"+str(self.__roll_no)
def UnitTestStudent():
    s1 = Student("Jeetendra", "Parvati", "29-12-1986","MSC", "A")
    print("Name:"+s1.getName())
    print("DOB:"+s1.getDOB())
    print("Course:"+s1.getCourse())
    print("Address:"+s1.getAddress())
    s1.updateAddress("Cambridge")
    print("Updated Address:"+s1.getAddress())
    s1.updateMarks("Principles Of Programming Language", 84)
    s1.updateMarks("Python Programming Language", 94)
    s1.updateMarks("Design Patterns", 75)
    print(s1.getMarks())

class StudentManager:
    def __init__(self, noOfStudents):
        self.__no_of_students = noOfStudents
        self.__enrolled_students = dict()
        self.__suspended_students = dict()

    def GetEnrolledStudents(self):
        return self.__enrolled_students

    def GetSuspendedStudents(self):
        return self.__suspended_students

    def EnrollStudent(self, name, address, dob, course, div):
        st = Student(name, address, dob, course, div)
        self.__enrolled_students[st.getRollNo()] = st

    def SuspendStudent(self, roll_no):
        if roll_no in self.__suspended_students:
            pass
        elif roll_no in self.__enrolled_students:
            st = self.__enrolled_students.pop(roll_no)
            self.__suspended_students[roll_no] = st
        else:
            return False
        return True

    def UpdateMarks(self, roll_no, subject, marks):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateMarks(subject, marks)
            return True
        return False
    def GetMarks(self, roll_no):
        return self.__enrolled_students[roll_no].getMarks()

    def UpdateAddress(self, roll_no, address):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateAddress(address)
            return True
        return False
    def GetAddress(self, roll_no):
        return self.__enrolled_students[roll_no].getAddress()
        
    def UpdateCourse(self, roll_no, course):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateCourse(course)
            return True
        return False
    def GetCourse(self, roll_no):
        return self.__enrolled_students[roll_no].getCourse()

    def UpdateDivision(self, roll_no, division):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateDivision(division)
            return True
        return False
    def GetDivision(self, roll_no):
        return self.__enrolled_students[roll_no].getDivision()
def UnitTestStudentManager():
    sm = StudentManager(50)
    sm.EnrollStudent("Jeetendra", "Parvati", "29-12-1986", "MSC", "A")
    sm.EnrollStudent("Bharat", "Parvati", "25-08-1985", "MCOM", "B")
    sm.EnrollStudent("Ravi", "Bibwewadi", "21-11-1989", "MBA", "A")
    #print("Enrolled Students:\n", sm.GetEnrolledStudents())
    print("\n***********Displaying Enrolled Students*********\n")
    students =  sm.GetEnrolledStudents()
    for st in students:
        print(students[st])
    sm.SuspendStudent(1)
    #print("Enrolled Students:\n", sm.GetEnrolledStudents())
    #print("Suspended Students:\n", sm.GetSuspendedStudents())

    print("\n***********Displaying Enrolled Students*********\n")
    students =  sm.GetEnrolledStudents()
    for st in students:
        print(students[st])
    print("\n***********Displaying Suspended Students**********\n")
    students =  sm.GetSuspendedStudents()
    for st in students:
        print(students[st])
    print(sm.GetMarks(2))
    sm.UpdateMarks(2, "Science", 45)
    print(sm.GetMarks(2))
    
    print(sm.GetCourse(2))
    sm.UpdateCourse(2, "Science")
    print(sm.GetCourse(2))

def Menu():
    pass
    #Enroll Student
    #Suspend Student
    #Print All Students
    #Print Enrolled Students with Percentage
    #Print Suspended Students
    #Update Student Details
        #Address
        #Division
        #Course
        #Marks
def StudentManagementSystem():
    n = 10 # accept from user
    sm = StudentManager(n)
    while True:
        ch = Menu()
        #if - elif to handle choices
def main():
    #UnitTestStudent()
    UnitTestStudentManager()
if __name__ == "__main__":
    main()
