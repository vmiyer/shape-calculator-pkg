from .shapes import Shape, Circle, Rectangle, Triangle

def calculate_area(shape: Shape):
    """
    Calculates the area of a given shape object.

    Args:
        shape (Shape): An instance of a Shape subclass (e.g., Circle, Rectangle, Triangle).

    Returns:
        float: The calculated area.
    """
    if not isinstance(shape, Shape):
        raise TypeError("Input must be an instance of a Shape subclass.")
    return shape.area()

def calculate_perimeter(shape: Shape):
    """
    Calculates the perimeter of a given shape object.

    Args:
        shape (Shape): An instance of a Shape subclass (e.g., Circle, Rectangle, Triangle).

    Returns:
        float: The calculated perimeter.
    """
    if not isinstance(shape, Shape):
        raise TypeError("Input must be an instance of a Shape subclass.")
    return shape.perimeter()

def describe_shape(shape: Shape):
    """
    Provides a description of the shape along with its area and perimeter.

    Args:
        shape (Shape): An instance of a Shape subclass.

    Returns:
        str: A formatted string describing the shape.
    """
    if not isinstance(shape, Shape):
        raise TypeError("Input must be an instance of a Shape subclass.")
    
    shape_type = shape.get_type()
    area = calculate_area(shape)
    perimeter = calculate_perimeter(shape)

    return (f"--- {shape_type} ---"
            f"\n  Details: {shape}"
            f"\n  Area: {area:.2f}"
            f"\n  Perimeter: {perimeter:.2f}")

if __name__ == '__main__':
    # Example usage within the module for testing
    print("--- Testing calculator.py directly ---")
    
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 6)
    my_triangle = Triangle(3, 4, 5) # A right-angled triangle

    print(describe_shape(my_circle))
    print("\n" + describe_shape(my_rectangle))
    print("\n" + describe_shape(my_triangle))

    try:
        invalid_shape = "not_a_shape"
        print(describe_shape(invalid_shape))
    except TypeError as e:
        print(f"\nCaught expected error: {e}")