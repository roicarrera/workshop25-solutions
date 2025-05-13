from . import puzzle1, puzzle2, puzzle3, puzzle4

class HiddenChecker:
    def __init__(self, puzzle_id):
        self.func = [
            puzzle1.main,
            puzzle2.main,
            puzzle3.main,
            puzzle4.main
        ][puzzle_id]

    def check(self, examples):
        correct = 0
        wrong = []
        for i, (inp, expected) in enumerate(examples):
            if self.func(inp) == expected:
                correct += 1
            else:
                wrong.append(i)
        print(f"Total cases: {len(examples)}")
        print(f"Correctly matched: {correct}")
        print("Check your logic again!" if correct < len(examples) else "Looks like you've got the rule!")
        return {
            "total": len(examples),
            "correct": correct,
            "incorrect_indices": wrong
        }