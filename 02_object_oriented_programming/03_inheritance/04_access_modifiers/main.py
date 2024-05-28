class PrivateAccessError(Exception):
    pass


class UIControl:
    def __init__(self, is_enabled=True):
        self.__is_enabled = is_enabled

    def enable(self):
        self.__is_enabled = True
        return f'Dynamically Call to Enable Method with attribute : {self.__is_enabled}'

    def __disable(self):
        self.__is_enabled = False
        return f'Dynamically Call to __disable Method with attribute : {self.__is_enabled}'

    def __is_enabled(self):
        return self.__is_enabled

    def access_private(self, attribute):
        if attribute == "__is_enabled":
            raise PrivateAccessError(f"Access to private attribute '{
                                     attribute}' is not allowed.")
        else:
            return getattr(self, attribute)

    def call_private(self, method):
        if method == "__disable" or method == "__is_enabled":
            raise PrivateAccessError(f"Access to private method '{
                                     method}' is not allowed.")
        else:
            return getattr(self, method)()


class TextBox(UIControl):
    def __init__(self):
        super().__init__(True)
        self.__text = ""

    def set_text(self, text):
        self.__text = text

    def clear(self):
        self.__text = ""

    def access_private(self, attribute):
        if attribute == "__text":
            raise PrivateAccessError(f"Access to private attribute '{
                                     attribute}' is not allowed.")
        else:
            return super().access_private(attribute)


# Creating an instance of TextBox
control = TextBox()
c = UIControl()
access = c.access_private('enable')
print(access())

# Attempting to access private method and raising an error
try:
    control._UIControl__disable()  # Forcefully accessing private method
except AttributeError:
    print("Direct access to private methods is not allowed.")

# Attempting to access private method using call_private method
try:
    control.call_private("__disable")
except PrivateAccessError as e:
    print(e)

# Attempting to access private attribute and raising an error
try:
    control.access_private("__is_enabled")
except PrivateAccessError as e:
    print(e)

# Checking if control is enabled
# Access private member indirectly
print(control.access_private("_UIControl__is_enabled"))
