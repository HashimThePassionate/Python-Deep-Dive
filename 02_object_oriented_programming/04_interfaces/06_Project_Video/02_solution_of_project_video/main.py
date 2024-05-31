from abc import ABC, abstractmethod

# Interfaces (Abstract Base Classes)


class IVideoEncoder(ABC):
    @abstractmethod
    def encode(self, video):
        pass


class IVideoDatabase(ABC):
    @abstractmethod
    def store(self, video):
        pass


class IEmailService(ABC):
    @abstractmethod
    def send_email(self, user):
        pass

# User class


class User:
    def __init__(self, email: str):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

# Video class


class Video:
    def __init__(self):
        self._file_name = None
        self._title = None
        self._user = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        self._file_name = file_name

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user: User):
        self._user = user

# Implementations


class VideoEncoder(IVideoEncoder):
    def encode(self, video: Video):
        print("Encoding video...")
        print("Done!\n")


class VideoDatabase(IVideoDatabase):
    def store(self, video: Video):
        print("Storing video metadata in a SQL database...")
        print(f"Title: {video.title}")
        print(f"File Name: {video.file_name}")
        print("Done!\n")


class EmailService(IEmailService):
    def send_email(self, user: User):
        print(f"Notifying {user.email}...")
        print("Done!\n")

# VideoProcessor class


class VideoProcessor:
    def __init__(self, encoder: IVideoEncoder, database: IVideoDatabase, email_service: IEmailService):
        self._encoder = encoder
        self._database = database
        self._email_service = email_service

    def process(self, video: Video):
        self._encoder.encode(video)
        self._database.store(video)
        self._email_service.send_email(video.user)


# Main execution
if __name__ == "__main__":
    video = Video()
    video.file_name = "birthday.mp4"
    video.title = "Jennifer's birthday"
    video.user = User("john@domain.com")

    encoder = VideoEncoder()
    database = VideoDatabase()
    email_service = EmailService()

    processor = VideoProcessor(encoder, database, email_service)
    processor.process(video)
