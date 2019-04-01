def disjoint(list1, list2):
    flag = True
    for i in range(len(list1)):
        if list1[i] in list2:
            flag = False            

    return flag

def main():
    list1 = eval(input("Enter list1 : "))
    list2 = eval(input("Enter list2 : "))
    res = disjoint(list1,list2)

    if res:
        print("The 2 lists are disjoint..")
    else:
        print("The 2 lists are not disjoint..")

if __name__ == '__main__':
    main()