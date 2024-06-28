from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

CANDIDATES = [f"Candidate {i}" for i in range(1, 11)]
CANDIDATES = pd.read_excel('assets/options.xlsx')['Options']
print(CANDIDATES)

INTRODUCTION = html.P(
        "Welcome to the voting platform. Please read the instructions and proceed to vote on the following questions.")

INTRODUCTION_PEILING = html.Div([
        html.P(" Tijdens de discussie over wat betaalbaarheid voor de Nieuwelaan zou betekenen hebben we ook gepraat "
               "over wat jullie, de oud-leden, betaalbaar of redelijk zouden vinden."),
        html.P("Om op 18 juli een goed geïnformeerde keuze te maken over hoe we betaalbaarheid op de Nieuwelaan kunnen "
               "bepalen, willen we graag jullie mening verzamelen middels een peiling. "
               "Deze peiling heeft als doel de huidige leden meer context te geven over welke methode betrokken "
               "partijen redelijk vinden om de betaalbaarheid voor de NWL te bepalen. Er volgt uit deze peiling geen "
               "verplichting voor de leden om hun mening over de methodes te veranderen."),
        "Er zijn verschillende opties hoe jullie mening meegenomend kan worden:",
        html.Br(),
        "1) Je geeft geranschikt orde van jullie top 5 methodes uit de lijst van 11 methodes + 4 varianten.        EN / OF        "
        "2) Je deelt jouw algemeen mening in een vrije tekst"])



# List of user IDs that are restricted from accessing the /peiling page
RESTRICTED_IDS_PEILING_ONLY = ['user1', 'user2', 'user3']  # example restricted user IDs

RESTRICTED_IDS_STEMMING_ONLY = ['user4', 'user5', 'user6']  # example restricted user IDs