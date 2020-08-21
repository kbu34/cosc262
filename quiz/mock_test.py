class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
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
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise or degenerate"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    return area > 0 

def is_strictly_convex(vertices):
    if len(vertices) < 3:
        return False
    count = 0
    while count < len(vertices)-2:
        if not is_ccw(vertices[count], vertices[count+1], vertices[count+2]):
            return False
        count += 1
    if not is_ccw(vertices[-1], vertices[0], vertices[1]):
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

verts = [
    (0, 0),
    (100, 0),
    (50, 50),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

# Insufficient points #1
verts = [
    (0, 0),
    (10, 10)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (60, 60),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))