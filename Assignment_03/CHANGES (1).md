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
| 1 | "can you help me with assignment 3" | The AI read the assignment, drafted the refactored code and change-table entries, and ran the provided self-test. | AI-drafted; I discussed the design and business rules in the walkthrough. | The AI ran `python Assignment_03.py`; it printed PASS. |
| 2 | "can you guide me each steps to do on my own"; "IDK can u explain me" | The AI explained tuple indexing, constructors, quantity validation, membership multipliers, the subtotal boundary, returned values, and product tax. I answered its questions about these topics. | Used as explanations; I responded to the walkthrough questions. | I explained several concepts in my own words during the conversation. |
| 3 | "can you explain ownership statement" | The AI explained the ownership statement and gave the command to run the self-test. | Used as guidance. | The AI ran the self-test and reported PASS. |
| 4 | "can you add calculation methods that return values and a separate reciept method." | The AI pointed out that `Order.subtotal()`, `discount()`, `tax()`, `total()`, and `points()` already return calculation results, while `Order.receipt()` builds the receipt text. No code change was needed for this request. | Existing implementation reviewed. | Checked the `Order` class and the self-test result. |

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
