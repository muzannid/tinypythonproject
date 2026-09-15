# Python Learning Notes
## Project 5 — Word Counter

---

## What This Project Does

A terminal program that takes a piece of text from the user, counts how many times each word appears, and displays the results sorted from most frequent to least frequent. Shows total unique words and total word count at the end.

## Mental Model — How to Think About This Project Before Coding

Before writing a single line, ask yourself three questions:

**1. What is the input?**
A string of text from the user — `"the quick brown fox the fox"`

**2. What is the output?**
A display showing each word and how many times it appeared, sorted highest first.

**3. What data structure connects input to output?**
A **dictionary** — where each word is a key and its count is the value:
```python
{"the": 2, "quick": 1, "brown": 1, "fox": 2}
```

Once you answer these three questions, the code writes itself:
- Get input → `.lower()` → `.split()` → loop → build dict → sort → print

**Always sketch the dummy structure first before coding:**
```python
# wordcounts = {
#     "the": 3,
#     "fox": 2,
#     "quick": 1
# }
```

Knowing what your data looks like at the end tells you exactly what operations you need to get there. This habit applies to every project — draw the target data structure before writing any logic.

---

## Concepts Covered

### 1. `.split()` — Turning a Sentence Into a List of Words

`.split()` is a string method that breaks a string into a list, splitting at every whitespace (space, tab, newline) by default:

```python
"the quick brown fox".split()
# ["the", "quick", "brown", "fox"]

"hello world".split()
# ["hello", "world"]

"one".split()
# ["one"]   — single word still becomes a list
```

**How it works internally:**
Python scans the string left to right, collecting characters until it hits a space — then it takes everything collected so far as one word, adds it to the list, and starts collecting again. Repeats until end of string.

**With a custom separator:**
```python
"a,b,c".split(",")    # ["a", "b", "c"] — split on comma
"a-b-c".split("-")    # ["a", "b", "c"] — split on dash
```

Default (no argument) splits on any whitespace and also ignores multiple spaces:
```python
"hello   world".split()    # ["hello", "world"] — handles multiple spaces
"  hello  ".split()        # ["hello"] — trims edges too
```

**In this project:**
```python
wordlow = word.lower()          # "The Fox THE" → "the fox the"
wordlist = wordlow.split()      # "the fox the" → ["the", "fox", "the"]
```

Now you have a list of individual words you can loop through one by one.

---

### 2. `.lower()` — Case-Insensitive Comparison

Converts every character in a string to lowercase:

```python
"The Quick Brown FOX".lower()
# "the quick brown fox"
```

**Why it matters for word counting:**
Without `.lower()`, "The" and "the" and "THE" would be counted as three separate words — because dict keys are case-sensitive:

```python
# WITHOUT .lower() — wrong
{"The": 1, "the": 2, "THE": 1}   # same word counted as 3 different keys

# WITH .lower() — correct
{"the": 4}   # all treated as the same word
```

**Apply it to the whole text first, then split:**
```python
wordlow = word.lower()     # lowercase the entire sentence first
wordlist = wordlow.split() # then split — every word is already lowercase
```

Order matters — lowercase first, then split. If you split first, you'd have to lowercase each word individually inside the loop.

---

### 3. Dictionary as a Counter — The Core Pattern

This is the most important concept in this project. A dictionary works perfectly as a counter because:
- Keys are unique — each word appears only once as a key
- Values are mutable — you can increment them

**The counting logic — two cases every time you see a word:**

```python
for word in wordlist:
    if word in wordcounts:      # case 1: word already exists in dict
        wordcounts[word] += 1   # increment its count by 1
    else:                       # case 2: word is new, never seen before
        wordcounts[word] = 1    # create it with count = 1
```

**Walking through `"the fox the"` step by step:**

```
Start: wordcounts = {}

Iteration 1 — word = "the"
    "the" in {} ? → NO
    → wordcounts["the"] = 1
    wordcounts = {"the": 1}

Iteration 2 — word = "fox"
    "fox" in {"the": 1} ? → NO
    → wordcounts["fox"] = 1
    wordcounts = {"the": 1, "fox": 1}

Iteration 3 — word = "the"
    "the" in {"the": 1, "fox": 1} ? → YES
    → wordcounts["the"] += 1  (1 + 1 = 2)
    wordcounts = {"the": 2, "fox": 1}

Final result: {"the": 2, "fox": 1}
```

**Key insight:** `wordcounts[word]` uses the word itself as the key — not a separate key called `"count"`. The word IS the key. The number IS the value.

---

### 4. Dictionary Methods — `.items()`, `.values()`, `.keys()`

Three ways to access a dictionary's contents:

**`.keys()` — all keys only:**
```python
wordcounts = {"the": 3, "fox": 2, "quick": 1}
list(wordcounts.keys())
# ["the", "fox", "quick"]
```

**`.values()` — all values only:**
```python
list(wordcounts.values())
# [3, 2, 1]
```

**`.items()` — all key-value pairs as tuples:**
```python
list(wordcounts.items())
# [("the", 3), ("fox", 2), ("quick", 1)]
```

**Used in a for loop with tuple unpacking:**
```python
for word, count in wordcounts.items():
    print(word, count)
# the 3
# fox 2
# quick 1
```

`word, count` unpacks each tuple `("the", 3)` into two separate variables in one line. This is the same pattern as `for name, grades in students.items()` from Project 3.

**Why you can't loop a dict directly for key-value pairs:**
```python
for word in wordcounts:           # gives keys only — "the", "fox", "quick"
for word, count in wordcounts:    # TypeError — can't unpack just a key
for word, count in wordcounts.items():  # correct — unpacks each (key, value) pair
```

---

### 5. `sorted()` with `key=` and `lambda`

**`sorted(iterable)`** — returns a new sorted list from any iterable:
```python
sorted([3, 1, 4, 1, 5])          # [1, 1, 3, 4, 5] — ascending by default
sorted([3, 1, 4], reverse=True)   # [4, 3, 1] — descending
sorted(["banana", "apple", "cherry"])  # ["apple", "banana", "cherry"] — alphabetical
```

**`key=` — sort by a custom rule:**
`key` takes a function that tells `sorted()` what value to use for comparison. Instead of comparing the items directly, it compares the result of calling `key(item)` on each item.

```python
# sort list of tuples by the second element (the count)
items = [("the", 3), ("fox", 2), ("quick", 1)]
sorted(items, key=lambda item: item[1])
# [("quick", 1), ("fox", 2), ("the", 3)]
```

**`lambda` — a tiny one-line function with no name:**

Normal function:
```python
def get_count(item):
    return item[1]
```

Same thing as a lambda:
```python
lambda item: item[1]
```

Syntax: `lambda input: output`
- `lambda` — keyword that starts it
- `item` — the input parameter (like a function parameter)
- `:` — separates input from output
- `item[1]` — what to return (no `return` keyword needed)

Lambda exists for situations where you need a tiny function for one specific use — passing it directly to `sorted()`, `map()`, `filter()` etc. without cluttering your code with a full `def`.

**Full sorted call used in this project:**
```python
sorted(wordcounts.items(), key=lambda item: item[1], reverse=True)
```

Reading it left to right:
- `wordcounts.items()` — the list of `(word, count)` pairs to sort
- `key=lambda item: item[1]` — sort by the count (position 1 of each tuple)
- `reverse=True` — highest count first

**Step by step for `{"the": 3, "fox": 2, "quick": 1}`:**
```
.items() gives: [("the", 3), ("fox", 2), ("quick", 1)]
lambda extracts: [3, 2, 1] — these are the sort values
sorted descending: [("the", 3), ("fox", 2), ("quick", 1)]
loop prints:
    the             3
    fox             2
    quick           1
```

---

### 6. `.values()` with `sum()` — Total Word Count

`.values()` returns all the values in a dict. `sum()` adds them all up:

```python
wordcounts = {"the": 3, "fox": 2, "quick": 1}

sum(wordcounts.values())   # sum([3, 2, 1]) = 6 — total words typed
len(wordcounts)            # 3 — total unique words (number of keys)
```

**The difference:**
- `len(wordcounts)` — counts how many **keys** exist = unique words
- `sum(wordcounts.values())` — adds up all **values** = total words including repeats

For input `"the fox the the"`:
```python
wordcounts = {"the": 3, "fox": 1}
len(wordcounts)              # 2 — two unique words
sum(wordcounts.values())     # 4 — four total words typed
```

---

### 7. `.strip()` — Removing Whitespace from Edges

`.strip()` removes all leading and trailing whitespace (spaces, tabs, newlines) from a string. Does NOT touch whitespace in the middle:

```python
"  hello world  ".strip()    # "hello world"
"  ".strip()                 # "" — empty string
"\nhello\n".strip()          # "hello"
"hello".strip()              # "hello" — no change if nothing to strip
```

**Used as an empty input guard:**
```python
if not word.strip():
    print("Please enter some text.")
    continue
```

If the user just presses Enter or types only spaces, `.strip()` gives `""` which is falsy — `not ""` is `True` — so the guard triggers and asks again.

Without this, `.split()` on an empty string gives `[]`, and the loop produces an empty dict, and the results section prints with nothing in it — confusing output.

---

### 8. Tuple Unpacking — Getting Two Values in One Line

A tuple is an ordered, immutable pair (or group) of values:
```python
pair = ("the", 3)
pair[0]   # "the"
pair[1]   # 3
```

**Tuple unpacking** lets you assign both values to separate variables in one line:
```python
word, count = ("the", 3)
print(word)    # "the"
print(count)   # 3
```

Used in the `for` loop with `.items()`:
```python
for word, count in wordcounts.items():
    # each iteration: word = "the", count = 3
    #                 word = "fox", count = 2
    #                 etc.
```

Python sees that `.items()` returns tuples, and that you have two variable names on the left — so it automatically unpacks each tuple into those two names.

---

## The Full Pipeline — Input to Output

```
User types: "The fox THE quick fox"
                ↓
        word.lower()
                ↓
        "the fox the quick fox"
                ↓
        wordlist = .split()
                ↓
        ["the", "fox", "the", "quick", "fox"]
                ↓
        loop + dict building
                ↓
        {"the": 2, "fox": 2, "quick": 1}
                ↓
        sorted(.items(), key=lambda, reverse=True)
                ↓
        [("the", 2), ("fox", 2), ("quick", 1)]
                ↓
        print with f-string column alignment
                ↓
        Word            Count
        the             2
        fox             2
        quick           1

        Total unique words: 3
        Total word count: 5
```

---

## Key Lessons From This Project

1. **Sketch the target data structure before coding** — knowing `{"the": 3, "fox": 2}` is your goal tells you exactly what operations to use to get there
2. `.split()` converts a sentence string into a list of word strings — it's the entry point for almost all text processing in Python
3. Always `.lower()` the text **before** `.split()` — so every word enters the loop already normalized
4. The dict-as-counter pattern (`if word in dict → increment, else → set to 1`) is one of the most reused patterns in Python — memorize it
5. `wordcounts[word]` uses the word as the key — the word IS the key, not a separate field called `"count"`
6. `.items()` gives `(key, value)` tuples for looping — always use it when you need both key and value
7. `lambda item: item[1]` is a tiny anonymous function — used with `sorted()` to sort by a specific part of a complex item
8. `len(dict)` = unique keys; `sum(dict.values())` = total of all values — two different counts, both useful
9. `.strip()` before checking empty input — spaces alone should not count as valid text
