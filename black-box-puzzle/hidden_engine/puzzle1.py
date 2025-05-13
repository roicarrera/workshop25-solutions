def main(numbers):
    evens = sum(1 for n in numbers if n % 2 == 0)
    odds = sum(1 for n in numbers if n % 2 != 0)
    return (evens % 2 == 1) and (odds % 2 == 0)