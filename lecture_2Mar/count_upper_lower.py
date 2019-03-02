# wap to accept a sentence which contains uppercase and lowercase words return a dict with count of total number of lowercase and lowercase chars..

def count_upper_lower(str1):
    upper = 0
    lower = 0
    for x in str1:
        if x.isupper():
            upper += 1
        else:
            lower += 1
    return {"upper":upper, "lower":lower}

def main():
    str1 = input("Enter the sentence :: ")
    res = count_upper_lower(str1)
    print(res)

if __name__ == "__main__":
    main()