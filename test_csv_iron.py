import clr
import csv
import time
from System.Diagnostics import Stopwatch

def sort_csv_file(input_file, output_file, sort_column):
    stopwatch = Stopwatch()
    stopwatch.Start()

    with open(input_file, 'r') as csv_input:
        reader = csv.DictReader(csv_input)
        data = list(reader)

    sorted_data = sorted(data, key=lambda x: x[sort_column])

    stopwatch.Stop()

    with open(output_file, 'w', newline='') as csv_output:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

    elapsed_time = stopwatch.Elapsed.TotalSeconds
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    input_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\assignmentcsv.csv"  # Replace with the path to your input CSV file
    output_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\assignmentcsvsorted.csv"  # Replace with the desired output path
    sort_column = "Value"  

    sort_csv_file(input_file, output_file, sort_column)
