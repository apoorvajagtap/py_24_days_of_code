import random
import zlib
import time

def compDecomp(s):
    s = bytes(s, 'utf-8')
    res = zlib.compress(s)

    # res = zlib.compress(s.encode())
    print(res)
    print(zlib.decompress(res))

def calRunTime():
    start = time.time()

    for i in range(0, 100):
        x = 1 + 1
    
    end = time.time()
    print(end-start)

def shuffle(ls):
    random.shuffle(ls)
    print(ls)

def mixUp():
    subjects = ["I", "You"]
    verb = ["Play", "Love"] 
    obj = ["Hockey","Football"]

    ## ATTEMPT 1
    for i in subjects:
        for j in verb:
            for k in obj:
                print("{0} {1} {2}".format(i, j, k))

def main():
    ## randomly print a integer number between 7 and 15 inclusive.
    ## ATTEMPT 2
    # print(random.randrange(7, 16))

    ## ATTEMPT 1
    # print(int(random.uniform(7, 16)))

    ## compress and decompress the string "hello world!hello world!hello world!hello world!"
    # compDecomp("hello world!hello world!hello world!hello world!")

    ## print the running time of execution of "1+1" for 100 times.
    # calRunTime()

    ## program to shuffle and print the list [3,6,7,8].
    # shuffle([3,6,7,8])

    ## generate all sentences where subject is in ["I", "You"] 
    ## and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
    mixUp()
    

if __name__ == "__main__":
    main()