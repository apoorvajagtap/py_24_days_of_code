import random

def evenAssert(ls):
    for ele in ls:
        assert ele % 2 == 0

def basicEvaluation(exp):
    print(eval(exp))

def binSearch(ls):
    find = int(input("Enter the element to find: "))

    ls = list([int(x) for x in ls])

    mid = round(len(ls) / 2)
    if find == ls[mid]:
        print(mid)
    elif find < ls[mid]:
        for i in range(mid):
            if find == ls[i]:
                print(i)
    else:
        for i in range(mid+1, len(ls)):
            if find == ls[i]:
                print(i)

def main():
    ## assert statement to check all even in the given list
    # evenAssert([2,4,6,8])

    ## accepts basic mathematic expression from console and print the evaluation result.
    # basicEvaluation(input("Enter the expression: "))

    ## search element in sorted list
    # binSearch(input("Enter the elements of list: ").split(','))

    ## generate random float from 1 to 100]
    # print(random.uniform(1, 100))

    ## generate a random float where the value is between 5 and 95 using Python module.
    print(random.uniform(5, 95))

if __name__ == "__main__":
    main()