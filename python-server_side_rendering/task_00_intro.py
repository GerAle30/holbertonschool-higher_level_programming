#!/usr/bin/env python3
"""
Module for generating personalized invitation files from a template.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None: Creates output files or logs error messages
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Create a copy of the template for processing
            processed_template = template
            
            # Replace each placeholder with corresponding value or "N/A"
            placeholders = ['name', 'event_title', 'event_date', 'event_location']
            
            for placeholder in placeholders:
                placeholder_key = '{' + placeholder + '}'
                value = attendee.get(placeholder)
                
                # Replace None or missing values with "N/A"
                if value is None:
                    value = "N/A"
                
                processed_template = processed_template.replace(placeholder_key, str(value))
            
            # Generate output filename
            output_filename = f"output_{index}.txt"
            
            # Write the processed template to the output file
            with open(output_filename, 'w') as output_file:
                output_file.write(processed_template)
            
            print(f"Generated {output_filename}")
            
        except Exception as e:
            print(f"Error processing attendee {index}: {e}")
            continue
