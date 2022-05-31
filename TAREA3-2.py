#WEEK3-2 - HOMEWORK
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

array = []
var1 = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line2 = line.lstrip('X-DSPAM-Confidence:')   
    array.append(float(line2))
    
for adicionar in array:
    var1 = adicionar + var1

average = var1 / len(array)

print("Average spam confidence:", average)
