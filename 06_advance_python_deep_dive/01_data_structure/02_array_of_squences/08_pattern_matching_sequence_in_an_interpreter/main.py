from typing import Any, Dict, List

Expression = List[Any]
Environment = Dict[str, Any]

def evaluate(exp: Expression, env: Environment) -> Any:
    """
    Evaluate an expression in an environment.

    Parameters:
    - exp: An expression in the form of a list, like ['add', 2, 3].
    - env: A dictionary representing the environment.

    Returns:
    - The result of the operation specified in the expression.
    """
    match exp:
        case ['add', x, y]:
            return x + y
        case ['subtract', x, y]:
            return x - y
        case ['multiply', x, y]:
            return x * y
        case ['divide', x, y] if y != 0:
            return x / y
        case _:
            raise ValueError("Unsupported operation or division by zero")

# Testing the function
print(evaluate(['add', 5, 3], {}))  # Expected Output: 8
print(evaluate(['subtract', 10, 4], {}))  # Expected Output: 6
print(evaluate(['multiply', 7, 6], {}))  # Expected Output: 42
print(evaluate(['divide', 20, 5], {}))  # Expected Output: 4
try:
    print(evaluate(['divide', 20, 0], {}))  # This should raise an error
except ValueError as e:
    print(e)  # Output: Unsupported operation or division by zero


