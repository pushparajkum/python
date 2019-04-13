# WAP to implement student management system.
# student should have - Name, address, dob, course, division, marks[]
# provide following methods - Addstudent, suspendStudent, UpdateAddress, UpdateMarks, 
# printAllStudentDetails and their percentage

from Person import Person 

class Student(Person):
    autoRollNo = 1

    def __init__(self, name, addr, dob, course, division):
        Person.__init__(self, name, addr, dob)
        self.__course = course
        self.__div = division
        self.__marks = dict()
        self.__rollNo = Student.autoRollNo
        Student.autoRollNo += 1

    def getName(self):
        return Person.getName(self)
    
    def getAddr(self):
        return Person.getAddr(self)

    def getdob(self):
        return Person.getdob(self)

    def getRollNo(self):
        return self.__rollNo

    def getCourse(self):
        return self.__course
    
    def getDivision(self):
        return self.__div
    
    def getMarks(self):
        return self.__marks
    
    def UpdateAddress(self, address):
        Person.UpdateAddress(self, address)

    def UpdateMarks(self, subject, marks):
        self.__marks[subject] = marks

    def UpdateCourse(self, course):
        self.__course = course
    
    def UpdateDivision(self, division):
        self.__div = division

    def __repr__(self):
        return "Name : "+self.getName() +"\nAddress : "+self.getAddr() +"\nDOB : "+self.getdob()+"\nCourse : "+self.__course+"\nDivision : "+self.__div

def unitTestStudent():
    stud = Student("Raj", "Chinchwad", "06-09-1989", "MCA", "A")
    print(stud.autoRollNo)
    print(stud.getName())
    print(stud.getAddr())
    print(stud.getCourse())
    print(stud.getDivision())
    print(stud.getdob())
    print(stud.getMarks())

    stud.UpdateAddress("Pune")
    print("Updated address :: "+stud.getAddr())
    stud.UpdateCourse("BA")
    stud.UpdateDivision("B")
    stud.UpdateMarks("maths", "100")
    stud.UpdateMarks("science", "80")
    print(stud.getMarks())

class StudentManager:
    def __init__(self,noOfStudents):
        self.__noOfStudents = noOfStudents
        self.__enrolledStudents = dict()
        self.__suspendedStudents = dict()
    
    def getEnrolledStudents(self):
        return self.__enrolledStudents

    def getSuspendedStudents(self):
        return self.__suspendedStudents

    def enrollStudent(self, name, addr, dob, course, div):
        stud = Student(name, addr, dob, course, div)
        self.__enrolledStudents[stud.getRollNo()] = stud

    def suspendStudent(self, rollNo):
        if rollNo in self.__suspendedStudents:
            pass
        elif rollNo in self.__enrolledStudents:
            self.__suspendedStudents[rollNo] = self.__enrolledStudents.pop(rollNo)
        else:
            return False
        return True

    def updateMarks(self, rollNo, subject, marks):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.UpdateMarks(subject, marks)
            return True
        return False

    def getMarks(self,rollNo):
        return self.__enrolledStudents[rollNo].getMarks()

    def updateAddress(self, rollNo, address):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.UpdateAddress(address)
            return True
        return False

    def getAddress(self,rollNo):
        return self.__enrolledStudents[rollNo].getAddr()

    def updateDiv(self, rollNo, div):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.UpdateDivision(div)
            return True
        return False

    def getDiv(self,rollNo):
        return self.__enrolledStudents[rollNo].getDivision()

    def updateCourse(self, rollNo, course):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.UpdateCourse(course)
            return True
        return False

    def getCourse(self,rollNo):
        return self.__enrolledStudents[rollNo].getCourse()

def unitTestStudentManager():
    studMgr = StudentManager(3)
    studMgr.enrollStudent("Raj","Chinchwad","06-09-1989","MCA","A")
    studMgr.enrollStudent("Pushp","Pune","04-02-1991","MCs","B")
    studMgr.enrollStudent("Pushparaj","Mumbai","12-10-1992","MBA","C")
    
    print("\n\nEnrolled Students List : ")
    students = studMgr.getEnrolledStudents()
    for st in students:
        print("\n",students[st])
    
    studMgr.suspendStudent(2)
    print("\n\nSuspended students list : ")
    student = studMgr.getSuspendedStudents()
    for st1 in student:
        print("\n",student[st1])

    print("\n\nUpdated students list : ")
    students = studMgr.getEnrolledStudents()
    for st2 in students:
        print("\n",students[st2])
    
    print("\n\nUpdate Marks, course, division and address : ")
    studMgr.updateMarks(1,"Science",94)
    print(studMgr.getMarks(1))

    studMgr.updateCourse(1,"BCA")
    print(studMgr.getCourse(1))

    studMgr.updateDiv(1,"D")
    print(studMgr.getDiv(1))

    studMgr.updateAddress(1,"Mumbai")
    print(studMgr.getAddress(1))

def displayStudentMenu(studMgr):
    ch = 1
    while(ch != 0):
        print("1. Get List of All Students")
        print("2. Get List of Enrolled Students List")
        print("3. Get List of Suspended Students List")
        print("4. Get Details of Student")
        print("5. Enroll Student")
        print("6. Suspend Student")
        print("7. Update Address")
        print("8. Update Division")
        print("9. Update Course")
        print("10. Update Marks")
        print("0. Exit")
        ch = eval(input("Enter your choice : "))
        if ch == 1:
            print(studMgr.getEnrolledStudents())
        elif ch == 2:
            print(studMgr.getEnrolledStudents())
        elif ch == 3:
            print(studMgr.getSuspendedStudents())
        elif ch == 4:
            rno = eval(input("Enter the roll number of student to display information : "))
            pass
        elif ch == 5:
            pass
        elif ch == 6:
            pass
        elif ch == 7:
            pass
        elif ch == 8:
            pass
        elif ch == 9:
            pass
        elif ch == 10:
            pass
        else:
            exit


def main():
    #unitTestStudent()
    unitTestStudentManager()
    
    #studNum = eval(input("Enter number of students you want : "))
    #studMgr = StudentManager(studNum)
    #displayStudentMenu(studMgr)
    #studMgr.enrollStudent("Raj","Chinchwad","06-09-1989","MCA","A")
    #studMgr.enrollStudent("Pushp","Pune","04-02-1991","MCs","B")
    #studMgr.enrollStudent("Pushparaj","Mumbai","12-10-1992","MBA","C")

if __name__ == "__main__":
    main()