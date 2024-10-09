# Quiz Time 😊
### ❓ **Quiz 1: Function with Unlimited Arguments**
**Problem:**  
You need to write a function that accepts **any number** of input arguments.  
💡 **Hint:** In Python, you can use `*args` to handle multiple arguments.

### ❓ **Quiz 2: Only Keyword Arguments Allowed**
**Problem:**  
You want a function to accept **only specific arguments** by keyword.  
💡 **Hint:** You can enforce this using `*` in the function definition to limit the function to keyword-only arguments.

### ❓ **Quiz 3: Adding Information to Arguments**
**Problem:**  
You’ve written a function but want to attach some **additional information** to the arguments so others know how the function should be used.  
💡 **Hint:** You can use decorators or function annotations to provide this information in Python.

### ❓ **Quiz 4: Returning Multiple Values**
**Problem:**  
You want to write a function that **returns multiple values**.  
💡 **Hint:** In Python, you can return multiple values using tuples, lists, or dictionaries.

### ❓ **Quiz 5: Optional Arguments with Default Values**
**Problem:**  
You want to define a function where **some arguments are optional** and have **default values**.  
💡 **Hint:** You can assign default values using `=` in the function definition, e.g., `def function(arg=default_value)`.

### ❓ **Quiz 6: Inline Callback Function (Without `def`)**
**Problem:**  
You need to supply a **short inline callback function** for use with operations like `sort()`, but you don’t want to write a full function with `def`.  
💡 **Hint:** Use a `lambda` function for quick one-line callbacks.

### ❓ **Quiz 7: Capturing Variables in a Lambda**
**Problem:**  
You’ve defined an anonymous function using **lambda**, but you also need to capture certain **variables' values at the time of definition**.  
💡 **Hint:** This can be done using closures or capturing values with `lambda`.

### ❓ **Quiz 8: Reducing Arguments in a Callable**
**Problem:**  
You have a callable that takes **too many arguments**, and you need to use it with other Python code, but it causes exceptions due to the argument count.  
💡 **Hint:** You can solve this using `functools.partial` to reduce the number of arguments.

### ❓ **Quiz 9: Extra State in Callback Functions**
**Problem:**  
You’re writing code that relies on **callback functions** (like event handlers or completion callbacks), and you want the callback to carry **extra state** inside the function.  
💡 **Hint:** You can manage this with closures or custom objects to carry state.

### ❓ **Quiz 10: Simplifying Callback Control Flow**
**Problem:**  
You want to simplify code that uses **callback functions**, making it look more like a **normal sequence of steps** instead of complex control flow.  
💡 **Hint:** Use generators or coroutines to streamline the control flow.

### ❓ **Quiz 11: Extending Closures**
**Problem:**  
You would like to extend a **closure** so that the inner variables can be **accessed and modified**.  
💡 **Hint:** You can achieve this by defining functions inside functions or using classes.
