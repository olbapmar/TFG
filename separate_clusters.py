import sys
import os

if not os.path.exists("clusters"):
    os.mkdir("clusters")

os.chdir("clusters")

if not os.path.exists(sys.argv[1].split('.')[0]):
    os.mkdir(sys.argv[1].split('.')[0])
os.chdir(sys.argv[1].split('.')[0])

archivo = sys.argv[1]

archivo = open(archivo, "r")

for line in archivo:
    filter_name = line.split(':')[0]
    cluster_number = line.split(" ")[-1]
    if not os.path.exists(cluster_number):
        os.mkdir(cluster_number)

