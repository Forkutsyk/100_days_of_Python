import turtle
import pandas


def creating_interface():
    image = "blank_states_img.gif"
    sc = turtle.Screen()
    sc.title("U.S. States Game")
    sc.addshape(image)
    turtle.shape(image)
    return sc


def guessed_state_positioning(user_choice, state):
    guessed_state = turtle.Turtle()
    guessed_state.hideturtle()
    guessed_state.penup()
    guessed_state.speed('fastest')
    guessed_x = int(user_choice['x'].iloc[0])
    guessed_y = int(user_choice['y'].iloc[0])
    # print(f"x:{guessed_x}")
    # print(f"x:{guessed_y}")
    guessed_state.goto(x=guessed_x, y=guessed_y)
    guessed_state.write(arg=state, align='center', font=('Courier', 8, 'normal'))


def main_logic(sc):

    data = pandas.read_csv('50_states.csv')
    all_states = data.state.to_list()
    wrong_guesses = 0
    guessed_states = []

    while len(guessed_states) != 50:
        user_input = sc.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                  prompt="What's another state's name?")
        try:
            user_input = user_input.title()
        except AttributeError:
            missing_states(guessed_states, all_states)
            return

        # print(user_input)
        if user_input == 'Exit' or wrong_guesses >= 5 or None:
            missing_states(guessed_states, all_states)
            return

        elif user_input not in all_states:
            wrong_guesses += 1
            print(wrong_guesses)

        else:
            if user_input in guessed_states:
                sc.textinput(title="Information", prompt=f"You have already guessed {user_input}")
            else:
                user_guess = data[data['state'] == user_input]
                # print(user_guess)
                guessed_state_positioning(user_guess, user_input)
                guessed_states.append(user_input)


def missing_states(guessed, states):
    state_name = []
    result = []

    for state in states:
        if state not in guessed:
            state_name.append(state)
            result.append("NO")
        else:
            state_name.append(state)
            result.append("YES")

    data_dict = {
        "State": state_name,
        "Guessed?": result
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("result.cvs")


if __name__ == "__main__":

    screen = creating_interface()
    main_logic(screen)
    screen.exitonclick()
