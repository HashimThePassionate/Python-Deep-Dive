from typing import Final, Tuple

DB_HOST: Final = "localhost"



def connect_to_test_database():
    global DB_HOST
    DB_HOST = "test-db.example.com"  # Accidentally reassigning DB_HOST for a test database
    # Proceed with test connection...

# CONFIG: Final[Tuple[str, str]] = ("debug_mode_off", "version_1.0")

# Attempting to change CONFIG or its content will raise an error with `mypy`
# CONFIG[0] = "debug_mode_on"  # Type error: Tuples are immutable