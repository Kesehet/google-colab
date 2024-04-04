import pandas as pd
import math
import os

def split_csv_into_parts(filename, output_folder, num_files=100):
    # Load the CSV file
    df = pd.read_csv(filename)
    
    # Calculate the number of rows per file
    rows_per_file = math.ceil(len(df) / num_files)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Split the dataframe and save each part
    for i in range(num_files):
        start_index = i * rows_per_file
        end_index = start_index + rows_per_file
        df_part = df.iloc[start_index:end_index]
        df_part.to_csv(os.path.join(output_folder, f'part_{i}.csv'), index=False)
    
    print(f'Successfully split the file into {num_files} parts.')


def merge_csv_parts(input_folder, output_filename):
    # List all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Sort files by their part number to maintain the original order
    csv_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    
    # Initialize an empty dataframe
    merged_df = pd.DataFrame()
    
    # Append each file's data to the merged dataframe
    for file in csv_files:
        df_part = pd.read_csv(os.path.join(input_folder, file))
        merged_df = pd.concat([merged_df, df_part], ignore_index=True)
    
    # Save the merged dataframe to a CSV file
    merged_df.to_csv(output_filename, index=False)
    
    print(f'Successfully merged {len(csv_files)} files into {output_filename}.')


#split_csv_into_parts("creditcard.csv","creditcard")
merge_csv_parts("creditcard","creditcard.csv")
