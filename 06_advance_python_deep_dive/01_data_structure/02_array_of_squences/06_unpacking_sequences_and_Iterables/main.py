coordinates = [33.9425, -118.408056]
latitude = coordinates[0]
longitude = coordinates[1]
print(latitude, longitude)  # Output: 33.9425 -118.408056


coordinates = [33.9425, -118.408056]
latitude, longitude = coordinates
print(latitude, longitude)  # Output: 33.9425 -118.408056

# Example of a generator
def countdown(num):
    while num > 0:
        yield num
        num -= 1

# Create a generator
gen = countdown(3)

# Unpacking the generator
first, second, third = gen
print(first, second, third)  # Output: 3 2 1



def record_scores(first, second, third, *others):
    print(f"First place: {first}")
    print(f"Second place: {second}")
    print(f"Third place: {third}")
    if others:
        print(f"Other scores: {others}")

# Calling the function with a list of scores
all_scores = [90, 85, 82, 80, 79, 75]
record_scores(*all_scores)


print('Divmod')
result = divmod(20, 8)
print(result)  # Output: (2, 4)
print('Unpacking')
t = (20, 8)
result = divmod(*t)
print(result)  # Output: (2, 4)

qoutient, remainder = divmod(*t)
quotient, remainder = divmod(*t)
print("Quotient:", quotient)   # Output: Quotient: 2
print("Remainder:", remainder) # Output: Remainder: 4


print('Path Unpack')
import os
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)


# Assigning first two items and capturing the rest
a, b, *rest = range(5)
print(a, b, rest)  # Output: 0 1 [2, 3, 4]

# Another example with fewer excess items
a, b, *rest = range(3)
print(a, b, rest)  # Output: 0 1 [2]

# Example with no excess items
a, b, *rest = range(2)
print(a, b, rest)  # Output: 0 1 []


# Capturing the middle section of the range
a, *body, c, d = range(5)
print(a, body, c, d)  # Output: 0 [1, 2] 3 4

# Capturing the beginning of the range
*head, b, c, d = range(5)
print(head, b, c, d)  # Output: [0, 1] 2 3 4


def print_scores(*args):
    for score in args:
        print(score)

print_scores(95, 85, 75, 65)  # Output: 95 85 75 65


print('Metro Areas')
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"City":15} | {"Latitude":>9} | {"Longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()

