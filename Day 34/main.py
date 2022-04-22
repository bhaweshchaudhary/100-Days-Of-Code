
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
*Set items are unchangeable, but you can remove and/or add items whenever you like.


Dictionary is a collection which is ordered** and changeable. No duplicate members.


thislist = ["mango", "pineapple"]
thistuple = ("orange", "apple", "banana")

thislist.extend(thistuple)
print(thislist)


LIST METHODS

append() adds an element at the end of the list
clear() removes all the element from the list
copy() returns the copy of the list
count() returns the number of elements with a specified value
extend() adds the element of the list (or any iterable), to the end of the current list
index() returns the index of the first element with the specified value
insert() adds the element at the specified position
pop() removes the element at the specified position
remove() removes the item with the specified value
reverse() reverse the order of the list
sort() sorts the list



UNPACKING TUPLE

fruits = ("mango", "orange", "pineapple")
(firstFruit, secondFruit, thirdFruit) = fruits
print(firstFruit, secondFruit, thirdFruit)
# Output -> mango orange pineapple


TUPLE METHOD

count() returns the number of times a specified value occurs in a tuple
index() searches the tuple for a specified value and returns the position of where it was found


SET METHODS

add() adds an element to the set
clear() removes all the elemet from the set
copy() returns the copy of the set
difference() returns a set containing the difference between two or more sets
 # example start
euta = {"orange", "apple", "mango"}
duita = {"suntala", "mango", "apple"}
tesro = euta.difference(duita)
print(tesro) // output -> orange
# example ends

difference_update() removes the items in this set that are not present in other, specified set(s)
discard() removes the specified item
intersection() returns a set that is the intersection of two other set
intersection_update() returns the item in this set that are not present in other specified set(s)
isdisjoint() return whether two sets have a intersection or not
issubset() return whether another set contain this set or not
issuperset() return whethter this set contain another set or not
pop() removes an element from the from the set
remove() removes the specified element
symmetric_difference() returns a set with a symmetric difference of two set
symmetric_difference_update() insert the symmetric differences from this set and another
union() return a set containing the union of sets
update() update the set with the union of this set and other


DICTIONARY METHODS

clear() removes all the elements from the dictionary
copy() returns a copy of the dictionary
fromkeys() returns a dictionary with a specified keys and values
get() returns the value of the specified key
items() returns a list containing a tuple for each key value pair
keys() returns a list containing the dictionary key's 
pop() removes the element with the specified key
popitem() removes the last inserted key-value pair
setdefault() returns the value of the specified key, if the key doesn't exit, then insert the key with the specified value
update() updates the dictionary with the specified key value pair
values() returns a list of all the values in the dictionary 




'''
