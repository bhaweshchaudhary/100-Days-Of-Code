## List Comprehension 3

💪 This exercise is HARD

# Instructions

Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, 
each number on a new line.

You are going to create a list called result which contains the numbers that are 
common in both files. 

e.g. if file1.txt contained:

```
1
```

```
2
```

```
3
```

and file2.txt contained:

```
2
```

```
3
```

```
4
```

```
result = [2, 3]
```

**IMPORTANT**: The result should be a list that contains **Integers**, 
not **Strings**. Try to use **List Comprehension** instead of a **Loop**.

# Example Output

```
[3, 6, 5, 33, 12, 7, 42, 13]
```

# Hint

1. Use the keyword method for starting the List comprehension and fill in the relevant parts.

2. First, you will need to read from the files and create a list using the lines in the files.

3. This method will be really useful: [https://www.w3schools.com/python/ref_file_readlines.asp](https://www.w3schools.com/python/ref_file_readlines.asp)

4. Remember you can check if a value exists in a list using the **in** keyword. [https://www.w3schools.com/python/ref_keyword_in.asp](https://www.w3schools.com/python/ref_keyword_in.asp)

5. Remember you can convert a string to an int using the int() method. [https://www.w3schools.com/python/ref_func_int.asp](https://www.w3schools.com/python/ref_func_int.asp)

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-26-3-test-your-code](https://repl.it/@appbrewery/day-26-3-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-26-3-solution](https://repl.it/@appbrewery/day-26-3-solution)