import pandas as pd
import json
# Define the column mappings to standardize column names
# column_mapping = {
#     'total_price': 'price',
#     'TimesViewed': 'times_viewed',
#     'StreamID': 'stream_id'
# }

def load_data(file_paths):
    data_frames = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                df = pd.json_normalize(data)
                # df.rename(columns=column_mapping, inplace=True)

                if 'invoice' in df.columns:
                    df['invoice'] = df['invoice'].astype(str).str.extract('(\d+)')
                # Replace missing customer IDs with -1
                df = df.fillna({'customer_id': -1})

                data_frames.append(df)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df


def aggregate_by_day(data):
    daily_data = data.groupby(['year', 'month', 'day']).agg({
        'price': 'sum',
        'times_viewed': 'sum',
        'customer_id': 'count'
    }).reset_index()

    return daily_data
