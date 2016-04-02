class UF():
    """docstring for UF"""

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))

    def get_count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        raise NotImplementedError("Should have implemented this")

    def union(self, p, q):
        raise NotImplementedError("Should have implemented this")
