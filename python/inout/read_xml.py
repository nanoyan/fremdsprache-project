import csv
import os.path
import uuid
import sys
import shutil


def read_xml():
    input_file = os.path.join("..", "..", "Alte Item-DatenBank", "DBPProps.csv")
    output_folder = os.path.join("..", "..", "Alte Item-DatenBank")
    output_file = os.path.join("..", "..", "Alte Item-DatenBank", "outputDBPProps.csv")
     
    with open(input_file, mode='r', encoding='utf-8') as fin, \
         open(output_file, mode ='w', newline='', encoding='utf-8') as fout:
        reader = csv.reader(fin, delimiter=";")

        writer = csv.writer(fout, delimiter=";")
        writer.writerow(['dateiname','url_id','main-title','main-description','title','description'])
        next(reader)
        old_file_name = ''
        n_count = 1
        #Create the steuerdatei.csv
        for row in reader:
            if (row[1] != old_file_name):
                if (old_file_name != '' ):    
                    writer.writerow([old_file_name.replace('/','').replace(':','')+'.csv', 'IQB-ItemDBPProps','IQB Item and Properties Database', old_file_name, row[8], n_count])
                old_file_name = row[1]
                n_count = 1
            else:
                n_count += 1
        writer.writerow([row[1]+'.csv', 'IQB-ItemDBPProps','IQB Item and Properties Database', row[1], row[8], n_count])         
    
    with open(input_file, mode='r', encoding='utf-8') as fin, \
         open(output_file, mode ='r', newline='', encoding='utf-8') as fin2:
        reader = csv.reader(fin, delimiter=";")
        next(reader)
        reader2 = csv.reader(fin2, delimiter=";")
        next(reader2)

        for row2 in reader2:
            counter = int(row2[5]) 
            if (counter > 1):
                filename = os.path.join(output_folder, row2[0])
                with open(filename, mode = 'w', newline='', encoding='utf-8') as fout:
                    writer = csv.writer(fout, delimiter = ";" )
                    writer.writerow(['notation','title','description'])
                    inc_counter = 1
                    while (counter>0):
                        line = next(reader)
                        writer.writerow([inc_counter, line[13],''])
                        counter -= 1
                        inc_counter +=1
            else:
                next(reader)
                               
