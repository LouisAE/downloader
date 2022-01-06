from dler import addr
from os import system
import random



with open(addr+"test2.txt","r",encoding = "utf-8") as f:
    s = f.readlines()
    random.shuffle(s)
    for each in s:
        print(each)
        system("pause")
