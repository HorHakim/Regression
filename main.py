import data_preparation


path_to_csv = "../vente_maillots_de_bain.csv"
x_column_name, y_column_name = "Years", "Sales"
percentage_split = 0.8


data_preparation_object = data_preparation.DataPreparation(path_to_csv, x_column_name, y_column_name, percentage_split)
# data_preparation_object.show_dataset()
data_preparation_object.split_data()