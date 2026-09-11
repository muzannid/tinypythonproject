# Python Learning Notes
## Project 2 — Simple Calculator

---

## What This Project Does

A terminal calculator that:
- Takes two numbers and an operator from the user
- Performs the calculation and displays the result
- Validates all inputs — re-asks on invalid entry instead of crashing
- Loops until the user chooses to exit

## Concepts Covered

### 1. `def` — Defining a Function

A function is a reusable block of code you define once and call whenever you need it. It keeps your logic organized and avoids repeating code.

```python
def calculate(firstnum, secondnum, operation):
    # function body here
```

**Rules:**
- Must be defined **before** it is called — Python reads top to bottom
- Parameters go inside the parentheses — these are the inputs the function expects
- The body must be indented

**Structure:**
```python
def function_name(parameter1, parameter2):
    # do something
    return result
```

---

### 2. `return` — Sending a Value Back Out of a Function

`return` exits the function immediately and hands a value back to whoever called it.

```python
def calculate(firstnum, secondnum, operation):
    if operation == "+":
        return firstnum + secondnum   # exits here, sends the sum back
```

**Key behaviors:**
- Once Python hits `return`, the function stops — nothing below it runs
- Without `return`, a function silently gives back `None`
- A function can have multiple `return` statements — the first one hit wins

```python
result = calculate(10, 5, "+")   # result = 15
```

---

### 3. `float()` — Decimal Number Conversion

Like `int()` but handles decimal numbers. Used instead of `int()` when you want the calculator to accept values like `3.14` or `2.5`.

```python
float("3.14")   # returns 3.14
float("10")     # returns 10.0
float("abc")    # throws ValueError
```

**`int()` vs `float()`:**

|          | `int()`      | `float()`          |
|---       |---           |---        c        |
| Input    | `"10"`       | `"10"` or `"10.5"` |
| Output   | `10`         | `10.0` or `10.5`   |
| Decimals | ✗ truncates | ✓ keeps them       |

Use `float()` for any calculation that might involve decimals.

---

### 4. `in` and `not in` — Membership Check

Checks whether a value exists inside a list (or string, or tuple).

```python
"+" in ["+", "-", "*", "/"]      # True
"%" in ["+", "-", "*", "/"]      # False

"+" not in ["+", "-", "*", "/"]  # False
"%" not in ["+", "-", "*", "/"]  # True
```

**Why use this instead of multiple `if` checks:**
```python
# verbose — hard to read
if operation != "+" and operation != "-" and operation != "*" and operation != "/":

# clean — same result
if operation not in ["+", "-", "*", "/"]:
```

You'll use `in` / `not in` constantly — checking valid commands, checking if a key exists in a dict, checking if a word is in a list, etc.

---

### 5. Nested Loops — A Loop Inside a Loop

A `while` loop can sit inside another `while` loop. The inner loop runs completely before the outer loop continues.

```python
while continue_calculation:       # outer loop — runs the whole calculator
    ...
    while True:                   # inner loop — keeps asking until valid operator
        operation = input("Enter operation:\n")
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid")
            continue              # continue here = back to TOP OF INNER LOOP
        break                     # break here = exits INNER LOOP only
    ...
```

**Critical distinction:** `continue` and `break` always apply to the **innermost loop** they're inside. A `break` inside the inner loop only exits the inner loop — the outer loop keeps running.

---

### 6. Division by Zero — Handling Inside the Function

Division by zero is a `ZeroDivisionError` in Python. Rather than letting it crash, handle it explicitly inside the function before it happens:

```python
elif operation == "/":
    if secondnum == 0:
        return "Error: cannot divide by zero"   # exit early with error message
    return firstnum / secondnum                  # only runs if secondnum != 0
```

This pattern — checking for a bad condition first and returning early — is called a **guard clause**. It keeps the happy path clean and unindented.

---

### 7. `.lower()` — String Method for Case-Insensitive Comparison

Converts a string to all lowercase. Used so the user can type `Y`, `y`, `YES`, `yes` and they all match the same condition.

```python
continue_choice = input("Continue? (y/n): ")
if continue_choice.lower() == "y":
    ...
```

`.lower()` doesn't modify the original variable — it returns a new lowercase version you compare against. Other useful string methods in the same family:

| Method | What it does |
|---|---|
| `.lower()` | `"YES"` → `"yes"` |
| `.upper()` | `"yes"` → `"YES"` |
| `.strip()` | `" hello "` → `"hello"` (removes whitespace) |
| `.replace(a, b)` | replaces all occurrences of `a` with `b` |

---

### 8. Dead Code — Code That Can Never Run

Dead code is code that exists in your file but can never actually be reached during execution. It's not an error — Python won't complain — but it's a sign of a logic issue worth cleaning up.

**Example from this project:**
```python
# After adding the while True validation loop for operation,
# this check can never trigger — an invalid operation is caught before calculate() runs
result = calculate(firstnum, secondnum, operation)
if result == "Invalid operation":   # dead code — unreachable
    print("Invalid operation...")
    continue
```

When you add validation earlier in the flow, always check whether downstream validation is now redundant.

---

### 9. Guard Clause Pattern

A guard clause checks for a bad/invalid condition at the top of a block and exits early, keeping the main logic clean and flat.

```python
# without guard clause — nested and hard to read
elif operation == "/":
    if secondnum != 0:
        return firstnum / secondnum
    else:
        return "Error"

# with guard clause — clean, flat
elif operation == "/":
    if secondnum == 0:
        return "Error: cannot divide by zero"   # exit early
    return firstnum / secondnum                  # happy path, no else needed
```

You'll see this pattern everywhere in professional Python code.

---

## New Patterns Introduced in This Project

### Function before everything else
Always define functions at the top of the file, before any code that uses them:
```
def calculate(...)   ← define first
    ...

while True:          ← use below
    result = calculate(...)
```

### Input → Validate → Use
Every input follows this three-step pattern:
```
get input from user
    ↓
validate it (try/except, not in, == 0 check)
    ↓
only then use it in calculation
```

### Nested loop for re-asking
When an input has a fixed set of valid options, wrap it in a `while True` + `break` loop so invalid input re-asks automatically:
```python
while True:
    value = input("Enter valid option:\n")
    if value not in valid_options:
        print("Invalid, try again")
        continue
    break   # only exits when input is valid
```

---

## Key Lessons From This Project

1. Define functions **before** calling them — Python reads top to bottom
2. Use `float()` instead of `int()` when decimals are possible
3. `not in [list]` is cleaner than chaining multiple `!=` conditions
4. `continue` and `break` apply to the **innermost** loop they're in — nested loops give you precise control over which loop to affect
5. Guard clauses (check bad condition first, return early) keep code flat and readable
6. After adding upstream validation, check whether downstream validation became dead code

---

*Next project: Student Grade Tracker — dicts, loops, basic math*
