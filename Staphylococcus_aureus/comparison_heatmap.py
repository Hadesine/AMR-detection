import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your combined table
df = pd.read_csv("AMR_Comparative_Table.csv")

# Create a presence/absence table (pivot)
heatmap_data = df.pivot_table(index='Gene', columns='Tool', aggfunc='size', fill_value=0)

# Optional: Sort genes by presence in tools
heatmap_data = heatmap_data.sort_values(by=list(heatmap_data.columns), ascending=False)

# Plotting the heatmap
plt.figure(figsize=(10, len(heatmap_data) * 0.4))  # Dynamic height
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", cbar=False, linewidths=.5, linecolor='gray')

plt.title("AMR Gene Detection by Tool")
plt.xlabel("Tool")
plt.ylabel("Gene")
plt.tight_layout()
plt.savefig("AMR_Tool_Comparison_Heatmap.png")
print('heatmap succesfully created')
plt.show()
