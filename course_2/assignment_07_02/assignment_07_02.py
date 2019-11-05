# Use the file name mbox-short.txt as the file name
count = 0
line_count = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        stripped = line.strip("X-DSPAM-Confidence:")
        count = count + float(stripped)
        line_count = line_count + 1
        fh.close
print("Average spam confidence:", count/line_count)
