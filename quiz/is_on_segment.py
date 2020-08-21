class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        

def is_on_segment(p, a, b):
    """True iff p lies on the line segment from a to b"""
    v1 = a - p
    v2 = b - p
    area = v1.x * v2.y - v1.y * v2.x # Two times area of triangle pab.
    if area == 0:
        seg_len_sq = (b - a).lensq()
        if (p - a).lensq() <= seg_len_sq and (b - p).lensq() <= seg_len_sq:  # ** FIXME **
            return True
    return False

a = Vec(1000, 2000)
b = Vec(0, 0)
p = Vec(500, 1000)
print(is_on_segment(p, a, b))
print()

a = Vec(0, 0)
b = Vec(1000, 2000)
point_tuples = [
    (-1, -1),
    (-1, -2),
    (-1000, -2000),
    (0, 0),
    (1, 2),
    (500, 1000),
    (500, 1001),
    (500, 999),
    (1000, 2000),
    (1001, 2001),
    (1001, 2002),
    (2000, 4000)]
points = [Vec(p[0], p[1]) for p in point_tuples]
for p in points:
    print(p, is_on_segment(p, a, b))