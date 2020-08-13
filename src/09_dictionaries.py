"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]
print(type(waypoints))  # list
print(type(waypoints[0]))  # dictionary
print("Original waypoints:", waypoints)

# Add a new waypoint to the list
# YOUR CODE HERE

new_waypoint = {"lat": 34.6413, "long": 139.6503, "name": "Tokyo, Japan"}
print("New waypoint:", new_waypoint)

waypoints.append(new_waypoint)
print("New waypoint added to dictionary:", waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

waypoints[0]['name'] = "not a real place"
print(f"Waypoint name updated to: \"{waypoints[0]['name']}\"!", waypoints)

waypoints[0]['lon'] = -130
print(f"Waypoint \"{waypoints[0]['name']}\" longitude updated to: \"{waypoints[0]['lon']}\"!", waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

waypoints_values = waypoints[0].values()

print("first waypoint values:", waypoints[0].values())
print("waypoint_values type:", type(waypoints_values))
print("waypoints type:", type(waypoints))


def fun1():
    return ()


func1(*waypoints)
print(func1)

# "The waypoint field values are:".
