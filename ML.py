# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import LinearRegression
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)


def runplt():
    plt.figure()
    plt.title('披萨价格与直径数据', fontproperties=font)
    plt.xlabel('直径（英寸）', fontproperties=font)
    plt.ylabel('价格（美元）', fontproperties=font)
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt


plt = runplt()
x = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
x2 = [[0], [10], [14], [25]]
model = LinearRegression()
model.fit(x, y)
y2 = model.predict(x2)
plt.plot(x, y, 'k.')
plt.plot(x2, y2, 'g-')
plt.show()
