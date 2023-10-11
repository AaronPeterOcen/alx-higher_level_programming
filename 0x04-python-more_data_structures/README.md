0x04. Python - More Data Structures: Set, Dictionary


List comprehension is a concise way to create new lists from existing lists and their values. It is a powerful tool that can be used to perform a variety of tasks, such as filtering, mapping, and reducing lists.

The basic syntax of a list comprehension is as follows:

Python
[new_element for old_element in existing_list if condition]
Use code with caution. Learn more
The new_element expression can be anything that can be evaluated to a Python object. The old_element variable is used to iterate over the elements of the existing_list. The condition expression is used to filter the elements of the list, and only the elements that evaluate to True will be included in the new list.

Here is an example of a simple list comprehension:

Python
>>> my_list = [1, 2, 3, 4, 5]
>>> even_numbers = [number for number in my_list if number % 2 == 0]
>>> even_numbers
[2, 4]
Use code with caution. Learn more
This list comprehension creates a new list called even_numbers that contains all of the even numbers from the list my_list. The number % 2 == 0 condition is used to filter the elements of my_list, and only the elements that are divisible by 2 are included in the new list.

List comprehensions can also be used to perform more complex tasks, such as mapping and reducing lists. For example, the following list comprehension maps all of the elements of the list my_list to their squares:

Python
>>> squared_numbers = [number * number for number in my_list]
>>> squared_numbers
[1, 4, 9, 16, 25]
Use code with caution. Learn more
The following list comprehension reduces the list my_list to a single value, which is the sum of all of the elements in the list:

Python
>>> sum_of_numbers = sum([number for number in my_list])
>>> sum_of_numbers
15
Use code with caution. Learn more
List comprehensions are a powerful tool that can be used to simplify and improve your Python code. If you are not already familiar with list comprehensions, I encourage you to learn more about them. They can be a valuable addition to your programming toolkit.
