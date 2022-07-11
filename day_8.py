from collections import Counter

def computeFrequency():
    sent = input("Enter the sentence: ").split()
    freq = {}

    ## ATTEMPT 2
    sent = Counter(sent)
    for ele in sorted(sent.items()):
        print("{0}: {1}".format(ele[0], ele[1]))

    ## ATTEMPT 1
    # for ele in sent:
    #     try:
    #         freq[ele] += 1  
    #     except KeyError:
    #         freq[ele] = 1

    # for key in freq:
    #     print("{0}:{1}".format(key, freq[key]))

def square(num):
    return num**2

class Example:
    name = "ABC"

    def __init__(self, name = None):
        self.name = name.upper()


def main():
    ##  count occurences of each word
    #computeFrequency()

    ## Calculate square value of a number
    #print(square(int(input("Enter the number: "))))

    ## skipping que_24

    ## sameClassInstance parameter
    var = Example(input("Enter the name to be printed in Caps: "))
    print(var.name, " ======== ", Example.name)

if __name__ == "__main__":
    main()