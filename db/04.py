import sqlite3

conn = sqlite3.connect("todo.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, description TEXT, due_date TEXT, done INTEGER DEFAULT 0)")

def add_task(description, due_date):
    cur.execute("INSERT INTO tasks(description, due_date) VALUES(?,?)", (description, due_date))
    conn.commit()
    print("Task added")

def view_tasks(show_all=False):
    if show_all:
        rows = cur.execute("SELECT * FROM tasks").fetchall()
    else:
        rows = cur.execute("SELECT * FROM tasks WHERE done=0").fetchall()

    if not rows:
        print("No tasks")
    for task_id, description, due_date, done in rows:
        print(task_id, description, due_date, "Done" if done else "Pending")

def mark_task_completed(task_id):
    cur.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
    conn.commit()
    print("Marked completed" if cur.rowcount else "Task not found")

def delete_task(task_id):
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Deleted" if cur.rowcount else "Task not found")

MENU = """
To-Do List Manager
1. Add New Task
2. View Pending Tasks
3. View All Tasks
4. Mark Task as Completed
5. Delete Task
6. Exit"""

while True:
    print(MENU)
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            add_task(input("Description: "), input("Due date: "))
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks(show_all=True)
        elif choice == "4":
            mark_task_completed(int(input("Task id: ")))
        elif choice == "5":
            delete_task(int(input("Task id: ")))
        elif choice == "6":
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter a valid number")
