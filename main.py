
names = list()
file = open('Sort Me.txt')

for name in file:
    names.append(name)
file.close()

names.sort()
names.sort(key=len)

for name in names:
    print(name)

print("_____________ Reverse It")
print("")

#code for reversing

names.sort(reverse=True)
names.sort(key=len, reverse=True)

for name in names:
    print(name)
