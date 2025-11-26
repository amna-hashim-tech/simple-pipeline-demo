def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b * 2  # BUG! Should not multiply by 2!

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b
