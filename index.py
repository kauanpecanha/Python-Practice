%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1896,1900, 1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008])
t = np.array([12.0,11,11,11.2,10.8,10.8,10.8,10.6,10.80,10.3,10.3,10.30,10.40,10.50,10.2,10.0,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85,9.69])
c = np.polyfit(x, t, 1)
y_fit = c[0]*x + c[1] 
xt = x*t


plt.plot(x, t)
plt.plot(x, y_fit, 'r--')
plt.title("Plotagem do gráfico")
plt.xlabel("x")
plt.ylabel("t")
plt.show() #plotagem do gráfico

#encontrar o parâmetro xt