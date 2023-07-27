import time

def lowercase_text_file(input_file, output_file):
    start_time = time.time()

    with open(input_file, 'r') as file_in:
        content = file_in.read()
        lowercase_content = content.upper()

    end_time = time.time()

    with open(output_file, 'w') as file_out:
        file_out.write(lowercase_content)

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.9f} seconds")

if __name__ == "__main__":
    input_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\input.txt"  # Replace with the path to your input text file
    output_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\output.txt"  # Replace with the desired output path

    lowercase_text_file(input_file, output_file)
