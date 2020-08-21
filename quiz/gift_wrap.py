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
        
def is_ccw(p0, p1, p2):
    """True if triangle p0, p1, p2 has vertices in counter-clockwise order"""
    return (p1 - p0) < (p2 - p0)
    
        
def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None or not is_ccw(hull[-1], candidate, p):
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]
verts = gift_wrap(points)
for v in verts:
    print(v)
    
print()
points = [
    Vec(1, 1),
    Vec(99, 1),
    Vec(100, 100),
    Vec(99, 99),
    Vec(0, 100),
    Vec(100, 0),
    Vec(1, 99),
    Vec(0, 0),
    Vec(50, 50)]
verts = gift_wrap(points)
for v in verts:
    print(v)