import re

# Define regular expressions for phone numbers and email addresses
phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{2,}')

# Open the file for reading
with open('example.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Search for phone numbers in the line
        phone_matches = phone_regex.findall(line)
        
        # Print any phone number matches found
        for match in phone_matches:
            print("Phone Number:", match)
        
        # Search for email addresses in the line
        email_matches = email_regex.findall(line)
        
        # Print any email address matches found
        for match in email_matches:
            print("Email Address:", match)
