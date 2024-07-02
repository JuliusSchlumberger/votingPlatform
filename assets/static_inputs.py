from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

CANDIDATES = [f"Candidate {i}" for i in range(1, 11)]
CANDIDATES = pd.read_excel('assets/options.xlsx')['Options']
CANDIDATES_Keys = pd.read_excel('assets/options.xlsx')['Key'].astype(str)
print(pd.read_excel('assets/options.xlsx'))
COLORS = pd.read_excel('assets/options.xlsx')['Colors3']
Colors_to_Candidates = {CANDIDATES[i]: COLORS[i] for i in range(len(CANDIDATES))}

Keys_to_Candidates = {CANDIDATES[i]: CANDIDATES_Keys[i] for i in range(len(CANDIDATES))}

INTRODUCTION = html.P(
        "Welkom op het stemplatform. Zoals besloten in de ALV van 26 juni gebruiken we het Instant-Runoff-Model om "
        " te bepalen welke methode de meeste voorkeur heeft om de betaalbaarheid aan de Nieuwelaan te bepalen. Jullie hebben allemaal de tijd gehad om "
        "naar het rapport met daarin de beschrijving van de methoden, de feedback van de gemeenschap van vandaag, de peiling "
        "met oud-leden en aspirant-leden, het perspectief vanuit de Commissie van Toezicht en de evaluatie door STUT."
        " Vul je stem in en verstuur. Mocht je een fout hebben gemaakt, dan kun je gewoon opnieuw insturen.")

INTRODUCTION_PEILING = html.Div([
        html.P(" Tijdens de discussie over wat betaalbaarheid voor de Nieuwelaan zou betekenen hebben we ook gepraat "
               "over wat jullie, de oud-leden, betaalbaar of redelijk zouden vinden."),
        html.P("Om op 18 juli een goed geïnformeerde keuze te maken over hoe we betaalbaarheid op de Nieuwelaan kunnen "
               "bepalen, willen we graag jullie mening verzamelen middels een peiling. "
               "Deze peiling heeft als doel de huidige leden meer context te geven over welke methode betrokken "
               "partijen redelijk vinden om de betaalbaarheid voor de NWL te bepalen. Er volgt uit deze peiling geen "
               "verplichting voor de leden om hun mening over de methodes te veranderen."),
        html.P("Er zijn verschillende opties hoe jullie mening meegenomen kan worden:"),
    html.Ul([
        html.Li("je geeft geranschikt orde van jullie top 5 methodes uit de lijst van mogelijkheden."),
            html.B("en/of"),
        html.Li("je deelt jouw algemeen mening in een vrije tekst.")])])



# List of user IDs that are restricted from accessing the /peiling page
# RESTRICTED_IDS_PEILING_ONLY = ['user1', 'user2', 'user3']  # example restricted user IDs
# RESTRICTED_IDS_STEMMING_ONLY = ['user4', 'user5', 'user6']  # example restricted user IDs

excel_with_ids = pd.read_excel('assets/peiling_with_identifiers.xlsx')
RESTRICTED_IDS_PEILING_ONLY = excel_with_ids[excel_with_ids.Vote == 'P'].copy()['Identifier'].values
# print(RESTRICTED_IDS_PEILING_ONLY)
RESTRICTED_IDS_STEMMING_ONLY = excel_with_ids[excel_with_ids.Vote == 'S'].copy()['Identifier'].values

