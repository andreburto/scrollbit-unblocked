from microbit import display, sleep
from scrollbit import ScrollBit


class BaseDisplay:
    start_x = 0
    start_y = 0
    x = 0
    y = 0

    def __init__(self, b=None, i=1):
        self.b = self._validate_b(b) if b else self.max_b
        self.i = i

    def _validate_b(self, b):
        if b > self.max_b:
            return self.max_b
        elif b < self.min_b:
            return self.min_b
        else:
            return b

    def step(self):
        self.x += self.i
        if self.x > self.w - self.i:
            self.x = self.start_x
            self.y += self.i
            if self.y > self.h - self.i:
                self.y = self.start_y


class BitDisplay(BaseDisplay):
    max_b = 9
    min_b = 0
    h = 5
    w = 5


class ScrollDisplay(BaseDisplay):
    max_b = 255
    min_b = 0
    h = 7
    w = 17


def main():
    sb = ScrollBit()
    sd = ScrollDisplay(100)
    bd = BitDisplay(7)

    while True:
        sb.set_pixel(sd.x, sd.y, sd.b)
        sb.show()
        display.set_pixel(bd.x, bd.y, bd.b)

        sd.step()
        bd.step()

        sleep(200)

        sb.clear()
        display.clear()


# Start the code.
main()
