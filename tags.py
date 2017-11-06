import re

packages=[]
with open("/home/ubuntu/django_files/travelapp/analysis/views_for_tags.py","r") as f:
    for line in f.readlines():
        if line[:4]=="from": 
            packages.append('.'.join(line.strip().split()[1::2]))
        if line[:6]=="import":
            packages.append(line.strip().split()[1])

print(*sorted(packages),sep="\n")
