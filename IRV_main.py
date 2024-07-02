from instant_run_off.evaluation import run_instant_runoff

import pandas as pd
import random

# The given list
items = [
    "Aanpassen aan huurprijzen van vergelijkbare voormalige kraakpanden in de omgeving",
    "Terugrekenen vanaf inkomen/ bijstandsniveau (voor student)",
    "CAO loonontwikkeling",
    "Terugrekenen vanaf inkomen/ bijstandsniveau (voor mens in bijstand)",
    "Huurpuntensysteem: Onzelfstandige woonruimte (standaard)",
    "Huurpuntensysteem: Onzelfstandige woonruimte (gereduceerd met 1,3 klusuren à €15,- / h)",
    "Contributie in valuta èn natura als basis",
    "Historische Nieuwelaanprijzen = betaalbaar",
    "Huurpuntensysteem: Zelfstandige woonruimte (Nieuwelaan telt as sociale huurwoning)",
    "Huurpuntensysteem: Zelfstandige woonruimte (standaard)",
    "Huurpuntenontwikkeling",
    "Gelijk risico lening t.o.v. 2006",
    "Sociale en lokale context: Kamers elders (sociale context - andere kamers in woongroepen: woongroep.net)",
    "Sociale en lokale context: Kamers elders (lokale context - andere kamers in Delft: kamernet.nl)",
    "Contributie op basis van inkomen van een 18-jarige"
]

# Generate 40 random orders
random_orders = [random.sample(items, len(items)) for _ in range(41)]

# Create a DataFrame to store the results
orders_data = []

# Populate the list with identifiers and orders
for idx, order in enumerate(random_orders):
    identifier = f"order_{idx + 1:02d}"
    orders_data.append({
        "Identifier": identifier,
        "Order": ";".join(order)  # Join the order list into a single string for Excel
    })

# Create the DataFrame
df_orders = pd.DataFrame(orders_data)

# Save the DataFrame to an Excel file
output_file_path = 'instant_run_off/stemming.xlsx'
df_orders.to_excel(output_file_path, index=False, header=False)


file_path = 'instant_run_off/stemming.xlsx'
store_path = 'instant_run_off/results'
run_instant_runoff(file_path,store_path, consider_invalid=False)