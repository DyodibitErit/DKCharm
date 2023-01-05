import os
import sys

filename = sys.argv[1]
os.system("chcp 65001>nul")
os.system("if exist " + filename + " (type " + filename + ")")

while True:
    text = input("~ ")
    if(text=='qwasd'):
        os.system("start dyokey " + filename)
    elif(text=='clearAll'):
        os.system("del " + filename)
    else:
        os.system("echo " + text + ">>" + filename)