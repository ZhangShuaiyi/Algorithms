from PIL import Image, ImageDraw
import os
from selection_sort import SelectionSort


class SelectionSortImage(SelectionSort):
    """使用PIL将交换的数据保存"""

    step = 1
    out_path = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_path, 'out')
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    @classmethod
    def exch(cls, a, i, j):
        super(SelectionSortImage, cls).exch(a, i, j)
        cls.drawList(a, 400, 400, str(cls.step) + '.jpg')
        cls.step += 1

    @classmethod
    def drawList(cls, buf, w, h, name, xs=10, lw=5, ys=10):
        '''
        xs：x坐标间隔
        lw：宽度
        ys：y坐标步长
        '''
        # 新建一个白色背景图片
        img = Image.new('RGB', (w, h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = 10
        draw.text((x, 0), name, (0, 255, 0))
        for d in buf:
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)
            draw.line((x, h, x, h - d * ys), fill=(255, 0, 0), width=lw)
            draw.text((x, h - d * ys - ys), s, (0, 0, 0))
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
