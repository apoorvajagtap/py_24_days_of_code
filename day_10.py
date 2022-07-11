def squareOfKeys():
    sq = {}
    for i in range (1, 21):
        sq[i] = i ** 2

    # for key in sq:
    #     print("{0}: {1}".format(key, sq[key]))

    return sq

def printKeysOnly(d):
    print(d.keys())

def squareList():
    sqLs = []
    for i in range(1, 21):
        sqLs.append(i ** 2)

    #print(', '.join([str(i) for i in sqLs]))
    return sqLs

def printFirstFive(ls):
    print(ls[:5])
    #print(', '.join([str(ls[i]) for i in range(5)]))

def printLastFive(ls):
    print(ls[-5:])

def printExceptFirstFive(ls):
    print(ls[5:])

def squareTup(ls):
    tp = tuple(ls)
    print(tp)

def main():
    ## function to print square of keys (in a dict)
    #squareOfKeys()

    ## same as squareOfKeys(), should just print keys only
    #printKeysOnly(squareOfKeys())

    ## generate & print a list with square of numbers 1 to 20
    squareList()

    ## same as squareList and print first 5 elements
    #printFirstFive(squareList())

    ## same as squareList and print last 5 elements    
    #printLastFive(squareList())

    ## same as squareList and print all except first 5 elements
    #printExceptFirstFive(squareList())

    ## generate & print tuple with squares of 1 to 20
    squareTup(squareList())

if __name__ == "__main__":
    main()