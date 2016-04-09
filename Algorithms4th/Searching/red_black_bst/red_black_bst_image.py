import os
from PIL import Image, ImageDraw
from red_black_bst import RedBlackBST


class BSTImage(RedBlackBST):
    """docstring for BSTImage"""

    def __init__(self, n=10):
        super(BSTImage, self).__init__()
        self.w = 600
        self.h = 400
        self.by = 40
        self.ys = (self.h - self.by) / n
        self.step = 1
        out_path = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(out_path, 'out')
        self.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def put(self, key, val):
        super(BSTImage, self).put(key, val)
        self.draw_tree(key)

    def draw_tree(self, key=None):
        if self.root is None:
            return
        # 新建一个白色背景图片
        img = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = self.w / 2
        ws = x / 2
        y = 10
        if self.isRed(self.root.left):
            tx = ws / 3
            x += tx
            ws -= tx
        self.draw_node(draw, self.root, x, ws, y, key)
        img.save(os.path.join(self.out_path, str(self.step) + '.jpg'), 'jpeg')
        self.step += 1

    def draw_node(self, draw, node, x, ws, y, key):
        if node is None:
            return
        black = (0, 0, 0)
        red = (255, 0, 0)
        color = black
        if key == node.key:
            draw.text((x, y), str(node.key), (0, 255, 255))
        else:
            draw.text((x, y), str(node.key), black)
        cws = ws / 2
        cy = y + self.by
        if node.left is not None:
            if self.isRed(node.left):
                color = red
                cx = x - ws
                cy = y
            else:
                color = black
                cx = x - ws
                if self.isRed(node.left.left):
                    tx = cws / 3
                    cx += tx
                    cws -= tx
            if color == red:
                draw.line((cx, cy, x, y), color)
            else:
                draw.line((cx, cy, x, y + 10), color)
            self.draw_node(draw, node.left, cx, cws, cy, key)
        if node.right is not None:
            color = black
            cx = x + cws
            cy = y + self.by
            if self.isRed(node.right.left):
                tx = cws / 3
                cx += tx
                cws -= tx
            draw.line((cx, cy, x, y + 10), color)
            self.draw_node(draw, node.right, cx, cws, cy, key)

if __name__ == '__main__':
    import sys
    bst = BSTImage()
    if len(sys.argv) < 2:
        # 二叉树结构和输入顺序有关
        bst_worst = list(range(15))
        for word in bst_worst:
            val = bst.get(word)
            if val is None:
                bst.put(word, 1)
            else:
                bst.put(word, val + 1)
    else:
        with open(sys.argv[1], 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    val = bst.get(word)
                    if val is None:
                        bst.put(word, 1)
                    else:
                        bst.put(word, val + 1)
