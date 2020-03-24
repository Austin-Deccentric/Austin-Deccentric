import math
'''
Implemented an OOP solution to getting the Area of a circle. I was able to implement some sort of user input validation.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius * self.radius

if __name__ == "__main__":
    while True:
        r = input("Enter the radius of the circle: ")
        try:
             r = float(r)
        except ValueError :
            print('Please input a number')
            continue
        if r < 1:
            print("Radius should be positive")
        else:
            break
        
    obj_1 = Circle(r)
    print("The area of the circle is %.2f" % obj_1.Area())
            
