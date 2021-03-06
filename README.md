# ScrollBit-Unblocked

### About

The [scroll:bit](https://shop.pimoroni.com/products/scroll-bit) is an **AMAZING** add-on to the [micro:bit](https://microbit.org/).

My one issue with their driver is that the text scroll is blocking.
This project tries to fix that by using some techniques I picked up when playing with [writing screen savers](https://github.com/andreburto/straight_lines).

This code is offered as-is and without any promises or claims.

### Files

##### Source

* `scrollbit.py`, classes that drive the scroll:bit.

##### Examples

All example files unless otherwise noted work alongside the `scrollbit.py` file.

* `dots`, original testbed used to develop `ScrollBit` class.
* `hello_goodbye`, main demonstration program used to show off the non-blocking text scroll.

### Resources

The original [micropython-scrollbit](https://github.com/pimoroni/micropython-scrollbit) library, which this project borrows from heavily.
I hope to contribute back to their library eventually, but not until this code reaches feature parity.

The [BBC micro:bit MicroPython](https://microbit-micropython.readthedocs.io/en/latest/index.html) docs. Very useful.

[Code with Mu](https://codewith.mu/). The best Python editor for bit bashing.

### Log

##### 2020-08-14
* Made minor changes to `scrollbit.py` to removed unneeded commands.
* Modified layout of project to keep driver class source code and examples in separate locations.

##### 2020-08-01
* Achieved non-blocking horizontal scrolling text. Woohoo!

### To Do

1. Reach feature parity with the original driver.
2. Write tests for the code.
3. Refactor not to use classes (maybe).
