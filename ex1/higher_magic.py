from collections.abc import Callable


# ---

def create_spell(mode: str) -> Callable[[str, int], str]:
    if mode == "fireball":
        def new_spell(target: str, power: int) -> str:
            return f"Fireball hits {target}(-{power})"
    elif mode == "heal":
        def new_spell(target: str, power: int) -> str:
            return f"Heal {target}(+{power})"
    else:
        raise ValueError(f"Unknown spell: {mode}")

    return new_spell


# ---

def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)

        return (result1, result2)

    return combined_spell


# ---

def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


# ---

def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:

    def sequential_spell(target: str, power: int) -> list[str]:
        results = [spell(target, power) for spell in spells]

        return results

    return sequential_spell


# ---

def main() -> None:
    P = "\033[38;5;205m"
    C = "\033[36m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    fireball = create_spell("fireball")
    heal = create_spell("heal")

    print(f"\033[35m████{RESET}" * 20, end="\n\n")

    print(f"{P}{BOLD}Testing spell combiner...{RESET}")
    combined = spell_combiner(fireball, heal)
    spell1, spell2 = combined("Wizard", 10)
    print(f"{C}Combined spell result:{RESET}  {spell1} and {spell2}\n")

    print(f"{P}{BOLD}Testing amplified spell...{RESET}")
    mega_fireball = power_amplifier(fireball, 3)
    print(
            f"{C}Original:{RESET}  {fireball("dragon", 10)}\n"
            f"{C}Amplified:{RESET}  {mega_fireball("dragon", 10)}\n"
            )

    print(f"{P}{BOLD}Testing conditional caster...{RESET}")
    big_fireball = conditional_caster(
            lambda target, power: power >= 20,
            fireball,
            )
    print(
            f"{DIM}Condition: power >= 20{RESET}\n"
            f"{C}power = 20:{RESET}  {big_fireball("Dragon", 20)}\n"
            f"{C}power = 10:{RESET}  {big_fireball("Dragon", 10)}\n"
            )

    print(f"{P}{BOLD}Testing spell sequence...{RESET}")
    spells = [fireball, heal]
    sequential_spell = spell_sequence(spells)
    print(
            f"{DIM}Fireball + Heal{RESET}\n"
            f"{C}List return:{RESET}  {sequential_spell("Dragon", 15)}"
            )

    print("\n" + f"\033[35m████{RESET}" * 20)


if __name__ == "__main__":
    main()
