#!/usr/bin/env python3
"""
Test script to verify Flask application functionality.
"""

from task_01_jinja import app

def test_routes():
    """Test that all routes can be accessed."""
    with app.test_client() as client:
        # Test home route
        response = client.get('/')
        print(f"Home route status: {response.status_code}")
        if response.status_code == 200:
            print("✓ Home route working")
        
        # Test about route
        response = client.get('/about')
        print(f"About route status: {response.status_code}")
        if response.status_code == 200:
            print("✓ About route working")
        
        # Test contact route
        response = client.get('/contact')
        print(f"Contact route status: {response.status_code}")
        if response.status_code == 200:
            print("✓ Contact route working")
        
        # Test items route
        response = client.get('/items')
        print(f"Items route status: {response.status_code}")
        if response.status_code == 200:
            print("✓ Items route working")
            # Check if the response contains expected content
            if b'Items List' in response.data:
                print("✓ Items template rendering correctly")

if __name__ == '__main__':
    test_routes()
    print("\nFlask application is ready!")
    print("To run the application, execute:")
    print("python3 task_01_jinja.py")
    print("Then visit http://localhost:5000 in your browser")
