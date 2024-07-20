from main import *

woody = Bird()
alert(woody)        # Runtime error: 'Bird' object has no attribute 'quack'
alert_duck(woody)   # Runtime error: Argument 1 to "alert_duck" has incompatible type "Bird"; expected "Duck"
alert_bird(woody)   # Runtime error: 'Bird' object has no attribute 'quack'