# creating the file with the names in it
names = list()
file = open('Sort Me.txt')

#looping through the array of words to append
for name in file:
    names.append(name)
file.close()

#first sort the results by character
#then by the length
names.sort()
names.sort(key=len)

#print
for name in names:
    print(name)


# print("_____________ Reverse It")
# print("")
#
# #code for reversing
#
# names.sort(reverse=True)
# names.sort(key=len, reverse=True)
#
# for name in names:
#     print(name)
