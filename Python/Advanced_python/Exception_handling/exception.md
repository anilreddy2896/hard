# There are 2 types of errors
   1. Syntax errors: 
         Errors occur due to invalid syntax is called are syntax errors
   2. Runtime errors:
        Errors that occur 

What is an exception? 
  unwanted event that distrubs normal flow of execution is called exception
what is the purpose exception handling?
  for gracefull termination of the program
what is the meaning of exception handling?
   to provide alternate solution for gracefull termination

Default exception handling:
   in this if an exception occurs pvm checks for  the exception code to handle ,if it doesn't found than terminates the program abnormally and prints the exception error msg on the console 
1. 
try:
  <code>
except <error name>:
     handling code

2. try with multiple exceptions
  try:
      <code>
   except 1:
      <handling code>
   except 2:
      <handling code>
3. single except block handling multiple exceptions
   try :
     <code>
   exccept (exception1,except2,exception3,....)
      <handling code>
4. default except block
   try :
     <code>
  except <exception name>:
     <handling code>
  except: # this is the default except block
     <handling code> 

 default except block should be at the last , if it is anywhere else it pvm will pushes the error


 ## finally      

try: 
    <risky code>
except:
   <handling code>
finally:
   <cleanup code>