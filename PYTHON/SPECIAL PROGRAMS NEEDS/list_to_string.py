# Python program to convert a list to string


#METHOD-1
# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

s = ['Geeks', 'for', 'Geeks']
print(listToString(s))

#METHOD -2
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])

print(listToStr)


#METHOD -3
# Python program to convert a list
# to string using list comprehension

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])

print(listToStr)


#METHOD-4
# Python program to convert a list
# to string using list comprehension

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join(map(str, s))

print(listToStr)
