from numpy import add


class point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def move(self):
        print("Move")

    def draw():
        print("Draw")
    
    def add(self):
        return self.x+self.y

point=point(10,20)
print(point.add())