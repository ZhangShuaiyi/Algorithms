import math
import os
from PIL import Image, ImageDraw


class HeapSortImage(object):
    """docstring for HeapSortImage"""

    @classmethod
    def sink(cls, a, k, n):
        '''
        由上至下的堆有序化（下沉）的实现
        '''
        # 子节点为2*k+1 和2*k-1
        j = 2 * k + 1
        while j <= n:
            if j < n and a[j] < a[j + 1]:
                j += 1
            cls.draw_list(a, n, ck=k, cw=j)
            if a[k] >= a[j]:
                break
            cls.draw_list(a, n, i=k, j=j)
            a[k], a[j] = a[j], a[k]
            k = j
            j = 2 * k + 1

    @classmethod
    def sort(cls, a):
        cls.init_image(a)
        n = len(a) - 1
        # 堆有序化，堆有序后a[0]为最大值
        for k in range((n - 1) // 2, -1, -1):
            cls.sink(a, k, n)
        while n > 0:
            cls.draw_list(a, n, i=0, j=n)
            # a[0]最大，将a[0]交换到最后
            a[0], a[n] = a[n], a[0]
            n -= 1
            # 减小堆大小，将a[0]下浮到对应位置
            cls.sink(a, 0, n)
        cls.draw_list(a)

    @classmethod
    def init_image(cls, a, w=400, h=400):
        cls.w = w
        cls.h = h
        cls.line_y = cls.h / 2 + 10
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        # y坐标的缩放值
        cls.ys = (cls.h - cls.line_y - 30.0) / max_a
        # x坐标的缩放值
        cls.xs = (cls.w - 10.0) / len(a)
        cls.lw = int(cls.xs) - 1
        cls.step = 1

        out_path = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(out_path, 'out')
        cls.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        n = len(a)
        # 堆总高度
        cls.heap_hn = int(math.log(n, 2))
        # 堆总宽度
        cls.heap_wn = 2**cls.heap_hn
        # 堆x基准偏移
        cls.heap_bx = 20
        # 堆y基准偏移
        cls.heap_by = 20
        # 堆x宽度
        cls.heap_xs = (cls.w - cls.heap_bx * 2) // cls.heap_wn
        # 堆y高度
        cls.heap_ys = (cls.h / 2 - cls.heap_by) / cls.heap_hn
        cls.heap_xy = [0] * n

    @classmethod
    def draw_heap(cls, draw, a, num, i=-1, j=-1, ck=-1, cw=-1):
        for n, v in enumerate(a):
            if n > num:
                break
            # 当前数据在堆的那一层
            heap_ny = int(math.log2(n + 1))
            # 该层最多保存元素个数
            heap_nx_a = 2**heap_ny
            # 数据在当前层的位置
            nx = n + 1 - heap_nx_a
            # 堆在当前层x坐标的基准偏移
            bx = (2**(cls.heap_hn - heap_ny) - 1) * cls.heap_xs / 2
            # 堆在当前层x坐标的宽度
            xs = 2**(cls.heap_hn - heap_ny) * cls.heap_xs
            # 数据的x坐标
            x = cls.heap_bx + bx + xs * nx
            # 数据的y坐标
            y = cls.heap_by + cls.heap_ys * heap_ny
            cls.heap_xy[n] = [x, y]
            # print(x, y)
            draw.text((x, y), v, (0, 0, 0))
            if n > 0:
                k = (n - 1) // 2
                kx, ky = cls.heap_xy[k]
                draw.line((x, y, kx, ky + 10), (0, 0, 0))
        if i != -1 and j != -1:
            x1, y1 = cls.heap_xy[i]
            x2, y2 = cls.heap_xy[j]
            draw.line((x1, y1 + 10, x2, y2), (255, 0, 0), width=2)
        if ck != -1 and cw != -1:
            x1, y1 = cls.heap_xy[ck]
            x2, y2 = cls.heap_xy[cw]
            draw.line((x1, y1 + 10, x2, y2), (0, 255, 255))

    @classmethod
    def draw_list(cls, a, num=-1, i=-1, j=-1, ck=-1, cw=-1):
        # 新建一个白色背景图片
        img = Image.new('RGB', (cls.w, cls.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        # 绘制分割线
        draw.line((0, cls.line_y, cls.w, cls.line_y), (0, 0, 255))
        list_x = 10
        if i != -1 and j != -1:
            x1 = cls.xs * i + list_x
            x2 = cls.xs * j + list_x
            y = cls.line_y + 10
            draw.line((x1, y, x2, y), fill=(255, 0, 0), width=2)
        if ck != -1 and cw != -1:
            x1 = cls.xs * ck + list_x
            x2 = cls.xs * cw + list_x
            y = cls.line_y + 10
            draw.line((x1, y, x2, y), fill=(0, 255, 255))

        cls.draw_heap(draw, a, num, i, j, ck, cw)
        for n, v in enumerate(a):
            s = ''
            if isinstance(v, str):
                s = v
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                v = int(v, 36)
            else:
                s = str(v)

            by = cls.h
            y = by - v * cls.ys
            if n <= num:
                draw.line((list_x, by, list_x, y),
                          fill=(192, 192, 192), width=cls.lw)
            else:
                draw.line((list_x, by, list_x, y),
                          fill=(128, 128, 128), width=cls.lw)
            draw.text((list_x, y - 10), s, (0, 0, 0))
            if n == i or n == j:
                y1 = cls.h - v * cls.ys - 12
                y2 = cls.line_y + 10
                draw.line((list_x, y1, list_x, y2), fill=(255, 0, 0), width=2)
            if n == ck or n == cw:
                y1 = cls.h - v * cls.ys - 12
                y2 = cls.line_y + 10
                draw.line((list_x, y1, list_x, y2), fill=(0, 255, 255))
            if n == num:
                draw.line((list_x, cls.line_y + 20, cls.w, cls.line_y + 20),
                          fill=(0, 0, 255))
                draw.line((list_x, y - 15, list_x, cls.line_y + 20),
                          fill=(0, 0, 255))
            list_x += cls.xs
        img.save(os.path.join(cls.out_path, str(cls.step) + '.jpg'), 'jpeg')
        cls.step += 1

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        HeapSortImage.init_image(a)
        HeapSortImage.draw_list(a, len(a))
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            a = []
            [a.extend(line.split()) for line in lines]
            HeapSortImage.sort(a)
            print(a)
