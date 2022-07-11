def countUpperLower():
    sent = input("Enter the sentence: ")
    upper, lower = 0, 0
    for char in sent:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("UPPER CASE ", upper)
    print("LOWER CASE ", lower)

def countValue():
    a = int(input("Enter the number: "))
    print(a + (a*10 + a) + (a*100 + a*10 + a) + (a*1000 + a*100 + a*10 + a))

def main():
    ## count upper case & lower case letters
    #countUpperLower()

    ## count a+aa+aaa+aaaa for given a
    countValue()

if __name__ == "__main__":
    main()