"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


with open('foo.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'a') as a_writer:
    a_writer.write('\nif, elsif, else, while, do-while, for. So, are you more front-end or back-end? Actually, I\'m fullstack. This is a bad idea. MATLAB is not programming. There are 3 kinds of people: those who can count and those who can\'t. 1 = 00000001. CSS Grid is the bees knees. \nNobody is proud of this. If at first you don\'t succeed, call it version 1.0. A programmer puts two glasses on his bedside table before going to sleep. A full one, in case he gets thirsty, and an empty one, in case he doesn\'t. Real programmers don\'t document. If it was hard to write, it should be hard to understand. A SQL statement walks into a bar and sees two tables. It approaches, and asks \'may I join you? \nDon\'t treat a semi colon as the end of the line, but rather as a possibility of a new beginning. There are 3 kinds of people: those who can count and those who can\'t. Don\'t treat a semi colon as the end of the line, but rather as a possibility of a new beginning. I\'m moving to the bay area. Unit test your methods. Java, Ruby, C, Javascript, GO, Rust, Cobol, Fortran')