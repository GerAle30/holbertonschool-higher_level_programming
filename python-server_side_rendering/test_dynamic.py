#!/usr/bin/env python3
"""
Test script to demonstrate dynamic template functionality.
"""

import json
import shutil
from task_01_jinja import app

def test_dynamic_content():
    """Test dynamic content with different JSON files."""
    print("=== Testing Dynamic Template Functionality ===\n")
    
    with app.test_client() as client:
        # Test 1: Normal items list
        print("1. Testing with normal items list:")
        response = client.get('/items')
        print(f"   Status: {response.status_code}")
        if b'Python Book' in response.data and b'Flask Mug' in response.data:
            print("   ✓ Items displayed correctly")
        if b'No items found' not in response.data:
            print("   ✓ No 'empty' message shown")
        
        # Test 2: Empty items list
        print("\n2. Testing with empty items list:")
        # Backup original file and use empty one
        shutil.copy('items.json', 'items_backup.json')
        shutil.copy('items_empty.json', 'items.json')
        
        response = client.get('/items')
        print(f"   Status: {response.status_code}")
        if b'No items found' in response.data:
            print("   ✓ 'No items found' message displayed")
        if b'<li>' not in response.data:
            print("   ✓ No list items shown for empty data")
        
        # Test 3: Extended items list
        print("\n3. Testing with extended items list:")
        shutil.copy('items_extended.json', 'items.json')
        
        response = client.get('/items')
        print(f"   Status: {response.status_code}")
        if b'Docker Container' in response.data and b'Linux Terminal' in response.data:
            print("   ✓ Extended items displayed correctly")
        if b'Total items:' in response.data:
            print("   ✓ Item count displayed")
        
        # Restore original file
        shutil.copy('items_backup.json', 'items.json')
        
        print("\n=== Dynamic Template Tests Complete ===")

def analyze_template_features():
    """Analyze the template features implemented."""
    print("\n=== Template Features Analysis ===")
    
    with open('templates/items.html', 'r') as f:
        template_content = f.read()
    
    features = {
        'Jinja loops': '{% for item in items %}' in template_content,
        'Jinja conditions': '{% if items %}' in template_content,
        'Template variables': '{{ item }}' in template_content,
        'Jinja filters': '{{ items|length }}' in template_content,
        'Template includes': "{% include 'header.html' %}" in template_content,
        'Else condition': '{% else %}' in template_content
    }
    
    print("Template features implemented:")
    for feature, implemented in features.items():
        status = "✓" if implemented else "✗"
        print(f"   {status} {feature}")

if __name__ == '__main__':
    test_dynamic_content()
    analyze_template_features()
    print(f"\nTo run the Flask app: python3 task_01_jinja.py")
    print("Then visit http://localhost:5000/items to see dynamic content")
