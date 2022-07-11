import random

def randomEven(ls):
    ## ATTEMPT 2
    print(random.choice([i for i in ls if i%2==0]))

    ## ATTEMPT 1
    # res = [i for i in ls if i%2 == 0]
    # print(random.choice(res))

def main():
    ## output a random even number between 0 and 10 inclusive using random module and list comprehension.
    # randomEven([0,1,2,3,4,5,6,7,8,9,10])

    ## output a random number, which is divisible by 5 and 7, 
    ## between 10 and 150 inclusive using random module and list comprehension.
    # print(random.choice([i for i in range(10, 151) if i%5==0 and i%7==0]))

    ## generate a list with 5 random numbers between 100 and 200 inclusive.
    # print(random.choices(range(100,201), k=5))

    ## randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    # print(random.choices([i for i in range(100,201) if i%2==0], k=5))

    ## randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
    print(random.choices([i for i in range(100,1001) if i%35==0], k=5))         ## another approach for multiple of 5 & 7

if __name__ == "__main__":
    main()