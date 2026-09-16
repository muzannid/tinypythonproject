# Contact Book: Python Learning Notes

This document highlights the key concepts learned from building the Python Contact Book terminal application.

## 1. Object-Oriented Programming: Making and Using Classes

Classes allow us to create our own custom data types. In this project, instead of passing around a bunch of separate strings for names, phones, and emails, we bundled them together into a `Contact` object.

### Creating the Class and the Constructor
```python
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
```
*   **`class Contact:`**: This defines the blueprint.
*   **`__init__`**: This is the constructor method. It runs automatically whenever you create a new `Contact`. 
*   **`self`**: This is a reference to the specific object being created. `self.name = name` means "take the `name` passed into the function and attach it to this specific object."

### Class Functions (Methods)
```python
    def display(self):
        print(f"Name : {self.name}")
        # ...
```
*   Functions inside a class are called **methods**. They also take `self` as their first parameter so they can access the data inside that specific object.
*   **How to use it:** When you find a contact in your search function, you trigger this method by typing `contact.display()`.

---

## 2. Accessing Class Objects in a List

In this project, the `contacts` list doesn't store simple strings; it stores full `Contact` objects.

```python
contacts = [] # Starts empty
new_contact = Contact("Muzan", 123456, "muzan@email.com")
contacts.append(new_contact) # Adding the object to the list
```

To access the data inside the list, you have to access the *object* first, and then ask for its *attribute* using "dot notation".
*   `contact` (The whole object)
*   `contact.name` (Just the name string inside the object)
*   `contact.phone` (Just the phone number inside the object)

---

## 3. The Two Types of For Loops: Direct vs. Index

A major lesson in this project is knowing *how* to walk through a list depending on what you want to achieve.

### A. Direct Iteration (Walking through items)
**When to use it:** When you just need to *look* at the data (reading, searching, printing).
```python
# Example from view_all_contact & search_contact
for contact in contacts:
    if contact.name.lower() == search_name.lower():
        # Do something
```
*   **Why it's good:** It's clean, easy to read, and less prone to errors. `contact` automatically becomes the next object in the list every time the loop repeats.

### B. Index Iteration (Using `i` and `range`)
**When to use it:** When you need to *modify* the list itself, specifically when you need to **delete** or **replace** an item.
```python
# Example from delete_contact
for i in range(len(contacts)):
    if contacts[i].name.lower() == name.lower():
        contacts.pop(i) # We need the index 'i' to tell pop() exactly what position to delete!
        break
```
*   **Why we used it here:** The `pop()` list method requires a number (an index) to know which item to remove. If we just used `for contact in contacts:`, we wouldn't know the exact position (0, 1, 2, etc.) of the contact we wanted to delete. By using `range(len(contacts))`, `i` becomes `0`, then `1`, then `2`, representing the exact slot in the list.

---

## 4. Other Important Concepts Used

*   **Error Handling (`try...except`)**: 
    You used this perfectly to prevent the program from crashing when a user types letters instead of numbers for their phone number or menu choice. It catches the `ValueError` and politely asks them to try again.
*   **String Formatting (`:<25`)**: 
    In your `view_all_contact` function, using `f"{contact.name:<25}"` ensures that the text takes up exactly 25 spaces, aligned to the left. This is what makes your terminal output look like a clean, organized table!
*   **Boolean Flags (`found = False`)**: 
    Used in searching and deleting. It acts as a switch. If the loop goes through the whole list and the switch never gets flipped to `True`, the program knows it's safe to say "Contact not found."