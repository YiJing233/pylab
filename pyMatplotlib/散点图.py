import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.title("散点图")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.xlabel("Value", fontsize= 10)   #设置x轴和x轴标签
plt.ylabel("Square of Value", fontsize=10) # 设置y轴与y轴标签
# plt.scatter(x_values, y_values, edgecolors= '#FF1231', s=40) # 指定位置与大小与线的颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40) #指定一个渐变色
plt.tick_params(axis='both', which='major', labelsize=14) # 刻度标记和标记大小
plt.axis([0, 1100, 0, 1100000]) # 设置横纵轴
plt.show()


