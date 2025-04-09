import pandas as pd
df = pd.read_csv("/Users/connerjamison/Downloads/Most-Recent-Cohorts-Institution 2.csv")

# List the columns you want to keep (adjust these names to match your actual CSV headers)
columns_to_keep = [
    'INSTNM', 'CITY', 'STABBR', 'ZIP',
    'ADM_RATE_ALL', 'ADMCON7', #Indicator for how test scores are considered in admissions
    'SAT_AVG', 'ACTCM25', 'ACTCM75', 'OPENADMP',
    'PCTFLOAN_DCS', #Percentage of students receiving loans
    'PCTPELL_DCS', 'FTFTPCTFLOAN', #Percentage receiving Pell Grants
    'UGDS', 'UGDS_MEN', 'UGDS_WOMEN', 'UG25ABV', #age
    'UGDS_WHITE', 'UGDS_BLACK', 'UGDS_HISP', 'UGDS_ASIAN', 'UGDS_AIAN', 'UGDS_NHPI', 'UGDS_2MOR', 'UGDS_NRA', 'UGDS_UNKN', #Race
    'FIRSTGEN_DEBT_MDN', 'NOTFIRSTGEN_DEBT_MDN', 'PAR_ED_PCT_1STGEN', #First-generation status
    'FAMINC', 'MD_FAMINC', #Family income
    'PCT_BORN_US', #Percentage of students born in the US
    'UNEMP_RATE', #Employment rate
    'COSTT4_A', 'COSTT4_P', #Cost of attendance
]

# Filter the DataFrame
filtered_df = df[columns_to_keep]

numeric_cols = filtered_df.select_dtypes(include='number').columns
df_cleaned = filtered_df[(filtered_df[numeric_cols] != 0).any(axis=1)]

# Save the modified CSV
df_cleaned.to_csv('filtered_dataset.csv', index=False)
