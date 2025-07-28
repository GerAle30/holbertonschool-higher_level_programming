#!/usr/bin/env python3
"""
Flask application for displaying product data from JSON or CSV files.
"""

import json
import csv
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

@app.route('/products')
def products():
    """
    Display product data based on source and optional ID.
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source', products=[], source=source)

    if source == 'json':
        products = read_products_from_json()
    else:
        products = read_products_from_csv()

    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]

    if not products and product_id is not None:
        return render_template('product_display.html', error='Product not found', products=[], source=source, product_id=product_id)

    return render_template('product_display.html', products=products, source=source, product_id=product_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
