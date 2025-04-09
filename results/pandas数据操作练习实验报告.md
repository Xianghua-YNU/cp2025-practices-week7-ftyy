# 实验报告 - Pandas 数据操作练习

## 一、实验目的
本次实验的主要目的是通过实际操作掌握Pandas库的基本使用方法，熟悉Pandas的DataFrame数据结构以及对数据的处理过程。

## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
说明你使用的读取数据的函数和过程。
'''
def load_data():
    """任务1: 读取数据文件"""
    return pd.read_csv('data/data.csv')
'''
使用pd.read_csv()函数读取CSV格式的数据文件。在代码中，我创建了load_data()函数专门用于数据读取
### 任务 2: 查看数据基本信息
描述如何查看数据的基本信息。
使用DataFrame的info()方法查看数据的基本信息，包括列名、非空值数量、数据类型等：
'''
def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("数据基本信息：")
    data.info()
'''
### 任务 3: 处理缺失值
说明你找出缺失值列和填充缺失值的方法。
首先找出包含缺失值的列,对数值型列使用均值填充缺失值
'''
def handle_missing_values(data):
    """任务3: 处理缺失值"""
    missing_columns = data.columns[data.isnull().any()].tolist()
    for col in missing_columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
    return data
'''
### 任务 4: 数据统计分析
说明你计算数值列均值、中位数和标准差的方法。
对数值列用模块计算均值、中位数和标准差：
'''
def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    numeric_columns = data.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        mean_value = data[col].mean()
        median_value = data[col].median()
        std_value = data[col].std()
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")
'''
### 任务 5: 数据可视化
描述你选择的数值列和绘制直方图的过程。
使用Matplotlib绘制成绩列的直方图：
'''
def visualize_data(data, column_name='成绩'):
    """任务5: 数据可视化"""
    data[column_name].plot.hist()
    plt.show()
'''
### 任务 6: 数据保存
说明你保存处理后数据的方法。
'''
def save_processed_data(data):
    """任务6: 保存处理后的数据"""
    data.to_csv('processed_data.csv', index=False)
'''
## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

### 任务 1: 读取数据
展示读取的数据的基本信息（如列名、行数等）。
成功读取包含5行4列的数据，列名分别为：姓名、年龄、成绩、城市。
### 任务 2: 查看数据基本信息
粘贴数据的基本信息输出。
数据基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   姓名      5 non-null      object
 1   年龄      4 non-null      float64
 2   成绩      5 non-null      float64
 3   城市      5 non-null      object
dtypes: float64(2), object(2)
memory usage: 292.0+ bytes
### 任务 3: 处理缺失值
说明处理后缺失值的情况。
成功处理了年龄列的缺失值，使用均值26.25进行了填充。
### 任务 4: 数据统计分析
列出数值列的均值、中位数和标准差。
年龄 列的均值: 26.25, 中位数: 26.25, 标准差: 3.031088913245535
成绩 列的均值: 86.8, 中位数: 88.0, 标准差: 5.227332015474051
### 任务 5: 数据可视化
插入绘制的直方图。
<img width="437" alt="image" src="https://github.com/user-attachments/assets/fbb34a05-3f2a-4a6e-b9ab-0852de3ab07c" />

### 任务 6: 数据保存
说明保存的文件路径和文件名。
src/processed_data.csv
## 四、总结
总结本次实验的收获和体会，分析遇到的问题及解决方法，对 Pandas 数据操作的理解和认识。
通过本次实验，我掌握了Pandas库的基本操作流程，包括数据读取、清洗、分析和可视化。特别是学会了如何处理缺失值，这是实际数据分析工作中经常遇到的问题。

遇到的问题及解决方法
问题：文件路径没设置好，读取时遇到问题
解决：设置成相对路径

Pandas提供了非常强大的数据操作功能，特别是DataFrame结构非常适合处理表格型数据。通过这次实验，我认识到Pandas不仅能够高效地处理数据，还能与其他库（如Matplotlib）无缝配合，实现数据的可视化分析。    
