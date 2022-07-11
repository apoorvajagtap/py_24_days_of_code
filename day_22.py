from itertools import permutations

def countChars(s):
    res = {}
    for c in s.lower():
        if c in res.keys():
            res[c] += 1
        else:
            res[c] = 1

    for k in res:
        print("{0}, {1}".format(k, res[k]))

def reverseStr(s):
    res = ""
    ## ATTEMPT 2
    res = reversed(s)
    print(''.join(list(res)))

    ## ATTEMPT 1
    # for i in range(len(s), 0, -1):
    #     res += s[i-1]
    # print(res)
    
def evenIdxChar(s):
    ## ATTEMPT 2
    print(''.join([s[i] for i in range(len(s)) if i%2==0]))

    ## ATTEMPT 1
    # res = []
    # for i in range(len(s)):
    #     if i%2 == 0:
    #         res.append(s[i])

    # print(''.join(res))

def main():
    ## count and print the numbers of each character in a string input by console.
    # countChars(input("Enter the string: "))

    ## accepts a string from console and print it in reverse order.
    # reverseStr(input("Enter the string: "))

    ## accepts a string from console and print the characters that have even indexes.
    # evenIdxChar(input("Enter the string: "))

    ## which prints all permutations of [1,2,3]
    print(list(permutations([1,2,3])))

    ## Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
    ## How many rabbits and how many chickens do we have?
    #### skipping due to algo for now

if __name__ == "__main__":
    main()