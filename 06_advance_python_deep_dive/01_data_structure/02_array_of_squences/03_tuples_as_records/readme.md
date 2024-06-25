## Tuples Are Not Just Immutable Lists
Tuples in Python are often introduced as immutable lists, but this description does not fully capture their utility and functionality. Beyond being immutable, tuples serve dual purposes: they can function as immutable lists and as records without named fields.

## Tuples as Records

When tuples are used as records, each element within the tuple is associated with a specific field, and the position of the element within the tuple defines its meaning. This positional significance makes the structure and order of items in tuples crucial when they are used as records. This differs from their use as simple lists where the immutability and perhaps the order of items are the only considerations.

### Example 1: Employee Record
Suppose we have a tuple that represents an employee:

```python
employee = ('John Doe', 'Software Developer', 50000)
```

In this tuple:
- The first element, `'John Doe'`, represents the employee's name.
- The second element, `'Software Developer'`, represents the employee's job title.
- The third element, `50000`, represents the employee's annual salary.

Here, the order is crucial because if you switch the position of the name and the salary, it would not make sense:

```python
# Incorrect interpretation if order is changed
employee_misordered = (50000, 'Software Developer', 'John Doe')
# This would suggest that '50000' is the name, which is incorrect.
```
Tuples are used as records:

1. **Geographic Coordinates:**
   ```python
   lax_coordinates = (33.9425, -118.408056)  # Latitude and longitude of LAX airport.
   ```
Latitude and longitude of the Los Angeles International Airport
2. **City Data:**
   ```python
   city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)  # Data about Tokyo.
   ```
Data about Tokyo: name, year, population (thousands), population change (%),
and area (km²).

3. **Traveler IDs:**
   ```python
   traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
   for passport in sorted(traveler_ids):
       print('%s/%s' % passport)
   ```
A list of tuples of the form (country_code, passport_number)
As we iterate over the list, passport is bound to each tuple.
The % formatting operator understands tuples and treats each item as a separate
field.

   Output:
   ```
   BRA/CE342567
   ESP/XDA205856
   USA/31195855
   ```

   Here, tuples store and transmit data about each traveler's country code and passport number efficiently.
4.  **Country**
```python
for country, _ in traveler_ids:
    print(country)
```
The for loop knows how to retrieve the items of a tuple separately—this is called
“unpacking.” Here we are not interested in the second item, so we assign it to _, a
dummy variable.