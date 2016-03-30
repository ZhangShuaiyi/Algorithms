import math
import os
from PIL import Image, ImageDraw


class HeapSortImage(object):
    """docstring for HeapSortImage"""

    @classmethod
    def init_image(cls, a, w=400, h=400):
        cls.w = w
        cls.h = h
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        # y坐标的缩放值
        cls.ys = (cls.h / 2 - 40.0) / max_a
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

    @classmethod
    def draw_list(cls, a, num):
        # 新建一个白色背景图片
        img = Image.new('RGB', (cls.w, cls.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        # 绘制分割线
        draw.line((0, cls.h/2+20, cls.w, cls.h/2+20), (0, 0, 255))
        list_x = 10
        for n, v in enumerate(a):
            s = ''
            if isinstance(v, str):
                s = v
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                v = int(v, 36)
            else:
                s = str(v)

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
            # print(x, y)
            draw.text((x, y), s, (0, 0, 0))

            by = cls.h
            draw.line((list_x, by, list_x, by - v * cls.ys),
                      fill=(128, 128, 128), width=cls.lw)
            draw.text((list_x, by - v * cls.ys - 10), s, (0, 0, 0))
            list_x += cls.xs
        img.save(os.path.join(cls.out_path, str(cls.step) + '.jpg'), 'jpeg')
        cls.step += 1

if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    HeapSortImage.init_image(a)
    HeapSortImage.draw_list(a, len(a))
