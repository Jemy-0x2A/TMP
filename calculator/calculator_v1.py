
import readchar  # type: ignore
from readchar import key


def get_input(mode: str, valids_input: set[str]) -> str:
    buffer: str = ""

    if mode == "number":
        buffer = "0"
        print("0", end="", flush=True)

    while True:
        touch: str = readchar.readkey()

        if touch == key.ENTER:
            if mode == "operator" and not buffer:
                continue
            break

        if touch in valids_input:
            if mode == "number":
                if buffer == "0":
                    buffer = touch
                else:
                    buffer += touch
            elif mode == "operator":
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
    valids_digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    valids_operators = {"+", "-", "*", "/"}

    print("First number:")
    n1: float = float(get_input("number", valids_digits))

    print("\nOperator: [+][-][*][/]")
    operator = get_input("operator", valids_operators)

    print("\nSecond number:")
    n2: float = float(get_input("number", valids_digits))

    try:
        result = get_result(n1, operator, n2)
        print(f"\nResult:  {result}")
    except ZeroDivisionError:
        print("\nResult:  Not defined")


if __name__ == "__main__":
    calculator()
