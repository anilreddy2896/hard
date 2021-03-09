import time
from imp import reload
import module1

print("the program going in to sleep")
time.sleep(30)
reload(module1)
time.sleep(30)
reload(module1)
print("end of program")
print(__name)