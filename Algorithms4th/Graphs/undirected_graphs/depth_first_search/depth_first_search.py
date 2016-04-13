import sys
import os
_libpath = os.path.dirname(os.path.abspath(__file__))
_libpath = os.path.dirname(_libpath)
_libpath = os.path.join(_libpath, 'graph')
sys.path.append(_libpath)
from graph import Graph


class DepthFirstSearch():

    def __init__(self, G, s):
        self._marked = [False] * G.V()
        self._count = 0
        self._dfs(G, s)

    def _dfs(self, G, v):
        self._marked[v] = True
        self._count += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)

    def marked(self, w):
        return self._marked[w]

    def count(self):
        return self._count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No input file')
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as f:
            V = int(f.readline())
            E = int(f.readline())
            graph = Graph(V)
            for i in range(E):
                v, w = [int(x) for x in f.readline().split()]
                graph.add_edge(v, w)
            print(graph)
            search = DepthFirstSearch(graph, 0)
            print(search.count())

