# Define a simple pattern matching function for lambda
def match_lambda(expr, param_values):
    """
    Matches and processes a lambda expression.
    
    Args:
        expr (list): The lambda expression to match.
        param_values (dict): A dictionary mapping parameter names to their values.
    """
    match expr:
        # Match the pattern for a lambda expression with parameters and body
        case ['lambda', [*params], *body] if body:
            print("Lambda Parameters:", params)
            print("Lambda Body:", body)
            
            # Check if the body contains a simple addition operation
            if len(body) == 1 and len(body[0]) == 3 and body[0][0] == '+':
                # Replace parameters with their actual values from param_values
                x_value = param_values[params[0]]
                y_value = param_values[params[1]]
                result = x_value + y_value
                print(f"Result of ({params[0]} + {params[1]}):", result)
        # Handle cases where the expression is not a lambda expression
        case _:
            print("Not a lambda expression")

# Example usage
param_values = {'x': 3, 'y': 5}
match_lambda(['lambda', ['x', 'y'], ['+', 'x', 'y']], param_values)
