# Function-based decorator implementation

is_logged_in = False # Global variable to track user login status

def login_required(func):
    """
    This is the decorator function. It wraps another function
    to add a login check. 
    """
    def wrapper(*args, **kwargs):
        global is_logged_in
        if is_logged_in:
            print("Access granted! 🔓")
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in first. ⛔")
            return None
    return wrapper

def login():
    """Simulates a user login."""
    global is_logged_in
    is_logged_in = True
    print("User logged in successfully! 👋")

def logout():
    """Simulates a user logout."""
    global is_logged_in
    is_logged_in = False
    print("User logged out. See you later! 👋")

@login_required
def view_dashboard():
    """A function that requires a user to be logged in."""
    print("Welcome to your private dashboard. Here is your secret data...")

@login_required
def post_new_article():
    """A function that also requires a user to be logged in."""
    print("Posting a new article...")

# --- User interaction flow ---

print("--- Scenario 1: Not logged in ---")
view_dashboard()
print("\n--- Scenario 2: Logging in and accessing dashboard ---")
login()
view_dashboard()
print("\n--- Scenario 3: Posting an article while logged in ---")
post_new_article()
print("\n--- Scenario 4: Logging out and trying again ---")
logout()
view_dashboard()



# Class-based decorator implementation

is_logged_in = False # Global variable to track user login status

class LoginRequired:
    """
    A class-based decorator to check if a user is logged in
    before executing a function.
    """
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        global is_logged_in
        if is_logged_in:
            print("Access granted! 🔓")
            return self.func(*args, **kwargs)
        else:
            print("Access denied. Please log in first. ⛔")
            return None

def login():
    """Simulates a user login."""
    global is_logged_in
    is_logged_in = True
    print("User logged in successfully! 👋")

def logout():
    """Simulates a user logout."""
    global is_logged_in
    is_logged_in = False
    print("User logged out. See you later! 👋")

@LoginRequired
def view_dashboard():
    """A function that requires a user to be logged in."""
    print("Welcome to your private dashboard. Here is your secret data...")

@LoginRequired
def post_new_article():
    """A function that also requires a user to be logged in."""
    print("Posting a new article...")

# --- User interaction flow ---

print("--- Scenario 1: Not logged in ---")
view_dashboard()
print("\n--- Scenario 2: Logging in and accessing dashboard ---")
login()
view_dashboard()
print("\n--- Scenario 3: Posting an article while logged in ---")
post_new_article()
print("\n--- Scenario 4: Logging out and trying again ---")
logout()
view_dashboard()