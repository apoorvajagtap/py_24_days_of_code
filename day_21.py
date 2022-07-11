def intersectionLs(ls1, ls2):
    if len(ls2) > len(ls1):
        temp = ls1
        ls1 = ls2
        ls2 = temp

    print([i for i in ls1 if i in ls2])

class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")


def main():
    ## print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
    # ls = [12,24,35,70,88,120,155]
    # print([ls[i] for i in range(len(ls)) if i not in (0,4,5)])

    ## print the list after removing the value 24 in [12,24,35,24,88,120,155]
    # ls = [12,24,35,24,88,120,155]
    ## ATTEMPT 2 (won't satisfy the requirement completely)
    # ls.remove(24)
    # print(ls)

    ## ATTEMPT 1
    # print([i for i in ls if i!=24])

    ## given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
    ## write a program to make a list whose elements are intersection of the above given lists.
    # intersectionLs([12,24,35,24,88,120,155], [1,3,6,78,35,55])

    ## given list [12,24,35,24,88,120,155,88,120,155], 
    ## write a program to print this list after removing all duplicate values with original order reserved.
    # print([key for key in dict.fromkeys([12,24,35,24,88,120,155,88,120,155])])

    ## class Person and its two child classes: Male and Female. 
    ## All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
    m = Male()
    f = Female()
    m.getGender()
    f.getGender()

if __name__ == "__main__":
    main()