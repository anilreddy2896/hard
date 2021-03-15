## Duck typing philosophy
In python we can type of object so it depends on the behaviour of the method
"uses the principle of Duck typing"

to Check whether the particular method is present or we use the 
## hasattr() method


# Overloading:
   1. operator overloading: 
        we implement magic methods using magic methods

        when ever we are trying to print object reference than internally 
        __str__() is called

    2. Method overloading:
         This concept is not applicable in python
         if the two different methods having the same name than python will consider the most recent method and the old method is not consider 
         # This is handled by the default arguments 
    3. Constuctor over loading is not possible in python.
        if we want to use overloading constructor use the default or variable length arguments

# over riding:
   if the child is inherit from the parent and the child class want to refined the method of parent is called over riding
   simply methods having same name but having different functionality
   method over riding is applicable for both methods and constructors
    