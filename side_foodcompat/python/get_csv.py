import pandas as pd
import os
import time
import sys

# TODO: This script, at least the folder creation part, should be written as a class so variables such as proj_path and date_format can be written as an attribute of the class

proj_path = os.getcwd()
date_format:str

# 1. Read Excel Document
def read_excel(filename):
    df = pd.read_excel(filename, sheet_name='FoodCompatibility', header=0, usecols="A:H", dtype=str)
    return df

# 2. Remove extra rows with N/A
def remove_nan(df):
    drop_item = []
    for x in range(0, len(df.item_zh)):
        if isinstance(df.item_zh[x], float):  # nan is considered as float, so detect for floating instance.
            drop_item.append(x)
    df_update = df.drop(index=drop_item)
    return df_update

# 3a. Get the date and time for folder naming and automatically generated text file.
def get_datetime():
    now = time.localtime()
    today_list = [now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec]
    return today_list

# 3b. Create folder to put all the files in
def create_folder(today_list:list):
    global date_format
    date_format = f"{today_list[0]}-{today_list[1]:02d}-{today_list[2]:02d} @ {today_list[3]:02d}.{today_list[4]:02d}.{today_list[5]:02d}"
    folder_name = f"{proj_path}/data/{date_format}"
    os.mkdir(folder_name)
    print(f"Folder created: \"{date_format}\" (at {proj_path}/data)")
    return folder_name

# 3c. Create text file that tells me when the CSV file was generated
def create_textfile(today_list:list, new_folder:str):
    filepath_today = f"{new_folder}/{date_format}.txt"
    txt_content = f"{today_list[0]}-{today_list[1]:02d}-{today_list[2]:02d} @ {today_list[3]:02d}:{today_list[4]:02d}:{today_list[5]:02d}"
    with open(filepath_today, 'w+') as f:
        f.write(f"CSV file was updated on {txt_content}.\n")
        f.write(f"This text file is automatically generated by Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}.")

# 4. Convert to CSV. This includes checking if the file already exists.
def to_csv(df, csv_filename):
    ans = input("File is about to be converted from XLSX to CSV.\nDo you want to perform this action? (Y/N):\n")
    ans = ans.lower()

    if (ans == 'yes') or (ans == 'y'):
        logic = os.path.isfile(csv_filename)
        if logic:
            print("File exists in the writing directory. Force EOF.")
            print("File path: " + csv_filename)
            exit()
        else:
            pd.DataFrame.to_csv(df, path_or_buf=csv_filename, na_rep='N/A', index=False)
            print("File successfully converted to CSV.\nEOP")
    else:
        print("Force EOP.")
        exit()


if __name__ == '__main__':
    file_path = f"{proj_path}/data/FoodCompatibility.xlsx"
    
    # 1. Read Excel document
    data = read_excel(file_path)
    
    # 2. Remove unnecessary N/A entries
    data_noNan = remove_nan(data)

    # 3. Create new folder to place file into.
    today_list = get_datetime()
    new_folder_name = create_folder(today_list)
    create_textfile(today_list, new_folder_name)

    # 4. Convert data frame to csv
    csv_path = f"{proj_path}/data/{date_format}/FoodCompatibility.csv"
    to_csv(data_noNan, csv_path)
