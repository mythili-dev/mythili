#!/usr/bin/env python
# coding: utf-8

# In[1]:


# List operations
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10
print("List after modifying an element:", my_list)

print()

# Dictionary operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['c'] = 30
print("Dictionary after modifying a value:", my_dict)

print()

# Set operations
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

# Note: Sets do not support indexing, so modifying an element is not straightforward
# You typically remove the element and add a new one if modification is needed
my_set.discard(3)
my_set.add(10)
print("Set after modifying an element (by removing and adding):", my_set)


# In[ ]:




