import os
from PIL import Image, ImageDraw
from quick_3way import Quick3way


class QuickSortImage(Quick3way):
    """快速排序使用PIL保存排序流程"""

    @classmethod
    def sort(cls, a):
        cls.init_image(a)
        super(QuickSortImage, cls).sort(a)
        cls.draw_list(a)

    @classmethod
    def sort_lh(cls, a, lo, hi):
        if hi <= lo:
            return
        lt = lo
        i = lo + 1
        gt = hi
        v = a[lo]
        while i <= gt:
            cls.draw_list(a, lo, hi, lt, gt, i=i)
            if a[i] < v:
                cls.draw_list(a, lo, hi, lt, gt, i=i, j=lt)
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif a[i] > v:
                cls.draw_list(a, lo, hi, lt, gt, i=i, j=gt)
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        cls.sort_lh(a, lo, lt - 1)
        cls.sort_lh(a, gt + 1, hi)

    @classmethod
    def draw_list(cls, a, lo=-1, hi=-1, lt=-1, gt=-1, i=-1, j=-1):
        # 新建一个白色背景图片
        img = Image.new('RGB', (cls.w, cls.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = 10
        swap_y = 20
        cmp_y = 10
        if lt != -1 and gt != -1:
            draw.line((x + cls.xs * lo, cmp_y, x + cls.xs * lt, cmp_y),
                      fill=(0, 0, 255))
            draw.line((x + cls.xs * gt, cmp_y, x + cls.xs * hi, cmp_y),
                      fill=(0, 0, 255))
            if j != -1:
                draw.line((cls.xs * i + x, swap_y, cls.xs * j + x, swap_y),
                          fill=(255, 0, 0), width=2)
        for n, d in enumerate(a):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)
            draw.text((x, cls.h - d * cls.ys - 12), s, (0, 0, 0))
            if n >= lo and n <= hi:
                draw.line((x, cls.h, x, cls.h - d * cls.ys),
                          fill=(128, 128, 128), width=cls.lw)
            else:
                draw.line((x, cls.h, x, cls.h - d * cls.ys),
                          fill=(192, 192, 192), width=cls.lw)
            if n == lt or n == gt:
                draw.line((x, cls.h - d * cls.ys - 12, x, cmp_y),
                          fill=(0, 0, 255))
            if n == i or n == j:
                if j != -1:
                    draw.line((x, cls.h - d * cls.ys - 12, x, swap_y),
                              fill=(255, 0, 0), width=2)
            if n == i:
                draw.line((x, cls.h - d * cls.ys + 12, x, cls.h -
                           d * cls.ys), fill=(0, 255, 0), width=cls.lw)
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
        cls.ys = (cls.h - 40.0) / max_a
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
        # a = list(range(11, 0, -1))
        a = [5, 2, 3, 1, 2, 3, 1, 2, 2, 2, 4, 4, 5, 5, 2]
        QuickSortImage.sort(a)
        print(a)
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            a = []
            [a.extend(line.split()) for line in lines]
            QuickSortImage.sort(a)
            print(a)
