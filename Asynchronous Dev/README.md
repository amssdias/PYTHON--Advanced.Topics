# Async with Python

In here I'm explaining with examples a little bit of this very advanced topic. Make sure to check comments on the code to understand and run them and play around with them.


## Synchronous
Actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.

## Asynchronous
Actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").

## Concurrency
The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.

## Parallelism
Running two or more things at the same time.

## Thread
A line of code execution that can run in one of your computer's cores.

## Process 
One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).

### Windows
   Due to the way Windows forks processes, you must make sure that the code that starts a process is surrounded by if `__name__ == "__main__"`.
   
   Otherwise when we start new processes on Windows, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.
   
   It's because Windows does not have os.fork , so instead of forking the process at the point where a new process is created, Windows has to start the process from scratch and import your Python file in order to run the process' target. In doing so, you'll run through the file and actually create another process, and then that'll do the same, and so on.


## GIL
A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.