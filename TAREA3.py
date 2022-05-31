#WEEK3 - HOMEWORK
fname = input("INGRESE EL ARCHIVO A LEER ")
fh = open(fname)

for line in fh:
    line = line.rstrip()
    print (line.upper())
