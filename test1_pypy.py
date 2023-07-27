import time

def uppercase_text_file(input_file, output_file):
    start_time = time.time()

    with open(input_file, 'r') as file_in:
        content = file_in.read()
        uppercase_content = content.upper()

    end_time = time.time()

    with open(output_file, 'w') as file_out:
        file_out.write(uppercase_content)

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    input_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\input.txt"  
    output_file = "C:\\Users\\krish\\OneDrive\\Desktop\\bda\\fybda\\cds\\output.txt"  

    uppercase_text_file(input_file, output_file)
