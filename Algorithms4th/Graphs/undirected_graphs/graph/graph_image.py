import os
from random import randint
from PIL import Image, ImageDraw
from graph import Graph


class GraphImage(Graph):
    """docstring for GraphImage"""

    def __init__(self, v):
        super(GraphImage, self).__init__(v)
        self.w = 400
        self.h = 400
        b = 20
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

    def draw_graph(self):
        image = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        for i in range(self.V()):
            draw.text(self.xy[i], str(i), (0, 0, 0))
        for v in range(self.V()):
            for w in self.adj(v):
                pv = self.xy[v]
                pw = self.xy[w]
                draw.line((pv, pw), (0, 0, 0))
        name = os.path.join(self.out_path, 'test.jpg')
        image.save(name, 'jpeg')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Need input file!')
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        V = int(f.readline())
        E = int(f.readline())
        graph = GraphImage(V)
        for i in range(E):
            v, w = [int(x) for x in f.readline().split()]
            graph.add_edge(v, w)
        print(graph)
        graph.draw_graph()
