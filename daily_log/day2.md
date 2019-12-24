# Day 2: Learning Python Basics

**Date:** 23-12-19 ; 24-12-19

After everything is installed, I guess, I hope to test some of NumPy and SciPy functionalities in my smartphone. I hope to learn some of the python philosophy and compare it to **MATLAB**. I've already installed MATLAB Mobile on my phone and hope to compare it to python.

**NOTE:** Since I also intend to improve my MATLAB programming skills, for I think python and MATLAB might by similar in some sense, I use **MATLAB: A Practical Introduction To Programming and Problem Solving**, from Stormy Attaway, to learn MATLAB too.

## Python nature

Python has interactive command windows where you can insert a series of instructions. This language is interpreted. That basically means that there is an **interpreter** that executes each command as soon as it gets to it. This reduces computation speed sometimes. You can write a script in python and execute it using command line:

```
python script.py
```

There are some simple examples on introducing python which are too easy to document. But there are some tips I might take into account:

* Declaration of variables do not require specifying type.
* I can get variable type using ```type()```.
* User entry can be achieved using ```input()```. But input is a string.
* Comments are introduced using '#'.
* Add packages using ```import pck_name as abbrev```
* Basic mathematical functions can be used with **math package**.
* Exponentiation is supported by ```**``` operator.

### Using functions in Python

Python supports user defined functions, you just need to use the sintax:

```python
def my_func(arg1,arg2):
    # Operations on arguments
    return(output1,output2)
```

### Conditionals and loops

If statements in python have this sintax:

```python
if cond:
   # do something
else:
   # do other thing
```

There can be nested conditionals. Chained conditionalas have the sintax:

```python
if cond1:
   # do action 1
elif cond2:
   # do action 2
else:
   # do default action
```

It is very important to know that python supports recursive functions. In fact, I plan to write a script that implements bisection recursively. An example of this kind of sintax is the file [**PyBasics.py**](https://github.com/DiegoHerrera262/PyLearning/blob/master/codes/PyBasics.py). Python can return an arbitary number of outputs from an arbitrary number of inputs. The operations may range from concatenating strings and print them, or perform complicated mathematical operations.

Concerning the loops, python seems to have definite papers for the common C++ while and for. The **while** sintax:

```python
while cond:
   # do same stuff
```

Is used for reapeating a determined action. Whereas de **for** sintax:

```python
for counter in array_of_things
    # do something with array elements
```

Is more suitable for iteration over array elements. Those apparent functions are not inherent to python language, but it looks to me as if that's the case. Both loop types can be stopped by using ```break```.

**NOTE:** Although string management in python is quite fun and apparently easy using **string** package, Idon't plan to get deep into this topic since my intentions are more realted to scientific computing.

### Lists, Tuples and Dictionaries

Basically, a **list** is an ordered set of elements that can be of very different type. You can even create nested lists (i.e. lists of lists). NUmerical lists can be created using ```brange(inf_lim, sup_lim)``` to create a list that ranges from inf_lim to sup_lim, step one by default.

Lists are created using the sintax:

```python
my_list = [elem1 , elem2 , elem3]
```

Lists have the following functionalities:

* Iteration over list elements can be performed using a for loop easilly:

```python
for element in list:
    # do something on elements
```

* Lists can be **concatenated** usign ```+``` operator, and replicated + concatenated using ```*``` operator.
* SLices of a list can be copied using ```list[inf_index:sup_index]```.
* ELements of lists can be deleted using ```del()``` functions. More generally, *list elements can be modified*.

**IMP:** When used as arguments of functions, lists are passed by reference. That means that the functions actually modifies the list passed as argument, if the function is required to do so.

**Tuples** are like immutable lists. A tuple can be created using the sintax:

```python
my_tuple = (el1, el2, el3, el4)
```

Actually, parentheses are not necessary. Selecting slices can be done as selecting slices of lists. Up to now, I don't know how importatn tuples might be in the future. ALso, there are so called **dictionaries**. These make honor of their nime, since they consist of a set of tuples, of two elements each, that associate two elements. It i lake associating a word and its meaning. A nice application can be counting the number of repetitions of a letter in a word (or even a text), and produce detailed statistics. In the future, when I learn how to use pandas, I might use this structures to analize information content per symbol on a text in English, in order to reproduce Shannon's results.  
 
## Multidimensional Arrays

Arrays are used whenever you have a lot of data over which you expect to perform the same operation. They make this operations far easier. Python being an **interpreted language** implies that **vectorized computations** are far more efficient than element to element computations.


## Emacs Notes

I have learned how to edit several files in emacs. I have to use the combination ```C-x C-f``` to open a new buffer, and select the file (I must remember de route). Then, I switch between buffers using ```C-x b``` and selecting the file name. This might prove usefull.