class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

