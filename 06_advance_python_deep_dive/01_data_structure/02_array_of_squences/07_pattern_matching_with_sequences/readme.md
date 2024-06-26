# Pattern Matching with Sequences

The most visible new feature in Python 3.10 is pattern matching with the `match/case` statement proposed in PEP 634—Structural Pattern Matching: Specification.

## Example: Handling Sequences with `match/case`

Imagine you are designing a robot that accepts commands as sequences of words and numbers, like `BEEPER 440 3`. After parsing, you get a message like `['BEEPER', 440, 3]`. You can handle such messages using the following method:

**Code**
```python  
class InvalidCommand(Exception):
    pass
class LED:
    def set_brightness(self, ident, intensity):
        print(f"Setting LED {ident} brightness to {intensity}")

    def set_color(self, ident, red, green, blue):
        print(f"Setting LED {ident} color to ({red}, {green}, {blue})")

class Robot:
    def __init__(self):
        self.leds = [LED() for _ in range(10)]

    def beep(self, times, frequency):
        print(f"Beeping {times} times at {frequency}Hz")

    def rotate_neck(self, angle):
        print(f"Rotating neck to {angle} degrees")

    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)

robot = Robot()
robot.handle_command(['BEEPER', 440, 3])      # Output: Beeping 3 times at 440Hz
robot.handle_command(['NECK', 90])            # Output: Rotating neck to 90 degrees
robot.handle_command(['LED', 1, 5])           # Output: Setting LED 1 brightness to 5
robot.handle_command(['LED', 1, 255, 0, 0])   # Output: Setting LED 1 color to (255, 0, 0)
robot.handle_command(['UNKNOWN', 'COMMAND'])
```
**Output**
```bash
Beeping 3 times at 440Hz
Rotating neck to 90 degrees
Setting LED 1 brightness to 5
Setting LED 1 color to (255, 0, 0)
    raise InvalidCommand(message)
InvalidCommand: ['UNKNOWN', 'COMMAND']
```

### Robot Class Example

#### Class `InvalidCommand`

This class is a custom exception class. It inherits from Python's built-in `Exception` class. When an invalid command is given to the robot, an instance of this exception is raised.

```python
class InvalidCommand(Exception):
    pass
```

- **Purpose**: To handle and signal invalid commands.
- **Usage**: When a command does not match any of the defined patterns in the `handle_command` method of the `Robot` class, this exception is raised.

#### Class `LED`

This class represents an LED component of the robot. It has two methods: `set_brightness` and `set_color`.

```python
class LED:
    def set_brightness(self, ident, intensity):
        print(f"Setting LED {ident} brightness to {intensity}")

    def set_color(self, ident, red, green, blue):
        print(f"Setting LED {ident} color to ({red}, {green}, {blue})")
```

- **Methods**:
  - `set_brightness(self, ident, intensity)`: Sets the brightness of the specified LED.
  - `set_color(self, ident, red, green, blue)`: Sets the color of the specified LED.
- **Purpose**: To control the brightness and color of LEDs on the robot.

#### Class `Robot`

This class represents the robot itself. It has several methods to handle different commands, including beeping, rotating the neck, and controlling LEDs.

```python
class Robot:
    def __init__(self):
        self.leds = [LED() for _ in range(10)]

    def beep(self, times, frequency):
        print(f"Beeping {times} times at {frequency}Hz")

    def rotate_neck(self, angle):
        print(f"Rotating neck to {angle} degrees")

    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)
```

- **Attributes**:
  - `leds`: A list of 10 `LED` objects.
- **Methods**:
  - `__init__(self)`: Initializes the robot with 10 LED objects.
  - `beep(self, times, frequency)`: Makes the robot beep a specified number of times at a given frequency.
  - `rotate_neck(self, angle)`: Rotates the robot's neck to a specified angle.
  - `handle_command(self, message)`: Handles different types of commands using the `match/case` statement.
    - **Patterns**:
      - `['BEEPER', frequency, times]`: Calls `beep` with the given frequency and times.
      - `['NECK', angle]`: Calls `rotate_neck` with the given angle.
      - `['LED', ident, intensity]`: Calls `set_brightness` on the specified LED with the given intensity.
      - `['LED', ident, red, green, blue]`: Calls `set_color` on the specified LED with the given color values.
      - `_`: Raises an `InvalidCommand` exception for any unmatched commands.

### Example Usage

Here's how you can use the `Robot` class to handle various commands:

```python
robot = Robot()
robot.handle_command(['BEEPER', 440, 3])      # Output: Beeping 3 times at 440Hz
robot.handle_command(['NECK', 90])            # Output: Rotating neck to 90 degrees
robot.handle_command(['LED', 1, 5])           # Output: Setting LED 1 brightness to 5
robot.handle_command(['LED', 1, 255, 0, 0])   # Output: Setting LED 1 color to (255, 0, 0)
robot.handle_command(['UNKNOWN', 'COMMAND'])  # Raises InvalidCommand exception
```

### Output
Running the example usage will produce:
```bash
Beeping 3 times at 440Hz
Rotating neck to 90 degrees
Setting LED 1 brightness to 5
Setting LED 1 color to (255, 0, 0)
Traceback (most recent call last):
  ...
InvalidCommand: ['UNKNOWN', 'COMMAND']
```

## Destructuring in Pattern Matching

One key improvement of `match` over `switch` is destructuring, a more advanced form of unpacking.


## Destructuring 
Destructuring in Python refers to the process of unpacking elements from data structures, such as lists, tuples, and dictionaries, into individual variables. This allows you to extract values from these structures directly into variables in a clean and readable manner.

In the context of Python, destructuring is often used with pattern matching (introduced in Python 3.10) and can also be seen in tuple unpacking. It is a powerful feature that simplifies the extraction of data from complex structures.

### Example: Destructuring Nested Lists

Let's consider a list of cities with their coordinates. We will print cities located in the Southern Hemisphere (latitude < 0).

```python
cities = [
    ['Sydney', 'AU', 5.312, (-33.8688, 151.2093)],
    ['Lima', 'PE', 9.752, (-12.0464, -77.0428)],
    ['Cape Town', 'ZA', 4.618, (-33.9249, 18.4241)],
    ['Rio de Janeiro', 'BR', 6.748, (-22.9068, -43.1729)],
    ['Jakarta', 'ID', 10.562, (-6.2088, 106.8456)],
]

def main():
    print(f'{"City":15} | {"latitude":>9} | {"longitude":>9}')
    for record in cities:
        match record:
            case [name, _, _, (lat, lon)] if lat < 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

main()
```

### Explanation:
- The subject of this `match` is `record`, each list in `cities`.
- The `case` clause contains a pattern and an optional guard (`if` clause).
- Example pattern: `[name, _, _, (lat, lon)]` matches a list with four items, where the last item is a two-item list.

### Output
Running the example will produce:
```bash
City            |  latitude | longitude
Sydney          |  -33.8688 |  151.2093
Lima            |  -12.0464 |  -77.0428
Cape Town       |  -33.9249 |   18.4241
Rio de Janeiro  |  -22.9068 |  -43.1729
Jakarta         |   -6.2088 |  106.8456
```

## Special Considerations

- Sequence patterns can be written as lists or tuples, and they can match instances of most subclasses of `collections.abc.Sequence`, except `str`, `bytes`, and `bytearray`.
- The `_` symbol is special in patterns; it matches any single item and is never bound to the value.
    1.  In the context of pattern matching in Python, the _ symbol has a special meaning. It acts as a wildcard that matches any single item in the given pattern but does not bind the matched value to a variable. This means you can use _ to indicate that you expect a value in that position, but you are not interested in using that value later in your code.
- The `as` keyword can bind parts of a pattern to variables.

### Example: Matching with Type Information

```python
case [str(name), _, _, (float(lat), float(lon))]:
```

- Matches a sequence where the first item is a `str`, and the last item is a pair of `float`.

### Example: Matching with Guard Clause

```python
match record:
    case [name, _, _, (lat, lon)] if lon <= 0:
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
```

- The nested block with the `print` statement runs only if the pattern matches and the guard expression is truthy.

