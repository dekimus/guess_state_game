import turtle, pandas

image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")

sc = turtle.Screen()
sc.setup(725,500)
sc.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.color("black")
t.penup()
t.hideturtle()

on = True
score = 0
answered = []


def print_loc(x , y):
    t.goto(x, y)
    t.write(s,font=("Arial", 8 , "normal"))


while len(answered) < 50:
    answer = sc.textinput(f"Guess the state {len(answered)}/50", "What's another state's name?")
    for s in data["state"]:
        if answer == None:
            break
        if s.lower() == answer.lower() and s not in answered:
            d = data[data.state==s]
            print_loc(int(d.x),int(d.y))
            answered.append(s)
            
            

sc.mainloop()

