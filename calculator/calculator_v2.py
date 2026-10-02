
import os
import readchar
from readchar import key

def screen_clean() -> None:
    os.system('clear')


def calculator() -> None:
    screen = ""

    while True:
        screen_clean()


if __name__ == "__main__":
    calculator()
