def calculator(num1, num2):
    try:
        # Ensure inputs are numbers
        num1 = float(num1)
        num2 = float(num2)
        
        # Perform addition
        result = num1 + num2
        
        return f"{num1} + {num2} = {result}"
    except ValueError:
        return "Error: Please enter valid numbers."

# Example usage
if __name__ == "__main__":
    # Replace input with predefined values to avoid I/O error
    num1, num2 = 10, 5  # Example values
    print(calculator(num1, num2))
