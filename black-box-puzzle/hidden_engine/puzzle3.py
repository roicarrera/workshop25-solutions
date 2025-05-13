def main(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))