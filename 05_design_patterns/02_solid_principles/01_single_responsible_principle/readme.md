# 📚 **Single Responsibility Principle** 🏆

Welcome to the easy-to-understand guide on the **Single Responsibility Principle (main)**! 🚀 This document breaks down what main is, why it's important, how to use it, and provides simple examples to help you grasp the concept. 💡 All code examples use **static typing** to make things clear and reliable. 🛠️✨

---

## 📖 Table of Contents 📖

- [📚 **Single Responsibility Principle** 🏆](#-single-responsibility-principle-)
  - [📖 Table of Contents 📖](#-table-of-contents-)
  - [🔍 Introduction](#-introduction)
  - [💡 What is the Single Responsibility Principle (main)?](#-what-is-the-single-responsibility-principle-main)
  - [🏆 Benefits of main](#-benefits-of-main)
  - [🛠️ How to Apply main](#️-how-to-apply-main)
  - [📂 Example: Report Generation Before main](#-example-report-generation-before-main)
  - [🔄 Refactoring to Follow main](#-refactoring-to-follow-main)
    - [1. Creating the `Report` Class](#1-creating-the-report-class)
    - [2. Creating the `ReportSaver` Class](#2-creating-the-reportsaver-class)
    - [3. Testing the Refactored Classes](#3-testing-the-refactored-classes)
  - [🧪 Testing the Example](#-testing-the-example)
  - [🔗 Conclusion](#-conclusion)

---

## 🔍 Introduction

The **Single Responsibility Principle (main)** is a key idea in software design. 🛡️ It says that each class should have only one job or reason to change. By keeping classes focused on one task, your code becomes easier to maintain, understand, and grow. 📈

---

## 💡 What is the Single Responsibility Principle (main)?

**Single Responsibility Principle (main)** means that a class should do just one thing. 🎯 Each class should handle only one part of the functionality. This makes your code easier to manage and reduces the chances of bugs when you make changes. 🏗️

---

## 🏆 Benefits of main

Using main brings several important benefits:

- **🔧 Maintainability**: Smaller, focused classes are easier to understand and update.
- **🛠️ Extensibility**: Adding new features or making changes is simpler without affecting other parts.
- **🧪 Testability**: Classes with one responsibility are easier to test, leading to better software quality.
- **📚 Readability**: Clear and simple classes make your code easier to read and follow.

---

## 🛠️ How to Apply main

Following main involves designing classes that handle only one task. 🧩 Here are some steps to apply main effectively:

1. **Identify Responsibilities**: Look at your classes to see if they are doing more than one thing.
2. **Separate Concerns**: Split classes into smaller ones, each handling a single responsibility.
3. **Use Interfaces and Protocols**: Define clear roles for each class, making them work well together without being tightly connected.
4. **Encapsulate Functionality**: Keep related actions within one class and separate unrelated actions into different classes.

By doing this, you create a well-organized and flexible codebase that’s easy to work with. 🔄

---

## 📂 Example: Report Generation Before main

Let's look at an example where a class does too much. Imagine you have a `Report` class that both creates report content and saves it to a file. 📝💾

```python
class Report:
    def __init__(self, content: str):
        self.content: str = content

    def generate(self) -> None:
        print(f"Report content: {self.content}")

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            file.write(self.content)
```

In this example, the `Report` class has two jobs:
1. Creating the report content.
2. Saving the report to a file.

This makes the class harder to manage and more likely to have bugs when you need to make changes. ⚠️

---

## 🔄 Refactoring to Follow main

To follow main, we'll split the `Report` class into two separate classes: `Report` and `ReportSaver`. 🛠️✨

### 1. Creating the `Report` Class

The `Report` class will only handle creating and managing the report content. 📄

```python
class Report:
    def __init__(self, content: str) -> None:
        self.content: str = content

    def generate(self) -> None:
        print(f"Report content: {self.content}")
```

### 2. Creating the `ReportSaver` Class

The `ReportSaver` class will handle saving the report content to a file. 💾

```python
class ReportSaver:
    def __init__(self, report: Report) -> None:
        self.report: Report = report

    def save_to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(self.report.content)
```

### 3. Testing the Refactored Classes

We'll add a test script to make sure our new classes work correctly. 🧪

```python
if __name__ == "__main__":
    report_content: str = "This is the content."
    report: Report = Report(report_content)
    report.generate()

    report_saver: ReportSaver = ReportSaver(report)
    report_saver.save_to_file("report.txt")
```

---

## 🧪 Testing the Example

To test the refactored code, follow these steps:

1. **Save the Code**: Make sure all the code is saved in a file named `01_single_responsible_principle/main.py`.

    ```python
    class Report:
        def __init__(self, content: str) -> None:
            self.content: str = content

        def generate(self) -> None:
            print(f"Report content: {self.content}")

    class ReportSaver:
        def __init__(self, report: Report) -> None:
            self.report: Report = report

        def save_to_file(self, filename: str) -> None:
            with open(filename, "w") as file:
                file.write(self.report.content)

    if __name__ == "__main__":
        report_content: str = "This is the content."
        report: Report = Report(report_content)
        report.generate()

        report_saver: ReportSaver = ReportSaver(report)
        report_saver.save_to_file("report.txt")
    ```

2. **Run the Code**: Open your terminal and run the following command:

    ```bash
    python 01_single_responsible_principle/main.py
    ```

3. **Expected Output**:

    ```
    Report content: This is the content.
    ```

4. **Check the File**: Look for a file named `report.txt` in the same directory. It should contain:

    ```
    This is the content.
    ```

This shows that our refactored classes work correctly and follow main, making the code cleaner and easier to manage. ✅

---

## 🔗 Conclusion

The **Single Responsibility Principle (main)** is a fundamental idea in software design that emphasizes giving each class only one job. 🛡️ By keeping classes focused and specialized, main makes your code easier to maintain, understand, and expand. 📈
