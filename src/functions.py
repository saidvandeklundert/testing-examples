def multiply(a: int, b: int) -> int:
    return a * b


def divide_small_numbers(a: int, b: int) -> float:
    if a > 100 or b > 100:
        raise ValueError("Not accepting numbers over 100")
    return a / b
