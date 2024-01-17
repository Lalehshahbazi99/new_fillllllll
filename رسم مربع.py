
import turtle
# ایجاد یک شیء از کلاس Turtle
t = turtle.Turtle()
# حلقه‌ای برای رسم یک مربع
for _ in range(4):
    t.forward(100)  # حرکت به جلو 100 واحد
    t.left(90)      # چرخش به چپ 90 درجه
# نگه داشتن پنجره‌ی نمایش باز
turtle.done()
