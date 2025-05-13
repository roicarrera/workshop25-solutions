# Facilitator's Audit Sheet

Known flaws:

1. TC-01: Combines two goals (login & dashboard) → not atomic
2. TC-02: Vague — does not describe expected result (missing oracle)
3. TC-03: Only tests a valid case, not rejection → missing negative path
4. TC-04: Tests two transitions (fail → success), unclear scope
5. TC-05: Locks after 10 attempts, REQ-003 says 5 → mismatch
6. TC-06: No mention of admin rights → missing authorization check
7. TC-07: Weak verb, unclear what is being verified
8. TC-08: Redundant with TC-01

Bonus flaws:
- REQ-004 (audit logging) is entirely untested.
- No negative or invalid password tests
- No tests mention edge cases (e.g. empty passwords, expired accounts)

Techniques teams might invoke:
- State transition testing (login fail → lock → unlock)
- Oracle quality / assertion clarity
- Negative testing
- Equivalence classes (password variants)
- Risk-based prioritization
- Test smells (vague names, duplication, lack of independence)
