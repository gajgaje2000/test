# 🐍 Database & GUI Practicals (Python, SQLite, Tkinter, MongoDB)

> Complete Syllabus, Journal Assignments & High-Yield Viva Bank.

---

## 📂 1. Repository Layout

```text
test/
├── db/
│   ├── 01.py          # Practical 01: SQLite CRUD, Commit/Rollback, iterdump & CSV Export
│   ├── 02.py          # Practical 02: Full Database Maintenance & Backup Utility (Journal 1)
│   ├── 03.py          # Practical 03: College Multi-Table with Foreign Keys, JOINs & CSV (Journal 2)
│   ├── 04.py          # Practical 04: Interactive To-Do List CLI Manager (Journal 4)
│   ├── 05.py          # Practical 05: Tkinter User Registration Form (Journal 5)
│   ├── 06.py          # Practical 06: Tkinter Complete SQLite CRUD Desktop Form (Journal 8)
│   ├── 07.py          # Practical 07: Tkinter Layouts, All Standard Widgets & Calculator (Journal 7)
│   ├── 08.py          # Practical 08: Student Information Gathering Form with Canvas (Journal 7 Q6)
│   ├── 09.py          # Practical 09: MongoDB CRUD, Aggregation Pipelines & JSON (Journal 6)
│   ├── 10.py          # Practical 10: Tkinter Window Geometry, Min/Max Size & Resize Events
│   ├── 11.py          # Practical 11: Tkinter Widget Attributes, Reliefs, Colors & States
│   ├── 12.py          # Practical 12: Additional Tkinter Widgets (Menu, Message, Menubutton, Spinbox, PanedWindow)
│   └── 13.py          # Practical 13: Full Desktop GUI + MongoDB Integration (Bank Management CRUD)
│
├── .gitignore         # Ignores *.db, *.sql, *.csv, *.json, __pycache__
└── README.md          # Master Guide & Viva Bank
```

---

## 🎯 2. Program Index & Execution Guide

| File | Syllabus / Journal Covered | What it Does & How to Run |
| :--- | :--- | :--- |
| **`db/01.py`** | Unit 3 & Journal 3 | Creates `products` table, executes single and bulk `INSERT`, `SELECT` (all, specific, low stock), `UPDATE`, `DELETE`, demonstrates `rollback()` for unsaved changes, dumps DB using `iterdump()`, and exports to CSV.<br>`python db/01.py` |
| **`db/02.py`** | Unit 3 & Journal 1 (Q1–Q14) | Complete 10-option maintenance menu: full backup (`iterdump()`), structure only, data only (INSERTs), restore from backup, display all tables, display schema (`sqlite_master`), count total records, dump `Book` table in `library.db`, export `Employee` structure, and dump Student/Course/Faculty INSERTs.<br>`python db/02.py` |
| **`db/03.py`** | Unit 3 & Journal 2 | Multi-table schema with Foreign Key enforcement (`PRAGMA foreign_keys = ON`): `students`, `courses`, `enrollments`. Demonstrates `INNER JOIN` queries, update operations, safe cascading delete vs. FK constraint error, CSV export, and CSV import.<br>`python db/03.py` |
| **`db/04.py`** | Unit 3 & Journal 4 | Interactive CLI application with functions: `add_task()`, `view_tasks()`, `mark_task_completed()`, `delete_task()`, and continuous menu loop with error handling.<br>`python db/04.py` |
| **`db/05.py`** | Unit 4 & Journal 5 | Tkinter registration form featuring Name, Email, Password (masked `*`), Country (`ttk.Combobox`), Languages (`Radiobutton`), and submit validation with popup alerts.<br>`python db/05.py` |
| **`db/06.py`** | Unit 4 & Journal 8 / 5 | Full desktop CRUD form connected to SQLite (`student.db`). Features entry inputs, `Add`, `Update`, `Delete` actions, `Listbox` view, and row selection click-to-edit binding. (Can be adapted for Member, Patient, or Employee by changing table/field names).<br>`python db/06.py` |
| **`db/07.py`** | Unit 4 & Journal 7 | Geometry managers: `pack()`, `grid()` (Login form), `place()` (coordinates), `Frame` splitting; standard widgets: `Label`, `Entry`, `Button`, `Checkbutton`, `Radiobutton`, `Listbox`, `Text`, `Scale`, `Toplevel` popup; plus an interactive calculator.<br>`python db/07.py` |
| **`db/08.py`** | Unit 4 & Journal 7 (Q6) | Comprehensive GUI form to gather student details: Name, Email, Phone, Address (`Text`), Class (`Radiobutton`), Semester (`Listbox`), Hobbies (`Checkbutton`), Student badge graphic (`Canvas`), and Submit.<br>`python db/08.py` |
| **`db/09.py`** | Units 1-2 & Journal 6 | MongoDB operations via Python (`pymongo`): collection drop, `insert_one()`, `insert_many()`, `find()`, `find_one()`, `sort()`, `skip()`, `limit()`, aggregation pipelines (`$group`, `$unwind`, `$avg`, `$elemMatch`), updates (`$set`, `$push`, `$`, `$pull`, `upsert=True`, `replace_one()`), deletes, JSON export/import, and collection rename.<br>`python db/09.py` |
| **`db/10.py`** | Unit 4 (4.2.2 & 4.2.3) | Demonstrates window dimensions (`geometry`), min/max constraints (`minsize`, `maxsize`), `grid_columnconfigure` / `grid_rowconfigure` weights for dynamic expansion, `sticky="nsew"`, centered `place(relx=0.5, rely=0.5)`, and `<Configure>` resize event binding.<br>`python db/10.py` |
| **`db/11.py`** | Unit 4 (4.3 & 4.4) | Widget styling & attributes: `bg`, `fg`, `font`, relief styles (`FLAT`, `RAISED`, `SUNKEN`, `GROOVE`, `RIDGE`), `bd`, `padx`/`pady`, `justify`, `activebackground`, `cursor`, button states (`NORMAL`/`DISABLED`), `config()` to change attributes dynamically, and `cget()` to read attributes.<br>`python db/11.py` |
| **`db/12.py`** | Unit 4 (4.3 & 4.4) | Advanced Tkinter widgets: top `Menu` bar (File/Help cascade, separator), auto-wrapping `Message`, `Menubutton` with dropdown options, `LabelFrame` container, `Spinbox`, `Scrollbar` bound to `Listbox`, and `PanedWindow` resizable horizontal panes.<br>`python db/12.py` |
| **`db/13.py`** | Units 2, 4 & Full Stack | Desktop GUI application connected to MongoDB (`bank.accounts`): Full CRUD (Create, Search, Update, Delete), financial calculations (Deposit, Withdraw using `$inc`), sorted accounts listbox, and row selection click-to-edit binding.<br>`python db/13.py` |

---

## 📚 3. Syllabus Mapping

| Unit | Syllabus Topics | Program(s) in `db/` |
| :--- | :--- | :--- |
| **Unit 1: Introduction to NoSQL** | NoSQL history, features, taxonomies (Key-Value, Document, Column-Family, Graph), CAP Theorem, ACID vs. BASE, comparison with RDBMS, MongoDB, Cassandra, HBase, Neo4j. | **Viva Bank below** |
| **Unit 2: Working & Querying with MongoDB** | MongoDB setup, shell usage, collections, CRUD operations, sort, limit, skip, aggregation, updates, upsert, save/replace, rename collection. | `db/09.py`<br>`db/13.py` |
| **Unit 3: Python Interaction with SQLite** | `sqlite3` module, `connect()`, `execute()`, `fetchone()` / `fetchall()`, CRUD operations, `commit()`, `rollback()`, SQLite dumps (`iterdump()`), database & table dumps. | `db/01.py`<br>`db/02.py`<br>`db/03.py`<br>`db/04.py` |
| **Unit 4: CSV Handling & Tkinter GUI** | CSV import/export (`csv` module), Tkinter geometry managers (`pack`, `grid`, `place`), window dimensions & resize handling, Tkinter widgets & attributes. | `db/01.py` (CSV)<br>`db/03.py` (CSV)<br>`db/05.py`<br>`db/06.py`<br>`db/07.py`<br>`db/08.py`<br>`db/10.py`<br>`db/11.py`<br>`db/12.py`<br>`db/13.py` |

---

## 🎓 4. High-Yield Viva & Exam Q&A Bank

### Q1: What is NoSQL and what are its 4 main data models?
**A:** NoSQL ("Not Only SQL") provides flexible, schema-less data storage with horizontal scaling for unstructured/semi-structured data:
1. **Document Stores** (MongoDB, CouchDB): Data stored in JSON/BSON documents with nested sub-documents and arrays.
2. **Key-Value Stores** (Redis, DynamoDB): Key associated with an arbitrary value; ultra-fast $O(1)$ lookups.
3. **Column-Family / Wide-Column** (Cassandra, HBase): Data grouped by column families, optimized for massive analytical writes/reads.
4. **Graph Databases** (Neo4j): Stores nodes, relationships (edges), and properties; optimized for social graphs, recommendations, and route optimization.

### Q2: What is the CAP Theorem?
**A:** Formulated by Eric Brewer, a distributed system can guarantee at most **two out of three** properties simultaneously:
- **Consistency (C):** Every read receives the most recent write or an error.
- **Availability (A):** Every non-failing request receives a non-error response.
- **Partition Tolerance (P):** The system continues operating despite dropped or delayed network messages.
*(Since physical network partitions are unavoidable, distributed systems choose between CP or AP).*

### Q3: Contrast ACID vs. BASE.
- **ACID (RDBMS):** **A**tomicity, **C**onsistency, **I**solation, **D**urability. Strict, immediate consistency for financial/relational transactions.
- **BASE (NoSQL):** **B**asically **A**vailable, **S**oft-state, **E**ventual consistency. Favors high availability and performance over instant consistency.

### Q4: How does `iterdump()` work in Python's `sqlite3`?
**A:** `connection.iterdump()` returns an iterator that yields SQL text statements (`CREATE TABLE`, `INSERT INTO`) necessary to reconstruct the current database. It is Python's programmatic equivalent of SQLite's `.dump` command.

### Q5: What is the difference between `commit()` and `rollback()`?
- `connection.commit()` permanently writes all pending transaction changes to the disk file.
- `connection.rollback()` reverts all changes back to the state of the last commit, canceling any uncommitted modifications.

### Q6: How are Foreign Keys enabled in SQLite?
**A:** By default, SQLite parses Foreign Key definitions but does not enforce them. To enforce them, run per connection:
```python
conn.execute("PRAGMA foreign_keys = ON")
```

### Q7: Explain the three Tkinter geometry managers.
- **`pack()`:** Stacks widgets in blocks horizontally or vertically (`side=LEFT/RIGHT/TOP/BOTTOM`, `fill=X/Y/BOTH`, `expand=True`).
- **`grid()`:** Places widgets in a 2D grid table (`row=0, column=1, padx=5, pady=5, sticky="nsew"`). Best for forms.
- **`place()`:** Positions widgets by explicit pixel coordinates (`x=20, y=50`) or relative coordinates (`relx=0.5, rely=0.5`).

### Q8: What are the main relief styles in Tkinter?
**A:** `FLAT`, `RAISED`, `SUNKEN`, `GROOVE`, and `RIDGE` (set via `relief=RAISED`, `bd=3`).

### Q9: Name the key stages in MongoDB Aggregation Pipelines.
- `$match`: Filters documents (SQL `WHERE`).
- `$group`: Groups documents by an `_id` and computes aggregates like `$sum`, `$avg` (SQL `GROUP BY`).
- `$unwind`: Deconstructs an array field from input documents to output a document for each element.
- `$sort`: Orders output documents (SQL `ORDER BY`).
