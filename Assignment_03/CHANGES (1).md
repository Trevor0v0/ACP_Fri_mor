# Assignment 03 — CHANGES

**Name:** ______________________  **Student ID:** ______________________

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | *e.g. product stored as a bare tuple `("Laptop", 1200.0, "electronics")`* | *`Product` class with `name`, `price`, `category`* | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | *e.g. repeated `if tier == ...` for discount and points* | *`Gold`/`Silver`/… subclasses with `discount_rate()` and `points_mult`* | Polymorphism | PASS |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> _your reflection..._

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Refactor this tier discount if/elif into subclasses"* | *Base `Customer` + 4 subclasses* | Edited (renamed methods) | Self-test PASS; read every line |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
