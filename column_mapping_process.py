import pandas as pd
import os
import json

folder_path = 'Data/cs-train'

column_mapping = {
    'total_price': 'price',
    'TimesViewed': 'times_viewed',
    'StreamID': 'stream_id'
}

def apply_column_mapping(df, column_mapping):
    return df.rename(columns=column_mapping)


def process(folder_path, column_mapping):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                df = pd.json_normalize(data)

            df = apply_column_mapping(df, column_mapping)

            updated_data = df.to_dict(orient='records')
            with open(file_path, 'w') as file:
                json.dump(updated_data, file, indent=4)

            print(f"Updated columns in '{filename}'")


process(folder_path, column_mapping)

print("Column names updated in all JSON files.")
