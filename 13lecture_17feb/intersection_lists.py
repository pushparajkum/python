
def intersection(list1, list2):
    list3 = []
    k = 0

    for i in range(len(list1)):
      for j in range(len(list2)):
        if list1[i] == list2[j]:
          list3.append(list2[j])
          k+=1
        else:
          continue
    return list3

def main():
    list1 = eval(input("Enter list1 : "))
    list2 = eval(input("Enter list2 : "))
    res = intersection(list1, list2)
    print("the intersection is : ", res)

if __name__  == "__main__":
    main()