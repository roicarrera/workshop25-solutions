# Unit Test Design Challenge: Grade Classifier

## Objective

Explore the quality of your unit tests and learn about techniques such as:
- **Equivalence Partitioning**
- **Boundary Value Analysis**
- **Mutation Testing**
- **Input Validation**
- **Code Coverage vs. Test Effectiveness**

---

## Phase 1: Understand the Function

Navigate in your terminal to this task's folder:

```bash
cd Task1
```

Export the project root to PYTHONPATH so Python can locate the module correctly:

```bash
export PYTHONPATH=.
```

Start by reviewing the function `classify_grade(score)` located in `classifier.py`.

This function takes a numeric score and returns a letter grade. Focus on the logic, read the docstring carefully, and form an idea of how it behaves.

---

## Phase 2: Write Basic Unit Tests

In `test_classifier.py`, begin by:
- Writing one **typical test case** for each expected grade category.
- Do **not** worry (yet) about edge cases, invalid inputs, or advanced test design.

Once your tests are written, run the suite using:

```bash
pytest
```

Check that all tests pass. Next, check the **code coverage**:

```bash
pytest --cov=classifier
```

You might find that your coverage is 100%. Great! But...

---

## Phase 3: Now, Think Critically

100% coverage means every line of code was **executed**, but does that mean it's **tested well**?

What happens if there’s a bug right at the boundary between B and A? Or if someone passes a float instead of an integer?

Now is the time to:
- Identify **equivalence partitions**.
- Add **boundary tests** (e.g. 89/90, 100/101, etc.).
- Add tests for **invalid inputs** (e.g., `-1`, `111`, `"90"`, `None`, `85.5`).

You’ll now begin to see where flaws might appear — even with full coverage.

---

## Phase 4: Mutation Testing 🔬

Now let’s test your tests — using **mutation testing** with [`mutmut`](https://github.com/boxed/mutmut).

Mutation testing simulates small bugs in your code (called **mutants**) and checks whether your tests catch them.

### How to Run It

1. Initialize the mutants:

```bash
mutmut run
```

2. Then check the results:

```bash
mutmut results
```

3. If you see any **surviving mutants**, you can inspect them individually:

```bash
mutmut show <mutant ID>
```

### Understanding the Results

Each **mutant** is a small change in your code (like changing `>=` to `>` or replacing a constant). The report will show:

- **killed** – the mutant was detected (your test failed as expected ✅)
- **survived** – your tests didn’t catch the mutant ❌
- **incompetent** – the mutant caused a runtime error

Your goal: **kill as many mutants as possible**. If a mutant **survives**, ask:

- Did we forget an edge case?
- Is the equivalence class properly tested?
- Is the logic under-tested?

---

## Phase 5: Strengthen Your Tests

Based on the surviving mutants, go back and:
- Add or refine test cases to catch them.
- Use techniques like **boundary value analysis** and **input validation** to target tricky logic.
- Re-run mutation testing until most or all mutants are killed.

This iterative approach builds a strong, well-tested function.

---

## Bonus Challenges

- Use `pytest.mark.parametrize` to refactor your test cases.
- Manually explore how bugs might hide at edges.
- Discuss: which tests were *redundant*, and which ones *really mattered*?

---

## Run All Tests Together

```bash
# Run your test suite with coverage
pytest --cov=classifier

# Run mutation testing
mutmut run
mutmut results
```

---

By the end of this exercise, you’ll see that:
- Coverage isn’t everything.
- Edge cases matter.
- Mutation testing reveals real weaknesses.
- **Good tests think like a bug.**
