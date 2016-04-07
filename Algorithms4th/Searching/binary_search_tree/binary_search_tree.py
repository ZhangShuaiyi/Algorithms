class BST():
    """二叉查找树"""

    class Node():
        """节点"""

        def __init__(self, key, val, n, left=None, right=None):
            self.key = key
            self.val = val
            self.N = n
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def size(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return 0
        else:
            return node.N

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
        self.root = self.put_node(key, val, self.root)

    def put_node(self, key, val, node):
        if node is None:
            return self.Node(key, val, 1)
        if key < node.key:
            node.left = self.put_node(key, val, node.left)
        elif key > node.key:
            node.right = self.put_node(key, val, node.right)
        else:
            node.val = val
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def min(self):
        return self.min_node(self.root).key

    def min_node(self, node):
        if node.left is None:
            return node
        return self.min_node(node.left)

    def delete_min(self):
        self.root = self.delete_min_node(self.root)

    def delete_min_node(self, node):
        if node.left is None:
            return node.right
        node.left = self.delete_min_node(node.left)
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            node = self.min_node(t.right)
            node.right = self.delete_min_node(t.right)
            node.left = t.left
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node
