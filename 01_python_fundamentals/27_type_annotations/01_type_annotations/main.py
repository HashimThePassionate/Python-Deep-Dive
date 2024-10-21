from datetime import datetime
import random

def schedule_restaurant_open(open_time: datetime, workers_needed: int) -> None:
    available_workers: list[Worker] = find_workers_available_for_time(open_time)
    if len(available_workers) < workers_needed:
        print("Not enough workers available.")
    else:
        # Use random.sample to pick the required number of workers
        for worker in random.sample(available_workers, workers_needed):
            worker.schedule(open_time)

class Worker:
    def __init__(self, name: str):
        self.name = name

    def schedule(self, time: datetime) -> None:
        print(f"Worker {self.name} scheduled at {time}.")

def find_workers_available_for_time(open_time: datetime) -> list[Worker]:
    return [Worker("Alice"), Worker("Bob"), Worker("Charlie")]

# Call the function
schedule_restaurant_open(datetime(2024, 10, 9, 9, 0), 2)
