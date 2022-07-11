from math import sqrt

def listVsTuple():
    print("Enter the elements: ")
    # numList = [int(item) for item in input(": ").split(",")]
    numList = input().split(',')
    numTuple = tuple(numList)

    print(numList, "\n", numTuple)

class getPrintString:

    ## ATTEMPT 2
    def getString(self):
        self.line = input("Enter the string to print back: ")

    def printString(self):
        print("Here is the string in upper case:: ", self.line.upper())

    ## ATTEMPT 1
    # def getString():
    #     line = input("Enter the string to print back: ")
    #     return line
    
    # def printString(line1):
    #     print("Here is the string in upper case:: ", line1.upper())

def calculate():
    c, h = 50, 30
    print("Enter the values: ")
    dList = [int(item) for item in input().split(',')]
    result = list(range(len(dList)))
    for idx in range(0, len(dList)):
        result[idx] = round(sqrt((2*c*dList[idx])/h))

    print(result)

def twoDArr():
    dimensions = [int(x) for x in input("Enter the dimensions (row,column): ").split(',')]
    x, y = dimensions[0], dimensions[1]
    result = []
    
    ## ATTEMPT 2
    result = [[i*j for j in range(y)] for i in range(x)]

    ## ATTEMPT 1
    # for i in range(x):
    #     col = []
    #     for j in range(y):
    #         col.append(i*j)

    #     result.append(col)

    print(result)

def stringSort():
    inp = input("Enter the strings to sort: ").split(',')
    print(', '.join([i for i in sorted(inp)]))


def changeUp():
    sentences = []
    print("Enter lines: ")
    while True:
        line = input()
        if line:
            sentences.append(line.upper())
        else: 
            break

    print(f'\n'.join(i for i in sentences))

def main():
    ## list and tuples
    #listVsTuple()

    ## get and print strings methods in a class
    # ATTEMPT 2
    # xx = getPrintString()
    # xx.getString()
    # xx.printString()

    # ATTEMPT 1
    #getPrintString.printString(getPrintString.getString())

    ## calculate as per formula sqrt[(2*c*d)/h]
    # calculate()

    ## 2D Array with multiples in the elements
    #twoDArr()

    ## sort strings alphabetically
    #stringSort()

    ## multiple string upper conversion
    changeUp()

if __name__ == "__main__":
    main()