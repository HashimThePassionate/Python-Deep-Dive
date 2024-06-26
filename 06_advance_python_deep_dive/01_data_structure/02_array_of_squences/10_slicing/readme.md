# Python Slicing

## Overview

Slicing is a powerful feature available in Python for lists, tuples, strings, and all sequence types. It allows you to access a subset of elements within a sequence using a simple and flexible syntax.

## Why Slices and Ranges Exclude the Last Item

In Python, slices and ranges exclude the last item by convention. This approach aligns well with Python's zero-based indexing system and offers several benefits:

1. **Easy Length Calculation**:
   - If you want to know how many items are in a slice, you can simply look at the stop position. For example, `range(3)` generates three items: `[0, 1, 2]`. Similarly, `my_list[:3]` gives you the first three items of `my_list`.

2. **Simple Length Computation**:
   - If you have both a start and stop position, calculating the number of items in the slice is straightforward: it’s just the difference between the stop and start positions. For instance, in `my_list[1:4]`, the number of items is `4 - 1 = 3`.

3. **Non-overlapping Splits**:
   - You can split a sequence into two parts at any index without any overlap. For example, if you split a list at index 2:
     ```python
     l = [10, 20, 30, 40, 50, 60]
     print(l[:2])  # This gives [10, 20]
     print(l[2:])  # This gives [30, 40, 50, 60]
     ```

## Slice Objects

Slices can also specify a step or stride, allowing you to skip elements or even reverse the order:

### Basic Slicing
- `s[a:b:c]` specifies a slice from index `a` to `b` with a step of `c`.
- Example:
  ```python
  s = 'bicycle'
  print(s[::3])   # 'bye'
  print(s[::-1])  # 'elcycib'
  print(s[::-2])  # 'eccb'
  ```

### Explanation of the Examples
1. **s[::3]**:
   - This means "start at the beginning of the string and take every third character."
   - For `'bicycle'`, it takes `'b'`, skips `'i'`, takes `'c'`, skips `'y'`, and takes `'c'`, resulting in `'bye'`.

2. **s[::-1]**:
   - This means "start at the end of the string and move backwards by one character each time."
   - For `'bicycle'`, it reverses the string to `'elcycib'`.

3. **s[::-2]**:
   - This means "start at the end of the string and move backwards by two characters each time."
   - For `'bicycle'`, it takes `'e'`, skips `'l'`, takes `'c'`, skips `'y'`, and takes `'b'`, resulting in `'eccb'`.

### Slice Object Creation
- The notation `a:b:c` is valid within `[]` and produces a slice object (`slice(a, b, c)`).
- Python uses this to evaluate slices by calling `seq.__getitem__(slice(start, stop, step))`.

### Named Slices
- Naming slices can make your code more readable, especially when working with structured data. For example:
  ```python
  invoice = """
  0.....6.................................40........52...55........
  1909   Pimoroni PiBrella                $17.50    3   $52.50
  1489   6mm Tactile Switch x20           $4.95     2   $9.90
  1510   Panavise Jr. - PV-201            $28.00    1   $28.00
  1601   PiTFT Mini Kit 320x240           $34.95    1   $34.95
  """

  # Define slices
  SKU = slice(0, 6)
  DESCRIPTION = slice(6, 40)
  UNIT_PRICE = slice(40, 52)
  QUANTITY = slice(52, 55)
  ITEM_TOTAL = slice(55, None)

  # Split the invoice into lines and skip the first line (headers)
  line_items = invoice.split('\n')[2:]

  # Print the unit price and description for each item
  for item in line_items:
      print(item[UNIT_PRICE], item[DESCRIPTION])
  ```

### Explanation of the Invoice Example
1. **Invoice String**:
   - A multi-line string `invoice` contains item details.

2. **Slice Definitions**:
   - Slices are defined for different parts of each line: SKU, Description, Unit Price, Quantity, and Item Total.

3. **Split Lines**:
   - The invoice string is split into lines and the first line (headers) is skipped.

4. **Loop and Print**:
   - For each item in `line_items`, the unit price and description are printed using the defined slices.

## Additional Features

- **Multidimensional Slices**:
  - Slicing can be used with multidimensional arrays and matrices.

- **Ellipsis Notation**:
  - The ellipsis (`...`) can be used in slicing to indicate "everything else".

By understanding and utilizing these slicing techniques, you can write more efficient and readable Python code.

## Example Output

```plaintext
 $17.50   Pimoroni PiBrella                
 $4.95    6mm Tactile Switch x20           
 $28.00   Panavise Jr. - PV-201            
 $34.95   PiTFT Mini Kit 320x240           
```
