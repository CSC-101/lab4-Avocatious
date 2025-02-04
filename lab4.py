import data

# Write your functions for each part in the space below.

# Part 1
def first_element(lst: list[list[int]]) -> list[int]:
    return [sublist[0] for sublist in lst if sublist] #returns a list of the first elements of each non-empty nested list

# Part 2
def x_coordinates(points:list[data.Point]) -> list[float]: #Returns a list of x-coordinates from a list of Point objects.
    return [p.x for p in points]
# Part 3
def are_in_positive_quadrant(points: list[data.Point])-> list[data.Point]: #Returns a list of points that are in the first quadrant
    return [p for p in points if p.x>0 and p.y >0 ] #ensures both x and y values are positive, i.e Q1
# Part 4
def distance(p1: data.Point, p2: data.Point) -> float: #computes Euclidean distance between two points
    return((p1.x-p2.x)**2 + (p1.y-p2.y)**2) ** 5 # equation for Euclidean distance ie pythagorean theorem


# Part 5
def manhattan_distance(p1: data.Point, p2: data.Point) -> float: #computes the manhattan distance between two points
    return abs(p1.x - p2.x) + abs(p1.y-p2.y)

# Part 6
def distance_all(points: list[data.Point]) -> list[float]: #returns a list of distances from origin to point
    origin = data.Point(0,0)
    return [distance(origin,p) for p in points]

