import turtle as tu
import random as ra
import math
tu.setup(1.0, 1.0)
tu.screensize(1, 1)    # 设置画布大小
tu.bgcolor('black')  # 设置画布颜色
# 库名称.函数名(),对象可以通过库中的一些函数来创建
t = tu.Pen()
# 对象.方法名(),对象.属性名(),对象的使用方法和其属性
t.ht()               # 隐藏画笔
colors = ['SkyBlue', 'white', 'cyan', 'aqua']   # 流星的颜色列表


class Star:    # 流星类
    def __init__(self):
        self.r = ra.randint(50, 100)  # randint()生成随机整数
        self.t = ra.randint(1, 3)
        self.x = ra.randint(-1500, 1000)   # 流星的横坐标
        self.y = ra.randint(0, 500)     # 流星的纵坐标
        self.speed = ra.randint(10, 15)     # 流星移动速度
        self.color = ra.choice(colors)    # 流星的颜色  choice 函数可以用于从列表、元组、字符串等序列中随机选择一个元素。
        self.outline = 1  # 流星的大小

    def star(self):                # 画流星函数
        t.pensize(self.outline)    # 流星的大小
        t.penup()                  # 提笔
        t.goto(self.x, self.y)      # 随机位置
        t.pendown()                # 落笔
        t.color(self.color)
        t.begin_fill()  # 开始填充
        t.fillcolor(self.color)  # 输入填充颜色
        t.setheading(-30)
        t.right(self.t)
        t.forward(self.r)
        t.left(self.t)
        t.circle(self.r*math.sin(math.radians(self.t)), 180)
        t.left(self.t)
        t.forward(self.r)
        t.end_fill()

    def move(self):                    # 流星移动函数
        if self.y >= -500:            # 当流星还在画布中时
            self.y -= self.speed     # 设置上下移动速度
            self.x += 2*self.speed   # 设置左右移动速度
        else:
            self.r = ra.randint(50, 100)
            self.t = ra.randint(1, 3)
            self.x = ra.randint(-1500, 1000)
            self.y = 400
            self.speed = ra.randint(10, 15)
            self.color = ra.choice(colors)
            self.outline = 1


Stars = []            # 用列表保存所有流星
for i in range(100):
    Stars.append(Star())
while True:           # 开始绘制
    tu.tracer(0)
    t.clear()
    for i in range(100):    # 80个流星
        Stars[i].move()
        Stars[i].star()
    tu.update()
# # 虽然警告显示此代码无法访问，但是有用
# tu.mainloop()
