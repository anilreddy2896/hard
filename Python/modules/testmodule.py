#import anilmath
# module name aliasing
#import anilmath as am
#am.add(20,30)
import  time
from imp import reload 
from anilmath import *
add(20,30)
time.sleep(30)
reload( anilmath )
div(12,2)
print(dir())