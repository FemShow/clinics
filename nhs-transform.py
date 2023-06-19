# This is a short succinct pandas script that 
# 1. identifies delimiters 
# 2. replaces the delimiters with commas,
# 3. eliminates white spaces present in the csv file
# 4. saves the resultant file in new-nhs.csv

import pandas as pd

# Step 1: Identify delimiters
# The choice of the delimiter used in NHS CSV "¬" file generates an error.
# The 'c' engine in pandas, which is the default engine, does not support separators longer than one character. 
# to address this, the 'python' engine is used to avoid the error, instead.

with open('Clinics.csv', 'r') as file:
    first_line = file.readline().strip()  # Read the first line
    delimiters = [',', ';', '\t', '¬']  # Add additional delimiters if needed

    # Check which delimiter occurs most frequently in the first line
    delimiter_count = {}
    for delimiter in delimiters:
        delimiter_count[delimiter] = first_line.count(delimiter)
    
    most_common_delimiter = max(delimiter_count, key=delimiter_count.get)

# Step 2: Replace delimiters with commas
df = pd.read_csv('Clinics.csv', delimiter=most_common_delimiter, engine='python')
df.to_csv('temp.csv', index=False)  # Save a temporary file with commas as the delimiter

# Step 3: Eliminate white spaces
df = pd.read_csv('temp.csv', delimiter=',', skipinitialspace=True)
df.to_csv('new-Clinics.csv', index=False)  # Save the resultant file with eliminated white spaces

# Cleanup: Delete the temporary file
import os
os.remove('temp.csv')
