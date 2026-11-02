import sqlite3, os

conn = sqlite3.connect("library.db")
cur = conn.cursor()

MENU = """
1 Full backup
2 Backup structure only (one table)
3 Backup data only (one or more tables)
4 Backup one table (structure + data)
5 Restore database from backup
6 Export database to another file
7 Display all tables
8 Display schema
9 Count records
0 Exit"""

def get_structure(table):
    cur.execute("SELECT sql FROM sqlite_master WHERE name=?", (table,))
    row = cur.fetchone()
    return row[0] if row else None

def get_inserts(table):
    lines = []
    for line in conn.iterdump():
        if line.startswith('INSERT INTO "' + table + '"'):
            lines.append(line)
    return lines

def table_names():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [row[0] for row in cur.fetchall()]

def full_backup():
    with open("backup.sql", "w") as f:
        f.write("\n".join(conn.iterdump()))
    print("Saved backup.sql")

def backup_structure():
    table = input("Table name: ")
    sql = get_structure(table)
    if sql is None:
        print("Table not found")
        return
    with open(table + "_structure.sql", "w") as f:
        f.write(sql + ";\n")
    print("Saved", table + "_structure.sql")

def backup_data():
    names = input("Table names (comma separated): ").split(",")
    with open("data.sql", "w") as f:
        for name in names:
            for line in get_inserts(name.strip()):
                f.write(line + "\n")
    print("Saved data.sql")

def backup_table():
    table = input("Table name: ")
    sql = get_structure(table)
    if sql is None:
        print("Table not found")
        return
    with open(table + ".sql", "w") as f:
        f.write(sql + ";\n")
        for line in get_inserts(table):
            f.write(line + "\n")
    print("Saved", table + ".sql")

def restore():
    if os.path.exists("restored.db"):
        os.remove("restored.db")
    new_conn = sqlite3.connect("restored.db")
    with open("backup.sql") as f:
        new_conn.executescript(f.read())
    new_conn.close()
    print("Restored into restored.db")

def export_db():
    new_conn = sqlite3.connect("copy.db")
    conn.backup(new_conn)
    new_conn.close()
    print("Exported to copy.db")

def show_schema():
    for table in table_names():
        print(get_structure(table))

def count_records():
    for table in table_names():
        cur.execute("SELECT COUNT(*) FROM " + table)
        print(table, cur.fetchone()[0])

while True:
    print(MENU)
    choice = input("Enter choice: ")

    if choice == "1":
        full_backup()
    elif choice == "2":
        backup_structure()
    elif choice == "3":
        backup_data()
    elif choice == "4":
        backup_table()
    elif choice == "5":
        restore()
    elif choice == "6":
        export_db()
    elif choice == "7":
        print("\n".join(table_names()))
    elif choice == "8":
        show_schema()
    elif choice == "9":
        count_records()
    elif choice == "0":
        break
