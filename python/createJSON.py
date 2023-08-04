from rdflib import URIRef
from myclass import Vocab
import sys
import json
import csv
import os.path


def read_csv(input):
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
        my_json = None
        for row in reader:
            my_json, my_vocab = read_header(my_json, row, output_folder)
            add_vocab(my_json, my_vocab, input_folder, output_folder, row)
    create_json(my_json, output_folder)    

def read_header(my_json, row, output_folder):
    file_name = row[0]
    main_title = row[2]
    main_description = row[3]
    vocab_title = row[4]
    vocab_description = row[5]
    if (row[1]==""):
        main_id = ''.join(row[2].split()).lower()
    else:
        main_id = row[1]
    vocab_id =  ''.join(row[4].split()).lower()
    
    if my_json != None:
        if my_json.id != main_id :
            create_json(my_json, output_folder)
            my_json = None

    if my_json == None:
        if main_description=="":
            my_json = Vocab(main_id, main_title, None, None)
        else:
            my_json = Vocab(main_id, main_title, None, main_description)

    if vocab_description=="":
        my_vocab = Vocab(vocab_id, vocab_title, None, None)
    else:
        my_vocab = Vocab(vocab_id, vocab_title, None, vocab_description)
    my_json.add_child(my_vocab)
    return (my_json, my_vocab)


def add_vocab(my_json, my_vocab, input_folder, output_folder, row):
    input_file = os.path.join(input_folder, row[0])


    with open(input_file, mode='r', encoding='utf-8') as fin:
        reader = csv.reader(fin, delimiter=";") 
        next(reader) 
        data_stack = []
        list_data = list(reader)
        parent_vocab = my_vocab
        actual_vocab = my_vocab
        actual_notation_level = 1
        for i in range(len(list_data)):
            notation_level = len(list_data[i][0].split('.'))
            if list_data[i][2]=="":
                vocab = Vocab(list_data[i][3], list_data[i][1], list_data[i][0], None)
            else:
                vocab = Vocab(list_data[i][3], list_data[i][1], list_data[i][0], list_data[i][2])
            if notation_level == actual_notation_level:
                parent_vocab.add_child(vocab)
                actual_vocab = vocab   
            elif notation_level > actual_notation_level:
                actual_notation_level = notation_level
                data_stack.append(parent_vocab)  
                parent_vocab = actual_vocab
                actual_vocab.add_child(vocab)
                actual_vocab = vocab
            else:
                difference = actual_notation_level - notation_level
                actual_notation_level = notation_level
                while (difference>0):
                    parent_vocab = data_stack.pop()
                    difference -= 1
                actual_vocab = vocab
                parent_vocab.add_child(vocab)

   
  
def create_json(my_json, output_folder):
     output_file = os.path.join(output_folder,my_json.id +".json")
     with open(output_file, "w", encoding = 'utf-8') as fout:
        fout.write(json.dumps(my_json.buildJson(), ensure_ascii=False, indent = 4))
