# Execution file with parameter

from readCSV import read_main_csv
from createJSON import read_csv
from json2ttl2 import buildGraph
import glob
import os.path
import sys



if len(sys.argv) > 1 and str(sys.argv[1]) == "help":
    exit("Please add one input json file to the command line and the base url_id")

data_csv = sys.argv[1]
read_main_csv(data_csv)
read_csv(data_csv)
# Count the number of json we have in the middle pakete
middle_folder = os.path.join("..", "data", "middle-data")
#print(glob.glob(middle_folder +"/*.json"))

for fjson in glob.glob(middle_folder +"/*.json"):
    buildGraph(fjson)

