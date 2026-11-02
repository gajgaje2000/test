import sqlite3, csv

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()

def show(sql):
    print(cur.execute(sql).fetchall())

cur.execute("CREATE TABLE students(student_id INTEGER PRIMARY KEY, name TEXT, major TEXT)")
cur.execute("CREATE TABLE courses(course_id INTEGER PRIMARY KEY, title TEXT)")
cur.execute("""CREATE TABLE enrollments(
                   enroll_id INTEGER PRIMARY KEY,
                   student_id INTEGER REFERENCES students(student_id),
                   course_id INTEGER REFERENCES courses(course_id),
                   grade TEXT)""")

show("SELECT * FROM students")
show("SELECT * FROM students WHERE major='CS'")
show("""SELECT s.name, c.title, e.grade FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id""")

cur.execute("UPDATE students SET major='AI' WHERE student_id=2")
cur.execute("UPDATE enrollments SET grade='A+' WHERE enroll_id=1")

cur.execute("DELETE FROM enrollments WHERE enroll_id=2")
try:
    cur.execute("DELETE FROM students WHERE student_id=1")
except sqlite3.IntegrityError as e:
    print("Error:", e)
cur.execute("DELETE FROM enrollments WHERE student_id=1")
cur.execute("DELETE FROM students WHERE student_id=1")
conn.commit()

with open("enrollments.csv", "w", newline="") as f:
    csv.writer(f).writerows(cur.execute("SELECT * FROM enrollments"))

with open("new_students.csv") as f:
    cur.executemany("INSERT INTO students VALUES(?,?,?)", csv.reader(f))
conn.commit()
show("SELECT * FROM students")
