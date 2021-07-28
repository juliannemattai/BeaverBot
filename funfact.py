import csv
import random

csv_name = "funfacts.csv"

def get_fun_fact(subject): 
    keyword = subject.lower()
    skule_dict = build_dictionary()
    keys = list(skule_dict.keys())

    if keyword in keys:
        facts = (skule_dict[keyword]['facts'])
        fact = random.choice(facts)	
        return fact

    else:
        return ("sorry i'm not smart enough yet. check out skulepedia.ca to find what you're looking for")

    #select a fact from the options, create dictionary and randomly pick one
    #offer skulepedia page for more info

def build_dictionary():

    skule_dict = {}
    with open(csv_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    
        for row in csv_reader:
            if "keyword" in row[0]:
                continue
            if(row[0] in skule_dict):
                skule_dict[row[0]]['facts'].append(row[1])
            else:
                skule_dict[row[0]]= {'facts' : [row[1]], 'skulepedia':row[2]}

    #print(skule_dict)

    #print(csv_reader)
    return skule_dict

