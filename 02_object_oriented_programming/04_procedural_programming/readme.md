
```python
def create_employee(base_salary, hourly_rate):
    return {
        "base_salary": base_salary,
        "hourly_rate": hourly_rate
    }

def calculate_wage(employee, extra_hours):
    return employee["base_salary"] + (employee["hourly_rate"] * extra_hours)

if __name__ == "__main__":
    employee = create_employee(50000, 20)
    wage = calculate_wage(employee, 20)
    print(wage)
```


### Why Encapsulation in Classes is Preferred over Spaghetti Functional Approach

#### Spaghetti Approach

The "spaghetti" approach refers to organizing code in a procedural or functional style without proper encapsulation. In this approach, data and functions are often spread across different parts of the codebase, leading to tangled and hard-to-follow logic. Here's why this approach is problematic:

1. **Lack of Encapsulation**: In the spaghetti approach, data and functions are not encapsulated within cohesive units. This can lead to global state, making it difficult to reason about the behavior of the system and increasing the risk of unintended side effects.

2. **Code Duplication**: Without encapsulation, related functionality tends to be duplicated across different parts of the codebase. This not only increases the amount of code to maintain but also makes it harder to ensure consistency and correctness.

3. **Limited Reusability**: Functions in a spaghetti codebase are often tightly coupled to specific data structures and contexts. This limits their reusability and makes it challenging to refactor or extend the codebase without introducing bugs.

4. **Debugging Complexity**: Understanding and debugging spaghetti code can be a daunting task due to its lack of structure and organization. Developers may spend significant time tracing the flow of data and logic, increasing the likelihood of introducing errors during maintenance or enhancements.

#### Why Encapsulation in Classes is Preferred

Encapsulation is a fundamental principle of object-oriented programming (OOP) that addresses many of the shortcomings of the spaghetti approach. Here's why encapsulation in classes is preferred:

1. **Modularity**: Classes encapsulate data and behavior into cohesive units, promoting modularity and reducing complexity. This makes it easier to understand, maintain, and extend the codebase.

2. **Information Hiding**: Encapsulation allows for information hiding, where the internal implementation details of a class are hidden from external users. This protects the integrity of the data and provides a clear interface for interacting with objects.

3. **Code Reusability**: OOP encourages reuse through inheritance and composition. By encapsulating functionality within classes, code becomes more reusable, as classes can be subclassed or composed to create new behaviors without modifying existing code.

4. **Encapsulation of State**: Classes encapsulate both data and behavior, allowing for better management of state. This reduces the risk of unexpected side effects and makes it easier to reason about the behavior of objects within the system.

In summary, encapsulation in classes offers numerous benefits over the spaghetti functional approach, including modularity, information hiding, code reusability, and better management of state. By adhering to OOP principles, developers can create codebases that are more maintainable, understandable, and robust.