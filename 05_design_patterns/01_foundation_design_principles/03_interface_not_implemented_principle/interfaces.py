from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Console: {message}")


class FileLogger(Logger):
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(f"File: {message}\n")


def log_message(logger: Logger, message: str) -> None:
    logger.log(message)

if __name__ == "__main__":
    log_message(ConsoleLogger(), "A console log.")
    log_message(FileLogger(), "A file log.")
