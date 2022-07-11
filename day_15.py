import re

def printCompanyName(email):
    for ele in email:
        print((ele.split('@')[-1]).split('.')[0])

def digitsOnly(sent):
    ## ATTEMPT 2
    res = re.findall("\d", sent)
    print(res)

    ## ATTEMPT 1
    # res = []
    # sent = sent.split()
    # for ele in sent:
    #     for c in ele:
    #         if 48 <= ord(c) <= 57:
    #             res.append(c)

    # print(res)

def unicodeStr():
    res = u"hello world!"
    print(res)

def asciiUni(sent):
    sent = sent.encode('utf-8')
    print(sent)

def computeFormula(num):
    res = 0.0
    for i in range(1,num+1):
        res += i/(i+1)

    print(round(res, 2))

def main():
    ## print the company name of a given email address.
    # printCompanyName(input("Enter the email address: "))

    ## accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
    # digitsOnly(input("Enter the sentence: "))

    ## Print a unicode string "hello world".
    # unicodeStr()

    ## read an ASCII string and to convert it to a unicode string encoded by utf-8.
    # asciiUni(input("Enter the string: "))

    ## special comment to indicate a Python source code file is in unicode.
    # -*- coding: utf-8 -*-

    ## compute 1/2+2/3+3/4+...+n/n+1
    computeFormula(int(input("Enter the number: ")))

if __name__ == "__main__":
    main()