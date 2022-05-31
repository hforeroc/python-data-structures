#WEEK4 - HOMEWORK
fname = input("Enter file name: ")
fh = open(fname)

#lst = set()

#for line in fh:
#    for palabra in line.split():
#        lst.add(palabra)
#print(sorted(lst))

lst = list()

for line in fh:
    for palabra in line.split():
        if palabra in lst:
            continue
        lst.append(palabra)
print(sorted(lst))

