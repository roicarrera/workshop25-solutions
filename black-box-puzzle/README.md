# Black Box Puzzle Challenge

Welcome to the Black Box Testing Challenge! Your mission is to reverse-engineer the logic of a hidden function using only input/output behavior.

## 🧩 What You Have

For each puzzle (puzzle1_solve.py to puzzle5_solve.py):
- You are given a set of initial input/output examples (read the file).
- You do NOT know how the function works internally.
- You must guess the logic and add **5 new test cases** of your own to confirm your theory.

Each script calls a hidden checker, which will tell you:
- How many of your 5 guessed examples match the actual output.
- Which indices of your guesses are wrong.

## 🛠 How to Play

1. Open one of the `puzzleX_solve.py` files.
2. Fill in the `examples` list with 5 new test cases and what you think the function should return.
3. Run the script.
4. If you get all 5 right, you likely cracked the rule!

You’re simulating a **black-box tester**: no access to code, only behavior.

Good luck!