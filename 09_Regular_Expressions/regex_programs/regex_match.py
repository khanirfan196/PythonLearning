import re


my_str1 = "1234abcd"
my_str2 = "abcd1234"

pattern = r"\d+" # /d are for numbers

# match() - only match at the start of the string
my_match = re.match(pattern, my_str1)

# re.match() also returns an object
print(type(my_match))

print("First match")
print(my_match)

print(my_match.group())

my_match2 = re.match(pattern, my_str2)

# returns None
print("Second match")
print(my_match2)


################################################################


str1 = "abC_123_helloworld" # only abC_123 is checked

str2 = "123_abc"

pattern = r"[A-Za-z]{3}_[\d]{3}"

valid_str = re.match(pattern, str1)

print("Check valid string1")
print(valid_str)

valid_str = re.match(pattern, str2)

print("Check valid string2")
print(valid_str)

