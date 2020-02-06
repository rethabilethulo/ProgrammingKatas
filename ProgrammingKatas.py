#Exercise : Hello

name = 'Hello Tshepo'
print(name)


#Exercise: check if a number is even

def odd_and_even():
    num = int(input("Enter a number :"))
    if (num % 2) == 0 :
        print("{0} is Even".format(num))
    else : 
        print("{0} is Odd".format(num))

#Exercise: Draw a square

def square():
    side = int(input("Please Enter any sides of a Square : "))

    print("Square Hash Pattern")

    for i in range(side) :
        for i in range(side) :
            print('#', end = ' ')
        print()


#Exercise: Draw a right angle triangle   
def right_angle_triangle():
    rows = int(input("Please Enter the Total Number of Rows : "))

    print("Right Angled Triangle Hash Pattern")

    for i in range(1, rows + 1) :
        for j in range(1 ,i + 1) :
            print('#', end = '')
        print()



#Exercise: Draw an isosceles triangle

def isosceles():
    length = int(input("Please Enter the number of rows : "))

    for i in range(0,length):
        for j in range(0, length - i -1):
            print(end = " ")
        for j in range(0, i + 1) :
            print("#", end = " ")
        print()
    

#Exercise: find the longest string

def find_longest_word(word_list = []):  
    longest_word = ''
    for word in word_list:
        if len(longest_word) < len(word):
            longest_word = word
    return "The longest word(s) in the list is: {}".format(longest_word)


words = ["the","quick","brown", "fox", "ate", "my", "chickens"]
print(find_longest_word(words))
