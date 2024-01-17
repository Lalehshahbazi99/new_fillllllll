import turtle

# ایجاد شیء نقاشی Turtle
t = turtle.Turtle()

# رسم مثلث متساوی الضلاع
for i in range(3):
    t.forward(100)  # حرکت به جلامی به طول 100 واحد
    t.left(120)     # چرخش به چپ 120 درجه

# نمایش پنجره گرافیکی
turtle.done()
