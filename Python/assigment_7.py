def invert_dictionary(input_dict):
    inverted_dict = {}
    for student, courses in input_dict.items():
        for course in courses:
            inverted_dict[course] = inverted_dict.get(course, []) + [student]
    return inverted_dict

# Sample input dictionary
input_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Print original dictionary
print("Original Dictionary:")
print(input_dict)

# Invert the dictionary
inverted_output = invert_dictionary(input_dict)

# Print inverted dictionary
print("Inverted Output:")
print(inverted_output)

