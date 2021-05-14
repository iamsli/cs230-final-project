import re
import os
import fnmatch 

def preprocess_file(readfile, writefile):
    write_file = open(writefile, 'a')
    
    read_file = open(readfile, 'r')
    Lines = read_file.readlines()
    
    # Strips the newline character
    for line in Lines:
        line = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", line)
        write_file.write(line)
    read_file.close()
    write_file.close()
        
        
def preprocess():
    d = './tasks_1-20_v1-2/en-valid-10k/'
    directory = os.fsencode(d)
    write_train = 'en-valid-all-train.txt'
    write_test = 'en-valid-all-test.txt'
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if fnmatch.fnmatch(filename, '*_train.txt'): 
            preprocess_file(d+filename, write_train)
        else:
            preprocess_file(d+filename, write_test)
            
preprocess()