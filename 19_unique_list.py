def unique_list(lst):
    
    unique_elements = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]
result = unique_list(my_list)
print("The unique list is:", result)


    




