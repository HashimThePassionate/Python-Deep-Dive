from dataclasses import dataclass, InitVar

# Example database type
class DatabaseType:
    def lookup(self, key):
        # Simulate a database lookup
        return 42

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

# Creating an instance of C
my_database = DatabaseType()
c = C(10, database=my_database)
print(c)
# Output: C(i=10, j=42)
