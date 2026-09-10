import numpy as np


class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.hidden_size = hidden_size
        self.W_xh = np.random.randn(hidden_size, input_size) * 0.01
        self.W_hh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.W_hy = np.random.randn(output_size, hidden_size) * 0.01
        self.b_h = np.zeros((hidden_size, 1))
        self.b_y = np.zeros((output_size, 1))

    def forward(self, x):
        sequence_length = x.shape[0]
        self.h = [np.zeros((self.hidden_size, 1))]
        self.outputs = []
        for t in range(sequence_length):
            x_t = x[t].reshape(-1, 1)
            h_t = np.tanh(np.dot(self.W_xh, x_t) + np.dot(self.W_hh, self.h[-1]) + self.b_h)
            y_t = np.dot(self.W_hy, h_t) + self.b_y
            self.h.append(h_t)
            self.outputs.append(y_t)
        return np.array([y.ravel() for y in self.outputs])

    def backward(self, x, y, learning_rate):
        sequence_length = x.shape[0]
        if not hasattr(self, "h") or not hasattr(self, "outputs"):
            self.forward(x)
        dW_xh = np.zeros_like(self.W_xh)
        dW_hh = np.zeros_like(self.W_hh)
        dW_hy = np.zeros_like(self.W_hy)
        db_h = np.zeros_like(self.b_h)
        db_y = np.zeros_like(self.b_y)
        dh_next = np.zeros((self.hidden_size, 1))
        for t in reversed(range(sequence_length)):
            x_t = x[t].reshape(-1, 1)
            target_t = y[t].reshape(-1, 1)
            h_t = self.h[t + 1]
            h_prev = self.h[t]
            y_pred = self.outputs[t]
            dy = y_pred - target_t
            dW_hy += np.dot(dy, h_t.T)
            db_y += dy
            dh = np.dot(self.W_hy.T, dy) + dh_next
            dh_raw = (1 - h_t**2) * dh
            db_h += dh_raw
            dW_xh += np.dot(dh_raw, x_t.T)
            dW_hh += np.dot(dh_raw, h_prev.T)
            dh_next = np.dot(self.W_hh.T, dh_raw)
        self.W_xh -= learning_rate * dW_xh
        self.W_hh -= learning_rate * dW_hh
        self.W_hy -= learning_rate * dW_hy
        self.b_h -= learning_rate * db_h
        self.b_y -= learning_rate * db_y


if __name__ == "__main__":
    np.random.seed(42)
    input_sequence = np.array(eval(input()))
    expected_output = np.array(eval(input()))
    # Initialize RNN
    rnn = SimpleRNN(input_size=input_sequence.shape[1], hidden_size=5, output_size=expected_output.shape[1])

    # Forward pass
    output = rnn.forward(input_sequence)

    # Backward pass
    rnn.backward(input_sequence, expected_output, learning_rate=0.01)

    print(output)
