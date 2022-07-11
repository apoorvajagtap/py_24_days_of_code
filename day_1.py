## multiples of 7 but not 5 in a specified range:
def sevenMultiple():
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            print(num, end=", ")
            num += 7


## factorial of a given number
def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

## dictionary with squares of each number
def squareDict():
    sdict = {}
    num = int(input("Enter the size of dictionary: "))
    for i in range(1, num+1):
        sdict[i] = i*i
    
    print(sdict)        

def main():
    ## multiples of 7 but not 5
    #sevenMultiple()

    ## factorial
    # num = int(input("Enter the number to factorize: "))
    # print(num, "! = ", factorial(num))

    ## squareDict
    squareDict()

if __name__ == "__main__":
    main()