import matplotlib.pyplot as plt


def fx(x):
    return (x**3) - (6 * x**2) + (x + 5)


def yx(x):
    return (x - 2)**2 - 6


# interval, number of points and step
start = -2
stop = 6
n = 100
step = (stop - start) / (n - 1)

# arg values and funcion values
xlist = [start + step * i for i in range(n)]
flist = [fx(x) for x in xlist]
ylist = [yx(x) for x in xlist]

# build lines
line_f = plt.plot(xlist, flist, label='f(x)')
line_y = plt.plot(xlist, ylist, label='y(x)')

# styles
plt.setp(line_f, color='blue', linewidth=2)
plt.setp(line_y, color='red', linewidth=2)

# spines
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# show legend
plt.legend(loc='best')

# show
plt.show()
