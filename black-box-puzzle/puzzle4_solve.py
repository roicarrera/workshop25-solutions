from hidden_engine.hidden_checker import HiddenChecker

# Replace this with your guessed test cases (5 new ones)
examples = [
    ('racecar', True),
    ('reverb', False),
    ('rotator', True),
    ('airplane', False),
    ('civic', True)
]

checker = HiddenChecker(puzzle_id=3)
result = checker.check(examples)
