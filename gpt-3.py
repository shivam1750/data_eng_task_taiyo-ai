import pandas as pd
import json

data = pd.read_csv("world_bank_preprocessed.csv")

def generate_completion(row):    
    summary = f"The project '{row['Project Name']}' is a {row['Project Development Objective ']} project in {row['Country']}. It was approved by the World Bank on {row['Board Approval Date']} and was closed on {row['Project Closing Date']}. The total cost of the project was {row['Current Project Cost']} USD, with an IBRD commitment of {row['IBRD Commitment ']} USD and an IDA commitment of {row['IDA Commitment']} USD."
    
    return summary

pairs = []

for index, row in data.iterrows():
    prompt = f"What is the summary of the '{row['Project Name']}' in {row['Country']}?"
    completion = generate_completion(row)
    pair = {"prompt": prompt, "completion": completion}
    pairs.append(pair)

with open("prompt_completion_pairs.json", "w") as outfile:
    json.dump(pairs, outfile)

