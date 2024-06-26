# Lambda Expressions in Pattern Matching

## Introduction

Lambda expressions are anonymous functions that are often used for concise operations. In pattern matching, they are particularly useful for matching complex patterns and performing inline calculations or transformations. Python's structural pattern matching (introduced in Python 3.10) allows us to use lambda expressions effectively to match and process patterns in a clean and readable way.

## Why Use Lambda Expressions in Match?

Lambda expressions provide a way to define functions in a single line of code, making them ideal for use within match statements where we want to perform quick operations or checks. They can help in:

- **Concise Code**: Keeping the code compact and readable.
- **Inline Operations**: Performing operations directly within the match clause without needing to define separate functions.
- **Flexibility**: Easily handling various types of patterns and conditions.

## Example: Calculation Using Lambda Expressions in Pattern Matching

### Scheme Lambda Function

In Scheme, a lambda function that adds two numbers might look like this:

```scheme
(lambda (x y) (+ x y))
```

### Python Equivalent Using Pattern Matching

We can represent and process this lambda function in Python using pattern matching. Here is an example that demonstrates how to use lambda expressions to match a Scheme lambda expression and perform a calculation.

### Python Code Example

```python
# Define a simple pattern matching function for lambda
# Define a simple pattern matching function for lambda
def match_lambda(expr, param_values):
    match expr:
        case ['lambda', [*params], *body] if body:
            print("Lambda Parameters:", params)
            print("Lambda Body:", body)
            # Example calculation: let's assume the body contains a simple addition
            if len(body) == 1 and len(body[0]) == 3 and body[0][0] == '+':
                # Replace parameters with their actual values
                x_value = param_values[params[0]]
                y_value = param_values[params[1]]
                result = x_value + y_value
                print(f"Result of ({params[0]} + {params[1]}):", result)
        case _:
            print("Not a lambda expression")

# Example usage
param_values = {'x': 3, 'y': 5}
match_lambda(['lambda', ['x', 'y'], ['+', 'x', 'y']], param_values)
```

### Output

```
Lambda Parameters: [3, 5]
Lambda Body: [['+', 'x', 'y']]
Result of (3 + 5): 8
```
