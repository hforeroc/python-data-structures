#WEEK 1 - HOMEWORK
text = "X-DSPAM-Confidence:    0.8475"
var1 = text.find(':')
var2 = text[var1+1:]
var3 = var2.strip()
print(float(var3))
