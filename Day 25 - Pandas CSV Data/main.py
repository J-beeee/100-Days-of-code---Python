from turtle import Screen
from map_label import Label
import pandas

#SCREEN CONTROL
s= Screen()
s.title("Bundesländer raten")
s.setup(650,850)
s.bgpic(picname="deutschland.png", )

#DATA CONTROL
data = pandas.read_csv("bundeslaender.csv")

#MAP_LABEL CONTROL
map_label = Label()

right_guesses = []
while len(right_guesses) < len(data):

    answer_state = s.textinput(title=f"Guess the State - {len(right_guesses)}/{len(data)}", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = {"states": [line for line in data["state"] if line not in right_guesses]}
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in data.iloc[:,0].values:
        if answer_state in right_guesses:
            print("Already guessed")
        else:
            right_guesses.append(answer_state)
            answer_state = data.loc[data[data.state == answer_state].index[0]]
            map_label.add_label(state_name=answer_state["state"], x_cord=answer_state["x"], y_cord=answer_state["y"])



