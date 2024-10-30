# 📝 Understanding `NewType` in Python

Welcome to this comprehensive guide on using `NewType` in Python! 🚀 In this README, we'll explore how to create distinct, specific types to prevent subtle bugs, enforce better type constraints, and make your code robust and maintainable. Let’s dive deep! 🎉

## 📚 Table of Contents

- [📝 Understanding `NewType` in Python](#-understanding-newtype-in-python)
  - [📚 Table of Contents](#-table-of-contents)
  - [📖 Introduction to `NewType`](#-introduction-to-newtype)
    - [How `NewType` Works](#how-newtype-works)
    - [Explanation](#explanation)
  - [📄 Use Case: Document Publishing System](#-use-case-document-publishing-system)
    - [🤔 Problem Statement](#-problem-statement)
    - [🚧 Problem Example](#-problem-example)
    - [🛠️ Implementing `NewType`](#️-implementing-newtype)
    - [Enforcing Type Constraints](#enforcing-type-constraints)
    - [Complete Example Workflow with Detailed Steps](#complete-example-workflow-with-detailed-steps)
    - [What Happens if We Use `mypy`?](#what-happens-if-we-use-mypy)
  - [🌍 Real-World Scenarios](#-real-world-scenarios)
  - [🔄 Difference Between `NewType` and Type Aliases](#-difference-between-newtype-and-type-aliases)
  - [🎯 Conclusion](#-conclusion)

## 📖 Introduction to `NewType`

Python’s `NewType` allows you to create a **new type based on an existing one**, but with a crucial difference: it introduces type constraints, where the new type is distinct from the base type in terms of type checking. This means that `NewType` allows Python’s type-checking tools (like `mypy`) to differentiate logically distinct data that might otherwise use the same data type.

### How `NewType` Works

Let's see how `NewType` works with an example where we want a distinct type to represent a `UserId`:

```python
from typing import NewType

# Create a new type `UserId`, which is distinct from an integer (`int`)
UserId = NewType('UserId', int)

# Function that expects a `UserId`
def get_user_data(user_id: UserId) -> str:
    return f"User data for user with ID {user_id}"

# Correct way to use `UserId`
user_id = UserId(1001)
print(get_user_data(user_id))  # Output: User data for user with ID 1001

# Incorrect usage: plain `int` passed instead of `UserId`
normal_int = 1001
# The line below will raise a type error if checked by `mypy`:
# print(get_user_data(normal_int))  # Error with mypy: Argument of type "int" cannot be assigned to parameter of type "UserId"
```

### Explanation

In this example:
- `UserId` is defined as a distinct type based on `int`, meaning that although it acts like an integer in usage, type checkers like `mypy` consider it a separate type.
- When `get_user_data` expects a `UserId`, passing a plain `int` will raise an error if checked with `mypy`, ensuring that `UserId` and `int` aren’t accidentally mixed.
  
**Why This Matters:** Using `NewType` makes it clear where specific types like `UserId` are expected, reducing accidental misuses and clarifying code intent. This ensures that the types of values you work with are precise, reducing bugs.

## 📄 Use Case: Document Publishing System

To understand `NewType` in action, let’s consider a **Document Publishing System** where documents need to be explicitly marked as **drafts** or **ready for publishing**. This will help prevent errors like publishing unreviewed documents.

### 🤔 Problem Statement

In a publishing system, there are two key states for documents:

1. **Draft Document**: A document that is still being edited and not yet approved for publishing.
2. **Ready-to-Publish Document**: A document that has been reviewed and is ready to be published.

The publishing function should only accept documents that are marked as **ready to publish**. Without `NewType`, it’s easy to accidentally pass an unreviewed document to the publishing function.

**Initial Code Without `NewType` Constraints:**

```python
class Document:
    def __init__(self, content: str):
        self.content = content
        self.reviewed = False

    def mark_reviewed(self):
        self.reviewed = True

    def is_reviewed(self) -> bool:
        return self.reviewed

def publish_document(doc: Document):
    # This function should only accept documents that are reviewed and ready to publish
    print(f"Publishing document: {doc.content}")
```

Here:
- `Document` has properties like `content` and a `reviewed` status.
- `publish_document` should ideally only accept reviewed documents, but nothing prevents an unreviewed document from being passed by mistake.

### 🚧 Problem Example

Without any restrictions, someone could accidentally pass an unreviewed document:

```python
draft_doc = Document("Draft content here")
publish_document(draft_doc)  # This could publish an unreviewed draft!
```

This setup can lead to serious issues if unreviewed documents get published. Let’s fix this using `NewType`.

### 🛠️ Implementing `NewType`

We can solve this by creating a `NewType` called `ReadyToPublishDocument`, ensuring only documents ready for publishing are passed to `publish_document`.

```python
from typing import NewType

# Create a new type `ReadyToPublishDocument` based on `Document`
ReadyToPublishDocument = NewType('ReadyToPublishDocument', Document)
```

By using `ReadyToPublishDocument`:
1. We can now specify that only ready-to-publish documents should be used in `publish_document`.
2. This restricts the type of documents passed to `publish_document` to those explicitly marked as ready.

Let’s update the code to reflect this constraint:

```python
def publish_document(doc: ReadyToPublishDocument):
    # Only accepts ReadyToPublishDocument instances
    print(f"Publishing document: {doc.content}")
```

Now, if we try to pass a general `Document` instead of `ReadyToPublishDocument`, `mypy` will catch the error.

### Enforcing Type Constraints

To make sure a `Document` is reviewed before being published, we can create a function `prepare_for_publishing` that checks the review status and converts it to `ReadyToPublishDocument`.

```python
def prepare_for_publishing(doc: Document) -> ReadyToPublishDocument:
    # Ensure the document is reviewed
    assert doc.is_reviewed(), "Document must be reviewed before publishing"
    return ReadyToPublishDocument(doc)
```

With this setup:
- Only documents that have been reviewed can be converted into `ReadyToPublishDocument`.
- This acts as a “safety gate” to ensure no draft documents accidentally make it to the publishing function.

### Complete Example Workflow with Detailed Steps

Here’s the final workflow with complete safety checks:

```python
if __name__ == "__main__":
    # Step 1: Create a new draft document
    draft_doc = Document("Draft content for review")
    print("Draft Document:", draft_doc.content)  # Initial content without review

    # Step 2: Mark the document as reviewed
    draft_doc.mark_reviewed()

    # Step 3: Convert to ready-to-publish document
    ready_doc = prepare_for_publishing(draft_doc)
    print("Ready Document:", ready_doc.content)  # Reviewed and ready for publishing

    # Step 4: Publish the document
    publish_document(ready_doc)  # Output: Publishing document: Draft content for review
```

### What Happens if We Use `mypy`?

With `mypy`, if we try to bypass `prepare_for_publishing` by passing a regular `Document` to `publish_document`, `mypy` will raise an error:

```plaintext
error: Argument 1 to "publish_document" has incompatible type "Document"; expected "ReadyToPublishDocument"
```

This error shows that `publish_document` only accepts `ReadyToPublishDocument`, enforcing the constraint that only reviewed documents should be published.

**Why This Matters:** This strict type-checking ensures that developers cannot accidentally publish drafts, promoting safe and reliable code.

## 🌍 Real-World Scenarios

Here are practical scenarios where `NewType` shines by enforcing clear boundaries between similar types:

1. **Security:** Distinguish between a regular `str` and a `SanitizedString` to prevent SQL injection or XSS attacks. This restricts functions to only operate on safe, sanitized input.
  
2. **Authentication:** Differentiate between `User` and `AuthenticatedUser` types, allowing only authenticated users to access certain functions, improving security.
   
3. **Validation:** Use a type like `ValidatedUserId` based on `int` to prevent accidental processing of invalid IDs, enforcing strict user validation throughout the code.

## 🔄 Difference Between `NewType` and Type Aliases

Understanding the difference between `NewType` and type aliases is crucial for using `NewType` effectively:

1. **Type Alias:** Provides an alternate name for a type but is **fully interchangeable** with the original type.
   ```python
   from typing import Union
   IdOrName = Union[str, int]
   ```

   In this case, `IdOrName` is treated the same as `Union[str, int]`.

2. **NewType:** Defines a **distinct type** that is not interchangeable with the base type. This strictness makes it useful for enforcing type boundaries.

   ```python
   UserId = NewType('UserId', int)
   ```



   Here, `UserId` is treated differently from `int`, adding a layer of safety against accidentally using raw integers where `UserId` is required.

**Use Case of Type Aliases:** Type aliases simplify complex nested types like `Union[Dict[int, User], List[Dict[str, User]]]`, whereas `NewType` is ideal for enforcing strict type requirements and preventing logical errors.

## 🎯 Conclusion

Using `NewType` in Python 3.12 enables more precise type constraints, allowing developers to prevent logical errors, enforce data integrity, and build more reliable code. This type-based approach makes Python type hints more robust, catching subtle bugs early and improving code quality overall.
