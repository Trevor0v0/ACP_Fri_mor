# Air Conditioner Bug Fixes Notes

## Reminder: used AI to fix errors and took notes for explanations from AI

This document details the six bugs identified and fixed in `ac.py` to ensure robust validation and correct state management[cite: 1, 2].

---

## 1. AttributeError in `__str__`
* **Issue:** Printing the object raised `AttributeError: 'AirConditioner' object has no attribute 'fan'`[cite: 1, 2].
* **Why it happened:** The `__str__` method referenced `self.fan`, but the attribute stored during initialization was named `self.fan_speed`[cite: 1].
* **How it was fixed:** Updated `self.fan` to `self.fan_speed` in the `__str__` string formatting[cite: 1].

---

## 2. RecursionError in `temperature` Setter
* **Issue:** Assigning a value to `ac.temperature` caused a `RecursionError: maximum recursion depth exceeded`[cite: 1, 2].
* **Why it happened:** Inside the property setter, the assignment `self.temperature = value` re-triggered the `@temperature.setter` method continuously in an infinite recursive loop[cite: 1].
* **How it was fixed:** Changed the internal assignment to target the private underlying variable `self._temperature = value`[cite: 1].

---

## 3. Stale State in `is_energy_saving`
* **Issue:** `is_energy_saving` did not update when `temperature` changed[cite: 1, 2].
* **Why it happened:** The original code set `self._is_energy_saving` once inside `__init__`, making it a static snapshot that ignored subsequent temperature updates[cite: 1].
* **How it was fixed:** Converted `is_energy_saving` into a read-only dynamic `@property` that computes `self.temperature >= 25` on-the-fly whenever accessed[cite: 1].

---

## 4. Range Validation Logical Flaw
* **Issue:** Invalid values like `5` or `40` were accepted without raising errors[cite: 1, 2].
* **Why it happened:** The guard check used `and` (`if value < MIN_TEMP and value > MAX_TEMP`), which is mathematically impossible for a single integer to satisfy[cite: 1].
* **How it was fixed:** Changed the operator to `or` (`if value < self.MIN_TEMP or value > self.MAX_TEMP`) so any value strictly outside the bounds triggers a `ValueError`[cite: 1].

---

## 5. Constructor Bypassing Validation
* **Issue:** Instantiating `AirConditioner("LG", "Office", temperature=99)` accepted `99` without raising a `ValueError`[cite: 1, 2].
* **Why it happened:** `__init__` assigned values directly to `self._temperature`, bypassing the validation rules inside `@temperature.setter`[cite: 1].
* **How it was fixed:** Updated `__init__` to assign to `self.temperature` instead of `self._temperature`, forcing initial values through the setter guard logic[cite: 1].

---

## 6. `cooler()` Lower Limit Breach
* **Issue:** Calling `ac.cooler()` at `16°C` dropped the temperature to `15°C`, breaching `MIN_TEMP`[cite: 1, 2].
* **Why it happened:** `cooler()` subtracted `1` directly from `self._temperature` without checking limits or invoking setter guards[cite: 1].
* **How it was fixed:** Updated `cooler()` to assign `self.temperature = max(self.MIN_TEMP, self.temperature - 1)`, guaranteeing the temperature never falls below `MIN_TEMP`[cite: 1].