fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst_two = list()

for line in fh:
    for word in line.split():
        if not word in lst:
            lst.append(word)

lst.sort()
    
print(lst)
