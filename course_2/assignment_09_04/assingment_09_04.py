filename = input("Enter file: ")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)

# Create a dictionary
email = dict()

# Loop to read each line in the text and split them
for line in handle:
    if line.startswith('From '):       
        line = line.split()
        address = line[1]
        email[address] = email.get(address, 0) + 1

most = None
for key in email:
    if most is None or email[key] > most:
        most = email[key]
        sender = key
print(sender, most)
