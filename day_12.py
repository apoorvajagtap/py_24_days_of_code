def mapListSquare():
    res = list(map(lambda x: x**2, range(1, 21)))
    print(res)

class American:
    pass

    # @staticmethod
    # def printNationality():
    #     print("I am American")

class NewYorker(American):
    pass

def main():
    ## use map() to make a list whose elements are square of numbers between 1 and 20 (both included).
    #mapListSquare()

    ## class named American which has a static method called printNationality.
    ## static methods are the methods bound to the class instead of its object, 
    ## hence would not require class instance creation & aren't dependent on state of object
    # print("Once! >> Will not run if @staticmethod decorator is not specified, because the class has no instance")
    # am = American()
    # am.printNationality()

    # print("Twice! >> Will run irrespective of the presence of @staticmethod decorator")
    # American.printNationality()

    ## Define a class named American and its subclass NewYorker.
    am = American()
    ny = NewYorker()

    print(am)
    print(ny)


if __name__ == "__main__":
    main()