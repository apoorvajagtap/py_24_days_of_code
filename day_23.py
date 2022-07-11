import textwrap
from datetime import date, datetime


def findRunnerUp():
    ls = []
    size = int(input("Enter the size of list: "))
    for i in range(size):
        ls.append(int(input()))
    
    ## ATTEMPT 2
    ls = sorted(set(ls))
    print("Runner up: ", ls[-2])

    ## ATTEMPT 1
    # max, secMax = 0, 0

    # for i in ls:
    #     if i > max:
    #         max = i
    #     elif i < max and i > secMax:
    #         secMax = i

    # print("Runner up: ", secMax)

def wrapAsW():
    s = input("Enter the string: ")
    w = int(input("Enter the width: "))

    res = textwrap.wrap(s, width=w)
    for line in res:
        print(line)

    # for i in range(0, len(s), w):
    #     print(s[i]+s[i+1]+s[i+2]+s[i+3])    # need if conditions to make it work for all cases

def rangoli(size):
    # init = 96
    val = 96+size
    print("alallala ", val, chr(val))

    dim = val + size - ord('a')
    dim += (dim - 1)

    ls = [['-']*dim]*size 

    for i in range(size-1, -1, -1):
        for j in range(dim):
            if j%2==0:
                ls[i][j] = chr(val)
                print(ls[i][j])

        val -= 1   

    for i in range(size):
        print(ls[i])

def findDay(d):
    day, mon, year = d.split('/')
    day_name = date(int(year), int(mon), int(day))

    print(day_name.strftime("%A"))

def main():
    ## Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
    ## You are given scores. Store them in a list and find the score of the runner-up.
    # findRunnerUp()

    ## You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
    # wrapAsW()

    ## You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
    # rangoli(int(input("Enter the size: ")))  YET TO COMPLETE

    ##  given a date. Your task is to find what the day is on that date.
    findDay(input("Enter the date (d/m/y): "))


if __name__ == "__main__":
    main()