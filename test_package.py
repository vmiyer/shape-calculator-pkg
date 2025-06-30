try:
    from shape_calculator import Circle, Rectangle, Triangle, calculate_area, calculate_perimeter, describe_shape
    print("Successfully imported 'shape_calculator' package.")
except ImportError as e:
    print(f"Error importing 'shape_calculator': {e}")
    print("Please ensure the package is installed. Run 'pip install .' in the project root directory.")
    exit(1)

def run_tests():
    """
    Demonstrates the functionality of the shape_calculator package.
    """
    print("\n--- Running Shape Calculator Package Tests ---")

    # --- Test Circle ---
    print("\nTesting Circle:")
    try:
        circle = Circle(5)
        print(describe_shape(circle))
        assert abs(circle.area() - 78.539) < 0.01
        assert abs(circle.perimeter() - 31.415) < 0.01
        print("  Circle tests passed.")
    except Exception as e:
        print(f"  Circle test failed: {e}")

    # Test invalid circle
    try:
        Circle(-1)
        print("  FAIL: Created circle with negative radius.")
    except ValueError:
        print("  PASS: Correctly rejected negative radius for Circle.")
    
    try:
        Circle("abc")
        print("  FAIL: Created circle with non-numeric radius.")
    except ValueError:
        print("  PASS: Correctly rejected non-numeric radius for Circle.")

    # --- Test Rectangle ---
    print("\nTesting Rectangle:")
    try:
        rectangle = Rectangle(width=10, height=4)
        print(describe_shape(rectangle))
        assert rectangle.area() == 40
        assert rectangle.perimeter() == 28
        print("  Rectangle tests passed.")
    except Exception as e:
        print(f"  Rectangle test failed: {e}")

    # Test invalid rectangle
    try:
        Rectangle(10, -5)
        print("  FAIL: Created rectangle with negative height.")
    except ValueError:
        print("  PASS: Correctly rejected negative height for Rectangle.")

    # --- Test Triangle ---
    print("\nTesting Triangle (3,4,5 - a right-angled triangle):")
    try:
        triangle = Triangle(3, 4, 5)
        print(describe_shape(triangle))
        assert abs(triangle.area() - 6.0) < 0.01 # Area of 3-4-5 triangle is 6
        assert triangle.perimeter() == 12
        print("  Triangle (3,4,5) tests passed.")
    except Exception as e:
        print(f"  Triangle (3,4,5) test failed: {e}")

    # Test an equilateral triangle
    print("\nTesting Triangle (equilateral 5,5,5):")
    try:
        equi_triangle = Triangle(5, 5, 5)
        print(describe_shape(equi_triangle))
        assert abs(equi_triangle.area() - 10.825) < 0.01
        assert equi_triangle.perimeter() == 15
        print("  Equilateral triangle (5,5,5) tests passed.")
    except Exception as e:
        print(f"  Equilateral triangle (5,5,5) test failed: {e}")

    # Test invalid triangle (violates triangle inequality)
    print("\nTesting invalid Triangle (1,2,5):")
    try:
        Triangle(1, 2, 5)
        print("  FAIL: Created invalid triangle (1,2,5).")
    except ValueError:
        print("  PASS: Correctly rejected invalid triangle (1,2,5).")

    # --- Test general utility functions ---
    print("\nTesting utility functions with different shapes:")
    shapes_to_test = [
        Circle(1),
        Rectangle(2, 2), # Square
        Triangle(6, 8, 10) # Another right-angled triangle
    ]

    for s in shapes_to_test:
        print(f"\n--- Testing {s.get_type()} ---")
        print(f"  Area via function: {calculate_area(s):.2f}")
        print(f"  Perimeter via function: {calculate_perimeter(s):.2f}")
        print(f"  Description:\n{describe_shape(s)}")

    # Test with non-Shape object for utility functions
    print("\nTesting utility functions with non-Shape object:")
    try:
        calculate_area("not a shape")
        print("  FAIL: calculate_area accepted non-Shape object.")
    except TypeError:
        print("  PASS: calculate_area correctly rejected non-Shape object.")
    
    try:
        describe_shape({"key": "value"})
        print("  FAIL: describe_shape accepted non-Shape object.")
    except TypeError:
        print("  PASS: describe_shape correctly rejected non-Shape object.")


    print("\n--- All tests completed ---")

if __name__ == "__main__":
    run_tests()
