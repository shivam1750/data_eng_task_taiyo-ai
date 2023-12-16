from credentials import API_KEY
import openai, pandas as pd


openai.api_key = API_KEY
model_id = "ft-CTyrZcYHx15C0kddVRUojf2d"


df = pd.read_csv("world_bank_preprocessed.csv")
p_names = df["Project Name"].value_counts().keys().to_list()
c_names = df["Country"].value_counts().keys().to_list()

def validate_and_preprocess(project, country):
    
    matches = [name for name in c_names if country.lower() in name.lower()]

    if ((project in p_names) and (len(matches) != 0)):
        return project, matches[0]
    else:
        return 0, 0

while 1:    

    print("What Project would you like to know about?\n")

    p_name = input("Project Name (Please type in the exact project name) : ")
    c_name = input("Country: ")

    project, country = validate_and_preprocess(p_name, c_name)

    if ((project, country) != (0,0)):

        prompt = f"What is the summary of the {project} in {country}?"

        response = openai.Completion.create(
            engine=model_id,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        print(response.choices[0].text)
        
    else:
        print("Data does not exist!")


# openai api fine_tunes.follow -i ft-CTyrZcYHx15C0kddVRUojf2d
