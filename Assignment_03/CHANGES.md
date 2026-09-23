# Assignment 03 — CHANGES

**Name:** Aung Khant Paing (Trevor)  **Student ID:** 6705140082

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products, customers, orders, and line items were represented by tuples and index lookups. | Added `Product`, `OrderItem`, `Customer`, and `Order` objects; orders compose customers and items, and items compose products. | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | Discount and points behavior used tier `if/elif` chains. | Added customer subclasses and a tier-to-class registry; subclass rates and multipliers provide the behavior. | Inheritance / polymorphism | Ran `python Assignment_03.py` → PASS; inspected each tier's constants. |
| 3 | Calculation and receipt output were mixed inside `calc`. | Added calculation methods that return values and a separate `receipt()` method that builds receipt text. | Pure calculations / separation of concerns | Compared captured output against the legacy golden output with the self-test. |
| 4 | Constructors did not validate quantities or object state. | Constructors now validate product fields, customer names, item product/quantity, and order contents. | Encapsulation / validation | Ran self-test; checked invalid quantity and composition cases by reading validation paths. |
| 5 | Tax decisions and business values relied on conditional logic and numeric literals; legacy calculation declared a `global`. | Named the thresholds/rates; products expose their tax rate; new calculations use no global state. | Encapsulation / constants / polymorphism | Ran `python Assignment_03.py` → PASS; checked the refactored section for global declarations. |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> Using classes improved the code most because named attributes like `product.price` are easier to understand than remembering tuple positions. An order item keeps a product together with its quantity, and a quantity of zero would mean nothing was ordered. The customer subclasses show why silver earns twice the base points and gold earns three times the base points. I had to preserve the original discount boundary: a subtotal of exactly 100 still gets the lower rate, while tax is calculated item by item because food and other products have different rates. I also kept the receipt order, rounding, and blank lines the same. I checked the result with the provided self-test, which compares the new output with the original output.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "can you help me with assignment 3" | Explained the assignment and drafted the refactor: domain classes, composition, tier subclasses, validation, named constants, and matching receipt generation. | Edited and reviewed | Ran the provided self-test and discussed the classes and business rules step by step. |
| 2 | "can you guide me each steps to do on my own"; "IDK can u explain me"; "which line i cant find" | Walked through tuple indexing, constructors, quantity validation, tier multipliers, subtotal boundaries, pure returns, and tax behavior with short questions. | Used as explanations; reviewed the code while following the walkthrough. | Explained the concepts in my own words during the conversation and checked the self-test result. |
| 3 | "can you do everything that needs to do with my assignment" | Completed the written change table and reflection draft, checked the remaining submission items, and reran the self-test. | Edited and reviewed; name and student ID left for me to enter. | Self-test printed PASS; I reviewed the reflection and ownership statement. |

**Ownership statement.** [x] *I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] In the refactored solution, products, orders, and line items are objects.
- [x] No tier condition chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; refactored calculations use named constants and no `global`.
- [x] The change table and reflection are filled in.
- [x] The prompt log reflects the AI help in this conversation.
- [x] I understand and can explain every line, and have checked the ownership statement above.
