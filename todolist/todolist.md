# Python Learning Notes
## Project 4 — To-Do List with JSON Persistence

---

## What This Project Does

A terminal app that manages a personal to-do list with **persistent storage** — tasks are saved to a JSON file and reloaded every time the program runs or an action is taken. You can:
- Add new tasks (auto-generated ID)
- View all tasks with status
- Mark tasks as completed by ID
- Delete tasks by ID
- All data survives after the program closes

## New Concepts Introduced in This Version

### 1. `import json` — The JSON Module

JSON (JavaScript Object Notation) is a universal text format for storing and transferring structured data. Python's built-in `json` module converts between Python objects and JSON text.

**Two directions:**

```python
import json

# Python dict/list → JSON text (to save to file or send over network)
json.dumps({"name": "Muzan", "age": 20})
# '{"name": "Muzan", "age": 20}'

# JSON text → Python dict/list (to read back)
json.loads('{"name": "Muzan", "age": 20}')
# {"name": "Muzan", "age": 20}
```

**Memory hook:**
- `dumps` = "dump to string" (Python → text)
- `loads` = "load from string" (text → Python)

For files specifically:
- `json.dump(data, file)` = write Python object to a file as JSON
- `json.load(file)` = read JSON from a file back into Python

No `s` at the end = file version. With `s` = string version.

---

### 2. `with open()` — Reading and Writing Files

`open()` opens a file. The `with` keyword ensures the file is **automatically closed** after the block finishes, even if an error occurs.

```python
# WRITE to a file
with open("task.json", "w") as file:
    json.dump(tasks, file)

# READ from a file
with open("task.json", "r") as file:
    tasks = json.load(file)
```

**The mode argument — second parameter of `open()`:**

| Mode  | Meaning| Behaviour                                                      |
|---    |---     |---                                                             |
| `"r"` | Read   | Opens existing file for reading. Crashes if file doesn't exist |
| `"w"` | Write  | Creates file if not exists. **Overwrites** if it does          |
| `"a"` | Append | Creates file if not exists. Adds to end if it does             |

**`as file`** — gives the opened file a variable name (`file`) so you can call methods on it (`.read()`, `.write()`, or pass it to `json.dump()`/`json.load()`).

**Why `with` and not just `open()`:**
```python
# without with — risky, file might stay open if error occurs
file = open("task.json", "r")
data = json.load(file)
file.close()   # you have to manually close it

# with with — file always closes automatically
with open("task.json", "r") as file:
    data = json.load(file)
# file is closed here automatically, no matter what
```

Always use `with open()` — it's the safe, modern Python way.

---

### 3. `json.dump()` and `json.load()` — Saving and Loading to File

**Saving (writing):**
```python
def save_tasks():
    with open("task.json", "w") as file:
        json.dump(tasks, file)
```

`json.dump(data, file)` takes your Python list/dict and writes it as JSON text into the file. After this, `task.json` on your disk contains something like:
```json
[{"id": 1, "task": "Buy groceries", "done": false}, {"id": 2, "task": "Study Python", "done": true}]
```

**Loading (reading):**
```python
def load_tasks():
    global tasks
    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
```

`json.load(file)` reads the JSON text from the file and converts it back into a Python list of dicts. If the file doesn't exist yet (first time running the program), `FileNotFoundError` is caught and `tasks` is set to an empty list instead of crashing.

---

### 4. `global` — Accessing a Variable from Outside the Function

By default, a variable assigned inside a function is **local** — it only exists inside that function and doesn't affect anything outside:

```python
tasks = []   # this is the GLOBAL tasks

def load_tasks():
    tasks = json.load(file)   # this creates a NEW LOCAL tasks — doesn't affect the global one!
```

To tell Python "I mean the global variable, not a new local one," use `global`:

```python
def load_tasks():
    global tasks             # "use the tasks that exists outside this function"
    tasks = json.load(file)  # now this updates the global tasks
```

**When you need `global`:**
Only when you're **reassigning** (using `=`) a global variable inside a function. You don't need it for just reading or mutating (`.append()`, `.pop()`) — those work on the global automatically.

```python
tasks = []

def add_task(new_task):
    tasks.append(new_task)   # no global needed — mutating, not reassigning

def reset_tasks():
    global tasks
    tasks = []               # global needed — reassigning with =
```

**Use `global` sparingly** — too much global state makes code hard to follow. In bigger projects, you'd pass data as parameters instead.

---

### 5. `FileNotFoundError` — Handling Missing Files

A specific exception Python throws when you try to open a file that doesn't exist on disk:

```python
try:
    with open("task.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []   # first time running — no file yet, start empty
```

This is the correct pattern for any program that reads from a file:
- If the file exists → load it
- If it doesn't exist yet → start fresh with empty data

Without this, the first time someone runs your program (before any tasks are saved), it crashes immediately.

---

### 6. `tasks[-1]` — Negative Indexing

Python lists support **negative indexes** — they count from the end backwards:

```python
tasks = ["a", "b", "c", "d"]

tasks[0]    # "a" — first item
tasks[-1]   # "d" — last item (same as tasks[3])
tasks[-2]   # "c" — second from last
```

Used in `add_task()` to get the last task's ID without knowing the list length:

```python
id_last = tasks[-1]["id"]   # get the id of the last task in the list
id = id_last + 1            # new id = last id + 1
```

**Why this is better than `len(tasks) + 1` for persistent data:**
When you save and reload from a file, tasks might have been deleted — so the list length no longer matches the last ID. Example:
```
Add task 1, 2, 3 → tasks has 3 items
Delete task 2 → tasks has 2 items, but last ID is 3
len(tasks) + 1 = 3 → COLLISION with deleted task 2's old ID
tasks[-1]["id"] + 1 = 4 → correct, always increments from last real ID
```

---

### 7. ID-Based Lookup vs Index-Based Lookup

**Previous version** used list index (position) to find tasks:
```python
tasks[task_index - 1]["done"] = True   # position-based — fragile after deletions
```

**This version** uses the actual stored `id` field — looping through and matching:
```python
for task in tasks:
    if task["id"] == target_id:   # ID-based — works regardless of position
        task["done"] = True
        break
```

**Why ID-based is better:**
After deleting a task, list positions shift. Task that was at index 2 might now be at index 1. But IDs never change — task ID 3 is always ID 3 regardless of what got deleted around it. This makes ID-based lookup more reliable for persistent data.

---

### 8. `found` Flag Pattern — Tracking Whether a Loop Found Something

When searching through a list for a specific item, use a boolean flag to track whether you found it:

```python
def mark_as_completed(target_id):
    found = False                    # assume not found
    for task in tasks:
        if task["id"] == target_id:
            found = True             # found it
            task["done"] = True      # do the action
            break                    # stop searching
    if not found:
        print("Invalid ID. That task doesn't exist.")
```

**Flow:**
```
set found = False
    ↓
loop through every task
    ↓
    if ID matches → set found = True, act, break
    ↓
after loop: if found is still False → nothing matched → tell user
```

This is one of the most common search patterns in Python. You'll use it constantly when working with lists of dicts where you need to find a specific record.

---

### 9. `range(len(list))` — Looping with Index Numbers

Sometimes you need the **position** of an item while looping, not just the item itself. `range(len(tasks))` generates a sequence of index numbers:

```python
tasks = ["a", "b", "c"]
range(len(tasks))   # range(3) → 0, 1, 2

for i in range(len(tasks)):
    print(i, tasks[i])
# 0 a
# 1 b
# 2 c
```

Used in `delete_task()` because `.pop()` needs an index position:

```python
for i in range(len(tasks)):
    if tasks[i]["id"] == target_id:
        tasks.pop(i)    # pop needs the index — i gives us that
        break
```

**When to use which loop style:**

| Situation                      | Use                                |
|---                             |---                                 |
| Just need each item            | `for task in tasks:`               |
| Need the item AND its position | `for i in range(len(tasks)):`      |
| Need both cleanly              | `for i, task in enumerate(tasks):` |

`enumerate()` is the cleanest way to get both — worth knowing for future:
```python
for i, task in enumerate(tasks):
    print(i, task["id"])   # i = position, task = the dict
```

---

### 10. Save After Every Mutation, Load After Every Action

**Pattern used in this project:**
```python
if choice == 1:
    add_task(input("Enter the new task: "))
    save_tasks()    # save immediately after changing data
...
load_tasks()        # reload at end of every loop iteration
```

**Why save immediately after every change:**
If the program crashes or closes unexpectedly between a change and a save, the change is lost. Saving right after every mutation (add, mark, delete) means you never lose more than the current action.

**Why reload after every action:**
In this project, reloading after every action is a way to confirm the file and the in-memory list stay in sync. In a more advanced project, you'd only load once at startup — but for a learning project this pattern makes the persistence obvious and easy to reason about.

---

## Patterns Introduced in This Version

### Persist → Load → Act → Save cycle
```
program starts
    ↓
load_tasks() — bring file data into memory
    ↓
user acts (add/mark/delete)
    ↓
save_tasks() — write updated memory back to file
    ↓
load_tasks() — confirm sync
    ↓
loop back
```

### Safe file read with fallback
```python
try:
    with open("file.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []   # file doesn't exist yet — start fresh
```

### Search by ID with found flag
```python
found = False
for item in list:
    if item["id"] == target_id:
        found = True
        # act on item
        break
if not found:
    print("Not found")
```

---

## Key Lessons From This Extended Version

1. `json.dump(data, file)` saves Python to a file; `json.load(file)` reads it back — no `s` = file, with `s` = string
2. Always use `with open()` — it automatically closes the file even if an error occurs
3. `global` is only needed when **reassigning** a global variable inside a function — not for `.append()` or `.pop()`
4. `FileNotFoundError` is the right exception to catch when reading a file that might not exist yet — always provide a fallback
5. `tasks[-1]` gets the last item — negative indexing counts from the end
6. ID-based lookup is more reliable than index-based for persistent data — positions shift after deletions, IDs don't
7. The `found` flag pattern is the standard way to search a list and report whether something was found
8. `range(len(list))` gives you index numbers for looping — use it when you need the position (e.g. for `.pop()`)
9. Save immediately after every mutation — never let a change sit unsaved

---

*Next project: Word Counter — `.split()`, dict manipulation, loops*
