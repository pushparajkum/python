import re

def validate_email(emailIdList):
    print(emailIdList)
    validId = []
    invalidId = []
    for email in emailIdList:
        #valid_exp = re.match("(\w+)@(\w+)\.(\w+)", email)
        valid_exp = re.match("(\w+.\w+)@(\w+)\.(\w+)", email)
        if valid_exp == None:
            invalidId.append(email)
        else:
            validId.append(email)
    print("Invalid id's : ", invalidId)
    print("Valid id's : ", validId)

def main():
    emailIdList = []
    while(True):
        emailId = input("Please enter email id to validate, 'n' to end : ")
        if emailId == 'n':
            break
        emailIdList.append(emailId)
    validate_email(emailIdList)

if __name__ == "__main__":
    main()