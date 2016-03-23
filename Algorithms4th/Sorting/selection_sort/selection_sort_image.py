from PIL import Image, ImageDraw
import os
from selection_sort import SelectionSort


class SelectionSortImage(SelectionSort):
    """使用PIL将交换的数据保存"""

    w = 400
    h = 400
    # 操作步数
    step = 1
    # x坐标的缩放值
    xs = 1.0
    # y坐标的缩放值
    ys = 1.0
    out_path = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_path, 'out')
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    @classmethod
    def less(cls, a, i, j):
        cls.drawList(a, cls.w, cls.h, str(cls.step) + '.jpg',
                     'compare step: ' + str(cls.step),
                     xs=cls.xs, lw=int(cls.xs) - 1, ys=cls.ys,
                     i=i, j=j, color=(0, 255, 255))
        cls.step += 1
        return super(SelectionSortImage, cls).less(a, i, j)

    @classmethod
    def exch(cls, a, i, j):
        cls.drawList(a, cls.w, cls.h, str(cls.step) + '.jpg',
                     'swap step: ' + str(cls.step),
                     xs=cls.xs, lw=int(cls.xs) - 1, ys=cls.ys,
                     i=i, j=j, color=(0, 0, 255))
        cls.step += 1
        super(SelectionSortImage, cls).exch(a, i, j)

    @classmethod
    def selection_sort(cls, a):
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        cls.ys = (cls.h - 20.0) / max_a
        cls.xs = (cls.w - 10.0) / len(a)
        super(SelectionSortImage, cls).selection_sort(a)

    @classmethod
    def drawList(cls, buf, w, h, name, text=None, xs=10, lw=5,
                 ys=10, i=-1, j=-1, color=(0, 0, 255)):
        '''
        xs：x坐标间隔
        lw：宽度
        ys：y坐标步长
        '''
        # 新建一个白色背景图片
        img = Image.new('RGB', (w, h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = 10
        if text is not None:
            draw.text((x, 0), text, (255, 0, 0))
        for n, d in enumerate(buf):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)
            if n == i or n == j:
                draw.line((x, h, x, h - d * ys), fill=color, width=lw)
            else:
                draw.line(
                    (x, h, x, h - d * ys), fill=(128, 128, 128), width=lw)
            draw.text((x, h - d * ys - 12), s, (0, 0, 0))
            x += xs
        # 显示图片
        # img.show()
        img.save(os.path.join(cls.out_path, name), 'jpeg')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Not enter file, draw test.jpg for test")
        buf = [3, 10, 4, 8, 6, 2, 7]
        SelectionSortImage.drawList(buf, 400, 400, 'test.jpg')
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            a = []
            [a.extend(line.split()) for line in lines]
            SelectionSortImage.selection_sort(a)
            print(a)
