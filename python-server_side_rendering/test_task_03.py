#!/usr/bin/env python3
"""
Test script for Task 3 - Displaying Data from JSON or CSV Files.
"""

from task_03_files import app

def test_file_functionality():
    """Test file reading and display functionality."""
    print("=== Testing Task 3 - File Display Functionality ===\n")
    
    with app.test_client() as client:
        test_cases = [
            # Test JSON source
            {
                'url': '/products?source=json',
                'description': 'All products from JSON',
                'expected_status': 200,
                'should_contain': [b'Laptop', b'Coffee Mug', b'Electronics']
            },
            # Test CSV source
            {
                'url': '/products?source=csv',
                'description': 'All products from CSV',
                'expected_status': 200,
                'should_contain': [b'Laptop', b'Coffee Mug', b'Electronics']
            },
            # Test JSON with specific ID
            {
                'url': '/products?source=json&id=1',
                'description': 'Product ID 1 from JSON',
                'expected_status': 200,
                'should_contain': [b'Laptop', b'799.99']
            },
            # Test CSV with specific ID
            {
                'url': '/products?source=csv&id=2',
                'description': 'Product ID 2 from CSV',
                'expected_status': 200,
                'should_contain': [b'Coffee Mug', b'15.99']
            },
            # Test invalid source
            {
                'url': '/products?source=xml',
                'description': 'Invalid source (xml)',
                'expected_status': 200,
                'should_contain': [b'Wrong source']
            },
            # Test invalid ID
            {
                'url': '/products?source=json&id=999',
                'description': 'Invalid product ID',
                'expected_status': 200,
                'should_contain': [b'Product not found']
            },
            # Tes missing source parameter
            {
                'url': '/products',
                'description': 'Missing source parameter',
                'expected_status': 200,
                'should_contain': [b'Wrong source']
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"{i}. Testing: {test_case['description']}")
            print(f"   URL: {test_case['url']}")
            
            response = client.get(test_case['url'])
            print(f"   Status: {response.status_code}")
            
            if response.status_code == test_case['expected_status']:
                print("   ✓ Status code correct")
            else:
                print(f"   ✗ Expected {test_case['expected_status']}, got {response.status_code}")
            
            # Check if expected content is present
            content_found = all(content in response.data for content in test_case['should_contain'])
            if content_found:
                print("   ✓ Expected content found")
            else:
                print("   ✗ Expected content missing")
                for content in test_case['should_contain']:
                    if content not in response.data:
                        print(f"     Missing: {content}")
            
            print()

def test_file_reading_functions():
    """Test individual file reading functions."""
    print("=== Testing File Reading Functions ===\n")
    
    from task_03_files import read_products_from_json, read_products_from_csv
    
    # Test JSON reading
    print("1. Testing JSON file reading:")
    json_products = read_products_from_json()
    print(f"   Products loaded: {len(json_products)}")
    if json_products:
        print(f"   First product: {json_products[0]}")
        print("   ✓ JSON reading successful")
    else:
        print("   ✗ JSON reading failed")
    
    print()
    
    # Test CSV reading
    print("2. Testing CSV file reading:")
    csv_products = read_products_from_csv()
    print(f"   Products loaded: {len(csv_products)}")
    if csv_products:
        print(f"   First product: {csv_products[0]}")
        print("   ✓ CSV reading successful")
    else:
        print("   ✗ CSV reading failed")

def analyze_template_features():
    """Analyze the template features implemented."""
    print("\n=== Template Features Analysis ===")
    
    with open('templates/product_display.html', 'r') as f:
        template_content = f.read()
    
    features = {
        'Table structure': '<table>' in template_content and '<th>' in template_content,
        'Error handling': '{% if error %}' in template_content,
        'Product iteration': '{% for product in products %}' in template_content,
        'Conditional display': '{% if products %}' in template_content,
        'Template filters': 'format(product.price)' in template_content,
        'Styling with CSS': '<style>' in template_content,
        'Template includes': "{% include 'header.html' %}" in template_content
    }
    
    print("Template features implemented:")
    for feature, implemented in features.items():
        status = "✓" if implemented else "✗"
        print(f"   {status} {feature}")

if __name__ == '__main__':
    test_file_reading_functions()
    test_file_functionality()
    analyze_template_features()
    print(f"\nTo run the Flask app: python3 task_03_files.py")
    print("Then visit http://localhost:5000/products?source=json")
    print("\nTest URLs:")
    print("- http://localhost:5000/products?source=json")
    print("- http://localhost:5000/products?source=csv")
    print("- http://localhost:5000/products?source=json&id=1")
    print("- http://localhost:5000/products?source=xml (invalid)")
    print("- http://localhost:5000/products?source=json&id=999 (not found)")
