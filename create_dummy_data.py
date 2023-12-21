import csv
import random

# Generate header row
header = [f"col_{i}" for i in range(1, 11)]

# Generate data for the CSV file
data = [[random.randint(1, 10000) for _ in range(10)] for _ in range(1000)]

# Write data to CSV file
with open('dummy_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    writer.writerow(header)
    
    # Write data rows
    writer.writerows(data)

print("CSV file 'dummy_data' has been created with random integer values.")