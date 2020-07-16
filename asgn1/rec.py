class Point:  # Point class for x and y coordinates

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:  # rectangle class
    def __init__(self, bottomLeftCorner, topRightcorner):
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightcorner = topRightcorner

        self.height = topRightcorner.y - bottomLeftCorner.y  # find the height
        self.width = topRightcorner.x - bottomLeftCorner.x  # find the width
        self.area = self.height * self.width  # calculate the area
        self.perimeter = 2 * (self.height + self.width)  # calculate the perimeter

    def intersect(bLC_1, tRC_1, bLC_2, tRC_2):  # this function is used to determine if the rectangles intersect

        return not (tRC_1.x < bLC_2.x or bLC_1.x > tRC_2.x or tRC_1.y < bLC_2.y or bLC_1.y > tRC_2.y)


rect = Rectangle(Point(1, 1), Point(4, 5))  # create objects of the rectangle class
print("The area is", rect.area)  # print calculated area
print("The perimeter is", rect.perimeter)  # print calculated perimiter
print("---------------------------------------")

print("From the top, moving left to right i will use the illustrations as the test cases")
print("---------------------------------------")
print("(1)")
rectA = Rectangle(Point(1, 4), Point(5, 7))
rectB = Rectangle(Point(4, 3), Point(8, 6))
# check if they intersect.

print(Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner))

print("---------------------------------------")
print("(2)")
rectA = Rectangle(Point(0, 1), Point(5, 5))
rectB = Rectangle(Point(4, 2), Point(7, 4))
# check if they intersect.

print(Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner))

print("---------------------------------------")
print("(3)")
rectA = Rectangle(Point(1, 2), Point(6, 6))
rectB = Rectangle(Point(2, 3), Point(5, 5))
# check if they intersect.

print(Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner))

print("---------------------------------------")
print("(4)")
rectA = Rectangle(Point(2, 2), Point(6, 6))
rectB = Rectangle(Point(1, 1), Point(4, 3))
# check if they intersect.

print(Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner))

print("---------------------------------------")
print("(5)")
rectA = Rectangle(Point(1, 2), Point(5, 5))
rectB = Rectangle(Point(6, 1), Point(9, 4))
# check if they intersect.

print(Rectangle.intersect(rectA.bottomLeftCorner, rectA.topRightcorner, rectB.bottomLeftCorner, rectB.topRightcorner))
