import heapq

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count
       and left and right subtrees, assumed to be the '0' and '1' children
       respectively.
    """
    def __init__(self, count, left, right):
        self.count = count
        self.left = left
        self.right = right

    def __str__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__str__(level + 1) + ',\n' +
            self.right.__str__(level + 1) + ')')

    def is_leaf(self):
        return False
    
    def __eq__(self, other):
        return self.count == other.count
    
    def __lt__(self, other):
        if self.count == other.count and isinstance(other, Leaf):
            return True
        else:
            return self.count < other.count
    
    def __gt__(self, other):
        if self.count == other.count and isinstance(other, Leaf):
            return False
        else:
            return self.count > other.count 

class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __str__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True
    
    def __eq__(self, other):
        return self.count == other.count
    
    def __lt__(self, other):
        if self.count == other.count and isinstance(other, Node):
            return False
        elif self.count == other.count:
            return self.char < other.char
        else:
            return self.count < other.count
            
    def __gt__(self, other):
        if self.count == other.count and isinstance(other, Node):
            return False
        elif self.count == other.count:
            return self.char > other.char
        else:
            return self.count > other.count
    
def finding(tree, all, def_code):
    if not tree.is_leaf():
        def_code += '0'
        finding(tree.left, all, def_code)
        def_code = def_code[:-1]
        def_code += '1'
        finding(tree.right, all, def_code)
    elif tree.is_leaf():
        all.append((tree.char, def_code))
        
def huffman_encode(s, tree):
    code = ''
    all = []
    def_code = ''
    finding(tree, all, def_code)
    bi_string = [char for char in s]
    for st in bi_string:
        for a in all:
            char, def_code = a
            if char == st:
                code += def_code
    return code

def decoding(tree, string_list, count):
    while not tree.is_leaf():
        if string_list[count] == '0':
            tree = tree.left
        else:
            tree = tree.right
        count += 1
    return tree.char, count

def huffman_decode(s, tree):
    decoded_str = ''
    string_list = [char for char in s]
    count = 0
    while count < len(string_list):
        decoded, count = decoding(tree, string_list, count)
        decoded_str += decoded
    return decoded_str

def huffman_tree(frequencies):
    leaf_list = []
    heap = []
    for key, item in frequencies.items():
        new_leaf = Leaf(item, key)
        leaf_list.append(new_leaf)
    for leaf in leaf_list:
        heapq.heappush(heap, leaf)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap) 
        c = Node(a.count+b.count, a, b)
        heapq.heappush(heap, c)
    return heap[0]

# The example from the lecture notes
"""tree = Node(42,
  Node(17,
    Leaf(8, 'b'),
    Leaf(9, 'a')),
  Node(25,
    Node(10,
      Node(5,
        Leaf(2, 'f'),
        Leaf(3, 'd')),
      Leaf(5, 'e')),
    Leaf(15, 'c')))
print(huffman_encode('adcb', tree))"""
            
# The example from the lecture notes
"""tree = Node(42,
  Node(17,
    Leaf(8, 'b'),
    Leaf(9, 'a')),
  Node(25,
    Node(10,
      Node(5,
        Leaf(2, 'f'),
        Leaf(3, 'd')),
      Leaf(5, 'e')),
    Leaf(15, 'c')))
print(huffman_decode('0110011100', tree))"""

# The example from the notes
freqs = {'a': 9,
         'b': 8,
         'c': 15,
         'd': 3,
         'e': 5,
         'f': 2}
print(huffman_tree(freqs))