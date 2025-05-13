from hidden_engine.hidden_checker import HiddenChecker

# Replace this with your guessed test cases (5 new ones)
examples = [
    ([1, 2, 3], True),
    ([3, 2, 1], False),
    ([4, 4, 4], True),
    ([1, 2, 1, 2], False),
    ([3, 3, 2], False)
]

checker = HiddenChecker(puzzle_id=2)
result = checker.check(examples)
