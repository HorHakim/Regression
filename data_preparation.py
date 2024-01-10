import pandas
import matplotlib.pyplot as plt 

class DataPreparation:
	def __init__(self, path_to_csv, x_column_name, y_column_name):
		self.dataset_df = pandas.read_csv(path_to_csv)
		self.x_column_name = x_column_name
		self.y_column_name = y_column_name
		self.dataset_df[x_column_name] = pandas.to_datetime(self.dataset_df[x_column_name])

	def prepare_data(self):
		self.standard_normalize_data()
		self.split_data()

	def standard_normalize_data(self):
		pass

	def split_data(self):
		pass

	def show_dataset(self):
		plt.figure(figsize=(15, 6))
		plt.plot(self.dataset_df[self.x_column_name], self.dataset_df[self.y_column_name])
		plt.show()