# Solution for Project Video

#### 1. Interfaces (Abstract Base Classes)

We define three abstract base classes to serve as interfaces for our components.

```python
from abc import ABC, abstractmethod

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
```

- **IVideoEncoder**: An interface with an abstract method `encode`, which will be implemented by concrete classes to encode a video.
- **IVideoDatabase**: An interface with an abstract method `store`, which will be implemented by concrete classes to store video metadata in a database.
- **IEmailService**: An interface with an abstract method `send_email`, which will be implemented by concrete classes to send email notifications to users.

#### 2. User Class

We define the `User` class to represent a user with an email address.

```python
class User:
    def __init__(self, email: str):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email
```

- **Constructor (`__init__`)**: Initializes the `_email` attribute.
- **Getter (`@property` `email`)**: Allows access to the `_email` attribute.
- **Setter (`@<property>.setter` `email`)**: Allows setting the `_email` attribute.

#### 3. Video Class

We define the `Video` class to represent a video with a file name, title, and associated user.

```python
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
```

- **Constructor (`__init__`)**: Initializes the `_file_name`, `_title`, and `_user` attributes.
- **Getters and Setters**: Provide access to and allow setting of the `_file_name`, `_title`, and `_user` attributes.

#### 4. Implementations

We provide concrete implementations for the interfaces defined earlier.

```python
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
```

- **VideoEncoder**: Implements the `encode` method to print a message indicating that the video is being encoded.
- **VideoDatabase**: Implements the `store` method to print a message indicating that the video metadata is being stored in a SQL database, along with the video's title and file name.
- **EmailService**: Implements the `send_email` method to print a message notifying the user's email address.

#### 5. VideoProcessor Class

We define the `VideoProcessor` class to orchestrate the encoding, storing, and email notification processes.

```python
class VideoProcessor:
    def __init__(self, encoder: IVideoEncoder, database: IVideoDatabase, email_service: IEmailService):
        self._encoder = encoder
        self._database = database
        self._email_service = email_service

    def process(self, video: Video):
        self._encoder.encode(video)
        self._database.store(video)
        self._email_service.send_email(video.user)
```

- **Constructor (`__init__`)**: Accepts instances of `IVideoEncoder`, `IVideoDatabase`, and `IEmailService` and assigns them to private attributes.
- **Process Method (`process`)**: Encodes the video, stores its metadata in the database, and sends an email notification to the user.

#### 6. Main Execution

Finally, we provide the main execution block to create instances and execute the process.

```python
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
```

- **Create Video Instance**: An instance of `Video` is created and its `file_name`, `title`, and `user` properties are set.
- **Create Service Instances**: Instances of `VideoEncoder`, `VideoDatabase`, and `EmailService` are created.
- **Create VideoProcessor Instance**: An instance of `VideoProcessor` is created with the service instances as arguments.
- **Process Video**: The `process` method of `VideoProcessor` is called with the `video` instance, triggering the encoding, storing, and email notification processes.
