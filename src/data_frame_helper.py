import pandas as pd
from enum import Enum

prompt_dict ={"prompt_0" : "data_csv/prompt_0/data_ppl.csv",
              "prompt_1" : "data_csv/prompt_0/data_ppl.csv",
              "prompt_2" : "data_csv/prompt_0/data_ppl.csv",
              "prompt_3" : "data_csv/prompt_0/data_ppl.csv",
              "prompt_4" : "data_csv/prompt_0/data_ppl.csv"}


def store_data(data, prompt):
    data.to_csv(prompt, index = False)

def get_data(prompt):
    value = prompt_dict[prompt]
    try:
       return pd.read_csv(value)
    except FileNotFoundError:
        if value== prompt_dict["prompt_0"]:
            return section_0_setup()
        elif value== prompt_dict["prompt_1"]:
            return
        elif value== prompt_dict["prompt_2"]:
            return
        elif value == prompt_dict["prompt_3"]:
            return
        elif value == prompt_dict["prompt_4"]:
            return



def section_0_setup():
    columns_section_0 = ["image_id", "number", "female", "male", "age_group_a", "age_group_b", "age_group_c", "json_response"]
    return pd.DataFrame(columns=columns_section_0)


def store_df(data, prompt):
    data.to_csv(prompt_dict[prompt])

