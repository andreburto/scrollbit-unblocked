# Original code: https://github.com/pimoroni/micropython-scrollbit
# This code is derived from the original ScrollBit code and refactored into a class.
# Much of the functionality is missing but that will come in time.


class ScrollBit():
    def __init__(self, w=17, h=7, o=0):
        from microbit import i2c
        self.i2c = i2c
        self.h = h
        self.w = w
        self.o = o
        # The bank control switch
        self._f = 0
        # Initialize scrollbit
        for a, b in ((253, 11), (10, 0), (10, 1), (0, 0), (6, 0)):
            self._w(a, b)
        for bank in [1, 0]:
            self._w(253, bank)
            self._w([0] + [255] * 17)
        self.clear()
        self.show()

    def _pixel_addr(self, x, y):
        y = (self.h - (y + 1)) * (1 - self.o) + self.o * y
        x = (self.w - (x + 1)) * self.o + (1 - self.o) * x
        if x > 8:
            x = x - 8
            y = 6 - (y + 8)
        else:
            x = 8 - x
        return (x * 16 + y) + 1

    def set_pixel(self, col, row, b):
        self._b[self._pixel_addr(col, row)] = b

    def _w(self, *args):
        self.i2c.write(116, bytes(args[0] if len(args) == 1 else args))

    def clear(self):
        self._b = bytearray(145)

    def show(self):
        b = bytearray([i for i in self._b])
        self._f = not self._f
        f = int(self._f)
        self._w(253, f)
        b[0] = 36
        self._w(b)
        self._w(253, 11)
        self._w(1, f)


class ScrollText():
    HEIGHT = 7
    WIDTH = 17

    start_x = 0
    start_y = 1

    def __init__(self, b=100, sb=None):
        from microbit import Image as I
        self.img = I
        self.i = [getattr(I, x) for x in dir(I) if hasattr(getattr(I, x), "get_pixel")]

        self.b = b
        self.sb = sb

        self.reset()

    def char_len(self, char):
        if char in b'"*+-0123<=>ABCDEFHKLOPQSUXZ[]^bcdefghjklnopqrsxz{':
            return 4
        if char in b"!'.:i|":
            return 2
        if char in b" (),;I`}":
            return 3
        return 5

    def set_text(self, text):
        self.tl = sum(self.char_len(c) + 1 for c in text)
        self.t = text

    def draw_icon(self, col, row, icon):
        for x in range(5):
            if col + x < 0:
                continue
            if col + x >= self.WIDTH:
                return False
            for y in range(5):
                if not icon.get_pixel(x, y):
                    continue
                try:
                    self.sb.set_pixel(x + col, y + row, int(self.b))
                except IndexError:
                    pass
        return True

    def write(self, offset_col=0, offset_row=0):
        i = None
        for letter in self.t:
            i = None
            letter_width = self.char_len(letter)
            if letter != " " and (offset_col + letter_width) >= 1:
                if ord(letter) > 127:
                    i = self.i[ord(letter) - 128]
                else:
                    try:
                        i = self.img(letter)
                    except:
                        pass
            if i is not None:
                if not self.draw_icon(offset_col, offset_row, i):
                    return
            offset_col += letter_width + 1
        del i

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y

    def step(self):
        self.write(int(-self.x + self.WIDTH), int(self.y))
        self.x += 1
        if self.x > self.tl + self.WIDTH:
            self.reset()
