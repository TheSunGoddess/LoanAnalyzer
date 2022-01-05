import csv
from pathlib import Path

csvpath = Path("/Users/MrsGlover/Desktop/FinTech-Workspace/02_Pathways_to_Success_Part_1/Solved/quarterly_data.csv")
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)


