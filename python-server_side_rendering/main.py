#!/usr/bin/env python3
"""
Main file to test the invitation generation program.
"""

from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
print("=== Testing with valid data ===")
generate_invitations(template_content, attendees)

print("\n=== Testing with empty template ===")
generate_invitations("", attendees)

print("\n=== Testing with empty attendees list ===")
generate_invitations(template_content, [])

print("\n=== Testing with invalid template type ===")
generate_invitations(123, attendees)

print("\n=== Testing with invalid attendees type ===")
generate_invitations(template_content, "not a list")

print("\n=== Testing with non-dictionary in attendees list ===")
generate_invitations(template_content, [{"name": "Alice"}, "not a dict"])
