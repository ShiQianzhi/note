# Python 装饰器（Decorator）总结

装饰器是 Python 中一种强大的语法特性，用于修改或增强函数、方法或类的行为。以下是 Python 中常用的 `@` 开头装饰器的作用和使用示例：

---

## 一、标准库内置装饰器

### 1. `@staticmethod` — 静态方法

**作用**：将方法标记为静态方法，不绑定到实例或类，不需要 `self` 或 `cls` 参数。

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 调用方式
result = MathUtils.add(3, 5)  # 无需创建实例
```

### 2. `@classmethod` — 类方法

**作用**：将方法标记为类方法，绑定到类而不是实例，第一个参数是 `cls`（类本身）。

```python
class Person:
    species = "Homo sapiens"
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod
    def create(cls, name, age):
        return cls(name, age)  # 使用 cls 创建实例

print(Person.get_species())  # Homo sapiens
```

### 3. `@property` — 属性装饰器

**作用**：将方法转换为属性访问，使方法调用看起来像属性访问。

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # 5（像属性一样访问）
print(circle.area)    # 78.53975
```

**属性 setter 和 deleter**：

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("半径必须大于0")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        del self._radius

circle = Circle(5)
circle.radius = 10  # 调用 setter
del circle.radius   # 调用 deleter
```

---

## 二、`functools` 模块装饰器

### 4. `@functools.wraps` — 保留原函数元信息

**作用**：在自定义装饰器中保留被装饰函数的名称、文档字符串等元信息。

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    """Greet someone"""
    return f"Hello, {name}"

print(greet.__name__)    # greet（保留原名）
print(greet.__doc__)     # Greet someone（保留文档）
```

### 5. `@functools.lru_cache` — 缓存装饰器

**作用**：缓存函数的返回结果，避免重复计算，提升性能。

```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # 快速计算，结果被缓存
print(fibonacci.cache_info())  # CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)
```

**参数**：
- `maxsize`：缓存最大数量，`None` 表示无限制
- `typed`：是否区分参数类型

### 6. `@functools.total_ordering` — 全序比较装饰器

**作用**：为类自动生成全部比较方法（`<`, `<=`, `>`, `>=`），只需定义 `__eq__` 和一个比较方法。

```python
import functools

@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(p1 < p2)   # True
print(p1 <= p2)  # True（自动生成）
print(p1 > p2)   # False（自动生成）
```

### 7. `@functools.singledispatch` — 单分派泛型函数

**作用**：根据第一个参数的类型执行不同的函数实现。

```python
import functools

@functools.singledispatch
def process(data):
    print(f"通用处理: {data}")

@process.register(int)
def _(data):
    print(f"处理整数: {data * 2}")

@process.register(str)
def _(data):
    print(f"处理字符串: {data.upper()}")

@process.register(list)
def _(data):
    print(f"处理列表: {len(data)} 个元素")

process(42)       # 处理整数: 84
process("hello")  # 处理字符串: HELLO
process([1,2,3]) # 处理列表: 3 个元素
```

### 8. `@functools.partial` — 偏函数（非装饰器，常用工具）

**作用**：固定函数的部分参数，返回一个新函数。

```python
import functools

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

---

## 三、常见第三方库装饰器

### 9. Flask 路由装饰器

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'
```

### 10. Django 视图装饰器

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
def profile(request):
    pass

@require_http_methods(["GET", "POST"])
def handle_form(request):
    pass
```

### 11. pytest 测试装饰器

```python
import pytest

@pytest.fixture
def database():
    # 设置测试环境
    db = create_test_db()
    yield db
    # 清理测试环境
    drop_test_db(db)

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4)])
def test_double(input, expected):
    assert input * 2 == expected
```

### 12. dataclass 装饰器

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Beijing"

person = Person("Alice", 25)
print(person)  # Person(name='Alice', age=25, city='Beijing')
```

---

## 四、自定义装饰器

### 基础自定义装饰器

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回 {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# 输出：
# 调用 add
# add 返回 8
```

### 带参数的装饰器

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    return "Hello"

print(say_hello())  # ['Hello', 'Hello', 'Hello']
```

### 类装饰器

```python
class Timer:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} 耗时 {end-start:.4f} 秒")
        return result

@Timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # slow_function 耗时 1.0012 秒
```

---

## 五、装饰器使用场景总结

| 装饰器 | 主要用途 |
|--------|----------|
| `@staticmethod` | 定义无需实例的工具方法 |
| `@classmethod` | 定义工厂方法或类级操作 |
| `@property` | 将方法转为属性访问，实现数据封装 |
| `@functools.wraps` | 自定义装饰器时保留原函数元信息 |
| `@functools.lru_cache` | 缓存计算结果，优化性能 |
| `@functools.total_ordering` | 自动生成比较方法 |
| `@functools.singledispatch` | 实现基于类型的函数重载 |
| `@dataclass` | 自动生成数据类的特殊方法 |

装饰器是 Python 中的高级特性，掌握它们可以让代码更简洁、更具可读性和可维护性。