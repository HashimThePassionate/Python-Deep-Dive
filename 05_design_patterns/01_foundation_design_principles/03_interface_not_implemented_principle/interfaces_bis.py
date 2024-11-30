from typing import Protocol

class Logger(Protocol):
    def log(self, message: str) -> None:
        ...

class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"Console: {message}")

class FileLogger:
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(f"File: {message}\n")

def log_message(logger: Logger, message: str) -> None:
    logger.log(message)


if __name__ == "__main__":
    log_message(ConsoleLogger(), "A console log.")
    log_message(FileLogger(), "A file log.")
