# Execution file with parameter

from inout.readcsv import read_csv  
from inout.createjson import read_data
from inout.json2ttl3 import buildGraph
import glob
import os.path
import os
import sys
import shutil

# Reading the input data

if len(sys.argv) > 1 and str(sys.argv[1]) == "help":
    exit("Please add one input json file to the command line")

if len(sys.argv) == 0:
    data_folder = os.path.join("..","data")
    data_csv = "steuerdatei.csv"
else:
    head, tail = os.path.split(sys.argv[1])
    data_csv = tail
    data_folder = head

print(data_folder)
# Creating the data file structure 
middle_folder = os.path.join(data_folder, "middle-data")
output_folder = os.path.join(data_folder, "output-data")
original_folder = os.path.join(data_folder, "original-data")
if not os.path.exists(middle_folder):
    shutil.copytree(data_folder, original_folder)
    os.makedirs(middle_folder)
else:
    pattern ="/*.csv"
    files = glob.glob(middle_folder + pattern)
    for f in files:
        filename = os.path.basename(f)
        print(filename)
        #os.remove(os.path.join(data_folder,filename))
        shutil.move(f,os.path.join(data_folder,filename))


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

data_csv = sys.argv[1] 
read_csv(data_folder, middle_folder, data_csv)
read_data(data_folder, middle_folder, data_csv)
for fjson in glob.glob(middle_folder +"/*.json"):
    buildGraph(fjson, output_folder)
