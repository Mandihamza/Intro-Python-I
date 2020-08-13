# For the exercise, look up the methods and functions that are available for use
# with Python lists.
import results as results

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("4 added to end of x list:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print("x with y appended to end:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print("x with 8 removed:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("x with 99 inserted at index 5:", x)

# Print the length of list x
# YOUR CODE HERE
print("Number of elements in x:", len(x))


# Print all the values in x multiplied by 1000
# YOUR CODE HERE
def multi_list(nums):
    for i in range(len(x)):
        nums[i] = nums[i] * 1000


multi_list(x)
print("Values of x * 1000:", x)
