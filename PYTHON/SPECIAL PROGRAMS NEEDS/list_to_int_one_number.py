numList = [1, 2, 3]

#METHOD-1
# Over-explaining a bit:
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

print(magic(numList))


#METHOD-2
# How I'd probably write it:
def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


# As a one-liner
num = int(''.join(map(str,numList)))


# Functionally:
s = reduce(lambda x,y: x+str(y), numList, '')
num = int(s)


# Using some oft-forgotten built-ins:
s = filter(str.isdigit, repr(numList))
num = int(s)