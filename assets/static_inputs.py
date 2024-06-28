from dash import html
import pandas as pd

CANDIDATES = [f"Candidate {i}" for i in range(1, 11)]
CANDIADTES = pd.read_excel('assets/options.xlsx')['Options']

INTRODUCTION = html.P(
        "Welcome to the voting platform. Please read the instructions and proceed to vote on the following questions.")


# List of user IDs that are restricted from accessing the /peiling page
RESTRICTED_IDS_PEILING_ONLY = ['user1', 'user2', 'user3']  # example restricted user IDs

RESTRICTED_IDS_STEMMING_ONLY = ['user4', 'user5', 'user6']  # example restricted user IDs