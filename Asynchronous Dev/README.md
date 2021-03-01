# Async with Python

In here I'm explaining with examples a little bit of this very advanced topic. Make sure to check comments on the code to understand and run them and play around with them.

## Concurrency
The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.

## Parallelism
Running two or more things at the same time.

## Synchronous
Actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.

## Asynchronous
Actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").

Async switches cooperatively, so you do need to add explicit code “yield” or “await” to cause a task switch.

Now you control when task switches occur, so locks and other synchronization are no longer needed.

Also, the cost task switches is very low. Calling a pure Python function has more overhead than restarting a generator or awaitable.

This means that async is very cheap.

In return, you’ll need a non-blocking version of just about everything you do. Accordingly, the async world has a huge ecosystem of support tools. This increases the learning curve.


## Thread
A line of code execution that can run in one of your computer's cores.
By nature, Python is a linear language, but the threading module comes in handy when you want a little more processing power. While threading in Python cannot be used for parallel CPU computation, it's perfect for I/O operations such as web scraping because the processor is sitting idle waiting for data.

Threads switch preemptively. This is convenient because you don’t need to add explicit code to cause a task switch.

The cost of this convenience is that you have to assume a switch can happen at any time. Accordingly, critical sections have to be guarded with locks.

#### Code example:
- [Thread](https://github.com/amssdias/python-advanced_topics/blob/master/Asynchronous%20Dev/threads.py)
- [Thread with pool](https://github.com/amssdias/python-advanced_topics/blob/master/Asynchronous%20Dev/threads_with_pool.py)

## Process 
One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).

Without multiprocessing, Python programs have trouble maxing out your system's specs because of the `GIL` (Global Interpreter Lock). Python wasn't designed considering that personal computers might have more than one core (shows you how old the language is), so the GIL is necessary because Python is not thread-safe and there is a globally enforced lock when accessing a Python object. Though not perfect, it's a pretty effective mechanism for memory management. What can we do?

Multiprocessing allows you to create programs that can run concurrently (bypassing the GIL) and use the entirety of your CPU core. Though it is fundamentally different from the threading library, the syntax is quite similar. The multiprocessing library gives each process its own Python interpreter and each their own GIL.

Because of this, the usual problems associated with threading (such as data corruption and deadlocks) are no longer an issue. Since the processes don't share memory, they can't modify the same memory concurrently.


#### _Windows_
   Due to the way Windows forks processes, you must make sure that the code that starts a process is surrounded by if `__name__ == "__main__"`.
   
   Otherwise when we start new processes on Windows, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.
   
   It's because Windows does not have os.fork , so instead of forking the process at the point where a new process is created, Windows has to start the process from scratch and import your Python file in order to run the process' target. In doing so, you'll run through the file and actually create another process, and then that'll do the same, and so on.

#### Code example:
- [Processes](https://github.com/amssdias/python-advanced_topics/blob/master/Asynchronous%20Dev/processes.py)
- [Processes with pool](https://github.com/amssdias/python-advanced_topics/blob/master/Asynchronous%20Dev/processes_with_pool.py)

## GIL
A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.

The `Python Global Interpreter Lock` or `GIL`, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an “infamous” feature of Python.

[More about the GIL](https://realpython.com/python-gil/)