try:
    x = int(input("Enter a number: "))
    y = 10 / x
    my_list = [1, 2, 3]
    print(my_list[x])
    
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    print(f"Exception details: {e}")
    
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")
    print(f"Exception details: {e}")
    
except IndexError as e:
    print("Error: List index out of range.")
    print(f"Exception details: {e}")