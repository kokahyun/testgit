class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calcPerimeter(self):
        self.calcperimeter=3.14*self.radius**2
    def calcArea(self):
        self.calcarea=3.14*2*self.radius
    def __str__(self):
        msg="반지름: "+str(self.radius)+"원의 면적: "+str(self.calcperimeter)+"원의 둘래: "+str(self.calcarea)
        return msg
myCircle=Circle(100)
myCircle.calcPerimeter()
myCircle.calcArea()
print(myCircle)
