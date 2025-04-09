"""
电偶极子电势与电场计算与可视化模板

本模板用于计算和可视化电偶极子的电势分布和电场线。
学生需要完成标有TODO的三个函数实现。
"""

import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置

def calculate_potential(X, Y):
    """
    计算二维空间电势分布
    
    参数:
        X, Y: 二维网格坐标矩阵 (numpy.ndarray)
        
    返回:
        V: 电势值矩阵 (numpy.ndarray)
    """
    # TODO 1: 实现电势计算
    # 提示: 计算每个点到正负电荷的距离，应用电势公式
    r_pos = np.sqrt((X - pos_charge_pos[0])**2 + (Y - pos_charge_pos[1])**2)
    r_neg = np.sqrt((X - neg_charge_pos[0])**2 + (Y - neg_charge_pos[1])**2)

    # 避免除以零
    r_pos[r_pos == 0] = 1e-12
    r_neg[r_neg == 0] = 1e-12

    V = k * (q_pos / r_pos + q_neg / r_neg)
    return V
    

def calculate_electric_field(V, spacing):
    """
    通过电势梯度计算电场强度
    
    参数:
        V: 电势值矩阵 (numpy.ndarray)
        spacing: 网格间距 (float)
        
    返回:
        Ex, Ey: 电场在x和y方向的分量 (numpy.ndarray, numpy.ndarray)
    """
    # TODO 2: 实现电场计算
    # 提示: 使用np.gradient计算电势梯度，注意负号和参数顺序
    dV_dy, dV_dx = np.gradient(V, spacing, edge_order=2) 
    # 指定梯度计算时的边界处理方式。edge_order=2 使用二阶精度的方法计算梯度，能提供更高的准确性。
    Ex = -dV_dx
    Ey = -dV_dy
    return Ex, Ey
    

def main():
    """
    主函数: 计算并可视化电势和电场
    """
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)#一个包含 100 个点的等间距数组，范围从 -0.2 到 0.2
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)#生成两个二维数组，分别表示网格的 x 和 y 坐标
    spacing = x[1] - x[0]  # 网格间距

    # TODO 3: 调用计算函数并绘制结果
    # 提示: 
    # 1. 先调用calculate_potential计算电势
    # 2. 用calculate_electric_field计算电场
    # 3. 使用plt.contourf绘制电势图
    # 4. 使用plt.streamplot绘制电场线
    # 5. 添加必要的标签、图例和标题

    plt.figure(figsize=(8, 6))
    # 计算电势和电场
    V = calculate_potential(X, Y)
    Ex, Ey = calculate_electric_field(V, spacing)

    # 绘制电势分布
    plt.contourf(X, Y, V, levels=50, cmap='coolwarm')# levels参数控制等高线的数量和范围 cmap参数控制颜色映射
    plt.colorbar(label="Electric Potential (V)")
    plt.title("Electric Field and Potential of an Electric Dipole")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")

    # 绘制电场线
    plt.streamplot(X, Y, Ex, Ey, color='k', density=1.5, linewidth=0.7)# density参数控制线的密度 linewidth控制线的宽度
    plt.quiver(X[::5, ::5], Y[::5, ::5], Ex[::5, ::5], Ey[::5, ::5], color='blue', scale=5e6) # 绘制电场矢量 sxale参数控制箭头的长度和密度

    # 添加电荷位置
    plt.scatter(*pos_charge_pos, color='red', label="Positive Charge", s=100) # s参数控制点的大小
    plt.scatter(*neg_charge_pos, color='blue', label="Negative Charge", s=100)
    plt.legend() # 添加图例
    plt.show()
    
    
    
    plt.show()

if __name__ == "__main__":
    main()
