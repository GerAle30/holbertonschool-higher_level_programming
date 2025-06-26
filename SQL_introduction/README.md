# SQL - Introduction

Welcome to the **SQL - Introduction** project! This project is part of the Holberton School curriculum and is designed to provide a solid foundation in SQL and relational database systems using MySQL.

---

## 📚 Resources

* What is Database & SQL?
* Install MySQL (MySQL Server)
* A Basic MySQL Tutorial
* Basic SQL statements: DDL and DML
* Basic queries: SQL and RA
* SQL techniques: functions and subqueries
* What makes the big difference between a backtick and an apostrophe?
* MySQL Cheat Sheet
* MySQL 8.0 SQL Statement Syntax

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

* Understand what a **database** and a **relational database** are
* Know what **SQL** stands for and what **MySQL** is
* Create and manipulate databases and tables in MySQL
* Understand and use **DDL** (Data Definition Language) and **DML** (Data Manipulation Language)
* Perform basic operations: `CREATE`, `ALTER`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`
* Use **subqueries** and **functions** in SQL

---

## ✅ Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Ubuntu 20.04 LTS with MySQL 8.0.25
* Each SQL file must end with a new line and start with a comment describing the task
* SQL keywords must be written in uppercase (e.g. `SELECT`, `WHERE`)
* A `README.md` file is mandatory
* Scripts must be tested using `cat file.sql | mysql -uroot -p`
* You are not allowed to use `SELECT` or `SHOW` in some tasks as specified

---

## 🧪 Project Structure and Tasks

```bash
holbertonschool-higher_level_programming/
└── SQL_introduction/
    ├── 0-list_databases.sql              # List all databases
    ├── 1-create_database_if_missing.sql # Create database hbtn_0c_0
    ├── 2-remove_database.sql            # Delete database hbtn_0c_0
    ├── 3-list_tables.sql                # List all tables in a database
    ├── 4-first_table.sql                # Create first_table
    ├── 5-full_table.sql                 # Print table description (without DESCRIBE)
    ├── 6-list_values.sql                # List all rows in first_table
    ├── 7-insert_value.sql               # Insert a new row into first_table
    ├── 8-count_89.sql                   # Count records where id = 89
    ├── 9-full_creation.sql              # Create second_table and insert rows
    ├── 10-top_score.sql                 # List records ordered by score
    ├── 11-best_score.sql                # List scores >= 10 ordered
    ├── 12-no_cheating.sql               # Update score for Bob to 10
    ├── 13-change_class.sql              # Remove records with score <= 5
    ├── 14-average.sql                   # Calculate average score
    ├── 15-groups.sql                    # Group records by score
    └── 16-no_link.sql                   # List only records with non-empty names
```

---

## ⚙️ How to Use

To execute any SQL script:

```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p <database_name>
```

For example:

```bash
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

## 📌 Tips for Success

* Always test your SQL commands in the sandbox before final submission.
* Use comments generously to describe your SQL queries.
* Stick to the task instructions: avoid using forbidden commands.
* Format your SQL files for readability and compliance with project requirements.

---

## 🧠 Bonus Knowledge

### Backtick vs Apostrophe:

* Use **backticks (\`)** for identifiers (e.g., table or column names)
* Use **apostrophes (')** for string values (e.g., `'Hello'`)

---

Good luck and enjoy learning SQL! 🧠💻
