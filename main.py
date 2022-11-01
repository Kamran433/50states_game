import turtle
from turtle import Screen, Turtle
import pandas
screen = Screen()
turtle.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
jenny = Turtle()
jenny.hideturtle()
jenny.penup()
jenny.speed("fastest")
score = Turtle()
score.hideturtle()
score.speed("fastest")
score.penup()
score.goto(280, 280)
cond = True
m = True
# answer = screen.textinput(title = "U.S. States Game", prompt = "What's another state's name?")
states = pandas.read_csv("50_states.csv")
place = states["state"]
cordx = states["x"]
cordy = states["y"]
cordx.to_list()
cordy.to_list()
count = 0
place.to_list()
box = []
# j = states.DataFrame
# print(j)
# answer = screen.textinput(title="U.S. States Game", prompt="What's another state's name?")
while cond:
  answer = screen.textinput(title="U.S. States Game", prompt="What's another state's name?")
  for i in range(50):
      # while m is True:
          score.write(f"Score : {count}", align="center", font=("Arial", 30, "normal"))
          if answer == place[i].lower():
              place[i] = "none"
              jenny.goto(cordx[i], cordy[i])
              jenny.write(f"{answer}", align="center", font=("Arial", 10, "normal"))
              count+=1
              score.clear()
          if answer == "Exit":
              if place[i] != "none":
                  box.append(place[i])
                  miss = pandas.DataFrame(box)
                  miss.to_csv("missed_states.csv")
              cond = False
          if count == 51:
              jenny.goto(0,0)
              jenny.write("You Won!", align="center", font=("Arial", 40, "bold"))
              cond = False



screen.exitonclick()