class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    def __le__(self, other):
        return self.x <= other.x or self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x or self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x or self.y >= other.y
