


files = open("files.txt", "r")

outfile = "this is a new line" + "\n"
files.readline()

for line in range (5):
    outfile += files.readline()

files.close()


files = open("files.txt", "w")
files.write(outfile)
files.close()