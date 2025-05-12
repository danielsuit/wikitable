import csv


input_file = 'Train.csv'

output_file = 'o.csv'

# Open the input CSV file for reading
with open(input_file, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as output:
        # Create a CSV writer object
        writer = csv.writer(output)

        # Iterate over each row in the input CSV file
        for row in reader:
            for i in range(len(row)):
                if row[i].find("[") != -1:
                    print(row[i])
                    for j in range(len(row[i])):
                        if row[i][j] == "[":
                            row[i] = row[i][:j]
                            break
                                    
            # Process the row as needed

            # Write the processed row to the output CSV file
            writer.writerow(row)

# Done! The input CSV file has been read and the processed data has been written to the output CSV file.