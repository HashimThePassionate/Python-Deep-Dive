import time

def cook_1():
    """First cook: Prepares the pizza dough and adds sauce."""
    steps = []
    steps.append("🥖 Cook 1: Preparing the pizza dough...")
    time.sleep(1)  # Simulating time delay
    steps.append("🍅 Cook 1: Adding tomato sauce...")
    time.sleep(1)
    return steps  # Returning progress

def cook_2(previous_steps):
    """Second cook: Adds toppings and preheats the oven."""
    steps = previous_steps  # Continuing from previous steps
    steps.append("🧀 Cook 2: Adding cheese and toppings...")
    time.sleep(1)
    steps.append("🔥 Cook 2: Preheating the oven...")
    time.sleep(1)
    return steps  # Returning progress

def cook_3(previous_steps):
    """Third cook: Bakes the pizza and serves it."""
    steps = previous_steps  # Continuing from previous steps
    steps.append("🍕 Cook 3: Placing the pizza in the oven...")
    time.sleep(1)
    steps.append("⏳ Cook 3: Waiting for the pizza to bake...")
    time.sleep(1)
    steps.append("✅ Cook 3: Pizza is ready to serve! 🍽️")
    return steps  # Final result

# Simulating the cooking process
steps_1 = cook_1()      # Cook 1 starts
steps_2 = cook_2(steps_1)  # Cook 2 continues
final_steps = cook_3(steps_2)  # Cook 3 finishes

# Display the step-by-step process
for step in final_steps:
    print(step)
