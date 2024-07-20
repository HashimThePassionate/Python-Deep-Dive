from main import *

daffy = Duck()
alert(daffy)        # Valid call, no type hints
alert_duck(daffy)   # Valid call, daffy is a Duck
alert_bird(daffy)   # Valid call, daffy is also a Bird
