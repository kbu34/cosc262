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
    
def is_ccw(a, b, c):
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    return area > 0
    
def intersecting(a, b, c, d):
    """True iff line segment ab intersects cd"""
    # 1. Check if points c & d are on opposite sides of the line ab
    condition1 = is_ccw(a, d, b) == is_ccw(a, b, c)
    
    #2. Check if points a & b are on opposite sides of the line cd
    condition2 = is_ccw(c, a, d) == is_ccw(c, d, b)
    return condition1 and condition2

def is_strictly_convex(vertices):
    """Return True iff the given vertices define a strictly convex polygon
       with all vertices in counter-clockwise order. The function returns
       false if there are fewer than 3 vertices or if any interior angle is
       less than 180 degrees or the vertices are not in counter-clockwise
       order
    """
    if len(vertices) < 3:
        return False
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        c = vertices[(i + 2) % len(vertices)]
        if not is_ccw(a, b, c):
            return False
    return True

verts = [
    (0, 0),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))