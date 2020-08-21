import matplotlib.pyplot as plt
import math

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)
        
    
class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25    
    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for root), used during recursion, and the
           maximum depth allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points.sort(key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or on the 
           boundary of the given query rectangle, which is defined by a pair of points
           (bottom_left, top_right).
        """
        bottom_left, top_right = query_rectangle
        if self.is_leaf is True:
            self.matches = []
            for point in self.points:
                if point.in_box(bottom_left, top_right) is True:
                    self.matches.append(point)
        else:
            self.matches = []
            lb_rectangle = False
            rt_rectangle = False
            if self.axis == 0:
                if (self.coord >= bottom_left.x and self.coord <= top_right.x) or self.coord == bottom_left.x:
                    lb_rectangle = True
                    rt_rectangle = True
                elif self.coord > bottom_left.x:
                    lb_rectangle = True 
                elif self.coord < bottom_left.x:
                    rt_rectangle = True   
            else:
                if (self.coord >= bottom_left.y and self.coord <= top_right.y) or self.coord == bottom_left.y:
                    lb_rectangle = True
                    rt_rectangle = True
                elif self.coord > bottom_left.y:
                    lb_rectangle = True 
                elif self.coord < bottom_left.y:
                    rt_rectangle = True                   
            if self.leftorbottom is not None and lb_rectangle:
                self.matches += self.leftorbottom.points_in_range(query_rectangle)
            if self.rightortop is not None and rt_rectangle:
                self.matches += self.rightortop.points_in_range(query_rectangle)
        return self.matches
    
    def nearest_point(self, p):
        """Return the nearest point"""
        current = self
        while current.is_leaf is False:
            if current.axis == 0:
                if p.x >= current.coord:
                    current = current.rightortop
                else:
                    current = current.leftorbottom
            else:
                if p.y >= current.coord:
                    current = current.rightortop
                else:
                    current = current.leftorbottom
        d = float('inf')
        for point in current.points:
            distance = math.sqrt(((point.x - p.x) ** 2) + ((point.y - p.y) ** 2))
            if distance < d:
                d = distance
        candidates = self.points_in_range((Vec(p.x - d, p.y - d), Vec(p.x + d, p.y + d)))
        shortest = candidates[0]
        shortest_dis = math.sqrt(((shortest.x - p.x) ** 2) + ((shortest.y - p.y) ** 2))
        for candidate in candidates:
            distance = math.sqrt(((candidate.x - p.x) ** 2) + ((candidate.y - p.y) ** 2))
            if distance < shortest_dis:
                shortest = candidate
                shortest_dis = distance
        return shortest
    
    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot; top, right, bottom, left are the x or y coordinates
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                    xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    
    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s
        
def main():
    point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
    points = [Vec(*tup) for tup in point_tuples]
    tree = KdTree(points)
    print(tree)
    axes = plt.axes()
    tree.plot(axes, 25, 35, 0, 0)
    plt.show()
    
"""point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
print(sorted(in_range))

	
point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
in_range = tree.points_in_range((Vec(5, 19), Vec(10, 20)))
print(sorted(in_range))

import random
random.seed(1234567)
Vec.box_calls = 0
point_tuples = [(int(10000 * random.random()), int(10000 * random.random())) for i in range(50000)]
points = [Vec(*p) for p in point_tuples]
tree = KdTree(points, max_depth=20)
in_range = tree.points_in_range((Vec(5, 19), Vec(100, 151)))
print(sorted(in_range))
if 6 <= Vec.box_calls <= 10:
    print("Plausible number of in_box calls")
else:
    print("Implausible number of in_box calls ({})".format(Vec.box_calls))"""

point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
p = Vec(6, 15)
print(f"Nearest point to {p} is {tree.nearest_point(p)}")