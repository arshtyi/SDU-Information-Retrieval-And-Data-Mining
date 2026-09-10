import numpy as np


def rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b):
    h_current = np.array(initial_hidden_state)
    hidden_states_history = []
    for x_t in input_sequence:
        x_t = np.array(x_t)
        linear_combination = np.dot(Wx, x_t) + np.dot(Wh, h_current) + b
        h_current = np.tanh(linear_combination)
        hidden_states_history.append(h_current)
    return np.round(h_current, 4).tolist()


if __name__ == "__main__":
    input_sequence = eval(input())
    initial_hidden_state = eval(input())
    Wx = eval(input())
    Wh = eval(input())
    b = eval(input())
    print(rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b))
