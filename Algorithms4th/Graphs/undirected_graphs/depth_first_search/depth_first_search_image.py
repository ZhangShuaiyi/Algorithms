from random import randint
from PIL import Image, ImageDraw
import sys
import os
_libpath = os.path.dirname(os.path.abspath(__file__))
_libpath = os.path.dirname(_libpath)
_libpath = os.path.join(_libpath, 'graph')
sys.path.append(_libpath)
from graph import Graph
from depth_first_search import DepthFirstSearch

class DepthFirstSearchImage(DepthFirstSearch):

    def __init__(self, G, s):
        self.w = 400
        self.h = 400
        b = 20
        v = G.V()
        self.G = G
        pw = (self.w + self.h - b * 4) // v
        hg = self.h - b*2
        wg = self.w - b*2
        self.xy = []
        for i in range(v):
            t = i * pw
            mi = 0 if t < hg else t - hg
            ma = t if t < wg else wg

            x = randint(mi, ma)
            y = t - x
            x += b
            y += b
            print(x, y)
            self.xy.append((x, y))
        out_path = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(out_path, 'out')
        self.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        self.step = 1
        super(DepthFirstSearchImage, self).__init__(G, s)

    def draw_graph(self):
        image = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        for i in range(self.G.V()):
            draw.text(self.xy[i], str(i), (0, 0, 0))
        for v in range(self.G.V()):
            for w in self.G.adj(v):
                pv = self.xy[v]
                pw = self.xy[w]
                if self._marked[w] and self._marked[v]:
                    draw.line((pv, pw), (255, 0, 0))
                else:
                    draw.line((pv, pw), (0, 0, 0))
        name = os.path.join(self.out_path, str(self.step) + 'jpg')
        image.save(name, 'jpeg')
        self.step += 1

    def _dfs(self, G, v):
        self._marked[v] = True
        self.draw_graph()
        self._count += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)

if __name__ == '__main__':
    import sys
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
            search = DepthFirstSearchImage(graph, 0)
            print(search.count())


