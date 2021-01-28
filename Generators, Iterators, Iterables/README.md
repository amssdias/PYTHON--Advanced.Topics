# Python Generators, Iterators, Iterables


## Generator

A **generator** in Python is a function that remembers the state it’s in, in between executions.
Let’s explain with an example. Imagine you wanted to build a list of 100 numbers, like this one:

```python
def hundred_numbers():
  nums = []
  i = 0
  while i < 100:
    nums.append(num)
    i += 1
  return nums
```

We could use list comprehension for this and the `range()` function, but for now let’s assume that this is a cool way of doing it. We construct a list, fill it with the first 100 numbers, and then return them.

We now have 100 numbers in a list. The entire list is in your computer’s RAM memory, taking up an admittedly small amount of space.

If we wanted 10,000,000 numbers, the list would be substantially bigger. As you grow the number, the amount of memory taken up by the list also grows.

A **generator** is used to circumvent this problem. Instead of having a list, the first time you run the function you would get the first number (`0`). The second time you run the function you’d get `1`. Then `2`, and so on.

You have to run the function every time you want a new number, that’s why it’s called a “generator”. It generates numbers (or indeed strings, or anything else you want to generate).

```python
def hundred_numbers():
  num = 0
  while num < 100:
    yield num
    num += 1
```

The `yield` keyword is very much like a `return`, in that it gives the value back to the caller and returns execution control to them (show this with example run). However, the next time you run the function, execution continues from the very next line inside the function, instead of from the top.

**Generator** comprehension:

```python
hundred_numbers = (n for n in range(100))
```



## Iterator

The below is class which implements `__next__`as if it was a function using the `yield` keyword:

```python
class FirstHundredGenerator(object):
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

gen = FirstHundredGenerator()
next(gen)  # 0
next(gen)  # 1
```

Notice how the object, with its property, remembers what the value of `self.number` is at all points in time.

This object is called in Python a **generator** because every time the next number is available not because it’s in a sequence, but because it is generated from its current state (in this case, by adding 1 to `self.number`).

All objects that have this `__next__` method are called iterators. ***All generators are iterators, but not the other way round.***

For example, you could have an **iterator** on which you can call `next()`, but that doesn’t generate its values. Instead, it could take them from a list or from a database.

*Important*: **iterators** are objects which have a `__next__` method.

In Python, an **iterator** and an **iterable** are different things. You can iterate over an **iterable**. The **iterator** is used to get the next value (either from a sequence or generated values).

You can iterate over **iterables**, not over **iterators**.



## Iterable

An **iterable** is an object that has an `__iter__` method defined. The `__iter__` method *must return an iterator*.

Here’s an example of using our generator to make an **iterable**:

```python
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()
```

Now we have an **iterable** which uses the iterator to get the next value of the sequence it generates. We can do this:

```python
print(sum(FirstHundredIterable()))  # gives 4950

for i in FirstHundredIterable():
    print(i)
```

An **iterable** either has:

* `__len__` and `__getitem__` defined; or
* An `__iter__` method that returns an iterator.

If you have either of those two, you have yourself an **iterable**.
