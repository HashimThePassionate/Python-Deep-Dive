from typing import Protocol

class MessageSender(Protocol):
    def send(self, message: str) -> None:
        ...

class Email:
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, sender: MessageSender) -> None:
        self.sender: MessageSender = sender

    def send(self, message: str) -> None:
        self.sender.send(message)

def send_notification(sender: MessageSender, message: str) -> None:
    notif = Notification(sender=sender)
    notif.send(message=message)

if __name__ == "__main__":
    email_sender = Email()
    send_notification(sender=email_sender, message="This is the message.")
