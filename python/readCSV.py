import csv
import os.path
import uuid
import sys
import shutil


def read_main_csv(input):
    #Steuerdatei lesen
    #if len(sys.argv) > 1 and str(sys.argv[1]) == "help":
    #    exit("Please add main input csv file to the command line")

    input_folder = os.path.join("..", "data", "input-data")
    #input_file =  os.path.join(input_folder, sys.argv[1])
    input_file =  os.path.join(input_folder, input)
    output_folder = os.path.join("..", "data", "middle-data")
     
    with open(input_file, mode='r', encoding='utf-8') as fin:
        reader = csv.reader(fin, delimiter=";")
        col_names = next(reader) 
        for row in reader:
            add_w3id_csv(input_folder,output_folder,row)
    

def add_w3id_csv(input_folder,output_folder, row):
    file_name = row[0]
    main_title = row[2]
    main_description = row[3]
    title = row[4]
    description = row[5] 

    if (row[1]==""):
        url_id = ''.join(row[2].split()).lower()
    else:
        url_id = row[1]
    url_id2 =  ''.join(row[4].split()).lower()

    input_file = os.path.join(input_folder, file_name)
    output_file = os.path.join(output_folder, file_name)

    with open(input_file, mode='r', encoding='utf-8') as fin, \
         open(output_file, mode ='w', newline='', encoding='utf-8') as fout:
        reader = csv.reader(fin, delimiter=";")
        writer = csv.writer(fout, delimiter=";")
        col_names = next(reader)
        writer.writerow(col_names)
        for row in reader:
            if (len(row)==2):
                row.append('')
            if (len(row)==3):
                row.append(str(uuid.uuid4()))
            writer.writerow(row)
    shutil.copyfile(output_file, input_file)
    
