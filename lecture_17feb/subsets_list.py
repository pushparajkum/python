def subset(list1, list2):
    cnt = 0
    for i in range(len(list2)):
        if list2[i] in list1:
           cnt+=1
    if cnt == len(list2):
        return True
    else:
        return False

def main():
    list1 = eval(input("Enter list1 : "))
    list2 = eval(input("Enter list2 : "))
    res = subset(list1, list2)

    if res:
        print("List2 is subset of list1.")
    else:
        print("List2 is not subset of list1.")

if __name__ == '__main__':
    main()