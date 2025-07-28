#!/usr/bin/env python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
Flask application for displaying product data from JSON, CSV, and SQLite database.
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_from_json():
    """
    Read product data from JSON file.
    """
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_products_from_csv():
    """
    Read product data from CSV file.
    """
    products = []
    try:
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, csv.Error):
        pass
    return products


def read_products_from_sql():
    """
    Read product data from SQLite database.
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        # Return empty list on database error
        pass
    except Exception as e:
        print(f"Unexpected error: {e}")
        pass
    
    return products


@app.route('/products')
def products():
    """
    Display product data based on source and optional ID.
    Supports json, csv, and sql data sources.
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error='Wrong source', 
                             products=[], 
                             source=source)

    # Get data based on source
    if source == 'json':
        products = read_products_from_json()
    elif source == 'csv':
        products = read_products_from_csv()
    elif source == 'sql':
        products = read_products_from_sql()

    # Filter by ID if provided
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        
        # If no products found with the specified ID
        if not products:
            return render_template('product_display.html', 
                                 error='Product not found', 
                                 products=[], 
                                 source=source, 
                                 product_id=product_id)

    return render_template('product_display.html', 
                         products=products, 
                         source=source, 
                         product_id=product_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
