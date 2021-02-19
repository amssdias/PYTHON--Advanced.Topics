def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')

# Another way instead of using Threads is using Generators. It's cheaper than threads.