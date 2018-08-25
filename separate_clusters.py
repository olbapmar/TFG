import sys
import os
import shutil

archivo = sys.argv[1]

archivo = open(archivo, "r")

if not os.path.exists("clusters"):
    os.mkdir("clusters")

os.chdir("clusters")

if not os.path.exists(sys.argv[1].split('.')[0]):
    os.mkdir(sys.argv[1].split('.')[0])
os.chdir(sys.argv[1].split('.')[0])

for line in archivo:
    filter_name = line.split(':')[0]
    cluster_number = (line.split(" ")[-1])[:-1]
    if not os.path.exists(cluster_number):
        os.mkdir(cluster_number)
    name_tokens = filter_name[2:].split("_")
    shutil.copyfile("../../features/"+name_tokens[0]+"_"+name_tokens[1]+"/"+name_tokens[2]+".png", cluster_number+"/"+filter_name[2:]+".png")

