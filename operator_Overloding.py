# https://replit.com/@codewithharry/77-Day-77-Operator-Overloading#.tutorial/Tutorial.md
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # OPERATION OVERLODING
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):    # OPERATION OVERLODING
        return Point (self.x - other.x,self.y - other.y)
    
    def __mul__(self,other):    # OPERATION OVERLODING 
        return Point(self.x * other.x,self.y * other.y)
    
    # def __lt__(self,other):    # OPERATION OVERLODING 
    #     return Point(self.x < other.x,self.y < other.y)
    
    def __gt__(self,other):    # OPERATION OVERLODING 
        return Point(self.x > other.x,self.y > other.y)
    
    def __eq__(self,other):    # OPERATION OVERLODING 
        return Point(self.x == other.x,self.y == other.y)

p1 = Point(48767352,2844)
p2 = Point(48767352,4741152)
p3 = p1 + p2 
p4 = p1 - p2 
p5 = p1 * p2
p6 = p1 > p2
p7 = p1 < p2
p8 = p1 == p2
print(p3.x,p3.y)
print(p4.x,p4.y)
print(p5.x,p5.y)
print(p6.x,p6.y)
print(p7.x,p7.y)
print(p8.x,p8.y)
