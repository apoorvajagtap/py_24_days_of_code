def computeN(num):
    if num == 0:
        return 0
    else:
        return computeN(num-1) + 100

def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
        
def fiboSeries(num):
    # res = []
    a, b = 0, 1
    print(a, end=', ')
    print(b, end=', ')
    for i in range(num-1):
        c = a + b
        print(c, end=', ')
        a = b
        b = c

def genP(num):
    for i in range(0, num+1, 2):
        if i%2 == 0:
            yield i

def main():
    ## program to compute f(n)=f(n-1)+100 when n>0 && f(0)=0
    # print(computeN(int(input("Enter the number: "))))

    ## specific location in fibonacci series
    # print(fibo(int(input("Enter the number: "))))

    ## print fibonacci series upto n
    # fiboSeries(int(input("Enter the number: ")))

    ## use generator to print the even numbers between 0 and n in comma separated form
    num = int(input("Enter the number: "))
    res = []
    for itr in genP(num):
        res.append(itr)

    print(', '.join([str(i) for i in res]))

if __name__ == "__main__":
    main()