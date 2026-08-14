from collections.abc import Callable
from typing import TypedDict


class MemoryVault(TypedDict):
    store: Callable[[str, int], None]
    recall: Callable[[str], int | str]


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> MemoryVault:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    Y = "\033[33m"
    C = "\033[36m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    print(f"\033[38;5;166m████{RESET}" * 20, end="\n\n")

    counter_a = mage_counter()
    counter_b = mage_counter()
    print(
            f"{Y}{BOLD}Testing mage counter...{RESET}\n"
            f"{C}counter_a call 1:{RESET}  {counter_a()}\n"
            f"{C}counter_a call 2:{RESET}  {counter_a()}\n"
            f"{C}counter_b call 1:{RESET}  {counter_b()}\n"
          )

    accumulation = spell_accumulator(100)
    print(
            f"{Y}{BOLD}Testing spell accumulator...{RESET}\n"
            f"{DIM}Base 100{RESET}\n"
            f"{C}call 1, add 20:{RESET}  {accumulation(20)}\n"
            f"{C}call 2, add 30:{RESET}  {accumulation(30)}\n"
            )

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(
            f"{Y}{BOLD}Testing enchantment factory...{RESET}\n"
            f"{flaming("Sword")}\n"
            f"{frozen("Shield")}\n"
          )

    vault = memory_vault()
    print(
            f"{Y}{BOLD}Testing memory vault...{RESET}\n"
            f"{C}Store 'secret' ={RESET} 42"
            )
    vault["store"]("secret", 42)
    print(
            f"{C}Recall 'secret':{RESET} {vault["recall"]("secret")}\n"
            f"{C}Recall 'unknown':{RESET} {vault["recall"]("unknown")}"
            )

    print("\n" + f"\033[38;5;166m████{RESET}" * 20)


if __name__ == "__main__":
    main()
