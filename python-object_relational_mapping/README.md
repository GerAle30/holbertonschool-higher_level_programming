# 🤖 Python - Object Relational Mapping (ORM)

Welcome to the **Python Object Relational Mapping (ORM)** project! In this project, we explore how Python can interact with MySQL databases using both raw SQL queries and Object Relational Mappers like **SQLAlchemy**.

---

## 🎓 Learning Objectives

By the end of this project, you will be able to:

* 📁 Connect a Python script to a MySQL database
* 🔢 Execute SELECT and INSERT queries using MySQLdb
* 🧰 Understand and apply Object Relational Mapping (ORM) concepts
* 🔹 Map Python classes to MySQL tables using SQLAlchemy
* 🌍 Build database-independent Python code with ORM abstractions

---

## 🔗 Key Concepts

### 🔄 From SQL to ORM

**Without ORM** (Raw SQL):

```python
import MySQLdb
conn = MySQLdb.connect(user="root", passwd="root", db="my_db")
cur = conn.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
```

**With ORM** (SQLAlchemy):

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State

engine = create_engine("mysql+mysqldb://root:root@localhost/my_db")
session = Session(engine)
for state in session.query(State).order_by(State.id):
    print(f"{state.id}: {state.name}")
session.close()
```

---

## 🧰 ORM Essentials

* ORM = Object Relational Mapper
* Maps classes to tables, attributes to columns
* Makes code more readable and independent of the underlying database
* With ORM, focus on what you want to do, not how the database stores it

---

## 📚 Technologies Used

| Tool       | Version |
| ---------- | ------- |
| Python     | 3.8.5   |
| MySQL      | 8.0.25  |
| MySQLdb    | 2.0.x   |
| SQLAlchemy | 1.4.x   |

---

## 🛋️ Project Structure

```bash
python-object_relational_mapping/
├── 0-select_states.py
├── 1-filter_states.py
├── 2-my_filter_states.py
├── 3-my_safe_filter_states.py
├── 4-cities_by_state.py
├── 5-filter_cities.py
├── model_state.py
├── 6-model_state.py
├── 7-model_state_fetch_all.py
├── 8-model_state_fetch_first.py
├── 9-model_state_filter_a.py
├── 10-model_state_my_get.py
├── 11-model_state_insert.py
├── 12-model_state_update_id_2.py
├── 13-model_state_delete_a.py
├── model_city.py
└── 14-model_city_fetch_by_state.py
```

---

## 🤝 Best Practices

* Always close cursors and sessions
* Sanitize user input to prevent SQL injection (especially when using MySQLdb)
* Use SQLAlchemy's query filter methods instead of raw SQL
* Use `Base.metadata.create_all(engine)` only after importing all models

---

## 🧰 Common ORM Patterns

### Define Models

```python
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
```

### Create Tables

```python
Base.metadata.create_all(engine)
```

### Query Data

```python
session.query(State).filter(State.name.like('%a%')).all()
```

### Insert Data

```python
new = State(name="Louisiana")
session.add(new)
session.commit()
```

### Update Data

```python
state = session.query(State).filter_by(id=2).first()
state.name = "New Mexico"
session.commit()
```

### Delete Data

```python
states = session.query(State).filter(State.name.like('%a%')).all()
for s in states:
    session.delete(s)
session.commit()
```

---

## 🫠 Tips for Success

* Read error messages carefully — SQLAlchemy is powerful but strict
* Check SQLAlchemy docs or cheat sheets when unsure
* Build small, test often — commit changes frequently
* Understand your models well; relationships and foreign keys matter!

---

## 🚀 Getting Started

1. ✅ Install MySQL and required Python packages:

```bash
sudo apt update
sudo apt install mysql-server python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient SQLAlchemy
```

2. ✅ Test imports:

```python
import MySQLdb
import sqlalchemy
```

3. ✅ Initialize database using `.sql` setup files

4. ✅ Run and test your scripts with:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

---

## 👨‍💻 Author

**Alejandro Garcia Sanchez**
Holberton School - San Juan Campus

