import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import e
from math import log
from math import radians


def fx(x):
    x = radians(x)
    s = sin(0.8 * x)
    return (e**cos(x)) + log(s**2 + 1) * cos(x)


def yx(x):
    x = radians(x)
    return -log((cos(x) + sin(x))**2 + 1.7) + 2

# arg values and func values 
xlist = list(np.linspace(-240, 360, (360 - (-240)) + 1))
flist = [fx(x) for x in xlist]
ylist = [yx(x) for x in xlist]

# build lines
line_f = plt.plot(xlist, flist, label='f(x)')
line_y = plt.plot(xlist, ylist, label='y(x)')

# styles
plt.setp(line_f, color='red', linewidth=2)
plt.setp(line_y, color='blue', linewidth=2)

# show legend
plt.legend(loc='best')
plt.grid(True)

# show
plt.show()