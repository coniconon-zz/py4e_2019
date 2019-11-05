# Use words.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
text = fhandle.read()

text = text.rstrip()
text = text.upper()
print(text)
