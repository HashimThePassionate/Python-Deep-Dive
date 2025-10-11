import asyncio
import copy

# --------------------------------------------------------------------------
# Step 1: Ek Fake Database Banayein
# Yeh ek simple dictionary hai jo hamare data ko store karegi.
# --------------------------------------------------------------------------
FAKE_DB = {
    "users": {
        # Data format: user_id: {user_data}
        1: {"name": "Arham", "email": "arham@example.com"},
        2: {"name": "Bisma", "email": "bisma@example.com"},
    }
}

# --------------------------------------------------------------------------
# Step 2: Practical Implementation: Asynchronous Fake DB Connection Manager
# Yeh class hamari dictionary ke "connection" ko manage karti hai.
# --------------------------------------------------------------------------
class AsyncFakeDbConnection:
    def __init__(self, db_dict: dict):
        """
        Constructor mein, hum original dictionary ka reference store karte hain.
        """
        self._db = db_dict
        self._conn = None
        print("🔹 Connection Manager Initialized (No connection yet).")

    async def __aenter__(self):
        """
        'async with' block shuru hone par yeh method chalta hai.
        - Yeh "connection" ko simulate karta hai.
        - Hum database ki ek deep copy banate hain taake transaction jaisa feel aaye.
        """
        print("🔗 Simulating connection to fake DB...")
        await asyncio.sleep(0.1)  # Network delay simulate karein
        
        # Ek transaction simulate karne ke liye, hum original DB ki copy par kaam karenge.
        self._conn = copy.deepcopy(self._db)
        
        print("✅ Connection successful. Working on a temporary copy (transaction).")
        return self  # 'as db' variable mein yeh object (self) jayega

    async def __aexit__(self, exc_type, exc_val, traceback):
        """
        'async with' block khatam hone par yeh method chalta hai.
        - Agar koi error nahi aya, to temporary changes ko original DB mein save karein.
        - Agar error aya, to changes ko discard kar dein (rollback).
        """
        print("🔗 Simulating closing connection...")
        await asyncio.sleep(0.1) # Teardown delay simulate karein

        if exc_type is None:
            # Koi error nahi, changes ko commit karein.
            print("COMMIT: No errors found. Saving changes to original DB.")
            self._db.clear()
            self._db.update(self._conn)
        else:
            # Error aya, transaction ko rollback karein.
            print(f"ROLLBACK: An error occurred ({exc_type.__name__}). Discarding all changes.")
        
        self._conn = None
        print("✅ Connection closed.")

    async def fetchall(self, table_name: str):
        """
        Table (dictionary key) se saara data fetch karta hai.
        """
        print(f"🔍 Fetching all records from table '{table_name}'...")
        await asyncio.sleep(0.05) # Disk read simulate karein
        return list(self._conn.get(table_name, {}).values())

    async def insert(self, table_name: str, record: dict):
        """
        Table mein ek naya record daalta hai.
        """
        print(f"➕ Inserting new record into '{table_name}'...")
        await asyncio.sleep(0.05) # Disk write simulate karein
        
        if table_name not in self._conn:
            self._conn[table_name] = {}
            
        # Ek naya ID generate karein
        new_id = max(self._conn[table_name].keys(), default=0) + 1
        self._conn[table_name][new_id] = record
        print(f"  - Record added with ID {new_id}.")
        return new_id

# --------------------------------------------------------------------------
# Step 3: Main function jo is fake DB connector ko istemal karega
# --------------------------------------------------------------------------
async def main():
    print("--- Starting operations with Fake Dictionary DB ---")
    print(f"Initial DB state: {FAKE_DB}\n")

    # 'async with' ka istemal karke ek "transaction" chalayein.
    try:
        async with AsyncFakeDbConnection(FAKE_DB) as db:
            print("\n[Inside a successful transaction block]")
            
            # Data read karein
            all_users = await db.fetchall("users")
            print(f"Current users found: {len(all_users)}")
            
            # Naya data insert karein
            await db.insert("users", {"name": "Cyrus", "email": "cyrus@example.com"})
            
            # Dubara read karke check karein
            all_users_after_insert = await db.fetchall("users")
            print(f"Users after insert: {all_users_after_insert}")

            print("[Transaction block finished successfully]\n")
    except Exception as e:
        print(f"An unexpected error occurred in the main block: {e}")


    print(f"Final DB state after successful commit: {FAKE_DB}\n")
    
    print("--- Now, demonstrating a failed transaction (rollback) ---")
    
    try:
        async with AsyncFakeDbConnection(FAKE_DB) as db:
            print("\n[Inside a failing transaction block]")
            await db.insert("users", {"name": "Dania", "email": "dania@example.com"})
            print("✔️ Dania inserted into temporary copy.")
            
            # Yahan ek error simulate karein
            raise ValueError("Something went wrong during the operation!")
            
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    print(f"\nFinal DB state after failed transaction: {FAKE_DB}")
    print("Note: 'Dania' was not added because the transaction was rolled back.")


if __name__ == "__main__":
    asyncio.run(main())
