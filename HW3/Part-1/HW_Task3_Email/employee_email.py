# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        firstName = row['first_name']
        lastName = row['last_name']
        ssn = row['ssn']
        email = f'{firstName}.{lastName}@example.com'
        employee = {'First Name':firstName, 'Last Name':lastName, 'ssn':ssn, 'email':email}
        new_employee_data.append(employee)

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join('Resources/output.csv')
with open(csvpath, "w") as csvfile:
    fieldnames = ['First Name', 'Last Name', 'ssn', 'email']
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writerows(new_employee_data)
    
