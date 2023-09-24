# Input two strings from the user
str1 = input("Enter String 1:\n")
str2 = input("Enter String 2:\n")

# Calculate the lengths of both strings
len_str1 = len(str1)
len_str2 = len(str2)

# Determine the shorter and longer strings
short_len = min(len_str1, len_str2)
long_len = max(len_str1, len_str2)

# Initialize a variable to count matching characters
match_count = 0

# Compare characters in the two strings
for i in range(short_len):
    if str1[i] == str2[i]:
        match_count += 1

# Calculate and print the similarity between the two strings
similarity = match_count / long_len
print("Similarity between the two strings:")
print(similarity)
