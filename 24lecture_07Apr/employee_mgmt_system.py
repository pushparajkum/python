# Employee Management System

class Employee:
    autoEmpNo = 1
    def __init__(self, empName, empAddr, empDOB, empContact, emrgencyContact, empGender, empEmail, empJobLevel, empRating):
        self.__empName = empName
        self.__empAddr = empAddr
        self.__empDOB = empDOB
        self.__empContact = empContact
        self.__emergencyContact = emrgencyContact
        self.__empGender = empGender
        self.__empEmail = empEmail
        self.__empJobLevel = empJobLevel
        self.__empRating = empRating
        self.__empNo = Employee.autoEmpNo
        Employee.autoEmpNo += 1

    def getEmpNo(self):
        return self.__empNo
    
    def getEmpName(self):
        return self.__empName

    def getEmpAddr(self):
        return self.__empAddr

    def getEmpDOB(self):
        return self.__empDOB
    
    def getEmpContact(self):
        return self.__empContact

    def getEmergencyContact(self):
        return self.__emergencyContact
    
    def getEmpGender(self):
        return self.__empGender

    def getEmpEmail(self):
        return self.__empEmail
    
    def getEmpJobLevel(self):
        return self.__empJobLevel
    
    def getEmpRating(self):
        return self.__empRating
    
    def updateAddress(self, addr):
        self.__empAddr = addr
    
    def updateContact(self, contact):
        self.__empContact = contact
    
    def updateEmergencyContact(self, contact):
        self.__emergencyContact = contact
    
    def updateJobLevel(self, jobLevel):
        self.__empJobLevel = jobLevel
    
    def updateRating(self, rating):
        self.__empRating = rating
    
    def __repr__(self):
        return "Name : "+self.__empName + "\nAddress : "+self.__empAddr+"\nDOB : "+self.__empDOB+"\nContact : "+self.__empContact+"\nEmergency Contact : "+self.__emergencyContact+"\nGender : "+self.__empGender+"\nEmail : "+self.__empEmail+"\nJob Level : "+self.__empJobLevel+"\nRating : "+self.__empRating

def unitTestEmployee():
    emp = Employee("Raj", "Pune", "06-09-1989", "9767149212", "9767105018", "M", "raj@gmail.com", "4","good")
    print("Employee number : ", emp.getEmpNo())
    print("Employee name : ", emp.getEmpName())
    print("Employee address : ", emp.getEmpAddr())
    print("Employee date of birth : ", emp.getEmpDOB())
    print("Employee contact : ", emp.getEmpContact())
    print("Employee emergency contact number : ", emp.getEmergencyContact())
    print("Employee gender : ", emp.getEmpGender())
    print("Employee email : ", emp.getEmpEmail())
    print("Employee Job level : ", emp.getEmpJobLevel())
    print("Employee rating : ", emp.getEmpRating())
    # empName, empAddr, empContact, emrgencyContact, empGender, empJobLevel, empRating
    emp.updateAddress("Chinchwad")
    print("updated Employee address : ", emp.getEmpAddr())
    emp.updateContact("9922841902")
    print("updated Employee contact : ", emp.getEmpContact())
    emp.updateEmergencyContact("9922841908")
    print("updated Employee emergency contact number : ", emp.getEmergencyContact())
    emp.updateJobLevel("4A")
    print("updated Employee Job level : ", emp.getEmpJobLevel())
    emp.updateRating("very good")
    print("updated Employee rating : ", emp.getEmpRating())

def main():
    unitTestEmployee()

if __name__ == "__main__":
    main()