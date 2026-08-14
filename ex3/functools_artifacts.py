from functools import reduce, partial
from operator import add, mul, gt


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} {target} ({power})"


def main() -> None:
    n1 = [10, 20, 30, 40]

    r1 = reduce(add, n1)

    print(r1)

    n2 = [2, 3, 4, 5]

    r2 = reduce(mul, n2)
    print(r2)
    r3 = reduce(
            lambda a, b: a if gt(a, b) else b,
            n2
            )
    print(r3)

    c = n2[0]
    for n in n2[1:]:
        c = (lambda a, b: a if gt(a, b) else b)(c, n)
    print(c)

    print(enchant(50, "Fire", "Sword"))
    fire_enchant = partial(enchant, 50, "Fire")
    print(fire_enchant("Shield"))
    sword_type = partial(enchant, 50, target="Sword")
    print(sword_type("Ice"))



if __name__ == "__main__":
    main()
