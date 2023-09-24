import os.path
import sys

# Input from the user for the filename
fname = input("Enter the filename: ")

# Check if the file exists
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)
# Open the file for reading
infile = open(fname, "r")

# Read all lines from the file into a list
with open('123.txt', 'r', encoding='iso-8859-1') as infile:
    lineList = infile.readlines()

# Print the first 20 lines of the file (or fewer if the file has fewer lines)
for i in range(5):
    print(i + 1, ":", lineList[i])

# Input from the user for a word to search
word = input("Enter a word: ")

# Count how many times the word appears in the file
cnt = 0
for line in lineList:
    cnt += line.count(word)

# Print the count of the word
print("The word", word, "appears", cnt, "times in the file")
