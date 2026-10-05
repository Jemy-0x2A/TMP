
import readchar
from readchar import key


def boucle2(operator: str) -> int:
    while True:
        touch: str = readchar.readkey()

        if touch in "+-*/":
            print(f"\b{touch}", end="", flush=True)
        elif touch in "0123456789":
            print(f"{touch}", end="", flush=True)
            return touch
        else:
            return touch


def boucle1() -> int:
    while True:
        touch: str = readchar.readkey()

        if touch in "0123456789":
            print(f"{touch}", end="", flush=True)
        elif touch in "+-*/":
            print(f" {touch} ", end="", flush=True)
            return touch
        else:
            return touch


def test() -> None:
    mode: int = 0
    touch: str = ""

    while True:
        if touch in "0123456789":
            touch = boucle1()

        elif touch in "+-*/":
            touch = boucle2(touch)

        else:
            break

    print("\nFIN")

test()
