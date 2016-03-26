from PIL import Image, ImageDraw
import os
from top_down_mergesort import TopDownMergeSort


class SortImage():
    """docstring for SortImage"""

    def __init__(self, a, w=400, h=400, out_path=None):
        self.w = w
        self.h = h
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        # y坐标的缩放值
        self.ys = (self.h / 2 - 10.0) / max_a
        # x坐标的缩放值
        self.xs = (self.w - 10.0) / len(a)
        self.lw = int(self.xs) - 1

        # create output path
        if out_path is None:
            out_path = os.path.dirname(os.path.abspath(__file__))
            out_path = os.path.join(out_path, 'out')

        self.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        self.step = 1

    def draw_lists(self, aux, a, lo, mid, hi, k=-1, i=-1):
        # 新建一个白色背景图片
        img = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        x = 10
        by = self.h / 2
        for n, d in enumerate(aux):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)

            if n == i:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(0, 255, 255), width=self.lw)
            elif n >= lo and n <= mid:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(0, 0, 255), width=self.lw)
            elif n > mid and n <= hi:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(0, 255, 0), width=self.lw)
            else:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(128, 128, 128), width=self.lw)
            draw.text((x, by - d * self.ys - 10), s, (0, 0, 0))
            x += self.xs

        x = 10
        by = self.h
        for n, d in enumerate(a):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)

            if n == k:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(0, 255, 255), width=self.lw)
            elif n >= lo and n <= hi:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(255, 0, 255), width=self.lw)
            else:
                draw.line((x, by, x, by - d * self.ys),
                          fill=(128, 128, 128), width=self.lw)
            draw.text((x, by - d * self.ys - 10), s, (0, 0, 0))
            x += self.xs
        img.save(os.path.join(self.out_path, str(self.step) + '.jpg'), 'jpeg')
        self.step += 1


class TopDownMergeSortImage(TopDownMergeSort):
    """docstring for TopDownMergeSortImage"""

    @classmethod
    def merge(cls, a, lo, mid, hi):
        cls.aux[lo:hi + 1] = a[lo:hi + 1]
        cls.sort_image.draw_lists(cls.aux, a, lo, mid, hi)
        i = lo
        j = mid + 1
        k = lo
        while i <= mid and j <= hi:
            if cls.aux[i] < cls.aux[j]:
                a[k] = cls.aux[i]
                cls.sort_image.draw_lists(
                    cls.aux, a, lo, mid, hi, k=k, i=i)
                k += 1
                i += 1
            else:
                a[k] = cls.aux[j]
                cls.sort_image.draw_lists(
                    cls.aux, a, lo, mid, hi, k=k, i=j)
                k += 1
                j += 1
        n = mid + 1 - i
        a[k:k + n] = cls.aux[i:mid + 1]
        k += n
        n = hi + 1 - j
        a[k:k + n] = cls.aux[j:hi + 1]
        cls.sort_image.draw_lists(cls.aux, a, lo, mid, hi)

    @classmethod
    def sort(cls, a):
        cls.sort_image = SortImage(a)
        super(TopDownMergeSortImage, cls).sort(a)


if __name__ == '__main__':
    import sys
    if (len(sys.argv) < 2):
        print('No file input!')
        a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        aux = a[:]
        sort_image = SortImage(a)
        lo = 0
        hi = len(a) - 1
        mid = lo + (hi - lo) // 2
        sort_image.draw_lists(aux, a, lo, mid, hi)
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            a = []
            [a.extend(line.split()) for line in lines]
            TopDownMergeSortImage.sort(a)
            print(a)
