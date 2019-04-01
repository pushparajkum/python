#a list that contain all the elements of another list, but with additional elements

def superset(list1, list2):
    cnt = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            cnt += 1

    if cnt == len(list1):
        return "list2"

    cnt1 = 0
    for j in range(len(list2)):
        if list2[j] in list1:
            cnt1 += 1

    if cnt1 == len(list2):
        return "list1"

def main():
    list1 = eval(input("Enter list1 : "))
    list2 = eval(input("Enter list2 : "))
    res = superset(list1,list2)

    if res == "list1":
        print("list1 is superset of list2..")
    elif res == "list2":
        print("list2 is superset of list1..")
    else:
        print("The lists are not superset of each other..")

if __name__ == '__main__':
    main()