def computeIndefinite():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("Why on earth you are dividing a number by ZERO!!")
    except:
        print("Other exception occured")

class CustomException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)

def printUsername(em):
    print(em.split('@')[0])

def main():
    ## function to compute 5/0 and use try/except to catch the exceptions.
    #computeIndefinite()

    ## Custom Exception class which takes a string message as attribute.
    #raise CustomException(input("Enter the string: "))

    ## Assuming that we have some email addresses in the "username@companyname.com" format, 
    ## please write program to print the user name of a given email address. 
    ## Both user names and company names are composed of letters only.
    printUsername(input("Ennter the email address: "))

if __name__ == "__main__":
    main()