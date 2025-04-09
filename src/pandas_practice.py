import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的CSV文件。
    """
    data = {
        "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
        "年龄": [18, 19, 20, 21, None],
        "成绩": [85, 90, None, 78, 88],
        "城市": ["北京", "上海", "广州", "深圳", None]
    }
    df = pd.DataFrame(data)
    df.to_csv("students.csv", index=False, encoding="utf-8")
    print("学生信息已保存为 students.csv 文件。")

def load_data():
    """任务1: 读取数据文件"""
    try:
        data = pd.read_csv("data.csv", encoding="utf-8")
        print("数据加载成功！")
        return data
    except FileNotFoundError:
        print("文件未找到，请先运行 creat_frame() 函数创建数据文件。")
        return None

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("数据基本信息：")
    print(data.info())
    print("\n数据预览：")
    print(data.head())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    print("\n处理缺失值...")
    data["年龄"].fillna(data["年龄"].mean(), inplace=True)
    data["成绩"].fillna(data["成绩"].mean(), inplace=True)
    data["城市"].fillna("未知", inplace=True)
    print("缺失值已处理。")
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    print("\n数值列统计分析：")
    print(data.describe())

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    print(f"\n绘制 {column_name} 的直方图...")
    plt.hist(data[column_name], bins=5, color='skyblue', edgecolor='black')
    plt.title(f"{column_name} 分布直方图")
    plt.xlabel(column_name)
    plt.ylabel("频数")
    plt.grid(alpha=0.3)
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    data.to_csv("processed_students.csv", index=False, encoding="utf-8")
    print("处理后的数据已保存为 processed_students.csv 文件。")

def main():
    """主函数，执行所有数据处理流程"""
    # 创建数据文件
    creat_frame()
    
    # 加载数据
    data = load_data()
    if data is None:
        return
    
    # 显示基本信息
    show_basic_info(data)
    
    # 处理缺失值
    data = handle_missing_values(data)
    
    # 统计分析
    analyze_statistics(data)
    
    # 数据可视化
    visualize_data(data, column_name="成绩")
    
    # 保存处理后的数据
    save_processed_data(data)

if __name__ == "__main__":
    main()
