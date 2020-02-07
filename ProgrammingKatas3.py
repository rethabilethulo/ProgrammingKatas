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

#Exercise: Frame some text


def frame(words) :
    len_words =len(words)
    len_longest = len(words[0])
    for i in range(len_words) :
        if len(words[i]) >= len_longest :
          len_longest = len(words[i])

    len_longest = len_words
    len_frame_row = len_longest + 4
    print('*' * len_frame_row)
    for word in words :
        row = '* ' + word
        while len(row) < len_frame_row - 1 :
            row = row + " "
        row = row + '*'
        print(row)
    print('*' * len_frame_row)
frame(["Write","good","code","every","day"])
