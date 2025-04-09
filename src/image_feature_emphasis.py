import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    """加载应力纤维数据"""
    return np.loadtxt('data/stressFibers.txt')

def create_gauss_filter():
    """创建高斯滤波器"""
    v = np.arange(-25, 26)
    X, Y = np.meshgrid(v, v)
    return np.exp(-0.5*(X**2/5 + Y**2/45))

def create_combined_filter(gauss_filter):
    """创建组合滤波器"""
    laplace_filter = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    return sim.convolve(gauss_filter, laplace_filter)

def plot_filter_surface(filter, title):
    """绘制滤波器3D表面图"""
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.arange(filter.shape[1]), np.arange(filter.shape[0]))
    ax.plot_surface(X, Y, filter, cmap='viridis')
    ax.set_title(title)
    plt.show()

def process_and_display(stressFibers, filter, vmax_ratio=0.5):
    """处理并显示结果"""
    result = sim.convolve(stressFibers, filter)
    plt.imshow(result, vmin=0, vmax=vmax_ratio*result.max())
    plt.colorbar()
    plt.show()
    return result

def main():
    # 加载数据
    stressFibers = load_stress_fibers()
    
    # 任务(a): 创建并显示高斯滤波器
    gauss_filter = create_gauss_filter()
    plt.imshow(gauss_filter)
    plt.title('Gaussian Filter')
    plt.colorbar()
    plt.show()
    plot_filter_surface(gauss_filter, 'Gaussian Filter Surface')
    
    # 任务(b): 创建组合滤波器并比较
    combined_filter = create_combined_filter(gauss_filter)
    plt.imshow(combined_filter, origin='lower')
    plt.title('Combined Filter')
    plt.colorbar()
    plt.show()
    plot_filter_surface(combined_filter, 'Combined Filter Surface')
    
    # 任务(c): 应用垂直滤波器
    print("垂直方向处理结果:")
    process_and_display(stressFibers, combined_filter)
    
    # 任务(d): 应用水平滤波器
    combined_filter2 = sim.rotate(combined_filter, angle=90)
    print("水平方向处理结果:")
    process_and_display(stressFibers, combined_filter2, 0.4)
    
    # 选做: 45度方向滤波器
    fig = plt.figure(figsize=(12, 5))
    
    # -45度
    ax1 = fig.add_subplot(121)
    combined_filter3 = sim.rotate(combined_filter, -45)
    result3 = sim.convolve(stressFibers, combined_filter3)
    ax1.imshow(result3, vmin=0, vmax=0.5*result3.max())
    ax1.set_title('-45 Degree Filter')
    
    # +45度
    ax2 = fig.add_subplot(122)
    combined_filter4 = sim.rotate(combined_filter, 45)
    result4 = sim.convolve(stressFibers, combined_filter4)
    ax2.imshow(result4, vmin=0, vmax=0.5*result4.max())
    ax2.set_title('+45 Degree Filter')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
