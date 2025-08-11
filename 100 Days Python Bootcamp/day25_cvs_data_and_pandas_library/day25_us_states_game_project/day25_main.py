import turtle
import pandas

screen = turtle.Screen()
screen.setup(750,500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)


states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()
guessed_states = []
t = turtle.Turtle()
remaining = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)} / 50 Correct ", prompt="What's state's name?").title()

    if answer_state == "Exit":
        for _ in range(len(states)):
            if states[_] not in guessed_states:
                remaining.append(states[_])
        data_dic = {
            "States": remaining
        }
        pandas.DataFrame(data_dic).to_csv("states_that_you_forget.csv")
        t.teleport(220, -230)
        t.color("red")
        t.write("Try Again", align="center", font=("Times New Roman", 50, "normal"))
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t.hideturtle()
        state_data = states_data[states_data.state == answer_state]            # index = state_data[state_data.state == answer_state].index[0]
        t.teleport(state_data.x.item(),state_data.y.item())                    # x_cords = state_data.x.to_list() and after then this -> x = x_cords[index] # y_cords = state_data.y.to_list() and after then this -> y = y_cords[index]
        t.write(answer_state)
        if len(guessed_states) == 50:
            t.teleport(220, -230)
            t.color("red")
            t.write("Winner", align="center", font=("Times New Roman", 50, "normal"))




turtle.mainloop()
