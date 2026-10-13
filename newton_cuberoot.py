"""Approximate the cube root of a number using Newton's method."""

from __future__ import annotations

import math
import sys


def newton_cuberoot(number: float, tolerance: float = 1e-12, max_iterations: int = 1000) -> float:
    """Return the cube root of ``number`` using Newton-Raphson iteration.

    The iteration is based on solving x^3 - n = 0 with:
        x_{k+1} = (2*x_k + n / x_k^2) / 3
    """
    if math.isnan(number) or math.isinf(number):
        raise ValueError("Input must be a finite real number.")

    if number == 0:
        return 0.0

    sign = -1.0 if number < 0 else 1.0
    absolute_value = abs(number)

    guess = max(1.0, absolute_value / 3.0)
    x = guess

    for _ in range(max_iterations):
        next_x = (2.0 * x + absolute_value / (x * x)) / 3.0
        if abs(next_x - x) < tolerance:
            return sign * next_x
        x = next_x

    return sign * x


def main() -> None:
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Enter a number: ")

    try:
        number = float(user_input)
    except ValueError as exc:
        raise SystemExit(f"Invalid number: {user_input!r}") from exc

    result = newton_cuberoot(number)
    print(f"Cube root of {number} is approximately {result:.12f}")


if __name__ == "__main__":
    main()
