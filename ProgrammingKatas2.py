#Exercise: combine two lists/arrays

import itertools
list1 = [11,22,33]
list2 = [1,2,3]

new_list=[]
for list1,list2 in itertools.zip_longest(list1,list2):
    if list1:
        new_list.append(list1)
    if list2:
        new_list.append(list2)
print(new_list)

