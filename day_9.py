def sumTwo(num1, num2):
    return num1 + num2

def convToString(num):
    print(str(num))
    print(type(str(num)))

def strToIntSum(num1, num2):
    print(int(num1) + int(num2))

def concatTwo(str1, str2):
    print(str1 + str2)

def maxLength(str1, str2):
    if len(str1) == len(str2):
        print(str1)
        print(str2)
    elif len(str1) > len(str2):
        print(str1)
    else:
        print(str2)

def main():
    ## compute sum of two numbers
    #num1, num2 = input("Enter the numbers to add: ").split()
    ## ATTEMPT 2:::
    # sum = lambda n1, n2: n1 + n2
    # print(sum(int(num1), int(num2)))
    ## ATTEMPT 1::::
    # print(sumTwo(int(num1), int(num2)))

    ## function to convert integer to string
    #convToString(int(input("Enter the number: ")))

    ## function to recieve two numbers in string type
    # numStr1, numStr2 = input("Enter the numbers: ").split()
    # strToIntSum(numStr1, numStr2)

    ## function to concatenate two strings and print
    # s1, s2 = input("Enter the two strings: ").split()
    # concatTwo(s1, s2)

    ## Print the string(s) with max length
    s1, s2 = input("Enter the two strings: ").split()
    maxLength(s1, s2)

if __name__ == "__main__":
    main()