# Class should Open for extension but closed for modification
from enum import Enum

class color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
    
    # Modification should be done via extension eg: filter_by_color_and_size
    # 2 --> 3
    # 3 --> 7 C S W CS SW CW CSW

class specification:
    def is_satisfied(self, item):
        pass

class filter:
    def filter(self, item, specification):
        pass

class color_specification(specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
    
class size_specification(specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class better_filter(filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

apple = Product("apple", color.GREEN,size.SMALL)
tree = Product("tree", color.GREEN, size.LARGE)
house = Product("house", color.BLUE, size.LARGE)

products = [apple,tree, house]
print("Green Products")
pf = ProductFilter()
for p in pf.filter_by_color(products,color.GREEN):
    print(f"- {p.name}  is green")

bf = better_filter()
green = color_specification(color.GREEN)
for p in bf.filter(products, green):
    print(f"- {p.name}  is green")

large = size_specification(size.LARGE)
for p in bf.filter(products, large):
    print(f"- {p.name}  is large")

class and_specification(specification):
    def __init__(self, *args):
        self.args = args
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

print("Large blue items")
large_blue = and_specification(large,color_specification(color.BLUE))
for p in bf.filter(products, large_blue):
    print(f"- {p.name}  is large and blue")