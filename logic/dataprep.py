# file to clean the raw csv files into something more useful
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent# points to our quantium folder, allows us to be OS independant

# load the files so that we can merge them

file1 = pd.read_csv(BASE_DIR / "data" / "daily_sales_data_0.csv")
file2 = pd.read_csv(BASE_DIR / "data" / "daily_sales_data_1.csv")
file3 = pd.read_csv(BASE_DIR / "data" / "daily_sales_data_2.csv")

combinedFile = pd.concat([file1, file2, file3], ignore_index=True)

# remove files which is not pink morsel
combinedFile = combinedFile[combinedFile["product"] == "pink morsel"]
# remove the '$' for calculation
combinedFile["price"] = combinedFile["price"].str.replace("$", "", regex=False).astype(float)
# convert into a number
combinedFile["quantity"] = pd.to_numeric(combinedFile["quantity"])
# create sales column
combinedFile["sales"] = combinedFile["price"] * combinedFile["quantity"]
combinedFile = combinedFile[["sales", "date", "region"]]# we want to reorder the columns into slaes, date and region + drop others
combinedFile.to_csv(BASE_DIR/"data"/"cleaned_data.csv", index=False)
print(combinedFile)
