# Custom exception class for invalid commands
class InvalidCommand(Exception):
    pass

# Class representing an LED component of the robot
class LED:
    def set_brightness(self, ident, intensity):
        print(f"Setting LED {ident} brightness to {intensity}")

    def set_color(self, ident, red, green, blue):
        print(f"Setting LED {ident} color to ({red}, {green}, {blue})")

# Class representing the robot itself
class Robot:
    def __init__(self):
        # Initialize the robot with 10 LED objects
        self.leds = [LED() for _ in range(10)]

    def beep(self, times, frequency):
        print(f"Beeping {times} times at {frequency}Hz")

    def rotate_neck(self, angle):
        print(f"Rotating neck to {angle} degrees")

    def handle_command(self, message):
        # Pattern matching for handling different commands
        match message:
            case ['BEEPER', frequency, times]:
                # Handle 'BEEPER' command: beep specified times at given frequency
                self.beep(times, frequency)
            case ['NECK', angle]:
                # Handle 'NECK' command: rotate neck to specified angle
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                # Handle 'LED' command: set brightness of specified LED
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                # Handle 'LED' command: set color of specified LED
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                # Handle unknown commands: raise InvalidCommand exception
                raise InvalidCommand(message)

# Example usage of the Robot class
robot = Robot()
robot.handle_command(['BEEPER', 440, 3])      # Output: Beeping 3 times at 440Hz
robot.handle_command(['NECK', 90])            # Output: Rotating neck to 90 degrees
robot.handle_command(['LED', 1, 5])           # Output: Setting LED 1 brightness to 5
robot.handle_command(['LED', 1, 255, 0, 0])   # Output: Setting LED 1 color to (255, 0, 0)
robot.handle_command(['UNKNOWN', 'COMMAND'])  # Raises InvalidCommand exception

# List of cities with their coordinates
cities = [
    ['Sydney', 'AU', 5.312, (-33.8688, 151.2093)],
    ['Lima', 'PE', 9.752, (-12.0464, -77.0428)],
    ['Cape Town', 'ZA', 4.618, (-33.9249, 18.4241)],
    ['Rio de Janeiro', 'BR', 6.748, (-22.9068, -43.1729)],
    ['Jakarta', 'ID', 10.562, (-6.2088, 106.8456)],
]

def main():
    # Print table headers
    print(f'{"City":15} | {"latitude":>9} | {"longitude":>9}')
    for record in cities:
        # Pattern matching to process cities in the Southern Hemisphere
        match record:
            case [name, _, _, (lat, lon)] if lat < 0:
                # Print city name and coordinates
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

# Execute the main function
main()
