# Day 1: Setting everything up

**Date:** 22-12-19

I'm using my Android Smartphone (Redmi Note 8) to set up the documentation repo **PyLearning**. I must say I'm very excited about this whole experience. Up to now, I've just used a laptop or desktop computer to code. Now I realize I can use my smartphone, with the additional advantages that I can use the integrated sensors, like accelerometer gyro or temperature sensor, to develop cool apps.

## Setting up the environment

First, I installed Termux, wich is a really cool app. It basically sets up a sort of Linux-based subsystem in your phone. In order to install packages like in your desktop computer, you can use either **pkg** or **apt**. Personally, at this point I use more pkg; apt is quite usefull though.

### Installing Python

I installed Python using the command

```
pkg install clang python
```

After installing python, another package is installed: **pip**. I updated pip using the command

```
pip install --upgrade pip
```

Pip is supposed to be the package manager of python. However, for many packages it doesn't work. So, you must be very eager to find in the internet a suitable way to install most of your packages. In the description of the repo I listed all the packages I thought I might need. So, I write the way I remember how those were installed in my phone using Termux.

### Installing NumPy

First, you must install a package called **wheels** using pip. I think this helps the compiler to set up a piece of code that runs the installing process. You can use the command:

```
pip install wheel
```

If you have upgraded pip, I'm pretty sure NumPy will be installed by running:

```
pip install numpy
```

However, if that does not work, you must use the **its-pointless** repo as explained in [this link](https://wiki.termux.com/wiki/Installing_Scipy_The_Easy_Way). Incidentally, that's how yo install SciPy.

### Installig SciPy

This package I couldn't install using pip. I had to use the **ts-pointless** repo. I followed the instructions on [this link](https://wiki.termux.com/wiki/Installing_Scipy_The_Easy_Way). Then, using the command:

```
pip list
```

I saw that both, NumPy and SciPy, where installed.

### Installing Matplotlib

This was a hard one. I tried using pip at first, but it was but a headache. So, I looked it up on google. I found [a nice page](https://github.com/termux/termux-packages/issues/3761) where I saw that I was missing some dependencies. I installed **pkg-config** using:

```
apt install pkg-config
```

And then reproduced the suggestons in that link. After that, I checked with pip, and I finally had Matplotlib.

### Installing Pandas

This is a complete mistery to me. I tried using pip, but it was in vane. I tried a while after, and everything was good. So, I don't know for sure what is the correct process for getting Pandas.

## Next Tasks

After installing all those packages, I plan to test them with simple sketches. Landau's book has an introductory chapter on python that uses matplotlib, and Johanssons' also has one on NumPy. SciPy and Pandas are more complex, and I hope to get there soon enough. 


**NOTE:** It's absolutelly important to learn how to include the tilde. Otherwise, I just have to turn off bluethooth keyboard and use google keyboard.