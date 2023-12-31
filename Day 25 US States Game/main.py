import turtle
import pandas


def goto_location(state_name):
    t = turtle.Turtle()
    t.hideturtle()
    state_data = states_data[states_data.state == state_name]
    t.penup()
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())


screen = turtle.Screen()
screen.title("Day 25 US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pandas.read_csv("50_states.csv")
all_states_list = states_data.state.to_list()
states_entered = 0
total_states = len(states_data)
guessed_states = []
# game_is_on = True

while len(guessed_states) < total_states:
    user_answer = screen.textinput(title =f"Name the US States {states_entered}/{total_states}",
                                   prompt="Enter State:").title()
    if user_answer in all_states_list:
        guessed_states.append(user_answer)
        goto_location(user_answer)
        states_entered += 1

    if user_answer.lower() == "q" or user_answer.lower() == "exit":
        break
missed_states = {}

if states_entered < total_states:
    for state in all_states_list:
        if state not in guessed_states:
            missed_states["States to Learn"] = [].append(state)
            goto_location(state)
    print(f"You got {states_entered} out {total_states} correct!")
else:
    print(f"Congratulations!! You got all states right. Well done!")

missed_states_df = pandas.DataFrame(missed_states)
missed_states_df.to_csv("states_to_learn.csv")

screen.exitonclick()
