# Exceptions Hierarchy

```plaintext
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    │   ├── NotImplementedError
    │   ├── RecursionError
    │   └── StopIteration
    ├── StopAsyncIteration
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    └── Warning
        ├── DeprecationWarning
        ├── PendingDeprecationWarning
        ├── RuntimeWarning
        ├── SyntaxWarning
        ├── UserWarning
        ├── FutureWarning
        ├── ImportWarning
        ├── UnicodeWarning
        └── BytesWarning
```
Sure! Here's an explanation of the hierarchy of exceptions in Python, detailing the primary exceptions and their subclasses:

### BaseException
- **BaseException**: The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes. It serves as the root of the exception hierarchy.

### SystemExit
- **SystemExit**: Raised by the `sys.exit()` function. It indicates an exit from the interpreter, and is not considered an error. It can be caught in rare cases, but typically should be allowed to propagate and terminate the program.

### KeyboardInterrupt
- **KeyboardInterrupt**: Raised when the user interrupts program execution, usually by pressing Ctrl+C. This exception can be caught to perform cleanup operations before the program exits.

### GeneratorExit
- **GeneratorExit**: Raised when a generator or coroutine is closed (via the `close()` method). It is typically used to clean up resources.

### Exception
- **Exception**: The base class for all non-exiting exceptions. User-defined exceptions should inherit from this class.

#### ArithmeticError
- **ArithmeticError**: The base class for errors that occur for numeric calculations.
  - **FloatingPointError**: Raised when a floating point operation fails.
  - **OverflowError**: Raised when a calculation exceeds the maximum limit for a numeric type.
  - **ZeroDivisionError**: Raised when division or modulo by zero takes place.

#### AssertionError
- **AssertionError**: Raised when an `assert` statement fails.

#### AttributeError
- **AttributeError**: Raised when an attribute reference or assignment fails.

#### BufferError
- **BufferError**: Raised when a buffer-related operation cannot be performed.

#### EOFError
- **EOFError**: Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.

#### ImportError
- **ImportError**: Raised when an import statement fails to find the module definition or when a `from ... import ...` statement fails to find a name that is to be imported.
  - **ModuleNotFoundError**: Raised when a module could not be located.

#### LookupError
- **LookupError**: The base class for errors raised when a lookup on a collection fails.
  - **IndexError**: Raised when a sequence subscript is out of range.
  - **KeyError**: Raised when a dictionary key is not found.

#### MemoryError
- **MemoryError**: Raised when an operation runs out of memory but the situation may still be handled gracefully.

#### NameError
- **NameError**: Raised when a local or global name is not found.
  - **UnboundLocalError**: Raised when a local variable is referenced before it has been assigned a value.

#### OSError
- **OSError**: The base class for operating system-related errors.
  - **BlockingIOError**: Raised when an operation would block on an object (e.g., socket) set for non-blocking operation.
  - **ChildProcessError**: Raised when an operation on a child process fails.
  - **ConnectionError**: A base class for connection-related issues.
    - **BrokenPipeError**: Raised when a pipe is broken.
    - **ConnectionAbortedError**: Raised when a connection attempt is aborted.
    - **ConnectionRefusedError**: Raised when a connection attempt is refused.
    - **ConnectionResetError**: Raised when a connection is reset by the peer.
  - **FileExistsError**: Raised when trying to create a file or directory that already exists.
  - **FileNotFoundError**: Raised when a file or directory is requested but doesn’t exist.
  - **InterruptedError**: Raised when a system call is interrupted.
  - **IsADirectoryError**: Raised when a file operation is requested on a directory.
  - **NotADirectoryError**: Raised when a directory operation is requested on something that is not a directory.
  - **PermissionError**: Raised when trying to run an operation without the adequate access rights.
  - **ProcessLookupError**: Raised when a given process doesn’t exist.
  - **TimeoutError**: Raised when a system function timed out at the system level.

#### ReferenceError
- **ReferenceError**: Raised when a weak reference proxy is used to access a garbage-collected referent.

#### RuntimeError
- **RuntimeError**: Raised when an error is detected that doesn’t fall in any of the other categories.
  - **NotImplementedError**: Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
  - **RecursionError**: Raised when the maximum recursion depth is exceeded.

#### StopIteration
- **StopIteration**: Raised by the `next()` function to indicate that there are no further items produced by the iterator.

#### StopAsyncIteration
- **StopAsyncIteration**: Raised by the `__anext__()` method of an asynchronous iterator to indicate that there are no further items produced by the iterator.

#### SyntaxError
- **SyntaxError**: Raised when the parser encounters a syntax error.
  - **IndentationError**: Raised when there is incorrect indentation.
    - **TabError**: Raised when indentation consists of inconsistent tabs and spaces.

#### SystemError
- **SystemError**: Raised when the interpreter detects internal error conditions, but the situation does not look fatal.

#### TypeError
- **TypeError**: Raised when an operation or function is applied to an object of inappropriate type.

#### ValueError
- **ValueError**: Raised when an operation or function receives an argument with the right type but inappropriate value.
  - **UnicodeError**: The base class for Unicode-related errors.
    - **UnicodeDecodeError**: Raised when a Unicode-related error occurs during decoding.
    - **UnicodeEncodeError**: Raised when a Unicode-related error occurs during encoding.
    - **UnicodeTranslateError**: Raised when a Unicode-related error occurs during translation.

#### Warning
- **Warning**: The base class for all warning categories.
  - **DeprecationWarning**: Raised for features that are deprecated and will be removed in future versions.
  - **PendingDeprecationWarning**: Raised for features that are deprecated and might be removed in the future.
  - **RuntimeWarning**: Raised for events that occur during runtime which are not considered errors.
  - **SyntaxWarning**: Raised for dubious syntactic features.
  - **UserWarning**: Raised when a user-generated warning is needed.
  - **FutureWarning**: Raised for features that will change in the future.
  - **ImportWarning**: Raised when there are issues with the import statement.
  - **UnicodeWarning**: Raised for Unicode-related warnings.
  - **BytesWarning**: Raised for issues with bytes and bytearray operations.

This hierarchy helps in structuring exception handling and allows you to catch and handle specific categories of errors effectively.