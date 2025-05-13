from hidden_engine.hidden_checker import HiddenChecker

# Replace this with your guessed test cases (5 new ones)
examples = [
    ([1, 2, 3],  True),
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 4, 5], False),
    ([2, 4, 6], True),
    ([1, 3], False)
]

checker = HiddenChecker(puzzle_id=0)
result = checker.check(examples)
