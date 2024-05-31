The Python code crashed due to an `AttributeError`. Here's a detailed explanation of what happened:

1. The `ExceptionsDemo` class has two static methods: `show` and `say_hello`.

2. The `show` method calls `say_hello` with `None` as the argument:
   ```python
   @staticmethod
   def show():
       ExceptionsDemo.say_hello(None)
   ```

3. The `say_hello` method attempts to call the `upper` method on the `name` argument:
   ```python
   @staticmethod
   def say_hello(name):
       print(name.upper())
   ```

4. When `ExceptionsDemo.show()` is executed, it calls `ExceptionsDemo.say_hello(None)`. Inside `say_hello`, `name` is `None`.

5. The `None` type in Python does not have an `upper` method. As a result, trying to call `None.upper()` raises an `AttributeError`.

Here's the traceback you would see if you ran this code:

```plaintext
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    ExceptionsDemo.show()
  File "script.py", line 4, in show
    ExceptionsDemo.say_hello(None)
  File "script.py", line 8, in say_hello
    print(name.upper())
AttributeError: 'NoneType' object has no attribute 'upper'
```

To prevent this crash, you should add a check in the `say_hello` method to ensure that `name` is not `None` before calling `upper`: