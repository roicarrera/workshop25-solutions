# Property-Based Testing Workshop: Invariants and Complex Properties

## Overview

This workshop is aimed at advanced Python developers who are new to **Property-Based Testing (PBT)**. It is structured in two major parts:

1. **Invariant Discovery (Theoretical)** – learn to identify general properties (invariants) of common functions.
2. **Evaluator Testing (Practical)** – implement PBT using Hypothesis to uncover hidden bugs in a seemingly correct function.

By the end of this exercise, you'll gain:

* A strong intuition for reasoning about *what should always be true* in your programs.
* Practical experience using Hypothesis to uncover real bugs.
* A repeatable mental model to apply PBT in your real projects.

---

### Setup

Install the dependencies with

```bash
pip install -r requirements.txt
```

---

## Part 1: Understanding Invariants (Theory-Only)

Invariants are general truths that must always hold about your code, regardless of specific inputs. Rather than checking individual cases (as in example-based testing), invariants express the core logic of your code, capturing its expected behavior in all valid scenarios.

For each function below, there is one example invariant to teach the concept.

### 1. `reverse(xs: list) -> list`

**Description:** Returns the list `xs` in reversed order.

#### 🔹 Given Example Invariant:

* `len(reverse(xs)) == len(xs)` (Reversing a list doesn't change its size.)

---

### 2. `sort(xs: list) -> list`

**Description:** Returns a new list containing the elements of `xs` in ascending order.

#### 🔹 Given Example Invariant:

* `set(sort(xs)) == set(xs)` (The multiset of elements is preserved even if their order changes.)

---

### 3. `deduplicate(xs: list) -> list`

**Description:** Removes duplicate elements from a list, preserving their first occurrence.

#### 🔹 Given Example Invariant:

* `len(set(deduplicate(xs))) == len(deduplicate(xs))` (The result contains only unique elements.)

---

## Instructions for Part 1

1. Read and understand each of the three example functions.
2. Use the given example invariant to build your intuition.
3. Try to come up with two additional invariants for each case.
4. Think critically:

   * Why is this property always true?
   * How does it reflect what the function is supposed to do?
   * What assumptions are you making about inputs?
5. As a bonus, you can try to implement them in the `tests/test_invariants.py` file, where you have the examples' implementations.

Once you’ve internalized this process, you will apply the same reasoning in Part 2 to define and test a real-world property using Hypothesis.

---

## Part 2: Property-Based Testing with Hypothesis

### Scenario: Arithmetic Expression Evaluator

You are given a function `eval_expr(expr: str)` that evaluates arithmetic expressions involving integers, `+`, and `*`. The function is designed to support basic arithmetic., but it contains a subtle bug.

Your goal is to:

1. Understand the function and the limitations of example-based testing.
2. Write a **property-based test** using Hypothesis.
3. Discover the bug via property testing.
4. Fix the bug and validate the solution.

### Steps

#### 🔹 Step 1: Run the example-based tests

* Open `tests/test_example_eval.py`
* Run with `pytest tests/test_example_eval.py`. All tests should pass.

#### 🔹 Step 2: Read the implementation

* Look at `eval_expr()` in `evaluator.py`.
* Understand how it parses tokens.

#### 🔹 Step 3: Write your property-based test

* Use Hypothesis to generate simple valid arithmetic expressions (e.g., combining numbers with `+` and `*`). 
* Define a property the function should uphold.
* More instructions in the `tests/test_property_eval.py` file

#### 🔹 Step 4: Run the property-based test

* Hypothesis should find a counterexample.
* Observe the failure.
* Hypothesis will shrink the input to a minimal failing case.

#### 🔹 Step 5: Fix the bug

* Update `eval_expr()`
* Rerun tests to confirm everything passes.

---

## Final Notes

You now understand two pillars of property-based testing:

* **Invariants**, discovered through reasoning.
* **Complex properties**, based on either internal logic or comparison with known behavior.

Use this skillset to:

* Improve testing confidence.
* Catch bugs early.
* Reduce reliance on fragile examples.

Happy testing!
