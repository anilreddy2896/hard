Multi tasking :
     executing multiple tasks simultaneously is known as multi tasking

2 types of multitasking:
    1. process based multitasking:
          executing several tasks simultaneously where each task is a seperate independent process
          this is done at os level
    2. thread based multitasking:
          this is done at program level
          executing several tasks simultaneously where each task is a seperate independent part of the same program
          and each independent part is called a thread

in python multithreading is supported my a module called threading

Every python program will consists of one default thread is called main thread 
 
 Thread:
    *  A thread is a independent part of program 
    *  Flow of execution 
    *  for every thread there is some job available
    *  that job will be executed when we call or run that thread

    1. single threaded program: will contain only one  thread   
    2. multi threaded program

    creating Thread in python:
        1> Creating a thread without using any class
        2. By extending the thread class
        3. without extending the thread class
                     

Thread identification number(ident):
----------------------------------------
t=Thread(target=test)
t.ident

# for active count of threads
active_count()

# to get name we can use
t.name
t.getName()

##   to get the list of all  the active threads count we use
enumerate() function

# to know whether the thread is alive
isAlive() 

# join() method:
     if you want your thread to wait until another thread is completed we go for join method 

## deamon Threads:
    the  thread which run in background is called daemon thread
    # to check whether the thread is daemon or not
    <threadname>.isDeamon() or
    <threadname>.daemon
    
    To set the deamon nature:
        <threadname>.setDaemon(True/False)

    Default nature of the main thread is non-daemon
    for all remaining threads the daemon nature is inherited from parent

    we cannot change the daemon nature of the thread once it started , if not starte we can change it.    

    # if last non-daemon thread is terminated than the daemon threads by default will be terminated
    because the daemon thread will give support to the non-daemon threads

# synchronization
----------------------
 to remove data inconsistency we go for synchronization so that only one thread will be executed once

 to implement synchronization we have 3 methods:
      1. locks:  
            to create lock: l=Lock()
            acquiring lock--> l.acquire()
            release lock---> l.release()
      2. r locks 
            rlocks are used during the recursion functions
            l=RLock()
            l.acquire()
            l.release()
      3. semaphores
           semaphore allows multiple thread to access at a time
           s=Semaphore(count)
           default count value is 1
           s=Semaphore(5) # this means it can be accessed by 5 threads
           if
             s.acquire(1) then the counter value is reduced by 1
             s.release(1) then counter value is increamented by 1
             the number of releases can exceed the number of acquire locks
             # bounded semaphore:
                it is same as semaphore but the number acquire calls  and release calls should be exactly equal
                s=BoundedSemaphore(count) 
# inter thread communication: 
       1. event
       2. condition
       3. queue
