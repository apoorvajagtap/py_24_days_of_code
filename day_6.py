import re

def checkPass():
    passList = input("Enter the passwords: ").split(',')
    for ps in passList:

        ## ATTEMPT 2
        if (6 <= len(ps) <= 12
        and re.search("[A-Z][a-z]", ps)
        and re.search("[0-9]", ps)
        and re.search("[$#@]", ps)):
            print(ps, end=', ')

        ## ATTEMPT 1
        # if len(ps) >= 6 and len(ps)<=12 and re.search("[A-Z][a-z]", ps):
        #     digCheck = re.findall("\d", ps)
        #     if digCheck:
        #         regex = re.compile('[$#@]')
        #         if (regex.search(ps) != None):
        #             print(ps, end=', ')

    print('\n')

def sortTuple():
    ls = []
    while True:
        line = input("Entry: ")
        if line:
            ls.append(tuple(line.split(',')))
        else:
            break
    
    # result = sorted(ls, key=lambda x: (x[0], x[1], x[2]))
    print(sorted(ls, key=lambda ele: (ele[0], int(ele[1]), int(ele[2]))))
        


def main():
    ## check password validity
    #checkPass()

    ## sort tuple name > age > score
    sortTuple()


if __name__ == "__main__":
    main()