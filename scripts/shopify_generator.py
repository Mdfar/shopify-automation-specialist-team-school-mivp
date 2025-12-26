import requests import json

SHOPIFY_STORE = "https://www.google.com/search?q=varsity-customs.myshopify.com" ACCESS_TOKEN = "shpat_xxxxxxxxxxxxxxxxxxxx"

def create_team_collection(team_name, access_code): """Creates a smart collection for a specific team.""" url = f"https://{SHOPIFY_STORE}/admin/api/2024-01/smart_collections.json"

payload = {
    "smart_collection": {
        "title": f"Store: {team_name}",
        "rules": [
            {
                "column": "tag",
                "relation": "equals",
                "condition": access_code
            }
        ],
        "published": False
    }
}

headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
return response.json()

Example usage
create_team_collection("Springfield High Tigers", "TIGERS2025")