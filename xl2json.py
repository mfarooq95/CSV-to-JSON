import pandas as pd
import json

json_output = {
    "class": "lookup_charge",
    "entries": []
}

df = pd.read_csv("C:\\Users\\Ibe\\Desktop\\Charges\\Final.csv")
for index, row in df.iterrows():
    category_ids = [
        3298139, #Assault Offenese
        3298140, #Drug Offense
        3298141, #Other
        3294743, #Property Crime
        3294741  #Sex Offense
    ]

    charge_name = row['Description']
    active = True
    statute_number = f"Title {row['Title']} Section {row['Section']}"
    state = "PA"
    charge_category_name = row['Category']

    if charge_category_name == "Assault Offense":
        charge_category_id = 3298139
    elif charge_category_name == "Drug Offense":
        charge_category_id = 3298140
    elif charge_category_name == "Other":
        charge_category_id = 3298141
    elif charge_category_name == "Property Crime":
        charge_category_id = 3294743
    elif charge_category_name == "Sex Offense":
        charge_category_id = 3294741
    else:
        charge_category_id == -1

    json_output["entries"].append(
        {
            "name": charge_name,
            "active": active,
            "statute_number": statute_number,
            "state": state,
            "charge_category_id": {
                "id": charge_category_id,
                "name": charge_category_name,
                "note": ""
            }
        }
    )

    if index == 4:
        with open("C:\\Users\\USER\\Desktop\\Charges\\firstfive2.json", 'w') as f:
            json.dump(json_output, f)

with open("C:\\Users\\USER\\Desktop\\Charges\\output2.json", 'w') as f:
    json.dump(json_output, f)
