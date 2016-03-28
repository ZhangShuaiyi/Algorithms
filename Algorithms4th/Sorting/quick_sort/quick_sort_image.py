import os
from PIL import Image, ImageDraw
from quick_sort import QuickSort


class QuickSortImage(QuickSort):
    """快速排序使用PIL保存排序流程"""

    @classmethod
    def sort(cls, a):
        cls.init_image(a)
        super(QuickSortImage, cls).sort(a)
        cls.draw_list(a)

    @classmethod
    def partition(cls, a, lo, hi):
        # 左右扫描索引
        i = lo + 1
        j = hi
        # 切分元素
        v = a[lo]
        while True:
            # 扫描左右，检查扫描是否结束并交换元素
            while a[i] < v:
                if i == hi:
                    break
                i += 1
            while v < a[j]:
                if j == lo:
                    break
                j -= 1
            if i >= j:
                break
            cls.draw_list(a, lo, hi, i, j)
            a[i], a[j] = a[j], a[i]
        cls.draw_list(a, lo, hi, lo, j)
        a[lo], a[j] = a[j], a[lo]
        # 结果a[lo..j-1] <= a[j] <= a[j+1..hi]
        return j

    @classmethod
    def draw_list(cls, a, lo=-1, hi=-1, i=-1, j=-1):
        # 新建一个白色背景图片
        img = Image.new('RGB', (cls.w, cls.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = 10
        for n, d in enumerate(a):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)
            draw.text((x, cls.h - d * cls.ys - 12), s, (0, 0, 0))
            if n == lo:
                draw.line((x, cls.h, x, cls.h - d * cls.ys),
                          fill=(0, 0, 0), width=cls.lw)
            elif n > lo and n <= hi:
                draw.line((x, cls.h, x, cls.h - d * cls.ys),
                          fill=(128, 128, 128), width=cls.lw)
            else:
                draw.line((x, cls.h, x, cls.h - d * cls.ys),
                          fill=(192, 192, 192), width=cls.lw)
            if n == i or n == j:
                draw.line((x, cls.h - d * cls.ys + 12, x, cls.h - d * cls.ys),
                          fill=(255, 0, 0), width=cls.lw)
                draw.text((x, cls.h - d * cls.ys - 12), s, (255, 0, 0))
            x += cls.xs
        # 显示图片
        # img.show()
        name = str(cls.step) + '.jpg'
        img.save(os.path.join(cls.out_path, name), 'jpeg')
        cls.step += 1

    @classmethod
    def init_image(cls, a):
        cls.w = 400
        cls.h = 400
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        # y坐标的缩放值
        cls.ys = (cls.h - 20.0) / max_a
        # x坐标的缩放值
        cls.xs = (cls.w - 10.0) / len(a)
        cls.lw = int(cls.xs) - 1
        # 操作步数
        cls.step = 1
        out_path = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(out_path, 'out')
        cls.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        a = list(range(11, 0, -1))
        QuickSortImage.sort(a)
        print(a)
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            a = []
            [a.extend(line.split()) for line in lines]
            QuickSortImage.sort(a)
            print(a)
