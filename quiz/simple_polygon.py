class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __lt__(self, other):
        """For convenience we define '<' to mean
           "less than with respect to angle", i.e.
           the direction of self is less than the
           direction of other in a CCW sense."""
        area = self.x * other.y - other.x * self.y
        return area > 0
        
def simple_polygon(points):
    """Return the given list of points ordered so that connecting them in order
       yields a simple polygon"""
       
    # Firstly swap the bottommost (and if necessary leftmost) point to the
    # 0th position in the list. The first line finds the bottommost point,
    # and the next line finds its index, so it can be swapped to the front.
    bottommost = min(points, key=lambda p: (p.y, p.x))
    index = points.index(bottommost)
    points[0], points[index] = points[index], points[0]
    
    # Now just sort the rest by angle from points[0]
    rest = points[1:]
    rest.sort(key=lambda x: points[0] - x) 
    return [points[0]] + rest

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = simple_polygon(points)
for v in verts:
    print(v)

print()
points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = simple_polygon(points)
for v in verts:
    print(v)
    
print()

import matplotlib.pyplot as plt

def plot_poly(points):
    """Plot the given set of points as a closed polygon"""
    plt.plot([v.x for v in points + [points[0]]], [v.y for v in points + [points[0]]])
    plt.show()
    
import random
random.seed(6543)
def rand_pt():
    vx = int(1000 * random.random())
    vy = int(1000 * random.random())
    return Vec(vx, vy)

points = [rand_pt() for _ in range(30)]
verts = simple_polygon(points)
for v in verts:
    print(v)
plot_poly(verts)