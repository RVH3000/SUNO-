"""Generate Deep House / Techno song title ideas."""

from __future__ import annotations

import random
from typing import Callable, Iterable, List, Optional

# Datenbank der Vektoren (Erweiterbar)
HARDWARE = [
    "Voltage",
    "Circuit",
    "Phase",
    "Bias",
    "Oscillator",
    "Gate",
    "Trigger",
    "Flux",
    "Signal",
    "Input",
    "909",
    "Tanzbaer",
]
TEXTURE = [
    "Dust",
    "Grain",
    "Static",
    "Hiss",
    "Blur",
    "Resonance",
    "Filter",
    "Raw",
    "Distortion",
    "Saturated",
    "Granular",
]
EMOTION = [
    "Memory",
    "Left",
    "Waiting",
    "Drifting",
    "Holding",
    "Void",
    "Silence",
    "Echo",
    "Patterns",
    "Cycles",
    "Lost",
]
URBAN = [
    "Concrete",
    "Transit",
    "Sector",
    "Dawn",
    "Warehouse",
    "Floor",
    "Asphalt",
    "Basement",
    "Grid",
    "City",
]


def build_structures(rng: random.Random) -> List[Callable[[], str]]:
    """Return combination templates for title generation."""
    return [
        lambda: f"{rng.choice(TEXTURE)} {rng.choice(EMOTION)}",
        lambda: f"{rng.choice(HARDWARE)} {rng.choice(URBAN)}",
        lambda: f"{rng.choice(EMOTION)} in {rng.choice(URBAN)}",
        lambda: f"{rng.choice(TEXTURE)} {rng.choice(HARDWARE)}",
        lambda: f"{rng.choice(URBAN)} {rng.choice(EMOTION)}",
        lambda: f"{rng.choice(EMOTION)} State",
        lambda: f"{rng.choice(HARDWARE)} Loop {rng.randint(1, 99)}",
    ]


def generate_titles(
    count: int = 20,
    *,
    seed: Optional[int] = None,
) -> Iterable[str]:
    """Generate title ideas.

    Args:
        count: Number of titles to generate.
        seed: Optional seed for reproducible output.
    """
    if count < 1:
        raise ValueError("count must be at least 1")

    rng = random.Random(seed)
    structures = build_structures(rng)

    for _ in range(count):
        yield rng.choice(structures)()


def main() -> None:
    """CLI entry point."""
    print("--- GENERIERTE TITEL (Deep House / Techno) ---")
    for title in generate_titles():
        print(title)


if __name__ == "__main__":
    main()
