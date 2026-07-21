# C 语言快速入门

## 1. 环境准备

C 语言是编译型语言，需要通过编译器将源代码转换为可执行文件。常用的编译器有 GCC（GNU Compiler Collection）和 Clang。

### 检查编译器安装

```bash
# 检查 GCC 版本
gcc --version

# 检查 Clang 版本
clang --version
```

### macOS 安装编译器

```bash
# 通过 Xcode Command Line Tools 安装（包含 Clang）
xcode-select --install

# 验证安装
clang --version
gcc --version   # macOS 上 gcc 通常是 clang 的别名
```

### Linux 安装 GCC

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install build-essential

# CentOS / RHEL
sudo yum groupinstall "Development Tools"

# 验证安装
gcc --version
```

### Windows 安装

推荐使用 MinGW-w64 或 MSYS2，也可以使用 WSL (Windows Subsystem for Linux)。

## 2. 第一个程序

### Hello, World!

创建文件 `hello.c`：

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### 编译与运行

```bash
# 编译（默认生成 a.out 或 a.exe）
gcc hello.c

# 运行
./a.out          # macOS / Linux
# 输出: Hello, World!

# 指定输出文件名
gcc hello.c -o hello
./hello
```

### 程序结构解析

- `#include <stdio.h>` — 预处理指令，引入标准输入输出头文件，提供 `printf` 等函数
- `int main()` — 程序入口函数，每个 C 程序有且仅有一个 `main` 函数
- `printf(...)` — 格式化输出函数，`\n` 表示换行
- `return 0` — 函数返回值，0 表示程序正常退出

## 3. 基本语法

### 注释

```c
// 单行注释

/*
   多行注释
   这是多行注释
*/
```

### 标识符与关键字

**标识符命名规则：**
- 由字母、数字、下划线组成
- 不能以数字开头
- 区分大小写
- 不能使用 C 关键字

**常用关键字（32 个）：**

| 类别 | 关键字 |
|------|--------|
| 数据类型 | `int`, `char`, `float`, `double`, `void`, `short`, `long`, `signed`, `unsigned`, `enum`, `struct`, `union`, `typedef` |
| 控制语句 | `if`, `else`, `switch`, `case`, `default`, `for`, `while`, `do`, `break`, `continue`, `goto`, `return` |
| 存储类 | `auto`, `static`, `extern`, `register` |
| 其他 | `const`, `volatile`, `sizeof` |

### 语句与分号

C 语言中每条语句以分号 `;` 结尾：

```c
int a = 10;   // 声明并初始化变量
printf("%d", a);  // 函数调用语句
```

## 4. 数据类型

### 基本数据类型

| 类型 | 大小（典型） | 取值范围 | 说明 |
|------|-------------|----------|------|
| `char` | 1 字节 | -128 ~ 127 | 字符型 |
| `unsigned char` | 1 字节 | 0 ~ 255 | 无符号字符 |
| `short` | 2 字节 | -32768 ~ 32767 | 短整型 |
| `int` | 4 字节 | -2^31 ~ 2^31-1 | 整型 |
| `unsigned int` | 4 字节 | 0 ~ 2^32-1 | 无符号整型 |
| `long` | 4/8 字节 | 平台相关 | 长整型 |
| `long long` | 8 字节 | -2^63 ~ 2^63-1 | 长长整型 |
| `float` | 4 字节 | 约 6~7 位有效数字 | 单精度浮点 |
| `double` | 8 字节 | 约 15~16 位有效数字 | 双精度浮点 |
| `void` | - | - | 空类型 |

### sizeof 运算符

```c
#include <stdio.h>

int main() {
    printf("char:    %zu 字节\n", sizeof(char));
    printf("short:   %zu 字节\n", sizeof(short));
    printf("int:     %zu 字节\n", sizeof(int));
    printf("long:    %zu 字节\n", sizeof(long));
    printf("float:   %zu 字节\n", sizeof(float));
    printf("double:  %zu 字节\n", sizeof(double));
    return 0;
}
```

### 类型限定符

```c
const int MAX = 100;   // 常量，不可修改
volatile int flag;     // 易变变量，禁止编译器优化
```

## 5. 变量与常量

### 变量声明与初始化

```c
// 声明
int age;
float price;
char grade;

// 声明并初始化
int a = 10;
double pi = 3.14159;
char ch = 'A';

// 同时声明多个变量
int x, y, z;
int m = 1, n = 2, p = 3;
```

### 变量命名规范

```c
// 推荐：见名知意，使用下划线或小驼峰
int student_age = 20;   // 下划线式
int studentAge = 20;    // 小驼峰式（C 风格更常用下划线）

// 避免：无意义的命名
int a, b, c;
```

### 常量定义

```c
// 方式一：#define 宏定义（预处理阶段替换）
#define PI 3.14159
#define MAX_SIZE 100

// 方式二：const 关键字（编译时类型检查）
const double E = 2.71828;
const int MAX = 100;
```

> **注意**：`#define` 是文本替换，没有类型检查；`const` 有类型检查，更安全，推荐优先使用。

## 6. 运算符

### 算术运算符

```c
int a = 10, b = 3;

a + b;    // 13  加法
a - b;    // 7   减法
a * b;    // 30  乘法
a / b;    // 3   整数除法（截断小数）
a % b;    // 1   取余（仅用于整数）

a++;      // 11  后置自增
++a;      // 12  前置自增
a--;      // 11  后置自减
--a;      // 10  前置自减
```

### 关系运算符

```c
int a = 5, b = 3;

a == b;   // 0 (假)  等于
a != b;   // 1 (真)  不等于
a > b;    // 1       大于
a < b;    // 0       小于
a >= b;   // 1       大于等于
a <= b;   // 0       小于等于
```

> C 语言中，0 表示假，非 0 表示真。

### 逻辑运算符

```c
int a = 1, b = 0;

a && b;   // 0  逻辑与（两边都为真才为真）
a || b;   // 1  逻辑或（一边为真即为真）
!a;       // 0  逻辑非（取反）
```

> **短路求值**：`&&` 左边为假时右边不执行；`||` 左边为真时右边不执行。

### 位运算符

```c
unsigned char a = 0b1100;  // 12
unsigned char b = 0b1010;  // 10

a & b;     // 0b1000 (8)   按位与
a | b;     // 0b1110 (14)  按位或
a ^ b;     // 0b0110 (6)   按位异或
~a;        // 按位取反
a << 1;    // 0b10000 (24) 左移
a >> 1;    // 0b0110 (6)   右移
```

### 赋值运算符

```c
int a = 10;

a += 5;    // a = a + 5;    → 15
a -= 3;    // a = a - 3;    → 12
a *= 2;    // a = a * 2;    → 24
a /= 4;    // a = a / 4;    → 6
a %= 4;    // a = a % 4;    → 2
a &= 3;    // a = a & 3;
a |= 5;    // a = a | 5;
a <<= 1;   // a = a << 1;
```

### 三元运算符

```c
// 条件 ? 表达式1 : 表达式2
// 条件为真，返回表达式1；否则返回表达式2

int a = 10, b = 20;
int max = (a > b) ? a : b;   // max = 20
```

### 运算符优先级（从高到低）

| 优先级 | 运算符 | 说明 |
|--------|--------|------|
| 1 | `()` `[]` `->` `.` | 括号、下标、成员访问 |
| 2 | `!` `~` `++` `--` `+` `-` `*` `&` `sizeof` | 单目运算符 |
| 3 | `*` `/` `%` | 算术乘除 |
| 4 | `+` `-` | 算术加减 |
| 5 | `<<` `>>` | 位移 |
| 6 | `<` `<=` `>` `>=` | 关系 |
| 7 | `==` `!=` | 相等 |
| 8 | `&` | 按位与 |
| 9 | `^` | 按位异或 |
| 10 | `|` | 按位或 |
| 11 | `&&` | 逻辑与 |
| 12 | `||` | 逻辑或 |
| 13 | `?:` | 三元 |
| 14 | `=` `+=` `-=` 等 | 赋值 |
| 15 | `,` | 逗号 |

## 7. 输入与输出

### printf 格式化输出

```c
#include <stdio.h>

int main() {
    int age = 25;
    float height = 1.75f;
    char grade = 'A';
    char name[] = "Tom";

    printf("姓名: %s\n", name);
    printf("年龄: %d\n", age);
    printf("身高: %.2f 米\n", height);
    printf("等级: %c\n", grade);
    printf("十六进制: 0x%X\n", 255);
    printf("指针地址: %p\n", &age);

    return 0;
}
```

**常用格式符：**

| 格式符 | 说明 | 示例 |
|--------|------|------|
| `%d` / `%i` | 十进制整数 | `printf("%d", 42)` |
| `%f` | 浮点数 | `printf("%.2f", 3.14)` |
| `%c` | 字符 | `printf("%c", 'A')` |
| `%s` | 字符串 | `printf("%s", "hello")` |
| `%x` / `%X` | 十六进制 | `printf("%x", 255)` |
| `%o` | 八进制 | `printf("%o", 8)` |
| `%p` | 指针 | `printf("%p", &a)` |
| `%%` | 百分号本身 | `printf("100%%")` |

### scanf 格式化输入

```c
#include <stdio.h>

int main() {
    int age;
    float height;
    char name[50];

    printf("请输入姓名: ");
    scanf("%s", name);        // 字符串不需要 &

    printf("请输入年龄: ");
    scanf("%d", &age);        // 基本类型需要 &（取地址）

    printf("请输入身高: ");
    scanf("%f", &height);

    printf("你好，%s！年龄 %d，身高 %.2f 米\n", name, age, height);

    return 0;
}
```

> **注意**：`scanf` 读取字符串时遇到空格会停止。如需读取整行，使用 `fgets`。

### 字符输入输出

```c
#include <stdio.h>

int main() {
    char ch;

    ch = getchar();     // 读取一个字符
    putchar(ch);        // 输出一个字符
    putchar('\n');

    return 0;
}
```

## 8. 控制流程

### if 条件语句

```c
#include <stdio.h>

int main() {
    int score = 85;

    if (score >= 90) {
        printf("优秀\n");
    } else if (score >= 80) {
        printf("良好\n");
    } else if (score >= 60) {
        printf("及格\n");
    } else {
        printf("不及格\n");
    }

    return 0;
}
```

### switch 多分支

```c
#include <stdio.h>

int main() {
    int day = 3;

    switch (day) {
        case 1:
            printf("星期一\n");
            break;
        case 2:
            printf("星期二\n");
            break;
        case 3:
            printf("星期三\n");
            break;
        default:
            printf("其他\n");
    }

    return 0;
}
```

> **注意**：每个 `case` 后必须加 `break`，否则会"穿透"到下一个 case。

### for 循环

```c
// 输出 1~10
for (int i = 1; i <= 10; i++) {
    printf("%d ", i);
}

// 从 10 到 1 倒序
for (int i = 10; i >= 1; i--) {
    printf("%d ", i);
}

// 嵌套循环：打印九九乘法表
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        printf("%d*%d=%-2d ", j, i, i * j);
    }
    printf("\n");
}
```

### while 循环

```c
// 计算 1~100 的和
int sum = 0;
int i = 1;

while (i <= 100) {
    sum += i;
    i++;
}
printf("1+2+...+100 = %d\n", sum);
```

### do-while 循环

```c
// 至少执行一次
int i = 1;
do {
    printf("%d ", i);
    i++;
} while (i <= 10);
```

### break 与 continue

```c
// break：跳出整个循环
for (int i = 1; i <= 10; i++) {
    if (i == 5) {
        break;   // 到 5 就结束循环
    }
    printf("%d ", i);  // 输出 1 2 3 4
}

// continue：跳过当前迭代，继续下一次
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;  // 跳过偶数
    }
    printf("%d ", i);  // 输出 1 3 5 7 9
}
```

### goto 语句（慎用）

```c
#include <stdio.h>

int main() {
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (j == 5) {
                goto end_loop;   // 跳出多层循环
            }
        }
    }
end_loop:
    printf("循环结束\n");
    return 0;
}
```

## 9. 函数

### 函数定义与调用

```c
#include <stdio.h>

// 函数声明（原型），也可以直接写在 main 前面
int add(int a, int b);

int main() {
    int result = add(3, 5);
    printf("3 + 5 = %d\n", result);
    return 0;
}

// 函数定义
int add(int a, int b) {
    return a + b;
}
```

### 函数参数

```c
// 无参数、无返回值
void say_hello() {
    printf("Hello!\n");
}

// 有参数、有返回值
int max(int a, int b) {
    return (a > b) ? a : b;
}

// 无返回值
void print_sum(int a, int b) {
    printf("%d + %d = %d\n", a, b, a + b);
}
```

### 值传递与地址传递

```c
#include <stdio.h>

// 值传递：函数内修改不影响外部
void swap_by_value(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

// 地址传递（指针）：函数内修改影响外部
void swap_by_pointer(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;

    swap_by_value(x, y);
    printf("值传递: x=%d, y=%d\n", x, y);  // x=10, y=20（没变）

    swap_by_pointer(&x, &y);
    printf("地址传递: x=%d, y=%d\n", x, y);  // x=20, y=10（已交换）

    return 0;
}
```

### 函数递归

```c
// 计算阶乘 n! = n * (n-1) * ... * 1
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// 斐波那契数列
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### 静态局部变量

```c
#include <stdio.h>

void count() {
    static int counter = 0;   // 静态变量只初始化一次，保留上一次的值
    counter++;
    printf("调用次数: %d\n", counter);
}

int main() {
    count();   // 1
    count();   // 2
    count();   // 3
    return 0;
}
```

## 10. 数组

### 一维数组

```c
// 声明与初始化
int arr[5];                      // 声明 5 个 int 元素的数组（值未定义）
int nums[5] = {1, 2, 3, 4, 5};  // 完全初始化
int arr2[] = {1, 2, 3};         // 省略大小，自动推断为 3
int arr3[5] = {0};              // 全部初始化为 0

// 访问元素（下标从 0 开始）
nums[0] = 10;
printf("%d\n", nums[0]);  // 10

// 遍历数组
for (int i = 0; i < 5; i++) {
    printf("%d ", nums[i]);
}
```

### 数组大小

```c
int arr[] = {1, 2, 3, 4, 5};
int len = sizeof(arr) / sizeof(arr[0]);   // 5
```

### 二维数组

```c
// 声明与初始化
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// 访问元素
matrix[0][0] = 100;   // 第一行第一列

// 遍历二维数组
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        printf("%d ", matrix[i][j]);
    }
    printf("\n");
}
```

### 数组与函数

```c
#include <stdio.h>

// 数组作为参数，传递的是首地址，所以需要单独传长度
void print_array(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 数组在函数内可以被修改（因为传的是指针）
void square_array(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        arr[i] = arr[i] * arr[i];
    }
}

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int len = sizeof(nums) / sizeof(nums[0]);

    print_array(nums, len);     // 1 2 3 4 5
    square_array(nums, len);
    print_array(nums, len);     // 1 4 9 16 25

    return 0;
}
```

## 11. 字符串

### 字符串基础

C 语言中，字符串是以 `\0`（空字符）结尾的字符数组。

```c
// 字符串声明与初始化
char str1[] = "Hello";             // 自动添加 '\0'，大小为 6
char str2[6] = {'H', 'e', 'l', 'l', 'o', '\0'};  // 手动添加
char str3[100] = "World";          // 指定大小

// 字符串长度（不包括 '\0'）
#include <string.h>
printf("%zu\n", strlen(str1));  // 5

// 字符串大小（包括 '\0'）
printf("%zu\n", sizeof(str1));  // 6
```

### 字符串输入输出

```c
#include <stdio.h>

int main() {
    char name[50];

    // 使用 scanf（遇到空格停止）
    printf("请输入姓名: ");
    scanf("%s", name);
    printf("你好，%s\n", name);

    // 使用 fgets（读取整行，包括空格）
    char line[100];
    printf("请输入一句话: ");
    getchar();  // 吃掉上次输入留下的换行符
    fgets(line, sizeof(line), stdin);
    printf("你输入的是: %s", line);

    return 0;
}
```

### 常用字符串函数

需要引入头文件 `<string.h>`：

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello";
    char str2[] = " World";
    char str3[50];

    // 字符串拼接：strcat(dest, src)
    strcat(str1, str2);
    printf("拼接: %s\n", str1);   // Hello World

    // 字符串复制：strcpy(dest, src)
    strcpy(str3, str1);
    printf("复制: %s\n", str3);   // Hello World

    // 字符串比较：strcmp(s1, s2)
    // 返回 0 表示相等，<0 表示 s1 < s2，>0 表示 s1 > s2
    int cmp = strcmp("abc", "abc");
    printf("比较: %d\n", cmp);    // 0

    // 查找字符：strchr(s, c)
    char *p = strchr("Hello World", 'W');
    if (p) {
        printf("找到: %s\n", p);  // World
    }

    // 查找子串：strstr(haystack, needle)
    char *sub = strstr("Hello World", "World");
    if (sub) {
        printf("找到子串: %s\n", sub);  // World
    }

    return 0;
}
```

## 12. 指针

### 指针基础

指针是一个变量，存储的是另一个变量的内存地址。

```c
#include <stdio.h>

int main() {
    int a = 10;
    int *p;      // 声明一个 int 类型的指针
    p = &a;      // & 是取地址运算符，p 指向 a

    printf("a 的值: %d\n", a);          // 10
    printf("a 的地址: %p\n", &a);       // 0x...
    printf("p 的值: %p\n", p);          // 0x...（和 &a 一样）
    printf("p 指向的值: %d\n", *p);     // 10（* 是解引用运算符）

    // 通过指针修改值
    *p = 20;
    printf("修改后 a 的值: %d\n", a);   // 20

    return 0;
}
```

### 指针与数组

```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;   // 数组名是数组首元素的地址

    // 方式一：下标访问
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    // 方式二：指针访问
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(p + i));
    }

    // 方式三：指针移动
    for (int *q = arr; q < arr + 5; q++) {
        printf("%d ", *q);
    }

    return 0;
}
```

> 数组名 `arr` 是常量指针，不能修改（不能 `arr++`）；而指针变量 `p` 可以修改（可以 `p++`）。

### 指针与函数

```c
// 通过指针交换两个变量的值
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 通过指针返回多个值
void calculate(int a, int b, int *sum, int *product) {
    *sum = a + b;
    *product = a * b;
}

int main() {
    int x = 10, y = 20;
    int s, p;
    calculate(x, y, &s, &p);
    printf("和: %d, 积: %d\n", s, p);  // 和: 30, 积: 200
    return 0;
}
```

### 二级指针

```c
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;     // 一级指针
    int **pp = &p;   // 二级指针

    printf("a = %d\n", a);          // 10
    printf("*p = %d\n", *p);        // 10
    printf("**pp = %d\n", **pp);    // 10

    return 0;
}
```

### void 指针

```c
#include <stdio.h>

int main() {
    int a = 10;
    float b = 3.14f;
    void *p;   // 通用指针，可以指向任意类型

    p = &a;
    printf("%d\n", *(int *)p);   // 强制类型转换后解引用

    p = &b;
    printf("%f\n", *(float *)p);

    return 0;
}
```

### 空指针

```c
int *p = NULL;   // 空指针，不指向任何有效地址

if (p != NULL) {
    // 使用前检查指针是否有效
    printf("%d\n", *p);
}
```

## 13. 结构体与枚举

### 结构体定义与使用

```c
#include <stdio.h>
#include <string.h>

// 定义结构体类型
struct Student {
    char name[50];
    int age;
    float score;
};

int main() {
    // 声明并初始化结构体变量
    struct Student s1 = {"张三", 20, 95.5f};

    // 访问成员
    printf("姓名: %s\n", s1.name);
    printf("年龄: %d\n", s1.age);
    printf("分数: %.1f\n", s1.score);

    // 修改成员
    s1.age = 21;
    strcpy(s1.name, "李四");

    return 0;
}
```

### 结构体数组

```c
struct Student students[3] = {
    {"张三", 20, 95.5f},
    {"李四", 21, 88.0f},
    {"王五", 19, 92.5f}
};

for (int i = 0; i < 3; i++) {
    printf("%s, %d, %.1f\n", students[i].name, students[i].age, students[i].score);
}
```

### 结构体指针

```c
struct Student s = {"张三", 20, 95.5f};
struct Student *p = &s;

// 方式一：(*p).成员
printf("%s\n", (*p).name);

// 方式二：p->成员（更常用）
printf("%s\n", p->name);
printf("%d\n", p->age);
```

### typedef 简化类型名

```c
typedef struct {
    char name[50];
    int age;
} Student;   // 以后可以直接用 Student 代替 struct Student

Student s1 = {"张三", 20};
```

### 枚举类型

```c
#include <stdio.h>

// 定义枚举
enum Weekday {
    MON,    // 默认 0
    TUE,    // 1
    WED,    // 2
    THU,    // 3
    FRI,    // 4
    SAT,    // 5
    SUN     // 6
};

// 指定枚举值
enum Color {
    RED = 1,
    GREEN = 2,
    BLUE = 4
};

int main() {
    enum Weekday day = WED;
    printf("%d\n", day);  // 2

    if (day == WED) {
        printf("今天是星期三\n");
    }

    return 0;
}
```

## 14. 内存管理

### 动态内存分配

需要引入头文件 `<stdlib.h>`。

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("请输入数组大小: ");
    scanf("%d", &n);

    // 动态分配内存
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("内存分配失败！\n");
        return 1;
    }

    // 使用动态数组
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // 释放内存（必须！否则内存泄漏）
    free(arr);
    arr = NULL;   // 置空，避免野指针

    return 0;
}
```

### 常用内存函数

| 函数 | 说明 |
|------|------|
| `malloc(size)` | 分配指定字节数的内存，内容未初始化 |
| `calloc(n, size)` | 分配 n 个元素的内存，初始化为 0 |
| `realloc(ptr, size)` | 重新调整已分配内存的大小 |
| `free(ptr)` | 释放动态分配的内存 |

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // calloc：分配并初始化为 0
    int *arr = (int *)calloc(5, sizeof(int));
    // arr[0]~arr[4] 都是 0

    // realloc：扩容
    arr = (int *)realloc(arr, 10 * sizeof(int));
    // 现在数组大小是 10

    free(arr);
    arr = NULL;

    return 0;
}
```

### 内存操作函数

需要引入头文件 `<string.h>`。

```c
#include <stdio.h>
#include <string.h>

int main() {
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5];

    // memcpy：内存拷贝
    memcpy(arr2, arr1, sizeof(arr1));

    // memset：内存设置
    char buf[10];
    memset(buf, 0, sizeof(buf));   // 全部置 0
    memset(buf, 'A', 5);           // 前 5 个字节设为 'A'

    // memcmp：内存比较
    int cmp = memcmp(arr1, arr2, sizeof(arr1));  // 0（相等）

    return 0;
}
```

## 15. 文件操作

需要引入头文件 `<stdio.h>`。

### 文件指针

```c
FILE *fp;   // 文件指针
```

### 打开与关闭文件

```c
// 打开文件
FILE *fp = fopen("example.txt", "r");
if (fp == NULL) {
    printf("文件打开失败！\n");
    return 1;
}

// 使用文件...

// 关闭文件（必须！）
fclose(fp);
```

**文件打开模式：**

| 模式 | 说明 |
|------|------|
| `"r"` | 只读（文件必须存在） |
| `"w"` | 只写（文件不存在则创建，存在则清空） |
| `"a"` | 追加（文件不存在则创建，存在则在末尾追加） |
| `"r+"` | 读写（文件必须存在） |
| `"w+"` | 读写（创建/清空） |
| `"a+"` | 读+追加 |
| `"rb"` | 二进制只读 |
| `"wb"` | 二进制只写 |

### 字符读写

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("test.txt", "w");
    if (fp == NULL) return 1;

    // 写入字符
    fputc('H', fp);
    fputc('i', fp);
    fclose(fp);

    // 读取字符
    fp = fopen("test.txt", "r");
    char ch;
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }
    fclose(fp);

    return 0;
}
```

### 字符串读写

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("test.txt", "w");
    if (fp == NULL) return 1;

    // 写入字符串
    fputs("Hello, World!\n", fp);
    fputs("第二行\n", fp);
    fclose(fp);

    // 读取一行
    fp = fopen("test.txt", "r");
    char line[100];
    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%s", line);
    }
    fclose(fp);

    return 0;
}
```

### 格式化读写

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("data.txt", "w");
    if (fp == NULL) return 1;

    // 格式化写入
    fprintf(fp, "姓名: %s, 年龄: %d, 分数: %.1f\n", "张三", 20, 95.5f);
    fclose(fp);

    // 格式化读取
    fp = fopen("data.txt", "r");
    char name[50];
    int age;
    float score;
    fscanf(fp, "姓名: %[^,], 年龄: %d, 分数: %f", name, &age, &score);
    printf("%s, %d, %.1f\n", name, age, score);
    fclose(fp);

    return 0;
}
```

### 二进制文件读写

```c
#include <stdio.h>

int main() {
    int data[] = {1, 2, 3, 4, 5};

    // 写入二进制文件
    FILE *fp = fopen("data.bin", "wb");
    fwrite(data, sizeof(int), 5, fp);
    fclose(fp);

    // 读取二进制文件
    int read_data[5];
    fp = fopen("data.bin", "rb");
    fread(read_data, sizeof(int), 5, fp);
    fclose(fp);

    for (int i = 0; i < 5; i++) {
        printf("%d ", read_data[i]);
    }

    return 0;
}
```

### 文件定位

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("test.txt", "r");
    if (fp == NULL) return 1;

    // 获取当前位置
    long pos = ftell(fp);

    // 移动文件指针
    fseek(fp, 0, SEEK_SET);   // 移到文件开头
    fseek(fp, 10, SEEK_CUR);  // 从当前位置向后移 10 字节
    fseek(fp, 0, SEEK_END);   // 移到文件末尾

    // 回到文件开头
    rewind(fp);

    fclose(fp);
    return 0;
}
```

## 16. 预处理器

### #define 宏定义

```c
#include <stdio.h>

#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    printf("PI = %f\n", PI);
    printf("MAX(3,5) = %d\n", MAX(3, 5));
    return 0;
}
```

### 条件编译

```c
#include <stdio.h>

#define DEBUG 1

int main() {
#if DEBUG
    printf("调试模式\n");
#else
    printf("发布模式\n");
#endif

#ifdef _WIN32
    printf("Windows 系统\n");
#elif __APPLE__
    printf("macOS 系统\n");
#elif __linux__
    printf("Linux 系统\n");
#endif

    return 0;
}
```

### 头文件包含

```c
// 系统头文件用尖括号
#include <stdio.h>
#include <stdlib.h>

// 自定义头文件用双引号
#include "myheader.h"
```

### 头文件保护

防止头文件被重复包含：

```c
// myheader.h
#ifndef MYHEADER_H
#define MYHEADER_H

// 头文件内容...

#endif // MYHEADER_H
```

## 17. 实践练习

### 练习 1：计算斐波那契数列

```c
#include <stdio.h>

int main() {
    int n;
    printf("请输入项数: ");
    scanf("%d", &n);

    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        printf("%d ", a);
        int temp = a + b;
        a = b;
        b = temp;
    }
    printf("\n");

    return 0;
}
```

### 练习 2：冒泡排序

```c
#include <stdio.h>

void bubble_sort(int arr[], int len) {
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 3};
    int len = sizeof(arr) / sizeof(arr[0]);

    bubble_sort(arr, len);

    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```

### 练习 3：字符串反转

```c
#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    int len = strlen(str);
    int left = 0, right = len - 1;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}

int main() {
    char str[] = "Hello, World!";
    reverse_string(str);
    printf("%s\n", str);  // !dlroW ,olleH
    return 0;
}
```

### 练习 4：实现链表

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *create_node(int data) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

void print_list(Node *head) {
    Node *p = head;
    while (p != NULL) {
        printf("%d -> ", p->data);
        p = p->next;
    }
    printf("NULL\n");
}

int main() {
    Node *head = create_node(1);
    head->next = create_node(2);
    head->next->next = create_node(3);

    print_list(head);  // 1 -> 2 -> 3 -> NULL

    // 释放内存
    Node *p = head;
    while (p != NULL) {
        Node *temp = p;
        p = p->next;
        free(temp);
    }

    return 0;
}
```

## 18. 学习资源

### 官方文档与参考
- **cppreference**: [https://en.cppreference.com/w/c](https://en.cppreference.com/w/c) — 权威的 C 语言参考
- **C 标准文档**: ISO/IEC 9899

### 在线练习
- **LeetCode**: [https://leetcode.com](https://leetcode.com) — 算法练习
- **HackerRank**: [https://www.hackerrank.com](https://www.hackerrank.com) — C 语言练习

### 推荐书籍
- **《C 程序设计语言》**（K&R）— C 语言之父的经典著作
- **《C Primer Plus》** — 入门友好，内容详尽
- **《C 和指针》** — 深入理解指针与内存
- **《C 专家编程》** — 进阶读物

### 编译调试工具
- **GCC** — GNU 编译器集合
- **Clang** — LLVM 编译器前端
- **GDB** — GNU 调试器
- **Valgrind** — 内存泄漏检测工具
