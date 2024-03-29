
import requests

def get_place(query, lat, lon, sort="RELEVANCE", limit=10):
    api_key = "fsq3/qWKdb9qPqlEThP0P7+f2kX52mr7qCPxMoBZAg3Ba/U="
    url = "https://api.foursquare.com/v3/places/search"
    
    ll = f"{lat},{lon}"
    
    params = {
        "query": query,
        "ll": ll,
        "open_now": "true",
        "sort":sort,
        "limit":limit
        }

    headers = {
        "Accept": "application/json",
        "Authorization": api_key
        }
    
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        for i in data['results']:
            fsq_id = i['fsq_id']
            name = i['name']
            address = i['location']['formatted_address']
            print(f"FSQ_ID: {fsq_id}")
            print(f"Place Name: {name}")
            print(f"Place Address {address}")
            print('-'*100)
            print('-'*100)    
            print()
            
