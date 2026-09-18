# Week 3 In-Class Lab — Fix the Broken Air Conditioner

**192-201 · OOP II: Encapsulation**  ·  **AI-use: Level 1** (AI may *explain* an error message; it may **not** fix the class for you)

## The situation

The QA team filed a bug report against the `AirConditioner` class. It was supposed to make invalid settings *impossible* — but it crashes on start-up, accepts a temperature of 5°C, and its "energy-saving" light is stuck on. **Your job: make it behave.**

You have two files:
- `ac.py` — the broken class. **This is the only file you edit.**
- `check.py` — an automatic checker. **Do not edit it.** Run it to see what's still wrong.

## How to work

1. Run the checker:  `python check.py`
2. Read the **first** failure and its error message. Fix that one thing in `ac.py`.
3. Run `check.py` again. Repeat until you see `6/6 checks passing`.
4. Commit after each fix with a message saying what you fixed, e.g. `fix: stop setter recursing`.

> Golden rule of debugging: **get it to run first, then get it right.** The crashes come before the logic bugs.

## The bug report (6 issues)

The checker will guide you, but here is what QA observed, in plain language:

1. **It won't even print.** Creating an AC and printing it throws an `AttributeError`.
2. **Setting the temperature hangs / crashes** with a `RecursionError`.
3. **The energy-saving light never updates.** Lower the temperature to 22°C and it *still* says energy-saving.
4. **Bad temperatures are accepted.** `ac.temperature = 5` and `ac.temperature = 40` should be refused — they aren't.
5. **The constructor lets bad data in.** `AirConditioner("LG", "Office", temperature=99)` should be refused — it isn't.
6. **`cooler()` breaks the floor.** Starting at 16°C, calling `cooler()` pushes it to 15°C.

## Definition of done

`python check.py` prints:
```
[PASS] 1. Builds and __str__ works
[PASS] 2. A valid temperature is stored
[PASS] 3. is_energy_saving reflects the CURRENT temperature
[PASS] 4. Out-of-range temperature is rejected
[PASS] 5. The constructor also rejects bad values
[PASS] 6. cooler() never drops below the minimum

6/6 checks passing
```

## While you work, be ready to answer

- Which line was causing the `RecursionError`, and *why* does storing into `self._temperature` fix it?
- Bug 5 still lets `99` through even after you fix the setter. What was the constructor doing wrong?
- Why should `is_energy_saving` be **calculated** each time instead of stored once?

## Allowed AI use (Level 1)

You may paste an **error message** and ask the AI *"what does this mean?"*. You may **not** paste the class and ask it to fix the bugs. If you ask the AI anything, write the question in `NOTES.md`. You must be able to explain every fix in the wrap-up.

## Finished early? (stretch)

- Add a `mode` bug of your own on purpose, watch a check fail, then fix it — prove you understand the setter pattern.
- Make `cooler()`/`warmer()` return the new temperature so `print(ac.cooler())` works.
- Add a read-only property `status_light` that returns `"green"` when energy-saving else `"amber"`.
