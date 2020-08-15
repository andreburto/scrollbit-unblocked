from microbit import sleep, button_a, button_b, display, Image
from scrollbit import ScrollBit, ScrollText


def btn_act(st, t, i):
    st.set_text(t)
    st.reset()
    display.show(i)


def main():
    a_t = "Hello"
    b_t = "Goodbye"

    sb = ScrollBit()
    st = ScrollText(sb=sb)

    btn_act(st, a_t, Image.ARROW_W)

    while True:
        sb.clear()
        st.step()
        sb.show()

        if button_a.is_pressed():
            btn_act(st, a_t, Image.ARROW_W)
        if button_b.is_pressed():
            btn_act(st, b_t, Image.ARROW_E)

        sleep(50)


# Start the code.
main()
