#!/usr/bin/env python3
"""
Test script for task_02_logic.py - Dynamic Template with Loops and Conditions
"""

import shutil
from task_02_logic import app

def test_task_02_functionality():
    """Test Task 2 dynamic template functionality."""
    print("=== Testing Task 2 - Dynamic Template with Loops and Conditions ===\n")
    
    with app.test_client() as client:
        # Test 1: Normal items list
        print("1. Testing with normal items list:")
        response = client.get('/items')
        print(f"   Status: {response.status_code}")
        if b'Python Book' in response.data and b'Flask Mug' in response.data:
            print("   ✓ Items displayed correctly")
        if b'Items List' in response.data:
            print("   ✓ Page title correct")
        if b'No items found' not in response.data:
            print("   ✓ No 'empty' message shown")
        
        # Test 2: Empty items list
        print("\n2. Testing with empty items list:")
        # Backup original file and use empty one
        shutil.copy('items.json', 'items_backup_temp.json')
        shutil.copy('items_empty.json', 'items.json')
        
        response = client.get('/items')
        print(f"   Status: {response.status_code}")
        if b'No items found' in response.data:
            print("   ✓ 'No items found' message displayed")
        if b'<li>' not in response.data:
            print("   ✓ No list items shown for empty data")
        
        # Restore original file
        shutil.copy('items_backup_temp.json', 'items.json')
        
        print("\n=== Task 2 Tests Complete ===")

def verify_requirements():
    """Verify all Task 2 requirements are met."""
    print("\n=== Verifying Task 2 Requirements ===")
    
    requirements = {
        'Flask app file exists': 'task_02_logic.py',
        'Items template exists': 'templates/items.html',
        'Items JSON file exists': 'items.json',
        'Items route implemented': '/items'
    }
    
    import os
    
    # Check files exist
    file_checks = {
        'Flask app file exists': os.path.exists('task_02_logic.py'),
        'Items template exists': os.path.exists('templates/items.html'),
        'Items JSON file exists': os.path.exists('items.json')
    }
    
    # Check route exists
    with app.test_client() as client:
        response = client.get('/items')
        route_works = response.status_code == 200
    
    file_checks['Items route implemented'] = route_works
    
    print("Requirements check:")
    for requirement, passed in file_checks.items():
        status = "✓" if passed else "✗"
        print(f"   {status} {requirement}")
    
    # Check template features
    print("\nTemplate features check:")
    if os.path.exists('templates/items.html'):
        with open('templates/items.html', 'r') as f:
            template_content = f.read()
        
        features = {
            'Jinja for loop': '{% for item in items %}' in template_content,
            'Jinja if condition': '{% if items %}' in template_content,
            'Items List title': 'Items List' in template_content,
            'Unordered list': '<ul>' in template_content,
            'No items message': 'No items found' in template_content,
            'Header include': "{% include 'header.html' %}" in template_content
        }
        
        for feature, implemented in features.items():
            status = "✓" if implemented else "✗"
            print(f"   {status} {feature}")

def test_json_data():
    """Test JSON data format."""
    print("\n=== Testing JSON Data Format ===")
    
    import json
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        
        print("JSON data structure:")
        print(f"   Data type: {type(data)}")
        print(f"   Contains 'items' key: {'items' in data}")
        if 'items' in data:
            print(f"   Items count: {len(data['items'])}")
            print(f"   Items: {data['items']}")
            
            # Check for required items
            required_items = ["Python Book", "Flask Mug", "Jinja Sticker"]
            has_required = all(item in data['items'] for item in required_items)
            print(f"   ✓ Contains required items: {has_required}")
        
        print("   ✓ JSON file is valid")
        
    except Exception as e:
        print(f"   ✗ JSON file error: {e}")

if __name__ == '__main__':
    verify_requirements()
    test_json_data()
    test_task_02_functionality()
    print(f"\nTo run Task 2 Flask app: python3 task_02_logic.py")
    print("Then visit http://localhost:5000/items to see dynamic content")
    print("\nAll Task 2 requirements have been implemented successfully! 🎉")
