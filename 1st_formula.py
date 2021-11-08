import tabulate
import matplotlib.pyplot as plt
import math
import numpy as np
Data=[]
data=[]
x_axis=[]
y_axis=[]
def falci(func,a,b,error_accept):
    def f(x):
        f = eval(func)
        return f
    error=b-a
    if(f(a)*f(b)>=0 and a>=b):
        print("wrong a,b")
        return
    x=a
    n = 0
    while error>=error_accept:
        data.append(n)
        n=n+1
        data.append(str(a))
        data.append(str(b))
        x = (x*f(b)-b*f(x))/(f(b)-f(x))
        data.append(str(x))
        x_axis.append(x)
        data.append(str(f(x)))
        y_axis.append(f(x))
        if f(x) == 0:
            break
        elif f(x) * f(b) < 0:
            a = x
        elif f(a) * f(x) < 0:
            b = x
        c=data.copy()
        Data.append(c)
        error=abs(b-a)
        data.clear()
    print("The root is %0.4f"%x)


falci('3*x-math.cos(x)-1',0,1,0.001)
print(tabulate.tabulate(Data,headers=['n','a','b','x','f(x)'],tablefmt='fancy_grid'))
x_axis=np.array(x_axis)
y_axis=np.array(y_axis)


plt.style.use('seaborn')
plt.plot(x_axis,y_axis,marker='*',color='deepskyblue',label=('f(x)'),linewidth='0.5')
plt.legend()
plt.title('Regular Falsi Method')
plt.xlabel('possible root values x',color='r')
plt.ylabel('function output (f(x))',color='r')
plt.show()




