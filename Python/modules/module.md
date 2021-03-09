# importing the modules
import modulename

# importing multiple modules
import module1,module2,module3,module4

# module aliasing
import module as m

import module1 as m1,module2 as m2,,module3 as m3,,module4 as m4

# importing members of moudule
from modulename import add,sub,x,y
from module import *

# member aliasing 
from module import add as a,sub as b,x as c,y as d

To list all the member of the module 
dir()

## RE-LOADING OF THE MODULE 
and this reload is the part of imp module
/// from imp import  reload
reload(modulename)


# random module
