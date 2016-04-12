class Graph():
    '''
    无向图
    '''

    def __init__(self, v):
        self._V = v
        self._E = 0
        self._adj = [0] * v
        for i in range(v):
            self._adj[i] = []

    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def __repr__(self):
        s = str.format("%d vertices, %d edges\n" % (self._V, self._E))
        for v in range(self._V):
            s += str.format("%d: " % (v))
            for w in self.adj(v):
                s += str.format("%d " % (w))
            s += "\n"
        return s

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Need input file!')
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        V = int(f.readline())
        E = int(f.readline())
        graph = Graph(V)
        for i in range(E):
            v, w = [int(x) for x in f.readline().split()]
            graph.add_edge(v, w)
        print(graph)
