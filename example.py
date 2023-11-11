from src.eq_generator import MediumEq

eq_inline = r'$y(x) = \frac{A_0}{2} + \sum_{n=1}^\infty A_n \cos(2\pi\frac{n}{p}x - \phi_n)$'

fig, ax = MediumEq()(eq_inline)
fig.savefig("assets/fourier_series_inline.png")

#note: we add \displaystyle to convert the equation from inline to full equation style
#see link for more detail: https://www.overleaf.com/learn/latex/Display_style_in_math_mode
#create image not in inline mode by adding \display to latex string
eq = r'$\displaystyle y(x) = \frac{A_0}{2} + \sum_{n=1}^\infty A_n \cos(2\pi\frac{n}{p}x - \phi_n)$'

fig, ax = MediumEq()(eq)
fig.savefig("assets/fourier_series.png")

#increase the y-height to 250 pixels
fig, ax = MediumEq(height=250)(eq)
fig.savefig("assets/fourier_series_tall.png")