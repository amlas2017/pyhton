import csv
#import pandas
url = "C:\\Users\\Fitec\\PycharmProjects\\Dossier3\\exemple.csv"

linecount = len(open(url, 'r').readlines())

print("le fichier a %d lignes" % linecount)

#print(I)