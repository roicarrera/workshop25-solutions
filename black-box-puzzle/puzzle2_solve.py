from hidden_engine.hidden_checker import HiddenChecker

# Replace this with your guessed test cases (5 new ones)
examples = [
    ('high', 'high'),
    ('low', 'high'),
    ('apple', 'low'),
    ('peach', 'medium'),
    ('nurse', 'medium')
]

checker = HiddenChecker(puzzle_id=1)
result = checker.check(examples)
