# Python Server Side Rendering

This project demonstrates Python server-side rendering techniques using Flask and Jinja templates.

## Tasks

### Task 0: Creating a Simple Templating Program
- **File**: `task_00_intro.py`
- **Description**: Generates personalized invitation files from a template with placeholders
- **Features**: 
  - String templating with placeholder replacement
  - Error handling for various edge cases
  - File I/O operations

### Task 1: Creating a Basic HTML Template in Flask
- **File**: `task_01_jinja.py`
- **Description**: Basic Flask application with Jinja templates
- **Features**:
  - Multiple routes (/, /about, /contact, /items)
  - Reusable header and footer templates
  - Navigation between pages
  - Template inheritance using `{% include %}`

### Task 2: Creating a Dynamic Template with Loops and Conditions
- **File**: `task_02_logic.py`
- **Description**: Flask application with dynamic template logic using loops and conditions
- **Features**:
  - Dynamic content rendering from JSON data
  - Jinja loops (`{% for %}`) for iterating over items
  - Jinja conditions (`{% if %}`) for conditional display
  - JSON file reading and parsing
  - Template filters for data manipulation
  - Unordered list display of items

### Task 3: Displaying Data from JSON or CSV Files
- **File**: `task_03_files.py`
- **Description**: Flask application for displaying product data from multiple file formats
- **Features**:
  - JSON and CSV file reading and parsing
  - Query parameter handling for source selection
  - Product filtering by ID
  - Error handling for invalid sources and missing products
  - Table-based data display with styling

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Template generation program
├── task_01_jinja.py          # Flask application with basic templates
├── task_02_logic.py          # Flask application with dynamic template logic
├── task_03_files.py          # Flask application for JSON/CSV data display
├── template.txt              # Invitation template
├── items.json                # JSON data for dynamic template
├── items_empty.json          # Empty JSON for testing
├── items_extended.json       # Extended JSON for testing
├── products.json             # Product data in JSON format
├── products.csv              # Product data in CSV format
├── templates/                # Flask templates directory
│   ├── header.html           # Reusable header component
│   ├── footer.html           # Reusable footer component
│   ├── index.html            # Home page template
│   ├── about.html            # About page template
│   ├── contact.html          # Contact page template
│   ├── items.html            # Dynamic items page template
│   └── product_display.html  # Product data display template
├── test_flask.py             # Flask application test script
├── test_dynamic.py           # Dynamic content test script
├── test_task_02_logic.py     # Task 2 specific test script
├── test_task_03.py           # Task 3 comprehensive test script
├── main.py                   # Test script for task 0
└── README.md                 # This file
```

## Requirements

- Python 3.x
- Flask

## Installation

```bash
pip install Flask
```

## Usage

### Task 0 - Template Generation
```bash
python3 task_00_intro.py
# or run the test script
python3 main.py
```

### Task 1 - Basic Flask Application with Templates
```bash
# Run the Flask application
python3 task_01_jinja.py

# Then visit in your browser:
# http://localhost:5000         (Home page)
# http://localhost:5000/about   (About page)
# http://localhost:5000/contact (Contact page)
# http://localhost:5000/items   (Dynamic items page)
```

### Task 2 - Dynamic Template with Loops and Conditions
```bash
# Run the Flask application with dynamic logic
python3 task_02_logic.py

# Then visit in your browser:
# http://localhost:5000/items   (Dynamic items page with loops and conditions)
```

### Task 3 - Product Data Display from Files
```bash
# Run the Flask application
python3 task_03_files.py

# Then visit in your browser:
# http://localhost:5000/products?source=json          (All products from JSON)
# http://localhost:5000/products?source=csv           (All products from CSV)
# http://localhost:5000/products?source=json&id=1     (Product ID 1 from JSON)
# http://localhost:5000/products?source=csv&id=2      (Product ID 2 from CSV)
# http://localhost:5000/products?source=xml           (Invalid source test)
# http://localhost:5000/products?source=json&id=999   (Product not found test)
```

### Testing Flask Applications
```bash
# Test basic routes (Task 1)
python3 test_flask.py

# Test dynamic content functionality (Task 2)
python3 test_dynamic.py

# Test Task 2 specific implementation
python3 test_task_02_logic.py

# Test file display functionality (Task 3)
python3 test_task_03.py
```

## Features

### Task 0 Features
- ✅ Template-based invitation generation
- ✅ Placeholder replacement with actual data
- ✅ Error handling for invalid inputs
- ✅ Missing data handling (replaces with "N/A")
- ✅ Sequential file naming (output_1.txt, output_2.txt, etc.)

### Task 1 Features
- ✅ Flask application running on port 5000
- ✅ Multiple routes with template rendering
- ✅ Reusable header and footer components
- ✅ Navigation links between pages
- ✅ Clean HTML structure with proper semantics

### Task 2 Features
- ✅ Dynamic content rendering from JSON files
- ✅ Jinja `{% for %}` loops for item iteration
- ✅ Jinja `{% if %}` conditions for empty state handling
- ✅ Template variables with `{{ item }}` syntax
- ✅ Jinja filters with `{{ items|length }}`
- ✅ JSON file reading and parsing with error handling
- ✅ Conditional display: "No items found" when list is empty
- ✅ Unordered list display of items
- ✅ Item count display

### Task 3 Features
- ✅ JSON and CSV file reading with proper parsing
- ✅ Query parameter handling (`source` and `id`)
- ✅ Dynamic source selection (JSON vs CSV)
- ✅ Product filtering by ID
- ✅ Error handling for invalid sources ("Wrong source")
- ✅ Error handling for missing products ("Product not found")
- ✅ Table-based data display with HTML styling
- ✅ Price formatting with currency symbol
- ✅ Responsive table design with CSS
- ✅ Usage examples and navigation links

## Author

Alejandro Garcia - Holberton School Student
