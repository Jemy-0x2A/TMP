
import readchar  # type: ignore
from readchar import key


# -- NUMBER

def get_number() -> str:
    valids_input = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    buffer: str = ""

    buffer = "0"
    print("0", end="", flush=True)

    while True:
        touch: str = readchar.readkey()

        if touch == key.ENTER:  # - ENTER
            break

        if touch in valids_input:  # - DIGIT
            if buffer == "0":
                if touch != ".":
                    buffer = touch
                else:
                    buffer += touch
            else:
                if touch == "." and touch in buffer:
                    continue

                buffer += touch

            print(f"\r{buffer}", end="", flush=True)

        if touch == key.BACKSPACE:  # - BACKSPACE
            buffer = buffer[:-1]

            if not buffer:
                buffer = "0"

            print(f"\r\033[K{buffer}", end="", flush=True)

    return buffer


# -- OPERATOR

def get_operator() -> str:
    valids_input = {"+", "-", "*", "/"}
    buffer: str = ""

    while True:
        touch: str = readchar.readkey()

        if touch == key.ENTER:
            if not buffer:
                continue
            break

        if touch in valids_input:
            buffer = touch

            print(f"\r{buffer}", end="", flush=True)

    return buffer


def get_result(n1: float, operator: str, n2: float) -> float:
    result: float = 0.0

    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2

    return result


def calculator() -> None:
    print("First number:")
    number1: float = float(get_number())

    print("\nOperator: [+][-][*][/]")
    operator = get_operator()

    print("\nSecond number:")
    number2: float = float(get_number())

    try:
        result = get_result(number1, operator, number2)
        print(f"\nResult:  {result}")
    except ZeroDivisionError:
        print("\nResult:  Not defined")


if __name__ == "__main__":
    calculator()
