def eliminateEven(ls):
    ## ATTEMPT 2
    print(', '.join([str(i) for i in list(filter(lambda x: x%2!=0, ls))]))

    ## ATTEMPT 1
    # print(', '.join([str(i) for i in ls if i%2!=0]))

def main():
    ## print the list after removing even numbers in [5,6,77,45,22,12,24]
    # eliminateEven([5,6,77,45,22,12,24])

    ## print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
    # print(', '.join([str(i) for i in [12,24,35,70,88,120,155] if i%5==0 and i%7==0]))

    ## print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
    # ls = [12,24,35,70,88,120,155]
    # print([ls[i] for i in range(len(ls)) if i%2!=0])

    ## print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
    ## skipping for later practice

    ## write a program generate a 3*5*8 3D array whose each element is 0.
    # for i in range(3):
    #     for j in range(5):
    #         for k in range(8):
    #             print(0, end=" ")
    #         print(" ")
    #     print(" ")

    arr = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
    print(arr)

if __name__ == "__main__":
    main()