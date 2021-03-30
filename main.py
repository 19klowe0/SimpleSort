# creating the file with the names in it

names = list()
file = open('SortMe.txt')

#looping through the array of words to append
for name in file:
    #remove whitespace
    name = name.strip()
    words = name.split()
    for word in words:
        names.append(name)
file.close()

#first sort the results by character
#then by the length
names.sort()
names.sort(key=len)

#print
for name in names:
    print(name)


