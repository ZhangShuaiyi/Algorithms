import os
from PIL import Image, ImageDraw
from binary_search_tree import BST


class BSTImage(BST):
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

    def draw_tree(self, key):
        if self.root is None:
            return
        # 新建一个白色背景图片
        img = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = self.w / 2
        ws = x / 2
        y = 0
        self.draw_node(draw, self.root, x, ws, y, key)
        img.save(os.path.join(self.out_path, str(self.step) + '.jpg'), 'jpeg')
        self.step += 1

    def draw_node(self, draw, node, x, ws, y, key):
        if node is None:
            return
        color = (0, 0, 0)
        if node.key == key:
            color = (255, 0, 0)
        draw.text((x, y), str(node.key), color)
        color = (0, 0, 0)
        cws = ws / 2
        if node.left is not None:
            cx = x - cws
            cy = y + self.ys
            if node.left.key == key:
                color = (255, 0, 0)
            draw.line((cx, cy, x, y + 10), color)
            self.draw_node(draw, node.left, cx, cws, cy, key)
        color = (0, 0, 0)
        if node.right is not None:
            cx = x + cws
            cy = y + self.ys
            if node.right.key == key:
                color = (255, 0, 0)
            draw.line((cx, cy, x, y + 10), color)
            self.draw_node(draw, node.right, cx, cws, cy, key)

if __name__ == '__main__':
    import sys
    bst = BSTImage()
    if len(sys.argv) < 2:
        # 二叉树结构和输入顺序有关
        bst_worst = list(range(6))
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
