from src.eq_generator import MediumEq

#note: we add \displaystyle to convert the equation from inline to full equation style
#see link for more detail: https://www.overleaf.com/learn/latex/Display_style_in_math_mode
eq = r'$\displaystyle y(x) = \frac{A_0}{2} + \sum_{n=1}^\infty A_n \cos(2\pi\frac{n}{p}x - \phi_n)$'

fig, ax = MediumEq()(eq)
fig.savefig("assets/fourier_series.png")