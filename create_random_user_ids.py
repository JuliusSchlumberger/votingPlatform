import pandas as pd
import random
import string

# Load the Excel file
file_path = 'assets/peiling.xlsx'
df = pd.read_excel(file_path)

# Function to generate a unique identifier
def generate_identifier(row):
    vote = row['Vote']
    group = row['Group']
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{vote}_{group}_{random_part}"

# Create the new column with unique identifiers
df['Identifier'] = df.apply(generate_identifier, axis=1)

# Save the updated DataFrame back to an Excel file
output_file_path = 'assets/peiling_with_identifiers.xlsx'
df.to_excel(output_file_path, index=False)

# import ace_tools as tools; tools.display_dataframe_to_user(name="Updated DataFrame", dataframe=df)
