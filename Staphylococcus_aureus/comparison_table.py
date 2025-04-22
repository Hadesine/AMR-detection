import pandas as pd

# Load AMRFinderPlus output
amr = pd.read_csv("AMRFinderplus/amrfinder_newoutput.tsv", sep="\t")
print(amr.columns)

# Clean and format
amr = amr[[
    'Element symbol', 'Class', 'Subclass', 'Method',
    '% Identity to reference', '% Coverage of reference'
]]
amr.columns = ['Gene', 'Drug Class', 'Subclass', 'Method', '% Identity', '% Coverage']
amr['Tool'] = 'AMRFinderPlus'

# Load RGI output (adjust path if needed)
rgi = pd.read_csv("RGI/Saureus_annotation_rgi_output.txt", sep='\t')

# Extract and rename key columns
rgi = rgi[[
    'Best_Hit_ARO', 'Drug Class', 'Resistance Mechanism', 'Model_type',
    'Best_Identities', 'Percentage Length of Reference Sequence'
]]
rgi.columns = ['Gene', 'Drug Class', 'Resistance Mechanism', 'Method', '% Identity', '% Coverage']
rgi['Tool'] = 'RGI'

# Add empty 'Resistance Mechanism' column to AMRFinderPlus for alignment
amr['Resistance Mechanism'] = None
rgi['Subclass'] = None

# Ensure column order matches
amr = amr[['Gene', 'Tool', 'Drug Class', 'Subclass', 'Method', '% Identity', '% Coverage', 'Resistance Mechanism']]
rgi = rgi[['Gene', 'Tool', 'Drug Class', 'Subclass', 'Method', '% Identity', '% Coverage', 'Resistance Mechanism']]

# Combine
combined = pd.concat([amr, rgi], ignore_index=True)

# Optional: Sort by gene or tool
combined_sorted = combined.sort_values(by=['Gene', 'Tool'])

# Save to CSV and display
combined_sorted.to_csv("AMR_Comparative_Table.csv", index=False)
print('Table created successfully')
combined_sorted.head()
