import numpy
class Regression:
	def __init__(self, data_preparation_object, learning_rate, number_of_epochs):
		self.dataset_train_df = data_preparation_object.dataset_train_df
		self.dataset_test_df = data_preparation_object.dataset_test_df

		self.mean_dataset = data_preparation_object.mean_dataset
		self.std_dataset = data_preparation_object.std_dataset

		self.learning_rate = learning_rate
		self.number_of_epochs = number_of_epochs

		self.a = 0
		self.b = 0


	def predict(self, x_value):
		return self.a * x_value + self.b

	def fit(self):
		train_length = len(self.dataset_train_df)
		for epoch in range(self.number_of_epochs):
			self.a -= 2*self.learning_rate/train_length * #
			self.b -= 2*self.learning_rate/train_length * #

	# def mse(self):
	# 	return 

