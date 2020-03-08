import math
x=int(input("introdu un numar intreg:"))
def A(x):
    print(abs(x)*x**3)
def B(x):
    print(math.log(x)+math.log10(x))
def C(x):
    print(math.sin(x)+math.sin(x)*math.cos(x))
def D(x):
    print(math.exp(x)+2*math.atan(x)-x)
A(x)
B(x)
C(x)
D(x)