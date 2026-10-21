"""Небольшой класс с арифметической логикой для модульного тестирования."""

from math import isqrt


class Calculator:
    """Складывает, делит и проверяет простоту целого числа."""

    def add(self, first: int, second: int) -> int:
        """Вернуть сумму двух чисел."""
        return first + second

    def divide(self, dividend: int, divisor: int) -> float:
        """Вернуть частное; при нулевом делителе Python вызовет ZeroDivisionError."""
        return dividend / divisor

    def is_prime_number(self, number: int) -> bool:
        """Вернуть True, если целое число больше 1 и не имеет делителей."""
        if number < 2:
            return False
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True
