# 🔐 Reducing Coupling with Mangling Convention in Python

In Python, **name mangling** (using `__` before method names) makes members private to a class. This convention doesn’t directly reduce coupling but supports **encapsulation** and **information hiding**, which help lower dependencies between classes.

---

## 📑 Table of Contents

- [🔐 Reducing Coupling with Mangling Convention in Python](#-reducing-coupling-with-mangling-convention-in-python)
  - [📑 Table of Contents](#-table-of-contents)
    - [⚙️ Original Code](#️-original-code)
    - [🔍 How Mangling Reduces Coupling](#-how-mangling-reduces-coupling)
    - [📜 Summary](#-summary)

---

### ⚙️ Original Code

```python
class Browser:
    def navigate(self, address):
        ip = self.__find_ip_address(address)
        html = self.__send_http_request(ip)
        print(html)

    def __send_http_request(self, ip):
        return "<html></html>" if ip else "No IP address or domain found"

    def __find_ip_address(self, address):
        return address or None

browser = Browser()
browser.navigate('127.0.0.0')
browser.navigate(None)
```

---

### 🔍 How Mangling Reduces Coupling

1. **Encapsulation**: Methods `__send_http_request` and `__find_ip_address` are hidden, keeping internal logic private and reducing dependencies on the class’s internal details.

2. **Preventing External Access**: Name mangling prevents external access and unintended overrides, ensuring `Browser` only exposes necessary methods.

3. **Information Hiding**: Mangling limits what external code sees, enforcing interaction solely through `navigate` and lowering coupling.

---

### 📜 Summary

Name mangling in Python supports encapsulation and information hiding, indirectly reducing coupling by keeping internals private, preventing interference, and promoting flexible, maintainable code.