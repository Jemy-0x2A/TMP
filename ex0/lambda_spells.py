from typing import TypedDict


class Artifact(TypedDict):
    name: str
    power: int


class Mage(TypedDict):
    name: str
    power: int


# ---

def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    artifacts_sorted = sorted(
            artifacts,
            key=lambda artifact: artifact["power"],
            reverse=True
            )

    return artifacts_sorted


# ---

def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    mages_filtered = filter(
            lambda mage: mage["power"] >= min_power,
            mages
            )

    return list(mages_filtered)


# ---

def spell_transformer(spells: list[str]) -> list[str]:
    spells_map = map(
            lambda spell: f"* {spell} *",
            spells
            )

    return list(spells_map)


# ---

def mage_stats(mages: list[Mage]) -> dict[str, int | float]:
    most_powerful = max(
            mages,
            key=lambda mage: mage["power"]
            )
    max_power = most_powerful["power"]

    least_powerful = min(
            mages,
            key=lambda mage: mage["power"]
            )
    min_power = least_powerful["power"]

    powers_list = [mage["power"] for mage in mages]
    avg_power = round(sum(powers_list) / len(powers_list), 2)

    return {
            "max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power
            }


def main() -> None:
    Y = "\033[33m"
    C = "\033[36m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    artifacts: list[Artifact] = [
            {"name": "Fire Staff", "power": 92},
            {"name": "Crystal Orb", "power": 85},
            {"name": "Magic Wand", "power": 100}
            ]

    mages: list[Mage] = [
            {"name": "Gandalf", "power": 90},
            {"name": "Merlin", "power": 70},
            {"name": "Saruman", "power": 85}
            ]

    spells: list[str] = ["fireball", "heal", "shield"]

    print(f"\033[38;5;166m████{RESET}" * 20, end="\n\n")

    print(f"{Y}{BOLD}Data created:{RESET}")
    print(f"{C}Artifacts list: {RESET}")
    for artifact in artifacts:
        print(DIM, artifact, RESET)
    print(f"{C}Mages list: {RESET}")
    for mage in mages:
        print(DIM, mage, RESET)
    print(f"{C}Spells list: {RESET}")
    print(DIM, spells, RESET)

    print(f"\n{Y}{BOLD}Testing artifact sorter...{RESET}")
    print(artifact_sorter(artifacts))

    print(f"\n{Y}{BOLD}Testing power filter...{RESET}")
    print(power_filter(mages, 80))

    print(f"\n{Y}{BOLD}Testing spell transformer...{RESET}")
    print(spell_transformer(spells))

    print(f"\n{Y}{BOLD}Testing mage stats...{RESET}")
    print(mage_stats(mages))

    print("\n" + f"\033[38;5;166m████{RESET}" * 20)


if __name__ == "__main__":
    main()
