def union(list1, list2):
    list3 = []

    for i in range(len(list1)):
      list3.append(list1[i])
    
    for j in range(len(list2)):
        if list2[j] not in list1:
          list3.append(list2[j])
    return list3

def main():
    list1 = eval(input("Enter list1 : "))
    list2 = eval(input("Enter list2 : "))
    res = union(list1, list2)
    print("the [union] is : ", res)

if __name__  == "__main__":
    main()