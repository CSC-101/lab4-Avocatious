import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input2 = [[5,6],[],[7,8,9],[10]]# write a second test here
        result = lab4.first_element(input2)
        expected = [5,7,10] #skips the empty lists
        self.assertEqual(expected,result)

    # Part 2
def test_x_coordinates_1(self):
    points = [data.Point(1,2), data.Point(3,4), data.Point(5,6)]
    result =  lab4.x_coordinates(points)
    expected = [1,3,5]
    self.assertEqual(expected,result)

def test_x_coordinates_2(self):
    points = [data.Point(7,8), data.Point(9,10),data.Point(8,-4)]
    result = lab4.x_coordinates(points)
    expected = [7,9,8]
    self.asserEquaul(expected,result)
    # Part 3
def tests_are_in_positive_quadrant_1(self):
    points = [data.Point(1,1), data.Point(-1,-2), data.Point(1000,-1000)]
    result = lab4.are_in_positive_quadrant(points)
    expected = [data.Point(1,1)]
    self.assertEqual(expected,result)

def tests_are_in_positive_quadrant_2(self):
    points = [data.Point(0,0), data.Point(-1,-1), data.Point(4,20)] #(0,0) and (-1,-1) should be excluded
    result = lab4.are_in_positive_quadrant(points)
    expected = [data.Point(4,20)]
    self.assertEqual(expected,result)
    # Part 4
def test_distance_1(self):
    p1, p2 = data.Point(1,1), data.Point(4,5)
    self.assertAlmostEqual(lab4.distance(p1,p2),5.0)

def test_distance_2(self):
    p1, p2 = data.Point(0,0), data.Point(3,4)
    self.assertAlmostEqual(lab4.distance(p1,p2),5.0)
    # Part 5
def test_manhattan_distance_1(self):
    p1, p2 = data.Point(1,2), data.Point(3,4)
    self.assertEqual(lab4.manhattan_distance(p1,p2),4)

def test_manhattan_distance_2(self):
    p1,p2 = data.Point(0,0), data.Point(10,10)
    self.assertEqual(lab4.manhattan_distance(p1,p2),20)

    # Part 6
def test_distance_all_1(self):
    points = [data.Point(6,8), data.Point(9,12)]
    self.assertEqual(lab4.distance_all(points), [10.0,15.0])

def test_distance_all_2(self):
    points = [data.Point(0,3), data.Point(4,0)]
    self.assertEqual(lab4.distance_all(points), [3.0,4.0])


if __name__ == '__main__':
    unittest.main()
