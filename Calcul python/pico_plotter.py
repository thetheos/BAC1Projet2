from numpy import *

def listifier(file_name):
    file = open(file_name, "r")

    lines = file.readlines()
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
    return time,chanA,chanB