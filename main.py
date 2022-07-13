import colorgram
import turtle
from random import choice

def main():
  turtle.colormode(255)
  timmy = turtle.Turtle()
  timmy.hideturtle()
  timmy.setpos(-200, -150)
  
  rgb_colors = []
  color_list = colorgram.extract("Damien Hirst.jpeg", 10)
  for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
  print(rgb_colors)

  rows = 10
  columns = 10

  for row in range(rows):
    for column in range(columns):
      timmy.pendown()
      timmy.dot(20, choice(rgb_colors))
      timmy.penup()
      timmy.fd(50)
  if row % 2 == 0:
    timmy.right(90)
    timmy.fd(50)
    timmy.right(90)
  else:
    timmy.left(90)
    timmy.fd(50)
    timmy.left(90)

  screen = turtle.Screen()
  screen.exitonclick()
  
    

  main()