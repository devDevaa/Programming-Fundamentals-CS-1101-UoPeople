# Existing list of 10 employees
employee_list = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]

# 1. Splitting the list into two sub-lists
subList1 = employee_list[:5]
subList2 = employee_list[5:]

# 2. Adding new employee "Kriti Brown"
subList2.append("Kriti Brown")

# 3. Removing second employee's name from subList1
del subList1[1]

# 4. Merging both lists
merged_list = subList1 + subList2
print("Merged List:", merged_list) # print the merged list

# 5. Assuming salaryList that stores salaries of employees
salaryList = [50000, 40000, 55000, 85000, 70000, 45000, 60000, 80000, 70000, 70000]
updated_salaryList = [salary * 1.04 for salary in salaryList] # Giving a rise of 4% to every employee

# 6. Sorting the updated salaryList
updated_salaryList.sort(reverse=True)
print("Top 3 Salaries:") # print top 3 salaries
for i in range(3):
    print(updated_salaryList[i])




# Function to convert a sentence into a word list
def sentence_to_wordlist(sentence):
    return sentence.split()

# Function to reverse word list
def reverse_wordlist(word_list):
    return list(reversed(word_list))

sentence = "University of the People"

# Convert the sentence into a word list
word_list = sentence_to_wordlist(sentence)

# Reverse the word list
reversed_word_list = reverse_wordlist(word_list)

print(reversed_word_list) # Print the reversed word list
