### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_stuff = ['Lemons', 'apples', 'computer', 'pack of gum', 'watch']

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_stuff.append('banana')

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_stuff.remove('apples')

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
my_stuff[3]

# Now slice the list.
# Code here
# Example: my_authors[1:4]
my_stuff[2:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
tuple_of_junk = ('Lemons', 'apples', 'computer', 'pack of gum', 'watch')

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
set_of_junk = {'Lemons', 'apples', 'computer', 'pack of gum', 'watch'}


# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
set_of_junk.add('mug')

# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
set_of_junk.add('mug')
print(set_of_junk)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

for thing in my_stuff:
    print(thing)

for item in tuple_of_junk:
    print(item)

for thing in set_of_junk:
    print(thing)

