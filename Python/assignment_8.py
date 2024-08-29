# Define the input and output file paths in a variable
input_file_path = 'input_dictionary.txt'
output_file_path = 'output_inverted_dictionary.txt'

try:
    # Initialize an empty dictionary to store key-value pairs from the input file
    original_dict = {}

    # Read from the input file and populate the original dictionary
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            key, values = line.strip().split(':')
            values_list = [value.strip() for value in values.split(',')]
            for value in values_list:
                original_dict[value] = key.strip()

    # Invert the original dictionary to create the inverted dictionary
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    # Write the inverted dictionary to the output file "output_inverted_dictionary.txt"
    with open(output_file_path, 'w') as output_file:
        for key, values in inverted_dict.items():
            output_file.write(f'{key}: {", ".join(values)}\n')

    print("Inverted dictionary has been written to the output file successfully.")

    # Error messages
except FileNotFoundError:
    print(f"Error: Input file '{input_file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to write to '{output_file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
