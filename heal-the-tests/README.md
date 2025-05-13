# 🏥 Test Hospital: Heal the Tests

Welcome to **Test Hospital**, a 30-minute skill-up game where you act as "test doctors" and rescue broken test code using pattern-based syringes.

Each test file is a **patient** with a specific symptom. Your job is to apply the correct **treatment** and refactor the test with clean, reusable patterns.

---

## 💡 Objective

Learn the following test design patterns:

- 🔹 Fixture Factory (`@pytest.fixture`)
- 🔸 Test Data Builder (class-based modular input creation)
- 🟢 Assertion Helper (encapsulating complex assert logic)

---

### ✅ Run Tests

```bash
pytest patients/
```

You'll see some messy but working tests.

## 🚑 Your Mission: Heal the Patients

You’ll find 3 patients in `patients/.` Each one has a symptom and a suggested treatment in the comments.
Navigate to each file and follow the steps inside.

### 👨‍⚕️ Patient 1: Duplicate Setup

> **Symptom**: Redundant code across test functions
>
> 💉 Use the `blue_syringe_fixture_factory.py` in `/treatments`

### 🧪 Patient 2: Hardcoded Data

> **Symptom**: Repetitive, rigid input data
>
> 💉 Use the `yellow_syringe_data_builder.py`

### 🤢 Patient 3: Spaghetti Assertions

> **Symptom**: Confusing, verbose assert logic
>
> 💉 Use the `green_syringe_assertion_helper.py`

### 🤢 Patient 4: Parametrized values

> **Symptom**: Repetitive, non logic focused
>
> 💉 Use the `purple_syringe_assertion_helper.py`

---

After that, you can:

- Refactor all 3 patients into a single, clean `tests/` module

- Try combining two or more treatments
