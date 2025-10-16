import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.category import UnitData

# 2.1 Read CSV file into pandas DataFrame

# Define the path to the CSV file
csv_file = "CNV_log2_skin_melanoma.csv"

# Function to read CSV file into DataFrame using pandas
df = pd.read_csv(csv_file)

# Read the CSV file and print the first few rows
print(df.head())


def orderChromosomes():
    """
Map chromosomes in the correct order and return as UnitData object.
"""
    ChromLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X']
    return UnitData(ChromLabels)

chr_ordered = orderChromosomes()

# 2.2 Plot chromosome vs cnv_log2 using matplotlib
# Ensure chromosomes are treated as categorical data with the correct order
plt.scatter(df['chromosome'], df['cnv_log2'], xunits=chr_ordered)
plt.xlabel("Chromosome")
plt.ylabel("Log2 number variation")
plt.title("Chromosome vs Log2 number variation")
plt.show()
plt.savefig("chromosome_vs_log2_variation.pdf")
