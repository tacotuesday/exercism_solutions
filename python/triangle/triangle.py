""" Group of functions to classify three-member lists as different types of triangles. This would make a great set
of class methods, but that probably wouldn't pass tests."""

def equilateral(sides: list) -> bool:
    """
    Determines whether the triangle is equilateral. An equilateral triangle has three sides of equal length.
    :param sides:
    """
    if sum(sides) == 0:
        return False
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) == 1


def isosceles(sides: list) -> bool:
    """
    Determines whether the triangle is isosceles. An isosceles triangle has at least two sides the same length.
    :param sides:
    """
    if (
        sides[0] + sides[1] < sides[2]
        or sides[1] + sides[2] < sides[0]
        or sides[0] + sides[2] < sides[1]
    ):
        return False
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) <= 2


def scalene(sides: list) -> bool:
    """
    Determines whether the triangle is scalene. Scalene triangles have no sides of equal length.
    :param sides:
    """
    if (
        sides[0] + sides[1] < sides[2]
        or sides[1] + sides[2] < sides[0]
        or sides[0] + sides[2] < sides[1]
    ):
        return False
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) == 3