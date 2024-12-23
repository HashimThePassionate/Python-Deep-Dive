# 🧪 Testing Your Code with pytest 🐍✨

Welcome to your **comprehensive guide** on testing your Python code using **pytest**! 🎉 Whether you're a beginner or looking to sharpen your testing skills, this README will walk you through everything you need to know to ensure your code works flawlessly. Let's dive in! 🚀

---

## 📖 Table of Contents

1. [🌟 Introduction](#-introduction)
2. [🧐 Why Testing is Important](#-why-testing-is-important)
3. [🐍 Getting Started with pytest](#-getting-started-with-pytest)
4. [📥 Installing pytest](#-installing-pytest)
5. [📝 Writing Your First Test](#-writing-your-first-test)
6. [🔍 Writing Tests with pytest](#-writing-tests-with-pytest)
7. [🛠️ Understanding Test Outputs](#-understanding-test-outputs)
8. [❌ A Failing Test](#-a-failing-test)
9. [🛠️ Responding to Test Failures](#-responding-to-test-failures)
10. [➕ Adding More Tests](#-adding-more-tests)
11. [🏛️ Testing Classes](#-testing-classes)
12. [🔧 Using Fixtures](#-using-fixtures)
13. [🏙️ Real-World Example: Building and Testing a To-Do List Application](#-real-world-example-building-and-testing-a-to-do-list-application)
14. [🏁 Try It Yourself Exercises](#-try-it-yourself-exercises)
15. [🎉 Conclusion](#-conclusion)
16. [📚 Additional Resources](#-additional-resources)

---

## 🌟 Introduction

Welcome,👋 In this guide, you'll learn how to **test your Python code** using the powerful **pytest** library. Testing is crucial to ensure your functions and classes behave as expected, especially as your projects grow in complexity. Let's embark on this journey to write reliable and maintainable code! 🛠️🔍

---

## 🧐 Why Testing is Important

When you write a function or a class, it's essential to verify that it works correctly under various conditions. Testing helps you:

- **✅ Ensure Correctness**: Validate that your code produces the expected output for different inputs.
- **🔄 Confidence in Changes**: Safely modify and extend your code without breaking existing functionality.
- **🛡️ Catch Errors Early**: Identify and fix mistakes before users encounter them, enhancing user experience.
- **🤝 Support Collaboration**: Make your codebase reliable for other developers to use and contribute to.

Every programmer makes mistakes, but regular testing helps catch and resolve issues promptly! 🕵️‍♂️✨

---

## 🐍 Getting Started with pytest

**pytest** is a versatile testing framework for Python that makes it easy to write simple and scalable test cases. It's highly favored for its simplicity and powerful features, allowing you to write tests effortlessly and manage them as your projects grow. 📈

---

## 📥 Installing pytest

Python doesn't include pytest by default, so you'll need to install it. Let's get started! 🏁

### 🛠️ Step 1: Update pip

Before installing pytest, ensure that your package installer, **pip**, is up to date. Open your terminal and run:

```bash
python -m pip install --upgrade pip
```

**Explanation**:
- `python -m pip`: Runs the pip module.
- `install --upgrade pip`: Upgrades pip to the latest version.

**Sample Output**:
```
Requirement already satisfied: pip in /.../python3.12/site-packages (22.0.4)
--snip--
Successfully installed pip-22.1.2
```

### 🛠️ Step 2: Install pytest

With pip updated, install pytest using the following command:

```bash
python -m pip install --user pytest
```

**Explanation**:
- `install --user pytest`: Installs pytest for the current user only, avoiding system-wide changes.

**Sample Output**:
```
Collecting pytest
--snip--
Successfully installed attrs-21.4.0 iniconfig-1.1.1 ...pytest-8.x.x
```

**Note**: If you encounter issues on Linux, try running the command without the `--user` flag.

---

## 📝 Writing Your First Test

Let's write a simple function and create tests for it using pytest. We'll use Python 3.12 throughout this guide. 🐍✨

### 🛠️ Example Function: Formatting Names

Create a file named `name_function.py` with the following content:

```python
# name_function.py

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

**Line-by-Line Explanation**:

- `def get_formatted_name(first, last):` 📝
  - **Function Definition**: Defines a function named `get_formatted_name` that takes two parameters: `first` and `last`.
- `"""Generate a neatly formatted full name."""` 📄
  - **Docstring**: Describes what the function does.
- `full_name = f"{first} {last}"` ➕
  - **Concatenation**: Combines `first` and `last` with a space in between.
- `return full_name.title()` 🔠
  - **Return Statement**: Returns the `full_name` with each word capitalized.

### 🛠️ Example Usage

Create another file named `names.py` to use this function:

```python
# names.py

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

**Line-by-Line Explanation**:

- `from name_function import get_formatted_name` 🔗
  - **Import Statement**: Imports the `get_formatted_name` function from `name_function.py`.
- `print("Enter 'q' at any time to quit.")` 📢
  - **Instruction**: Informs the user how to exit the program.
- `while True:` 🔄
  - **Infinite Loop**: Continues to prompt the user until they decide to quit.
- `first = input("\nPlease give me a first name: ")` 📝
  - **User Input**: Prompts the user to enter a first name.
- `if first == 'q':` ❌
  - **Exit Condition**: Checks if the user wants to quit.
- `break` 🚪
  - **Break Statement**: Exits the loop if the user inputs 'q'.
- `last = input("Please give me a last name: ")` 📝
  - **User Input**: Prompts the user to enter a last name.
- `if last == 'q':` ❌
  - **Exit Condition**: Checks if the user wants to quit.
- `break` 🚪
  - **Break Statement**: Exits the loop if the user inputs 'q'.
- `formatted_name = get_formatted_name(first, last)` 🔍
  - **Function Call**: Calls the `get_formatted_name` function with the provided first and last names.
- `print(f"\tNeatly formatted name: {formatted_name}.")` 🖨️
  - **Output**: Displays the neatly formatted full name to the user.

**Sample Interaction**:

```
Enter 'q' at any time to quit.

Please give me a first name: muhammad
Please give me a last name: hashim
    Neatly formatted name: Muhammad Hashim.

Please give me a first name: muzammil
Please give me a last name: abbas
    Neatly formatted name: Muzammil Abbas.

Please give me a first name: q
```

---

## 🔍 Writing Tests with pytest

Automate the testing of your functions to ensure they behave as expected. pytest allows you to write tests efficiently and run them seamlessly. Let's create our first test! 🧪✨

### 🛠️ Step 1: Create Test File

Create a file named `test_name_function.py` with the following content:

```python
# test_name_function.py

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'muhammad hashim' work?"""
    formatted_name = get_formatted_name('muhammad', 'hashim')
    assert formatted_name == 'Muhammad Hashim'
```

**Line-by-Line Explanation**:

- `from name_function import get_formatted_name` 🔗
  - **Import Statement**: Imports the `get_formatted_name` function to be tested.
- `def test_first_last_name():` 🧪
  - **Test Function Definition**: Defines a test function named `test_first_last_name`.
- `"""Do names like 'muhammad hashim' work?"""` 📄
  - **Docstring**: Describes what the test is verifying.
- `formatted_name = get_formatted_name('muhammad', 'hashim')` 📝
  - **Function Call**: Calls the `get_formatted_name` function with sample input.
- `assert formatted_name == 'Muhammad Hashim'` ✅
  - **Assertion**: Checks if the output matches the expected result.

### 🛠️ Step 2: Run the Test

Open your terminal, navigate to the directory containing `test_name_function.py`, and run:

```bash
python -m pytest
```

**Sample Output**:

```python
========================= test session starts ==========================
platform win32 -- Python 3.12.2, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\DELL\Desktop\Python-Deep-Dive\01_python_fundamentals\26_testing_your_code
collected 1 item

test_name_function.py .                                           [100%] 

========================== 1 passed in 0.07s ===========================
```

**Line-by-Line Explanation**:

- `============================= test session starts =============================` 🏁
  - **Session Start**: Indicates the beginning of the test session.
- `platform darwin -- Python 3.12.x, pytest-8.x.x, pluggy-1.x.x` 🖥️🐍
  - **Environment Info**: Displays the platform and versions of Python and pytest.
- `rootdir: /.../python_work/sections_testing` 📁
  - **Root Directory**: Shows the directory where tests are being run.
- `collected 1 item` 📋
  - **Tests Collected**: Indicates the number of tests found.
- `test_name_function.py . [100%]` ✅
  - **Test Result**: A dot (`.`) represents a passing test; `[100%]` indicates all tests passed.
- `============================== 1 passed in 0.00s ==============================` 🥳
  - **Summary**: Confirms that one test passed successfully.

---

## 🛠️ Understanding Test Outputs

When you run pytest, the output provides valuable information:

- **🏷️ Platform & Python Version**: Shows the environment in which tests are running.
- **📁 Root Directory**: Indicates where pytest is executing the tests.
- **📋 Collected Items**: Number of tests collected and executed.
- **✅ Test Results**: Dots (`.`) for passed tests, `F` for failed tests.
- **📝 Summary**: Details about passed and failed tests, including time taken.

**Example**:

```python
============================= test session starts =============================
collected 1 item

test_name_function.py . [100%]

============================== 1 passed in 0.00s ==============================
```

**Detailed Explanation**:

- **`test_name_function.py . [100%]`** ✅
  - **`.` (Dot)**: Represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

In a larger project with multiple tests, you might see multiple dots, `F` for failures, and other indicators. Understanding these symbols helps you quickly assess the status of your tests. 🔍📊

---

## ❌ A Failing Test

Let's see what happens when a test fails! 🛑 Modify `get_formatted_name` to handle middle names improperly:

```python
# name_function.py

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

**Line-by-Line Explanation**:

- `def get_formatted_name(first, middle, last):` 📝
  - **Function Modification**: Added a `middle` parameter, making it mandatory.
- `"""Generate a neatly formatted full name."""` 📄
  - **Docstring**: Describes the function.
- `full_name = f"{first} {middle} {last}"` ➕
  - **Concatenation**: Combines `first`, `middle`, and `last` with spaces.
- `return full_name.title()` 🔠
  - **Return Statement**: Returns the `full_name` with each word capitalized.

### 🛠️ Run the Test Again

```bash
python -m pytest
```

**Sample Output**:

```
============================= test session starts =============================
collected 1 item

test_name_function.py F [100%]

================================== FAILURES ===================================
______________________________ test_first_last_name ______________________________

    def test_first_last_name():
        """Do names like 'muhammad hashim' work?"""
        formatted_name = get_formatted_name('muhammad', 'hashim')
>       assert formatted_name == 'Muhammad Hashim'
E       TypeError: get_formatted_name() missing 1 required positional argument: 'last'

test_name_function.py:5: TypeError
=========================== short test summary info ============================
FAILED test_name_function.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last'
============================== 1 failed in 0.04s ===============================
```

**Line-by-Line Explanation**:

- `test_name_function.py F [100%]` ❌
  - **`F`**: Indicates a failed test.
- `______________________________ test_first_last_name ______________________________` 🛑
  - **Failure Section**: Highlights the test that failed.
- ```python
  def test_first_last_name():
      """Do names like 'muhammad hashim' work?"""
      formatted_name = get_formatted_name('muhammad', 'hashim')
  >   assert formatted_name == 'Muhammad Hashim'
  E   TypeError: get_formatted_name() missing 1 required positional argument: 'last'
  ```
  - **Error Details**:
    - **`TypeError`**: The function was called with missing arguments.
    - **Line Reference**: Points to the exact line in the test file where the error occurred.
- `=========================== short test summary info ============================` 📄
  - **Summary**: Provides a brief overview of the failure.
- `FAILED test_name_function.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last'` ❌
  - **Failure Message**: Explains why the test failed.

This detailed output helps you identify and understand the exact issue that caused the test to fail. 🕵️‍♂️🔍

---

## 🛠️ Responding to Test Failures

When a test fails, **don't change the test**! Instead, **fix your code** to meet the test's expectations. Here's how to address the failure we encountered. 🛠️🔧

### 🛠️ Fixing the Function

Make the `middle` parameter optional by providing a default value:

```python
# name_function.py

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

**Line-by-Line Explanation**:

- `def get_formatted_name(first, last, middle=''):` 📝
  - **Function Signature**: Now accepts an optional `middle` parameter with a default value of an empty string.
- `"""Generate a neatly formatted full name."""` 📄
  - **Docstring**: Describes the function.
- `if middle:` 🔍
  - **Condition Check**: Determines if a middle name was provided.
- `full_name = f"{first} {middle} {last}"` ➕
  - **With Middle Name**: Concatenates first, middle, and last names.
- `else:` ❌
  - **No Middle Name**: Handles cases without a middle name.
- `full_name = f"{first} {last}"` ➕
  - **Without Middle Name**: Concatenates only first and last names.
- `return full_name.title()` 🔠
  - **Return Statement**: Returns the formatted full name with capitalization.

### 🛠️ Run the Test Again

```bash
python -m pytest
```

**Sample Output**:

```
============================= test session starts =============================
collected 1 item

test_name_function.py . [100%]

============================== 1 passed in 0.00s ==============================
```

**Line-by-Line Explanation**:

- `test_name_function.py . [100%]` ✅
  - **`.` (Dot)**: Represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Test Passed**: The function now handles both two-name and three-name inputs correctly. 🎉✅

By making the middle name optional, we've restored the original functionality and ensured that the test passes. 🛠️🔧✅

---

## ➕ Adding More Tests

Enhance your test suite by adding more test cases to cover different scenarios. Let's add a test for names with middle names. 🧪🔍

### 🛠️ Step 1: Update Test File

Add a new test function in `test_name_function.py`:

```python
# test_name_function.py

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'muhammad hashim' work?"""
    formatted_name = get_formatted_name('muhammad', 'hashim')
    assert formatted_name == 'Muhammad Hashim'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```

**Line-by-Line Explanation**:

- `def test_first_last_middle_name():` 🧪
  - **New Test Function**: Defines a test to check handling of middle names.
- `"""Do names like 'Wolfgang Amadeus Mozart' work?"""` 📄
  - **Docstring**: Describes the purpose of the test.
- `formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')` 📝
  - **Function Call**: Calls the function with first, last, and middle names.
- `assert formatted_name == 'Wolfgang Amadeus Mozart'` ✅
  - **Assertion**: Checks if the output matches the expected formatted name.

### 🛠️ Step 2: Run All Tests

```bash
python -m pytest
```

**Sample Output**:

```
============================= test session starts =============================
collected 2 items

test_name_function.py .. [100%]

============================== 2 passed in 0.01s ==============================
```

**Line-by-Line Explanation**:

- `test_name_function.py .. [100%]` ✅✅
  - **Two Dots (`..`)**: Each dot represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Both Tests Passed**: The function correctly handles both two-name and three-name inputs. 🎉✅✅

Adding more tests ensures that your function behaves as expected across a wider range of scenarios, increasing confidence in your code's reliability. 📈🛡️

---

## 🏛️ Testing Classes

Testing isn't limited to functions; you can also test classes to ensure their methods work as intended. Let's create and test a simple class. 🏗️🐍

### 🛠️ Example Class: AnonymousSurvey

Create a file named `survey.py` with the following content:

```python
# survey.py

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

**Line-by-Line Explanation with Emojis**:

- `class AnonymousSurvey:` 🏛️
  - **Class Definition**: Defines a class named `AnonymousSurvey`.
- `"""Collect anonymous answers to a survey question."""` 📄
  - **Docstring**: Describes the purpose of the class.
- `def __init__(self, question):` 🛠️
  - **Initializer**: Defines the constructor method that initializes the survey with a question.
- `"""Store a question, and prepare to store responses."""` 📄
  - **Docstring**: Describes what the initializer does.
- `self.question = question` 📝
  - **Attribute Assignment**: Stores the survey question.
- `self.responses = []` 📄
  - **Attribute Initialization**: Initializes an empty list to store responses.
- `def show_question(self):` 👀
  - **Method Definition**: Defines a method to display the survey question.
- `"""Show the survey question."""` 📄
  - **Docstring**: Describes the method's purpose.
- `print(self.question)` 🖨️
  - **Print Statement**: Outputs the survey question.
- `def store_response(self, new_response):` 🛠️
  - **Method Definition**: Defines a method to store a new response.
- `"""Store a single response to the survey."""` 📄
  - **Docstring**: Describes the method's purpose.
- `self.responses.append(new_response)` ➕
  - **Append Operation**: Adds the new response to the `responses` list.
- `def show_results(self):` 👀
  - **Method Definition**: Defines a method to display all survey responses.
- `"""Show all the responses that have been given."""` 📄
  - **Docstring**: Describes the method's purpose.
- `print("Survey results:")` 🖨️
  - **Print Statement**: Outputs the header for survey results.
- `for response in self.responses:` 🔄
  - **Loop**: Iterates over each response in the `responses` list.
- `print(f"- {response}")` 🖨️
  - **Print Statement**: Outputs each response with a bullet point.

### 🛠️ Example Usage

Create a file named `survey_program.py`:

```python
# survey_program.py

from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
```

**Line-by-Line Explanation with Emojis**:

- `from survey import AnonymousSurvey` 🔗
  - **Import Statement**: Imports the `AnonymousSurvey` class from `survey.py`.
- `question = "What language did you first learn to speak?"` 📝
  - **Question Definition**: Defines the survey question.
- `language_survey = AnonymousSurvey(question)` 🆕
  - **Instance Creation**: Creates an instance of `AnonymousSurvey` with the defined question.
- `language_survey.show_question()` 👀
  - **Method Call**: Displays the survey question.
- `print("Enter 'q' at any time to quit.\n")` 📢
  - **Instruction**: Informs the user how to exit the survey.
- `while True:` 🔄
  - **Infinite Loop**: Continues to prompt the user until they decide to quit.
- `response = input("Language: ")` 📝
  - **User Input**: Prompts the user to enter their response.
- `if response == 'q':` ❌
  - **Exit Condition**: Checks if the user wants to quit.
- `break` 🚪
  - **Break Statement**: Exits the loop if the user inputs 'q'.
- `language_survey.store_response(response)` ➕
  - **Method Call**: Stores the user's response in the survey.
- `print("\nThank you to everyone who participated in the survey!")` 🙏
  - **Thank You Message**: Thanks all participants for their responses.
- `language_survey.show_results()` 👀
  - **Method Call**: Displays all the collected survey responses.

**Sample Interaction**:

```
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```

---

## 🛠️ Testing the AnonymousSurvey Class

Create tests to ensure the `AnonymousSurvey` class behaves correctly. 🧪✅

### 🛠️ Step 1: Create Test File

Create a file named `test_survey.py` with the following content:

```python
# test_survey.py

from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```

**Line-by-Line Explanation**:

- `from survey import AnonymousSurvey` 🔗
  - **Import Statement**: Imports the `AnonymousSurvey` class to be tested.
- `def test_store_single_response():` 🧪
  - **Test Function Definition**: Defines a test function named `test_store_single_response`.
- `"""Test that a single response is stored properly."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `question = "What language did you first learn to speak?"` 📝
  - **Question Definition**: Defines the survey question for the test.
- `language_survey = AnonymousSurvey(question)` 🆕
  - **Instance Creation**: Creates an instance of `AnonymousSurvey` with the defined question.
- `language_survey.store_response('English')` ➕
  - **Method Call**: Stores the response `'English'` in the survey.
- `assert 'English' in language_survey.responses` ✅
  - **Assertion**: Checks if `'English'` is present in the `responses` list.

### 🛠️ Step 2: Run the Test

```bash
pytest test_survey.py
```

**Sample Output**:

```
============================= test session starts =============================
collected 1 item

test_survey.py . [100%]

============================== 1 passed in 0.01s ==============================
```

**Line-by-Line Explanation**:

- `test_survey.py . [100%]` ✅
  - **`.` (Dot)**: Represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Test Passed**: Confirms that the single response was stored correctly. 🎉✅

### 🛠️ Step 3: Add More Tests

Enhance `test_survey.py` by adding more test functions:

```python
# test_survey.py

from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
```

**Line-by-Line Explanation**:

- `def test_store_three_responses():` 🧪
  - **New Test Function**: Defines a test function named `test_store_three_responses`.
- `"""Test that three individual responses are stored properly."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `responses = ['English', 'Spanish', 'Mandarin']` 📝
  - **Responses List**: Defines a list of three responses to be tested.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response in the list.
- `language_survey.store_response(response)` ➕
  - **Method Call**: Stores each response in the survey.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response again to verify.
- `assert response in language_survey.responses` ✅
  - **Assertion**: Checks if each response is present in the `responses` list.

### 🛠️ Step 4: Run All Tests

```bash
pytest test_survey.py
```

**Sample Output**:

```
============================= test session starts =============================
collected 2 items

test_survey.py .. [100%]

============================== 2 passed in 0.01s ==============================
```

**Line-by-Line Explanation**:

- `test_survey.py .. [100%]` ✅✅
  - **Two Dots (`..`)**: Each dot represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Both Tests Passed**: Confirms that both single and multiple responses are stored correctly. 🎉✅✅

Adding more tests ensures comprehensive coverage of different scenarios, increasing the reliability of your code. 📈🛡️

---

## 🔧 Using Fixtures

Fixtures in pytest help **set up a consistent test environment** and **reduce repetitive code**. Let's implement fixtures to streamline our tests. 🛠️🔧

### 🛠️ Step 1: Update Test File with Fixtures

Modify `test_survey.py` to include fixtures:

```python
# test_survey.py

import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
```

**Line-by-Line Explanation**:

- `import pytest` 🐍🔗
  - **Import Statement**: Imports the pytest framework.
- `@pytest.fixture` 🛠️
  - **Fixture Decorator**: Marks the following function as a fixture.
- `def language_survey():` 🧪
  - **Fixture Function**: Defines a fixture named `language_survey`.
- `"""A survey that will be available to all test functions."""` 📄
  - **Docstring**: Describes the purpose of the fixture.
- `return AnonymousSurvey(question)` 🆕
  - **Return Statement**: Returns a new instance of `AnonymousSurvey` with the specified question.
- `def test_store_single_response(language_survey):` 🧪
  - **Test Function**: Defines a test function that uses the `language_survey` fixture.
- `language_survey.store_response('English')` ➕
  - **Method Call**: Stores the response `'English'` in the survey.
- `assert 'English' in language_survey.responses` ✅
  - **Assertion**: Checks if `'English'` is present in the `responses` list.
- `def test_store_three_responses(language_survey):` 🧪
  - **Test Function**: Defines another test function that uses the `language_survey` fixture.
- `responses = ['English', 'Spanish', 'Mandarin']` 📝
  - **Responses List**: Defines a list of three responses to be tested.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response in the list.
- `language_survey.store_response(response)` ➕
  - **Method Call**: Stores each response in the survey.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response again to verify.
- `assert response in language_survey.responses` ✅
  - **Assertion**: Checks if each response is present in the `responses` list.

### 🛠️ Step 2: Run the Tests

```bash
pytest test_survey.py
```

**Sample Output**:

```
============================= test session starts =============================
collected 2 items

test_survey.py .. [100%]

============================== 2 passed in 0.01s ==============================
```

**Line-by-Line Explanation**:

- `test_survey.py .. [100%]` ✅✅
  - **Two Dots (`..`)**: Each dot represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Tests Passed**: Fixtures effectively provide the necessary setup for each test, ensuring consistency and reducing repetitive code. 🎉✅✅

**Benefits of Fixtures**:

- **🔄 DRY Principle**: Avoids repeating setup code in each test.
- **🔧 Maintainability**: Easier to manage and update test setups.
- **📈 Scalability**: Simplifies writing tests for larger projects.

Using fixtures makes your test code cleaner, more organized, and easier to maintain. 🧹🛠️

---


## 🏙️ Real-World Example: Building and Testing a To-Do List Application

Let's delve deeper into a real-world scenario to understand testing better. We'll build a simple **To-Do List Application** and write comprehensive tests for it. This example will illustrate how testing ensures your application behaves as expected under various conditions. 🌟📋

### 🛠️ Step 1: Creating the To-Do List Application

We'll create a `todo.py` module that allows users to add, remove, and view tasks.

```python
# todo.py

class ToDoList:
    """A simple To-Do List application."""

    def __init__(self):
        """Initialize the to-do list with an empty list of tasks."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the to-do list.

        Parameters:
            task (str): The task to be added.
        """
        if task and isinstance(task, str):
            self.tasks.append(task.title())
            return True
        return False

    def remove_task(self, task):
        """
        Remove a task from the to-do list.

        Parameters:
            task (str): The task to be removed.
        """
        try:
            self.tasks.remove(task.title())
            return True
        except ValueError:
            return False

    def view_tasks(self):
        """Return a list of all tasks."""
        return self.tasks.copy()
```

**Line-by-Line Explanation with Emojis**:

- `class ToDoList:` 🏛️
  - **Class Definition**: Defines a class named `ToDoList`.
- `"""A simple To-Do List application."""` 📄
  - **Docstring**: Describes the purpose of the class.
- `def __init__(self):` 🛠️
  - **Initializer**: Defines the constructor method that initializes the to-do list.
- `"""Initialize the to-do list with an empty list of tasks."""` 📄
  - **Docstring**: Describes what the initializer does.
- `self.tasks = []` 📄
  - **Attribute Initialization**: Initializes an empty list to store tasks.
- `def add_task(self, task):` ➕📝
  - **Method Definition**: Defines a method to add a new task.
- `"""Add a new task to the to-do list."""` 📄
  - **Docstring**: Describes the method's purpose.
- `if task and isinstance(task, str):` 🔍✅
  - **Condition Check**: Ensures the task is a non-empty string.
- `self.tasks.append(task.title())` ➕🔠
  - **Append Operation**: Adds the capitalized task to the `tasks` list.
- `return True` 🟢
  - **Return Statement**: Indicates the task was added successfully.
- `return False` 🔴
  - **Return Statement**: Indicates the task was not added (invalid input).
- `def remove_task(self, task):` ➖📝
  - **Method Definition**: Defines a method to remove a task.
- `"""Remove a task from the to-do list."""` 📄
  - **Docstring**: Describes the method's purpose.
- `try:` 🔄
  - **Try Block**: Attempts to remove the task.
- `self.tasks.remove(task.title())` ➖🔠
  - **Remove Operation**: Removes the capitalized task from the `tasks` list.
- `return True` 🟢
  - **Return Statement**: Indicates the task was removed successfully.
- `except ValueError:` ❌
  - **Except Block**: Catches the error if the task doesn't exist.
- `return False` 🔴
  - **Return Statement**: Indicates the task was not found and thus not removed.
- `def view_tasks(self):` 👀📝
  - **Method Definition**: Defines a method to view all tasks.
- `"""Return a list of all tasks."""` 📄
  - **Docstring**: Describes the method's purpose.
- `return self.tasks.copy()` 🔄📄
  - **Return Statement**: Returns a copy of the `tasks` list to prevent external modifications.

### 🛠️ Step 2: Write Tests for the To-Do List Application

Create a test file named `test_todo.py` to verify the functionality of the `ToDoList` class.

```python
# test_todo.py

import pytest  # 🐍🔗
from todo import ToDoList  # 📥🔗

@pytest.fixture
def todo_list():
    """Create a new ToDoList instance for each test."""  # 🛠️🔧
    return ToDoList()  # 🆕📋

def test_add_task_success(todo_list):
    """Test adding a valid task."""  # ✅➕📝
    result = todo_list.add_task('buy groceries')  # ➕🛒
    assert result is True  # 🟢
    assert 'Buy Groceries' in todo_list.view_tasks()  # ✅📋

def test_add_task_invalid(todo_list):
    """Test adding an invalid task (e.g., empty string)."""  # ❌➕📝
    result = todo_list.add_task('')  # ➕❌
    assert result is False  # 🔴
    assert '' not in todo_list.view_tasks()  # ❌📋

def test_remove_existing_task(todo_list):
    """Test removing a task that exists."""  # ✅➖📝
    todo_list.add_task('read book')  # ➕📚
    result = todo_list.remove_task('read book')  # ➖📚
    assert result is True  # 🟢
    assert 'Read Book' not in todo_list.view_tasks()  # ✅❌

def test_remove_nonexistent_task(todo_list):
    """Test removing a task that does not exist."""  # ❌➖📝
    result = todo_list.remove_task('go jogging')  # ➖🏃‍♂️
    assert result is False  # 🔴

def test_view_tasks(todo_list):
    """Test viewing tasks."""  # 👀📋
    tasks = ['walk the dog', 'do laundry', 'write code']  # 📝📋
    for task in tasks:
        todo_list.add_task(task)  # ➕📝
    assert todo_list.view_tasks() == ['Walk The Dog', 'Do Laundry', 'Write Code']  # ✅📋
```

**Line-by-Line Explanation**:

- `import pytest` 🐍🔗
  - **Import Statement**: Imports the pytest framework.
- `from todo import ToDoList` 🔗
  - **Import Statement**: Imports the `ToDoList` class to be tested.
- `@pytest.fixture` 🛠️
  - **Fixture Decorator**: Marks the following function as a fixture.
- `def todo_list():` 🧪
  - **Fixture Function**: Defines a fixture named `todo_list`.
- `"""Create a new ToDoList instance for each test."""` 📄
  - **Docstring**: Describes the purpose of the fixture.
- `return ToDoList()` 🆕
  - **Return Statement**: Returns a new instance of `ToDoList`.
- `def test_add_task_success(todo_list):` 🧪
  - **Test Function**: Defines a test function that uses the `todo_list` fixture.
- `"""Test adding a valid task."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `result = todo_list.add_task('buy groceries')` ➕🛒
  - **Method Call**: Adds the task `'buy groceries'` to the to-do list.
- `assert result is True` 🟢
  - **Assertion**: Checks if the task was added successfully.
- `assert 'Buy Groceries' in todo_list.view_tasks()` ✅📋
  - **Assertion**: Ensures the task appears in the list.
- `def test_add_task_invalid(todo_list):` 🧪
  - **Test Function**: Defines a test function for invalid task input.
- `"""Test adding an invalid task (e.g., empty string)."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `result = todo_list.add_task('')` ➕❌
  - **Method Call**: Attempts to add an empty string as a task.
- `assert result is False` 🔴
  - **Assertion**: Confirms the addition failed.
- `assert '' not in todo_list.view_tasks()` ❌📋
  - **Assertion**: Ensures no empty task is present.
- `def test_remove_existing_task(todo_list):` 🧪
  - **Test Function**: Defines a test function for removing an existing task.
- `"""Test removing a task that exists."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `todo_list.add_task('read book')` ➕📚
  - **Method Call**: Adds the task `'read book'` to the to-do list.
- `result = todo_list.remove_task('read book')` ➖📚
  - **Method Call**: Removes the task `'read book'` from the to-do list.
- `assert result is True` 🟢
  - **Assertion**: Checks if the removal was successful.
- `assert 'Read Book' not in todo_list.view_tasks()` ✅❌
  - **Assertion**: Ensures the task no longer appears in the list.
- `def test_remove_nonexistent_task(todo_list):` 🧪
  - **Test Function**: Defines a test function for removing a non-existent task.
- `"""Test removing a task that does not exist."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `result = todo_list.remove_task('go jogging')` ➖🏃‍♂️
  - **Method Call**: Attempts to remove a task that isn't in the list.
- `assert result is False` 🔴
  - **Assertion**: Confirms the removal failed.
- `def test_view_tasks(todo_list):` 🧪
  - **Test Function**: Defines a test function for viewing tasks.
- `"""Test viewing tasks."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `tasks = ['walk the dog', 'do laundry', 'write code']` 📝📋
  - **Tasks List**: Defines a list of tasks to be added.
- `for task in tasks:` 🔄
  - **Loop**: Iterates over each task in the list.
- `todo_list.add_task(task)` ➕📝
  - **Method Call**: Adds each task to the to-do list.
- `assert todo_list.view_tasks() == ['Walk The Dog', 'Do Laundry', 'Write Code']` ✅📋
  - **Assertion**: Checks if the tasks are correctly stored and formatted.

### 🛠️ Step 3: Run All Tests

```bash
pytest test_survey.py
```

**Sample Output**:

```
============================= test session starts =============================
collected 2 items

test_survey.py .. [100%]

============================== 2 passed in 0.01s ==============================
```

**Line-by-Line Explanation**:

- `test_survey.py .. [100%]` ✅✅
  - **Two Dots (`..`)**: Each dot represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **Both Tests Passed**: Confirms that both single and multiple responses are stored correctly. 🎉✅✅

### 🛠️ Step 4: Understanding the Real-World Example

Let's break down what's happening in our **To-Do List Application** and its tests. 🕵️‍♀️🔍

1. **Application Logic (`todo.py`)**:
   - **Adding Tasks**: The `add_task` method ensures that only non-empty strings are added, capitalizing them for consistency. 📝➕
   - **Removing Tasks**: The `remove_task` method tries to remove a task and handles the case where the task doesn't exist gracefully. ➖📝
   - **Viewing Tasks**: The `view_tasks` method provides a copy of the current tasks to prevent unintended modifications. 👀📋

2. **Testing Logic (`test_todo.py`)**:
   - **Fixture**: `todo_list` fixture provides a fresh instance of `ToDoList` for each test, ensuring tests are isolated and don't interfere with each other. 🛠️🔧
   - **Adding Tasks**:
     - **Success Case**: Verifies that valid tasks are added correctly. ✅➕📝
     - **Invalid Case**: Ensures that invalid tasks (like empty strings) are not added. ❌➕📝
   - **Removing Tasks**:
     - **Existing Task**: Confirms that existing tasks can be removed successfully. ✅➖📝
     - **Non-Existent Task**: Checks that attempting to remove a task that doesn't exist fails gracefully. ❌➖📝
   - **Viewing Tasks**: Validates that the `view_tasks` method returns the correct list of tasks. 👀📋

**Benefits Illustrated**:

- **Comprehensive Coverage**: Tests cover all functionalities, including edge cases. 📚✅
- **Reliability**: Ensures that each part of your application works as intended. 🛡️✅
- **Maintainability**: Makes it easier to update and refactor your code without introducing bugs. 🛠️🔄
- **Scalability**: Facilitates adding new features with confidence that existing functionality remains intact. 📈🔧

---

## 🔧 Using Fixtures (Continued)

Fixtures help in setting up a consistent environment for your tests, making them more reliable and easier to maintain. Let's explore further how fixtures enhance our testing strategy. 🛠️✨

### 🛠️ Step 1: Creating a Fixture

In `test_survey.py`, the `language_survey` fixture provides a standardized setup for all tests that require a survey instance.

```python
@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)
```

**Line-by-Line Explanation**:

- `@pytest.fixture` 🛠️
  - **Fixture Decorator**: Indicates that the following function is a fixture.
- `def language_survey():` 🧪
  - **Fixture Function**: Defines a fixture named `language_survey`.
- `"""A survey that will be available to all test functions."""` 📄
  - **Docstring**: Describes the purpose of the fixture.
- `question = "What language did you first learn to speak?"` 📝
  - **Question Definition**: Sets the survey question.
- `return AnonymousSurvey(question)` 🆕
  - **Return Statement**: Returns a new instance of `AnonymousSurvey` with the specified question.

### 🛠️ Step 2: Using the Fixture in Test Functions

Test functions can now accept `language_survey` as a parameter, utilizing the fixture for setup.

```python
def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
```

**Line-by-Line Explanation**:

- `def test_store_single_response(language_survey):` 🧪
  - **Test Function**: Utilizes the `language_survey` fixture for testing.
- `language_survey.store_response('English')` ➕
  - **Method Call**: Stores the response `'English'` in the survey.
- `assert 'English' in language_survey.responses` ✅
  - **Assertion**: Checks if `'English'` is present in the `responses` list.
- `def test_store_three_responses(language_survey):` 🧪
  - **Test Function**: Utilizes the `language_survey` fixture for testing.
- `responses = ['English', 'Spanish', 'Mandarin']` 📝
  - **Responses List**: Defines a list of three responses to be tested.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response in the list.
- `language_survey.store_response(response)` ➕
  - **Method Call**: Stores each response in the survey.
- `for response in responses:` 🔄
  - **Loop**: Iterates over each response again to verify.
- `assert response in language_survey.responses` ✅
  - **Assertion**: Checks if each response is present in the `responses` list.

### 🛠️ Step 3: Benefits of Using Fixtures

- **🔄 Consistency**: Ensures that each test starts with the same setup.
- **🧹 Clean Code**: Reduces repetition, making tests cleaner and easier to read.
- **🔧 Easy Maintenance**: Changes to the setup only need to be made in the fixture, not in every test function.
- **📈 Scalability**: Facilitates writing additional tests without redundant code.

By leveraging fixtures, your tests become more organized, efficient, and scalable. 🛠️✨📈

---

## 🏙️ Real-World Example: Building and Testing a To-Do List Application (Continued)

To further understand testing in a real-world context, let's extend our **To-Do List Application** by adding new features and corresponding tests. 🛠️🔍

### 🛠️ Step 3: Extending the Application with a New Feature

Let's add a new feature: marking tasks as completed. We'll update our application and tests accordingly. 📝✅

#### 🛠️ Updating `todo.py` with `complete_task` Method

```python
# todo.py

class ToDoList:
    """A simple To-Do List application."""

    def __init__(self):
        """Initialize the to-do list with an empty list of tasks."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the to-do list.

        Parameters:
            task (str): The task to be added.
        """
        if task and isinstance(task, str):
            self.tasks.append({'task': task.title(), 'completed': False})
            return True
        return False

    def remove_task(self, task):
        """
        Remove a task from the to-do list.

        Parameters:
            task (str): The task to be removed.
        """
        for t in self.tasks:
            if t['task'] == task.title():
                self.tasks.remove(t)
                return True
        return False

    def view_tasks(self):
        """Return a list of all tasks."""
        return self.tasks.copy()

    def complete_task(self, task):
        """
        Mark a task as completed.

        Parameters:
            task (str): The task to be marked as completed.
        """
        for t in self.tasks:
            if t['task'] == task.title():
                t['completed'] = True
                return True
        return False
```

**Line-by-Line Explanation with Emojis**:

- `def complete_task(self, task):` ✅📝
  - **Method Definition**: Defines a method to mark a task as completed.
- `"""Mark a task as completed."""` 📄
  - **Docstring**: Describes the method's purpose.
- `for t in self.tasks:` 🔄📄
  - **Loop**: Iterates over each task in the list.
- `if t['task'] == task.title():` 🔍📝
  - **Condition Check**: Checks if the task matches the one to be marked as completed.
- `t['completed'] = True` ✅
  - **Update Operation**: Marks the task as completed.
- `return True` 🟢
  - **Return Statement**: Indicates the task was marked successfully.
- `return False` 🔴
  - **Return Statement**: Indicates the task was not found and thus not marked.

#### 🛠️ Step 4: Updating `test_todo.py` with New Tests

Add new test functions to `test_todo.py` to verify the new `complete_task` method.

```python
# test_todo.py

import pytest
from todo import ToDoList

@pytest.fixture
def todo_list():
    """Create a new ToDoList instance for each test."""
    return ToDoList()

def test_add_task_success(todo_list):
    """Test adding a valid task."""
    result = todo_list.add_task('buy groceries')
    assert result is True
    assert {'task': 'Buy Groceries', 'completed': False} in todo_list.view_tasks()

def test_add_task_invalid(todo_list):
    """Test adding an invalid task (e.g., empty string)."""
    result = todo_list.add_task('')
    assert result is False
    assert '' not in [t['task'] for t in todo_list.view_tasks()]

def test_remove_existing_task(todo_list):
    """Test removing a task that exists."""
    todo_list.add_task('read book')
    result = todo_list.remove_task('read book')
    assert result is True
    assert {'task': 'Read Book', 'completed': False} not in todo_list.view_tasks()

def test_remove_nonexistent_task(todo_list):
    """Test removing a task that does not exist."""
    result = todo_list.remove_task('go jogging')
    assert result is False

def test_view_tasks(todo_list):
    """Test viewing tasks."""
    tasks = ['walk the dog', 'do laundry', 'write code']
    for task in tasks:
        todo_list.add_task(task)
    expected = [
        {'task': 'Walk The Dog', 'completed': False},
        {'task': 'Do Laundry', 'completed': False},
        {'task': 'Write Code', 'completed': False}
    ]
    assert todo_list.view_tasks() == expected

def test_complete_task_success(todo_list):
    """Test marking an existing task as completed."""
    todo_list.add_task('buy groceries')
    result = todo_list.complete_task('buy groceries')
    assert result is True
    assert {'task': 'Buy Groceries', 'completed': True} in todo_list.view_tasks()

def test_complete_task_nonexistent(todo_list):
    """Test marking a non-existent task as completed."""
    result = todo_list.complete_task('go jogging')
    assert result is False
```

**Line-by-Line Explanation**:

- `def test_complete_task_success(todo_list):` 🧪
  - **New Test Function**: Defines a test function for successfully marking a task as completed.
- `"""Test marking an existing task as completed."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `todo_list.add_task('buy groceries')` ➕🛒
  - **Method Call**: Adds the task `'buy groceries'` to the to-do list.
- `result = todo_list.complete_task('buy groceries')` ✅➕🛒
  - **Method Call**: Marks the task `'buy groceries'` as completed.
- `assert result is True` 🟢
  - **Assertion**: Checks if the marking was successful.
- `assert {'task': 'Buy Groceries', 'completed': True} in todo_list.view_tasks()` ✅📋
  - **Assertion**: Ensures the task is marked as completed in the list.
- `def test_complete_task_nonexistent(todo_list):` 🧪
  - **Test Function**: Defines a test function for attempting to mark a non-existent task as completed.
- `"""Test marking a non-existent task as completed."""` 📄
  - **Docstring**: Describes what the test is verifying.
- `result = todo_list.complete_task('go jogging')` ✅🏃‍♂️
  - **Method Call**: Attempts to mark `'go jogging'` as completed.
- `assert result is False` 🔴
  - **Assertion**: Confirms the marking failed since the task doesn't exist.

### 🛠️ Step 5: Run the Extended Tests

```bash
pytest test_todo.py
```

**Sample Output**:

```
============================= test session starts =============================
collected 7 items

test_todo.py ....... [100%]

============================== 7 passed in 0.02s ==============================
```

**Line-by-Line Explanation**:

- `test_todo.py ....... [100%]` ✅✅✅✅✅✅✅
  - **Seven Dots (`.......`)**: Each dot represents a passing test.
  - **`[100%]`**: Indicates that all tests have passed successfully.

**Explanation**:

- **All Tests Passed**: Confirms that all functionalities, including the new `complete_task` method, work as intended. 🎉✅✅✅✅✅✅✅

### 🛠️ Step 6: Analyzing the Real-World Example

**Application Logic Enhancements**:

- **Task Structure**: Each task is now a dictionary containing `task` and `completed` status. 📋✅
- **Adding Tasks**: Validates input and ensures tasks are stored with proper capitalization and completion status. 📝➕✅
- **Removing Tasks**: Searches for the task and removes it if found, handling non-existent tasks gracefully. ➖📝🔍
- **Completing Tasks**: Marks a task as completed if it exists. ✅🔍📝

**Testing Enhancements**:

- **New Tests**:
  - **`test_complete_task_success`**: Verifies that existing tasks can be marked as completed. ✅✅📝
  - **`test_complete_task_nonexistent`**: Ensures that attempting to complete non-existent tasks fails gracefully. ❌✅📝
- **Assertions**:
  - Checks not only the success of operations but also the state of the `tasks` list after operations. 📋✅

**Benefits Illustrated**:

- **Comprehensive Coverage**: Tests cover all functionalities, including edge cases. 📚✅
- **Reliability**: Ensures that each part of your application works as intended. 🛡️✅
- **Maintainability**: Makes it easier to update and refactor your code without introducing bugs. 🛠️🔄
- **Scalability**: Facilitates adding new features with confidence that existing functionality remains intact. 📈🔧

By following this real-world example, you've learned how to build and test a simple application, ensuring its reliability and robustness. 🛠️✨📈

---

## 🏁 Try It Yourself Exercises

Put your knowledge to the test with these exercises! 💪✨

### 📝 11-1. City, Country

**Task**:

1. **Function**: Write a function that accepts two parameters: a city name and a country name.
2. **Return**: The function should return a single string in the format `City, Country`, e.g., `Santiago, Chile`.
3. **Module**: Store the function in a module called `city_functions.py`.
4. **Test File**: Create `test_cities.py` to test the function.
5. **Test Function**: Write `test_city_country()` to verify that calling your function with values like `'santiago'` and `'chile'` returns the correct string.
6. **Run Test**: Ensure `test_city_country()` passes.

**Hints**:

- Use `assert` statements to verify expected outcomes.
- Follow the DRY (Don't Repeat Yourself) principle by using fixtures if applicable.

### 📝 11-2. Population

**Task**:

1. **Modify Function**: Update your city function to require a third parameter, `population`.
2. **Return**: Now return a string like `City, Country – population xxx`, e.g., `Santiago, Chile – population 5000000`.
3. **Run Test**: Run the test to ensure `test_city_country()` fails (since population wasn't handled before).
4. **Make Parameter Optional**: Modify the function so `population` is optional.
5. **Run Test**: Ensure `test_city_country()` passes again.
6. **Additional Test**: Write `test_city_country_population()` to verify the function can handle `city`, `country`, and `population`.
7. **Run All Tests**: Ensure both tests pass.

**Hints**:

- Use default parameters to make `population` optional.
- Ensure your tests cover both cases: with and without `population`.

### 📝 11-3. Employee

**Task**:

1. **Class**: Write a class called `Employee`.
   - **`__init__()`**: Takes `first_name`, `last_name`, and `annual_salary`, storing each as attributes.
   - **Method**: `give_raise()` adds $5,000 to `annual_salary` by default but accepts a different raise amount.
2. **Test File**: Create a test file for `Employee` with two test functions:
   - `test_give_default_raise()`
   - `test_give_custom_raise()`
3. **Initial Tests**: Write tests **without** using a fixture and ensure they pass.
4. **Implement Fixtures**: Refactor tests to use a fixture to avoid creating a new employee instance in each test function.
5. **Run Tests**: Ensure both tests still pass after using the fixture.

**Hints**:

- Use `@pytest.fixture` to create reusable components.
- Utilize `assert` statements to verify expected outcomes.
- Test both default and custom raise scenarios to ensure flexibility.

---

## 🎉 Conclusion

Congratulations, **[Your Name]**! 🎊 You've successfully learned how to **test your Python 3.12 code using pytest**. By implementing tests, you ensure your code remains robust, reliable, and maintainable as your projects grow. Remember:

- **🏁 Start Simple**: Begin with basic tests and gradually add more as needed.
- **🔧 Use Fixtures**: Streamline your tests and adhere to the DRY principle.
- **❌➡️✅ Embrace Failure**: Use failing tests as opportunities to improve your code.
- **🕒🔍 Practice Regularly**: Consistent testing leads to better code quality and fewer bugs.

Keep experimenting, keep testing, and happy coding! 🥳🐍✨

---

## 📚 Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/7.2.x/) 📖🔗
- [Python Official Documentation](https://docs.python.org/3.12/) 🐍📚
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) 💻📘

---

Feel free to reach out if you have any questions or need further assistance. Happy testing! 🚀🔍✨
