import sqlite3, csv

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

def show(sql):
    print(cur.execute(sql).fetchall())

cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)")

cur.execute("INSERT INTO products VALUES(1, 'Pen', 10, 100)")
cur.executemany("INSERT INTO products VALUES(?,?,?,?)", [(2, 'Book', 50, 20), (3, 'Bag', 500, 5)])
conn.commit()

show("SELECT * FROM products")
print(cur.execute("SELECT * FROM products WHERE name='Book'").fetchone())
show("SELECT * FROM products WHERE quantity < 10")

cur.execute("UPDATE products SET quantity=50 WHERE name='Book'")
cur.execute("DELETE FROM products WHERE name='Bag'")
conn.commit()
show("SELECT * FROM products")

cur.execute("INSERT INTO products VALUES(4, 'Temp', 1, 1)")
conn.rollback()

with open("backup.sql", "w") as f:
    f.write("\n".join(conn.iterdump()))

with open("products.csv", "w", newline="") as f:
    csv.writer(f).writerows(cur.execute("SELECT * FROM products"))
