import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load RGI output file (edit this to your file's name)
df = pd.read_csv("Ecoli_annotation.faa.txt", sep="\t")

# Drop rows with NaN in Drug Class, if any
df = df.dropna(subset=['Drug Class'])

# Split multiple drug classes and explode into separate rows
df['Drug Class'] = df['Drug Class'].str.split('; ')
df = df.explode('Drug Class')

# Filter and count drug classes
drug_class_counts = df['Drug Class'].value_counts()
print(drug_class_counts)

# Create the barplot
plt.figure(figsize=(18, 12))
barplot = sns.barplot(x=drug_class_counts.values, y=drug_class_counts.index, hue=drug_class_counts.index, palette="deep6")
plt.title("Detected AMR Genes in E. coli by Drug Class (RGI-CARD)", fontsize=16)
plt.xlabel("Number of Genes Detected", fontsize=12)
plt.ylabel("Drug Class", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=8)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout(pad=3)

# Add count labels on top of each bar
#for patch in barplot.patches:
#    width = patch.get_width()
#   y = patch.get_y() + patch.get_height() / 2
#    barplot.text(width + 0.1, y, int(width), va='center', ha='left', fontsize=8, color='brown')

# Save the plot
plt.savefig("AMR_Genes_Ecoli_By_Drug_Class.png", dpi=300)
print ('plot created succesfully')

# Show the plot (optional)
plt.show()
