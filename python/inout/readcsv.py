import csv
import os.path
import uuid
import sys
import shutil


def read_csv(input_folder, middle_folder, input):
    input_file =  os.path.join(input_folder, input)
     
    with open(input_file, mode='r', encoding='utf-8') as fin:
        reader = csv.reader(fin, delimiter=";")
        col_names = next(reader) 
        for row in reader:
            add_w3id_csv(input_folder,middle_folder,row)
    

def add_w3id_csv(input_folder,middle_folder,row):
    file_name = row[0]
    main_title = row[2]
    title = row[3]
    description = row[4] 

    if (row[1]==""):
        url_id = ''.join(row[2].split()).lower()
    else:
        url_id = row[1]
    url_id2 =  ''.join(row[3].split()).lower()

    input_file = os.path.join(input_folder, file_name)
    middle_file = os.path.join(middle_folder, file_name)
    counter = 1

    with open(input_file, mode='r', encoding='utf-8') as fin, \
         open(middle_file, mode ='w', newline='', encoding='utf-8') as fout:
        reader = csv.reader(fin, delimiter=";")
        writer = csv.writer(fout, delimiter=";")
        col_names = next(reader)
        writer.writerow(col_names)
        for row in reader:
            if (len(row)==2):
                row.append('')
            if (len(row)==3):
                counter +=1 
                padded_num ="".join(["0"] * (3 - len(str(counter)))) + str(counter)
                row.append(padded_num)
            writer.writerow(row)
