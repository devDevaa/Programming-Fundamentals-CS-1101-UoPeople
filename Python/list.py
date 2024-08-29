# Equivalent but not Identical
num1 = [1, 2, 3]
num2 = [1, 2, 3]

print(num1 == num2) # Equivalent: Contents of both lists are the same
print(num1 is num2) # Not Identical: They are different objects in memory

#Identical and Equivalent
list1 = [1, 2, 3]
list2 = list1

print(list2 == list1) # Equivalent: Contents of both lists are the same
print(list2 is list1) # Identical: They refer to the same object in memory



def add_element(list, element):
    list.append(element)

my_list = [1, 2, 3]
add_element(my_list, 4)

print(my_list)  # [1, 2, 3, 4]