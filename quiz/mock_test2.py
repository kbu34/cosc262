class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
    
    def __repr__(self):
        return f"Vec({self.x}, {self.y})"
    

def closest_pair(points_in):
    """Return the two closest points in the given point set.
       Precondition: points has a length >= 2.
       The return value is a tuple of two points of type Vec, sorted by
       their x values and then, if they are equal, their y values.
    """
    points = sorted(points_in, key=lambda p: (p.x, p.y))  # Point list acts as event queue
    solution = (points[0], points[1])      # Current best point pair
    d_sq = (points[1] - points[0]).lensq() # Current best point-pair distance squared

    # Construct the frontier list, which in this implementation is just a simple
    # unsorted list.
    # **** Insert some code here to create the initial frontier list with
    # **** the first two elements of the sorted point list.
    frontier = [points[0], points[1]]
    # Now sweep the line across the point set, starting with points[2]
    i = 2
    while d_sq > 0 and i < len(points):
        p = points[i]
        # Remove points that no longer belong in the frontier. Since the
        # frontier isn't being kept sorted in this implementation, a o(n)
        # removal cost is OK.
        # **** Insert code here
        for front in frontier:
            if (p.x - front.x) ** 2 > d_sq:
                frontier.remove(front)
        # Check all points within the frontier set (NB: we're not keeping the
        # frontier set sorted in y so have to check all points).
        # *** Insert code here.
        for front in frontier:
            if (p.y - front.y) ** 2 < d_sq:
                d_sq = (p - front).lensq()
                solution = (front, p)
        frontier.append(p)
        i += 1
        
    return tuple(sorted(solution, key=lambda p: (p.x, p.y)))


# Now a test with 10,000 points.
from random import random, seed
N = 10000
SIZE = 1000000
seed(12345)
points = [Vec(int(SIZE * random()), int(SIZE * random())) for _ in range(N)]
print(closest_pair(points))