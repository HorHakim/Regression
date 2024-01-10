import data_preparation


path_to_csv = "../vente_maillots_de_bain.csv"
x_column_name, y_column_name = "Years", "Sales"


data_preparation_object = data_preparation.DataPreparation(path_to_csv, x_column_name, y_column_name)
data_preparation_object.show_dataset()