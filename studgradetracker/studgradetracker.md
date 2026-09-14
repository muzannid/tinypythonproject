# Python Learning Notes
## Project 3 — Student Grade Tracker

---

## What This Project Does

A terminal program that manages a class of students and their grades. You can:
- Add new students
- Add grades for existing students
- View all students with their grades and average
- Find the highest and lowest scorer
- Data lives in memory for the whole session

## Concepts Covered

### 1. Dictionary of Lists — Main Data Structure

A dictionary where each key is a student name and each value is a **list** of their grades. This lets one student hold multiple grades that can grow over time.

```python
students = {
    "muzan":  [80, 50],   # key = name (str), value = list of grades
    "daniel": [50],
    "wan":    [70],
}
```

**Why a list and not a set `{}`:**

|                   | List `[]` | Set `{}`            |
|---                |---        |---                  |
| Allows duplicates | ✓ yes     | ✗ silently ignores |
| Keeps order       | ✓ yes     | ✗  no              |
| Use `.append()`   | ✓ yes     | ✗ uses `.add()`    |

Always use a list when you need to store multiple values for one key and order/duplicates matter.

**Accessing nested values:**
```python
students["muzan"]        # [80, 50] — the whole list
students["muzan"][0]     # 80 — first grade only
```

---

### 2. `.append()` — Adding to a List

Adds a new item to the **end** of an existing list, in place.

```python
students["muzan"].append(90)
# students["muzan"] is now [80, 50, 90]
```

**`.append()` vs `.add()`:**
- `.append()` is for **lists** — adds to the end
- `.add()` is for **sets** — adds without order or duplicates

---

### 3. `.items()` — Iterating a Dictionary

`.items()` returns every key-value pair in a dictionary as a tuple. Used with a `for` loop to loop through all entries:

```python
for name, grades in students.items():
    print(name, grades)
# muzan [80, 50]
# daniel [50]
# wan [70]
```

`name` catches the key, `grades` catches the value — both in one line. This is called **tuple unpacking**.

Other dictionary iteration methods:
```python
for name in students.keys():     # keys only — "muzan", "daniel", "wan"
for grades in students.values(): # values only — [80,50], [50], [70]
for name, grades in students.items(): # both together
```

---

### 4. `sum()` and `len()` — Built-in Math Functions

**`sum(iterable)`** — adds up all values in a list:
```python
sum([80, 50, 90])   # 220
```

**`len(iterable)`** — counts how many items are in a list:
```python
len([80, 50, 90])   # 3
```

**Together for average:**
```python
grades = [80, 50, 90]
average = sum(grades) / len(grades)   # 220 / 3 = 73.33
```

**Guard against empty list** — `len([])` is `0`, so dividing by it causes `ZeroDivisionError`. Always check first:
```python
if len(grades) == 0:
    return 0
```

---

### 5. `round()` — Rounding Decimal Numbers

Rounds a float to a specified number of decimal places:

```python
round(73.3333333, 2)   # 73.33
round(84.5678, 1)      # 84.6
round(100.0, 2)        # 100.0
```

**Syntax:** `round(number, decimal_places)`

Without `round()`, averages print as `73.33333333333333` — messy and hard to read.

---

### 6. Reusable Utility Function — `check_list()`

A function whose only job is to check one condition and return `True` or `False`. Used across multiple other functions instead of repeating the same check everywhere.

```python
def check_list():
    if not students:
        print("No students data in the list yet.")
        return False
    return True
```

Called inside other functions:
```python
def display_all_students():
    if check_list():    # reuses the check — no duplication
        ...
```

**Why this matters:** if the check logic ever changes (e.g. you add a minimum student count), you only update it in ONE place — `check_list()` — not in every function that needs it. This is called the **DRY principle** (Don't Repeat Yourself).

---

### 7. Truthy and Falsy Values

In Python, some values are treated as `False` in an `if` condition without needing `== False`:

| Value         | Treated as           |
|---            |---                   |
| `0`           | False                |
| `""`          | False (empty string) |
| `[]`          | False (empty list)   |
| `{}`          | False (empty dict)   |
| `None`        | False                |
| anything else | True                 |

```python
students = {}

if not students:        # True — dict is empty, so "not empty" = True
    print("empty")

if students:            # False — empty dict is falsy
    print("has data")
```

Used in `check_list()`:
```python
if not students:   # same as: if len(students) == 0
```
---

### 8. Guard Clause — Exit Early on Bad Condition

A guard clause checks for an invalid/edge-case condition at the top of a function and returns immediately, keeping the main logic clean and flat below it.

```python
def average_grade(name):
    if len(students[name]) == 0:   # guard — bad condition
        print(f"{name} has no grade yet.")
        return 0                    # exit immediately
    # only reaches here if list is NOT empty
    total = sum(students[name])
    avg = round(total / len(students[name]), 2)
    return avg
```

**Without guard clause — nested and harder to read:**
```python
def average_grade(name):
    if len(students[name]) != 0:
        total = sum(students[name])
        avg = round(total / len(students[name]), 2)
        return avg
    else:
        return 0
```

**Rule:** if a condition means "don't proceed," handle it first and return early. Everything below the guard is the happy path.

---

### 9. Tracking the Best Value While Looping

A common pattern: initialize a "best so far" variable before the loop, update it whenever you find something better during the loop.

```python
def highest_scorer():
    highest_name = ""
    highest_grade = -1          # starting value lower than any possible grade

    for name, grades in students.items():
        avg = average_grade(name)
        if avg > highest_grade:  # is this better than best so far?
            highest_name = name  # update best name
            highest_grade = avg  # update best score

    print(f"Highest: {highest_name} with {highest_grade}")
```

**Why `-1` and `101` as starting values:**
- `highest_grade = -1` — any real grade (0-100) will be higher, so the first student always wins the first comparison
- `lowest_grade = 101` — any real grade (0-100) will be lower, so the first student always wins the first comparison

**More robust alternative for future:**
```python
highest_grade = float("-inf")   # negative infinity — everything beats this
lowest_grade = float("inf")     # infinity — everything is lower than this
```

---

### 10. `return 0` vs `return` vs `return None`

When a function hits `return`, it exits immediately — nothing below runs.

|               | What it returns        | Safe to compare with numbers? |
|---            |---                     |---                            |
| `return 0`    | the integer `0`        | ✓ yes                         |
| `return`      | `None`                 | ✗ no — `None > 5` crashes     |
| `return None` | `None` (same as above) | ✗ no                          |

In `average_grade()`, returning `0` instead of `None` means the caller (`highest_scorer`, `lowest_scorer`) can safely compare the result against a number without crashing.

---

### 11. Symmetric Functions — Mirror Structure

`highest_scorer()` and `lowest_scorer()` are structurally identical — only three things differ:

|                | `highest_scorer()`              | `lowest_scorer()`              |
|---             |---                              |---                             |
| Starting value | `-1`                            | `101`                          |
| Comparison     | `avg > highest_grade`           | `avg < lowest_grade`           |
| Variable names | `highest_name`, `highest_grade` | `lowest_name`, `lowest_grade`  |

**Lesson:** when two functions solve the same problem in opposite directions, keep their structure identical. Fix a bug in one → immediately check if the other needs the same fix.

---

### 12. Dead Code — Code That Can Never Run

Code that exists in your file but can never actually be reached. Not an error — Python won't complain — but a sign of redundant logic worth cleaning up.

**How it happens:** you add upstream validation, which makes downstream validation unreachable.

```python
# After adding check_list() at the top of a function,
# the else branch below becomes dead code if check_list()
# already prints the message and returns False
if check_list():
    ...
else:
    print("Enter Student data first")   # this is now duplicate — check_list() already said this
```

When you add validation earlier in the flow, always ask: "is any check below this now unreachable?"

---

## New Patterns Introduced in This Project

### Dictionary as a database
```
students dict = your in-memory database
keys = unique identifiers (student names)
values = the data belonging to that identifier (list of grades)
```

### Check → Act pattern
Every function that modifies or reads data follows this order:
```
1. check if the subject exists (name in students)
2. only then act on it
```

```python
def addgrade(name, grade):
    if name not in students:    # check first
        print("not found")
    else:
        students[name].append(grade)   # act only if found
```

### Reusable utility functions
Extract repeated checks into their own named function. Call that function everywhere instead of copy-pasting the check:
```
check_list() → called by display_all_students, highest_scorer, lowest_scorer
average_grade() → called by display_all_students, highest_scorer, lowest_scorer
```

---

## Key Lessons From This Project

1. `[]` is a list (ordered, allows duplicates, use `.append()`); `{}` alone is a set (unordered, no duplicates, use `.add()`) — don't mix them up
2. Always guard against `len([]) == 0` before dividing — `ZeroDivisionError` is silent and only shows up at runtime
3. `return 0` vs `return` matters when the caller uses the result in a comparison — `None` can't be compared to numbers
4. Reusable utility functions (`check_list`, `average_grade`) are called from multiple places — changing them once updates every caller automatically
5. When two functions mirror each other (highest/lowest), keep their structure identical — a fix in one likely applies to the other
6. Truthy/falsy: `if not students` is cleaner than `if len(students) == 0` — both mean the same thing
7. Guard clauses keep the happy path flat and readable — check the bad condition first, return early, then write the main logic without nesting

---

*Next project: To-Do List — lists, functions, while True menu*
