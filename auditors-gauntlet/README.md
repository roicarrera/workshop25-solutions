# The Auditor’s Gauntlet

## 📜 Scenario

A system was recently released to production, but a surprise internal audit has uncovered issues in the documentation and planning of the test suite. While all test execution logs appear clean on the surface, something feels... off. You’ve been brought in to analyze the **test design quality**, **traceability**, and **coverage completeness** — and to defend the release before the real audit begins.

Your team will act as QA analysts and test designers to fix what others missed.

---

## 🎯 Objectives

- Identify **flaws or gaps** in the existing test cases: missing coverage, vague phrasing, duplication, requirement mismatch, weak planning.
- Fix the **traceability matrix** so that all requirements are mapped and logically covered.
- Propose 1–2 **improved or new test cases** using actual testing techniques (you may reference the concept cards).
- Rewrite 1–2 of the current test cases to be more effective and compliant.
- Suggest **one process-level improvement** that would prevent these issues in the future.

---

## 🧩 What to Watch For

Think like an auditor. Be alert to:

- Test cases that are **unclear**, too broad, or too vague.
- Tests that seem to **test multiple things** or **repeat** others.
- **Missing tests** for critical paths (e.g. negative cases, boundaries).
- **Incorrect assumptions** or **incomplete requirement coverage**.
- Test cases that don't fully explain what they're verifying or how.

Don’t just look for bugs in the code — look for holes in the **test design** and **planning** itself.

---

## 📁 Provided Materials

- `requirements.txt`: List of product requirements
- `test_cases.txt`: The current set of test cases
- `test_results.txt`: Most recent test execution report
- `traceability_matrix.csv`: The trace matrix (some links may be incorrect or missing)
- `concept_cards/`: Optional cards introducing test techniques you can apply

---

## 📤 Deliverables

Submit the following as a team:

1. ✅ An updated traceability matrix
2. 🕵️ A short list of **at least 4 identified flaws** in the test plan
3. 🧪 Descriptions of **1–2 new test cases** that improve coverage, based on testing techniques
4. 🧹 Rewritten versions of **1–2 existing test cases** to remove test smells or planning gaps
5. 📈 One actionable recommendation to improve test planning processes

---