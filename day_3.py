from math import pow
from unicodedata import digit

def sortEntries():
    sentence = input("Enter the string: ").split()
    print(' '.join(sorted(set(sentence))))

def binDecimalByFive():
    binList = input("Enter the binary values: ").split(",")
    result = []

    ## ATTEMPT 2
    for ele in binList:
        if int(ele, 2)%5 == 0:
            result.append(ele)

    ## ATTEMPT 1
    # for idx in range(len(binList)):
    #     val = binList[idx].strip()
    #     decimal = 0
    #     for i in range(len(val)-1, -1, -1):
    #         decimal += int(str(val[i])) * int(pow(2, i))
            
    #     if decimal % 5 == 0:
    #         result.append(binList[idx])

    print(','.join([i for i in result]))


def allEvensInOne():
    result = []
    print("here")
    for num in range(1000, 3000, 2):
        strVal = str(num)
        flag = 1
        for ele in strVal:
            if int(ele)%2 != 0:
                flag = 0
                break
            
        if flag == 1:
            result.append(num)

    print(','.join([str(i) for i in result]))

def calculateAlphaDigits():
    inpList = input("Enter the sentence: ")
    alphabets, digits = 0, 0

    ## could also play with regex as attempt 2

    for idx in range(len(inpList)):
        asciiVal = ord(inpList[idx])
        if (asciiVal >= 97 and asciiVal <=122) or (asciiVal >= 65 and asciiVal <= 90):
            alphabets += 1
        elif asciiVal >= 48 and asciiVal <=57:
            digits += 1

    print("LETTERS ", alphabets)
    print("DIGITS ", digits)

def main():
    ## remove the duplicate elements & sort alphanumerically
    #sortEntries()

    ## binary form of multiples of 5
    #binDecimalByFive()

    ## each digit is an even number from 1000 to 3000
    #allEvensInOne()

    ## calculate alphabets and digits
    calculateAlphaDigits()

if __name__ == "__main__":
    main()