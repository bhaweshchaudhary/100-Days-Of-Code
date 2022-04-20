
'''
fruits = ['orange', 'pineapple', 'mango']
x, y, z = fruits
print(x)
print(y)
print(z)

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview


a = 1j # this is complex number

[Modify Strings]

.upper() to convert to upper case
.lower() to convert to lower case
.strip() to remove whitespace
.replace() to replace string
.split() to split string

[String Methods]

capitalize() converts the first character to upper case
casefold() converts string into lower case
center() returns a centered string
count() returns the number of times a specified value occurs in a string
encode() returns an encoded version of the string
endswith() returns true if the string ends with the specified value
expandtabs() sets the tab size of the string
find() searches the string for a specified value and return the position of it
format() formats specified value in a string
format_map() formats specified value in a string
index() searches the string for a specified value and returns the position of where it was found
isalnum() returns true if all character in the string are alphanumeric
isalpha() returns true if all characters in the string are in the alphabet
isdecimal() returns true if all characters in string are in decimal
isdigit() returns true if all characters in the string are digit
isidentifier() returns true if the string is an identifier
islower() returns true if all character in the string are lower case
isnumeric() returns true if all character in the string are numeric
isprintable() returns true if all characters in the string are printable
isspace() returns true if all characters in the string are whitespace
istitle() returns true if the string follows the rule of a title
isupper() returns true if all the characters in the string are upper case
join() join the elements of an iterable to the end of the string
ljust() returns the left justified version of the string
lower() converts the string into lower case
lstrip() returns a left trim version of the string
maketrans() returns a translation table to be used in translation
partition() returns a tuple where the string is parted into three parts
replace() returns a string where a specified value is replaced with a specified value
rfind() searches the string for a specified value and returns the last position of where it was found
rindex() searches the string for a specified value and returns the last position of where it was found
rjust() returns a right justified version of the string
rpartition() returns a tuple where the string is parted into three parts
rsplit() splits the string at the specified seperator and returns a list
rstrip() returns a right trim version of the string
split() splits the string at the specified separator and returns a list
splitlines() splits the string at line breaks and returns a list
startswith() returns true if the string start with the specified value 
strip() returns a trimmed version of the string
swapcase() swap cases, lower case becomes upper case and vice versa
title() converts the first character of each word to upper case
translate() returns a translated string
upper() converts a string into upper case
zfill() fills the string with a specified number of 0 values at the beginning 



Python List

print(list(("hello", "namaste"))) # this is list constructor

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''


