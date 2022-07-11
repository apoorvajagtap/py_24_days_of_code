def printHalves(tp):
    midSize = int(len(tp)/2)
    print(tp[:midSize])
    print(tp[-midSize:])

def printEven(tp):
    tp1 = tuple(filter(lambda x: x%2 == 0, tp))
    print(', '.join(str(i) for i in tp1))

    ## ATTEMPT 1
    # for i in tp:
    #     if i % 2 == 0:
    #         print(i, end=', ')

def checkYes():
    ch = input("Enter Yes/No: ")
    if ch == "yes" or ch == "YES" or ch == "Yes":
        print("Yes")
    else:
        print("No")

def mapSquare(ls):
    res = list(map(lambda x: x**2, ls))
    print(res)

def mapEvenSquare(ls):
    # squares = list(map(lambda x: x**2, ls))
    # res = list(filter(lambda x: x%2 == 0, squares))

    # res = list(filter(lambda x: x%2==0, map(lambda y: y**2, ls)))

    ## efficient approach (first filters than squares)
    res = list(map(lambda y: y**2, filter(lambda x: x%2==0, ls)))
    print(res)

def evenFilter():
    res = list(filter(lambda x: x%2==0, range(1, 21)))
    print(res)

def main():
    #tp = (1,2,3,4,5,6,7,8,9,10)
    #ls = [1,2,3,4,5,6,7,8,9,10]

    ## Print halves of a tuple in different line
    #printHalves(tp)

    ## Print values that are even in given tuple
    #printEven(tp)

    ## string to print Yes if input >> ("yes" or "YES" or "Yes") else No
    #checkYes()

    ## use map() to generate a list with squares of elements of ls
    # mapSquare(ls)

    ## use map() and filter() to make a list whose elements are square of even number in ls
    #mapEvenSquare(ls)

    ## filter even elements from a list of 1to20(included) using filter
    evenFilter()

if __name__ == "__main__":
    main()