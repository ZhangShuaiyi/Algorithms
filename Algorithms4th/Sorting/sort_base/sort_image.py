from PIL import Image, ImageDraw
import os


class SortImage():
    """使用PIL将交换的数据保存"""

    def __init__(self, a, w=400, h=400, out_path=None):
        self.buf = a
        self.w = w
        self.h = h
        max_a = max(a)
        if isinstance(max_a, str):
            max_a = int(max_a, 36)
        # y坐标的缩放值
        self.ys = (self.h - 20.0) / max_a
        # x坐标的缩放值
        self.xs = (self.w - 10.0) / len(a)
        self.lw = int(self.xs) - 1
        # 操作步数
        self.step = 1
        if out_path is None:
            out_path = os.path.dirname(os.path.abspath(__file__))
            out_path = os.path.join(out_path, 'out')

        self.out_path = out_path
        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def drawList(self, text=None, i=-1, j=-1, color=(0, 0, 255)):
        '''
        xs：x坐标间隔
        lw：宽度
        ys：y坐标步长
        '''
        # 新建一个白色背景图片
        img = Image.new('RGB', (self.w, self.h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x = 10
        if text is not None:
            text = text + ' setep: ' + str(self.step)
        else:
            text = ' setep: ' + str(self.step)
        draw.text((x, 0), text, (255, 0, 0))
        for n, d in enumerate(self.buf):
            s = ''
            if isinstance(d, str):
                s = d
                # 如果是字符串的话，就按照36进制转换为整数，所有字母可转换为整数
                d = int(d, 36)
            else:
                s = str(d)
            if n == i or n == j:
                draw.line((x, self.h, x, self.h - d * self.ys),
                          fill=color, width=self.lw)
            else:
                draw.line((x, self.h, x, self.h - d * self.ys),
                          fill=(128, 128, 128), width=self.lw)
            draw.text((x, self.h - d * self.ys - 12), s, (0, 0, 0))
            x += self.xs
        # 显示图片
        # img.show()
        name = str(self.step) + '.jpg'
        img.save(os.path.join(self.out_path, name), 'jpeg')
        self.step += 1

if __name__ == '__main__':
    print("SortImage test!!")
    buf = [3, 10, 4, 8, 6, 2, 7]
    sort_image = SortImage(buf)
    sort_image.drawList()
