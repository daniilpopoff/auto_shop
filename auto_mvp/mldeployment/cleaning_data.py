import pandas as pd
import os
file_path = 'columns_f.txt'
model_columns = []
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
            stiped_lines = [line.strip() for line in file]
            model_columns.append(stiped_lines)
    print("t")
print(stiped_lines)
print("Current Working Directory:", os.getcwd())

