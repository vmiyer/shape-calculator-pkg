import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        raise NotImplementedError("Subclasses must implement 'area' method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement 'perimeter' method.")

    def get_type(self):
        """Returns the type of the shape."""
        return self.__class__.__name__

class Circle(Shape):
    """Represents a circle with a given radius."""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    """Represents a rectangle with given width and height."""
    def __init__(self, width, height):
        if not all(isinstance(dim, (int, float)) and dim >= 0 for dim in [width, height]):
            raise ValueError("Width and height must be non-negative numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Triangle(Shape):
    """Represents a triangle with given side lengths (a, b, c).
    Uses Heron's formula for area and sum of sides for perimeter.
    """
    def __init__(self, a, b, c):
        if not all(isinstance(side, (int, float)) and side >= 0 for side in [a, b, c]):
            raise ValueError("Side lengths must be non-negative numbers.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid side lengths for a triangle.")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Calculates the area of the triangle using Heron's formula."""
        s = self.perimeter() / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """Calculates the perimeter of the triangle."""
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"