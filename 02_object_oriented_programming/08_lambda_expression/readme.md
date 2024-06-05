# Lambda Expression

In Python, a lambda expression is a small anonymous function defined using the `lambda` keyword. It allows you to create a function without a name. Lambda functions can have any number of arguments, but they can only have one expression. 

The syntax for a lambda function in Python is:

```python
lambda arguments: expression
```

Here's a simple example of a lambda function that adds two numbers:

```python
add = lambda x, y: x + y
```

In this example, `lambda x, y: x + y` is a lambda function that takes two arguments `x` and `y` and returns their sum. The `add` variable now holds a reference to this lambda function.

Lambda functions are often used as arguments to higher-order functions or in situations where defining a named function is unnecessary or cumbersome. For example, you might use a lambda function with the `sorted()` function to define custom sorting criteria:

```python
points = [(1, 2), (3, 1), (5, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
```

In this example, the `key` parameter of the `sorted()` function specifies a function that is called to extract the sorting key from each element. Here, the lambda function `lambda point: point[1]` extracts the second element from each tuple in the `points` list, so the list will be sorted based on the second element of each tuple.