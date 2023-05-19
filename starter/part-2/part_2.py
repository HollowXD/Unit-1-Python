### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["J.K. Rowling", "R. L. Stine", "John Steinbeck", "Rick Riordan", "Ernest Cline", "Tatsuki Fujimoto", "Gege Akutami"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
my_authors.append("Suzanne Collins")
print(my_authors)

# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

# Code here
my_authors.remove("Rick Riordan")
print(my_authors)

# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
print(my_authors[5])

# Example: my_authors[2]


# Now slice the list.

# Code here
print(my_authors[0:2])

# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
my_author_tuple = ("J.K. Rowling", "R. L. Stine", "John Steinbeck", "Rick Riordan", "Ernest Cline", "Tatsuki Fujimoto", "Gege Akutami")

# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
my_author_set = {"J.K. Rowling", "R. L. Stine", "John Steinbeck", "Rick Riordan", "Ernest Cline", "Tatsuki Fujimoto", "Gege Akutami"}

# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here
my_author_set.add("Dr. Seuss")

# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

# Code here
my_author_set.add("Dr. Suess")
print(my_author_set)

# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
for book in my_authors:
    print(book)

for book in my_author_tuple:
    print(book)

for book in my_author_set:
    print(book)

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)