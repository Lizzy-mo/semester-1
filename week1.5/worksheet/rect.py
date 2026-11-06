# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """

    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an int")
        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError("height must be an int")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns True if the rectangle is a square, otherwise False.
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)
