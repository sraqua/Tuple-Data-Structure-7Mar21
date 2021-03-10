'''
creating a tuple
'''


# tuple = ()
# tuple = ("Sphynx", 200, 3.5, [1,2,3,4])
# print(tuple)

# '''
# python recognises a comma separated list as tuple even WITHOUT round brackets (below).So a tuple is still a tuple even with one item in it as long as it has a TRAILING COMMA at the end
# '''
# tuple = "Microwave", 200, 3.5, [1,2,3,4]
# print(tuple)

# tuple = ('orange', 'apple', 'pear', 'grapes', 'banana')

# print(tuple)

# '''
# # slicing tuples, you can either start with an index postion to print a range of items either before/after that point.  You also count every nth term
# # '''
# # tuple = ('orange', 'apple', 'pear', 'grapes', 'banana')
# # print(tuple[3:5])
# # print(tuple[::2])

# fruit = ('orange', 'apple', 'pear', 'grapes', 'banana','orange', 'orange', 'orange')

# # ''' counts the number of times orange appears in the list'''
# print(fruit.count('orange'))

''' 
confirms the index position of apple in the list
'''

fruit = ('orange', 'apple', 'pear', 'grapes', 'banana','orange', 'orange', 'orange')

print(fruit.index('apple'))

