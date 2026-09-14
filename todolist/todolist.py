import json

tasks = [] #showing at start, the list is still empty

def save_tasks():
    with open("task.json", "w") as file:
        json.dump(tasks,file)

def load_tasks():
    global tasks
    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def add_task(new_task):
    if not tasks:
        id = 1
    else:
        id_last = tasks[-1]["id"] # task[-1] show {"id": id, "task": new_task, "done": False} but  the last list
        id = id_last + 1
    tasks.append({"id": id, "task": new_task, "done": False})

def check_list():
    if not tasks:
        print("No tasks in the list yet.\n")
        return False
    return True

def view_tasks():
    if not check_list():
        return 
    else:
        print("\n=== All Tasks ===")
        print(f"{'ID':<5} {'Status':<15} {'Task'}")
        print("-" * 40)
        for task in tasks:
            id = task["id"]
            done = task["done"]
            task = task["task"]
            print(f"{id:<5} {'✓ Completed' if done else '✗ Pending':<15} {task}") # refer back on this one on the last

def mark_as_completed(target_id):
    if not check_list():
        return

    found = False
    for task in tasks:
        if task["id"] == target_id:
            found = True
            task["done"] = True
            break # stop the loop
    if not found:
        print("Invalid Id. That task doesn't exist.")

def delete_task(target_id):
    if not check_list():
        return
    found = False
    for i in range(len(tasks)):
        if tasks[i]["id"] == target_id:
            found = True
            delete_task = tasks.pop(i)
            break
         
while True:
    print("\n=== To-DO List Application ===\n")
    print("1. Add task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit\n" )

    try:
        choice = int(input("Choose Option (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        add_task(input("Enter the new task: "))
        save_tasks()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        try:
            mark_as_completed(int(input("Enter the index of the task you want to mark as completed: ")))
            save_tasks()
        except ValueError:
            print("Please enter only number that shown on the all task only.")
    elif choice == 4:
        try:
            delete_task(int(input("Enter the index of the task that you want to delete: ")))
            save_tasks()
        except ValueError:
            print("Please enter only number that shown on the all task only.")
    elif choice == 5:
        print("Exiting the application. GoodBye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

    load_tasks()
