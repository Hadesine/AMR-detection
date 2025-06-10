import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the full paths to each file
rgi_path = os.path.join(r"C:\Users\*****\AMR project\Report and Results\E_coli_1\RGI", 'Ecoli_annotation.faa.txt')
amr_path = os.path.join(r"C:\Users\*****\AMR project\Report and Results\E_coli_1\AMRFinderPlus", 'amrfinder_ecoli.tsv')
resfinder_path = os.path.join(r"C:\Users\*****\AMR project\Report and Results\E_coli_1\Resfinder", 'Resfinder Ecoli 1.txt')

# Load each file
rgi = pd.read_csv(rgi_path, sep='\t')
amr = pd.read_csv(amr_path, sep='\t')
resfinder = pd.read_csv(resfinder_path, sep=r'\s{2,}|\t', engine='python', comment='#') # Add a column to identify source tool

rgi['Tool'] = 'RGI'
amr['Tool'] = 'AMRFinderPlus'
resfinder['Tool'] = 'ResFinder'

# Filter ResFinder to keep only rows with Resistant phenotype
resfinder = resfinder[resfinder['WGS-predicted phenotype'].str.contains('Resistant', case=False)]

rgi['Drug Class'] = rgi['Drug Class']
resfinder['Drug Class'] = resfinder ['Antimicrobial']
amr['Drug Class'] = amr ['Class']

# Combine all data into one DataFrame
df = pd.concat([rgi, amr, resfinder])

# Split multiple drug classes and explode into separate rows
df['Drug Class'] = df['Drug Class'].str.split('; ')
df = df.explode('Drug Class')

# Group by Tool and Drug Class to count genes
summary = df.groupby(['Tool', 'Drug Class']).size().unstack(fill_value=0)

# Plot stacked bar chart
summary.plot(kind='bar', stacked=True, figsize=(16, 10), colormap='tab20')
plt.ylabel('Number of Genes')
plt.title('E. coli AMR genes identified across Drug Classes by different tools')
plt.xticks(rotation=0)
plt.legend(title='Drug Class', bbox_to_anchor=(1.08, 1), loc='upper left', fontsize=8, ncol=1) #ncol - no. of columns 
#plt.tight_layout()

plt.savefig('Tool comparison for gene detection', dpi=300)
print('plot created succesfully')

plt.show()
