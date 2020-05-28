import matplotlib.pyplot as plt

# 折线图
inputValues = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.title("折线图") # 设置标题
plt.xlabel("Value", fontsize= 10)   #设置x轴和x轴标签
plt.ylabel("Square of Value", fontsize=10) # 设置y轴与y轴标签
plt.tick_params(axis= 'both', labelsize = 10)   # 刻度标记的大小
plt.plot(inputValues, squares, linewidth=2)
plt.show()
