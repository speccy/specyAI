import numpy as np

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

np.random.seed(1)
class net:
	def __init__(self):
		#parameters
		self.inputSize = 9
		self.hiddenSize = 18
		self.outputSize = 9
		self.w1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
		self.w2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

	def forward(self, X):
		#forward propagation through our network
		self.a = np.dot(X, self.w1) # dot product of X (input) and first set of 3x2 weights
		self.b = sigmoid(self.a) # activation function
		self.c = np.dot(self.b, self.w2) # dot product of hidden layer (z2) and second set of 3x1 weights
		i = sigmoid(self.c) # final activation function
		return i
	
nn = net();	

#blackmagicfuckery - converts the list of strings into list of floats fed forward into the neural network
def process(board): 
	board = [b.replace(" ", '0') for b in board]
	board = [b.replace("X", '1') for b in board]
	board = [b.replace("O", '-1') for b in board]
	inp = [float(i) for i in board]
	vals = nn.forward(inp)
	out = vals.argmax() + 1
	return out



print(nn.w2)
