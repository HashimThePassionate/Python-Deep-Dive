class User:
    def __init__(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


class Video:
    def __init__(self):
        self.__file_name = None
        self.__title = None
        self.__user = None

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user


class VideoDatabase:
    def store(self, video):
        print("Storing video metadata in a SQL database...")
        print("Title:", video.get_title())
        print("File Name:", video.get_file_name())
        print("Done!\n")


class VideoEncoder:
    def encode(self, video):
        print("Encoding video...")
        print("Done!\n")


class VideoProcessor:
    def process(self, video):
        encoder = VideoEncoder()
        encoder.encode(video)

        database = VideoDatabase()
        database.store(video)

        email_service = EmailService()
        email_service.send_email(video.get_user())


class EmailService:
    def send_email(self, user):
        print("Notifying", user.get_email(), "...")
        print("Done!\n")


video = Video()
video.set_file_name("birthday.mp4")
video.set_title("Jennifer's birthday")
video.set_user(User("john@domain.com"))

processor = VideoProcessor()
processor.process(video)
