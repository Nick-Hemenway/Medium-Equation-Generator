# Overview
The writing platform [Medium](https://medium.com/) does not currently support math equations on it's website. This is incredibly unfortunate for technical writers like myself as equations must be included as images of the correct size and format. If you want the equations to look at all decent when published, it becomes a massive undertaking, especially if your article has a lot of equations in it.

This small repository aims to alleviate the issue described above by providing a simple way to generate equation images using python. The code provides a thin wrapper around `matplotlib` and `Latex` and provides a clean interface for generating equation images. Default parameters are set such that the images should look good on the medium platform by default without any script customization.

# Installation
Currently, this repository is not set up as an official python package that can be installed. To use the code, you must clone this repository and manually place the `eq_generator.py` script in an appropriate location such that python can find it (for example, in your working directory). Note, matplotlib is using latex as a dependency to render the equations, which means you must have latex installed on your computer for the script to work.

# Useage
The code only contains a single `MediumEq` class that must be imported. 

Then it can be used as follows:


```python
from eq_generator import MediumEq

#create latex formatted equation string
eq = r'$y(x) = \frac{A_0}{2} + \sum_{n=1}^\infty A_n \cos(2\pi\frac{n}{p}x - \phi_n)$'

#instantiate a medium equation generator object
eq_gen = MediumEq()

#the object is callable and returns a matplotlib figure and axes object
fig, ax = eq_gen(eq)

#save the figure as an image file
fig.savefig("fourier_series_inline.png")
```

We get the following image:
![](./assets/fourier_series_inline.png)

Note that by default, the equation string will be rendered in inline mode. We can circumvent this by adding the latex command `\displaystyle` to our equation string as follows (see [here](https://www.overleaf.com/learn/latex/Display_style_in_math_mode) for more details):

```python
eq = r'$\displaystyle y(x) = \frac{A_0}{2} + \sum_{n=1}^\infty A_n \cos(2\pi\frac{n}{p}x - \phi_n)$'

fig, ax = MediumEq()(eq)
fig.savefig("fourier_series.png")
```
![](assets/fourier_series.png)

We can see that our equation gets cut off on the top and bottom. We can add more vertical space by manually specifying the `height` parameter when we instantiate the equation generator object (note: height is given in pixels)

```python
fig, ax = MediumEq(height=250)(eq)
fig.savefig("assets/fourier_series_tall.png")
```

And we get the following:
![](./assets/fourier_series_tall.png)

Ta da! A beautiful image of our equation that can be loaded directly to Medium, and by default it's the correct width (1400px) such that it will not look blurry or pixelate on their website.