# 🌐 Browser Class with Abstraction

This example demonstrates abstraction in Python using a `Browser` class that simulates web navigation. The class allows users to navigate to a specified address and receive an HTML response if the address is valid, or an error message if invalid. Abstraction hides the complexity of IP validation, HTTP request simulation, and address processing, exposing only essential functionality.

---

## 📑 Table of Contents

- [🌐 Browser Class with Abstraction](#-browser-class-with-abstraction)
  - [📑 Table of Contents](#-table-of-contents)
    - [🔍 What is Abstraction?](#-what-is-abstraction)
    - [⚙️ Browser Class Code](#️-browser-class-code)
    - [🧩 Key Methods](#-key-methods)
    - [💡 Example Usage](#-example-usage)
    - [Expected Output](#expected-output)
    - [📜 Conclusion](#-conclusion)

---

### 🔍 What is Abstraction?

**Abstraction** is a key OOP principle that hides complex details, exposing only what is essential. In the `Browser` class, private methods prefixed with `__` encapsulate the complexity of IP validation and HTTP requests, allowing users to interact with a simple `navigate` method.

---

### ⚙️ Browser Class Code

```python
class Browser:
    def navigate(self, address: str):
        ip = self.__find_ip_address(address)
        if ip is None:
            return "No IP address or domain found"
        return self.__send_http_request(ip)

    def __find_ip_address(self, address: str) -> str:
        return address if address else None

    def __send_http_request(self, ip: str):
        if self.__is_valid_ip(ip) or ip == 'localhost':
            return "<html><h1>Welcome to the website</h1></html>"
        return "404 Not Found"

    def __is_valid_ip(self, ip: str) -> bool:
        parts = ip.split('.')
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
```

---

### 🧩 Key Methods

1. **`navigate(self, address: str) -> str`**: Public method for navigation. Calls private methods to process the address and simulate an HTTP request.

2. **`__find_ip_address(self, address: str) -> str`**: Private method that checks for a valid address or returns `None`.

3. **`__send_http_request(self, ip: str) -> str`**: Private method that simulates an HTTP request, returning HTML content for valid IPs or "404 Not Found" otherwise.

4. **`__is_valid_ip(self, ip: str) -> bool`**: Private method to validate an IPv4 address format.

---

### 💡 Example Usage

```python
nav = Browser()
print(nav.navigate('localhost'))       # Returns HTML content
print(nav.navigate(''))                # Returns "No IP address or domain found"
print(nav.navigate(None))              # Returns "No IP address or domain found"
print(nav.navigate('127.0.0.1'))       # Returns HTML content
print(nav.navigate('invalid-ip'))      # Returns "404 Not Found"
```

### Expected Output

```
<html><h1>Welcome to the website</h1></html>
No IP address or domain found
No IP address or domain found
<html><h1>Welcome to the website</h1></html>
404 Not Found
```

---

### 📜 Conclusion

The `Browser` class demonstrates **abstraction** by hiding complex IP validation and HTTP request logic within private methods, allowing users to focus on the `navigate` method. This encapsulation simplifies the class’s usage and enhances maintainability.