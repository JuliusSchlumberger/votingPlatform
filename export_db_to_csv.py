import os
import pandas as pd
from sqlalchemy import create_engine
import requests
import base64

# Fetch the database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Adjust the URL format if necessary
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)

# Query the database
query = "SELECT * FROM survey_responses"
df = pd.read_sql_query(query, engine)

# Export to CSV
csv_content = df.to_csv(index=False)

# GitHub upload details
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = os.getenv('GITHUB_REPO')
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO}/contents/survey_responses.csv'
message = "Add survey responses CSV"

# Encode CSV content to base64
encoded_content = base64.b64encode(csv_content.encode()).decode()

# Prepare the request payload
payload = {
    "message": message,
    "content": encoded_content
}

# Make the request to GitHub API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Check if the file already exists
response = requests.get(GITHUB_API_URL, headers=headers)
if response.status_code == 200:
    # File exists, get the SHA and include it in the payload
    sha = response.json()['sha']
    payload['sha'] = sha

# Make the request to create or update the file on GitHub
response = requests.put(GITHUB_API_URL, json=payload, headers=headers)

if response.status_code in [200, 201]:
    print("Data exported to survey_responses.csv and uploaded to GitHub")
else:
    print("Failed to upload to GitHub", response.json())
