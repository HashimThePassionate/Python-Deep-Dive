# What is Abstraction?

Abstraction is one of the fundamental principles of object-oriented programming (OOP). It involves hiding the complex implementation details of a method or class and exposing only the essential features to the user. This allows users to interact with an object without needing to understand the underlying complexity.

### How Abstraction is Used in the `Browser` Class

In the `Browser` class, abstraction is used through the use of private methods, which are prefixed with double underscores (`__`). These methods include:

- **`__find_ip_address`:** Abstracts the logic for determining the IP address or handling empty inputs.
- **`__send_http_request`:** Abstracts the process of simulating an HTTP request and generating the corresponding response.
- **`__is_valid_ip`:** Abstracts the logic for validating an IPv4 address.

These private methods are not exposed to the user directly; instead, the user interacts with the public `navigate` method, which provides a simple interface for navigating to a web address. The complexity of address validation, HTTP request simulation, and IP checking is hidden from the user, making the class easier to use and understand.

### Why Use Abstraction?

Abstraction is used to:
- Simplify the interaction with complex systems.
- Reduce the likelihood of user errors by limiting access to only the necessary methods.
- Make the code easier to maintain and update, as the internal implementation can be changed without affecting the public interface.

In this example, the user of the `Browser` class only needs to understand how to use the `navigate` method, without worrying about the details of IP validation or how HTTP requests are simulated.
# Browser Class
This section file provides a comprehensive explanation of a Python class named `Browser`, which simulates the basic functionality of a web browser. The `Browser` class allows you to navigate to a given address (either a domain name or an IP address) and return an HTML response if the address is valid, or an error message if it is not. 

This example also demonstrates the concept of abstraction in object-oriented programming (OOP), which is used to hide the complexity of certain methods and expose only the necessary functionality to the user.

## Complete Code

```python
class Browser:
    def navigate(self, address: str):
        ip = self.__find_ip_address(address)
        if ip is None:
            return "No IP address or domain found"
        html = self.__send_http_request(ip)
        return html

    def __find_ip_address(self, ip: str) -> str:
        if not ip:
            return None
        return ip

    def __send_http_request(self, ip: str):
        if self.__is_valid_ip(ip) or ip == 'localhost':
            return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>Welcome to the website</h1>
            </body>
            </html>"""
        else:
            return "404 Not Found"


    def __is_valid_ip(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
            return True
        return False

# Testing the code
nav = Browser()
print(nav.navigate('localhost'))  # Should return HTML content
print(nav.navigate(''))           # Should return "No IP address or domain found"
print(nav.navigate(None))         # Should return "No IP address or domain found"
print(nav.navigate('127.0.0.1'))  # Should return HTML content for the IP
print(nav.navigate('invalid-ip'))  # Should return "404 Not Found"
```

## Class: Browser

### Overview of the `Browser` Class

The `Browser` class is designed to simulate simple web navigation. It allows you to navigate to a given address (either a domain name or an IP address) and return HTML content or an error message. The class uses several private methods to encapsulate and abstract the details of IP address validation and HTTP request simulation.

### Methods

#### 1. `navigate(self, address: str) -> str`

This is the primary method of the `Browser` class that users interact with. It accepts a string `address` and returns an HTML response if the address is valid, or an error message if it is not.

- **Parameters:**
  - `address` (str): The web address (either a domain name or an IP address) that the browser will navigate to.

- **Process:**
  1. The method first calls the private method `__find_ip_address` to process the input address.
  2. If the address is empty or `None`, it returns "No IP address or domain found."
  3. It then calls the private method `__send_http_request` to simulate sending an HTTP request to the processed IP.
  4. The method finally returns the HTML content if the address is valid or a "404 Not Found" error if it is not.

- **Example Usage:**
  ```python
  nav = Browser()
  print(nav.navigate('localhost'))  # Returns HTML content
  print(nav.navigate(''))           # Returns "No IP address or domain found"
  print(nav.navigate(None))         # Returns "No IP address or domain found"
  print(nav.navigate('127.0.0.1'))  # Returns HTML content for the IP
  print(nav.navigate('invalid-ip'))  # Returns "404 Not Found"
  ```

#### 2. `__find_ip_address(self, ip: str) -> str`

This is a private method that processes the input address. The method is designed to be internal and not accessed directly by users of the `Browser` class.

- **Parameters:**
  - `ip` (str): The address or IP provided to the `navigate` method.

- **Returns:**
  - The provided address if it is not empty.
  - `None` if the input is an empty string or `None`.

- **Purpose:**
  - This method abstracts the complexity of address validation. It ensures that if an empty or `None` input is provided, the `navigate` method can handle it gracefully by returning an appropriate message.

#### 3. `__send_http_request(self, ip: str) -> str`

This private method simulates sending an HTTP request to the provided IP address or domain name.

- **Parameters:**
  - `ip` (str): The IP address or domain name to which the request is sent.

- **Returns:**
  - A string containing HTML content if the IP or domain is valid (including the special case of 'localhost').
  - A "404 Not Found" message if the IP or domain is invalid.

- **Purpose:**
  - The method is abstracted from the user, meaning they don't need to understand the details of how an HTTP request is simulated. The method handles both valid IPs and the special case of 'localhost'.

#### 4. `__is_valid_ip(self, ip: str) -> bool`

This private method checks if the input string is a valid IPv4 address.

- **Parameters:**
  - `ip` (str): The IP address to be validated.

- **Returns:**
  - `True` if the IP address is valid (consists of four numeric segments, each between 0 and 255).
  - `False` if the IP address is not valid.

- **Detailed Explanation:**
  - The IP address is split into segments using the dot (`.`) separator.
  - The method ensures that there are exactly four segments and that each segment is a number within the valid range for an IPv4 address (0 to 255).

- **Purpose:**
  - This method abstracts the complexity of IP validation, ensuring that only valid IPv4 addresses are accepted by the `navigate` method.

### Example Usage of the `Browser` Class

Here is an example of how the `Browser` class can be used:

```python
nav = Browser()
print(nav.navigate('localhost'))  # Should return HTML content
print(nav.navigate(''))           # Should return "No IP address or domain found"
print(nav.navigate(None))         # Should return "No IP address or domain found"
print(nav.navigate('127.0.0.1'))  # Should return HTML content for the IP
print(nav.navigate('invalid-ip'))  # Should return "404 Not Found"
```

### Output
When running the above example code, you should expect the following output:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to the website</h1>
</body>
</html>
No IP address or domain found
No IP address or domain found
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to the website</h1>
</body>
</html>
404 Not Found
```

## Conclusion

The `Browser` class in this example illustrates the use of abstraction to hide complex logic while providing a simple and intuitive interface for users. By using private methods, the class encapsulates the details of IP address validation,

 HTTP request simulation, and input handling, allowing users to focus on the main functionality of navigating to web addresses. This example is a practical demonstration of how abstraction can be effectively used in object-oriented programming.