# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def search_tree(nums, is_sorted=False, start=0, end=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
    n = end + 1 - start
    if start == end:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = n // 2  # Halfway (approx)
        mid += start
        left = search_tree(nums, True, start, mid - 1)
        right = search_tree(nums, True, mid, end)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)



tree = search_tree([15, 3, 11, 21, 7, 0, 19, 33, 29, 4])
print_tree(tree)

print()
nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
tree = search_tree(nums)
print_tree(tree)