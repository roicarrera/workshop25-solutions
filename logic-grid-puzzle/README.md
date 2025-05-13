# 🧩 The Messy Test Matrix – Logic Puzzle Challenge

## 🔍 Context

Five different software testing scenarios were recently executed by an outsourced QA vendor with, let’s say… *“a unique approach to testing”*. The documentation is a mess, the reports contradict each other, and no one knows for sure which tool was used for what, in which environment, or even what the objective of each test was. All we know is that each scenario had one:

- **Environment** (Local, CI/CD, Staging, QA, UAT)
- **Testing Level** (Unit, API, Integration, UI, Acceptance)
- **Objective** (New Feature, Regression, Performance, Smoke, Compatibility)
- **Pattern/Approach** (TDD, BDD, Exploratory, Mocking, POM)
- **Tool** (JUnit, Cucumber, Selenium, JMeter, Postman)

No two scenarios share any of these attributes — but they’re all completely jumbled. Your task is to deduce the correct configuration of each scenario using only the logic-based clues below.

The original team clearly didn’t understand testing best practices — so don’t be surprised if some of the combinations make no sense from a real-world perspective. Once you've figured out the correct mapping, **your job doesn't end there**: reflect on the results and suggest how you would reassign or redesign the combinations to reflect solid testing principles.

---

## 🧠 Your Task

1. Read the clues below carefully.
2. Deduce the only possible valid configuration that fits all of them.
3. Submit your result using the JSON format provided in `my_results.json`.
4. Run the `checker` to see how many values you got right (but it won’t tell you the correct answers).
5. After solving it correctly, propose a *realistic* version of the test plan.

---

## 🧩 The Clues

- The scenario that tested the **API** used **Cucumber**, and it was **not a regression test**.
- The tests executed in the **QA environment** are of a **lower level** than those using the **Page Object Model**, but of a **higher level** than those targeting **performance**.
- The **acceptance tests** were written in **Python**, but the **smoke tests** could not be written in that language.
- The scenario that used **JMeter** was either for **integration testing** or **acceptance testing**.
- The **Page Object Model** wasn’t used in any scenario that involved **deployment**, but both the **smoke tests** and those using **Postman** were deployed.
- **Selenium** was either used for **compatibility testing** or executed in the **staging environment**, but **not both**.
- One of the **non-functional testing** scenarios used **BDD** and was executed in the **staging environment**.
- The test using **Selenium** did **not use mocking**; however, any test that used **mocking** had to be written in **Java**.
- Tests for **new features** and **exploratory tests** were neither **unit tests** nor did they use **Postman**.
- Neither **regression tests** nor **unit tests** required **scripting**, but the **TDD-based** scenario did require it.
- No **functional** test was performed at the **acceptance level**.
- **Integration tests** were executed in the **CI/CD environment**.
- The scenario using the **Page Object Model** was executed in an **earlier environment** than the one testing a **new feature**.
- The scenario using **TDD** was executed in a **later environment** than the **smoke tests**.

---

## 📤 Submitting Your Solution

Fill out the `my_results.json` file with your guessed configuration. Each array should include **exactly 5 values** in the order of positions 1 to 5. For example:

```json
{
  "Environment": ["QA", "CICD", "UAT", "Local", "Staging"],
  "Level": ["Unit", "API", "UI", "Integration", "Acceptance"],
  "Objective": ["Regression", "Smoke", "New Feature", "Performance", "Compatibility"],
  "Pattern": ["TDD", "Exploratory", "BDD", "Mocking", "POM"],
  "Tool": ["JUnit", "Postman", "Cucumber", "JMeter", "Selenium"]
}
```

Run the script with:

```bash
python checker.pyc my_results.json
```

The checker will mark each value with:

* ✅ if it's correct
* ❌ if it's incorrect
* ⚠️ if it's not a valid value for that category

## 🧠 Final Challenge

Once you've solved the puzzle:

> 🔁 Look at the resulting combinations and ask yourself: "**Do these test designs make sense?**"
>
> 🛠 Propose your own version of the matrix with combinations that follow good testing practices.
