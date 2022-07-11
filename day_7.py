from audioop import mul
import math


class multipleSeven:
    def sevenMultipleGen(self, n):
        for i in range(n+1):
            if i%7 == 0:
                yield i

def euclideanDist():
    start, end = (0, 0), [0, 0]
    direction = {}
    print("Enter the directions: ")
    for i in range(4):
        tempList = input().split()
        direction[tempList[0]] = int(tempList[1])

    for key in direction:
        if key == "UP":
            end[1] += direction[key]
        elif key == "DOWN":
            end[1] -= direction[key]
        elif key == "LEFT":
            end[0] -= direction[key]
        elif key == "RIGHT":
            end[0] += direction[key]

    result = round(math.sqrt(math.pow(end[0]-start[0], 2) + math.pow(end[1]-start[1], 2)))
    print(result)
 
def main():
    ## clas with generators to iterate multiples of 7 from 0 to n
    # ob = multipleSeven()
    # val = ob.sevenMultipleGen(int(input("Enter the range: ")))

    # for ele in val:
    #     print(ele)

    ## Find euclidean distance from (0,0) as instructed
    euclideanDist()

if __name__ == "__main__":
    main()