from cv2 import rectangle


class Circle:
    def __init__(self, r):
        self.radius = r

    def computeArea(self):
        area = self.radius**2 * 3.14
        print(area)

class Rectange:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def computeArea(self):
        return (self.length * self.width)

class Shape:
    def __init__(self) -> None:
        pass

    def computeArea(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def computeArea(self):
        return(self.length ** 2)

def main():
    ## class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
    # radius = int(input("Enter the radius: "))
    # ca = Circle(radius)
    # ca.computeArea()

    ## class named Rectangle which can be constructed by a length and width.
    ## The Rectangle class has a method which can compute the area.
    # length, width = input("Enter the length & width: ").split(',')
    # rec = Rectange(int(length), int(width))
    # print(rec.computeArea())

    ## class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
    ## Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
    # sqr = Square(5)
    # print(sqr.computeArea())

    # print(Square().computeArea())

    ## Raise runtime error exception
    raise RuntimeError("here we go!!")


if __name__ == "__main__":
    main()