class RedBlackBST():
    """docstring for RedBlackBST"""

    @property
    def RED(self):
        return True

    @property
    def BLACK(self):
        return False

    class Node():
        """docstring for Node"""

        def __init__(self, key, val, N, color):
            self.key = key
            self.val = val
            self.N = N
            self.color = color
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def isRed(self, x):
        if x is None:
            return False
        return x.color == self.RED

    def size(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return 0
        else:
            return node.N

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        x.N = h.N
        h.N = self.size(h.left) + self.size(h.right) + 1
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        x.N = h.N
        h.N = self.size(h.left) + self.size(h.right) + 1
        return x

    def flip_colors(self, h):
        h.color = self.RED
        h.left.color = self.BLACK
        h.right.color = self.BLACK

    def get(self, key):
        return self.get_node(key, self.root)

    def get_node(self, key, node):
        if node is None:
            return None
        if key < node.key:
            return self.get_node(key, node.left)
        elif key > node.key:
            return self.get_node(key, node.right)
        else:
            return node.val

    def put(self, key, val):
        self.root = self.put_node(self.root, key, val)
        self.root.color = self.BLACK

    def put_node(self, h, key, val):
        if h is None:
            return self.Node(key, val, 1, self.RED)
        if key < h.key:
            h.left = self.put_node(h.left, key, val)
        elif key > h.key:
            h.right = self.put_node(h.right, key, val)
        else:
            h.val = val

        if self.isRed(h.right) and not self.isRed(h.left):
            h = self.rotate_left(h)
        if self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotate_right(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flip_colors(h)

        h.N = self.size(h.left) + self.size(h.right) + 1
        return h
