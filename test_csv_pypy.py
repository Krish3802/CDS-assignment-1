import csv
import time

def sort_csv_file(input_file, output_file, sort_column):
    # Measure the start time
    start_time = time.time()

    # Read the CSV file and extract the data into a list of dictionaries
    with open(input_file, 'r') as csv_input:
        reader = csv.DictReader(csv_input)
        data = list(reader)

    # Sort the data based on the specified column
    sorted_data = sorted(data, key=lambda x: x[sort_column])

    # Measure the end time
    end_time = time.time()

    # Write the sorted data back to the output CSV file
    with open(output_file, 'w', newline='') as csv_output:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    input_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\assignmentcsv.csv"  # Replace with the path to your input CSV file
    output_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\assignmentcsvsortedby_pypy.csv"  # Replace with the desired output path
    sort_column = "Value"  # Replace with the column name you want to sort by

    sort_csv_file(input_file, output_file, sort_column)
