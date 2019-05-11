from numpy import *
from os.path import isfile, join
from os import listdir

def listifier(file_name):
    file = open(file_name, "r")

    lines = file.readlines()
    lines = lines[5:]
    time = zeros(len(lines))
    chanA = zeros(len(lines))
    chanB = zeros(len(lines))
    
    for pos,line in enumerate(lines):
        line_ar = line.split("\t")
        try:
            if len(line_ar) == 3:
                time[pos] = float(line_ar[0].strip())
                chanA[pos] = float(line_ar[1].strip())
                chanB[pos] = float(line_ar[2].strip())
            if len(line_ar) == 2:
                time[pos] = line_ar[0].strip()
                chanA[pos] = line_ar[1].strip()
        except:
            pass
    return {'time':time, 'chanA': chanA, 'chanB':chanB}



def dir_listifier(dir_name,f_count = 32):
    onlyfiles = [f for f in listdir(dir_name) if isfile(join(dir_name, f))]
    all_time = []
    all_chanA = []
    all_chanB = []
    for n,file in enumerate(onlyfiles):
        if n < f_count :
            path = dir_name + "/" + file
            file = open(path, "r")
            lines = file.readlines()
            lines = lines[5:]

            time = zeros(len(lines))
            chanA = zeros(len(lines))
            chanB = zeros(len(lines))
            for pos,line in enumerate(lines):
                line_ar = line.split("\t")
                try:
                    if len(line_ar) == 3:
                        time[pos] = float(line_ar[0].strip())
                        chanA[pos] = float(line_ar[1].strip())
                        chanB[pos] = float(line_ar[2].strip())
                    if len(line_ar) == 2:
                        time[pos] = line_ar[0].strip()
                        chanA[pos] = line_ar[1].strip()
                except:
                    pass
            all_time.extend(time + n*200)

            all_chanA.extend(chanA)
            all_chanB.extend(chanB)
            file.close()
        else:
            break
    return {'time':all_time, 'chanA': all_chanA, 'chanB':all_chanB}