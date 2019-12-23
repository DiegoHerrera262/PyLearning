# Day 2: Learning Python Basics

**Date: 23-12-19**

After everything is installed, I guess, I hope to test some of NumPy and SciPy functionalities in my smartphone. I hope to learn some of the python philosophy and compare it to **MATLAB**. I've already installed MATLAB Mobile on my phone and hope to compare it to python.

**NOTE:** Since I also intend to improve my MATLAB programming skills, for I think python and MATLAB might by similar in some sense, I use **MATLAB: A Practical INtroduction To Programming and Problem Solving**, from Stormy Attaway, to learn MATLAB too.

## Python nature

Both MATLAB and Python have interactive command windows where you can insert a series of instructions. Both languages are interpreted. That basically means that there is an **interpreter** that executes each command as soon as it gets to it. This reduces computation speed sometimes. You can write a script in python and execute it using command line:

```
python script.py
```

There are some simple examples on introducing python which are too easy to document. But there are some tips I might take into account:

* Declaration of variables do not require specifying type.
* I can get variable type using ```type()```. 
* Comments are introduced using '#'.
* Add packages using ```import pck_name as abbrev```
* Basic mathematical functions can be used with **math package**.

### Using functions in Python

Python supports user defined functions, you just need to use the sintax:

```python
def my_func(arg1,arg2):
    # Operatios on arguments
    return output
```

## Multidimensional Arrays

Arrays are used whenever you have a lot of data over which you expect to perform the same operation. They make this operations far easier. Python being an **interpreted language** implies that **vectorized computations** are far more efficient than element to element computations.


