import re

def is_valid_phone_number(num_str):
    # Check if the input string matches the format "xxx-xxx-xxxx" without using regular expressions.
    if len(num_str) != 12:
        return False
    for i in range(len(num_str)):
        if i in (3, 7):
            if num_str[i] != "-":
                return False
        else:
            if not num_str[i].isdigit():
                return False
    return True

def is_valid_phone_number_regex(num_str):
    # Use a regular expression to validate the phone number format.
    phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(phone_number_pattern.match(num_str))

ph_num = input("Enter a phone number: ")

print("Without using Regular Expression:")
if is_valid_phone_number(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression:")
if is_valid_phone_number_regex(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
