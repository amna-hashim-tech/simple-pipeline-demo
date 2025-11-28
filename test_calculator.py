import calculator

def test_add():
    """Test addition"""
    assert calculator.add(2, 3) == 5
    assert calculator.add(0, 0) == 0
    printe("✓ Addition test passed!")

def test_subtract():
    """Test subtraction"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    print("✓ Subtraction test passed!")

def test_multiply():
    """Test multiplication"""
    assert calculator.multiply(2, 3) == 6  # This will FAIL! (code returns 12)
    assert calculator.multiply(5, 4) == 20  # This will FAIL! (code returns 40)
    print("✓ Multiplication test passed!")

def test_divide():
    """Test division"""
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(10, 2) == 5
    print("✓ Division test passed!")

# Run all tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()  # This will fail!
    test_divide()
    print("\n✅ All tests passed!")
