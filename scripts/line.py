from scripts.point import Point

class Line:
    def __init__(self, point, slope="infinity"):
        self.x = point.x
        self.y = point.y
        self.slope = slope
    
    # must not have same x value
    @classmethod
    def frompoints(cls, point1, point2):
        slope = (point2.y - point1.y) / (point2.x - point1.x)
        return cls(point1, slope)
    
    @classmethod
    def fromcoords(cls, x, y, slope):
        point = Point(x, y)
        return cls(point, slope)
    
    @classmethod
    def verticalline(cls, x):
        point = Point(x, 0)
        return cls(point)
    
    def intersection(self, other):
        if self.slope != other.slope:
            if self.slope == "infinity":
                intersection_x = self.x
                intersection_y = other.slope * (intersection_x - other.x) + other.y
            elif other.slope == "infinity":
                intersection_x = other.x
                intersection_y = self.slope * (intersection_x - self.x) + self.y
            else:
                intersection_x = ((other.slope * other.x - self.slope * self.x) - (other.y - self.y)) / (other.slope - self.slope)
                intersection_y = self.slope * (intersection_x - self.x) + self.y
            return Point(intersection_x, intersection_y)
        print("slopes are equal")

    def perplineatpoint(self, point):
        return Line(point, (-1/self.slope))
    
    def pointdistfromline(self, point):
        if self.slope == "infinity":
            return abs(self.x - point.x)
        elif self.slope == 0:
            return abs(self.y - point.y)
        perpline = self.perplineatpoint(point)
        intersection = self.intersection(perpline)
        distance = point.distance(intersection)
        return distance

    def __repr__(self):
        return f"Line.fromcoords({self.x}, {self.y}, {self.slope})"
