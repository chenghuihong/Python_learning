import pygame
import random
# 初始化
pygame.init()  # 初始化pygame的各种模块和功能
pygame.display.set_caption("黑客帝国")  # 设置窗口标题
font = pygame.font.SysFont('宋体', 25)  # 创建字体对象，设置字体形式和大小
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 创建一个窗口显示界面，全屏
screen = pygame.display.set_mode((800, 600))
screenwidth = screen.get_width()  # 获取屏幕的宽度
screenheight = screen.get_height()  # 获取屏幕的高度
surface = pygame.Surface((screenwidth, screenheight), pygame.SRCALPHA)  # 创建Surface对象用于在屏幕上绘制透明效果
# 对Surface对象进行转换和填充颜色
pygame.Surface.convert(surface)
surface.fill((0, 0, 0, 10))
screen.fill((0, 0, 0, 10))  # 在屏幕上填充黑色背景
# 内容，chr(i)字符串解密：将ASCII码值转换为字符
str = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(97, 123)]  # 定义包含数字和小写字母的列表，
texts = [font.render(i, True, (0, 255, 0)) for i in str]  # render将数据或模板转换为最终的可视化输出或渲染到屏幕上，并放入新的列表
lst = list(range(99))  # 创建一个0-98的整数列表
# 进入游戏循环
while True:
    for event in pygame.event.get():  # 获取所有的事件
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(50)  # 设置延迟时间为50毫秒，控制字符下落速度
    screen.blit(surface, (0, 0))  # 在屏幕上绘制透明背景
    # 遍历整个整数列表，每次循环选择随机字符，并在对应位置绘制到屏幕
    for i in range(len(lst)):
        text = random.choice(texts)
        screen.blit(text, (i * 20, lst[i] * 20))
        lst[i] += 1  # 整数元素加1，实现字符下落效果
        if random.random() < 0.05:  # 以5%的概率将整数列表的元素重置为0.实现字符重新下落效果
            lst[i] = 0
    pygame.display.flip()   # 绘制图形，更新屏幕显示
