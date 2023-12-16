from fuzzywuzzy import fuzz, process
import pandas as pd
import Levenshtein

df = pd.read_csv("world_bank_preprocessed.csv")

p_names = df["Project Name"].value_counts().keys().to_list()
c_names = df["Country"].value_counts().keys().to_list()

p_name = input("Project Name (Please type in the exact project name) : ")
c_name = input("Country: ")

def validate_and_preprocess(project, country):
    
    matches = [name for name in c_names if country.lower() in name.lower()]

    if ((project in p_names) and (len(matches) != 0)):
        return project, matches[0]
    else:
        return 0, 0
    
project, country = validate_and_preprocess(p_name, c_name)

print((project, country) != (0,0))


