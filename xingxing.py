import turtle as tu  # turtle是python中内置的画图库
import random as ra
width, height = 800, 600
int_width = int(width/2)
int_height = int(height/2)
# turtle.screensize(width,height,bg) 设置花板的大小，长宽，bg为画布颜色
# turtle.penup()：抬起画笔，此时移动画笔不会在画布上留下痕迹哦
# turtle.pendown()：放下画笔，与turtle.penup相对应，放下画笔后就可以继续画画了（放下画笔后画画会在画布上留下痕迹）
# turtle.pensize()：控制画笔的大小（可以根据需求自行定义画笔的大小哦）
# turtle.pencolor()：控制画笔的颜色（可以自己在网上查阅所有python可以使用的颜色，python里面可以用的颜色有很多的哦）
# turtle.hideturtle()：隐藏画笔（隐藏画笔以后画图时画笔就看不到了）
# ①turtle.forward(x)：将画笔向前移动x个像素（x可以理解为距离）
# ②turtle.backward(x)：将画笔向后移动x个像素（x可以理解为距离）
# ③turtle.left(n)：将画笔向左旋转n度
# ④turtle.right(n)：将画笔向右旋转n度
# ⑤turtle.speed()：设置画笔画图的速度（1~10递增，0最快）
tu.setup(width, height)
tu.title("3D星空")
tu.bgcolor("black")
tu.delay(0)
# 每个星球看成一个质点，每个质点用小海龟表示，克隆小海龟生成一个个星球
t = tu.Turtle(visible=False, shape='circle')
t.pencolor("white")  # 画笔颜色
t.fillcolor("white")  # 输入填充颜色
t.penup()  # 抬起画笔
t.goto(ra.randint(int_width, width), ra.randint(-int_height, int_height))
stars = []
for i in range(99):
    star = t.clone()
    s = ra.uniform(0, 1)/3
    star.shapesize(s, s)
    star.speed(ra.randint(2, 5))
    star.setx(ra.randint(int_width, width))
    star.sety(ra.randint(-int_height, int_height))
    star.showturtle()
    stars.append(star)
# 浪漫星空，循环，当每个星球从左边消失时，我们将它重新加入右侧，继续循环
while True:
    for star in stars:
        star.setx(star.xcor()-star.speed())
        if star.xcor() < -width/2:
            star.hideturtle()  # 隐藏画笔
            star.setx(ra.randint(int_width, width))
            star.sety(ra.randint(-int_height, int_height))
            star.showturtle()
