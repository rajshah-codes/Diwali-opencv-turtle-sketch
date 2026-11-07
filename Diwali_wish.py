import cv2
import numpy as np
import turtle

img_path="assets/image.png"
image=cv2.imread(img_path)

img_height,img_width,img_channel=image.shape
print(f"The actual height of this image is: {img_height}")
print(f"The actual width of this image is: {img_width}")
target_width=900
target_height=490

image=cv2.resize(image,(target_width,target_height))
lakshmiji_img=image[:target_height, :target_width//2]
ganeshji_img=image[:target_height, target_width//2:]

cv2.imwrite("lakshmiji.gif",lakshmiji_img)
cv2.imwrite("ganeshji.gif",ganeshji_img)

window=turtle.Screen()
window.setup(width=960,height=550)
window.bgcolor("white")
window.title("Diwali Wish By Raj Shah")
window.register_shape("lakshmiji.gif")
window.register_shape("ganeshji.gif")

t=turtle.Turtle()
turtle.colormode(255)
turtle.tracer(20,5)
t.hideturtle()
t.speed(0)


def top_to_bottom(contours):
    return contours[0][0][1]

def draw_god_godess(half_img, x_offset,nameGif,x_center):
    gray=cv2.cvtColor(half_img,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,60,160)
    contours,hierarchy=cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    contours=sorted(contours,key=top_to_bottom)
    t.pencolor("black")
    t.pensize(2)

    step_count=0
    for line in contours:
        if len(line)<15:
            continue
        first_x=line[0][0][0]+x_offset
        first_y=line[0][0][1]
        turtle_x=first_x-(target_width/2)
        turtle_y=(target_height/2)-first_y

        t.penup()
        t.goto(turtle_x,turtle_y)
        t.pendown()

        for i in line:
            px=i[0][0]+x_offset
            py=i[0][1]
            tx=px-(target_width/2)
            ty=(target_height/2)-py
            t.goto(tx,ty)

            step_count+=1
            if step_count%40==0:
                turtle.update()
    t.clear()

    color_turtle=turtle.Turtle()
    color_turtle.hideturtle()
    color_turtle.penup()
    color_turtle.goto(x_center,0)
    color_turtle.shape(nameGif)
    color_turtle.stamp()
    turtle.update()
draw_god_godess(lakshmiji_img,0,"lakshmiji.gif",-225)
draw_god_godess(ganeshji_img,target_width//2,"ganeshji.gif",225)

def write_text(x,y,text,text_size,border_color,fill_color):
    font_style=("Nirmala UI",text_size,"bold")
    t.penup()
    for i in [3,4]:
        t.hideturtle()
        t.pencolor("#451A03")
        t.goto(x+i,y-i)
        t.write(text,align="center",font=font_style)
    turtle.update()
    for x1 in [-2,0,2]:
        for y1 in [-2,0,2]:
            t.penup()
            t.goto(x+x1,y+y1)
            t.pencolor(border_color)
            t.write(text,align="center",font=font_style)
    turtle.update()
    t.goto(x,y)
    t.pencolor(fill_color)
    t.write(text,align="center",font=font_style)
    turtle.update()

top_y=(target_height/2)-95
syllables=[
        (-135,"शु","#7F1D1D","#EF4444"),   
        (-85,"भ", "#9A3412","#F97316"),   
        (-10,"दी","#831843","#EC4899"),   
        (50,"पा","#78350F","#F59E0B"),   
        (105,"व","#581C87","#A855F7"),   
        (155,"ली","#065F46","#10B981"), 
]

for x,text,brdr_color,fl_color in syllables:
    write_text(x,top_y,text,42,brdr_color,fl_color)
    turtle.time.sleep(0.18)
t.penup()
middle_x=8
om_y=(target_height/2)-255
t.goto(middle_x,om_y)
t.pendown()
write_text(middle_x,om_y,"ॐ",78,"#7C2D12","#FF5722")

turtle.update()
turtle.done()











