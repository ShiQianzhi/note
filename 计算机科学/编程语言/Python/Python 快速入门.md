# Python 快速入门

## 1. 环境准备

### 检查 Python 安装

```bash
# 检查 Python 3 版本
python3 --version

# 检查 Python 2 版本（已废弃）
python --version
```

### macOS 安装 Python

```bash
# 使用 Homebrew 安装
brew install python3

# 验证安装
python3 --version
```

### 创建虚拟环境

```bash
# 创建项目目录
mkdir myproject && cd myproject

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 退出虚拟环境
deactivate
```

## 2. 基础语法

### 第一个程序

```python
# hello.py
print("Hello, World!")
```

```bash
python3 hello.py
```

### 注释

```python
# 单行注释

"""
多行注释
这是多行注释
"""

'''
也可以用单引号
'''
```

### 缩进

Python 使用缩进表示代码块，**不要混合使用空格和制表符**！

```python
if True:
    print("正确缩进")
    print("同一代码块")
else:
    print("错误缩进")
```

## 3. 变量与数据类型

### 变量定义

```python
# 不需要声明类型
name = "Python"
age = 2024
pi = 3.14159
is_active = True
```

### 基本数据类型

| 类型 | 示例 | 说明 |
|------|------|------|
| int | `42`, `-10` | 整数 |
| float | `3.14`, `2.5e10` | 浮点数 |
| str | `"hello"`, `'world'` | 字符串 |
| bool | `True`, `False` | 布尔值 |
| None | `None` | 空值 |

### 字符串操作

```python
# 字符串拼接
greeting = "Hello" + " " + "Python"

# 字符串格式化
name = "Alice"
print(f"Hello, {name}!")  # f-string（推荐）
print("Hello, %s!" % name)  # 旧式格式化
print("Hello, {}!".format(name))  # str.format

# 字符串方法
s = "  Hello Python  "
s.strip()  # 去除首尾空格
s.lower()  # 转小写
s.upper()  # 转大写
s.replace("Python", "World")  # 替换
```

## 4. 控制流程

### 条件语句

```python
age = 18

if age < 18:
    print("未成年")
elif age >= 18 and age < 65:
    print("成年")
else:
    print("老年")
```

### 循环语句

**for 循环：**

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历范围
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

**while 循环：**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**循环控制：**

```python
for i in range(10):
    if i == 3:
        continue  # 跳过当前迭代
    if i == 7:
        break  # 跳出循环
    print(i)
```

## 5. 数据结构

### 列表 (List)

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# 访问元素
print(numbers[0])   # 第一个元素
print(numbers[-1])  # 最后一个元素

# 切片
print(numbers[1:4])  # [2, 3, 4]
print(numbers[:3])   # [1, 2, 3]
print(numbers[2:])   # [3, 4, 5]

# 修改元素
numbers[0] = 10

# 添加元素
numbers.append(6)        # 末尾添加
numbers.insert(2, 2.5)   # 指定位置插入

# 删除元素
numbers.remove(3)        # 删除值
del numbers[0]           # 删除索引

# 常用方法
len(numbers)      # 长度
sum(numbers)      # 求和
sorted(numbers)   # 排序
```

### 字典 (Dictionary)

```python
# 创建字典
person = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}

# 访问值
print(person["name"])
print(person.get("age"))

# 修改值
person["age"] = 26

# 添加键值对
person["email"] = "alice@example.com"

# 删除键值对
del person["city"]

# 遍历字典
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

### 元组 (Tuple)

```python
# 创建元组（不可变）
point = (3, 4)
colors = ("red", "green", "blue")

# 访问元素
print(point[0])

# 解包
x, y = point
print(x, y)
```

### 集合 (Set)

```python
# 创建集合（无序，不重复）
fruits = {"apple", "banana", "cherry"}

# 添加元素
fruits.add("orange")

# 删除元素
fruits.remove("banana")

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
a.union(b)        # {1, 2, 3, 4, 5}
a.intersection(b) # {3}
a.difference(b)   # {1, 2}
```

## 6. 函数

### 定义函数

```python
def greet(name):
    """打招呼函数"""
    return f"Hello, {name}!"

# 调用函数
print(greet("Python"))
```

### 参数

```python
# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 可变参数
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4))  # 10

# 关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
```

### 返回值

```python
def calculate(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = calculate(10, 5)
```

## 7. 面向对象

### 类与对象

```python
class Person:
    # 类属性
    species = "Homo sapiens"
    
    # 构造方法
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
    
    # 方法
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    # 类方法
    @classmethod
    def get_species(cls):
        return cls.species

# 创建对象
person = Person("Alice", 25)

# 访问属性和方法
print(person.name)
print(person.greet())
print(Person.get_species())
```

### 继承

```python
class Student(Person):
    def __init__(self, name, age, grade):
        # 调用父类构造方法
        super().__init__(name, age)
        self.grade = grade
    
    def study(self):
        return f"{self.name} is studying in grade {self.grade}"

student = Student("Bob", 15, 9)
print(student.greet())   # 继承父类方法
print(student.study())   # 子类特有方法
```

## 8. 模块与包

### 导入模块

```python
# 导入标准库
import math
print(math.pi)
print(math.sqrt(16))

# 导入特定函数
from math import pi, sqrt

# 别名
import numpy as np
```

### 创建模块

```python
# utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

```python
# main.py
import utils
print(utils.add(2, 3))
```

## 9. 文件操作

### 读取文件

```python
# 方式一：手动关闭
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# 方式二：自动关闭（推荐）
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 逐行读取
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### 写入文件

```python
# 写入（覆盖）
with open("output.txt", "w") as file:
    file.write("Hello, Python!")

# 追加
with open("output.txt", "a") as file:
    file.write("\nWelcome to Python!")
```

## 10. 异常处理

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 捕获特定异常
    print("不能除以零")
except Exception as e:
    # 捕获所有异常
    print(f"发生错误: {e}")
else:
    # 没有异常时执行
    print(f"结果: {result}")
finally:
    # 无论如何都会执行
    print("执行完毕")
```

## 11. 常用内置函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `print()` | 打印输出 | `print("Hello")` |
| `len()` | 长度 | `len([1,2,3])` |
| `type()` | 类型 | `type(42)` |
| `range()` | 范围 | `range(5)` |
| `sum()` | 求和 | `sum([1,2,3])` |
| `sorted()` | 排序 | `sorted([3,1,2])` |
| `max()` | 最大值 | `max([1,2,3])` |
| `min()` | 最小值 | `min([1,2,3])` |
| `str()` | 转字符串 | `str(42)` |
| `int()` | 转整数 | `int("42")` |
| `float()` | 转浮点数 | `float("3.14")` |

## 12. 实践练习

### 练习 1：计算斐波那契数列

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
```

### 练习 2：猜数字游戏

```python
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("猜一个数字 (1-100): "))
    if guess < secret_number:
        print("太小了！")
    elif guess > secret_number:
        print("太大了！")
    else:
        print(f"恭喜！你猜对了，答案是 {secret_number}")
        break
```

### 练习 3：统计文件词频

```python
with open("example.txt", "r") as file:
    text = file.read().lower()
    words = text.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
```

## 13. 学习资源

- **官方文档**: [docs.python.org](https://docs.python.org/3/)
- **Python 教程**: [python.org/tutorial](https://docs.python.org/3/tutorial/)
- **在线练习**: LeetCode、HackerRank
- **书籍推荐**: 《Python 编程：从入门到实践》、《流畅的 Python》