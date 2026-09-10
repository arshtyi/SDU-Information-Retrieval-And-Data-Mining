import numpy as np
import copy
import math

# DO NOT CHANGE SEED
np.random.seed(42)


# DO NOT CHANGE LAYER CLASS
class Layer(object):
    def set_input_shape(self, shape):

        self.input_shape = shape

    def layer_name(self):
        return self.__class__.__name__

    def parameters(self):
        return 0

    def forward_pass(self, X, training):
        raise NotImplementedError()

    def backward_pass(self, accum_grad):
        raise NotImplementedError()

    def output_shape(self):
        raise NotImplementedError()


# Your task is to implement the Dense class based on the above structure
class Dense(Layer):
    def __init__(self, n_units, input_shape=None):
        self.layer_input = None
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
        self.W = None
        self.w0 = None

    def initialize(self, optimizer):
        limit = 1 / math.sqrt(self.input_shape[0])
        self.W = np.random.uniform(-limit, limit, (self.input_shape[0], self.n_units))
        self.w0 = np.zeros((1, self.n_units))
        self.W_opt = copy.copy(optimizer)
        self.w0_opt = copy.copy(optimizer)

    def forward_pass(self, X, training=True):
        self.layer_input = X
        return np.dot(X, self.W) + self.w0

    def backward_pass(self, accum_grad):
        W = self.W.copy()
        if self.trainable:
            grad_w = self.layer_input.T.dot(accum_grad)
            grad_w0 = np.sum(accum_grad, axis=0, keepdims=True)
            self.W = self.W_opt.update(self.W, grad_w)
            self.w0 = self.w0_opt.update(self.w0, grad_w0)
        accum_grad = accum_grad.dot(W.T)
        return accum_grad

    def number_of_parameters(self):
        return np.prod(self.W.shape) + np.prod(self.w0.shape)

    def parameters(self):
        return self.number_of_parameters()

    def output_shape(self):
        return (self.n_units,)


if __name__ == "__main__":
    # Initialize a Dense layer with 3 neurons and input shape (2,)
    dense_layer = Dense(n_units=3, input_shape=(2,))

    # Define a mock optimizer with a simple update rule
    class MockOptimizer:
        def update(self, weights, grad):
            return weights - 0.01 * grad

    optimizer = MockOptimizer()

    # Initialize the Dense layer with the mock optimizer
    dense_layer.initialize(optimizer)

    # Perform a forward pass with sample input data
    X = np.array(eval(input()))
    output = dense_layer.forward_pass(X)
    print("Forward pass output:", output)

    accum_grad = np.array([[0.1, 0.2, 0.3]])
    back_output = dense_layer.backward_pass(accum_grad)
    print("Backward pass output:", back_output)
