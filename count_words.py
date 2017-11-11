# By: Lev Epshtein
# Programm take txt file as argument count number of occurences and print histobar with number

import sys

file_name = sys.argv[1]
alpha_statistic = {}

def print_dictionary(dic, file_name):
    print("Word\tNumber of occurrences in {0}",file_name)
    for key in dic.keys():
        delimeter = dic[key] * "-"
        print("{0}{2}{1}".format(key, dic[key], delimeter))


with open(file_name,'r') as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            if word.rstrip() in alpha_statistic.keys():
                alpha_statistic[word]+=1
            else:
                alpha_statistic[word]=1

print_dictionary(alpha_statistic, file_name)