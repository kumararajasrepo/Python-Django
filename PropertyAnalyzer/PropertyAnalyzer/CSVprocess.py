import csv

# Define the data to be written to the CSV file
data = [
    ['Property Type', 'Location', 'Price','Bedrooms Count','Bathrooms Count','Square Footage'],
    ['Apartments', 'Chennai, Perumbakkam', '4100000','2','2','840'],
    ['Apartments', 'Chennai, Nanganallur', '6400000','2','3','900'],
    ['Apartments', 'Chennai, Medavakkam', '5400000','3','2','870'],
    ['Row houses', 'Chennai, Perumbakkam', '8100000','2','2','840'],
    ['Row houses', 'Chennai, Nanganallur', '14000000','2','3','900'],
    ['Row houses', 'Chennai, Medavakkam', '9500000','3','2','870'],
    ['Villas', 'Chennai, Perumbakkam', '11000000','2','2','840'],
    ['Villas', 'Chennai, Nanganallur', '17500000','2','3','900'],
    ['Villas', 'Chennai, Medavakkam', '15000000','3','2','870']
]

# Open a new CSV file for writing
with open('ProperyInfo.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    for row in data:
        writer.writerow(row)

print('CSV file created successfully!')