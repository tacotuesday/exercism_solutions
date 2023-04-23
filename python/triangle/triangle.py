""" Group of functions to classify three-member lists as different types of triangles. This would make a great set
of class methods, but that probably wouldn't pass tests."""

def triangle(func: callable) -> callable:
    """Decorator to check if the sides of a triangle are valid. If not, return False.

    :param func: Function to be decorated
    :type func: function
    """       
    def is_triangle(sides):
        if sum(sides) != 0 and (
            sides[0] + sides[1] >= sides[2]
            and sides[1] + sides[2] >= sides[0]
            and sides[0] + sides[2] >= sides[1]
        ): return func(sides)
        else:
            return False
    return is_triangle

@triangle
def equilateral(sides: list) -> bool:
    """
    Determines whether the triangle is equilateral. An equilateral triangle has three sides of equal length.
    :param sides: List of three sides of a triangle
    """
    return len(set(sides)) == 1

@triangle
def isosceles(sides: list) -> bool:
    """
    Determines whether the triangle is isosceles. An isosceles triangle has at least two sides the same length.
    :param sides: List of three sides of a triangle
    """
    return len(set(sides)) <= 2

@triangle
def scalene(sides: list) -> bool:
    """
    Determines whether the triangle is scalene. Scalene triangles have no sides of equal length.
    :param sides: List of three sides of a triangle
    """
    return len(set(sides)) == 3
