# Python I/O Mastery 🐍📁

> “Readable code is not enough; it must also be understandable and maintainable.” — Holberton School Motto

Welcome to **Python I/O Mastery**, a mini‐project designed to showcase best practices in reading, writing, and managing files in Python. By the end of this project, you’ll be able to open, read, write, serialize, and deserialize data like a true Python professional—no magic tricks, just clean, idiomatic code.

---

## 📚 Table of Contents

1. [Project Overview](#project-overview)  
2. [Learning Objectives](#learning-objectives)  
3. [Why Python I/O Matters](#why-python-io-matters)  
4. [Getting Started](#getting-started)  
   - [Requirements](#requirements)  
   - [Installation](#installation)  
5. [Project Structure](#project-structure)  
6. [Usage & Examples](#usage--examples)  
   - [Reading a Text File](#reading-a-text-file)  
   - [Writing to a File](#writing-to-a-file)  
   - [JSON Serialization & Deserialization](#json-serialization--deserialization)  
   - [Command-Line Interface](#command-line-interface)  
7. [Testing](#testing)  
8. [Coding Style & Conventions](#coding-style--conventions)  
9. [Advanced Tips & Tricks](#advanced-tips--tricks)  
10. [License & Acknowledgments](#license--acknowledgments)

---

## 🚀 Project Overview

The core script in this repository, `usuarios.py`, demonstrates how to:

1. **Read** a CSV-like text file (`.txt`) line by line, parsing names and ages.  
2. **Validate** and filter input (e.g., handling malformed lines, missing files, permissions).  
3. **Serialize** the resulting Python data structures (list of dictionaries) into a clean, indented JSON file (`.json`).  
4. **Deserializing** back to Python objects (if needed), and gracefully handling errors.  
5. **Expose** a simple CLI so anyone can supply input/output file paths at runtime.

Along the way, we practice best practices in file I/O, context managers (`with`), exception handling, documentation, Pythonic style, and project organization.

---

## 🎯 Learning Objectives

By completing this project, you will be able to:

- Open and close files safely using **context managers** (`with` statement).  
- Read entire files vs. **line‐by‐line** processing to handle large datasets.  
- Move the file cursor (`tell()`, `seek()`) when necessary (bonus).  
- Write text data to a file, including handling encodings (UTF-8).  
- Understand **binary vs. text** modes (`rb`, `wb` vs. `r`, `w`).  
- Use the **`json`** module to **serialize** (dump) and **deserialize** (load) Python objects.  
- Access **command-line arguments** via `sys.argv` (or optionally with `argparse`).  
- Handle common **exceptions** (`FileNotFoundError`, `PermissionError`, `ValueError`) and implement a “clean-up” strategy.  
- Write **docstrings** for modules, classes, and functions to satisfy Holberton’s testing requirements.  
- Ensure compliance with **pycodestyle** (version 2.7.\*) and maintain a neat Git project structure.  
- Create simple **doctest** files to verify functionality automatically.

---

## 💡 Why Python I/O Matters

> “Data is the new oil, but only if you know how to refine it.”  
> — Imaginary Python Guru

In almost every real-world application, you’ll need to persist data: configuration files, user logs, reports, JSON payloads, or even binary blobs like images. Mastering Python’s I/O makes your scripts robust, maintainable, and production-ready. This mini-project encapsulates common scenarios:

- Data ingestion (reading & parsing).  
- Data transformation (cleaning & validating).  
- Data persistence (writing & serializing).  
- Data interchange (JSON ↔ Python).  
- CLI integration (make your script flexible).  

By the end, you’ll feel confident tackling any file-based problem in Python—whether you’re automating a daily report, building a web service, or prototyping a data pipeline.

---

## 🛠 Getting Started

### Requirements

- **Operating System**: Ubuntu 20.04 LTS (or any Unix-like system).  
- **Python Version**: Python 3.8.5 (or newer).  
- **Editors**: `vi`, `vim`, or `emacs` (as per Holberton guidelines).  
- **Dependencies**: Only Python’s standard library (`json`, `sys`, `os`).  
- **Style Checker**: `pycodestyle` 2.7.\*.  

### Installation

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/python-io-mastery.git
   cd python-io-mastery

