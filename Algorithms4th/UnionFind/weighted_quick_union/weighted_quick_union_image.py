import os
from PIL import Image, ImageDraw
from weighted_quick_union import WeightedQuickUnion

class WeightedQuickUnionImage(WeightedQuickUnion):
    """docstring for WeightedQuickUnionImage"""

    def __init__(self, n):
        super(WeightedQuickUnionImage, self).__init__(n)
        self.w = 400
        self.h = 400
        self.division = self.w * 3 / 4
        self.bx = 20
        self.xs = (self.w - self.bx*2) / n
        self.xw = int(self.xs) - 1
        self.ys = self.division/n
        # 当前结点深度，绘图时使用
        self.depth = [1]*n
        self.out_path = os.path.dirname(os.path.abspath(__file__))
        self.out_path = os.path.join(self.out_path, 'out')
        if not os.path.exists(self.out_path):
            os.makedirs(self.out_path)
        self.step = 1

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        t = pRoot
        # 将小树的根节点接到大树的根节点
        if self.sz[pRoot] < self.sz[qRoot]:
            self.id[pRoot] = qRoot
            self.sz[qRoot] += self.sz[pRoot]
        else:
            self.id[qRoot] = pRoot
            self.sz[pRoot] += self.sz[qRoot]
            t = qRoot
        self.set_depth()
        self.draw_list(p, q, t)
        self.count -= 1

    def set_depth(self):
        '''
        使用遍历的方式计算深度
        '''
        n = len(self.id)
        for i in range(n):
            self.depth[i] = 1
            p = i
            while p != self.id[p]:
                p = self.id[p]
                self.depth[i] += 1

    def draw_list(self, p=-1, q=-1, pRoot=-1):
        img = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.line((0, self.division, self.w, self.division), (0, 0, 255))
        if p != -1 and q != -1:
            x1 = self.bx + self.xs*p
            y_connect = self.division + 20
            x2 = self.bx + self.xs*q
            draw.line((x1, y_connect, x2, y_connect), (0, 255, 255))

        x = self.bx
        for n, v in enumerate(self.id):
            y = self.h - 12
            draw.text((x, y), str(n), (0, 0, 0))
            if n == p or n == q:
                draw.line((x, y, x, y_connect), (0, 255, 255))
            y = self.ys * self.depth[n]
            draw.text((x, y), str(n), (0, 0, 0))
            x_id = self.bx + self.xs*v
            y_id = y - self.ys
            draw.text((x_id, y_id), str(v), (0, 0, 0))
            color = (0, 0, 0)
            if n == pRoot:
                color = (255, 0, 0)
            draw.line((x, y, x_id, y_id+12), color)
            x += self.xs

        name = str(self.step) + '.jpg'
        img.save(os.path.join(self.out_path, name), 'jpeg')
        self.step += 1

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        n = 10
        uf_image = WeightedQuickUnionImage(n)
        # 加权quick-union最坏的情况
        d_worst = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [4, 6], [0, 4]]
        for p, q in d_worst:
            if uf_image.connected(p, q):
                continue
            uf_image.union(p, q)
        print(uf_image.get_count()) 
    else:
        with open(sys.argv[1], 'r') as f:
            n = int(f.readline())
            uf = WeightedQuickUnionImage(n)
            for line in f.readlines():
                p, q = [int(x) for x in line.split()]
                if uf.connected(p, q):
                    continue
                uf.union(p, q)
            print(uf.get_count())        
