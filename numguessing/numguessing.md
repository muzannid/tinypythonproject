# Python Learning Notes
## Project 1 — Number Guessing Game

---

## Concepts Covered

### 1. `import` — Using Modules

A module is a toolbox of pre-built functions Python ships with. You bring it into your file with `import`.

```python
import random
```

Once imported, you access its tools using dot notation:

```python
random.randint(1, 100)   # go into random module, use the randint tool
```

**Rule:** `import` statements always go at the very top of your file, before any other code.

---

### 2. `random.randint(a, b)` — Generating a Random Integer

Picks one random whole number between `a` and `b`, **inclusive** (both endpoints can be picked).

```python
randomnum = random.randint(1, 100)  # picks any number from 1 to 100
```

Word by word breakdown:
- `random` — the module (toolbox)
- `.` — access operator, "go inside and find"
- `randint` — the function inside the module ("random integer")
- `(1, 100)` — arguments: minimum and maximum of the range
- `randomnum =` — stores the result in a variable

---

### 3. `input()` — Getting User Input

Displays a prompt and waits for the user to type something and press Enter.

```python
guess = input("Enter your guess: ")
```

**Critical rule:** `input()` ALWAYS returns a **string**, even if the user types a number. `"50"` not `50`.

To use the input as a number, convert it:

```python
guess = int(input("Enter your guess: "))
```

Adding `\n` at the end of the prompt moves the cursor to a new line:

```python
guess = int(input("Enter your guess:\n"))
```

---

### 4. `int()` — Type Conversion

Converts a value into an integer (whole number).

```python
int("50")      # returns 50
int("hello")   # throws ValueError — can't convert letters to a number
```

Common conversions:
- `int()` — to whole number
- `float()` — to decimal number
- `str()` — to string
- `bool()` — to True/False

---

### 5. `try` / `except` — Handling Errors Gracefully

Wraps risky code so that if an error occurs, the program handles it cleanly instead of crashing.

```python
try:
    guessnum = int(input("Guess:\n"))   # risky — user might type letters
except ValueError:
    print("Please enter only numbers")
    continue
```

**Structure:**
- `try:` — attempt this block
- `except ErrorType:` — if THIS specific error happens, run this block instead
- Everything after `except` only runs if that error actually occurred

**Rule:** always catch the **specific** error type you expect, not a bare `except:` which catches everything including bugs you didn't intend.

---

### 6. Built-in Exception Types

Python has named error types for every kind of problem. You use these names in `except` clauses:

| Exception | When it happens |
|---|---|
| `ValueError` | Wrong value for the type — `int("abc")` |
| `ZeroDivisionError` | Dividing by zero — `10 / 0` |
| `KeyError` | Dict key doesn't exist — `data["missing"]` |
| `IndexError` | List index out of range — `list[999]` |
| `TypeError` | Wrong type — `"hello" + 5` |
| `FileNotFoundError` | Opening a file that doesn't exist |
| `NameError` | Using a variable before defining it |

These are **not variables you define** — they are pre-built classes Python already knows about. You just point at them in your `except` clause to filter which error you want to catch.

You can catch multiple error types:

```python
try:
    risky_code()
except ValueError:
    print("wrong value")
except ZeroDivisionError:
    print("can't divide by zero")
```

---

### 7. `while` Loop — Repeating Until a Condition is False

Keeps running its block of code as long as the condition is `True`. Stops the moment the condition becomes `False`.

```python
while guessnum != randomnum:
    # this block repeats until guessnum equals randomnum
```

**Structure:**
```
check condition
    ↓ True
run block
    ↓
check condition again
    ↓ True
run block
    ↓
... repeats until condition is False
    ↓ False
exit loop, continue program
```

**Common pattern — infinite loop with manual exit:**
```python
while True:          # always True — runs forever
    # do something
    if done:
        break        # manually exit when ready
```

---

### 8. `if` / `elif` / `else` — Branching Logic

Runs different code depending on which condition is true.

```python
if guessnum < randomnum:
    print("Too low")
elif guessnum > randomnum:
    print("Too high")
else:
    print("Correct!")
```

**Rules:**
- `if` — checked first, always
- `elif` — only checked if all previous conditions were False (short for "else if")
- `else` — runs if nothing above matched, no condition needed
- Only ONE branch runs per evaluation — the first one that matches wins, the rest are skipped

---

### 9. `break` — Exit the Loop Immediately

When Python hits `break` inside a loop, it exits the entire loop right then, regardless of the loop condition. Execution continues at the line after the loop.

```python
while guessnum != randomnum:
    guessnum = int(input("Guess:\n"))
    if guessnum == randomnum:
        break   # correct — stop looping immediately

print("You got it!")   # continues here after break
```

---

### 10. `continue` — Skip to Next Iteration

When Python hits `continue`, it immediately abandons everything below it in the current iteration and jumps back to the top of the loop to check the condition again.

```python
while guessnum != randomnum:
    try:
        guessnum = int(input("Guess:\n"))
    except ValueError:
        print("Numbers only")
        continue        # jump back to top — skip attempts += 1 and if/elif

    attempts += 1       # only reaches here if input was valid
    if guessnum < randomnum:
        ...
```

**Layman version:** "this one doesn't count, try the next one."

---

### 11. `break` vs `continue` — The Distinction

| | What it does | Where it goes |
|---|---|---|
| `continue` | Skip rest of **this iteration** | Back to **top of loop** |
| `break` | Exit the **entire loop** | Line **after the loop** |

```python
while True:
    value = input("Enter something:\n")

    if value == "skip":
        continue    # go back to top, ask again

    if value == "quit":
        break       # exit loop entirely

    print(f"You entered: {value}")
```

---

### 12. `+=` — Increment Shorthand

A shorthand for adding to a variable and storing the result back in itself.

```python
attempts += 1       # same as: attempts = attempts + 1
attempts += 5       # same as: attempts = attempts + 5
```

Works for other operators too:
```python
x -= 1    # subtract
x *= 2    # multiply
x /= 2    # divide
```

---

### 13. f-strings — Embedding Variables in Strings

An f-string lets you embed variables or expressions directly inside a string using `{}` curly braces. The `f` prefix before the quote activates this.

```python
name = "Muzan"
score = 95

print(f"Player {name} scored {score} points")
# Player Muzan scored 95 points
```

You can put any Python expression inside `{}`:
```python
print(f"Double the score: {score * 2}")     # expression
print(f"Uppercase: {name.upper()}")          # method call
print(f"Range: {low} to {high}")             # multiple variables
```

**Old way vs f-string:**
```python
# old — messy with many variables
print("Player " + name + " scored " + str(score) + " points")

# f-string — clean
print(f"Player {name} scored {score} points")
```

---

### 14. `None` — A Variable That Exists But Has No Value

`None` is Python's way of saying "this variable exists, but it has no meaningful value yet." Useful as a placeholder before you assign a real value.

```python
guessnum = None   # exists, but empty

# later...
guessnum = int(input("Guess:\n"))   # now it has a real value
```

Commonly used as a default when you need a variable to exist before a loop runs but don't have a value for it yet.

---

## Final Project Code

```python
import random

randomnum = random.randint(1, 100)
attempts = 0
guessnum = 0

high = 100
low = 1

while guessnum != randomnum:
    try:
        guessnum = int(input(f"Guess a number between {low} and {high}:\n"))
    except ValueError:
        print("Please enter only numbers, not letters or symbols")
        continue

    attempts += 1

    if guessnum < randomnum:
        low = guessnum + 1
        print("Your guess is lower than the actual number, try again")
    elif guessnum > randomnum:
        high = guessnum - 1
        print("Your guess is higher than the actual number, try again")
    else:
        break

print(f"Congrats, you guessed the number {randomnum} in {attempts} attempts")
```

---

## Key Lessons From This Project

1. `input()` always returns a string — always convert with `int()` or `float()` when you need a number
2. Put `continue` after printing an error message inside `except` — otherwise the loop body keeps running with stale/invalid data
3. `attempts += 1` must go **after** the `try/except` block, not inside it — so invalid inputs don't count as attempts
4. `break` and `continue` are tools to control loop flow precisely — don't avoid them, learn when each fits
5. Dynamic range hints (`low` and `high` updating after each guess) improve UX and came from thinking beyond the spec — good habit

---

*Next project: Simple Calculator — functions, if/elif/else, type conversion*
