# Overview
The writing platform [Medium](https://medium.com/) does not currently support math equations on it's website. This is incredibly unfortunate for technical writers like myself as equations must be included as images of the correct size and format. If you want the equations to look at all decent when published, it becomes a massive undertaking, especially if your article has a lot of equations in it.

This small repository aims to alleviate the issue described above by providing a simple way to generate equation images using python. The code provides a thin wrapper around `matplotlib` and `Latex` and provides a clean interface for generating equation images. Default parameters are set such that the images should look good on the medium platform by default without any script customization.

# Installation
Currently, this repository is not set up as an official python package that can be installed. To use the code, you must clone this repository and manually place the `eq_generator.py` script in an appropriate location such that python can find it (for example, in your working directory).

# Useage
