#liskov substituion principle
#The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program
class rectangle():
    def __init__(self, width, height):
        self._height = height
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(F'Expected an area of {expected}, got {rc.area}')

rc = rectangle(2,3)
use_it(rc)

class square(rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    @rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

sq = square(5)
use_it(sq)

# Use boolean to check if it is square. setters violates lsp in square