import pandas as pd
import os


def read_csv(csv_path):
    #read csv file with pandas
    df = pd.read_csv(csv_path)
    return df

DATASET="StudentEval"

SCRIPT = "q"+str(3)
CODE_DIR = os.path.join(
                  os.getcwd(),
                DATASET,
                "Reference_Scripts", "Repair_st", SCRIPT,
                "",
            )


repair_dt = read_csv(os.path.join(CODE_DIR,  "refactory_online_st.csv"))


for i, row in repair_dt.iterrows():
    file_name = "repair_"+repair_dt['File Name'][i]
    repair_content = repair_dt['Repair'][i]
    output_path = os.path.join(CODE_DIR, file_name)

    if isinstance(repair_content, str):
        with open(output_path, "w") as output:
            output.write(repair_content)
        output.close()
        print(file_name)
    else:
        print("no repair for "+file_name)



