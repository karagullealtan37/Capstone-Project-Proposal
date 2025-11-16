import pandas as pd

# 1. Load your raw file (semicolon separator)
df = pd.read_csv("GVKEY US Firms csv.csv", sep=';')

# 2. Keep only the columns you need for the mapping
mapping = df[['gvkey', 'tic', 'cusip', 'sic']].copy()

# 3. Drop rows with missing cusip
mapping = mapping.dropna(subset=['cusip'])

# 4. Normalize CUSIP and create CUSIP6 for CDS matching
mapping['cusip'] = mapping['cusip'].astype(str).str.strip()
mapping['cusip6'] = mapping['cusip'].str[:6]

# 5. One row per gvkey (choose the first CUSIP per firm)
mapping = mapping.drop_duplicates(subset=['gvkey'])

# 6. Save mapping to CSV for CDS extraction
mapping.to_csv("firm_cusip_mapping_for_cds.csv", index=False)


