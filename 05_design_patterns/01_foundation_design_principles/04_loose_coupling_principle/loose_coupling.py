from typing import Protocol

class Sender(Protocol):
    def send(self, message: str) -> None:
        ...

class MessageService:
    def __init__(self, sender: Sender) -> None:
        self.sender: Sender = sender

    def send_message(self, message: str) -> None:
        self.sender.send(message)

class EmailSender:
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")

class SMSSender:
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")

if __name__ == "__main__":
    email_service: MessageService = MessageService(EmailSender())
    email_service.send_message("Hello via Email")
    
    sms_service: MessageService = MessageService(SMSSender())
    sms_service.send_message("Hello via SMS")
