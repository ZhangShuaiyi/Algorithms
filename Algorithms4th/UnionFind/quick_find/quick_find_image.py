import os
from PIL import Image, ImageDraw
from quick_find import QuickFind

class QuickFindImage(QuickFind):
    """docstring for QuickFindImage"""

    def __init__(self, n):
        super(QuickFindImage, self).__init__(n)
        self.w = 400
        self.h = 400
        self.division = self.w * 3 / 4
        self.bx = 20
        self.xs = (self.w - self.bx*2) / n
        self.xw = int(self.xs) - 1
        self.out_path = os.path.dirname(os.path.abspath(__file__))
        self.out_path = os.path.join(self.out_path, 'out')
        if not os.path.exists(self.out_path):
            os.makedirs(self.out_path)
        self.step = 1

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return
        for i, v in enumerate(self.id):
            if v == pID:
                self.id[i] = qID
                self.draw_list(p, q, i)
        self.count -= 1

    def draw_list(self, p=-1, q=-1, i=-1):
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
            y = self.division - 12
            draw.text((x, y), str(n), (0, 0, 0))
            x_id = self.bx + self.xs*v
            y_id = 30
            draw.text((x_id, y_id), str(v), (0, 0, 0))
            color = (0, 0, 0)
            if n == i:
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
        qf_image = QuickFindImage(n)
        qf_image.draw_list(1, 2)
    else:
        with open(sys.argv[1], 'r') as f:
            n = int(f.readline())
            uf = QuickFindImage(n)
            for line in f.readlines():
                p, q = [int(x) for x in line.split()]
                if uf.connected(p, q):
                    continue
                uf.union(p, q)
            print(uf.get_count())
